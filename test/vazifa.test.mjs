import test from "node:test";
import assert from "node:assert/strict";
import { analogSavol, variantlarniAjrat, tanla, javobTozala, bahola, holat, tekshir, xabarMatni, oquvchiSavol, oquvchiAmal, adminAmal, vazifaEslatma, vazifaTugma, vazifaMatn, javobHarflari, SONI_MAX } from "../api/_vazifa.js";

const NOW = new Date("2026-11-20T10:00:00Z");
// Soxta baza: jadvallar oddiy massiv; so'rovlar filtrlanadi, insert id beradi, update/upsert qatorlarni o'zgartiradi.
function fakeDb(tables) {
  const seq = {};
  const from = (name) => {
    const rows = (tables[name] ||= []), q = { op: "select", f: [] };
    const hit = () => rows.filter((r) => q.f.every((f) => f(r)));
    const run = () => {
      if (q.op === "insert") { const add = (Array.isArray(q.val) ? q.val : [q.val]).map((r) => ({ id: (seq[name] = (seq[name] || rows.length) + 1), holat: name === "vazifa_topshiriq" ? "berilgan" : undefined, javoblar: name === "vazifa_topshiriq" ? {} : undefined, ...r })); rows.push(...add); return { data: add, error: null }; }
      if (q.op === "upsert") { for (const r of q.val) { const i = rows.findIndex((x) => x.student_id === r.student_id && x.question_id === r.question_id); if (i >= 0) rows[i] = { ...rows[i], ...r }; else rows.push(r); } return { data: q.val, error: null }; }
      if (q.op === "update") { const h = hit(); h.forEach((r) => Object.assign(r, q.val)); return { data: h, error: null }; }
      return { data: hit(), error: null };
    };
    const api = {
      select() { return api; }, limit() { return api; }, order() { return api; },
      insert(v) { q.op = "insert"; q.val = v; return api; }, update(v) { q.op = "update"; q.val = v; return api; }, upsert(v) { q.op = "upsert"; q.val = v; return api; },
      eq(k, v) { q.f.push((r) => r[k] === v); return api; }, neq(k, v) { q.f.push((r) => r[k] !== v); return api; },
      in(k, vs) { q.f.push((r) => vs.includes(r[k])); return api; }, not(k) { q.f.push((r) => r[k] != null); return api; },
      gt(k, v) { q.f.push((r) => r[k] > v); return api; }, lt(k, v) { q.f.push((r) => r[k] < v); return api; },
      then(a, b) { return Promise.resolve(run()).then(a, b); },
    };
    return api;
  };
  return { from, tables };
}
const Q = (id, correct = "B") => ({ id, question_text: `Savol ${id}`, formula: "", option_a: "1", option_b: "2", option_c: "3", option_d: "4", correct_option: correct, question_type: "mcq" });
// Analog yozuvi bazadagidek: savol "shart A) ..; B) ..", javob "C) ...".
const A = (id, question_id, harf, extra = {}) => ({ id, question_id, savol: `Savol ${id} A) 1; B) 2; C) 3; D) 4`, formula: "", javob: `${harf}) ${" 1234"["ABCD".indexOf(harf) + 1]}`, is_approved: true, ...extra });
const baza = () => ({
  // q1..q4 birinchi variantning savollari, ularning analoglari a1..a4; a5 tasdiqlanmagan, a6 variantlarsiz
  questions: ["s1", "s2", "s3", "s4", "s5", "s6"].map((id) => ({ id, variant_id: "v1" })),
  analog_questions: [A("q1", "s1", "A"), A("q2", "s2", "B"), A("q3", "s3", "C"), A("q4", "s4", "D"), A("a5", "s5", "A", { is_approved: false }), A("a6", "s6", "A", { savol: "Variantsiz savol" })],
  topic_examples: [{ id: "e1", topic_id: "t-mol" }], topic_example_analogs: [{ example_id: "e1", analog_savol: "Mol savoli A) 1; B) 2; C) 3; D) 4", analog_javob: "A) 1" }],
  topics: [{ id: "t-mol", name: "Mol", sort_order: 1 }, { id: "t-bosh", name: "Bo'sh mavzu", sort_order: 2 }],
  variants: [{ id: "v1", teacher_id: "t1", variant_number: 2 }], teachers: [{ id: "t1", name: "DTM 2019" }],
  profiles: [{ id: "ali", full_name: "Ali Valiyev", plan: "premium" }, { id: "vali", full_name: "Vali", plan: "premium" }, { id: "guli", full_name: "Guli", plan: "free" }, { id: "adm", full_name: "Ustoz", is_admin: true }],
  sotuv_leads: [{ tg_id: 1, linked_user_id: "ali", remind: true }, { tg_id: 2, linked_user_id: "vali", remind: false }],
  vazifalar: [], vazifa_topshiriq: [], answers: [],
});
const yarat = async (db, extra = {}, sent = [], dep = {}) => adminAmal(db, "adm", { amal: "yarat", nom: "pH vazifasi", variantlar: ["v1"], manba_nom: "DTM 2019, 2-variant", soni: 3, kun: 2, oquvchilar: ["ali", "vali", "guli", "adm"], ...extra },
  { now: NOW, rnd: () => 0.999, send: async (tg_id, text, markup) => { sent.push({ tg_id, text, markup }); return { ok: true }; }, log: async () => {}, site: "https://sayt.uz", sendDoc: null, pdf: async () => Buffer.from("pdf"), ...dep });

