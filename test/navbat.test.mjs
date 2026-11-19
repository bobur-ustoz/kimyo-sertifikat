import test from "node:test";
import assert from "node:assert/strict";
import { tayyorla, yoz, holatQoy, oqi, xulosa } from "../api/_navbat.js";

const NOW = new Date("2026-11-18T06:00:00Z");
const soatOldin = (h) => new Date(NOW.getTime() - h * 3600e3).toISOString();

// agent_navbat jadvalining xotiradagi nusxasi: supabase-js so'rovlarining shu kodda ishlatiladigan qismi.
function fakeDb({ fail = null } = {}) {
  const rows = [];
  let seq = 0;
  const from = () => {
    const q = { op: "select", filters: [], limitN: Infinity };
    const run = () => {
      if (fail) return { data: null, error: { message: fail } };
      const match = (r) => q.filters.every((f) => f(r));
      if (q.op === "insert" || q.op === "upsert") {
        if (q.op === "upsert" && q.row.kalit && rows.some((r) => r.kalit === q.row.kalit)) return { data: [], error: null };
        if (q.row.kalit && rows.some((r) => r.kalit === q.row.kalit)) return { data: null, error: { message: "duplicate key" } };
        const r = { id: ++seq, created_at: NOW.toISOString(), updated_at: NOW.toISOString(), ...q.row };
        rows.push(r);
        return { data: [{ id: r.id }], error: null };
      }
      if (q.op === "update") {
        const hit = rows.filter(match);
        hit.forEach((r) => Object.assign(r, q.patch));
        return { data: hit.map((r) => ({ id: r.id })), error: null };
      }
      const out = rows.filter(match).sort((a, b) => b.created_at.localeCompare(a.created_at) || b.id - a.id).slice(0, q.limitN);
      return q.single ? { data: out[0] || null, error: null } : { data: out, error: null };
    };
    const api = {
      insert(row) { q.op = "insert"; q.row = row; return api; },
      upsert(row) { q.op = "upsert"; q.row = row; return api; },
      update(patch) { q.op = "update"; q.patch = patch; return api; },
      select() { return api; },
      order() { return api; },
      limit(n) { q.limitN = n; return api; },
      eq(k, v) { q.filters.push((r) => r[k] === v); return api; },
      in(k, vs) { q.filters.push((r) => vs.includes(r[k])); return api; },
      gte(k, v) { q.filters.push((r) => r[k] >= v); return api; },
      maybeSingle() { q.single = true; return Promise.resolve(run()); },
      then(res, rej) { return Promise.resolve(run()).then(res, rej); },
    };
    return api;
  };
  return { from, rows };
}

const jim = async (fn) => { const e = console.error; console.error = () => {}; try { return await fn(); } finally { console.error = e; } };

test("tayyorla: bajarilgan ish va hisobot 'bajarildi', xato va savol 'yangi' holatida boshlanadi", () => {
  assert.equal(tayyorla({ agent: "montaj", tur: "ish", sarlavha: "Montaj bitdi" }).holat, "bajarildi");
  assert.equal(tayyorla({ agent: "nazoratchi", tur: "hisobot", sarlavha: "Kunlik" }).holat, "bajarildi");
  assert.equal(tayyorla({ agent: "nazoratchi", tur: "xato", sarlavha: "Sahifa ochilmadi" }).holat, "yangi");
  assert.equal(tayyorla({ agent: "sotuv", tur: "savol", sarlavha: "Ustoz kerak" }).holat, "yangi");
  assert.equal(tayyorla({ agent: "montaj", tur: "ish", sarlavha: "Montaj boshlandi", holat: "jarayonda" }).holat, "jarayonda");
});

test("tayyorla: nom kichik harfga o'tadi, sarlavha 300 belgida kesiladi, tafsilot har doim obyekt", () => {
  const r = tayyorla({ agent: " Montaj ", tur: "ish", sarlavha: "a".repeat(400), tafsilot: "fayl.mp4", kimga: "USTOZ" });
  assert.equal(r.agent, "montaj");
  assert.equal(r.kimga, "ustoz");
  assert.equal(r.sarlavha.length, 300);
  assert.deepEqual(r.tafsilot, { qiymat: "fayl.mp4" });
  assert.deepEqual(tayyorla({ agent: "kod", tur: "ish", sarlavha: "x" }).tafsilot, {});
  assert.equal(tayyorla({ agent: "kod", tur: "ish", sarlavha: "x" }).kimga, null);
});

