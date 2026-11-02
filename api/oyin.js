import { createClient } from "@supabase/supabase-js";
import { selectDaily } from "./_oyin/select.js";
import { publicQuestion, check } from "./_oyin/view.js";
import { scoreAnswer, canStake, dailyBonus, applyRank, POINTS } from "./_oyin/score.js";

// Organika game API. One function (Vercel Hobby allows 12), the action is in the body:
//   state                       -> season, today's day number, the student's totals, the list of days
//   today   { day? }            -> today's set of questions (without answers) and what is already answered
//   answer  { day, position, answer, stake?, ms? } -> checks on the server, scores, reveals the answer
// Correct answers live in og_questions.secret and never leave the server before the student answers.
// The game is free for every signed-in student.

const TZ_HOURS = 5;   // Tashkent
const dayNumber = (startsOn) => {
  const today = new Date(Date.now() + TZ_HOURS * 3600 * 1000).toISOString().slice(0, 10);
  return Math.floor((Date.parse(today) - Date.parse(startsOn)) / 86400000) + 1;
};
const tashkentDate = () => new Date(Date.now() + TZ_HOURS * 3600 * 1000).toISOString().slice(0, 10);

const fail = (res, status, error) => res.status(status).json({ error });

// og_questions rows -> the shape the engine reads (slots with variants)
export function buildDays(dayRows, qRows) {
  return dayRows.map((d) => {
    const slots = new Map();
    for (const r of qRows.filter((x) => x.day === d.day)) {
      const v = { ...r.secret, ...r.public, id: r.id, day: r.day, slot: r.slot, group: r.grp, type: r.type, lvl: r.lvl, bundle: r.bundle || undefined, bundleGroup: r.bundle_group || null, uses: r.uses || [], w: r.explanation, trap: r.trap || undefined };
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

  // the active season; the first request creates "1-mavsum" starting today when none exists yet
  let { data: season, error: sErr } = await admin.from("og_seasons").select("*").neq("status", "finished").order("id", { ascending: false }).limit(1).maybeSingle();
  if (sErr) return fail(res, 503, "O'yin hali ishga tushirilmagan");
  if (!season) {
    const ins = await admin.from("og_seasons").insert({ name: "1-mavsum", starts_on: tashkentDate(), status: "active" }).select("*").single();
    if (ins.error) return fail(res, 500, ins.error.message);
    season = ins.data;
  }
  const current = dayNumber(season.starts_on);

  const { data: dayRows } = await admin.from("og_days").select("*").order("day");
  const available = new Set((dayRows || []).map((d) => d.day));

  // the student's totals (created on the first visit)
  let { data: player } = await admin.from("og_players").select("*").eq("user_id", userId).eq("season_id", season.id).maybeSingle();
  if (!player) {
    const ins = await admin.from("og_players").insert({ user_id: userId, season_id: season.id }).select("*").single();
    if (ins.error) return fail(res, 500, ins.error.message);
    player = ins.data;
  }
  const totals = (p) => ({ xp: p.xp, rank: p.rank_points, streak: p.streak, shields: p.shields });

  if (action === "state") {
    const { data: sets } = await admin.from("og_daily_sets").select("day,status").eq("user_id", userId).eq("season_id", season.id);
    const status = Object.fromEntries((sets || []).map((s) => [s.day, s.status]));
    const days = (dayRows || []).map((d) => ({ day: d.day, topic: d.topic, open: d.day <= current, status: status[d.day] || "new" }));
    return res.status(200).json({ season: { name: season.name, days: season.days, current }, player: totals(player), days });
  }

  const day = Number.isInteger(dayIn) ? dayIn : Math.min(current, season.days);
  if (day < 1 || day > season.days) return fail(res, 400, "Bunday kun yo'q");
  if (day > current) return fail(res, 403, "Bu kun hali ochilmagan");
  if (!available.has(day)) return fail(res, 404, "Bu kunning savollari tez orada qo'shiladi");

  const { data: qRows } = await admin.from("og_questions").select("*").eq("active", true);
  const days = buildDays(dayRows, qRows || []);
  const byId = new Map(days.flatMap((d) => d.slots.flatMap((s) => s.variants)).map((q) => [q.id, q]));

  // today's set: built once and stored, so a reload gives the same questions
  let { data: set } = await admin.from("og_daily_sets").select("*").eq("user_id", userId).eq("season_id", season.id).eq("day", day).maybeSingle();
  if (!set) {
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
  }
  const items = set.items;
  const { data: ans } = await admin.from("og_answers").select("position, ok, stake, trap_hit, xp").eq("user_id", userId).eq("season_id", season.id).eq("day", day);
  const answered = new Map((ans || []).map((a) => [a.position, a]));

  if (action === "today") {
    const topic = days.find((d) => d.day === day)?.topic;
    return res.status(200).json({
      day, topic, status: set.status, stakesUsed: set.stakes_used, maxStakes: POINTS.maxStakes, total: items.length, player: totals(player),
      items: items.map((it, i) => {
        const q = byId.get(it.id);
        const a = answered.get(i);
        return { position: i, review: it.review, fromDay: it.fromDay, canStake: canStake({ lvl: q.lvl, stakesUsed: set.stakes_used }) && !a,
          question: publicQuestion(q, it.order), answered: a ? { ok: a.ok, stake: a.stake, xp: a.xp } : null };
      }),
    });
  }

  if (action === "answer") {
    if (!Number.isInteger(position) || position < 0 || position >= items.length) return fail(res, 400, "Savol topilmadi");
    if (answered.has(position)) return fail(res, 409, "Bu savolga javob berilgan");
    const q = byId.get(items[position].id);
    const wantsStake = !!stake && canStake({ lvl: q.lvl, stakesUsed: set.stakes_used });
    const r = check(q, answer);
    const sc = scoreAnswer({ ok: r.ok, stake: wantsStake, replay: false, hasShield: (player.shields || 0) > 0 });

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
    }
    if (Object.keys(setPatch).length) await admin.from("og_daily_sets").update(setPatch).eq("user_id", userId).eq("season_id", season.id).eq("day", day);
    await admin.from("og_players").update(playerPatch).eq("user_id", userId).eq("season_id", season.id);

    const correctCount = [...answered.values()].filter((a) => a.ok).length + (r.ok ? 1 : 0);
    return res.status(200).json({
      ok: r.ok, trapHit: r.trapHit, reveal: r.reveal, xp: sc.xp, stakeLost: sc.stakeLost, shieldUsed: sc.shieldUsed,
      done, bonus, correct: correctCount, total: items.length,
      player: { xp: playerPatch.xp, rank: playerPatch.rank_points, streak: playerPatch.streak ?? player.streak, shields: playerPatch.shields ?? player.shields },
    });
  }

  return fail(res, 400, "Noma'lum amal");
}
