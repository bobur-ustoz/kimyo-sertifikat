import test from "node:test";
import assert from "node:assert/strict";
import { findFlags, formatReport, runNazorat, nudgeText, MAX_LINES, NUDGE_EVERY_DAYS } from "../api/_nazorat.js";

const NOW = new Date("2026-11-10T04:00:00Z");
const daysAgo = (d) => new Date(NOW.getTime() - d * 86400e3).toISOString();
const student = (id, extra = {}) => ({ id, full_name: id, email: `${id}@mail.uz`, plan: "premium", plan_expires_at: null, created_at: daysAgo(60), ...extra });
const ans = (id, n, correct, ago = 0) => Array.from({ length: n }, (_, i) => ({ student_id: id, is_correct: i < correct, at: daysAgo(ago) }));

test("3 kun va undan ko'p faolsiz o'quvchi bayroqlanadi, 2 kunligi emas", () => {
  const flags = findFlags({
    students: [student("ali"), student("vali")],
    views: [{ student_id: "ali", last_at: daysAgo(5) }, { student_id: "vali", last_at: daysAgo(2) }],
    answers: [], now: NOW,
  });
  assert.equal(flags.length, 1);
  assert.equal(flags[0].student.id, "ali");
  assert.match(flags[0].reasons[0], /5 kundan beri/);
});

test("oxirgi javob ham faollik hisoblanadi (video ochmasa ham)", () => {
  const flags = findFlags({ students: [student("ali")], views: [{ student_id: "ali", last_at: daysAgo(9) }], answers: ans("ali", 3, 3, 1), now: NOW });
  assert.equal(flags.length, 0);
});

test("oxirgi 20 javobda foiz 40 dan past bo'lsa bayroqlanadi; 40 va undan yuqori emas; 20 dan kam javobda hisoblanmaydi", () => {
  const base = { views: [{ student_id: "a", last_at: daysAgo(0) }, { student_id: "b", last_at: daysAgo(0) }, { student_id: "c", last_at: daysAgo(0) }], now: NOW };
  const flags = findFlags({ ...base, students: [student("a"), student("b"), student("c")], answers: [...ans("a", 20, 7), ...ans("b", 20, 8), ...ans("c", 10, 0)] });
  assert.deepEqual(flags.map((f) => f.student.id), ["a"]);
  assert.match(flags[0].reasons[0], /35%/);
});

test("foiz faqat oxirgi 20 javobdan olinadi (eskilari hisobga kirmaydi)", () => {
  const answers = [...ans("a", 20, 20, 0), ...ans("a", 40, 0, 10)];       // yaqinda hammasi to'g'ri, ancha oldin hammasi xato
  const flags = findFlags({ students: [student("a")], views: [{ student_id: "a", last_at: daysAgo(0) }], answers, now: NOW });
  assert.equal(flags.length, 0);
});

test("hech narsa ochmagan o'quvchi: to'lov paytidan (tugash sanasi - 30 kun) hisoblanadi", () => {
  const paid4DaysAgo = student("ali", { plan_expires_at: new Date(NOW.getTime() + 26 * 86400e3).toISOString() });   // 30 kunlikning 4-kuni
  const paid1DayAgo = student("vali", { plan_expires_at: new Date(NOW.getTime() + 29 * 86400e3).toISOString() });
  const flags = findFlags({ students: [paid4DaysAgo, paid1DayAgo], views: [], answers: [], now: NOW });
  assert.deepEqual(flags.map((f) => f.student.id), ["ali"]);
  assert.match(flags[0].reasons[0], /hali hech narsa ochmagan \(4 kun\)/);
});

test("ikkala sabab birga chiqadi", () => {
  const flags = findFlags({ students: [student("a")], views: [{ student_id: "a", last_at: daysAgo(6) }], answers: ans("a", 20, 2, 6), now: NOW });
  assert.equal(flags[0].reasons.length, 2);
});

