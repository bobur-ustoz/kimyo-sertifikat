import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "fs";
import { loadDay, allQuestions } from "../api/_oyin/content.js";
import { gradeEquation, gradeBuild, buildName, normalizeStructure, questionKey } from "../api/_oyin/chem.js";
import { selectDaily, levelMix, REVIEW_COUNT } from "../api/_oyin/select.js";
import { scoreAnswer, applyRank, dailyBonus, canStake, POINTS } from "../api/_oyin/score.js";
import { publicQuestion, check } from "../api/_oyin/view.js";

const json1 = JSON.parse(readFileSync(new URL("../supabase/seed/oyin/kun_01.json", import.meta.url), "utf8"));
const day1 = loadDay(json1);
const day2 = loadDay({ ...json1, day: 2, topic: "Sikloalkanlar" });          // tajriba uchun: 1-kun mazmuni 2-kun sifatida
const q = (id) => allQuestions([day1]).find((x) => x.id === id);

test("tenglama: to'g'ri va noto'g'ri yozuvlar", () => {
  const p = q("d01-ok-3-1");                                                  // propan yonishi
  assert.equal(gradeEquation("C3H8+5O2→3CO2+4H2O", p).ok, true);
  assert.match(gradeEquation("C3H8+O2→3CO2+4H2O", p).msg, /tenglashtirilmagan/);
  assert.match(gradeEquation("C3H8+5O2→3CO2", p).msg, /mahsulotlar/);
  assert.match(gradeEquation("C3H8+5Cl2→3CO2+4H2O", p).msg, /Reagentlar/);
  assert.match(gradeEquation("2C3H8+10O2→6CO2+8H2O", p).msg, /eng kichik/);
  assert.match(gradeEquation("C3H8+5O2", p).msg, /xato/);
  assert.equal(gradeEquation("C3H8+5O2→3CO2+4H2O".repeat(30), p).ok, false);
  assert.equal(gradeEquation(null, p).ok, false);
});

test("tenglama: qavs va kasr koeffitsient", () => {
  const al = q("d01-ox-2-1");
  assert.equal(gradeEquation("Al4C3+12H2O→4Al(OH)3+3CH4", al).ok, true);
  const frac = { re: ["C3H7OH", "O2"], pr: ["CO2", "H2O"] };
  assert.equal(gradeEquation("C3H7OH+4,5O2→3CO2+4H2O", frac).ok, true);
  assert.equal(gradeEquation("2C3H7OH+9O2→6CO2+8H2O", frac).ok, true);
});

test("yig'ish: tuzilish tekshiruvi va noto'g'ri kirishlar", () => {
  const br = (...pairs) => { const b = Array.from({ length: 7 }, () => [0, 0]); pairs.forEach(([i, k]) => (b[i][k] = 1)); return b; };
  const target = q("d01-nom-3-1");                                           // 2,3-dimetilbutan
  assert.equal(gradeBuild({ n: 4, br: br([1, 0], [2, 1]) }, target).ok, true);
  assert.equal(gradeBuild({ n: 4, br: br([1, 0], [1, 1]) }, target).ok, false);
  assert.equal(buildName({ n: 4, br: br([1, 0], [1, 1]) }), "2,2-dimetilbutan");
  assert.equal(normalizeStructure({ n: 0, br: [] }), null);
  assert.equal(normalizeStructure({ n: 8, br: [] }), null);
  assert.equal(normalizeStructure({ n: 4, br: br([0, 0]) }), null, "chetki uglerodga tarmoq qo'yib bo'lmaydi");
  assert.equal(normalizeStructure({ n: 4, br: br([3, 0]) }), null, "oxirgi uglerodga ham");
  const weird = br(); weird[1] = [2, 0];
  assert.equal(normalizeStructure({ n: 4, br: weird }), null, "qiymat 0 yoki 1 bo'lishi kerak");
  assert.equal(gradeBuild("2,3-dimetilbutan", target).ok, false, "nomni to'g'ridan-to'g'ri yuborib bo'lmaydi");
});

test("mijoz ko'rinishida to'g'ri javob, kalit va tuzoq belgisi yo'q", () => {
  const secretKeys = ["ok", "no", "ans", "re", "pr", "trap", "w", "uses", "bundle", "build"];
  for (const x of allQuestions([day1])) {
    const pub = publicQuestion(x, [0, 1, 2, 3]);
    for (const k of secretKeys) assert.ok(!(k in pub), `${x.id}: "${k}" mijozga chiqib ketdi`);
    const text = JSON.stringify(pub);
    if (x.type === "write") { assert.ok(!text.includes(x.ans), `${x.id}: tenglama javobi ko'rinib qoldi`); }
    if (x.type === "choice") { assert.equal(pub.options.length, 4); assert.ok(!("trap" in pub)); }
    if (x.type === "build") assert.equal(pub.build, undefined);
  }
});

