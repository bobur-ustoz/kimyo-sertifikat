// Kunlik savollar faylidan oddiy PDF yasaydi: savollar daftari + javoblar kaliti.
// Google Chrome (headless) kerak.
//
//   node supabase/seed/kun_pdf.mjs supabase/seed/oyin_kun_01.json kitob/Organika_1-kun_Alkanlar.pdf
//
// Chrome boshqa joyda bo'lsa: CHROME=/yo'l/chrome node ...
import { readFileSync, writeFileSync, mkdtempSync } from "fs";
import { execFileSync } from "child_process";
import { tmpdir } from "os";
import { join, resolve } from "path";

const [src, out] = process.argv.slice(2);
if (!src || !out) { console.error("Usage: node kun_pdf.mjs <kun.json> <chiqish.pdf>"); process.exit(1); }
const items = JSON.parse(readFileSync(src, "utf8"));
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

// ---------- matn yordamchilari
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const SUB = { "₀": 0, "₁": 1, "₂": 2, "₃": 3, "₄": 4, "₅": 5, "₆": 6, "₇": 7, "₈": 8, "₉": 9 };
// Unicode pastki indekslar -> <sub>; <sub> teglari o'zi qoladi
const rich = (s) => esc(s).replace(/&lt;(\/?sub)&gt;/g, "<$1>").replace(/[₀-₉]+/g, (m) => "<sub>" + [...m].map((c) => SUB[c]).join("") + "</sub>");
// "C3H8+5O2→3CO2" -> pastki indeks va oraliq bilan
const eq = (s) => {
  let o = "", prev = "", sub = false, dec = false;
  for (const ch of s) {
    if (/\d/.test(ch)) { sub = !dec && (/[A-Za-z)]/.test(prev) || (sub && /\d/.test(prev))); o += sub ? `<sub>${ch}</sub>` : ch; }
    else if (ch === ",") { sub = false; dec = true; o += ch; }
    else { sub = false; dec = false; o += ch === "+" || ch === "→" ? ` ${ch} ` : esc(ch); }
    prev = ch;
  }
  return o;
};