test("hisobot: bo'sh bo'lsa null, uzun bo'lsa qisqartiriladi, HTML belgilari qochiriladi", () => {
  assert.equal(formatReport([]), null);
  const many = Array.from({ length: MAX_LINES + 3 }, (_, i) => ({ student: student(`s${i}`), reasons: ["5 kundan beri"] }));
  const text = formatReport(many);
  assert.match(text, new RegExp(`\\(${MAX_LINES + 3} ta\\)`));
  assert.match(text, /va yana 3 ta/);
  const evil = formatReport([{ student: student("x", { full_name: "<b>Ali</b>" }), reasons: ["a<b"] }]);
  assert.ok(!evil.includes("<b>Ali</b>"));
});

// Soxta baza: .neq/.in/.order/.limit zanjiri va then.
function fakeDb(tables) {
  const q = (rows) => { const o = { select: () => o, neq: () => o, in: () => o, order: () => o, limit: () => o, then: (f, r) => Promise.resolve({ data: rows, error: null }).then(f, r) }; return o; };
  return { from: (t) => q(tables[t] || []) };
}

test("runNazorat: bayroq bo'lsa bitta xabar yuboradi, bo'lmasa jim; bepul va admin o'quvchilar kirmaydi", async () => {
  const sent = [];
  const notify = async (t) => sent.push(t);
  const db = fakeDb({
    profiles: [student("ali"), student("adm", { is_admin: true }), student("eski", { plan_expires_at: daysAgo(1) })],
    video_views: [{ student_id: "ali", last_at: daysAgo(8) }, { student_id: "adm", last_at: daysAgo(8) }],
    answers: [], adaptive_answers: [],
  });
  const r = await runNazorat(db, notify, NOW);
  assert.deepEqual(r, { flagged: 1, sent: true, nudged: 0 });
  assert.equal(sent.length, 1);
  assert.match(sent[0], /ali@mail\.uz/);
  assert.ok(!sent[0].includes("adm@"));
  assert.ok(!sent[0].includes("eski@"));

  const quiet = fakeDb({ profiles: [student("ali")], video_views: [{ student_id: "ali", last_at: daysAgo(0) }], answers: [], adaptive_answers: [] });
  const r2 = await runNazorat(quiet, notify, NOW);
  assert.deepEqual(r2, { flagged: 0, sent: false, nudged: 0 });
  assert.equal(sent.length, 1);
});

test("adaptive_answers jadvali bazada bo'lmasa hisobot yiqilmaydi", async () => {
  const sent = [];
  const base = fakeDb({ profiles: [student("ali")], video_views: [{ student_id: "ali", last_at: daysAgo(8) }], answers: [] });
  const from = (t) => t === "adaptive_answers"
    ? { select() { return this; }, in() { return this; }, order() { return this; }, limit() { return this; }, then: (f, r) => Promise.resolve({ data: null, error: { message: "table missing" } }).then(f, r) }
    : base.from(t);
  const r = await runNazorat({ from }, async (t) => sent.push(t), NOW);
  assert.deepEqual(r, { flagged: 1, sent: true, nudged: 0 });
});

// ---- O'quvchiga eslatma ----
// Soxta baza: sotuv_leads select/update ni yozib boradi.
function nudgeDb(leads, tables = {}) {
  const updates = [];
  const q = (rows) => { const o = { select: () => o, neq: () => o, in: () => o, order: () => o, limit: () => o, update: (patch) => ({ eq: (c, v) => { updates.push({ patch, [c]: v }); return Promise.resolve({ error: null }); } }), then: (f, r) => Promise.resolve({ data: rows, error: null }).then(f, r) }; return o; };
  return { updates, from: (t) => q(t === "sotuv_leads" ? leads : tables[t] || []) };
}
const inactiveDb = (leads) => nudgeDb(leads, { profiles: [student("ali", { full_name: "Ali Valiyev" })], video_views: [{ student_id: "ali", last_at: daysAgo(5) }] });