test("analogSavol: matndan shart, to'rt javob va kalit harfi ajratiladi; ajralmasa savol ishlatilmaydi", () => {
  assert.deepEqual(variantlarniAjrat("Qaysi sinf? A) aldegidlar; B) kislotalar; C) spirtlar; D) efirlar"), { stem: "Qaysi sinf?", opts: { A: "aldegidlar", B: "kislotalar", C: "spirtlar", D: "efirlar" } });
  const q = analogSavol({ id: "x", savol: "Qaysi sinf? A) aldegidlar; B) kislotalar; C) spirtlar; D) efirlar", javob: "C) spirtlar" });
  assert.deepEqual({ t: q.question_text, c: q.option_c, k: q.correct_option }, { t: "Qaysi sinf?", c: "spirtlar", k: "C" });
  assert.equal(analogSavol({ id: "x", savol: "Variantsiz savol", javob: "C) x" }), null);
  assert.equal(analogSavol({ id: "x", savol: "S A) 1; B) 2; C) 3; D) 4", javob: "42" }), null);
  assert.deepEqual(tanla([1, 2, 3, 4], 2, () => 0.999), [1, 2]);
  assert.equal(tanla([1, 2], 5).length, 2);
});

test("bahola va javobTozala: begona savol va noto'g'ri harf tashlanadi, javobsiz savol xato", () => {
  const j = javobTozala({ q1: "a", q2: "Z", begona: "A" }, ["q1", "q2"]);
  assert.deepEqual(j, { q1: "A" });
  const n = bahola([Q("q1", "A"), Q("q2", "B")], j);
  assert.deepEqual({ togri: n.togri, jami: n.jami }, { togri: 1, jami: 2 });
  assert.deepEqual(n.tafsil[1], { id: "q2", tanlangan: null, togri_javob: "B", togri: false });
  assert.equal("correct_option" in oquvchiSavol(Q("q1")), false);
});

