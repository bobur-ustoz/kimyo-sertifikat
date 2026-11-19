import test from "node:test";
import assert from "node:assert/strict";
import { tayyorla, sahifaYol, kalit, qosh, xatoYoz, xabarYoz, KUN_MAX, OGOH_QURILMA, XABAR_KUN_MAX } from "../api/_xato.js";

const NOW = new Date("2026-11-19T10:00:00Z");
// Soxta navbat jadvali: tanlash, sanash, qo'shish (kalit bo'yicha takrorsiz) va yangilash.
function fakeDb(rows = [], profiles = []) {
  let id = rows.length;
  const from = (name) => {
    const src = name === "profiles" ? profiles : rows, q = { f: [], op: "select" };
    const hit = () => src.filter((r) => q.f.every((f) => f(r)));
    const run = () => {
      if (q.op === "update") { hit().forEach((r) => Object.assign(r, q.patch)); return { data: hit(), error: null }; }
      if (q.op === "insert") {
        if (q.row.kalit && src.some((r) => r.kalit === q.row.kalit)) return { data: [], error: null };
        const r = { id: ++id, created_at: NOW.toISOString(), ...q.row }; src.push(r); return { data: [r], error: null };
      }
      return q.head ? { count: hit().length, error: null } : { data: hit(), error: null };
    };
    const api = {
      select(_c, o) { if (o?.head) q.head = true; return api; }, limit() { return api; }, order() { return api; },
      eq(k, v) { q.f.push((r) => r[k] === v); return api; }, gte(k, v) { q.f.push((r) => r[k] >= v); return api; },
      update(p) { q.op = "update"; q.patch = p; return api; }, insert(r) { q.op = "insert"; q.row = r; return api; }, upsert(r) { q.op = "insert"; q.row = r; return api; },
      maybeSingle() { return Promise.resolve({ data: hit()[0] || null, error: null }); },
      then(a, b) { return Promise.resolve(run()).then(a, b); },
    };
    return api;
  };
  return { from, rows };
}
const X = (extra = {}) => ({ xabar: "TypeError: x is undefined", sahifa: "https://sayt.uz/mavzu/12?token=abc#oyin", stack: "at a.js:1", qurilma: "abc123def", ...extra });

test("tayyorla: shovqin tashlanadi, manzildan so'rov qismi olinadi, matn qisqartiriladi", () => {
  for (const s of ["Script error.", "ResizeObserver loop limit exceeded", "TypeError: Failed to fetch", "Load failed", "ab"]) assert.equal(tayyorla({ xabar: s }), null);
  assert.equal(tayyorla({ xabar: "Xato", stack: "chrome-extension://abc/x.js" }), null);
  const t = tayyorla(X({ xabar: "a".repeat(900), qurilma: "<script>" }));
  assert.equal(t.xabar.length, 300);
  assert.equal(t.sahifa, "/mavzu/12#oyin");
  assert.equal(t.qurilma, null);
  assert.equal(sahifaYol("/admin?x=1"), "/admin");
});

test("kalit: sonlari va id si boshqa bir xil xato bitta kalit; boshqa kun yoki boshqa xato boshqa kalit", () => {
  const a = kalit("2026-11-19", tayyorla(X({ xabar: "Savol 123 topilmadi" }))), b = kalit("2026-11-19", tayyorla(X({ xabar: "Savol 456 topilmadi" })));
  assert.equal(a, b);
  assert.notEqual(a, kalit("2026-11-20", tayyorla(X({ xabar: "Savol 123 topilmadi" }))));
  assert.notEqual(a, kalit("2026-11-19", tayyorla(X())));
});

test("xatoYoz: birinchi marta kod agentiga yozuv; takrori sanaladi; uchinchi qurilmada ustozga bir marta xabar", async () => {
  const db = fakeDb(), ogoh = [];
  const yubor = (q) => xatoYoz(db, X({ qurilma: q }), { now: NOW, ogohlantir: async (t) => ogoh.push(t) });
  assert.deepEqual(await yubor("qurilma1"), { ok: true, yangi: true });
  assert.equal(db.rows.length, 1);
  assert.deepEqual({ agent: db.rows[0].agent, tur: db.rows[0].tur, kimga: db.rows[0].kimga, holat: db.rows[0].holat }, { agent: "sayt", tur: "xato", kimga: "kod", holat: "yangi" });
  assert.match(db.rows[0].sarlavha, /^Saytda xato: TypeError: x is undefined \(\/mavzu\/12#oyin\)$/);
  await yubor("qurilma1"); await yubor("qurilma2");
  assert.equal(ogoh.length, 0);
  assert.equal((await yubor("qurilma3")).ogoh, true);
  await yubor("qurilma4");
  assert.equal(ogoh.length, 1);                                  // faqat chegaraga yetgan paytda
  assert.match(ogoh[0], new RegExp(`${OGOH_QURILMA} ta qurilmada`));
  assert.equal(db.rows.length, 1);
  assert.deepEqual({ soni: db.rows[0].tafsilot.soni, q: db.rows[0].tafsilot.qurilmalar.length }, { soni: 5, q: 4 });
  assert.equal(JSON.stringify(db.rows[0]).includes("token"), false);      // manzildagi parametr saqlanmaydi
});

test("xatoYoz: shovqin yozilmaydi; kuniga xil xatolar soni cheklangan", async () => {
  const db = fakeDb();
  assert.equal((await xatoYoz(db, { xabar: "Failed to fetch" }, { now: NOW })).sabab, "shovqin");
  for (let i = 0; i < KUN_MAX + 5; i++) await xatoYoz(db, X({ xabar: `Xato turi ${"abcdefghijklmnopqrstuvwxyzABCDEFGHIJ"[i]}` }), { now: NOW, ogohlantir: async () => {} });
  assert.equal(db.rows.length, KUN_MAX);
});

test("xabarYoz: o'quvchi xabari navbatga va ustozga; juda qisqa matn va kunlik chegara rad etiladi", async () => {
  const db = fakeDb([], [{ id: "u1", full_name: "Ali <b>" }]), ogoh = [];
  const opt = { now: NOW, ogohlantir: async (t) => ogoh.push(t) };
  assert.equal((await xabarYoz(db, { matn: "ab" }, { id: "u1" }, opt)).status, 400);
  assert.deepEqual(await xabarYoz(db, { matn: "Video ochilmayapti", sahifa: "/mavzu/3?a=1" }, { id: "u1" }, opt), { ok: true });
  assert.deepEqual({ tur: db.rows[0].tur, kimga: db.rows[0].kimga, sahifa: db.rows[0].tafsilot.sahifa }, { tur: "savol", kimga: "kod", sahifa: "/mavzu/3" });
  assert.match(ogoh[0], /Ali &lt;b&gt;: Video ochilmayapti/);
  for (let i = 1; i < XABAR_KUN_MAX; i++) await xabarYoz(db, { matn: `Yana muammo ${i}` }, { id: "u1" }, opt);
  assert.equal((await xabarYoz(db, { matn: "To'rtinchi xabar" }, { id: "u1" }, opt)).status, 429);
  assert.deepEqual(await xabarYoz(db, { matn: "Boshqa o'quvchi" }, { id: "u2" }, opt), { ok: true });
});

test("qosh: qurilma takrorlansa sanalmaydi", () => {
  const r = qosh({ soni: 1, qurilmalar: ["a"] }, "a");
  assert.deepEqual(r, { tafsilot: { soni: 2, qurilmalar: ["a"] }, ogoh: false });
});
