import test from "node:test";
import assert from "node:assert/strict";
import { topKamchilik, formatTekshiruv, runTekshiruv, bunnyRoyxat, TOLOV_SOAT, ESKI_XATO_KUN } from "../api/_tekshiruv.js";

const NOW = new Date("2026-11-20T04:00:00Z");
const soat = (h) => new Date(NOW.getTime() - h * 3600e3).toISOString();
const kodlar = (k) => k.map((x) => x.kod);
const toza = {
  topics: [{ id: "t1", name: "Alkanlar", bunny_video_id: "v1" }],
  examples: [{ id: "e1", topic_id: "t1", example_number: 1, bunny_video_id: "v2" }],
  transcripts: [{ topic_id: "t1", example_id: null }, { topic_id: null, example_id: "e1" }],
  variants: [{ id: "var1", variant_number: 1 }],
  questions: [{ variant_id: "var1", question_number: 1, bunny_video_id: "v3", correct_option: "A", correct_answer_text: null }],
};

test("hammasi joyida bo'lsa kamchilik yo'q", () => {
  assert.deepEqual(topKamchilik({ ...toza, now: NOW }), []);
  assert.deepEqual(topKamchilik({ now: NOW }), []);
});

test("mavzu: videosi yo'q, matni yo'q, misol matni yo'q alohida ushlanadi va platforma agentiga beriladi", () => {
  const k = topKamchilik({
    topics: [{ id: "t1", name: "Alkanlar", bunny_video_id: null }, { id: "t2", name: "Alkenlar", bunny_video_id: "v" }, { id: "t3", name: "Alkinlar", bunny_video_id: "v9" }],
    examples: [{ id: "e2", topic_id: "t3", example_number: 4, bunny_video_id: "x" }, { id: "e1", topic_id: "t3", example_number: 2, bunny_video_id: "y" }, { id: "e3", topic_id: "t3", example_number: 5, bunny_video_id: null }],
    transcripts: [{ topic_id: "t3" }], now: NOW,
  });
  assert.deepEqual(kodlar(k), ["mavzu_videosiz:t1", "mavzu_matnsiz:t2", "misol_matnsiz:t3"]);
  assert.ok(k.every((x) => x.kimga === "platforma"));
  assert.match(k[2].sarlavha, /2 ta misol videosida matn yo'q \(2, 4\)/);     // videosiz 5-misol sanalmaydi
});

test("variant: yarim qolgan video tahlil va kiritilmagan javob ustozga; hali boshlanmagan variant kamchilik emas", () => {
  const q = (v, n, video, opt, text = null) => ({ variant_id: v, question_number: n, bunny_video_id: video, correct_option: opt, correct_answer_text: text });
  const k = topKamchilik({
    variants: [{ id: "a", variant_number: 1 }, { id: "b", variant_number: 2 }],
    questions: [q("a", 1, "v", "A"), q("a", 6, null, null), q("a", 17, "v", null, "  "), q("a", 20, "v", null, "12,5"), q("b", 1, null, "A"), q("b", 2, null, "B")],
    now: NOW,
  });
  assert.deepEqual(kodlar(k), ["savol_videosiz:a", "savol_javobsiz:a"]);
  assert.match(k[0].sarlavha, /1-variant: 1 ta savolda video tahlil yo'q \(6\)/);
  assert.match(k[1].sarlavha, /2 ta savolda to'g'ri javob kiritilmagan \(6, 17\)/);   // ochiq savolning matnli javobi javob hisoblanadi
  assert.ok(k.every((x) => x.kimga === "ustoz"));
});

test("to'lov: faqat belgilangan vaqtdan ko'p kutgan so'rovlar bitta kamchilik bo'lib chiqadi", () => {
  const p = (status, h) => ({ status, created_at: soat(h) });
  assert.deepEqual(topKamchilik({ purchases: [p("pending", TOLOV_SOAT - 1), p("paid", 100), p("cancelled", 100)], now: NOW }), []);
  const k = topKamchilik({ purchases: [p("pending", 13), p("pending", 40), p("pending", 2)], now: NOW });
  assert.deepEqual(kodlar(k), ["tolov_kutmoqda"]);
  assert.match(k[0].sarlavha, /^2 ta to'lov so'rovi/);
  assert.equal(k[0].tafsilot.eng_eski, soat(40));
});

test("kanal: xato post va bir soatdan ko'p 'yuborilmoqda' turgan post kod agentiga", () => {
  const k = topKamchilik({ posts: [{ id: 1, holat: "xato", xato: "Forbidden: bot is not a member" }, { id: 2, holat: "yuborilmoqda", sent_at: soat(2) }, { id: 3, holat: "yuborilmoqda", sent_at: soat(0.2) }], now: NOW });
  assert.deepEqual(kodlar(k), ["kanal_xato:1", "kanal_qotdi:2"]);
  assert.match(k[0].sarlavha, /not a member/);
});

test("baza: yetishmayotgan jadval yoki ustun kod agentiga", () => {
  const k = topKamchilik({ sxemaYoq: [["tg_logins", "code", "Telegram orqali kirish"]], now: NOW });
  assert.deepEqual(k.map((x) => [x.kod, x.kimga]), [["sxema:tg_logins.code", "kod"]]);
  assert.match(k[0].sarlavha, /"Telegram orqali kirish" ishlamaydi/);
});

test("Bunny: yo'qolgan, xato bilan to'xtagan va kodlanmay qolgan video ushlanadi; yangi yuklangani kutiladi", () => {
  const bunny = new Map([["v2", { status: 5, dateUploaded: soat(50) }], ["v3", { status: 2, dateUploaded: soat(10) }], ["v4", { status: 2, dateUploaded: soat(1) }], ["v5", { status: 4, dateUploaded: soat(99) }]]);
  const k = topKamchilik({
    topics: [{ id: "t1", name: "Alkanlar", bunny_video_id: "v1" }],
    examples: [{ id: "e1", topic_id: "t1", example_number: 3, bunny_video_id: "v2" }],
    materials: [{ title: "Sxema", bunny_video_id: "v4" }],
    variants: [{ id: "a", variant_number: 2 }],
    questions: [{ variant_id: "a", question_number: 7, bunny_video_id: "v3", correct_option: "A" }, { variant_id: "a", question_number: 8, bunny_video_id: "v5", correct_option: "A" }],
    transcripts: [{ topic_id: "t1" }, { example_id: "e1" }], bunny, now: NOW,
  });
  assert.deepEqual(kodlar(k), ["video_yoq:v1", "video_buzuq:v2", "video_kodlanmadi:v3"]);
  assert.match(k[0].sarlavha, /"Alkanlar" darsi: video Bunny'da topilmadi/);
  assert.match(k[1].sarlavha, /"Alkanlar" 3-misol/);
  assert.match(k[2].sarlavha, /2-variant 7-savol/);
});

test("Bunny tekshirilmagan bo'lsa (null) video haqida hech narsa deyilmaydi", () => {
  assert.deepEqual(topKamchilik({ ...toza, bunny: null, now: NOW }), []);
});

test("bunnyRoyxat: sozlanmagan, xato javob yoki tarmoq uzilishida null; sahifalab o'qiydi", async () => {
  assert.equal(await bunnyRoyxat(async () => { throw new Error("chaqirilmasligi kerak"); }, {}), null);
  const env = { BUNNY_LIBRARY_ID: "7", BUNNY_API_KEY: "k" };
  assert.equal(await bunnyRoyxat(async () => ({ ok: false }), env), null);
  assert.equal(await bunnyRoyxat(async () => { throw new Error("uzildi"); }, env), null);
  const urls = [];
  const m = await bunnyRoyxat(async (u) => { urls.push(u); const p = Number(new URL(u).searchParams.get("page")); return { ok: true, json: async () => ({ totalItems: 3, items: p === 1 ? [{ guid: "a", status: 4 }, { guid: "b", status: 5 }] : [{ guid: "c", status: 4 }] }) }; }, env);
  assert.deepEqual([...m.keys()], ["a", "b", "c"]);
  assert.equal(urls.length, 2);
  assert.match(urls[0], /library\/7\/videos\?page=1/);
});

test("formatTekshiruv: yangilik bo'lmasa xabar yo'q; yangi, tuzalgan va eski kamchiliklar ko'rsatiladi, HTML qochiriladi", () => {
  assert.equal(formatTekshiruv({ yangi: [], tuzaldi: [], ochiq: 5, eski: [] }), null);
  const t = formatTekshiruv({ yangi: [{ sarlavha: "A <b> & C", kimga: "kod" }, { sarlavha: "Video yo'q", kimga: "ustoz" }], tuzaldi: [{}], ochiq: 4, eski: [{ sarlavha: "Eski" }] });
  assert.match(t, /Yangi kamchiliklar \(2 ta\)/);
  assert.match(t, /A &lt;b&gt; &amp; C <i>\(kod agenti\)<\/i>/);
  assert.match(t, /Video yo'q <i>\(siz\)<\/i>/);
  assert.match(t, /Tuzalgan: 1 ta/);
  assert.match(t, new RegExp(`${ESKI_XATO_KUN} kundan beri ochiq: 1 ta`));
  assert.match(t, /Jami ochiq: 4 ta/);
});

// Bazaning xotiradagi nusxasi: jadvallar nomi bo'yicha qatorlar; "yoq" dagi jadvallar xato qaytaradi.
function fakeDb(tables, yoq = []) {
  let seq = 100;
  const from = (name) => {
    const q = { op: "select", filters: [] };
    const run = () => {
      if (yoq.includes(name)) return { data: null, error: { message: `relation ${name} does not exist` } };
      const rows = (tables[name] ||= []);
      if (q.op === "insert") { const r = { id: ++seq, created_at: NOW.toISOString(), ...q.row }; rows.push(r); return { data: [{ id: r.id }], error: null }; }
      const hit = rows.filter((r) => q.filters.every((f) => f(r)));
      if (q.op === "update") { hit.forEach((r) => Object.assign(r, q.patch)); return { data: hit.map((r) => ({ id: r.id })), error: null }; }
      return q.single ? { data: hit[0] || null, error: null } : { data: hit, error: null };
    };
    const api = {
      select() { return api; }, order() { return api; }, limit() { return api; },
      insert(row) { q.op = "insert"; q.row = row; return api; },
      upsert(row) { q.op = "insert"; q.row = row; return api; },
      update(patch) { q.op = "update"; q.patch = patch; return api; },
      eq(k, v) { q.filters.push((r) => r[k] === v); return api; },
      in(k, vs) { q.filters.push((r) => vs.includes(r[k])); return api; },
      maybeSingle() { q.single = true; return Promise.resolve(run()); },
      then(res, rej) { return Promise.resolve(run()).then(res, rej); },
    };
    return api;
  };
  return { from, tables };
}
const baza = (extra = {}) => ({
  topics: [{ id: "t1", name: "Alkanlar", bunny_video_id: "v1" }, { id: "t2", name: "Alkenlar", bunny_video_id: null }],
  topic_examples: [], video_transcripts: [], variants: [], questions: [], agent_navbat: [], ...extra,
});

test("runTekshiruv: yangi kamchilik navbatga bir marta yoziladi, ustozga xabar ketadi; ertasi kuni qayta yozilmaydi va xabar yo'q", async () => {
  const db = fakeDb(baza()), notes = [];
  const r1 = await runTekshiruv(db, async (t) => { notes.push(t); }, { now: NOW });
  assert.deepEqual(r1, { topildi: 2, yangi: 2, tuzaldi: 0, ochiq: 2, bunny: false });
  assert.deepEqual(db.tables.agent_navbat.map((r) => [r.agent, r.tur, r.holat, r.kimga, r.tafsilot.kod]), [["nazoratchi", "xato", "yangi", "platforma", "mavzu_matnsiz:t1"], ["nazoratchi", "xato", "yangi", "platforma", "mavzu_videosiz:t2"]]);
  assert.equal(notes.length, 1);
  const r2 = await runTekshiruv(db, async (t) => { notes.push(t); }, { now: new Date(NOW.getTime() + 24 * 3600e3) });
  assert.deepEqual({ yangi: r2.yangi, ochiq: r2.ochiq }, { yangi: 0, ochiq: 2 });
  assert.equal(db.tables.agent_navbat.length, 2);
  assert.equal(notes.length, 1);
});

test("runTekshiruv: kamchilik yo'qolsa yozuvi yopiladi; qayta paydo bo'lsa yangi yozuv ochiladi", async () => {
  const t = baza();
  const db = fakeDb(t);
  await runTekshiruv(db, async () => {}, { now: NOW });
  t.video_transcripts.push({ topic_id: "t1", example_id: null });           // matn joylandi
  const notes = [];
  const r = await runTekshiruv(db, async (x) => { notes.push(x); }, { now: NOW });
  assert.deepEqual({ tuzaldi: r.tuzaldi, ochiq: r.ochiq }, { tuzaldi: 1, ochiq: 1 });
  const yopilgan = t.agent_navbat.find((x) => x.tafsilot.kod === "mavzu_matnsiz:t1");
  assert.equal(yopilgan.holat, "bajarildi");
  assert.match(yopilgan.tafsilot.izoh, /topilmadi/);
  assert.match(notes[0], /Tuzalgan: 1 ta/);
  t.video_transcripts.length = 0;                                            // matn yana yo'qoldi
  await runTekshiruv(db, async () => {}, { now: NOW });
  assert.equal(t.agent_navbat.filter((x) => x.tafsilot.kod === "mavzu_matnsiz:t1").length, 2);
});

test("runTekshiruv: Bunny tekshirilmagan kuni ochiq video kamchiligi 'tuzaldi' deb yopilmaydi", async () => {
  const t = baza({ video_transcripts: [{ topic_id: "t1" }], topics: [{ id: "t1", name: "Alkanlar", bunny_video_id: "v1" }] });
  const db = fakeDb(t);
  await runTekshiruv(db, async () => {}, { now: NOW, bunny: new Map() });      // v1 Bunny'da yo'q
  assert.equal(t.agent_navbat[0].tafsilot.kod, "video_yoq:v1");
  const r = await runTekshiruv(db, async () => {}, { now: NOW, bunny: null });  // bugun Bunny javob bermadi
  assert.equal(r.tuzaldi, 0);
  assert.equal(t.agent_navbat[0].holat, "yangi");
  const r3 = await runTekshiruv(db, async () => {}, { now: NOW, bunny: new Map([["v1", { status: 4 }]]) });
  assert.equal(r3.tuzaldi, 1);
});

test("runTekshiruv: eski kamchilik har kuni emas, har uch kunda bir eslatiladi", async () => {
  const t = baza({ topics: [{ id: "t2", name: "Alkenlar", bunny_video_id: null }] });
  const db = fakeDb(t), kun = (n) => new Date(NOW.getTime() + n * 24 * 3600e3);
  await runTekshiruv(db, async () => {}, { now: NOW });
  const xabarlar = [];
  for (const n of [1, 2, 3, 4, 5, 6]) { const notes = []; await runTekshiruv(db, async (x) => { notes.push(x); }, { now: kun(n) }); xabarlar.push(notes.length); }
  assert.deepEqual(xabarlar, [0, 0, 1, 0, 0, 1]);
});

test("runTekshiruv: ixtiyoriy jadval (kanal_postlar) yo'q bo'lsa tekshiruv to'xtamaydi, u sxema kamchiligi bo'lib chiqadi", async () => {
  const db = fakeDb(baza({ topics: [] }), ["kanal_postlar"]);
  const r = await runTekshiruv(db, async () => {}, { now: NOW });
  assert.equal(r.topildi, 1);
  assert.equal(db.tables.agent_navbat[0].tafsilot.kod, "sxema:kanal_postlar.id");
});

test("runTekshiruv: asosiy jadval o'qilmasa xato yashirilmaydi", async () => {
  await assert.rejects(() => runTekshiruv(fakeDb(baza(), ["topics"]), async () => {}, { now: NOW }), /topics does not exist/);
});
