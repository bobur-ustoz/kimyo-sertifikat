// Kunlik savol faylini (v2) tekshiradi. Har keyingi kun fayli shu skriptdan o'tishi shart.
//
//   node supabase/seed/oyin/check.mjs supabase/seed/oyin/kun_01.json
//
// Tekshiradi: har variantning to'g'riligi (tenglama tenglashganmi, nom yig'iladimi, variantlar takrorlanmaganmi),
// variantlar bir xil darajada va bir xil turdami, tuzoq belgisi to'g'ri joyda turibdimi, majburiy moddalar
// qamrovi, va 1000 ta tasodifiy o'quvchi uchun tanlov: har biri to'liq to'plam, takrorsiz tenglamalar,
// hamma majburiy moddalar, zanjir bir xil to'plamdan.
import { readFileSync } from "fs";
import { loadDay } from "../../../api/_oyin/content.js";
import { gradeEquation, buildableNames, questionKey } from "../../../api/_oyin/chem.js";
import { selectDaily, levelMix } from "../../../api/_oyin/select.js";

const file = process.argv[2];
if (!file) { console.error("Usage: node check.mjs <kun_NN.json>"); process.exit(1); }
const day = loadDay(JSON.parse(readFileSync(file, "utf8")));
const earlier = process.argv.slice(3).map((f) => loadDay(JSON.parse(readFileSync(f, "utf8"))));   // oldingi kunlar (takror savollar uchun)
const errors = [];
const bad = (id, msg) => errors.push(`${id}: ${msg}`);
const buildable = buildableNames();

for (const s of day.slots) {
  if (!s.variants.length) bad(s.slot, "variant yo'q");
  if (s.variants.length < 2) bad(s.slot, "kamida 2 ta variant kerak (aks holda hammaga bir xil savol chiqadi)");
  for (const q of s.variants) {
    if (!q.p || !q.w) bad(q.id, "savol matni (p) va izoh (w) kerak");
    if (s.type === "choice") {
      if (!q.ok || q.no?.length !== 3) bad(q.id, "1 ta to'g'ri (ok) va 3 ta noto'g'ri (no) javob kerak");
      else if (new Set([q.ok, ...q.no]).size !== 4) bad(q.id, "variantlar takrorlangan");
      if (q.trap) {
        if (!q.no?.includes(q.trap.opt)) bad(q.id, `tuzoq varianti ("${q.trap.opt}") noto'g'ri javoblar orasida bo'lishi kerak`);
        if (!q.trap.why) bad(q.id, "tuzoq uchun izoh (why) kerak");
      }
    } else if (s.type === "build") {
      if (!buildable.has(q.build.toLowerCase())) bad(q.id, `"${q.build}" yig'ish maydonida yig'ib bo'lmaydi yoki nomi noto'g'ri`);
      if (q.trap) bad(q.id, "tuzoq faqat tanlovli savollarda bo'ladi");
    } else if (s.type === "write") {
      const r = gradeEquation(q.ans, q);
      if (!r.ok) bad(q.id, "tenglama: " + (r.msg || "noto'g'ri"));
      if (q.chain && !(q.chain.all?.length >= 2 && q.chain.at >= 0 && q.chain.at < q.chain.all.length - 1)) bad(q.id, "zanjir (chain) noto'g'ri");
      if (q.trap) bad(q.id, "tuzoq faqat tanlovli savollarda bo'ladi");
    } else bad(s.slot, "noma'lum tur: " + s.type);
  }
  // variantlar bir-biridan farq qilsin
  const keys = s.variants.map(questionKey);
  if (new Set(keys).size !== keys.length) bad(s.slot, "variantlar bir-biriga o'xshash (bir xil savol)");
  if (s.bundleGroup) {
    const b = s.variants.map((v) => v.bundle);
    if (b.some((x) => !x) || new Set(b).size !== b.length) bad(s.slot, "zanjir variantlarida bundle (A, B...) har xil bo'lishi kerak");
  }
}
// bir zanjir guruhi uchun hamma o'rinda bir xil to'plamlar bo'lishi kerak
for (const g of new Set(day.slots.map((s) => s.bundleGroup).filter(Boolean))) {
  const sets = day.slots.filter((s) => s.bundleGroup === g).map((s) => s.variants.map((v) => v.bundle).sort().join(","));
  if (new Set(sets).size !== 1) bad(g, "zanjir o'rinlarida to'plamlar (bundle) bir xil emas");
}

