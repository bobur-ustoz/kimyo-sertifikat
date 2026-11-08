import test from "node:test";
import assert from "node:assert/strict";
import { buildItems, buildMessage, isActivePremium, runYangilik } from "../api/_yangilik.js";

test("yangi mavzu o'z misollari bilan, eski mavzuga yangi misollar alohida", () => {
  const items = buildItems({
    topics: [{ id: "t1", name: "Reaksiya turlari" }],
    examples: [...Array(20).fill({ topic_id: "t1" }), { topic_id: "t2" }, { topic_id: "t2" }],
    topicNames: { t2: "Proporsiya" },
    variants: [{ variant_number: 3 }, { variant_number: 3 }],
  });
  assert.deepEqual(items.map((i) => i.text), ["Reaksiya turlari — yangi mavzu, 20 ta misol videosi", "Proporsiya: 2 ta yangi misol videosi", "Variant 3 — yangi"]);
  assert.match(buildMessage([{ text: "A<b>" }]), /A&lt;b&gt;/);
});

test("faqat muddati tugamagan Premium", () => {
  const now = new Date("2026-11-07T00:00:00Z");
  assert.equal(isActivePremium({ plan: "premium", plan_expires_at: "2026-11-10T00:00:00Z" }, now), true);
  assert.equal(isActivePremium({ plan: "premium", plan_expires_at: "2026-11-01T00:00:00Z" }, now), false);
  assert.equal(isActivePremium({ plan: "free", plan_expires_at: null }, now), false);
});

// Minimal Supabase o'rniga: jadval nomi bo'yicha tayyor javoblar.
function fakeDb(tables, log = []) {
  const q = (name) => {
    const st = { name, op: "select" };
    const chain = new Proxy({}, {
      get: (_, k) => {
        if (k === "then") return (res) => res(st.op === "insert" || st.op === "update" ? (log.push([name, st.op, st.payload]), { data: null, error: null }) : { data: tables[name] ?? [], error: null });
        if (k === "insert" || k === "update") return (p) => { st.op = k; st.payload = p; return chain; };
        return () => chain;
      },
    });
    return chain;
  };
  return { from: q };
}

test("yangilik bo'lmasa hech narsa yuborilmaydi", async () => {
  const sent = [];
  const r = await runYangilik(fakeDb({ digest_runs: [] }), async (...a) => (sent.push(a), { ok: true }), "https://x", {});
  assert.equal(r.items, 0); assert.equal(sent.length, 0);
});

test("faqat Premium va ulangan o'quvchilarga bitta xabar", async () => {
  const sent = [], log = [];
  const db = fakeDb({
    digest_runs: [], topics: [{ id: "t1", name: "Sikloalkanlar" }], topic_examples: [], variants: [],
    sotuv_leads: [{ tg_id: 1, linked_user_id: "u1" }, { tg_id: 2, linked_user_id: "u2" }],
    profiles: [{ id: "u1", plan: "premium", plan_expires_at: null }, { id: "u2", plan: "free", plan_expires_at: null }],
  }, log);
  const r = await runYangilik(db, async (id, text, btn) => (sent.push([id, text, btn]), { ok: true }), "https://x", {});
  assert.equal(r.sent, 1); assert.equal(sent[0][0], 1); assert.match(sent[0][1], /Sikloalkanlar/);
  assert.equal(sent[0][2].url, "https://x");
  assert.ok(log.some(([n, op]) => n === "digest_runs" && op === "insert"));
});

test("sinov rejimi yubormaydi va yozmaydi", async () => {
  const log = [];
  const r = await runYangilik(fakeDb({ digest_runs: [], topics: [{ id: "t", name: "A" }], topic_examples: [], variants: [] }, log), async () => assert.fail(), "https://x", { dryRun: true });
  assert.equal(r.items, 1); assert.match(r.text, /A/); assert.equal(log.length, 0);
});
