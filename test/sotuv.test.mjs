import test from "node:test";
import assert from "node:assert/strict";
import { handleUpdate, parseTags, toChat, tashkentDay, DAILY_LIMIT, SYSTEM } from "../api/_sotuv.js";

// Xotiradagi soxta baza, Telegram, Claude va ustoz xabari.
function setup(reply = "Salom, yordam beraman.") {
  const leads = new Map();
  const msgs = [];
  const sent = [];
  const notes = [];
  const asked = [];
  const store = {
    async getLead(id) { return leads.get(id) || null; },
    async insertLead(row) { const l = { stage: "new", human: false, last_update_id: 0, msg_day: null, msg_count: 0, handoff_reason: null, ...row }; leads.set(row.tg_id, l); return { ...l }; },
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
  assert.deepEqual(parseTags("Albatta.\n[[UZAT: pul qaytarish]]"), { text: "Albatta.", handoff: "pul qaytarish", stop: false });
  assert.deepEqual(parseTags("Xo'p. [[TOXTA]]"), { text: "Xo'p.", handoff: null, stop: true });
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
  assert.match(t.sent[0].text, /AI yordamchi/);
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

test("[[UZAT]]: ustozga xabar ketadi, belgi foydalanuvchiga ko'rinmaydi, keyin AI jim", async () => {
  const t = setup("Bu savolni ustozga yetkazaman. [[UZAT: pul qaytarish so'radi]]");
  await t.say("Pulni qaytarib bera olasizmi?");
  const texts = t.sent.filter((s) => s.method === "sendMessage").map((s) => s.text);
  assert.ok(texts.every((x) => !x.includes("[[")));
  assert.equal(t.notes.length, 1);
  assert.match(t.notes[0], /pul qaytarish/);
  assert.equal(t.leads.get(7).human, true);
  assert.equal(t.leads.get(7).stage, "handoff");
  const askedBefore = t.asked.length;
  await t.say("Hali shu yerdamisiz?");
  assert.equal(t.asked.length, askedBefore);
  assert.equal(t.notes.length, 2);
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
  await handleUpdate({ update_id: t.next(), callback_query: { id: "c2", from: { id: 7 }, data: "ustoz" } }, t.deps);
  assert.equal(t.leads.get(7).human, true);
  assert.equal(t.notes.length, 1);
});