// majburiy moddalar: har biri kamida 2 ta alohida o'rinda bo'lishi kerak (qamrovni ta'minlash uchun)
for (const sub of day.substances) {
  const where = new Set(day.slots.filter((s) => s.variants.some((v) => v.uses.includes(sub))).map((s) => s.slot));
  if (where.size < 3) bad("modda", `majburiy modda "${sub}" faqat ${where.size} ta o'rinda uchraydi (kamida 3 ta kerak, shunda qamrov har doim ta'minlanadi)`);
}
const trapSlots = day.slots.filter((s) => s.variants.some((v) => v.trap)).length;
if (trapSlots < 3) bad("tuzoq", `tuzoqli o'rinlar ${trapSlots} ta, kamida 3 ta kerak`);

// kun tarkibi
const groups = [...new Set(day.slots.map((s) => s.group))];
const lv = [1, 2, 3].map((l) => day.slots.filter((s) => s.lvl === l).length);
const target = levelMix(day.day);
console.log(`${day.day}-kun · ${day.topic}: ${day.slots.length} o'rin, ${day.slots.reduce((n, s) => n + s.variants.length, 0)} variant`);
console.log("Guruhlar:", groups.map((g) => `${g} ${day.slots.filter((s) => s.group === g).length}`).join(" · "));
console.log(`Darajalar: ${lv.join("/")} (${lv.map((x) => Math.round(x / day.slots.length * 100)).join("/")}%), jadvaldagi maqsad ${target.join("/")}%`);
console.log(`Tuzoqli o'rinlar: ${trapSlots}, majburiy moddalar: ${day.substances.length}`);
const wantN = day.day === 1 ? 30 : 24;
if (day.slots.length !== wantN) bad("tarkib", `${day.day}-kunda ${wantN} ta o'rin kerak, ${day.slots.length} ta bor`);
for (const g of groups) if (day.slots.filter((s) => s.group === g).length < 2) bad("tarkib", `"${g}" guruhida 2 tadan kam o'rin`);

// 1000 ta tasodifiy o'quvchi uchun tanlov
if (!errors.length) {
  let dup = 0, miss = 0, bundleBad = 0; const seenSets = new Set(); const pick = {};
  for (let u = 0; u < 1000; u++) {
    const r = selectDaily({ day: day.day, days: [...earlier, day], userId: "u" + u });
    const own = r.items.filter((i) => !i.review);
    const qs = own.map((i) => day.slots.flatMap((s) => s.variants).find((v) => v.id === i.id));
    if (qs.length !== day.slots.length) bad("tanlov", `to'plam ${qs.length} ta, ${day.slots.length} ta bo'lishi kerak`);
    if (new Set(qs.map(questionKey)).size !== qs.length) dup++;
    if (r.missing.length) miss++;
    const zb = new Set(qs.filter((q) => q.bundleGroup).map((q) => q.bundle));
    if (zb.size > 1) bundleBad++;
    seenSets.add(r.items.map((i) => i.id).join("|"));
    qs.forEach((q) => { pick[q.slot] = pick[q.slot] || {}; pick[q.slot][q.id] = (pick[q.slot][q.id] || 0) + 1; });
  }
  console.log(`\n1000 o'quvchi uchun: har xil to'plamlar ${seenSets.size} ta`);
  if (dup) bad("tanlov", `${dup} ta o'quvchida takroriy tenglama/nom bor`);
  if (miss) bad("tanlov", `${miss} ta o'quvchida majburiy modda tushib qolgan`);
  if (bundleBad) bad("tanlov", `${bundleBad} ta o'quvchida zanjir aralash to'plamdan`);
  const skew = Object.entries(pick).filter(([, m]) => { const v = Object.values(m); return Math.max(...v) / 1000 > 0.9; }).map(([s]) => s);
  if (skew.length) console.log("Eslatma: bir variant 90% dan ko'p chiqadigan o'rinlar (majburiy moddalar tufayli):", skew.join(", "));
}

if (errors.length) { console.log("\nXATOLAR:"); errors.forEach((e) => console.log(" - " + e)); process.exit(1); }
console.log("\nHAMMASI TO'G'RI");
