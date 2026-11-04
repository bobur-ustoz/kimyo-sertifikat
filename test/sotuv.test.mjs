import test from "node:test";
import assert from "node:assert/strict";
import { handleUpdate, parseTags, toChat, tashkentDay, DAILY_LIMIT, HANDOFF_HOURS, SYSTEM } from "../api/_sotuv.js";

// Xotiradagi soxta baza, Telegram, Claude va ustoz xabari.
function setup(reply = "Salom, yordam beraman.") {
  const leads = new Map();
  const msgs = [];
  const sent = [];
  const notes = [];
  const asked = [];
  const store = {
    async getLead(id) { return leads.get(id) || null; },
    async insertLead(row) { const l = { stage: "new", human: false, last_update_id: 0, msg_day: null, msg_count: 0, handoff_reason: null, handoff_at: null, ack_at: null, ...row }; leads.set(row.tg_id, l); return { ...l }; },
    async updateLead(id, patch) { Object.assign(leads.get(id), patch); },
    async addMessage(id, role, content) { msgs.push({ tg_id: id, role, content }); },
    async history(id, n) { return msgs.filter((m) => m.tg_id === id).slice(-n); },
  };
  const deps = {
    store,
    send: async (method, p) => { sent.push({ method, ...p }); return { ok: true }; },
    ask: async (system, chat) => { asked.push({ system, chat }); return typeof reply === "function" ? reply() : reply; },
    notify: async (t) => { notes.push(t); },
  };
  let uid = 0;
  const say = (text, from = { id: 7, first_name: "Ali", username: "ali" }) =>
    handleUpdate({ update_id: ++uid, message: { chat: { type: "private" }, from, text } }, deps);
  return { leads, msgs, sent, notes, asked, say, deps, next: () => ++uid };
}

test("parseTags: belgilar ajratiladi va matndan olib tashlanadi", () => {
  assert.deepEqual(parseTags("Albatta.\n[[UZAT: pul o'tdi, ochilmadi]]"), { text: "Albatta.", handoff: "pul o'tdi, ochilmadi", note: null, stop: false });
  assert.deepEqual(parseTags("Xo'p. [[TOXTA]]"), { text: "Xo'p.", handoff: null, note: null, stop: true });
  assert.deepEqual(parseTags("Ustoz yozadi. [[ESLAT: aloqa so'rovi]]"), { text: "Ustoz yozadi.", handoff: null, note: "aloqa so'rovi", stop: false });
  assert.equal(parseTags("[[uzat]]").handoff, "sabab ko'rsatilmagan");
  assert.equal(parseTags("Oddiy javob").text, "Oddiy javob");
  assert.equal(parseTags(null).text, "");
});

test("toChat: rollar almashadi, user bilan boshlanib user bilan tugaydi", () => {
  const chat = toChat([
    { role: "assistant", content: "x" }, { role: "user", content: "a" }, { role: "user", content: "b" },
    { role: "assistant", content: "c" }, { role: "user", content: "d" }, { role: "assistant", content: "e" },
  ]);
  assert.deepEqual(chat, [{ role: "user", content: "a\nb" }, { role: "assistant", content: "c" }, { role: "user", content: "d" }]);
});

test("/start: lid manba bilan yaratiladi, AI chaqirilmaydi, tugmalar chiqadi", async () => {
  const t = setup();
  await t.say("/start ig_valent");
  assert.equal(t.leads.get(7).source, "ig_valent");
  assert.equal(t.asked.length, 0);
  assert.ok(t.sent[0].reply_markup.inline_keyboard.length === 2);
  assert.match(t.sent[0].text, /yordamchi bot/);
  assert.doesNotMatch(t.sent[0].text, /AI/);
});

test("oddiy xabar: AI javobi yuboriladi va jurnalga yoziladi", async () => {
  const t = setup("11-sinfman deb yozdingiz, tushundim.");
  await t.say("11-sinfman, Milliy sertifikat");
  assert.equal(t.sent.at(-1).text, "11-sinfman deb yozdingiz, tushundim.");
  assert.deepEqual(t.msgs.map((m) => m.role), ["user", "assistant"]);
  assert.equal(t.leads.get(7).stage, "chatting");
  assert.equal(t.leads.get(7).msg_count, 1);
  assert.equal(t.asked[0].system, SYSTEM);
  assert.equal(t.asked[0].chat.at(-1).role, "user");
});

