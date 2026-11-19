import test from "node:test";
import assert from "node:assert/strict";
import { holat, xabar, collectMurabbiy, runMurabbiy, yakshanbami, KUN_ORALIQ, FAOLSIZ_KUN, ZAIF_MIN } from "../api/_murabbiy.js";

const NOW = new Date("2026-11-19T04:00:00Z");                    // payshanba, Toshkentda 09:00
const YAK = new Date("2026-11-22T04:00:00Z");                    // yakshanba
const kunOldin = (d, now = NOW) => new Date(now.getTime() - d * 86400e3).toISOString();
const kunKeyin = (d) => new Date(NOW.getTime() + d * 86400e3).toISOString();
const topics = [
  { id: "t1", name: "Proporsiya", sort_order: 5, bunny_video_id: "v1" },
  { id: "t2", name: "Reaksiya turlari", sort_order: 6, bunny_video_id: "v2" },
  { id: "t3", name: "Beqaror moddalar", sort_order: 8, bunny_video_id: null },
  { id: "t4", name: "Alkanlar", sort_order: 101, bunny_video_id: "v4" },
];
const examples = [1, 2, 3].map((n) => ({ id: `e${n}`, topic_id: "t1", example_number: n, bunny_video_id: n === 3 ? null : `ve${n}` }));
const st = (extra = {}) => ({ id: "s1", full_name: "Ali Valiyev", plan: "premium", plan_expires_at: kunKeyin(20), is_admin: false, ...extra });
const view = (kind, ref_id, d) => ({ student_id: "s1", kind, ref_id, last_at: kunOldin(d) });
const ans = (qid, ok, d = 1) => ({ student_id: "s1", question_id: qid, is_correct: ok, answered_at: kunOldin(d) });

test("holat: oxirgi ko'rilgan dars va keyingi qadam (Premium: shu mavzuning ko'rilmagan misoli)", () => {
  const h = holat(st(), { views: [view("topic", "t1", 5), view("example", "e1", 4)], topics, examples, now: NOW });
  assert.deepEqual(h.oxirgi, { mavzu: "Proporsiya", misol: 1 });
  assert.deepEqual(h.keyingi, { mavzu: "Proporsiya", misol: 2 });       // 3-misolning videosi yo'q
  assert.equal(h.faolsiz, 4);
});

test("holat: misollar tugasa yoki reja Standart bo'lsa keyingi videoli mavzu; videosiz mavzu taklif qilinmaydi", () => {
  const hammasi = [view("topic", "t1", 3), view("example", "e1", 2), view("example", "e2", 1)];
  assert.deepEqual(holat(st(), { views: hammasi, topics, examples, now: NOW }).keyingi, { mavzu: "Reaksiya turlari", misol: null });
  assert.deepEqual(holat(st({ plan: "standart" }), { views: [view("topic", "t1", 3)], topics, examples, now: NOW }).keyingi, { mavzu: "Reaksiya turlari", misol: null });
  assert.deepEqual(holat(st(), { views: [view("topic", "t2", 1)], topics, examples, now: NOW }).keyingi, { mavzu: "Alkanlar", misol: null });   // t3 videosiz
  assert.equal(holat(st(), { views: [view("topic", "t4", 1)], topics, examples, now: NOW }).keyingi, null);
});

test("holat: hali hech narsa ochmagan o'quvchi: faolsiz null, birinchi videoli mavzu taklif qilinadi", () => {
  const h = holat(st(), { topics, examples, now: NOW });
  assert.deepEqual([h.faolsiz, h.oxirgi, h.keyingi], [null, null, { mavzu: "Proporsiya", misol: null }]);
});

test("holat: qiyin mavzu faqat yetarli javob bo'lganda va 50% dan past bo'lsa; eski javoblar sanalmaydi", () => {
  const questions = new Map([["q1", { topic: "Proporsiya" }], ["q2", { topic: " reaksiya turlari " }], ["q3", { topic: "Elektroliz" }], ["q4", { topic: "" }]]);
  const answers = [
    ...Array.from({ length: ZAIF_MIN }, (_, i) => ans("q1", i < 2)),             // 2/6 = 33%
    ...Array.from({ length: ZAIF_MIN - 1 }, () => ans("q2", false)),             // javob kam
    ...Array.from({ length: 8 }, (_, i) => ans("q3", i < 3)),                    // 3/8 = 38%, darsi yo'q
    ...Array.from({ length: 10 }, () => ans("q4", false)),                       // mavzusi yozilmagan
    ...Array.from({ length: 10 }, () => ans("q2", false, 40)),                   // 30 kundan eski
  ];
  const h = holat(st(), { answers, topics, examples, questions, now: NOW });
  assert.deepEqual(h.zaif, [{ mavzu: "Proporsiya", soni: 6, foiz: 33, dars: true }, { mavzu: "Elektroliz", soni: 8, foiz: 38, dars: false }]);
  assert.deepEqual(h.hafta, { video: 0, savol: 29, togri: 5 });
});

