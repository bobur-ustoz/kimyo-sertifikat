// Organika bot: the whole game (screens, rules, database calls). The leading underscore keeps
// Vercel from exposing this file; api/organika-webhook.js is the only endpoint and just
// authenticates the call and hands the update to handleUpdate().
//
// State lives in Supabase (ob_* tables), never in memory: every Vercel call is a fresh process.
// `db` is a service-role Supabase client and `send(method, payload)` calls the Bot API, so the
// game can be driven by tests without Telegram or a database.
//
// Callback data (Telegram allows 64 bytes):
//   m = map   p = profile   i = start the entry test   n = next question
//   s:<stage> = start a stage of chapter 1   a:<idx>:<option> = answer   l = locked stage

import { escapeHtml } from "./_telegram.js";

export const CHAPTER = 1;
export const CHAPTER_TITLE = "Alkanlar";
export const STAGES = {
  1: { part: "nomlanish", title: "Nomlanish", hearts: 3 },
  2: { part: "olinishi", title: "Olinishi", hearts: 3 },
  3: { part: "xossa", title: "Kimyoviy xossalari", hearts: 3 },
  4: { part: "boss", title: "Boss sinovi", hearts: 2 },
};
export const QUESTIONS_PER_STAGE = 10;
export const XP = { correct: 10, replay: 3, stage: 20, boss: 40 };
const LEVELS = { 1: "Boshlang'ich", 2: "O'rta", 3: "Kuchli" };
const LETTERS = ["A", "B", "C", "D"];

export const shuffle = (a) => {
  const x = a.slice();
  for (let i = x.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [x[i], x[j]] = [x[j], x[i]];
  }
  return x;
};

// Calendar day in Tashkent (UTC+5, no DST) as YYYY-MM-DD.
export const tashkentDay = (ms = Date.now()) => new Date(ms + 5 * 3600e3).toISOString().slice(0, 10);
const dayBefore = (day) => new Date(Date.parse(day) - 86400e3).toISOString().slice(0, 10);

// Streak after playing on `today`: same day keeps it, the day after extends it, a gap restarts it.
export const nextStreak = (last, streak, today = tashkentDay()) => {
  if (last === today) return Math.max(streak, 1);
  return last === dayBefore(today) ? streak + 1 : 1;
};
// What the profile shows: a streak that was not played yesterday or today has already ended.
export const liveStreak = (last, streak, today = tashkentDay()) =>
  last === today || last === dayBefore(today) ? streak : 0;

// Entry test result: <40% -> 1, <80% -> 2, otherwise 3.
export const levelFromScore = (score, total) => {
  const r = total ? score / total : 0;
  return r < 0.4 ? 1 : r < 0.8 ? 2 : 3;
};

export const heartsLine = (hearts, max) => (max ? "❤️".repeat(Math.max(hearts, 0)) + "🖤".repeat(Math.max(max - hearts, 0)) : "");
const bar = (done, total) => "▰".repeat(done) + "▱".repeat(Math.max(total - done, 0));
const btn = (text, data) => ({ text, callback_data: data });

// ---------------------------------------------------------------- screens

export function questionScreen(q, run) {
  const stage = run.chapter === 0 ? "Kirish testi" : `${STAGES[run.stage].title}`;
  const head = [`<b>${stage}</b>`, heartsLine(run.hearts, run.max_hearts)].filter(Boolean).join("   ");
  const text =
    `${head}\n${bar(run.idx, run.q_ids.length)}  ${run.idx + 1}/${run.q_ids.length}\n\n` +
    `${escapeHtml(q.text)}\n\n` +
    q.options.map((o, i) => `<b>${LETTERS[i]})</b> ${escapeHtml(o)}`).join("\n");
  return { text, reply_markup: { inline_keyboard: [q.options.map((_, i) => btn(LETTERS[i], `a:${run.idx}:${i}`))] } };
}

function mapScreen(user, done) {
  const rows = Object.keys(STAGES).map((k) => {
    const s = Number(k);
    const open = s === 1 || done.has(s - 1);
    const mark = done.has(s) ? "✅" : open ? "▶️" : "🔒";
    return [btn(`${mark} ${s}. ${STAGES[s].title}`, open ? `s:${s}` : "l")];
  });
  rows.push([btn("👤 Profil", "p")]);
  const text =
    `<b>${CHAPTER}-bob. ${CHAPTER_TITLE}</b>\n` +
    `${bar(done.size, Object.keys(STAGES).length)}  ${done.size}/${Object.keys(STAGES).length} bosqich\n\n` +
    `Bosqichlarni ketma-ket o'ting. Har bosqichda ${QUESTIONS_PER_STAGE} ta savol, xato qilsangiz jon kamayadi. ` +
    `Jon tugasa, bosqich qaytadan boshlanadi (XP saqlanadi).\n\n2–11 boblar tez orada.`;
  return { text, reply_markup: { inline_keyboard: rows } };
}