test("nudgeText: ism bilan, /stop eslatiladi; hali boshlamagan uchun boshqa matn", () => {
  const a = nudgeText({ full_name: "Ali Valiyev" }, { days: 5, never: false });
  assert.match(a, /^Salom, Ali!/);
  assert.match(a, /kirmadingiz/);
  assert.match(a, /\/stop/);
  assert.match(nudgeText({ full_name: "" }, { days: 4, never: true }), /^Salom! Platformada hali hech narsa ochmadingiz/);
});

test("eslatma: ulangan o'quvchiga yuboriladi, last_nudge_at yoziladi, hisobotda belgilanadi", async () => {
  const sentTo = [];
  const db = inactiveDb([{ tg_id: 555, linked_user_id: "ali", remind: true, last_nudge_at: null }]);
  const notes = [];
  const r = await runNazorat(db, async (t) => notes.push(t), NOW, async (id, text) => { sentTo.push([id, text]); return { ok: true }; });
  assert.deepEqual(r, { flagged: 1, sent: true, nudged: 1 });
  assert.equal(sentTo.length, 1);
  assert.equal(sentTo[0][0], 555);
  assert.match(sentTo[0][1], /Salom, Ali!/);
  assert.ok(db.updates.some((u) => u.tg_id === 555 && u.patch.last_nudge_at));
  assert.match(notes[0], /eslatma yuborildi/);
});

test("eslatma: ulanmagan, /stop qilgan va yaqinda yuborilgan o'quvchilarga yuborilmaydi, sabab hisobotda", async () => {
  const cases = [
    [[], /Telegram ulanmagan/],
    [[{ tg_id: 1, linked_user_id: "ali", remind: false, last_nudge_at: null }], /o'chirgan/],
    [[{ tg_id: 1, linked_user_id: "ali", remind: true, last_nudge_at: daysAgo(NUDGE_EVERY_DAYS - 1) }], /yaqinda/],
  ];
  for (const [leads, expected] of cases) {
    const sent = [], notes = [];
    await runNazorat(inactiveDb(leads), async (t) => notes.push(t), NOW, async (...a) => { sent.push(a); return { ok: true }; });
    assert.equal(sent.length, 0);
    assert.match(notes[0], expected);
  }
});

test("eslatma: uch kundan keyin yana yuboriladi; Telegram xato bersa 'yuborilmadi' deb belgilanadi", async () => {
  const sent = [];
  const old = inactiveDb([{ tg_id: 1, linked_user_id: "ali", remind: true, last_nudge_at: daysAgo(NUDGE_EVERY_DAYS + 1) }]);
  await runNazorat(old, async () => {}, NOW, async (...a) => { sent.push(a); return { ok: true }; });
  assert.equal(sent.length, 1);

  const notes = [];
  const fail = inactiveDb([{ tg_id: 1, linked_user_id: "ali", remind: true, last_nudge_at: null }]);
  const r = await runNazorat(fail, async (t) => notes.push(t), NOW, async () => ({ ok: false }));
  assert.equal(r.nudged, 0);
  assert.match(notes[0], /yuborilmadi/);
  assert.equal(fail.updates.length, 0);
});

test("past foizli, lekin faol o'quvchiga eslatma yuborilmaydi (faqat ustozga hisobot)", async () => {
  const db = nudgeDb([{ tg_id: 1, linked_user_id: "a", remind: true, last_nudge_at: null }], {
    profiles: [student("a")], video_views: [{ student_id: "a", last_at: daysAgo(0) }], answers: ans("a", 20, 2, 0),
  });
  const sent = [];
  const r = await runNazorat(db, async () => {}, NOW, async (...a) => { sent.push(a); return { ok: true }; });
  assert.equal(r.flagged, 1);
  assert.equal(sent.length, 0);
});
