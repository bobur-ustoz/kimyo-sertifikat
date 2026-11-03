import { createClient } from "@supabase/supabase-js";
import { selectDaily } from "./_oyin/select.js";
import { publicQuestion, check } from "./_oyin/view.js";
import { drawTeams, pickTeamForLate, lateAllowed, TEAM_NAMES } from "./_oyin/teams.js";
import { scoreAnswer, canStake, dailyBonus, applyRank, POINTS, timeLimit, isLate } from "./_oyin/score.js";

// Organika game API. One function (Vercel Hobby allows 12), the action is in the body:
//   state                       -> season, today's day number, the student's totals, the list of days
//   today   { day? }            -> today's set of questions (without answers) and what is already answered
//   answer  { day, position, answer, stake?, ms? } -> checks on the server, scores, reveals the answer
//   draw    { preview?, seed? }  -> admin only: random, strength-balanced team draw (once per season); preview does not save
// Correct answers live in og_questions.secret and never leave the server before the student answers.
// The game is free for every signed-in student.

const MAX_SHIELDS = 2;
const TZ_HOURS = 5;   // Tashkent
const dayNumber = (startsOn) => {
  const today = new Date(Date.now() + TZ_HOURS * 3600 * 1000).toISOString().slice(0, 10);
  return Math.floor((Date.parse(today) - Date.parse(startsOn)) / 86400000) + 1;
};
const tashkentDate = () => new Date(Date.now() + TZ_HOURS * 3600 * 1000).toISOString().slice(0, 10);

const fail = (res, status, error) => res.status(status).json({ error });
const cache = { at: 0, season: null, dayRows: null };   // the season and the day list rarely change

// og_questions row -> the question object the engine reads
export const rowToQ = (r) => ({ ...r.secret, ...r.public, id: r.id, day: r.day, slot: r.slot, group: r.grp, type: r.type, lvl: r.lvl, bundle: r.bundle || undefined, bundleGroup: r.bundle_group || null, uses: r.uses || [], w: r.explanation, trap: r.trap || undefined });

// rows -> days with slots and variants (the shape selectDaily reads)
export function buildDays(dayRows, qRows) {
  return dayRows.map((d) => {
    const slots = new Map();
    for (const r of qRows.filter((x) => x.day === d.day)) {
      const v = rowToQ(r);
      if (!slots.has(r.slot)) slots.set(r.slot, { slot: r.slot, group: r.grp, type: r.type, lvl: r.lvl, bundleGroup: r.bundle_group || null, variants: [] });
      slots.get(r.slot).variants.push(v);
    }
    return { day: d.day, topic: d.topic, substances: d.substances || [], slots: [...slots.values()] };
  });
}