function profileScreen(user, done) {
  const streak = liveStreak(user.last_play, user.streak);
  const text =
    `<b>${escapeHtml(user.name || "O'quvchi")}</b>\n\n` +
    `Daraja: ${LEVELS[user.level] || "kirish testi topshirilmagan"}\n` +
    `XP: ${user.xp}\n` +
    `🔥 Seriya: ${streak} kun\n` +
    `Tugatilgan bosqichlar: ${done.size}/${Object.keys(STAGES).length}`;
  return { text, reply_markup: { inline_keyboard: [[btn("🗺 Xarita", "m")]] } };
}

const WELCOME =
  "Assalomu alaykum! Bu <b>Organika</b> — organik kimyoni o'yin orqali o'rganish boti.\n\n" +
  "Bosqichlarni o'tasiz, XP yig'asiz, har kuni kirsangiz 🔥 seriyangiz o'sadi.\n\n" +
  "Avval 5 ta savollik kirish testi: u darajangizni aniqlaydi. Jon yo'qotilmaydi.";

const HELP =
  "<b>Buyruqlar</b>\n/oyin — bob xaritasi\n/profil — XP, daraja, seriya\n/yordam — shu xabar\n\n" +
  "Xato qilsangiz ❤️ kamayadi. Jon tugasa, bosqich qaytadan boshlanadi. XP hech qachon yo'qolmaydi.";

// ---------------------------------------------------------------- database helpers

async function getUser(db, id) {
  const { data } = await db.from("ob_users").select("*").eq("tg_id", id).maybeSingle();
  return data;
}

async function ensureUser(db, from) {
  const found = await getUser(db, from.id);
  if (found) return found;
  const name = [from.first_name, from.last_name].filter(Boolean).join(" ").trim().slice(0, 60) || "O'quvchi";
  await db.from("ob_users").upsert({ tg_id: from.id, name, username: from.username ?? null }, { onConflict: "tg_id", ignoreDuplicates: true });
  return getUser(db, from.id);
}

async function progressOf(db, tgId) {
  const { data } = await db.from("ob_progress").select("stage, done, best_score").eq("tg_id", tgId).eq("chapter", CHAPTER);
  const rows = data || [];
  return { done: new Set(rows.filter((r) => r.done).map((r) => r.stage)), rows };
}

const getRun = async (db, tgId) => (await db.from("ob_runs").select("*").eq("tg_id", tgId).maybeSingle()).data;
const getQuestion = async (db, id) => (await db.from("ob_questions").select("*").eq("id", id).maybeSingle()).data;

async function startRun(db, user, chapter, stage, part, count, hearts) {
  const { data } = await db.from("ob_questions").select("id").eq("chapter", chapter).eq("part", part).eq("active", true);
  if (!data?.length) return null;
  const run = {
    tg_id: user.tg_id, chapter, stage, q_ids: shuffle(data.map((q) => q.id)).slice(0, count),
    idx: 0, correct: 0, hearts, max_hearts: hearts, started_at: new Date().toISOString(),
  };
  await db.from("ob_runs").upsert(run, { onConflict: "tg_id" });
  return run;
}

// ---------------------------------------------------------------- Telegram plumbing

// Shows `screen` by editing the message a button was pressed on, or sends a new message.
async function show(send, cb, chatId, screen) {
  const payload = { parse_mode: "HTML", ...screen };
  if (cb?.message) {
    await send("editMessageText", { chat_id: cb.message.chat.id, message_id: cb.message.message_id, ...payload });
  } else {
    await send("sendMessage", { chat_id: chatId, ...payload });
  }
}
const ack = (send, cb, text, alert = false) =>
  send("answerCallbackQuery", { callback_query_id: cb.id, ...(text ? { text, show_alert: alert } : {}) });