const hBase = { oxirgi: null, keyingi: null, faolsiz: 0, zaif: [], hafta: { video: 0, savol: 0, togri: 0 }, rejaKun: 20 };

test("xabar: faol va muammosiz o'quvchiga oddiy kunda hech narsa yuborilmaydi", () => {
  assert.equal(xabar(st(), hBase), null);
  assert.equal(xabar(st(), { ...hBase, faolsiz: FAOLSIZ_KUN - 1 }), null);
  assert.equal(xabar(st(), hBase, { yakshanba: true }), null);                 // hafta bo'sh: maqtaydigan narsa yo'q
});

test("xabar: faolsiz o'quvchiga qayerda to'xtagani va keyingi qadam aytiladi", () => {
  const x = xabar(st(), { ...hBase, faolsiz: 5, oxirgi: { mavzu: "Proporsiya", misol: 1 }, keyingi: { mavzu: "Proporsiya", misol: 2 } });
  assert.equal(x.tur, "davom");
  assert.match(x.text, /^Assalomu alaykum, Ali! 5 kundan beri ko'rinmay qoldingiz\. Hammasi joyidami\?/);
  assert.match(x.text, /"Proporsiya" mavzusining 1-misoligacha yetib kelgan edingiz\. Keyingisi: "Proporsiya" mavzusining 2-misoli\./);
});

test("xabar: hali boshlamagan o'quvchiga boshlash taklifi; ismsiz o'quvchiga 'Salom!'", () => {
  const x = xabar(st({ full_name: "" }), { ...hBase, faolsiz: null, keyingi: { mavzu: "Proporsiya", misol: null } });
  assert.equal(x.tur, "boshlash");
  assert.match(x.text, /^Assalomu alaykum! Platformada hali birorta dars ochmabsiz\. "Proporsiya" mavzusidan boshlasangiz bo'ladi\./);
});

test("xabar: qiyin mavzu sonlar bilan, uyaltirmasdan; darsi bo'lsagina videoni qayta ko'rish taklif qilinadi", () => {
  const x = xabar(st(), { ...hBase, zaif: [{ mavzu: "Proporsiya", soni: 6, foiz: 33, dars: true }] });
  assert.equal(x.tur, "qiyin");
  assert.match(x.text, /"Proporsiya" mavzusidan 6 ta savol yechibsiz, 2 tasi to'g'ri chiqibdi\./);
  assert.match(x.text, /Dars videosini yana bir marta ko'rib/);
  assert.doesNotMatch(xabar(st(), { ...hBase, zaif: [{ mavzu: "Elektroliz", soni: 8, foiz: 38, dars: false }] }).text, /dars videosi/i);
});

test("xabar: reja muddati 3 kun ichida bir marta eslatiladi, bosimsiz; eslatilgan bo'lsa qayta emas", () => {
  const x = xabar(st(), { ...hBase, rejaKun: 3 });
  assert.equal(x.tur, "reja");
  assert.match(x.text, /Premium rejangiz 3 kundan keyin tugaydi\. Davom ettirish yoki to'xtatish o'zingizning ixtiyoringiz\./);
  assert.match(xabar(st({ plan: "standart" }), { ...hBase, rejaKun: 0 }).text, /Standart rejangiz bugun tugaydi/);
  assert.equal(xabar(st(), { ...hBase, rejaKun: 3 }, { eslatilgan: true }), null);
  assert.equal(xabar(st(), { ...hBase, rejaKun: 4 }), null);
  assert.equal(xabar(st(), { ...hBase, rejaKun: null }), null);
});

test("xabar: yakshanba kuni faol o'quvchiga haftalik natija", () => {
  const x = xabar(st(), { ...hBase, hafta: { video: 4, savol: 10, togri: 7 }, keyingi: { mavzu: "Alkanlar", misol: null } }, { yakshanba: true });
  assert.equal(x.tur, "hafta");
  assert.match(x.text, /Bu hafta 4 ta video ko'ribsiz, 10 ta savol yechibsiz \(70% to'g'ri\)\. Barakalla, shu tartibda davom eting\. Keyingi hafta uchun: "Alkanlar" mavzusi\./);
  assert.equal(xabar(st(), { ...hBase, hafta: { video: 4, savol: 0, togri: 0 } }), null);       // yakshanba emas
});

test("xabar: har bir xabarda /stop eslatiladi; va'da, uyaltirish va bosim so'zlari yo'q", () => {
  const hammasi = [
    xabar(st(), { ...hBase, rejaKun: 2 }), xabar(st(), { ...hBase, faolsiz: null }), xabar(st(), { ...hBase, faolsiz: 9 }),
    xabar(st(), { ...hBase, zaif: [{ mavzu: "X", soni: 6, foiz: 0, dars: true }] }), xabar(st(), { ...hBase, hafta: { video: 1, savol: 0, togri: 0 } }, { yakshanba: true }),
  ];
  for (const x of hammasi) {
    assert.match(x.text, /\/stop deb yozing\.$/);
    assert.doesNotMatch(x.text, /kafolat|albatta o'tasiz|100|shoshiling|oxirgi imkoniyat|chegirma|yomon|uyat|dangasa|oson mavzu|ko'pchilik|menga yozing/i);
    assert.ok(x.text.length < 600);
  }
});

test("yakshanbami: Toshkent vaqti bilan", () => {
  assert.equal(yakshanbami(YAK), true);
  assert.equal(yakshanbami(NOW), false);
});

// Bazaning xotiradagi nusxasi. ustunYoq: sotuv_leads da reja_eslatma ustuni hali yo'q holatini beradi.
function fakeDb(tables, { ustunYoq = false, yoq = [] } = {}) {
  const from = (name) => {
    const q = { op: "select", filters: [], cols: "" };
    const run = () => {
      if (yoq.includes(name)) return { data: null, error: { message: `relation ${name} does not exist` } };
      if (ustunYoq && name === "sotuv_leads" && (q.cols.includes("reja_eslatma") || (q.patch && "reja_eslatma" in q.patch))) return { data: null, error: { message: "column reja_eslatma does not exist" } };
      const hit = (tables[name] ||= []).filter((r) => q.filters.every((f) => f(r)));
      if (q.op === "update") { hit.forEach((r) => Object.assign(r, q.patch)); return { data: hit, error: null }; }
      return { data: hit, error: null };
    };
    const api = {
      select(c = "") { if (q.op === "select") q.cols = c; return api; }, order() { return api; }, limit() { return api; },
      update(patch) { q.op = "update"; q.patch = patch; return api; },
      eq(k, v) { q.filters.push((r) => r[k] === v); return api; },
      neq(k, v) { q.filters.push((r) => r[k] !== v); return api; },
      in(k, vs) { q.filters.push((r) => vs.includes(r[k])); return api; },
      then(res, rej) { return Promise.resolve(run()).then(res, rej); },
    };
    return api;
  };
  return { from, tables };
}
const lead = (tg_id, uid, extra = {}) => ({ tg_id, linked_user_id: uid, remind: true, last_nudge_at: null, reja_eslatma: null, ...extra });
const baza = (extra = {}) => ({
  profiles: [st({ id: "ali", full_name: "Ali" }), st({ id: "vali", full_name: "Vali" }), st({ id: "guli", full_name: "Guli" }), st({ id: "sami", full_name: "Sami" }), st({ id: "bepul", plan: "free" }), st({ id: "adm", is_admin: true }), st({ id: "eski", plan_expires_at: kunOldin(2) })],
  sotuv_leads: [lead(1, "ali"), lead(2, "vali", { remind: false }), lead(3, "guli", { last_nudge_at: kunOldin(KUN_ORALIQ - 1) })],
  video_views: ["ali", "vali", "guli", "sami"].map((id) => ({ student_id: id, kind: "topic", ref_id: "t1", last_at: kunOldin(6) })),
  answers: [], topics, topic_examples: examples, questions: [], ...extra,
});
function setup(tables, opt, reply = { ok: true }) {
  const db = fakeDb(tables, opt), sent = [], logs = [];
  const run = (now = NOW) => runMurabbiy(db, async (tg_id, text) => { sent.push({ tg_id, text }); return typeof reply === "function" ? reply(tg_id) : reply; }, { now, log: async (y) => { logs.push(y); } });
  return { db, sent, logs, run };
}

test("collectMurabbiy: faqat faol pullik o'quvchilar; ulanmagan, /stop qilgan va yaqinda xabar olganlar sababi bilan o'tkaziladi", async () => {
  const r = await collectMurabbiy(fakeDb(baza()), { now: NOW });
  assert.deepEqual(r.map((x) => [x.student.id, x.xabar?.tur, x.sabab]), [["ali", "davom", null], ["vali", "davom", "/stop qilgan"], ["guli", "davom", "yaqinda xabar yuborilgan"], ["sami", "davom", "Telegram ulanmagan"]]);
});

test("runMurabbiy: faqat ruxsat etilgan o'quvchiga yuboradi, vaqtini belgilaydi, navbatga kunlik bitta yozuv qo'yadi", async () => {
  const t = setup(baza());
  assert.deepEqual(await t.run(), { oquvchilar: 4, yuborildi: 1, xato: 0, turlar: { davom: 1 } });
  assert.deepEqual(t.sent.map((s) => s.tg_id), [1]);
  assert.match(t.sent[0].text, /^Assalomu alaykum, Ali! 6 kundan beri/);
  assert.equal(t.db.tables.sotuv_leads[0].last_nudge_at, NOW.toISOString());
  assert.deepEqual({ agent: t.logs[0].agent, tur: t.logs[0].tur, kalit: t.logs[0].kalit }, { agent: "murabbiy", tur: "hisobot", kalit: "murabbiy:2026-11-19" });
  assert.equal((await t.run(new Date(NOW.getTime() + 3600e3))).yuborildi, 0);          // kron qayta ishlasa ikkinchi xabar ketmaydi
  assert.equal(t.sent.length, 1);
  assert.equal((await t.run(new Date(NOW.getTime() + (KUN_ORALIQ + 0.1) * 86400e3))).yuborildi, 2);   // oraliq o'tgach yana (ali va guli)
});

test("runMurabbiy: reja eslatmasi shu muddat uchun bir marta; uzaytirilsa yangi muddatga yana bir marta", async () => {
  const tugash = kunKeyin(2);
  const tb = baza({ profiles: [st({ id: "ali", full_name: "Ali", plan_expires_at: tugash })], sotuv_leads: [lead(1, "ali")], video_views: [{ student_id: "ali", kind: "topic", ref_id: "t1", last_at: kunOldin(0.5) }] });
  const t = setup(tb);
  assert.deepEqual((await t.run()).turlar, { reja: 1 });
  assert.equal(tb.sotuv_leads[0].reja_eslatma, tugash);
  tb.sotuv_leads[0].last_nudge_at = null;                                           // oraliq o'tgan deb hisoblaymiz
  assert.equal((await t.run()).yuborildi, 0);                                        // shu muddat uchun eslatilgan
  tb.profiles[0].plan_expires_at = new Date(new Date(tugash).getTime() + 30 * 86400e3).toISOString();   // uzaytirdi
  assert.equal((await t.run()).yuborildi, 0);                                        // muddat uzoq: eslatma yo'q
  assert.equal((await t.run(new Date(NOW.getTime() + 30 * 86400e3))).turlar.reja, 1); // yangi muddat yaqinlashganda yana
});

test("runMurabbiy: reja_eslatma ustuni hali yo'q bo'lsa ham ulangan o'quvchilar ko'rinadi va xabar vaqti yoziladi", async () => {
  const tugash = kunKeyin(2);
  const tb = baza({ profiles: [st({ id: "ali", full_name: "Ali", plan_expires_at: tugash })], sotuv_leads: [{ tg_id: 1, linked_user_id: "ali", remind: true, last_nudge_at: null }], video_views: [] });
  const t = setup(tb, { ustunYoq: true });
  assert.deepEqual(await t.run(), { oquvchilar: 1, yuborildi: 1, xato: 0, turlar: { reja: 1 } });
  assert.equal(tb.sotuv_leads[0].last_nudge_at, NOW.toISOString());
  assert.equal((await t.run(new Date(NOW.getTime() + 3600e3))).yuborildi, 0);
});

test("runMurabbiy: Telegram yubora olmasa vaqt belgilanmaydi va xato navbatga kod agenti uchun yoziladi", async () => {
  const t = setup(baza(), undefined, { ok: false });
  assert.deepEqual(await t.run(), { oquvchilar: 4, yuborildi: 0, xato: 1, turlar: {} });
  assert.equal(t.db.tables.sotuv_leads[0].last_nudge_at, null);
  assert.deepEqual({ tur: t.logs[0].tur, kimga: t.logs[0].kimga }, { tur: "xato", kimga: "kod" });
});

test("runMurabbiy: pullik o'quvchi yo'q bo'lsa yoki xabar kerak bo'lmasa navbatga hech narsa yozilmaydi", async () => {
  const t = setup(baza({ profiles: [st({ id: "bepul", plan: "free" })] }));
  assert.deepEqual(await t.run(), { oquvchilar: 0, yuborildi: 0, xato: 0, turlar: {} });
  assert.equal(t.logs.length, 0);
});

test("runMurabbiy: asosiy jadval o'qilmasa xato yashirilmaydi va hech kimga yozilmaydi", async () => {
  const t = setup(baza(), { yoq: ["video_views"] });
  await assert.rejects(() => t.run(), /video_views does not exist/);
  assert.equal(t.sent.length, 0);
});
