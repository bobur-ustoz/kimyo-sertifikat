import test from "node:test";
import assert from "node:assert/strict";
import { handleUpdate, parseTags, toChat, tashkentDay, DAILY_LIMIT, HANDOFF_HOURS, SYSTEM, LINKED_TEXT, LINKED_NOTE, LOGIN_DONE, PHONE_TEXT_LOGIN, PHONE_TEXT_NOLOGIN, isPhoneText, LINK_ALREADY, LOGIN_USED_LINKED } from "../api/_sotuv.js";

// Xotiradagi soxta baza, Telegram, Claude va ustoz xabari.
function setup(reply = "Salom, yordam beraman.") {
  const leads = new Map();
  const codes = new Map();
  const logins = new Map();
  const msgs = [];
  const sent = [];
  const notes = [];
  const asked = [];
  const store = {
    async getLead(id) { return leads.get(id) || null; },
    async insertLead(row) { const l = { stage: "new", human: false, last_update_id: 0, msg_day: null, msg_count: 0, handoff_reason: null, handoff_at: null, ack_at: null, linked_user_id: null, remind: true, ...row }; leads.set(row.tg_id, l); return { ...l }; },
    async updateLead(id, patch) { Object.assign(leads.get(id), patch); },
    async getLogin(code) { const l = logins.get(code); return l && !l.user_id && !l.expired ? { code } : null; },
    async attachLogin(code, tgId) { logins.get(code).tg_id = tgId; },
    async pendingLoginFor(tgId) { const e = [...logins.entries()].find(([, l]) => l.tg_id === tgId && !l.user_id && !l.expired); return e ? { code: e[0] } : null; },
    async completeLogin(code, info) { const userId = `u-${info.tgId}`; Object.assign(logins.get(code), { user_id: userId, info }); Object.assign(leads.get(info.tgId), { linked_user_id: userId, remind: true }); return userId; },
    async redeemLinkCode(code) { const c = codes.get(code); if (!c || c.used || c.expired) return null; c.used = true; return c.user_id; },
    async linkLead(id, userId) { for (const l of leads.values()) if (l.linked_user_id === userId) l.linked_user_id = null; Object.assign(leads.get(id), { linked_user_id: userId, remind: true }); },
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
  const say = (text, from = { id: 7, first_name: "Ali", username: "ali" }, extra = {}) =>
    handleUpdate({ update_id: ++uid, message: { chat: { type: "private" }, from, text, ...extra } }, deps);
  return { leads, codes, logins, msgs, sent, notes, asked, say, deps, next: () => ++uid };
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

// ---- Telegramni ulash ----
test("/start ulash_KOD: hisob ulanadi, kod manba sifatida saqlanmaydi, AI chaqirilmaydi", async () => {
  const t = setup();
  t.codes.set("ABC123", { user_id: "user-1", used: false });
  await t.say("/start ulash_ABC123");
  assert.equal(t.leads.get(7).linked_user_id, "user-1");
  assert.equal(t.leads.get(7).source, null);
  assert.equal(t.sent.at(-1).text, LINKED_TEXT);
  assert.equal(t.asked.length, 0);
  assert.match(LINKED_TEXT, /\/stop/);
});

test("ulash kodi bir marta ishlaydi: ulanmagan odamga 'eskirgan', allaqachon ulangan odamga tasdiq ko'rsatiladi", async () => {
  const t = setup();
  t.codes.set("OLD", { user_id: "user-2", used: false, expired: true });
  await t.say("/start ulash_OLD");                       // hali ulanmagan: xato
  assert.match(t.sent.at(-1).text, /eskirgan yoki allaqachon ishlatilgan/);
  t.codes.set("ONCE", { user_id: "user-1", used: false });
  await t.say("/start ulash_ONCE");
  assert.equal(t.leads.get(7).linked_user_id, "user-1");
  await t.say("/start ulash_ONCE");                      // ikkinchi bosish: ulangan, xato emas
  assert.equal(t.sent.at(-1).text, LINK_ALREADY);
  await t.say("/start ulash_YOQ");
  assert.equal(t.sent.at(-1).text, LINK_ALREADY);
  assert.equal(t.leads.get(7).linked_user_id, "user-1");
});

test("kirish havolasi ishlatilgan/eskirgan: ulangan odamga yumshoq xabar, ulanmaganga xato", async () => {
  const t = setup();
  await t.say("/start kirish_YOQ");
  assert.match(t.sent.at(-1).text, /eskirgan yoki ishlatilgan/);
  assert.notEqual(t.sent.at(-1).text, LOGIN_USED_LINKED);
  t.leads.get(7).linked_user_id = "user-1";
  await t.say("/start kirish_YOQ");
  assert.equal(t.sent.at(-1).text, LOGIN_USED_LINKED);
  assert.match(LOGIN_USED_LINKED, /hammasi joyida/);
});

test("bitta hisobga bitta Telegram: yangi ulash eskisini bo'shatadi", async () => {
  const t = setup();
  t.codes.set("A", { user_id: "user-1", used: false });
  t.codes.set("B", { user_id: "user-1", used: false });
  await t.say("/start ulash_A");
  await t.say("/start ulash_B", { id: 8, first_name: "Vali" });
  assert.equal(t.leads.get(7).linked_user_id, null);
  assert.equal(t.leads.get(8).linked_user_id, "user-1");
});

test("/stop eslatmalarni o'chiradi; ulangan o'quvchi uchun AI'ga sotmaslik eslatmasi qo'shiladi", async () => {
  const t = setup("Albatta, yordam beraman.");
  t.codes.set("A", { user_id: "user-1", used: false });
  await t.say("/start ulash_A");
  await t.say("Menga biror mavzuda yordam kerak");
  assert.equal(t.asked.at(-1).system, SYSTEM + LINKED_NOTE);
  await t.say("/stop");
  assert.equal(t.leads.get(7).remind, false);
  assert.equal(t.leads.get(7).stage, "stopped");
});

import { newCode, deepLink } from "../api/_tglink.js";
test("ulash kodi: 12 belgi, Telegram /start parametriga yaroqli; havola botga ochiladi", () => {
  for (let i = 0; i < 50; i++) assert.match(newCode(), /^[A-Za-z0-9_-]{12}$/);
  assert.notEqual(newCode(), newCode());
  assert.match(deepLink("XyZ123abc_-9"), /^https:\/\/t\.me\/[A-Za-z0-9_]+bot\?start=ulash_XyZ123abc_-9$/);
});

// ---- Telegram orqali kirish ----
test("/start kirish_KOD: telefon so'raladi (contact tugmasi), kod manba bo'lib saqlanmaydi", async () => {
  const t = setup();
  t.logins.set("L1", { user_id: null });
  await t.say("/start kirish_L1");
  assert.equal(t.leads.get(7).source, null);
  assert.equal(t.logins.get("L1").tg_id, 7);
  const kb = t.sent.at(-1).reply_markup.keyboard[0][0];
  assert.equal(kb.request_contact, true);
  assert.equal(t.asked.length, 0);
});

test("kontakt ulashilsa kirish tasdiqlanadi, telefon '+' bilan, ustozga xabar ketadi, klaviatura yopiladi", async () => {
  const t = setup();
  t.logins.set("L1", { user_id: null });
  await t.say("/start kirish_L1");
  await t.say(undefined, undefined, { contact: { user_id: 7, phone_number: "998901112233" } });
  assert.equal(t.logins.get("L1").user_id, "u-7");
  assert.equal(t.logins.get("L1").info.phone, "+998901112233");
  assert.equal(t.leads.get(7).linked_user_id, "u-7");
  assert.equal(t.sent.at(-1).text, LOGIN_DONE);
  assert.deepEqual(t.sent.at(-1).reply_markup, { remove_keyboard: true });
  assert.match(t.notes.at(-1), /Telegram orqali kirdi/);
  assert.match(t.notes.at(-1), /\+998901112233/);
});

test("boshqa odamning kontaktini yuborib kirib bo'lmaydi", async () => {
  const t = setup();
  t.logins.set("L1", { user_id: null });
  await t.say("/start kirish_L1");
  await t.say(undefined, undefined, { contact: { user_id: 999, phone_number: "998900000000" } });
  assert.equal(t.logins.get("L1").user_id, null);
  assert.match(t.sent.at(-1).text, /o'zingizning raqamingizni/);
});

test("kirish: eskirgan kod rad etiladi, kodsiz kontakt yuborilsa avval saytdagi tugma so'raladi", async () => {
  const t = setup();
  t.logins.set("OLD", { user_id: null, expired: true });
  await t.say("/start kirish_OLD");
  await t.say("/start kirish_YOQ");
  assert.equal(t.sent.filter((s) => /eskirgan yoki ishlatilgan/.test(s.text || "")).length, 2);
  await t.say(undefined, undefined, { contact: { user_id: 7, phone_number: "998900000000" } });
  assert.match(t.sent.at(-1).text, /Avval saytdagi/);
  assert.equal(t.logins.get("OLD").user_id, null);
});

import { tgEmail, isTgEmail, hashSecret, loginLink } from "../api/_tgauth.js";
test("Telegram hisob email'i, sir xeshi va kirish havolasi", () => {
  assert.equal(tgEmail(123456), "tg123456@example.com");
  assert.ok(isTgEmail("tg123456@example.com"));
  assert.ok(!isTgEmail("ali@example.com") && !isTgEmail("tg1@gmail.com") && !isTgEmail(null));
  assert.equal(hashSecret("abc"), hashSecret("abc"));
  assert.notEqual(hashSecret("abc"), hashSecret("abd"));
  assert.match(loginLink("XyZ123abc_-9"), /\?start=kirish_XyZ123abc_-9$/);
});

// ---- Telefon raqami matn bo'lib kelsa ----
test("isPhoneText: raqam shakllari ha, oddiy jumlalar va qisqa sonlar yo'q", () => {
  for (const ok of ["+998901112233", "998901112233", "90 111 22 33", "+998 (90) 111-22-33", "901112233"]) assert.equal(isPhoneText(ok), true, ok);
  for (const no of ["10 sinf, 22 noyabr", "22", "2026", "Premium 200 000 so'm", "men 998901112233 raqamdan yozyapman", "", "salom"]) assert.equal(isPhoneText(no), false, no);
});

test("raqam matn bo'lib kelsa va kirish jarayonda: tugma qayta chiqadi, AI chaqirilmaydi, 'qabul qilindi' deyilmaydi", async () => {
  const t = setup();
  t.logins.set("L1", { user_id: null });
  await t.say("/start kirish_L1");
  await t.say("+998901112233");
  const last = t.sent.at(-1);
  assert.equal(last.text, PHONE_TEXT_LOGIN);
  assert.equal(last.reply_markup.keyboard[0][0].request_contact, true);
  assert.equal(t.asked.length, 0);
  assert.doesNotMatch(last.text, /qabul qilindi/);
  assert.equal(t.logins.get("L1").user_id, null);        // matn orqali kirish ochilmaydi
  assert.equal(t.notes.length, 0);
});

test("raqam matn bo'lib kelsa va kirish jarayoni yo'q: saytdagi tugma tushuntiriladi, raqam ustozga yuboriladi", async () => {
  const t = setup();
  await t.say("/start");
  await t.say("+998 90 111 22 33");
  assert.equal(t.sent.at(-1).text, PHONE_TEXT_NOLOGIN);
  assert.match(PHONE_TEXT_NOLOGIN, /Telegram orqali kirish/);
  assert.equal(t.asked.length, 0);
  assert.equal(t.notes.length, 1);
  assert.match(t.notes[0], /\+998 90 111 22 33/);
  assert.match(t.notes[0], /raqam yozib qoldirdi/);
});

test("bilim hujjatida saytga kirish yo'li bor va 'raqamingiz qabul qilindi' deyish taqiqlangan", () => {
  assert.match(SYSTEM, /Telegram orqali kirish/);
  assert.match(SYSTEM, /Raqamni ulashish/);
  assert.match(SYSTEM, /oldin email bilan/i);
  assert.match(SYSTEM, /raqamingiz qabul qilindi" demang/);
});