async function showQuestion(db, send, cb, chatId, run) {
  const q = await getQuestion(db, run.q_ids[run.idx]);
  if (!q) return show(send, cb, chatId, { text: "Savol topilmadi. Keyinroq urinib ko'ring.", reply_markup: { inline_keyboard: [[btn("🗺 Xarita", "m")]] } });
  return show(send, cb, chatId, questionScreen(q, run));
}

async function showMap(db, send, cb, chatId, user) {
  const { done } = await progressOf(db, user.tg_id);
  return show(send, cb, chatId, mapScreen(user, done));
}

// ---------------------------------------------------------------- game actions

async function startStage(db, send, cb, user, stage) {
  const st = STAGES[stage];
  if (!st) return ack(send, cb);
  const { done } = await progressOf(db, user.tg_id);
  if (stage > 1 && !done.has(stage - 1)) return ack(send, cb, "Avval oldingi bosqichni tugating", true);
  const run = await startRun(db, user, CHAPTER, stage, st.part, QUESTIONS_PER_STAGE, st.hearts);
  if (!run) return ack(send, cb, "Bu bosqichning savollari hali tayyor emas", true);
  await ack(send, cb);
  return showQuestion(db, send, cb, cb.message?.chat.id, run);
}

async function startIntro(db, send, cb, user) {
  if (user.level) {
    await ack(send, cb);
    return showMap(db, send, cb, cb.message?.chat.id, user);
  }
  const run = await startRun(db, user, 0, 1, "intro", 5, 0);
  if (!run) return ack(send, cb, "Kirish testi hali tayyor emas", true);
  await ack(send, cb);
  return showQuestion(db, send, cb, cb.message?.chat.id, run);
}

async function awardXp(db, tgId, amount) {
  if (amount > 0) await db.rpc("ob_add_xp", { p_tg: tgId, p_xp: amount });
}

async function touchStreak(db, user) {
  const today = tashkentDay();
  if (user.last_play === today) return;
  await db.from("ob_users").update({ streak: nextStreak(user.last_play, user.streak, today), last_play: today }).eq("tg_id", user.tg_id);
}

async function onAnswer(db, send, cb, user, idx, opt) {
  const run = await getRun(db, user.tg_id);
  if (!run || run.idx !== idx) return ack(send, cb, "Bu savolga allaqachon javob berilgan");
  const q = await getQuestion(db, run.q_ids[idx]);
  if (!q || !(opt >= 0 && opt < q.options.length)) return ack(send, cb);

  const ok = opt === q.correct;
  const hearts = ok || !run.max_hearts ? run.hearts : run.hearts - 1;
  const correct = run.correct + (ok ? 1 : 0);
  const failed = run.max_hearts > 0 && hearts <= 0;
  const finished = failed || idx + 1 >= run.q_ids.length;

  // Compare-and-set on idx: a second tap or a retried update matches no row and is ignored.
  const { data: moved } = await db.from("ob_runs").update({ idx: idx + 1, correct, hearts }).eq("tg_id", user.tg_id).eq("idx", idx).select("tg_id").maybeSingle();
  if (!moved) return ack(send, cb, "Bu savolga allaqachon javob berilgan");

  await db.from("ob_answers").insert({ tg_id: user.tg_id, question_id: q.id, ok });
  await touchStreak(db, user);

  const { done, rows } = run.chapter === 0 ? { done: new Set(), rows: [] } : await progressOf(db, user.tg_id);
  const replay = done.has(run.stage);
  const gain = ok && run.chapter > 0 ? (replay ? XP.replay : XP.correct) : 0;
  await awardXp(db, user.tg_id, gain);

  const verdict = ok
    ? `✅ <b>To'g'ri!</b>${gain ? ` +${gain} XP` : ""}`
    : `❌ <b>Noto'g'ri.</b> To'g'ri javob: <b>${LETTERS[q.correct]})</b> ${escapeHtml(q.options[q.correct])}`;
  let text = `${escapeHtml(q.text)}\n\n${verdict}`;
  if (q.explanation) text += `\n\n💡 ${escapeHtml(q.explanation)}`;
  if (run.max_hearts) text += `\n\n${heartsLine(hearts, run.max_hearts)}`;

  await ack(send, cb);
  const kb = [];

  if (!finished) {
    kb.push([btn("Keyingi ▶", "n")]);
  } else {
    await db.from("ob_runs").delete().eq("tg_id", user.tg_id);
    if (failed) {
      text += `\n\n💔 <b>Jon tugadi.</b> Bosqich qaytadan boshlanadi, XP saqlanadi.`;
      kb.push([btn("🔁 Qayta urinish", `s:${run.stage}`)], [btn("🗺 Xarita", "m")]);
    } else if (run.chapter === 0) {
      const level = levelFromScore(correct, run.q_ids.length);
      await db.from("ob_users").update({ level }).eq("tg_id", user.tg_id);
      text += `\n\n🎯 <b>Kirish testi tugadi:</b> ${correct}/${run.q_ids.length}\nDarajangiz: <b>${LEVELS[level]}</b>`;
      kb.push([btn("🗺 Xaritaga o'tish", "m")]);
    } else {
      const bonus = replay ? 0 : run.stage === 4 ? XP.boss : XP.stage;
      await awardXp(db, user.tg_id, bonus);
      const prev = rows.find((r) => r.stage === run.stage)?.best_score || 0;
      await db.from("ob_progress").upsert(
        { tg_id: user.tg_id, chapter: run.chapter, stage: run.stage, done: true, best_score: Math.max(prev, correct), updated_at: new Date().toISOString() },
        { onConflict: "tg_id,chapter,stage" });
      text += `\n\n🎉 <b>Bosqich tugadi!</b> To'g'ri javoblar: ${correct}/${run.q_ids.length}` + (bonus ? `\n+${bonus} XP bonus` : "");
      if (STAGES[run.stage + 1]) kb.push([btn(`▶️ ${run.stage + 1}. ${STAGES[run.stage + 1].title}`, `s:${run.stage + 1}`)]);
      kb.push([btn("🗺 Xarita", "m")]);
    }
  }
  return show(send, cb, cb.message?.chat.id, { text, reply_markup: { inline_keyboard: kb } });
}