test("tekshir: nom, mavzu, son va o'quvchi shart; muddat kun oxiriga qo'yiladi", () => {
  assert.match(tekshir({ nom: "a" }).xato, /nomini/);
  assert.match(tekshir({ nom: "ab", soni: 5, oquvchilar: ["x"] }).xato, /Variant yoki mavzuni/);
  assert.deepEqual(tekshir({ nom: "ab", mavzular: ["t1", "t2", "t1"], soni: 5, oquvchilar: ["x"] }, NOW).mavzular, ["t1", "t2"]);
  assert.match(tekshir({ nom: "ab", variantlar: ["v1"], soni: SONI_MAX + 1, oquvchilar: ["x"] }).xato, /Savollar soni/);
  assert.match(tekshir({ nom: "ab", variantlar: ["v1"], soni: 5, oquvchilar: [] }).xato, /o'quvchini/);
  const t = tekshir({ nom: "ab", variantlar: ["v1"], soni: 5, kun: 2, oquvchilar: ["x", "x"] }, NOW);
  assert.equal(t.muddat, "2026-11-22T18:59:00.000Z");          // 22-noyabr 23:59 Toshkent
  assert.deepEqual(t.oquvchilar, ["x"]);
  assert.equal(tekshir({ nom: "ab", variantlar: ["v1"], soni: 5, oquvchilar: ["x"] }, NOW).muddat, null);
});

test("yarat: vazifa va topshiriqlar yoziladi, boshqa admin kirmaydi, Telegram faqat ulangan va /stop demaganga", async () => {
  const db = fakeDb(baza()), sent = [];
  const r = await yarat(db, {}, sent);
  assert.deepEqual(r.body, { ok: true, id: 1, oquvchilar: 4, yuborildi: 1, yetmadi: 0, xabarsiz: 3 });      // tayinlagan adminning o'zi ham kiradi (sinov uchun)
  assert.deepEqual(db.tables.vazifalar[0].savollar, ["q1", "q2", "q3"]);
  assert.deepEqual(db.tables.vazifa_topshiriq.map((t) => t.student_id), ["ali", "vali", "guli", "adm"]);
  assert.deepEqual(sent.map((s) => s.tg_id), [1]);
  assert.match(sent[0].text, /^Assalomu alaykum, Ali! Yangi uyga vazifa: "pH vazifasi", 3 ta savol\. Muddati: 22\.11\.2026 gacha\./);
  assert.deepEqual(sent[0].markup.inline_keyboard, [[{ text: "✍️ Javoblarni qanday yuboraman?", callback_data: "vz:b:1" }], [{ text: "Saytda ochish", url: "https://sayt.uz/#vazifa" }]]);
  assert.ok(db.tables.vazifa_topshiriq[0].tg_xabar_at && !db.tables.vazifa_topshiriq[1].tg_xabar_at);
});

test("yarat: mavzuda savol yetmasa rad etadi va hech narsa yozmaydi", async () => {
  const db = fakeDb(baza());
  const r = await yarat(db, { soni: 9 });
  assert.equal(r.status, 400);
  assert.match(r.body.error, /faqat 4 ta analog savol/);          // tasdiqlanmagan va variantsiz analoglar sanalmaydi
  assert.equal(db.tables.vazifalar.length, 0);
});

test("yarat: variant va dars mavzusi analoglari birga olinadi; begona manbada savol yo'q", async () => {
  const db = fakeDb(baza());
  const a = await yarat(db, { mavzular: ["t-mol"], soni: 5, manba_nom: "Aralash" });
  assert.equal(a.status, 200);
  assert.deepEqual({ n: db.tables.vazifalar[0].savollar.length, e1: db.tables.vazifalar[0].savollar.includes("e1"), mavzu: db.tables.vazifalar[0].mavzu }, { n: 5, e1: true, mavzu: "Aralash" });
  assert.equal((await yarat(db, { variantlar: ["yoq"], soni: 1 })).status, 400);
  const ol = await oquvchiAmal(db, "ali", { action: "vazifa-ol", id: 1 }, { now: NOW });
  assert.equal(ol.body.savollar.length, 5);                       // dars analogi ham savol bo'lib keladi
});

test("o'quvchi: ro'yxat, savollar kalitsiz, saqlash, topshirish va natija; ikkinchi marta topshirib bo'lmaydi", async () => {
  const db = fakeDb(baza());
  await yarat(db);
  const am = (action, extra = {}, who = "ali") => oquvchiAmal(db, who, { action, id: 1, ...extra }, { now: NOW });
  const ro = await am("vazifa-royxat");
  assert.deepEqual({ n: ro.body.vazifalar.length, holat: ro.body.vazifalar[0].holat, soni: ro.body.vazifalar[0].soni }, { n: 1, holat: "yangi", soni: 3 });
  const ol = await am("vazifa-ol");
  assert.equal(ol.body.savollar.length, 3);
  assert.equal(JSON.stringify(ol.body).includes("correct_option"), false);
  assert.equal(ol.body.natija, undefined);
  await am("vazifa-saqla", { javoblar: { q1: "A" } });
  assert.equal((await am("vazifa-royxat")).body.vazifalar[0].holat, "jarayonda");
  const tp = await am("vazifa-topshir", { javoblar: { q1: "A", q2: "C", q3: "C" } });
  assert.deepEqual({ togri: tp.body.natija.togri, jami: tp.body.natija.jami }, { togri: 2, jami: 3 });
  assert.equal(db.tables.answers.length, 0);                                 // analog javoblari umumiy statistikaga yozilmaydi
  assert.equal((await am("vazifa-topshir", { javoblar: { q1: "B" } })).status, 409);
  const keyin = await am("vazifa-ol");
  assert.equal(keyin.body.natija.tafsil[1].togri_javob, "B");               // topshirgach kalit ko'rinadi
  assert.equal((await am("vazifa-ol", {}, "begona")).status, 404);          // berilmagan o'quvchi ko'rmaydi
  assert.equal((await am("vazifa-royxat", {}, "vali")).body.vazifalar[0].holat, "yangi");
});

test("admin: malumot mavzularni va o'quvchilarni beradi; natija kim bajarganini ko'rsatadi", async () => {
  const db = fakeDb(baza());
  await yarat(db);
  await oquvchiAmal(db, "ali", { action: "vazifa-topshir", id: 1, javoblar: { q1: "A", q2: "B", q3: "C" } }, { now: NOW });
  const m = await adminAmal(db, "adm", { amal: "malumot" }, { now: NOW, send: null });
  assert.deepEqual(m.body.mavzular, [{ id: "t-mol", nom: "Mol", soni: 1 }]);          // analogi yo'q mavzu ko'rinmaydi
  assert.deepEqual(m.body.variantlar, [{ id: "v1", nom: "DTM 2019, 2-variant", soni: 4 }]);
  assert.deepEqual(m.body.oquvchilar.map((o) => [o.ism, o.telegram]), [["Ustoz", "yo'q"], ["Ali Valiyev", "ulangan"], ["Vali", "o'chirgan"], ["Guli", "yo'q"]]);
  assert.equal(m.body.oquvchilar[0].oz, true);
  assert.equal((await adminAmal(db, "boshqa-admin", { amal: "malumot" }, { now: NOW, send: null })).body.oquvchilar.some((o) => o.ism === "Ustoz"), false);
  assert.deepEqual({ berilgan: m.body.vazifalar[0].berilgan, bajargan: m.body.vazifalar[0].bajargan, ortacha: m.body.vazifalar[0].ortacha }, { berilgan: 4, bajargan: 1, ortacha: 100 });
  const n = await adminAmal(db, "adm", { amal: "natija", id: 1 }, { now: NOW, send: null });
  assert.deepEqual(n.body.oquvchilar.map((o) => [o.ism, o.holat, o.togri]), [["Ali Valiyev", "bajarildi", 3], ["Guli", "yangi", null], ["Ustoz", "yangi", null], ["Vali", "yangi", null]]);
});

test("holat: muddat o'tsa kechikkan; eslatma muddatga yaqin, topshirmagan va ulangan o'quvchiga bir marta", async () => {
  assert.equal(holat({ muddat: "2026-11-19T00:00:00Z" }, { holat: "berilgan" }, NOW), "kechikkan");
  assert.equal(holat({ muddat: "2026-11-19T00:00:00Z" }, { holat: "topshirilgan" }, NOW), "bajarildi");
  const db = fakeDb(baza()), sent = [];
  await yarat(db, { kun: 1 });                                   // muddat 21-noyabr 23:59 Toshkent
  const send = async (tg_id, text) => { sent.push({ tg_id, text }); return { ok: true }; };
  assert.deepEqual(await vazifaEslatma(db, send, { now: NOW }), { yuborildi: 1 });   // 33 soat qoldi
  assert.match(sent[0].text, /"pH vazifasi" vazifasining muddati 21\.11\.2026 da tugaydi/);
  assert.deepEqual(await vazifaEslatma(db, send, { now: NOW }), { yuborildi: 0 });   // ikkinchi marta yo'q
  assert.match(xabarMatni({ tur: "imtihon", nom: "X", savollar: [1, 2], muddat: null }, {}), /^Assalomu alaykum! Sizga imtihon tayinlandi: "X", 2 ta savol\./);
});

// ---- yordamchi bot ichida ishlash ----
function bot(db, dep = {}) {
  const out = [];
  const send = async (method, payload) => { out.push({ method, ...payload }); return { ok: true }; };
  const bos = (data, from = 1, message = { chat: { id: from }, message_id: 50 }) => vazifaTugma(db, send, { id: "cq", data, from: { id: from }, message }, { now: NOW, site: "https://sayt.uz", sendDoc: null, pdf: async () => Buffer.from("pdf"), ...dep });
  return { out, bos, oxirgi: () => out[out.length - 1] };
}

test("bot (PDF'siz zaxira rejim): savol matni xabarda, javobdan keyin hukm, oxirida vazifa topshiriladi va natija yoziladi", async () => {
  const db = fakeDb(baza());
  await yarat(db);                                              // ali (tg 1) ga 3 ta savol: q1 A, q2 B, q3 C
  const b = bot(db);
  await b.bos("vz:b:1");
  assert.deepEqual({ m: b.oxirgi().method, n: /1\/3/.test(b.oxirgi().text), tugma: b.oxirgi().reply_markup.inline_keyboard[0].map((x) => x.callback_data) },
    { m: "sendMessage", n: true, tugma: ["vz:a:1:0:A:m", "vz:a:1:0:B:m", "vz:a:1:0:C:m", "vz:a:1:0:D:m"] });
  assert.match(b.oxirgi().text, /Savol q1/);                    // PDF yuborilmagan: savol matni shu yerda
  assert.equal(JSON.stringify(b.out).includes("correct_option"), false);
  await b.bos("vz:a:1:0:A:m");
  assert.deepEqual({ m: b.oxirgi().method, ok: /✅/.test(b.oxirgi().text), keyingi: b.oxirgi().reply_markup.inline_keyboard[0][0].callback_data }, { m: "editMessageText", ok: true, keyingi: "vz:n:1:m" });
  await b.bos("vz:a:1:0:B");                                    // ikkinchi marta bosish o'tmaydi
  assert.match(b.oxirgi().text, /allaqachon javob berilgan/);
  await b.bos("vz:n:1");
  assert.deepEqual({ m: b.oxirgi().method, n: /2\/3/.test(b.oxirgi().text) }, { m: "editMessageText", n: true });
  await b.bos("vz:a:1:1:D");
  assert.match(b.oxirgi().text, /❌ <b>Noto'g'ri\.<\/b> To'g'ri javob: <b>B\)<\/b> 2/);
  await b.bos("vz:n:1"); await b.bos("vz:a:1:2:C");
  assert.match(b.oxirgi().text, /Vazifa topshirildi: 2 \/ 3/);
  const t = db.tables.vazifa_topshiriq.find((x) => x.student_id === "ali");
  assert.deepEqual({ holat: t.holat, togri: t.togri, jami: t.jami }, { holat: "topshirilgan", togri: 2, jami: 3 });
  await b.bos("vz:b:1");
  assert.match(b.oxirgi().text, /topshirilgan: 2 \/ 3/);
});