test("tekshiruv: to'g'ri, xato va tuzoq; izoh faqat javobdan keyin", () => {
  const c = q("d01-nom-1-1");                                                 // 2-metilpropan, tuzoq: Butan
  assert.equal(check(c, "2-metilpropan").ok, true);
  const wrong = check(c, "2-metilbutan");
  assert.equal(wrong.ok, false); assert.equal(wrong.trapHit, false); assert.equal(wrong.reveal.trapWhy, undefined);
  const trap = check(c, "Butan");
  assert.equal(trap.ok, false); assert.equal(trap.trapHit, true); assert.ok(trap.reveal.trapWhy);
  assert.equal(check(q("d01-ok-3-1"), "C3H8+5O2→3CO2+4H2O").ok, true);
  const bw = check(q("d01-nom-2-1"), { n: 4, br: [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]] });
  assert.equal(bw.ok, true); assert.equal(bw.reveal.correct.name, "2-metilbutan");
  assert.equal(bw.reveal.correct.formula, "CH3–CH(CH3)–CH2–CH3");
});

test("tanlov: 1-kunda 30 yangi savol, takror yo'q, har o'rindan bittadan", () => {
  const r = selectDaily({ day: 1, days: [day1], userId: "ali" });
  assert.equal(r.items.length, 30);
  assert.ok(r.items.every((i) => !i.review));
  assert.equal(new Set(r.items.map((i) => i.id.split("-").slice(0, 3).join("-"))).size, 30);
  assert.deepEqual(r.missing, []);
});

test("tanlov: bir o'quvchida bir xil, turli o'quvchilarda har xil", () => {
  const a1 = selectDaily({ day: 1, days: [day1], userId: "ali" }), a2 = selectDaily({ day: 1, days: [day1], userId: "ali" });
  assert.deepEqual(a1, a2);
  const sets = new Set(); for (let u = 0; u < 200; u++) sets.add(selectDaily({ day: 1, days: [day1], userId: "u" + u }).items.map((i) => i.id).join());
  assert.ok(sets.size > 190, "200 o'quvchidan kamida 190 tasi har xil to'plam olishi kerak: " + sets.size);
  // variantlar tartibi: har o'quvchida alohida, to'g'ri javob har xil harfga tushadi ("3-savol B" ma'nosiz)
  const positions = new Set();
  for (let u = 0; u < 200; u++) {
    const r = selectDaily({ day: 1, days: [day1], userId: "p" + u });
    const it = r.items.find((i) => i.id === "d01-nom-1-1") || r.items.find((i) => i.id.startsWith("d01-nom-1-"));
    assert.equal(it.order.slice().sort().join(), "0,1,2,3");
    positions.add(it.order.indexOf(0));                                       // 0-indeks = to'g'ri javob (ok)
  }
  assert.equal(positions.size, 4, "to'g'ri javob barcha 4 ta harfga tushishi kerak");
});

test("tanlov: 1000 o'quvchi, majburiy moddalar hammada, zanjir bitta to'plamdan, takrorsiz", () => {
  const qs = new Map(allQuestions([day1]).map((x) => [x.id, x]));
  for (let u = 0; u < 1000; u++) {
    const r = selectDaily({ day: 1, days: [day1], userId: "s" + u });
    assert.deepEqual(r.missing, [], "majburiy modda tushib qoldi: s" + u);
    const items = r.items.map((i) => qs.get(i.id));
    assert.equal(new Set(items.map(questionKey)).size, 30, "takroriy savol: s" + u);
    assert.equal(new Set(items.filter((x) => x.bundleGroup).map((x) => x.bundle)).size, 1, "zanjir aralashdi: s" + u);
  }
});