test("tayyorla: noto'g'ri yozuv rad etiladi", () => {
  assert.throws(() => tayyorla({ agent: "", tur: "ish", sarlavha: "x" }), /agent/);
  assert.throws(() => tayyorla({ agent: "kod", tur: "boshqa", sarlavha: "x" }), /tur/);
  assert.throws(() => tayyorla({ agent: "kod", tur: "ish", sarlavha: "  " }), /sarlavha/);
  assert.throws(() => tayyorla({ agent: "kod", tur: "ish", sarlavha: "x", holat: "tugadi" }), /holat/);
  assert.throws(() => tayyorla(), /agent/);
});

test("yoz: yozuv qo'shiladi va id qaytadi", async () => {
  const db = fakeDb();
  const r = await yoz(db, { agent: "montaj", tur: "ish", sarlavha: "Montaj bitdi", tafsilot: { fayl: "a.mp4" } });
  assert.deepEqual(r, { ok: true, id: 1 });
  assert.equal(db.rows[0].agent, "montaj");
  assert.deepEqual(db.rows[0].tafsilot, { fayl: "a.mp4" });
});

test("yoz: bir xil kalit ikkinchi marta yozilmaydi (cron ikki marta ishlasa ham kuniga bitta)", async () => {
  const db = fakeDb();
  const y = { agent: "nazoratchi", tur: "hisobot", sarlavha: "Kunlik tekshiruv", kalit: "nazorat:2026-11-18" };
  assert.deepEqual(await yoz(db, y), { ok: true, id: 1 });
  assert.deepEqual(await yoz(db, y), { ok: true, takror: true });
  assert.equal(db.rows.length, 1);
  assert.equal((await yoz(db, { ...y, kalit: "nazorat:2026-11-19" })).id, 2);
});

test("yoz: baza ishlamasa ham, yozuv noto'g'ri bo'lsa ham xato otmaydi", async () => {
  const a = await jim(() => yoz(fakeDb({ fail: "relation does not exist" }), { agent: "sotuv", tur: "xato", sarlavha: "x" }));
  assert.deepEqual(a, { ok: false, error: "relation does not exist" });
  const b = await jim(() => yoz(fakeDb(), { agent: "sotuv", tur: "notogri", sarlavha: "x" }));
  assert.equal(b.ok, false);
  const c = await jim(() => yoz({ from() { throw new Error("tarmoq uzildi"); } }, { agent: "sotuv", tur: "xato", sarlavha: "x" }));
  assert.deepEqual(c, { ok: false, error: "tarmoq uzildi" });
});

test("holatQoy: holat o'zgaradi, izoh tafsilotga qo'shiladi, eski tafsilot saqlanadi", async () => {
  const db = fakeDb();
  const { id } = await yoz(db, { agent: "nazoratchi", tur: "xato", sarlavha: "Sahifa ochilmadi", tafsilot: { sahifa: "/oyin" }, kimga: "kod" });
  assert.deepEqual(await holatQoy(db, id, "jarayonda"), { ok: true });
  assert.equal(db.rows[0].holat, "jarayonda");
  assert.deepEqual(await holatQoy(db, id, "bajarildi", "loadTeam yuqoriga ko'chirildi"), { ok: true });
  assert.equal(db.rows[0].holat, "bajarildi");
  assert.deepEqual(db.rows[0].tafsilot, { sahifa: "/oyin", izoh: "loadTeam yuqoriga ko'chirildi" });
});