test("bot: ulanmagan odam, begona vazifa va imtihon rad etiladi; botda berilgan javob saytda o'zgarmaydi", async () => {
  const db = fakeDb(baza());
  await yarat(db);
  await yarat(db, { tur: "imtihon", nom: "Imtihon" });
  const b = bot(db);
  await b.bos("vz:b:1", 999);
  assert.match(b.oxirgi().text, /Telegramni hisobingizga ulang/);
  await b.bos("vz:b:77");
  assert.match(b.oxirgi().text, /topilmadi/);
  await b.bos("vz:b:2");
  assert.match(b.oxirgi().text, /Imtihon saytda ishlanadi/);
  await b.bos("vz:b:1"); await b.bos("vz:a:1:0:D");            // q1 ga botda xato javob (to'g'risi A)
  const ol = await oquvchiAmal(db, "ali", { action: "vazifa-ol", id: 1 }, { now: NOW });
  assert.deepEqual({ qulf: ol.body.qulf, javoblar: ol.body.javoblar }, { qulf: true, javoblar: { q1: "D" } });
  const tp = await oquvchiAmal(db, "ali", { action: "vazifa-topshir", id: 1, javoblar: { q1: "A", q2: "B", q3: "C" } }, { now: NOW });
  assert.deepEqual({ togri: tp.body.natija.togri, q1: tp.body.natija.tafsil[0].tanlangan }, { togri: 2, q1: "D" });      // saytda to'g'rilab bo'lmadi
  assert.equal((await oquvchiAmal(db, "ali", { action: "vazifa-royxat" }, { now: NOW })).body.vazifalar.find((x) => x.id === 1).javob_berilgan, 3);
});

