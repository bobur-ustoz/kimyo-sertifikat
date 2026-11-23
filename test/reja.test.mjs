import test from "node:test";
import assert from "node:assert/strict";
import { taqsim, rejaMavzular, keyingiMavzu, rejaIsh, rejaOquvchi, rejaAdmin, kirishSavollar, kirishNatija, ESLATMA_KUN, KIRISH_SAVOL } from "../api/_reja.js";

const KUN = (n) => new Date(Date.parse("2026-11-23T04:50:00Z") + n * 86400e3);
// Soxta baza (vazifa testidagi bilan bir xil qoida): jadvallar massiv, insert id beradi.
function fakeDb(tables) {
  const seq = {};
  const from = (name) => {
    const rows = (tables[name] ||= []), q = { op: "select", f: [] };
    const hit = () => rows.filter((r) => q.f.every((f) => f(r)));
    const run = () => {
      if (q.op === "insert") { const add = (Array.isArray(q.val) ? q.val : [q.val]).map((r) => ({ id: (seq[name] = (seq[name] || rows.length) + 1), ...(name === "vazifa_topshiriq" ? { holat: "berilgan", javoblar: {} } : {}), ...r })); rows.push(...add); return { data: add, error: null }; }
      if (q.op === "update") { const h = hit(); h.forEach((r) => Object.assign(r, q.val)); return { data: h, error: null }; }
      return { data: hit(), error: null };
    };
    const api = {
      select() { return api; }, limit() { return api; }, order() { return api; },
      insert(v) { q.op = "insert"; q.val = v; return api; }, update(v) { q.op = "update"; q.val = v; return api; },
      eq(k, v) { q.f.push((r) => r[k] === v); return api; }, neq(k, v) { q.f.push((r) => r[k] !== v); return api; },
      in(k, vs) { q.f.push((r) => vs.includes(r[k])); return api; }, not(k) { q.f.push((r) => r[k] != null); return api; },
      then(a, b) { return Promise.resolve(run()).then(a, b); },
    };
    return api;
  };
  return { from, tables };
}
// Mavzuga n ta analog (misol + uning analogi).
const analoglar = (topic, n) => Array.from({ length: n }, (_, i) => ({ ex: { id: `${topic}-e${i}`, topic_id: topic }, an: { example_id: `${topic}-e${i}`, analog_savol: `${topic} savol ${i} A) 1; B) 2; C) 3; D) 4`, analog_javob: "A) 1" } }));
function baza() {
  const a = [...analoglar("t1", 20), ...analoglar("t3", 4)];
  return {
    topics: [{ id: "t3", name: "Proporsiya", sort_order: 3, bunny_video_id: "v" }, { id: "t1", name: "Valentlik", sort_order: 1, bunny_video_id: "v" }, { id: "t2", name: "Mol", sort_order: 2, bunny_video_id: "v" }, { id: "t0", name: "Videosiz", sort_order: 0, bunny_video_id: null }],
    topic_examples: a.map((x) => x.ex), topic_example_analogs: a.map((x) => x.an), analog_questions: [], questions: [],
    profiles: [{ id: "ali", full_name: "Ali Valiyev", plan: "premium" }, { id: "vali", full_name: "Vali", plan: "premium" }, { id: "guli", full_name: "Guli", plan: "free" }, { id: "adm", full_name: "Ustoz", plan: "premium", is_admin: true }],
    sotuv_leads: [{ tg_id: 1, linked_user_id: "ali", remind: true }],
    video_views: [], oquvchi_reja: [], vazifalar: [], vazifa_topshiriq: [], log: [],
  };
}
function yur(db, kun, sent = [], kirish = true) {
  return rejaIsh(db, { now: KUN(kun), kirish, rnd: () => 0.999, site: "https://sayt.uz", sendDoc: null, pdf: async () => Buffer.from("pdf"),
    log: async (y) => { db.tables.log.push(y); }, send: async (tg_id, text) => { sent.push({ tg_id, text }); return { ok: true }; } });
}
const ali = (db) => db.tables.oquvchi_reja.find((r) => r.student_id === "ali");
const kor = (db, topic, who = "ali") => db.tables.video_views.push({ student_id: who, kind: "topic", ref_id: topic });
const topshir = (db, who = "ali") => db.tables.vazifa_topshiriq.filter((t) => t.student_id === who).forEach((t) => { t.holat = "topshirilgan"; });

test("taqsim: savol kam bo'lsa vazifa va imtihon yo'q; yetarli bo'lsa ikkiga bo'linadi, ko'pi bilan 10 tadan", () => {
  assert.deepEqual([2, 3, 5, 6, 12, 25].map(taqsim), [{ vazifa: 0, imtihon: 0 }, { vazifa: 3, imtihon: 0 }, { vazifa: 5, imtihon: 0 }, { vazifa: 3, imtihon: 3 }, { vazifa: 6, imtihon: 6 }, { vazifa: 10, imtihon: 10 }]);
});