test("[[UZAT]]: ustozga xabar ketadi, belgi ko'rinmaydi, ikkinchi ortiqcha xabar yo'q, keyin AI jim", async () => {
  const t = setup("Pul o'tgan bo'lsa, ustoz tekshiradi, odatda 3–4 soat ichida. [[UZAT: pul o'tkazdi, ochilmadi]]");
  await t.say("Pul o'tkazdim, lekin ochilmadi");
  const texts = t.sent.filter((s) => s.method === "sendMessage").map((s) => s.text);
  assert.equal(texts.length, 1);
  assert.ok(!texts[0].includes("[["));
  assert.equal(t.notes.length, 1);
  assert.match(t.notes[0], /ochilmadi/);
  assert.equal(t.leads.get(7).human, true);
  assert.equal(t.leads.get(7).stage, "handoff");
  assert.ok(t.leads.get(7).handoff_at);
  const askedBefore = t.asked.length;
  await t.say("Hali shu yerdamisiz?");
  assert.equal(t.asked.length, askedBefore);
  assert.equal(t.notes.length, 2);
});

test("ustoz rejimida 'yetkazildi' xabari takrorlanmaydi, lekin har xabar ustozga boradi", async () => {
  const t = setup("Xo'p. [[UZAT: shikoyat]]");
  await t.say("Shikoyatim bor");
  const before = t.sent.length;
  await t.say("birinchi");
  await t.say("ikkinchi");
  assert.equal(t.sent.length, before);          // AI javobi allaqachon aytgan, 30 daqiqa ichida qayta yozilmaydi
  assert.equal(t.notes.length, 3);              // lekin har xabar ustozga yetadi
  t.leads.get(7).ack_at = new Date(Date.now() - 31 * 60e3).toISOString();
  await t.say("uchinchi");
  await t.say("to'rtinchi");
  assert.equal(t.sent.length - before, 1);      // 30 daqiqadan keyin faqat bitta "yetkazildi"
  assert.equal(t.notes.length, 5);
});

test("[[ESLAT]]: ustozga jim xabar, suhbat davom etadi va AI javob berishda qoladi", async () => {
  const t = setup("Jonli dars hozir rejada yo'q, bo'lsa e'lon qilinadi. [[ESLAT: jonli dars so'radi]]");
  await t.say("Jonli dars qachon?");
  assert.equal(t.notes.length, 1);
  assert.match(t.notes[0], /jonli dars/);
  assert.equal(t.leads.get(7).human, false);
  await t.say("Mayli, mavzu videolari bormi?");
  assert.equal(t.asked.length, 2);
  assert.equal(t.sent.filter((s) => s.method === "sendMessage").length, 2);
});

test("to'liq uzatishdan HANDOFF_HOURS o'tsa AI o'zi qaytadi", async () => {
  const t = setup("Marhamat.");
  await t.say("/start");
  Object.assign(t.leads.get(7), { human: true, stage: "handoff", handoff_at: new Date(Date.now() - (HANDOFF_HOURS + 1) * 3600e3).toISOString() });
  await t.say("Premium nimalarni beradi?");
  assert.equal(t.asked.length, 1);
  assert.equal(t.leads.get(7).human, false);
});

test("eski (handoff_at yo'q) ustoz rejimidagi lid ham AI'ga qaytadi", async () => {
  const t = setup("Marhamat.");
  await t.say("/start");
  Object.assign(t.leads.get(7), { human: true, stage: "handoff", handoff_at: null });
  await t.say("Salom");
  assert.equal(t.asked.length, 1);
});