test("takrorlash: 2-kundan 6 ta (20%), eski kundan, zaif mavzu ustuvor, ko'rilganlar chetlab o'tiladi", () => {
  const days = [day1, day2];
  const r = selectDaily({ day: 2, days, userId: "ali" });
  const rev = r.items.filter((i) => i.review);
  assert.equal(rev.length, REVIEW_COUNT);
  assert.ok(rev.every((i) => i.fromDay === 1 && i.id.startsWith("d01-")));
  assert.equal(new Set(rev.map((i) => i.id.split("-").slice(0, 3).join("-"))).size, REVIEW_COUNT, "bir o'rindan ikki marta olinmasin");
  const total = r.items.length;                                               // bu tajribada 2-kun 30 o'rinli, shuning uchun 6/36
  assert.equal(total, 30 + REVIEW_COUNT);
  const seen = rev.map((i) => i.id);
  const again = selectDaily({ day: 2, days, userId: "ali", history: { seen } }).items.filter((i) => i.review);
  assert.ok(again.some((i) => !seen.includes(i.id)), "ko'rilgan variantlar o'rniga yangilari tanlanishi kerak");
  // zaif mavzu ustuvor: bitta zaif mavzu bo'lsa takrorning kamida 3 tasi shu kundan, ikkita bo'lsa eng zaifidan kamida 2 ta
  const day3 = loadDay({ ...json1, day: 3, topic: "Alkenlar" });
  for (let u = 0; u < 50; u++) {
    const one = selectDaily({ day: 3, days: [day1, day2, day3], userId: "z" + u, history: { errors: { Sikloalkanlar: 0.9 } } }).items.filter((i) => i.review);
    assert.equal(one.length, REVIEW_COUNT);
    assert.ok(one.filter((i) => i.fromDay === 2).length >= 3, "bitta zaif mavzudan kamida 3 ta bo'lishi kerak: z" + u);
    const two = selectDaily({ day: 3, days: [day1, day2, day3], userId: "z" + u, history: { errors: { Sikloalkanlar: 0.9, Alkanlar: 0.2 } } }).items.filter((i) => i.review);
    assert.ok(two.filter((i) => i.fromDay === 2).length >= 2 && two.filter((i) => i.fromDay === 1).length >= 1, "ikki zaif mavzudan 2+1: z" + u);
  }
});

test("qiyinlik ulushi: jami 100%, 3-daraja oshadi, 1-daraja kamayadi", () => {
  let prev = null;
  for (let d = 1; d <= 24; d++) {
    const m = levelMix(d);
    assert.equal(m[0] + m[1] + m[2], 100); assert.ok(m.every((x) => x >= 0));
    if (prev) { assert.ok(m[2] >= prev[2]); assert.ok(m[0] <= prev[0]); }
    prev = m;
  }
  assert.deepEqual(levelMix(1), [45, 47, 8]); assert.deepEqual(levelMix(24), [0, 20, 80]);
});

test("ball: oddiy, stavka, qalqon, qayta o'ynash, tuzoq", () => {
  assert.deepEqual(scoreAnswer({ ok: true }), { xp: 10, rank: 10, stakeLost: false, shieldUsed: false });
  assert.deepEqual(scoreAnswer({ ok: false }), { xp: 0, rank: 0, stakeLost: false, shieldUsed: false });
  assert.deepEqual(scoreAnswer({ ok: true, stake: true }), { xp: 20, rank: 20, stakeLost: false, shieldUsed: false });
  assert.deepEqual(scoreAnswer({ ok: false, stake: true }), { xp: 0, rank: -10, stakeLost: true, shieldUsed: false });
  assert.deepEqual(scoreAnswer({ ok: false, stake: true, hasShield: true }), { xp: 0, rank: 0, stakeLost: false, shieldUsed: true });
  assert.equal(scoreAnswer({ ok: true, replay: true }).xp, 3);
  assert.ok(scoreAnswer({ ok: false, stake: true }).xp >= 0, "umumiy XP hech qachon kamaymaydi");
  assert.equal(applyRank(4, -10), 0, "kunlik reyting 0 dan pastga tushmaydi");
  assert.equal(dailyBonus({ completed: true, trapHit: false }), POINTS.dailyBonus);
  assert.equal(dailyBonus({ completed: true, trapHit: true }), 0, "tuzoqqa tushsa kunlik bonus yo'q");
  assert.equal(dailyBonus({ completed: false, trapHit: false }), 0);
  assert.equal(canStake({ lvl: 3, stakesUsed: 1 }), true);
  assert.equal(canStake({ lvl: 3, stakesUsed: 2 }), false, "kuniga 2 tadan ko'p stavka yo'q");
  assert.equal(canStake({ lvl: 2, stakesUsed: 0 }), false, "stavka faqat 3-darajada");
});
