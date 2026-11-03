// Kunlik savollar faylini tekshiradi: tarkib, darajalar, tanlov javoblari, tuzilish nomlari va
// reaksiya tenglamalarining tenglashganligi (atomlar soni bo'yicha).
//
//   node supabase/seed/check_kun.mjs supabase/seed/oyin_kun_01.json
//
// Xato bo'lsa chiqish kodi 1 bo'ladi.
import { readFileSync } from "fs";

const file = process.argv[2];
if (!file) { console.error("Usage: node check_kun.mjs <kun.json>"); process.exit(1); }
const items = JSON.parse(readFileSync(file, "utf8"));
const errors = [];
const bad = (id, msg) => errors.push(`${id}: ${msg}`);

// --- formulalarni o'qish (o'yindagi tekshiruv bilan bir xil qoida)
function parseFormula(s) {
  let i = 0;
  const num = () => { const m = /^\d+/.exec(s.slice(i)); if (!m) return 1; i += m[0].length; return +m[0]; };
  const grp = () => {
    const c = {};
    while (i < s.length && s[i] !== ")") {
      if (s[i] === "(") { i++; const inner = grp(); if (s[i] !== ")") throw 0; i++; const m = num(); for (const k in inner) c[k] = (c[k] || 0) + inner[k] * m; }
      else { const m = /^[A-Z][a-z]?/.exec(s.slice(i)); if (!m) throw 0; i += m[0].length; const n = num(); c[m[0]] = (c[m[0]] || 0) + n; }
    }
    return c;
  };
  const r = grp();
  if (i !== s.length || !Object.keys(r).length) throw 0;
  return r;
}
const canon = (c) => Object.keys(c).sort((a, b) => (a === "C" ? -2 : a === "H" ? -1 : 0) - (b === "C" ? -2 : b === "H" ? -1 : 0) || a.localeCompare(b)).map((k) => k + (c[k] > 1 ? c[k] : "")).join("");
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
function checkEquation(q) {
  let L, R;
  const side = (t) => t.split("+").map((x) => { const m = /^(\d+(?:,\d+)?)?(.+)$/.exec(x); if (!m) throw 0; const c = m[1] ? parseFloat(m[1].replace(",", ".")) : 1; const cnt = parseFormula(m[2]); return { c, cnt, k: canon(cnt) }; });
  try { const p = q.ans.split("→"); if (p.length !== 2) throw 0; L = side(p[0]); R = side(p[1]); } catch { return "tenglama yozuvi noto'g'ri"; }
  const key = (a) => a.map((x) => x.k).sort().join("|");
  const want = (a) => a.map((f) => canon(parseFormula(f))).sort().join("|");
  if (key(L) !== want(q.re)) return "reagentlar ro'yxati (re) tenglamaga mos emas";
  if (key(R) !== want(q.pr)) return "mahsulotlar ro'yxati (pr) tenglamaga mos emas";
  const tot = (s) => { const t = {}; s.forEach((x) => { for (const k in x.cnt) t[k] = (t[k] || 0) + x.cnt[k] * x.c; }); return t; };
  const a = tot(L), b = tot(R);
  for (const e of new Set([...Object.keys(a), ...Object.keys(b)])) if (Math.abs((a[e] || 0) - (b[e] || 0)) > 1e-9) return `tenglashmagan: ${e} chapda ${a[e] || 0}, o'ngda ${b[e] || 0}`;
  if ([...L, ...R].every((x) => Number.isInteger(x.c)) && [...L, ...R].reduce((s, x) => gcd(s, x.c), 0) > 1) return "koeffitsientlar eng kichik butun sonlarda emas";
  return null;
}

// --- yig'ish vazifalari uchun mumkin bo'lgan nomlar (zanjir 1..7, metil tarmoqlari)
const NAMES = ["", "metan", "etan", "propan", "butan", "pentan", "geksan", "geptan"];
const PRE = ["", "metil", "dimetil", "trimetil", "tetrametil", "pentametil", "geksametil"];
const buildable = new Set();
for (let n = 1; n <= 7; n++) {
  const inner = Math.max(0, n - 2);
  for (let m = 0; m < 3 ** inner; m++) {
    const loc = []; let x = m;
    for (let i = 0; i < inner; i++) { const k = x % 3; x = Math.floor(x / 3); for (let j = 0; j < k; j++) loc.push(i + 2); }
    if (!loc.length) { buildable.add(NAMES[n]); continue; }
    const fw = loc.slice().sort((a, b) => a - b), rev = loc.map((p) => n + 1 - p).sort((a, b) => a - b);
    let use = fw; for (let i = 0; i < fw.length; i++) if (rev[i] !== fw[i]) { use = rev[i] < fw[i] ? rev : fw; break; }
    if (use.length < PRE.length) buildable.add(use.join(",") + "-" + PRE[use.length] + NAMES[n]);
  }
}

// --- har savol
const ids = new Set();
for (const q of items) {
  if (ids.has(q.id)) bad(q.id, "id takrorlangan"); ids.add(q.id);
  if (![1, 2, 3].includes(q.lvl)) bad(q.id, "daraja 1, 2 yoki 3 bo'lishi kerak");
  if (!q.p || !q.w) bad(q.id, "savol matni (p) va izoh (w) kerak");
  if (q.type === "choice") {
    if (!q.ok || q.no?.length !== 3) bad(q.id, "1 ta to'g'ri (ok) va 3 ta noto'g'ri (no) javob kerak");
    else if (new Set([q.ok, ...q.no]).size !== 4) bad(q.id, "variantlar takrorlangan");
  } else if (q.type === "build") {
    if (!buildable.has(q.build)) bad(q.id, `"${q.build}" yig'ish maydonida yig'ib bo'lmaydi yoki nomi noto'g'ri`);
  } else if (q.type === "write") {
    const e = checkEquation(q); if (e) bad(q.id, e);
    if (q.chain && !(q.chain.all?.length >= 2 && q.chain.at >= 0 && q.chain.at < q.chain.all.length - 1)) bad(q.id, "zanjir (chain) noto'g'ri");
  } else bad(q.id, "noma'lum tur: " + q.type);
}

// --- tarkib
const count = (f) => items.filter(f).length;
const groups = [...new Set(items.map((q) => q.group))];
const lv = [1, 2, 3].map((l) => count((q) => q.lvl === l));
console.log(`Savollar: ${items.length}, kunlar: ${[...new Set(items.map((q) => q.day))].join(",")}`);
console.log("Guruhlar:", groups.map((g) => `${g} ${count((q) => q.group === g)}`).join(" · "));
console.log("Turlar:", ["choice", "build", "write"].map((t) => `${t} ${count((q) => q.type === t)}`).join(" · "));
console.log(`Darajalar: 1-daraja ${lv[0]} (${Math.round(lv[0] / items.length * 100)}%), 2-daraja ${lv[1]} (${Math.round(lv[1] / items.length * 100)}%), 3-daraja ${lv[2]} (${Math.round(lv[2] / items.length * 100)}%)`);
for (const g of groups) if (count((q) => q.group === g) < 2) bad("tarkib", `"${g}" guruhida 2 tadan kam savol`);
if (items.length !== 30) bad("tarkib", `kunlik 30 savol kerak, ${items.length} ta bor`);

if (errors.length) { console.log("\nXATOLAR:"); errors.forEach((e) => console.log(" - " + e)); process.exit(1); }
console.log("\nHAMMASI TO'G'RI: tenglamalar tenglashgan, nomlar yig'iladi, variantlar takrorlanmaydi");
