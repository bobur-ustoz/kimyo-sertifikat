// Test-generator PDF in the look of the printed Kimyo books: Latin Modern serif, two columns with a
// rule between them, a green header band, option letters in roman and the option text slanted.
// Pure drawing code (no DOM), so the app and a Node preview share it. Fonts are registered by
// the caller as "LM" (normal/bold), "LMSl" (slanted) and "DejaVu" (symbols Latin Modern lacks).
const GREEN = [15, 81, 50], INK = [20, 20, 20], GRAY = [90, 100, 96], RULE = [150, 150, 150];
const PT = 0.3528;                      // 1 pt in mm

const SUB = { "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9", "ₐ": "a", "ₑ": "e", "ₒ": "o", "ₓ": "x", "ₕ": "h", "ₖ": "k", "ₗ": "l", "ₘ": "m", "ₙ": "n", "ₚ": "p", "ₛ": "s", "ₜ": "t", "₊": "+", "₋": "−" };
const SUP = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "−", "⁺": "+", "ⁿ": "n" };
// Glyphs Latin Modern has no outline for: drawn in the fallback font.
const FALLBACK = /[Α-ωΔ≤≥≈⇄↔⇌∆∞√∑∫∂≠≡⁄·]/;

// Uzbek apostrophes: oʻ / gʻ become the typographic ‘ (as in the books), any other ' becomes ’.
const typo = (s) => String(s ?? "")
  .replace(/([oOgG])[ʻʼ'’‘`´]/g, "$1‘")
  .replace(/[ʻʼ'`´]/g, "’")
  .replace(/[ \t\r\n]+/g, " ");

const ELEMENTS = new Set("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu R".split(" "));
// A chemical formula or element symbol (NaOH, H₂SO₄, Cu(OH)₂, Fe, CO₂, ²²⁶Ra, KMnO₄): every capital + lowercase
// pair must be a real element, so words like "Bu" or "Natriy" are left alone. Such "substances" are slanted.
const SUBC = Object.keys(SUB).join(""), SUPC = Object.keys(SUP).join("");
const PIECE = new RegExp(`([${SUPC}]*)([A-Z][a-z]?)([${SUBC}]*\\d*)|[()\\[\\]]|[${SUBC}${SUPC}]+|\\d+|[·+−-]`, "g");
const ROMAN = /^(?:I{1,3}|IV|VI{0,3}|IX|X)$/;      // "III valentli" is a number, not iodine
const isFormula = (w) => {
  if (!w || !/[A-Z]/.test(w) || ROMAN.test(w)) return false;
  let rest = w, hasEl = false;
  rest = rest.replace(PIECE, (m, sup, el) => { if (el) { if (!ELEMENTS.has(el)) return "\u0000"; hasEl = true; } return ""; });
  return hasEl && rest === "";
};

// text -> words, each word a list of runs { t, k: "n" | "sub" | "sup", f: "LM" | "DejaVu", b: bold, s: slanted }
function words(text, base) {
  const out = [];
  for (const chunk of typo(text).split(" ")) {
    if (!chunk) continue;
    // punctuation around a formula stays upright: "(NaOH)," -> ( NaOH ) ,
    let lead = "", core = chunk, trail = "";
    let m = core.match(/^(.*?)([.,;:?!»”’]*)$/); core = m[1]; trail = m[2];
    if (!isFormula(core)) {
      if (core.endsWith(")") && isFormula(core.slice(0, -1))) { trail = ")" + trail; core = core.slice(0, -1); }
      if (core.startsWith("(") && isFormula(core.slice(1))) { lead = "("; core = core.slice(1); }
    }
    const slant = !base.s && !base.plain && isFormula(core);
    const cur = [];
    const push = (t, k, f, sl) => { if (!t) return; const l = cur[cur.length - 1]; if (l && l.k === k && l.f === f && l.s === sl) l.t += t; else cur.push({ t, k, f, b: base.b, s: sl }); };
    const emit = (str, sl) => { for (const ch of str) {
      if (SUB[ch]) push(SUB[ch], "sub", "LM", sl);
      else if (SUP[ch]) push(SUP[ch], "sup", "LM", sl);
      else push(ch, "n", FALLBACK.test(ch) ? "DejaVu" : "LM", sl);
    } };
    emit(lead, !!base.s); emit(core, !!base.s || slant); emit(trail, !!base.s);
    if (cur.length) out.push(cur);
  }
  return out;
}

export function buildTestPdf(doc, { questions, brand = "nooracademy", label = "Aralash test", subtitle = "" }) {
  const W = doc.internal.pageSize.getWidth(), H = doc.internal.pageSize.getHeight();
  const mx = 14, gap = 9, colW = (W - mx * 2 - gap) / 2, bottom = H - 17;
  const SIZE = 10.5, LEAD = 4.95, SUBK = 0.7;

  const fontOf = (r) => r.f === "DejaVu" ? ["DejaVu", "normal"] : r.s ? ["LMSl", "normal"] : ["LM", r.b ? "bold" : "normal"];
  const runW = (r, size) => { const [f, st] = fontOf(r); doc.setFont(f, st); doc.setFontSize(r.k === "n" ? size : size * SUBK); return doc.getTextWidth(r.t); };
  const wordW = (w, size) => w.reduce((a, r) => a + runW(r, size), 0);
  const spaceW = (size, slanted) => { doc.setFont(slanted ? "LMSl" : "LM", "normal"); doc.setFontSize(size); return doc.getTextWidth(" "); };

  // Greedy wrap of runs into lines no wider than `width`; `first` is the indent of the first line.
  const wrap = (ws, width, size, first = 0) => {
    const lines = []; let line = [], x = first;
    const sp = spaceW(size, ws[0]?.[0]?.s);
    for (const w of ws) {
      const ww = wordW(w, size);
      if (line.length && x + sp + ww > width) { lines.push({ line, x0: lines.length ? 0 : first }); line = []; x = 0; }
      x += (line.length ? sp : 0) + ww; line.push(w);
    }
    if (line.length) lines.push({ line, x0: lines.length ? 0 : first });
    return lines.length ? lines : [{ line: [], x0: first }];
  };

  const drawRuns = (ws, x, y, size) => {
    const sp = spaceW(size, ws[0]?.[0]?.s);
    ws.forEach((w, i) => {
      w.forEach((r) => {
        const [f, st] = fontOf(r);
        doc.setFont(f, st); doc.setTextColor(...INK);
        const sz = r.k === "n" ? size : size * SUBK;
        doc.setFontSize(sz);
        const dy = r.k === "sub" ? size * 0.22 * PT : r.k === "sup" ? -size * 0.36 * PT : 0;
        doc.text(r.t, x, y + dy);
        x += doc.getTextWidth(r.t);
      });
      if (i < ws.length - 1) x += sp;
    });
  };

  // ---- one question -> { h, draw(x, y) } ----
  const layout = (q, n) => {
    const ops = []; let h = 0;
    const text = (ws, indent, width, size = SIZE, first = 0) => {
      wrap(ws, width - indent, size, first).forEach(({ line, x0 }) => {
        const yy = h + size * PT * 0.82; ops.push((x, y) => drawRuns(line, x + indent + x0, y + yy, size)); h += LEAD;
      });
    };
    // number (bold) + stem, as "29.  text"
    const num = words(`${n}.`, { b: true, plain: true });
    const numW = wordW(num[0], SIZE) + 1.6;
    const stem = words(q.question_text || "(savol matni kiritilmagan)", {});
    { // first line starts after the bold number
      const lines = wrap(stem, colW, SIZE, numW);
      lines.forEach(({ line, x0 }, i) => {
        const yy = h + SIZE * PT * 0.82;
        ops.push((x, y) => { if (i === 0) drawRuns(num, x, y + yy, SIZE); drawRuns(line, x + x0, y + yy, SIZE); });
        h += LEAD;
      });
    }
    if (q.formula) { h += 0.6; text(words(q.formula, {}), 5, colW); }

    const opts = q.question_type === "match"
      ? (q.option_groups?.options || []).map((o) => [o.letter, o.text])
      : q.question_type === "mcq" || !q.question_type
        ? ["a", "b", "c", "d"].map((l) => [l.toUpperCase(), q[`option_${l}`]]).filter(([, t]) => t != null && t !== "")
        : [];
    if (opts.length) {
      const cell = (L, t) => ({ lab: words(`${L})`, { plain: true })[0], ws: words(t, { s: true }) });
      const cells = opts.map(([L, t]) => cell(L, t));
      const labW = (c) => wordW(c.lab, SIZE) + 1.4;
      const oneW = (c) => labW(c) + c.ws.reduce((a, w, i) => a + wordW(w, SIZE) + (i ? spaceW(SIZE, true) : 0), 0);
      const drawCell = (c, x, y, yy) => { drawRuns([c.lab], x, y + yy, SIZE); drawRuns(c.ws, x + labW(c), y + yy, SIZE); };
      const fitsRow = cells.length === 4 && cells.every((c) => oneW(c) <= colW / 4 - 3.2);
      const fitsGrid = cells.length === 4 && cells.every((c) => oneW(c) <= colW / 2 - 3.5);
      if (fitsRow) {
        const yy = h + SIZE * PT * 0.82;
        ops.push((x, y) => cells.forEach((c, i) => drawCell(c, x + 3 + i * (colW - 3) / 4, y, yy))); h += LEAD;
      } else if (fitsGrid) {
        for (let r = 0; r < 2; r++) {
          const yy = h + SIZE * PT * 0.82;
          ops.push((x, y) => [0, 1].forEach((k) => drawCell(cells[r * 2 + k], x + 3 + k * (colW - 3) / 2, y, yy))); h += LEAD;
        }
      } else {
        cells.forEach((c) => {
          const lines = wrap(c.ws, colW - 3 - labW(c), SIZE);
          lines.forEach(({ line }, i) => {
            const yy = h + SIZE * PT * 0.82;
            ops.push((x, y) => { if (i === 0) drawRuns([c.lab], x + 3, y + yy, SIZE); drawRuns(line, x + 3 + labW(c), y + yy, SIZE); }); h += LEAD;
          });
        });
      }
    } else if (q.question_type && q.question_type !== "mcq") {
      const yy = h + SIZE * PT * 0.82 + 1.5;
      ops.push((x, y) => { drawRuns(words("Javob:", { b: true }), x, y + yy, SIZE); doc.setDrawColor(...INK); doc.setLineWidth(0.2); doc.line(x + 13, y + yy + 0.4, x + colW * 0.7, y + yy + 0.4); }); h += LEAD + 1.5;
    }
    return { h: h + 3.4, draw: (x, y) => ops.forEach((o) => o(x, y)) };
  };

  // ---- page furniture ----
  let page = 0;
  const header = () => {
    page++;
    doc.setFillColor(...GREEN); doc.roundedRect(mx, 11, 10, 10, 1.6, 1.6, "F");
    doc.setFont("LM", "bold"); doc.setFontSize(17); doc.setTextColor(255, 255, 255); doc.text("n", mx + 5, 18.4, { align: "center" });
    doc.setFont("LM", "bold"); doc.setFontSize(17); doc.setTextColor(...GREEN); doc.text(brand, mx + 13, 18.6);
    doc.setFont("LM", "bold"); doc.setFontSize(10.5);
    const pw = doc.getTextWidth(label) + 9;
    doc.setFillColor(...GREEN); doc.roundedRect(W - mx - pw, 12, pw, 7.4, 3.7, 3.7, "F");
    doc.setTextColor(255, 255, 255); doc.text(label, W - mx - pw / 2, 17, { align: "center" });
    doc.setFont("LM", "normal"); doc.setFontSize(10); doc.setTextColor(...GRAY);
    doc.text(String(page), W / 2, H - 9, { align: "center" });
  };
  const rule = (top) => { doc.setDrawColor(...RULE); doc.setLineWidth(0.25); doc.line(W / 2, top, W / 2, bottom); };

  header();
  let top = 25;
  if (subtitle) { doc.setFont("LM", "normal"); doc.setFontSize(9.5); doc.setTextColor(...GRAY); doc.text(subtitle, mx, 26.6); top = 30; }
  top += 3; rule(top);
  let col = 0, y = top;
  questions.forEach((q, i) => {
    const b = layout(q, i + 1);
    if (y + b.h > bottom && y > top) {
      if (col === 0) { col = 1; y = top; }
      else { doc.addPage(); header(); top = 28; rule(top); col = 0; y = top; }
    }
    b.draw(mx + col * (colW + gap), y); y += b.h;
  });
}