// ---------------------------------------------------------------- entry points

async function onCallback(db, send, cb) {
  const user = await ensureUser(db, cb.from);
  if (!user) return ack(send, cb);
  const data = cb.data || "";
  const chatId = cb.message?.chat.id;

  if (data === "m") { await ack(send, cb); return showMap(db, send, cb, chatId, user); }
  if (data === "p") {
    await ack(send, cb);
    const { done } = await progressOf(db, user.tg_id);
    return show(send, cb, chatId, profileScreen(user, done));
  }
  if (data === "l") return ack(send, cb, "Avval oldingi bosqichni tugating", true);
  if (data === "i") return startIntro(db, send, cb, user);
  if (data === "n") {
    const run = await getRun(db, user.tg_id);
    await ack(send, cb);
    return run && run.idx < run.q_ids.length ? showQuestion(db, send, cb, chatId, run) : showMap(db, send, cb, chatId, user);
  }
  let m = /^s:(\d)$/.exec(data);
  if (m) return startStage(db, send, cb, user, Number(m[1]));
  m = /^a:(\d+):(\d)$/.exec(data);
  if (m) return onAnswer(db, send, cb, user, Number(m[1]), Number(m[2]));
  return ack(send, cb);
}

async function onText(db, send, msg) {
  const cmd = (msg.text.trim().split(/[\s@]/)[0] || "").toLowerCase();
  const chatId = msg.chat.id;
  const user = await ensureUser(db, msg.from);
  if (!user) return;

  if (cmd === "/start") {
    if (user.level) return showMap(db, send, null, chatId, user);
    return send("sendMessage", { chat_id: chatId, parse_mode: "HTML", text: WELCOME, reply_markup: { inline_keyboard: [[btn("Testni boshlash", "i")]] } });
  }
  if (cmd === "/oyin") return user.level ? showMap(db, send, null, chatId, user) : send("sendMessage", { chat_id: chatId, parse_mode: "HTML", text: WELCOME, reply_markup: { inline_keyboard: [[btn("Testni boshlash", "i")]] } });
  if (cmd === "/profil") {
    const { done } = await progressOf(db, user.tg_id);
    return show(send, null, chatId, profileScreen(user, done));
  }
  if (cmd === "/yordam") return send("sendMessage", { chat_id: chatId, parse_mode: "HTML", text: HELP });
  if (cmd.startsWith("/")) return send("sendMessage", { chat_id: chatId, text: "Bunday buyruq yo'q. /oyin yoki /yordam ni bosing." });
}

export async function handleUpdate(update, db, send) {
  if (update.callback_query) return onCallback(db, send, update.callback_query);
  const msg = update.message;
  if (msg?.text && msg.chat?.type === "private" && msg.from && !msg.from.is_bot) return onText(db, send, msg);
}