test("holatQoy: noto'g'ri holat va yo'q yozuv rad etiladi", async () => {
  const db = fakeDb();
  await yoz(db, { agent: "kod", tur: "xato", sarlavha: "x" });
  assert.equal((await jim(() => holatQoy(db, 1, "tugadi"))).ok, false);
  assert.equal(db.rows[0].holat, "yangi");
  assert.match((await jim(() => holatQoy(db, 99, "bajarildi"))).error, /topilmadi/);
  assert.match((await jim(() => holatQoy(db, 99, "bajarildi", "izoh"))).error, /topilmadi/);
});

test("oqi: oxirgi kun yozuvlari, yangisi birinchi; kimga, agent va tur bo'yicha saralanadi", async () => {
  const db = fakeDb();
  db.rows.push(
    { id: 1, agent: "montaj", tur: "ish", holat: "bajarildi", kimga: null, sarlavha: "eski", created_at: soatOldin(30) },
    { id: 2, agent: "montaj", tur: "ish", holat: "bajarildi", kimga: null, sarlavha: "bugungi montaj", created_at: soatOldin(5) },
    { id: 3, agent: "nazoratchi", tur: "xato", holat: "yangi", kimga: "kod", sarlavha: "bugungi xato", created_at: soatOldin(2) },
  );
  assert.deepEqual((await oqi(db, { now: NOW })).map((r) => r.id), [3, 2]);
  assert.deepEqual((await oqi(db, { now: NOW, kun: 2 })).map((r) => r.id), [3, 2, 1]);
  assert.deepEqual((await oqi(db, { now: NOW, kimga: "kod" })).map((r) => r.id), [3]);
  assert.deepEqual((await oqi(db, { now: NOW, agent: "montaj" })).map((r) => r.id), [2]);
  assert.deepEqual((await oqi(db, { now: NOW, tur: "xato" })).map((r) => r.id), [3]);
});

test("oqi: 'ochiq' rejimida eski bo'lsa ham bajarilmagan yozuvlar chiqadi, bajarilganlari chiqmaydi", async () => {
  const db = fakeDb();
  db.rows.push(
    { id: 1, agent: "nazoratchi", tur: "xato", holat: "yangi", kimga: "kod", sarlavha: "bir hafta oldingi xato", created_at: soatOldin(170) },
    { id: 2, agent: "nazoratchi", tur: "xato", holat: "bajarildi", kimga: "kod", sarlavha: "tuzatilgan", created_at: soatOldin(3) },
    { id: 3, agent: "sotuv", tur: "savol", holat: "jarayonda", kimga: "ustoz", sarlavha: "savol", created_at: soatOldin(1) },
  );
  assert.deepEqual((await oqi(db, { now: NOW, ochiq: true })).map((r) => r.id), [3, 1]);
  assert.deepEqual((await oqi(db, { now: NOW, ochiq: true, kimga: "kod" })).map((r) => r.id), [1]);
});

test("oqi: baza xatosi yashirilmaydi (hisobot bo'sh deb o'ylanmasin)", async () => {
  await assert.rejects(() => oqi(fakeDb({ fail: "permission denied" }), { now: NOW }), /permission denied/);
});

test("xulosa: agent va tur bo'yicha sanaydi, ochiq xato va savollarni ajratadi", () => {
  const x = xulosa([
    { agent: "montaj", tur: "ish", holat: "bajarildi" },
    { agent: "montaj", tur: "ish", holat: "jarayonda" },
    { agent: "nazoratchi", tur: "xato", holat: "yangi", sarlavha: "a" },
    { agent: "nazoratchi", tur: "xato", holat: "bajarildi", sarlavha: "b" },
    { agent: "sotuv", tur: "savol", holat: "jarayonda", sarlavha: "c" },
    { agent: "nazoratchi", tur: "hisobot", holat: "bajarildi" },
  ]);
  assert.equal(x.jami, 6);
  assert.deepEqual(x.agentlar.montaj, { ish: 2, xato: 0, savol: 0, hisobot: 0 });
  assert.deepEqual(x.agentlar.nazoratchi, { ish: 0, xato: 2, savol: 0, hisobot: 1 });
  assert.deepEqual(x.ochiq.map((r) => r.sarlavha), ["a", "c"]);
  assert.deepEqual(xulosa([]), { jami: 0, agentlar: {}, ochiq: [] });
});
