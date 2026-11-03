// O'yin dvigateli: kimyoviy tekshiruv. Javoblar shu yerda, serverda tekshiriladi.
// Leading underscore keeps Vercel from exposing the folder as endpoints.

// ---------- formulalar va tenglamalar
export function parseFormula(s) {
  let i = 0;
  const num = () => { const m = /^\d+/.exec(s.slice(i)); if (!m) return 1; i += m[0].length; return +m[0]; };
  const grp = () => {
    const c = {};
    while (i < s.length && s[i] !== ")") {
      if (s[i] === "(") { i++; const inner = grp(); if (s[i] !== ")") throw new Error("qavs"); i++; const m = num(); for (const k in inner) c[k] = (c[k] || 0) + inner[k] * m; }
      else { const m = /^[A-Z][a-z]?/.exec(s.slice(i)); if (!m) throw new Error("element"); i += m[0].length; const n = num(); c[m[0]] = (c[m[0]] || 0) + n; }
    }
    return c;
  };
  const r = grp();
  if (i !== s.length || !Object.keys(r).length) throw new Error("formula");
  return r;
}

// Hill tartibi: C, H, qolganlari alifbo bo'yicha
export const canon = (c) => Object.keys(c)
  .sort((a, b) => (a === "C" ? -2 : a === "H" ? -1 : 0) - (b === "C" ? -2 : b === "H" ? -1 : 0) || a.localeCompare(b))
  .map((k) => k + (c[k] > 1 ? c[k] : "")).join("");

const gcd = (a, b) => (b ? gcd(b, a % b) : a);

function parseSide(t) {
  return t.split("+").map((x) => {
    const m = /^(\d+(?:,\d+)?)?(.+)$/.exec(x);
    if (!m) throw new Error("had");
    const c = m[1] ? parseFloat(m[1].replace(",", ".")) : 1;
    if (!c) throw new Error("koeffitsient");
    const cnt = parseFormula(m[2]);
    return { c, cnt, k: canon(cnt) };
  }).reduce((acc, x) => {   // bir xil modda ikki marta yozilsa (masalan C3H7Cl + C3H7Cl), koeffitsientlar qo'shiladi
    const same = acc.find((y) => y.k === x.k);
    if (same) same.c += x.c; else acc.push(x);
    return acc;
  }, []);
}

// Tenglama yozuvi q.re (reagentlar) va q.pr (mahsulotlar) ga mosmi, tenglashganmi, koeffitsientlar eng kichikmi.
export function gradeEquation(str, q) {
  if (typeof str !== "string" || str.length > 200) return { ok: false, msg: "Yozuv noto'g'ri." };
  let L, R;
  try {
    const p = str.split("→");
    if (p.length !== 2) throw new Error("strelka");
    L = parseSide(p[0]); R = parseSide(p[1]);
  } catch { return { ok: false, msg: "Yozuvda xato bor: formulalar va \"→\" belgisini tekshiring." }; }
  const key = (a) => a.map((x) => x.k).sort().join("|");
  const want = (a) => a.map((f) => canon(parseFormula(f))).sort().join("|");
  if (key(L) !== want(q.re)) return { ok: false, msg: "Reagentlar noto'g'ri." };
  if (key(R) !== want(q.pr)) return { ok: false, msg: "Reaksiya mahsulotlari noto'g'ri." };
  const tot = (side) => { const t = {}; side.forEach((x) => { for (const k in x.cnt) t[k] = (t[k] || 0) + x.cnt[k] * x.c; }); return t; };
  const a = tot(L), b = tot(R);
  for (const e of new Set([...Object.keys(a), ...Object.keys(b)])) {
    if (Math.abs((a[e] || 0) - (b[e] || 0)) > 1e-9) return { ok: false, msg: `Tenglama tenglashtirilmagan: ${e} atomlari chapda ${a[e] || 0} ta, o'ngda ${b[e] || 0} ta.` };
  }
  const all = [...L, ...R];
  if (all.every((x) => Number.isInteger(x.c)) && all.reduce((s, x) => gcd(s, x.c), 0) > 1) return { ok: false, msg: "Koeffitsientlarni eng kichik butun sonlarda yozing." };
  return { ok: true };
}