test("PDF: uyga vazifa dizaynli fayl bo'lib ketadi (matn fayl ostida), ikkinchi o'quvchiga fayl qayta yuklanmaydi; imtihon oddiy xabar", async () => {
  const tb = baza(); tb.sotuv_leads[1].remind = true;           // vali ham xabar oladi
  const db = fakeDb(tb), sent = [], docs = [];
  const sendDoc = async (chat_id, d) => { docs.push({ chat_id, ...d }); return { ok: true, result: { document: { file_id: "F1" } } }; };
  const r = await yarat(db, {}, sent, { sendDoc });
  assert.deepEqual({ yuborildi: r.body.yuborildi, matnXabar: sent.length, fayl: docs.length }, { yuborildi: 2, matnXabar: 0, fayl: 2 });
  assert.deepEqual({ yuklandi: !!docs[0].buffer, nom: docs[0].filename, qayta: docs[1].file_id, tugma: docs[0].reply_markup.inline_keyboard[0][0].callback_data }, { yuklandi: true, nom: "pH_vazifasi.pdf", qayta: "F1", tugma: "vz:b:1" });
  assert.match(docs[0].caption, /Savollar shu fayl ichida\. Ishlab bo'lgach, javoblarni shu yerga bitta xabar qilib yozing, masalan: ABC \(3 ta harf\)/);
  await yarat(db, { tur: "imtihon", nom: "Imtihon" }, sent, { sendDoc });
  assert.deepEqual({ matnXabar: sent.length, fayl: docs.length }, { matnXabar: 2, fayl: 2 });          // imtihonga PDF yuborilmaydi
  const yiq = await yarat(fakeDb(baza()), {}, sent, { sendDoc, pdf: async () => { throw new Error("shrift yo'q"); } });
  assert.equal(yiq.body.yuborildi, 1);                          // PDF yasalmasa oddiy xabar ketadi
});

test("javobHarflari: turli yozilishlar o'tadi, oddiy gap esa javob emas", () => {
  assert.equal(javobHarflari("ABCDABCDAB"), "ABCDABCDAB");
  assert.equal(javobHarflari("a b c d"), "ABCD");
  assert.equal(javobHarflari("1A 2B 3C"), "ABC");
  assert.equal(javobHarflari("1-a, 2-b, 3-d"), "ABD");
  assert.equal(javobHarflari("АВСД"), "ABCD");                   // kirill harflar
  for (const t of ["Salom", "A", "Bu savolda xato bor", "ABCE", "narxi qancha"]) assert.equal(javobHarflari(t), null);
});

test("bot (PDF rejimi): javoblar bitta xabarda yoziladi, tasdiqdan keyin topshiriladi va har savol natijasi chiqadi", async () => {
  const db = fakeDb(baza());
  await yarat(db);                                              // ali (tg 1): q1 A, q2 B, q3 C
  const b = bot(db, { sendDoc: async () => ({ ok: true }) });
  const yoz = (text, from = 1) => vazifaMatn(db, async (method, payload) => { b.out.push({ method, ...payload }); return { ok: true }; }, { text, from: { id: from }, chat: { id: from } }, { now: NOW });
  await b.bos("vz:b:1", 1, { chat: { id: 1 }, message_id: 9, document: { file_id: "F" } });
  assert.match(b.oxirgi().text, /bitta xabar qilib yozing\. 3 ta harf/);          // tugma faqat yo'riqnoma beradi
  assert.equal(await yoz("Assalomu alaykum, savolim bor"), false);                 // oddiy gap: yordamchi botga o'tadi
  assert.equal(await yoz("ABCD"), true);                                          // soni mos emas
  assert.match(b.oxirgi().text, /3 ta savol bor, siz 4 ta javob yozdingiz/);
  assert.equal(await yoz("a b d"), true);
  assert.match(b.oxirgi().text, /1-A  2-B  3-D/);
  assert.deepEqual(b.oxirgi().reply_markup.inline_keyboard.map((r) => r[0].callback_data), ["vz:t:1:ABD", "vz:q:1"]);
  assert.equal(db.tables.vazifa_topshiriq[0].holat, "berilgan");                   // tasdiqlanmaguncha topshirilmaydi
  await b.bos("vz:t:1:ABD");
  assert.match(b.oxirgi().text, /Natija: 2 \/ 3[\s\S]*1\. ✅ A\n2\. ✅ B\n3\. ❌ D \(to'g'ri: C\)/);
  const t = db.tables.vazifa_topshiriq[0];
  assert.deepEqual({ holat: t.holat, togri: t.togri, qulf: t.javoblar._bot }, { holat: "topshirilgan", togri: 2, qulf: true });
  assert.equal(await yoz("ABC"), false);                                          // ochiq vazifa qolmadi: oddiy xabar
  await b.bos("vz:t:1:ABC");
  assert.match(b.oxirgi().text, /topshirilgan/);
  assert.equal(await yoz("ABC", 999), false);                                     // ulanmagan odam
});

test("bot: eslatmadagi tugmadan boshlansa avval PDF keladi; qayta yozish tugmasi yo'riqnomani beradi", async () => {
  const db = fakeDb(baza()), docs = [];
  await yarat(db);
  const e = bot(db, { sendDoc: async (chat_id, d) => { docs.push(d); return { ok: true }; } });
  await e.bos("vz:b:1");                                        // oddiy xabar (eslatma) ostidagi tugma
  assert.equal(docs.length, 1);
  assert.match(e.oxirgi().text, /bitta xabar qilib yozing/);
  await e.bos("vz:q:1");
  assert.match(e.oxirgi().text, /qaytadan yozing/);
  await e.bos("vz:t:1:AB");
  assert.match(e.oxirgi().text, /to'liq emas/);
});