test("tizim ko'rsatmasi: salom takrorlanmaydi, yordamchi bot, ESLAT va UZAT bor, yangi bilim kiritilgan", () => {
  assert.match(SYSTEM, /qayta salomlashmang/);
  assert.match(SYSTEM, /yordamchi bot/);
  assert.match(SYSTEM, /\[\[ESLAT/);
  assert.match(SYSTEM, /FAQAT to'lov muammosi/);
  assert.match(SYSTEM, /plastik kartaga/);
  assert.match(SYSTEM, /3–4 soat/);
  assert.match(SYSTEM, /qaytarilmaydi/);
  assert.match(SYSTEM, /Nazorat qanday bo'ladi/);
  assert.match(SYSTEM, /Faqat so'ralgan narsaga javob bering/);
  assert.match(SYSTEM, /BO'SH QATOR/);
  assert.match(SYSTEM, /ALOHIDA QATORDA "•"/);
  assert.doesNotMatch(SYSTEM, /ro'yxat belgilarisiz/);
  assert.match(SYSTEM, /TO'LOVGA yo'naltirishdan oldin/);
});

test("[[TOXTA]] va /stop: stopped holati, qayta /start bilan tiklanadi", async () => {
  const t = setup("Xo'p, rahmat. [[TOXTA]]");
  await t.say("Qiziq emas");
  assert.equal(t.leads.get(7).stage, "stopped");
  await t.say("/start");
  assert.equal(t.leads.get(7).stage, "new");
  await t.say("/stop");
  assert.equal(t.leads.get(7).stage, "stopped");
});

test("kunlik chegara oshsa AI chaqirilmaydi", async () => {
  const t = setup();
  await t.say("/start");
  Object.assign(t.leads.get(7), { msg_day: tashkentDay(), msg_count: DAILY_LIMIT });
  const before = t.asked.length;
  await t.say("yana savol");
  assert.equal(t.asked.length, before);
  assert.match(t.sent.at(-1).text, /chegara/);
});

test("Telegram bir xil update'ni qayta yuborsa ikki marta javob bermaydi", async () => {
  const t = setup();
  const upd = { update_id: 500, message: { chat: { type: "private" }, from: { id: 9, first_name: "Vali" }, text: "salom" } };
  await handleUpdate(upd, t.deps);
  const n = t.sent.length;
  await handleUpdate(upd, t.deps);
  assert.equal(t.sent.length, n);
});

test("AI xato bersa: ustozga ogohlantirish va muloyim javob, assistant xabari yozilmaydi", async () => {
  const t = setup(() => { throw new Error("429"); });
  await t.say("Narxi qancha?");
  assert.equal(t.notes.length, 1);
  assert.match(t.sent.at(-1).text, /ustozga yetkazdim/);
  assert.deepEqual(t.msgs.map((m) => m.role), ["user"]);
});

test("guruh, bot va matnsiz xabarlar: guruh e'tiborsiz, matnsizga tushuntirish", async () => {
  const t = setup();
  await handleUpdate({ update_id: 1, message: { chat: { type: "group" }, from: { id: 1 }, text: "salom" } }, t.deps);
  await handleUpdate({ update_id: 2, message: { chat: { type: "private" }, from: { id: 2, is_bot: true }, text: "salom" } }, t.deps);
  assert.equal(t.sent.length, 0);
  await t.say("");
  assert.match(t.sent.at(-1).text, /matn/);
});

test("narx va ustoz tugmalari", async () => {
  const t = setup();
  await t.say("/start");
  await handleUpdate({ update_id: t.next(), callback_query: { id: "c1", from: { id: 7 }, data: "narx" } }, t.deps);
  assert.match(t.sent.at(-1).text, /200 000/);
  assert.match(t.sent.at(-1).text, /49 900/);
  assert.match(t.sent.at(-1).text, /\n\n👑/);                       // bo'limlar bo'sh qator bilan ajratilgan
  assert.doesNotMatch(t.sent.at(-1).text, /qaytar/i);              // qaytarish tafsiloti narx tugmasida yo'q, so'ralganda AI aytadi
  await handleUpdate({ update_id: t.next(), callback_query: { id: "c2", from: { id: 7 }, data: "ustoz" } }, t.deps);
  assert.equal(t.leads.get(7).human, true);
  assert.equal(t.notes.length, 1);
});

// ---- askClaude: kesilgan/bo'sh javoblar (haqiqiy xato: o'ylash tokenlari max_tokens ni yeb qo'ygan) ----
import { askClaude } from "../api/_sotuv.js";

const withFetch = async (responses, fn) => {
  const calls = [];
  const orig = globalThis.fetch;
  globalThis.fetch = async (url, init) => {
    calls.push(JSON.parse(init.body));
    const { status = 200, body } = responses.shift();
    return { ok: status < 400, status, json: async () => body };
  };
  try { return await fn(calls); } finally { globalThis.fetch = orig; }
};

test("askClaude: o'ylash o'chiriladi, max_tokens katta, matn bloklari birlashtiriladi", async () => {
  await withFetch([{ body: { stop_reason: "end_turn", usage: { output_tokens: 40 }, content: [{ type: "thinking", thinking: "" }, { type: "text", text: "Javob." }] } }], async (calls) => {
    assert.equal(await askClaude("sys", [{ role: "user", content: "q" }]), "Javob.");
    assert.deepEqual(calls[0].thinking, { type: "between_tools" });
    assert.ok(calls[0].max_tokens >= 1000);
  });
});

test("askClaude: thinking parametri 400 bersa, usiz qayta uriniladi", async () => {
  await withFetch([
    { status: 400, body: { error: { message: "thinking: not supported for this model" } } },
    { body: { stop_reason: "end_turn", content: [{ type: "text", text: "Mayli." }] } },
  ], async (calls) => {
    assert.equal(await askClaude("sys", []), "Mayli.");
    assert.equal(calls.length, 2);
    assert.equal("thinking" in calls[1], false);
  });
});

test("askClaude: matn bo'lmasa (max_tokens ga yetib qolgan) xato beradi, 'tushunmadim' deb yashirmaydi", async () => {
  await withFetch([{ body: { stop_reason: "max_tokens", content: [{ type: "thinking", thinking: "..." }] } }], async () => {
    await assert.rejects(() => askClaude("sys", []), /bo'sh javob \(stop_reason=max_tokens\)/);
  });
});

test("askClaude: boshqa 4xx/5xx xatolari o'z xabari bilan ko'tariladi", async () => {
  await withFetch([{ status: 429, body: { error: { message: "rate limited" } } }], async () => {
    await assert.rejects(() => askClaude("sys", []), /rate limited/);
  });
});