export default async function handler(req, res) {
  if (req.method !== "POST") return fail(res, 405, "Method not allowed");
  const url = process.env.VITE_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return fail(res, 503, "Hali sozlanmagan");

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return fail(res, 401, "O'ynash uchun hisobingizga kiring");
  const anon = createClient(url, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return fail(res, 401, "Sessiya eskirgan. Qayta kiring.");
  const userId = userData.user.id;

  const admin = createClient(url, serviceKey);
  const { action, day: dayIn, position, answer, stake, ms } = req.body || {};

  // the active season (cached); the first request creates "1-mavsum" starting today when none exists yet
  if (!cache.season || Date.now() - cache.at > 30000) {
    const [sRes, dRes] = await Promise.all([
      admin.from("og_seasons").select("*").neq("status", "finished").order("id", { ascending: false }).limit(1).maybeSingle(),
      admin.from("og_days").select("*").order("day"),
    ]);
    if (sRes.error) return fail(res, 503, "O'yin hali ishga tushirilmagan");
    let season = sRes.data;
    if (!season) {
      const ins = await admin.from("og_seasons").insert({ name: "1-mavsum", starts_on: tashkentDate(), status: "active" }).select("*").single();
      if (ins.error) return fail(res, 500, ins.error.message);
      season = ins.data;
    }
    Object.assign(cache, { at: Date.now(), season, dayRows: dRes.data || [] });
  }
  const season = cache.season, dayRows = cache.dayRows;
  const current = dayNumber(season.starts_on);
  const available = new Set(dayRows.map((d) => d.day));

  const getPlayer = async () => {
    let { data: p } = await admin.from("og_players").select("*").eq("user_id", userId).eq("season_id", season.id).maybeSingle();
    if (!p) {
      const ins = await admin.from("og_players").insert({ user_id: userId, season_id: season.id }).select("*").single();
      if (ins.error) throw new Error(ins.error.message);
      p = ins.data;
    }
    return p;
  };
  const totals = (p) => ({ xp: p.xp, rank: p.rank_points, streak: p.streak, shields: p.shields });

  if (action === "state") {
    const [player, { data: sets }] = await Promise.all([getPlayer(), admin.from("og_daily_sets").select("day,status").eq("user_id", userId).eq("season_id", season.id)]);
    const status = Object.fromEntries((sets || []).map((x) => [x.day, x.status]));
    const days = dayRows.map((d) => ({ day: d.day, topic: d.topic, open: d.day <= current, status: status[d.day] || "new" }));
    const team = await loadTeam(player.team_id).catch(() => null);
    return res.status(200).json({ season: { name: season.name, days: season.days, current }, player: totals(player), days, team });
  }

  const shortName = (n) => { const [a, b] = String(n || "").trim().split(/\s+/); return a ? (b ? `${a} ${b[0]}.` : a) : "O'quvchi"; };
  // the student's team with member first names and ratings (null when there is none or the team tables are not set up yet)
  const loadTeam = async (teamId) => {
    if (!teamId) return null;
    const [{ data: team }, { data: mem }] = await Promise.all([
      admin.from("og_teams").select("id,name").eq("id", teamId).maybeSingle(),
      admin.from("og_players").select("user_id,rank_points,xp").eq("season_id", season.id).eq("team_id", teamId),
    ]);
    if (!team) return null;
    const { data: profs } = await admin.from("profiles").select("id,full_name").in("id", (mem || []).map((m) => m.user_id));
    const names = new Map((profs || []).map((x) => [x.id, x.full_name]));
    const members = (mem || []).map((m) => ({ name: shortName(names.get(m.user_id)), rank: m.rank_points, me: m.user_id === userId })).sort((a, b) => b.rank - a.rank);
    const avg = members.length ? Math.round(members.reduce((acc, m) => acc + m.rank, 0) / members.length) : 0;
    return { name: team.name, members, avg };
  };

  if (action === "draw") {
    const { data: prof } = await admin.from("profiles").select("is_admin").eq("id", userId).maybeSingle();
    if (!prof?.is_admin) return fail(res, 403, "Faqat admin");
    const preview = !!req.body?.preview;
    if (season.teams_drawn_at && !preview) return fail(res, 409, "Jamoalar allaqachon tuzilgan");
    const { data: done } = await admin.from("og_daily_sets").select("user_id").eq("season_id", season.id).eq("status", "done");
    const days = new Map();
    for (const d of done || []) days.set(d.user_id, (days.get(d.user_id) || 0) + 1);
    const eligible = [...days].filter(([, n]) => n >= 2).map(([id]) => id);
    if (eligible.length < 2) return fail(res, 400, "Qur'a uchun kamida 2 kunni bajargan 2 o'quvchi kerak");
    const { data: pl } = await admin.from("og_players").select("user_id,xp,rank_points").eq("season_id", season.id).in("user_id", eligible);
    const seed = Number.isInteger(req.body?.seed) ? req.body.seed : Math.floor(Math.random() * 2 ** 31);
    const teams = drawTeams((pl || []).map((p) => ({ user_id: p.user_id, xp: p.xp })), { seed });
    const { data: profs } = await admin.from("profiles").select("id,full_name").in("id", eligible);
    const names = new Map((profs || []).map((x) => [x.id, x.full_name]));
    const xp = new Map((pl || []).map((p) => [p.user_id, p.xp]));
    const view = teams.map((t) => ({ name: t.name, size: t.members.length, avgXp: Math.round(t.members.reduce((a, u) => a + (xp.get(u) || 0), 0) / t.members.length), members: t.members.map((u) => shortName(names.get(u))) }));
    if (preview) return res.status(200).json({ preview: true, seed, players: eligible.length, teams: view });
    for (const t of teams) {
      const ins = await admin.from("og_teams").insert({ season_id: season.id, name: t.name }).select("id").single();
      if (ins.error) return fail(res, 500, ins.error.message);
      const up = await admin.from("og_players").update({ team_id: ins.data.id }).eq("season_id", season.id).in("user_id", t.members);
      if (up.error) return fail(res, 500, up.error.message);
    }
    const drawnAt = new Date().toISOString();
    await admin.from("og_seasons").update({ teams_drawn_at: drawnAt }).eq("id", season.id);
    cache.at = 0;
    return res.status(200).json({ preview: false, seed, players: eligible.length, teams: view });
  }

  if (action === "team") {
    const p = await getPlayer();
    return res.status(200).json({ team: await loadTeam(p.team_id).catch(() => null), drawn: !!season.teams_drawn_at });
  }

  const day = Number.isInteger(dayIn) ? dayIn : Math.min(current, season.days);
  if (day < 1 || day > season.days) return fail(res, 400, "Bunday kun yo'q");
  if (day > current) return fail(res, 403, "Bu kun hali ochilmagan");
  if (!available.has(day)) return fail(res, 404, "Bu kunning savollari tez orada qo'shiladi");

  // the student, today's stored set and the answers so far, in one round trip
  const [player, setRes, ansRes] = await Promise.all([
    getPlayer(),
    admin.from("og_daily_sets").select("*").eq("user_id", userId).eq("season_id", season.id).eq("day", day).maybeSingle(),
    admin.from("og_answers").select("position, ok, stake, trap_hit, xp").eq("user_id", userId).eq("season_id", season.id).eq("day", day),
  ]);
  let set = setRes.data;
  const answered = new Map((ansRes.data || []).map((a) => [a.position, a]));
  let byId;

  if (!set) {
    // first visit of this day: build the set from the whole question bank (once)
    const { data: qRows } = await admin.from("og_questions").select("*").eq("active", true);
    const days = buildDays(dayRows, qRows || []);
    byId = new Map(days.flatMap((d) => d.slots.flatMap((sl) => sl.variants)).map((q) => [q.id, q]));
    const { data: past } = await admin.from("og_answers").select("ok, og_questions(day, id)").eq("user_id", userId).eq("season_id", season.id).limit(2000);
    const errs = {}, tot = {}, seen = [];
    for (const a of past || []) {
      const d = days.find((x) => x.day === a.og_questions?.day);
      if (!d) continue;
      tot[d.topic] = (tot[d.topic] || 0) + 1; if (!a.ok) errs[d.topic] = (errs[d.topic] || 0) + 1;
      seen.push(a.og_questions.id);
    }
    const history = { seen, errors: Object.fromEntries(Object.keys(tot).map((t) => [t, (errs[t] || 0) / tot[t]])) };
    const pick = selectDaily({ day, days, userId, season: season.id, history });
    const ins = await admin.from("og_daily_sets").insert({ user_id: userId, season_id: season.id, day, items: pick.items }).select("*").single();
    if (ins.error) return fail(res, 500, ins.error.message);
    set = ins.data;
  } else {
    // later requests only need the questions of this set (for "answer": just the one being answered)
    const ids = action === "answer" && Number.isInteger(position) && set.items[position] ? [set.items[position].id] : set.items.map((it) => it.id);
    const { data: qRows } = await admin.from("og_questions").select("*").in("id", ids);
    byId = new Map((qRows || []).map((r) => [r.id, rowToQ(r)]));
  }
  const items = set.items;
  const topic = dayRows.find((d) => d.day === day)?.topic;

  if (action === "today") {
    return res.status(200).json({
      day, topic, status: set.status, stakesUsed: set.stakes_used, maxStakes: POINTS.maxStakes, total: items.length, player: totals(player),
      items: items.map((it, i) => {
        const q = byId.get(it.id);
        const a = answered.get(i);
        return { position: i, review: it.review, fromDay: it.fromDay, canStake: canStake({ lvl: q.lvl, stakesUsed: set.stakes_used }) && !a,
          question: publicQuestion(q, it.order), limit: timeLimit(q.type, false), stakeLimit: timeLimit(q.type, true), answered: a ? { ok: a.ok, stake: a.stake, xp: a.xp } : null };
      }),
    });
  }

  if (action === "answer") {
    if (!Number.isInteger(position) || position < 0 || position >= items.length) return fail(res, 400, "Savol topilmadi");
    if (answered.has(position)) return fail(res, 409, "Bu savolga javob berilgan");
    const q = byId.get(items[position].id);
    const wantsStake = !!stake && canStake({ lvl: q.lvl, stakesUsed: set.stakes_used });
    const r = check(q, answer);
    const late = isLate(ms, q.type, wantsStake);
    const sc = scoreAnswer({ ok: r.ok, stake: wantsStake, replay: false, hasShield: (player.shields || 0) > 0, late });

    const insA = await admin.from("og_answers").insert({ user_id: userId, season_id: season.id, day, position, question_id: q.id, ok: r.ok, stake: wantsStake,
      trap_hit: r.trapHit, xp: sc.xp, rank: sc.rank, ms: Number.isFinite(ms) ? Math.round(ms) : null });
    if (insA.error) return fail(res, insA.error.code === "23505" ? 409 : 500, insA.error.code === "23505" ? "Bu savolga javob berilgan" : insA.error.message);

    const setPatch = {};
    if (wantsStake) setPatch.stakes_used = set.stakes_used + 1;
    if (r.trapHit) setPatch.trap_hit = true;
    const nowAnswered = answered.size + 1;
    const done = nowAnswered >= items.length;
    let bonus = 0;
    const playerPatch = { xp: player.xp + sc.xp, rank_points: applyRank(player.rank_points, sc.rank) };
    if (sc.shieldUsed) playerPatch.shields = Math.max(0, (player.shields || 0) - 1);
    if (done) {
      bonus = dailyBonus({ completed: true, trapHit: set.trap_hit || r.trapHit });
      Object.assign(setPatch, { status: "done", completed_at: new Date().toISOString() });
      playerPatch.xp += bonus;
      playerPatch.rank_points = applyRank(playerPatch.rank_points, bonus);
      playerPatch.streak = player.last_day === day - 1 || !player.last_day ? player.streak + 1 : player.last_day === day ? player.streak : 1;
      playerPatch.last_day = day;
      // every 5th day in a row earns a shield (at most 2 kept)
      if (playerPatch.streak % 5 === 0 && playerPatch.streak > player.streak) playerPatch.shields = Math.min(MAX_SHIELDS, (playerPatch.shields ?? player.shields ?? 0) + 1);
    }
    if (Object.keys(setPatch).length) await admin.from("og_daily_sets").update(setPatch).eq("user_id", userId).eq("season_id", season.id).eq("day", day);
    await admin.from("og_players").update(playerPatch).eq("user_id", userId).eq("season_id", season.id);
    if (done && season.teams_drawn_at && !player.team_id && lateAllowed(dayNumber(player.joined_on))) {
      // joined after the draw (and by day 18): goes to the smallest team automatically; a new team is opened when all are full
      try {
        const [{ data: ts }, { data: mem }] = await Promise.all([
          admin.from("og_teams").select("id,name").eq("season_id", season.id),
          admin.from("og_players").select("team_id").eq("season_id", season.id).not("team_id", "is", null),
        ]);
        const size = new Map(); for (const m of mem || []) size.set(m.team_id, (size.get(m.team_id) || 0) + 1);
        let teamId = pickTeamForLate((ts || []).map((t) => ({ id: t.id, size: size.get(t.id) || 0 })));
        if (!teamId) {
          const taken = new Set((ts || []).map((t) => t.name));
          const name = TEAM_NAMES.find((n) => !taken.has(n)) || `Jamoa ${(ts || []).length + 1}`;
          const ins = await admin.from("og_teams").insert({ season_id: season.id, name }).select("id").single();
          teamId = ins.data?.id;
        }
        if (teamId) await admin.from("og_players").update({ team_id: teamId }).eq("user_id", userId).eq("season_id", season.id);
      } catch { /* the answer is already saved; the student can be placed on the next finished day */ }
    }

    const correctCount = [...answered.values()].filter((a) => a.ok).length + (r.ok ? 1 : 0);
    return res.status(200).json({
      ok: r.ok, trapHit: r.trapHit, reveal: r.reveal, xp: sc.xp, stakeLost: sc.stakeLost, shieldUsed: sc.shieldUsed,
      late, done, bonus, shieldEarned: (playerPatch.shields ?? player.shields) > player.shields - (sc.shieldUsed ? 1 : 0), correct: correctCount, total: items.length,
      player: { xp: playerPatch.xp, rank: playerPatch.rank_points, streak: playerPatch.streak ?? player.streak, shields: playerPatch.shields ?? player.shields },
    });
  }

  return fail(res, 400, "Noma'lum amal");
}
