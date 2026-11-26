import test from "node:test";
import assert from "node:assert/strict";
import { sorovAjrat, yigishlar, tuzatishSorov, ochirishSorov, tekshir, toliqMatn, yigish, runKanal, tashkentKun, IMZO, KANAL } from "../api/_kanal.js";

const NOW = new Date("2026-11-20T15:00:00Z");           // Toshkentda 20:00, 20-noyabr

// kanal_postlar jadvalining xotiradagi nusxasi.
function fakeDb(rows, { failOn = null } = {}) {
  const from = () => {
    const q = { op: "select", filters: [], orders: [], limitN: Infinity };
    const run = () => {
      if (failOn === q.op) return { data: null, error: { message: "baza ishlamadi" } };
      const hit = rows.filter((r) => q.filters.every((f) => f(r)));
      if (q.op === "update") { hit.forEach((r) => Object.assign(r, q.patch)); return { data: hit.map((r) => ({ id: r.id })), error: null }; }
      const out = [...hit].sort((a, b) => { for (const k of q.orders) { if (a[k] < b[k]) return -1; if (a[k] > b[k]) return 1; } return 0; }).slice(0, q.limitN);
      return { data: out, error: null };
    };
    const api = {
      select() { return api; },
      update(patch) { q.op = "update"; q.patch = patch; return api; },
      eq(k, v) { q.filters.push((r) => r[k] === v); return api; },
      in(k, vs) { q.filters.push((r) => vs.includes(r[k])); return api; },
      gte(k, v) { q.filters.push((r) => r[k] != null && r[k] >= v); return api; },
      lte(k, v) { q.filters.push((r) => r[k] <= v); return api; },
      order(k) { q.orders.push(k); return api; },
      limit(n) { q.limitN = n; return api; },
      then(res, rej) { return Promise.resolve(run()).then(res, rej); },
    };
    return api;
  };
  return { from };
}
const post = (id, extra = {}) => ({ id, matn: `Post ${id}`, rasm_url: null, imzo: true, reja_kuni: "2026-11-20", holat: "tasdiqlangan", message_id: null, xato: null, sent_at: null, ...extra });
function setup(rows, reply = { ok: true, result: { message_id: 555 } }, dbOpt) {
  const sent = [], logs = [];
  const send = async (method, payload) => { sent.push({ method, payload }); return typeof reply === "function" ? reply() : reply; };
  const run = (now = NOW) => runKanal(fakeDb(rows, dbOpt), send, { now, log: async (y) => { logs.push(y); } });
  return { sent, logs, run };
}

test("tashkentKun: kun Toshkent vaqti bilan almashadi (UTC 19:00 = ertangi kun)", () => {
  assert.equal(tashkentKun(new Date("2026-11-20T18:59:00Z")), "2026-11-20");
  assert.equal(tashkentKun(new Date("2026-11-20T19:00:00Z")), "2026-11-21");
});