// ---------- aralashtirish (o'yindagi bilan bir xil, shuning uchun harflar mos keladi)
const rng = (seed) => () => { seed |= 0; seed = (seed + 0x6d2b79f5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
const options = (q, n) => { const r = rng(n * 7919 + 17), o = [q.ok, ...q.no]; for (let i = 3; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [o[i], o[j]] = [o[j], o[i]]; } return o; };

// ---------- yig'ish nomidan qisqa tuzilish formulasi
const NAMES = ["", "metan", "etan", "propan", "butan", "pentan", "geksan", "geptan"], PRE = ["", "metil", "dimetil", "trimetil", "tetrametil", "pentametil", "geksametil"];
function nameOf(n, br) {
  const loc = [];
  for (let i = 1; i < n - 1; i++) for (let j = 0; j < br[i]; j++) loc.push(i + 1);
  if (!loc.length) return NAMES[n][0].toUpperCase() + NAMES[n].slice(1);
  const fw = loc.slice().sort((a, b) => a - b), rev = loc.map((p) => n + 1 - p).sort((a, b) => a - b);
  let use = fw; for (let i = 0; i < fw.length; i++) if (rev[i] !== fw[i]) { use = rev[i] < fw[i] ? rev : fw; break; }
  return use.join(",") + "-" + PRE[use.length] + NAMES[n];
}
function structureOf(target) {
  for (let n = 1; n <= 7; n++) {
    const inner = Math.max(0, n - 2);
    for (let m = 0; m < 3 ** inner; m++) {
      const br = Array(n).fill(0); let x = m;
      for (let i = 0; i < inner; i++) { br[1 + i] = x % 3; x = Math.floor(x / 3); }
      if (nameOf(n, br).toLowerCase() === target.toLowerCase()) {
        return Array.from({ length: n }, (_, i) => (i === 0 || i === n - 1 ? "CH3" : br[i] === 0 ? "CH2" : br[i] === 1 ? "CH(CH3)" : "C(CH3)2")).join("–");
      }
    }
  }
  return "";
}
const MOL = { "d01-nom-1": "CH3–CH(CH3)–CH3" };   // rasmli savolning matnli ko'rinishi

// ---------- HTML
const day = items[0].day, topic = items[0].topic;
const groups = [...new Set(items.map((q) => q.group))];
const lv = [1, 2, 3].map((l) => items.filter((q) => q.lvl === l).length);
const lvlName = ["", "1-daraja", "2-daraja", "3-daraja"];
let no = 0, key = "";
let body = "";
for (const g of groups) {
  body += `<h2>${esc(g)}</h2>`;
  for (const q of items.filter((x) => x.group === g)) {
    no++;
    const n = items.indexOf(q);
    let task = "", ans = "";
    if (q.type === "choice") {
      const o = options(q, n);
      task = (MOL[q.id] ? `<div class="f">${eq(MOL[q.id])}</div>` : "") + `<ol class="opt">${o.map((t) => `<li>${/[+→]/.test(t) ? eq(t) : rich(t)}</li>`).join("")}</ol>`;
      ans = `<b>${"ABCD"[o.indexOf(q.ok)]})</b> ${rich(q.ok)}`;
    } else if (q.type === "build") {
      task = `<div class="blank">Tuzilish formulasini chizing yoki yozing:</div>`;
      ans = `${rich(q.build)}<br><span class="f2">${eq(structureOf(q.build))}</span>`;
    } else {
      const chain = q.chain ? `<div class="chain">${q.chain.all.map((f, i) => `<span class="${i === q.chain.at || i === q.chain.at + 1 ? "on" : ""}">${eq(f)}</span>`).join(" → ")}</div>` : "";
      task = chain + `<div class="blank">Tenglamani yozing:</div>`;
      ans = eq(q.ans);
    }
    body += `<div class="q"><div class="h"><b>${no}.</b> ${rich(q.p)} <span class="l l${q.lvl}">${lvlName[q.lvl]}</span></div>${task}</div>`;
    key += `<tr><td class="n">${no}</td><td>${ans}</td><td class="w">${q.w}</td></tr>`;
  }
}

const html = `<!doctype html><html lang="uz"><head><meta charset="utf-8"><title>Organika · ${day}-kun · ${esc(topic)}</title><style>
@page{size:A4;margin:16mm 15mm}
*{box-sizing:border-box}
body{font:11.5pt/1.45 Arial,Helvetica,sans-serif;color:#111;margin:0}
h1{font-size:20pt;margin:0 0 2mm}
.sub0{color:#555;margin:0 0 6mm;font-size:10.5pt}
h2{font-size:12.5pt;margin:7mm 0 2.5mm;padding:1.5mm 3mm;background:#e8f1ec;border-left:3mm solid #0c8e5e;break-after:avoid}
.q{margin:0 0 3.6mm;break-inside:avoid}
.h{margin-bottom:1.2mm}
.l{display:inline-block;font-size:8pt;padding:.3mm 2mm;border-radius:2mm;margin-left:1.5mm;vertical-align:1px}
.l1{background:#d8f2e6;color:#08603f}.l2{background:#fff0cc;color:#7a5200}.l3{background:#e6e1ff;color:#3b2d99}
.opt{list-style:upper-alpha;margin:0;padding-left:9mm}
.opt li{margin:.6mm 0}
.f{font-size:13pt;margin:1mm 0 1.5mm 9mm}
.blank{border:1px dashed #999;border-radius:1.5mm;padding:2mm 3mm 11mm;color:#777;font-size:9.5pt;margin-top:1.5mm}
.chain{margin:0 0 1mm;font-size:11pt}.chain span{padding:0 1.5mm}.chain .on{background:#fff0cc;border-radius:1.5mm}
sub{font-size:.7em;line-height:0}
.pb{break-before:page}
table{width:100%;border-collapse:collapse;font-size:10pt}
td{border-bottom:.3mm solid #ddd;padding:1.6mm 1.5mm;vertical-align:top}
td.n{width:8mm;font-weight:bold;color:#555}td.w{color:#444;width:46%}
.f2{color:#444}
.note{font-size:9.5pt;color:#555;margin-top:5mm}
</style></head><body>
<h1>Organika · ${day}-kun · ${esc(topic)}</h1>
<p class="sub0">${items.length} savol · ${groups.length} bosqich · 1-daraja ${lv[0]} ta, 2-daraja ${lv[1]} ta, 3-daraja ${lv[2]} ta. Javoblar kaliti oxirgi sahifada.</p>
${body}
<div class="pb"></div>
<h1>Javoblar kaliti</h1>
<p class="sub0">${day}-kun · ${esc(topic)}</p>
<table>${key}</table>
<p class="note">Tenglamalarda koeffitsientlar eng kichik butun sonlarda yozilgan. Reaksiya shartlari (t, katalizator) savol matnida berilgan.</p>
</body></html>`;

const dir = mkdtempSync(join(tmpdir(), "kunpdf-"));
const htmlPath = join(dir, "kun.html");
writeFileSync(htmlPath, html);
execFileSync(CHROME, ["--headless=new", "--disable-gpu", "--no-pdf-header-footer", `--print-to-pdf=${resolve(out)}`, `file://${htmlPath}`], { stdio: "ignore" });
console.log("PDF tayyor:", resolve(out));