test("rejaMavzular: faqat videosi bor mavzular, tartib bo'yicha; keyingiMavzu tugatilmagan birinchisi", () => {
  const m = rejaMavzular(baza().topics);
  assert.deepEqual(m.map((x) => x.id), ["t1", "t2", "t3"]);
  assert.equal(keyingiMavzu(m, ["t1"]).id, "t2");
  assert.equal(keyingiMavzu(m, ["t1", "t2", "t3"]), null);
});

test("reja: boshlanish, dars eslatmasi, uyga vazifa, imtihon, keyingi mavzu, savolsiz mavzu va yakun", async () => {
  const db = fakeDb(baza()), sent = [];
  assert.deepEqual(await yur(db, 0, sent, false), { oquvchilar: 2, kirish: 0, boshlandi: 2, vazifa: 0, imtihon: 0, keyingi: 0, eslatma: 0, tugadi: 0 });       // faqat pullik, admin va bepul kirmaydi
  assert.deepEqual({ topic: ali(db).topic_id, bosqich: ali(db).bosqich }, { topic: "t1", bosqich: "dars" });
  assert.match(sent[0].text, /^Assalomu alaykum, Ali! Siz uchun o'qish rejasi tayyor: 3 ta mavzu, ketma-ket\. Birinchisi: "Valentlik"/);
  assert.equal(sent.length, 1);                                                    // Telegram ulanmagan o'quvchiga xabar yo'q, lekin reja yuradi

  assert.equal((await yur(db, 1, sent, false)).eslatma, 0);                               // hali erta
  assert.equal((await yur(db, ESLATMA_KUN, sent, false)).eslatma, 2);                     // dars ko'rilmagan: eslatma
  assert.match(sent.at(-1).text, /"Valentlik" mavzusining darsi turibdi/);
  assert.equal((await yur(db, ESLATMA_KUN + 1, sent, false)).eslatma, 0);                 // har kuni emas

  kor(db, "t1");
  assert.equal((await yur(db, 3, sent, false)).vazifa, 1);                                // dars ko'rildi: uyga vazifa
  const v1 = db.tables.vazifalar[0];
  assert.deepEqual({ tur: v1.tur, nom: v1.nom, n: v1.savollar.length, bosqich: ali(db).bosqich }, { tur: "uyga", nom: "Valentlik: uyga vazifa", n: 10, bosqich: "vazifa" });
  assert.deepEqual(await yur(db, 4, sent, false).then((h) => [h.vazifa, h.imtihon]), [0, 0]);   // vazifa topshirilmagan: kutadi

  topshir(db);
  assert.equal((await yur(db, 5, sent, false)).imtihon, 1);
  const v2 = db.tables.vazifalar[1];
  assert.deepEqual({ tur: v2.tur, n: v2.savollar.length, takror: v2.savollar.some((id) => v1.savollar.includes(id)) }, { tur: "imtihon", n: 10, takror: false });

  topshir(db);
  assert.equal((await yur(db, 6, sent, false)).keyingi, 1);
  assert.deepEqual({ topic: ali(db).topic_id, bosqich: ali(db).bosqich, tugagan: ali(db).tugagan }, { topic: "t2", bosqich: "dars", tugagan: ["t1"] });
  assert.match(sent.at(-1).text, /Keyingisi: "Mol" \(2\/3\)/);

  kor(db, "t2");                                                                   // "Mol"da analog yo'q
  assert.equal((await yur(db, 7, sent, false)).keyingi, 1);
  assert.equal(ali(db).topic_id, "t3");
  assert.deepEqual({ kimga: db.tables.log.at(-1).kimga, s: /"Mol" mavzusida analog savol yo'q/.test(db.tables.log.at(-1).sarlavha) }, { kimga: "ustoz", s: true });

  kor(db, "t3");                                                                   // 4 ta analog: faqat vazifa, imtihonsiz
  assert.equal((await yur(db, 8, sent, false)).vazifa, 1);
  assert.equal(db.tables.vazifalar.at(-1).savollar.length, 4);
  topshir(db);
  assert.equal((await yur(db, 9, sent, false)).tugadi, 1);
  assert.deepEqual({ bosqich: ali(db).bosqich, n: ali(db).tugagan.length }, { bosqich: "tugadi", n: 3 });
  assert.match(sent.at(-1).text, /hamma mavzularni tugatdingiz/);

  db.tables.topics.push({ id: "t4", name: "Alkanlar", sort_order: 9, bunny_video_id: "v" });      // ustoz yangi mavzu qo'shdi
  assert.equal((await yur(db, 10, sent, false)).keyingi, 1);
  assert.deepEqual({ topic: ali(db).topic_id, bosqich: ali(db).bosqich }, { topic: "t4", bosqich: "dars" });
});

test("ko'rinishlar: o'quvchi o'z rejasini, ustoz mavzular va har o'quvchi qayerdaligini ko'radi", async () => {
  const db = fakeDb(baza());
  assert.deepEqual(await rejaOquvchi(db, "ali"), { yoq: true });
  await yur(db, 0, [], false); kor(db, "t1"); await yur(db, 1, [], false);
  assert.deepEqual((await rejaOquvchi(db, "ali")).mavzular, [{ nom: "Valentlik", holat: "hozir", bosqich: "vazifa" }, { nom: "Mol", holat: "kutmoqda" }, { nom: "Proporsiya", holat: "kutmoqda" }]);
  const a = await rejaAdmin(db, { now: KUN(3) });
  assert.deepEqual(a.mavzular.map((m) => [m.tartib, m.nom, m.analoglar, m.vazifa, m.imtihon, m.oquvchilar]), [[1, "Valentlik", 20, 10, 10, 2], [2, "Mol", 0, 0, 0, 0], [3, "Proporsiya", 4, 4, 0, 0]]);
  assert.deepEqual(a.oquvchilar.map((o) => [o.ism, o.mavzu, o.bosqich]), [["Ali Valiyev", "Valentlik", "vazifa"], ["Vali", "Valentlik", "dars"]]);
});

test("kirish testi: har mavzudan 3 tadan savol; hammasi to'g'ri bo'lgan mavzu rejadan chiqadi, qolgani va savolsiz mavzu rejada qoladi", async () => {
  const db = fakeDb(baza()), sent = [];
  assert.deepEqual(await yur(db, 0, sent).then((h) => [h.kirish, h.boshlandi]), [2, 0]);
  const v = db.tables.vazifalar[0];
  assert.deepEqual({ tur: v.tur, nom: v.nom, n: v.savollar.length, bosqich: ali(db).bosqich }, { tur: "imtihon", nom: "Kirish testi", n: 2 * KIRISH_SAVOL, bosqich: "kirish" });   // t1 va t3 da savol bor, t2 da yo'q
  assert.deepEqual(await rejaOquvchi(db, "ali"), { kirish: true });
  assert.equal((await yur(db, 1, sent)).boshlandi, 0);                             // topshirilmagan: kutadi

  // Ali: Valentlik (t1) hammasi to'g'ri, Proporsiya (t3) bittasi xato.
  const top = db.tables.vazifa_topshiriq.find((t) => t.student_id === "ali" && t.vazifa_id === v.id);
  top.javoblar = Object.fromEntries(v.savollar.map((id) => [id, "A"])); top.javoblar[v.savollar.find((id) => id.startsWith("t3"))] = "B"; top.holat = "topshirilgan";
  assert.equal((await yur(db, 2, sent)).boshlandi, 1);
  assert.deepEqual({ topic: ali(db).topic_id, bosqich: ali(db).bosqich, bilgan: ali(db).bilgan, kirish: ali(db).kirish }, { topic: "t2", bosqich: "dars", bilgan: ["t1"], kirish: { t1: [3, 3], t3: [2, 3] } });
  assert.match(sent.at(-1).text, /Kirish testi tekshirildi\. 1 ta mavzuni bilar ekansiz, ularni rejaga qo'shmadim\. Rejangizda 2 ta mavzu\. Birinchisi: "Mol"/);
  assert.deepEqual((await rejaOquvchi(db, "ali")).mavzular.map((m) => m.holat), ["biladi", "hozir", "kutmoqda"]);
  const a = await rejaAdmin(db, { now: KUN(2) });
  assert.deepEqual(a.oquvchilar.map((o) => [o.ism, o.bosqich, o.bilgan, o.qoldi]), [["Ali Valiyev", "dars", 1, 2], ["Vali", "kirish", 0, 3]]);
});

test("kirishSavollar va kirishNatija: savoli kam mavzu testga kirmaydi; javobsiz savol xato hisoblanadi", () => {
  const pool = [1, 2, 3, 4].map((i) => ({ id: `a${i}`, topic_id: "a", correct_option: "A" })).concat([{ id: "b1", topic_id: "b", correct_option: "C" }]);
  const ks = kirishSavollar([{ id: "a" }, { id: "b" }], pool, () => 0.999);
  assert.deepEqual(ks.map((q) => q.topic_id), ["a", "a", "a"]);
  assert.deepEqual(kirishNatija(ks, { [ks[0].id]: "A", [ks[1].id]: "A" }), { natija: { a: [2, 3] }, bilgan: [] });
});