test("imzo: har post oxiriga bot, Telegram va Instagram havolalari qo'shiladi; imzosiz postda yo'q", () => {
  const t = toliqMatn({ matn: "  Salom  ", imzo: true });
  assert.ok(t.startsWith("Salom\n\n🤖"));
  assert.match(t, /start=kanal_post">Yordamchi bot<\/a>/);
  assert.match(t, /t\.me\/KimyogarBobur">Telegram<\/a> \| <a href="https:\/\/instagram\.com\/kimyogarbobur">Instagram<\/a>/);
  assert.equal(toliqMatn({ matn: "Salom", imzo: false }), "Salom");
  assert.deepEqual(tekshir({ matn: IMZO, reja_kuni: "2026-11-20", imzo: false }), []);     // imzoning o'zi yaroqli HTML
});

test("tekshir: yaroqli post xatosiz o'tadi", () => {
  assert.deepEqual(tekshir({ matn: `🧪 <b>Kun savoli</b>\n\nP₂O₅ da fosforning valentligi?\n<a href="https://t.me/KimyogarBobur">kanal</a> &amp; A &lt; B`, reja_kuni: "2026-11-20" }), []);
});

test("tekshir: bo'sh matn, noma'lum teg, yopilmagan teg, noto'g'ri havola, '&', sana", () => {
  const x = (p) => tekshir({ reja_kuni: "2026-11-20", ...p }).join(" | ");
  assert.match(x({ matn: "  " }), /bo'sh/);
  assert.match(x({ matn: "<div>salom</div>" }), /ruxsat etilmagan teg/);
  assert.match(x({ matn: "massa < 5 va hajm > 2" }), /ruxsat etilmagan teg/);       // "<" Telegramda xato beradi
  assert.match(x({ matn: "<b>qalin" }), /yopilmagan teg: <b>/);
  assert.match(x({ matn: "<b><i>x</b></i>" }), /noto'g'ri yopilgan/);
  assert.match(x({ matn: `<a href="t.me/x">havola</a>` }), /https/);
  assert.match(x({ matn: "tuz & suv" }), /&amp;/);
  assert.match(tekshir({ matn: "ok", reja_kuni: "20.11.2026" }).join(), /reja_kuni/);
  assert.match(tekshir({ matn: "ok" }).join(), /reja_kuni/);
  assert.match(tekshir({ matn: "ok", reja_kuni: "2026-11-20", rasm_url: "http://x.uz/a.jpg" }).join(), /rasm_url/);
});

test("tekshir: uzunlik imzo bilan birga sanaladi; rasmli postda chegara 1000", () => {
  assert.deepEqual(tekshir({ matn: "a".repeat(3800), reja_kuni: "2026-11-20" }), []);
  assert.match(tekshir({ matn: "a".repeat(3990), reja_kuni: "2026-11-20" }).join(), /matn uzun/);
  assert.match(tekshir({ matn: "a".repeat(990), reja_kuni: "2026-11-20", rasm_url: "https://x.uz/a.jpg" }).join(), /rasmli post/);
  assert.deepEqual(tekshir({ matn: "a".repeat(990), reja_kuni: "2026-11-20", rasm_url: "https://x.uz/a.jpg", imzo: false }), []);
});

test("yigish: matnli post sendMessage, rasmli post sendPhoto; HTML rejimi va kanal manzili", () => {
  const a = yigish(post(1));
  assert.equal(a.method, "sendMessage");
  assert.deepEqual({ chat: a.payload.chat_id, mode: a.payload.parse_mode, preview: a.payload.disable_web_page_preview }, { chat: KANAL, mode: "HTML", preview: true });
  assert.ok(a.payload.text.startsWith("Post 1\n\n"));
  const b = yigish(post(2, { rasm_url: "https://x.uz/a.jpg" }), "@sinov");
  assert.equal(b.method, "sendPhoto");
  assert.deepEqual({ chat: b.payload.chat_id, photo: b.payload.photo }, { chat: "@sinov", photo: "https://x.uz/a.jpg" });
  assert.ok(b.payload.caption.includes("Yordamchi bot"));
});

test("runKanal: reja kuni kelgan eng eski tasdiqlangan post yuboriladi, holat va xabar raqami yoziladi", async () => {
  const rows = [post(3, { reja_kuni: "2026-11-20" }), post(2, { reja_kuni: "2026-11-19" }), post(1, { reja_kuni: "2026-11-19", holat: "qoralama" }), post(4, { reja_kuni: "2026-11-21" })];
  const t = setup(rows);
  assert.deepEqual(await t.run(), { sent: 1, id: 2 });
  assert.equal(t.sent.length, 1);
  assert.ok(t.sent[0].payload.text.startsWith("Post 2"));
  const p2 = rows.find((r) => r.id === 2);
  assert.deepEqual({ holat: p2.holat, message_id: p2.message_id, sent_at: p2.sent_at }, { holat: "yuborildi", message_id: 555, sent_at: NOW.toISOString() });
  assert.deepEqual(rows.filter((r) => r.id !== 2).map((r) => r.holat), ["tasdiqlangan", "qoralama", "tasdiqlangan"]);
  assert.deepEqual({ agent: t.logs[0].agent, tur: t.logs[0].tur }, { agent: "kanal", tur: "ish" });
});

test("runKanal: tasdiqlanmagan (qoralama) post hech qachon yuborilmaydi", async () => {
  const rows = [post(1, { holat: "qoralama" }), post(2, { holat: "bekor" }), post(3, { holat: "xato" })];
  const t = setup(rows);
  assert.deepEqual(await t.run(), { sent: 0, sabab: "tasdiqlangan post yo'q" });
  assert.equal(t.sent.length, 0);
});

test("runKanal: reja kuni kelmagan post kutadi", async () => {
  const t = setup([post(1, { reja_kuni: "2026-11-21" })]);
  assert.equal((await t.run()).sent, 0);
  assert.equal(t.sent.length, 0);
  assert.equal((await t.run(new Date("2026-11-21T15:00:00Z"))).sent, 1);
});

test("runKanal: kuniga bitta. Bugun post chiqqan bo'lsa ikkinchisi ertaga qoladi; kron ikki marta ishlasa ham bitta ketadi", async () => {
  const rows = [post(1), post(2)];
  const t = setup(rows);
  assert.equal((await t.run()).id, 1);
  assert.deepEqual(await t.run(), { sent: 0, sabab: "bugun post chiqqan" });
  assert.equal(t.sent.length, 1);
  assert.equal(rows[1].holat, "tasdiqlangan");
  assert.deepEqual(await t.run(new Date("2026-11-21T15:00:00Z")), { sent: 1, id: 2 });
});

test("runKanal: kecha Toshkent vaqti bilan chiqqan post bugungi navbatni to'smaydi", async () => {
  const rows = [post(1, { holat: "yuborildi", sent_at: "2026-11-19T15:00:00Z" }), post(2)];
  assert.deepEqual(await setup(rows).run(), { sent: 1, id: 2 });
});

test("runKanal: Telegram rad etsa post 'xato' bo'ladi, sababi yoziladi, kod agentiga xabar tushadi va kun band bo'lmaydi", async () => {
  const rows = [post(1), post(2)];
  const t = setup(rows, { ok: false, description: "Forbidden: bot is not a member of the channel chat" });
  const r = await t.run();
  assert.deepEqual({ sent: r.sent, id: r.id }, { sent: 0, id: 1 });
  assert.deepEqual({ holat: rows[0].holat, sent_at: rows[0].sent_at }, { holat: "xato", sent_at: null });
  assert.match(rows[0].xato, /not a member/);
  assert.deepEqual({ tur: t.logs[0].tur, kimga: t.logs[0].kimga }, { tur: "xato", kimga: "kod" });
  assert.equal(rows[1].holat, "tasdiqlangan");            // xato post keyingisini o'zi bilan olib ketmaydi
});

test("runKanal: baza o'qilmasa xato yashirilmaydi va hech narsa yuborilmaydi", async () => {
  const t = setup([post(1)], undefined, { failOn: "select" });
  await assert.rejects(() => t.run(), /baza ishlamadi/);
  assert.equal(t.sent.length, 0);
});

test("runKanal: postni egallab bo'lmasa (yozish ishlamasa) yuborilmaydi", async () => {
  const t = setup([post(1)], undefined, { failOn: "update" });
  await assert.rejects(() => t.run(), /baza ishlamadi/);
  assert.equal(t.sent.length, 0);
});

test("tuzatishSorov va ochirishSorov: faqat kanalga chiqqan post uchun; rasmli postda rasm osti yozuvi tuzatiladi", () => {
  const post = { id: 3, matn: "Yangi <b>matn</b>", holat: "yuborildi", message_id: 77, imzo: false, rasm_url: null };
  assert.deepEqual(tuzatishSorov(post, "@k"), { method: "editMessageText", payload: { chat_id: "@k", message_id: 77, parse_mode: "HTML", text: "Yangi <b>matn</b>", disable_web_page_preview: true } });
  assert.equal(tuzatishSorov({ ...post, rasm_url: "https://x.uz/a.jpg" }, "@k").method, "editMessageCaption");
  assert.deepEqual(ochirishSorov(post, "@k"), { method: "deleteMessage", payload: { chat_id: "@k", message_id: 77 } });
  assert.throws(() => tuzatishSorov({ ...post, holat: "tasdiqlangan" }), /faqat kanalga chiqqan/);
  assert.throws(() => ochirishSorov({ ...post, message_id: null }), /faqat kanalga chiqqan/);
});

// ---- so'rovnoma (quiz) ----
const SOROV = `#sorov
Olmani kesib qo'ysangiz, bir necha daqiqada qorayadi. Nega?
A) Olma suvi bug'lanib ketadi
B) Olmadagi moddalar kislorod bilan oksidlanadi *
C) Olmaga chang qo'nadi
izoh: Kesilganda hujayralar buziladi, ichidagi moddalar havodagi kislorod bilan oksidlanadi.`;

test("so'rovnoma: savol, javoblar, to'g'ri javob va izoh ajratiladi; xatolar aytiladi", () => {
  const s = sorovAjrat(SOROV);
  assert.deepEqual({ savol: s.savol, n: s.variantlar.length, togri: s.togri, b: s.variantlar[1] }, { savol: "Olmani kesib qo'ysangiz, bir necha daqiqada qorayadi. Nega?", n: 3, togri: 1, b: "Olmadagi moddalar kislorod bilan oksidlanadi" });
  assert.equal(sorovAjrat("Oddiy post"), null);
  assert.deepEqual(tekshir({ matn: SOROV, reja_kuni: "2026-11-24" }), []);
  assert.match(tekshir({ matn: SOROV.replace(" *", ""), reja_kuni: "2026-11-24" }).join(), /to'g'ri javob bitta/);
  assert.match(tekshir({ matn: "#sorov\nSavol?\nA) bitta *", reja_kuni: "2026-11-24" }).join(), /2 tadan 10 tagacha/);
  assert.match(tekshir({ matn: SOROV.replace("Olmaga chang qo'nadi", "x".repeat(120)), reja_kuni: "2026-11-24" }).join(), /javob uzun/);
  assert.match(tekshir({ matn: SOROV + "y".repeat(200), reja_kuni: "2026-11-24" }).join(), /izoh uzun/);
});

test("so'rovnoma: rasm bo'lsa avval rasm, keyin quiz; kanalga ikkalasi chiqadi; tuzatib bo'lmaydi", async () => {
  const post = { id: 9, matn: SOROV, rasm_url: "https://x.uz/olma.png", imzo: true, reja_kuni: "2026-11-20", holat: "tasdiqlangan" };
  const q = yigishlar(post, "@k");
  assert.deepEqual(q.map((x) => x.method), ["sendPhoto", "sendPoll"]);
  assert.deepEqual({ type: q[1].payload.type, ok: q[1].payload.correct_option_id, opt: q[1].payload.options[0], izoh: /oksidlanadi/.test(q[1].payload.explanation) }, { type: "quiz", ok: 1, opt: { text: "Olma suvi bug'lanib ketadi" }, izoh: true });
  assert.deepEqual(yigishlar({ ...post, rasm_url: null }, "@k").map((x) => x.method), ["sendPoll"]);
  assert.equal(yigishlar({ matn: "Oddiy", imzo: false }, "@k").length, 1);
  const t = setup([post]);
  assert.deepEqual(await t.run(), { sent: 1, id: 9 });
  assert.deepEqual(t.sent.map((x) => x.method), ["sendPhoto", "sendPoll"]);
  assert.throws(() => tuzatishSorov({ ...post, holat: "yuborildi", message_id: 5 }), /so'rovnomani tuzatib bo'lmaydi/);
});

test("majbur: ustoz aytganda bugun ikkinchi post ham chiqadi, lekin tasdiqlanmagani baribir chiqmaydi", async () => {
  const bugun = { id: 1, matn: "Birinchi", rasm_url: null, imzo: true, reja_kuni: "2026-11-20", holat: "yuborildi", sent_at: NOW.toISOString() };
  const rows = [bugun, post(2), post(3, { holat: "qoralama" })];
  const sent = [];
  const send = async (method, payload) => { sent.push({ method, payload }); return { ok: true, result: { message_id: 7 } }; };
  assert.deepEqual(await runKanal(fakeDb(rows), send, { now: NOW, log: async () => {} }), { sent: 0, sabab: "bugun post chiqqan" });
  assert.deepEqual(await runKanal(fakeDb(rows), send, { now: NOW, log: async () => {}, majbur: true }), { sent: 1, id: 2 });
  assert.deepEqual(await runKanal(fakeDb(rows), send, { now: NOW, log: async () => {}, majbur: true }), { sent: 0, sabab: "tasdiqlangan post yo'q" });
});

test("kalitMos: faqat aynan bir xil va yetarlicha uzun kalit mos keladi", async () => {
  const { kalitMos } = await import("../api/_kanal.js");
  const k = "a".repeat(40);
  assert.equal(kalitMos(k, k), true);
  assert.equal(kalitMos(k, "a".repeat(39) + "b"), false);
  assert.equal(kalitMos("qisqa", "qisqa"), false);          // qisqa kalit qabul qilinmaydi
  assert.equal(kalitMos("", ""), false);
  assert.equal(kalitMos(k, undefined), false);               // jadval bo'sh
  assert.equal(kalitMos(undefined, k), false);
});