// ---------- tuzilish yig'ish (alkan: zanjir + o'rta uglerodlardagi metillar)
export const NAMES = ["", "metan", "etan", "propan", "butan", "pentan", "geksan", "geptan"];
export const PRE = ["", "metil", "dimetil", "trimetil", "tetrametil", "pentametil", "geksametil"];
export const MAXC = 7;

// Mijozdan kelgan tuzilishni tekshiradi: { n: 1..7, br: [[0|1,0|1] x 7] }, chetki uglerodlarda tarmoq yo'q.
export function normalizeStructure(input) {
  if (!input || !Number.isInteger(input.n) || input.n < 1 || input.n > MAXC) return null;
  const br = Array.from({ length: MAXC }, () => [0, 0]);
  if (!Array.isArray(input.br)) return null;
  for (let i = 0; i < MAXC; i++) {
    const row = input.br[i];
    if (row === undefined) continue;
    if (!Array.isArray(row) || row.length !== 2 || !row.every((v) => v === 0 || v === 1)) return null;
    if (row[0] + row[1] > 0 && (i === 0 || i >= input.n - 1)) return null;
    br[i] = [row[0], row[1]];
  }
  return { n: input.n, br };
}

export function buildName(s) {
  const loc = [];
  for (let i = 1; i < s.n - 1; i++) for (let j = 0; j < s.br[i][0] + s.br[i][1]; j++) loc.push(i + 1);
  if (!loc.length) return NAMES[s.n][0].toUpperCase() + NAMES[s.n].slice(1);
  const fw = loc.slice().sort((a, b) => a - b), rev = loc.map((p) => s.n + 1 - p).sort((a, b) => a - b);
  let use = fw;
  for (let i = 0; i < fw.length; i++) if (rev[i] !== fw[i]) { use = rev[i] < fw[i] ? rev : fw; break; }
  return use.join(",") + "-" + PRE[use.length] + NAMES[s.n];
}

export function gradeBuild(input, q) {
  const s = normalizeStructure(input);
  if (!s) return { ok: false, msg: "Tuzilish noto'g'ri yuborilgan." };
  const got = buildName(s);
  return { ok: got.toLowerCase() === q.build.toLowerCase(), got };
}

// Yig'ish maydonida hosil bo'lishi mumkin bo'lgan barcha nomlar (savol faylini tekshirish uchun)
export function buildableNames() {
  const set = new Set();
  for (let n = 1; n <= MAXC; n++) {
    const inner = Math.max(0, n - 2);
    for (let m = 0; m < 3 ** inner; m++) {
      const br = Array.from({ length: MAXC }, () => [0, 0]);
      let x = m;
      for (let i = 0; i < inner; i++) { const k = x % 3; x = Math.floor(x / 3); br[1 + i] = [k >= 1 ? 1 : 0, k === 2 ? 1 : 0]; }
      set.add(buildName({ n, br }).toLowerCase());
    }
  }
  return set;
}

// Qisqa tuzilish formulasi (javoblar kaliti uchun)
export function condensed(target) {
  for (let n = 1; n <= MAXC; n++) {
    const inner = Math.max(0, n - 2);
    for (let m = 0; m < 3 ** inner; m++) {
      const br = Array.from({ length: MAXC }, () => [0, 0]);
      const k = []; let x = m;
      for (let i = 0; i < inner; i++) { k.push(x % 3); x = Math.floor(x / 3); br[1 + i] = [k[i] >= 1 ? 1 : 0, k[i] === 2 ? 1 : 0]; }
      if (buildName({ n, br }).toLowerCase() === target.toLowerCase()) {
        return Array.from({ length: n }, (_, i) => (i === 0 || i === n - 1 ? "CH3" : k[i - 1] === 0 ? "CH2" : k[i - 1] === 1 ? "CH(CH3)" : "C(CH3)2")).join("–");
      }
    }
  }
  return "";
}

// ---------- takrorlanishni aniqlash uchun savol kaliti
export function questionKey(q) {
  if (q.type === "write") return "w:" + q.re.map((f) => canon(parseFormula(f))).sort().join("+") + ">" + q.pr.map((f) => canon(parseFormula(f))).sort().join("+");
  if (q.type === "build") return "b:" + q.build.toLowerCase();
  return "c:" + q.p + "|" + q.ok;
}
