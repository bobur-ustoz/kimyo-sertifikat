// Analog-question worksheet PDF: the question and its four options, nothing else (no solution, no answer). Pure drawing code (no DOM) so the app and a Node preview use
// the same file. `T` flattens text when no Unicode font is available.
const GREEN = [15, 81, 50], TEAL = [13, 148, 136], MINT = [240, 253, 244], SOFT = [209, 250, 229], BORDER = [134, 239, 172];
const GRAY = [100, 116, 139], INK = [15, 23, 42], WHITE = [255, 255, 255], LINE = [226, 232, 240];

// "stem ... A) x; B) y; C) z; D) w"  ->  { stem, opts:{A,B,C,D} } (null when it does not look like that)
export function splitOptions(text) {
  const t = String(text || "").replace(/\s+/g, " ").trim();
  const i = t.search(/(?:Variantlar:\s*)?A\)\s/);
  if (i < 0) return null;
  const stem = t.slice(0, i).replace(/[\s:]+$/, "");
  const parts = t.slice(i).replace(/^Variantlar:\s*/i, "").split(/\s*([ABCD])\)\s*/).slice(1);
  const opts = {};
  for (let k = 0; k + 1 < parts.length; k += 2) opts[parts[k]] = parts[k + 1].replace(/[;\s]+$/, "");
  return ["A", "B", "C", "D"].every(l => opts[l]) ? { stem, opts } : null;
}

export function buildAnalogPdf(doc, { font, T, analog, teacher, variant, qNum, topic }) {
  const W = doc.internal.pageSize.getWidth(), H = doc.internal.pageSize.getHeight(), mx = 18, tw = W - mx * 2;
  let y = 0;
  const fill = c => doc.setFillColor(...c), ink = c => doc.setTextColor(...c), stroke = c => doc.setDrawColor(...c);
  const txt = (s, x, yy, size, { bold = false, color = INK, align = "left" } = {}) => { doc.setFont(font, bold ? "bold" : "normal"); doc.setFontSize(size); ink(color); doc.text(T(s), x, yy, { align }); };
  const wrap = (s, size, width, bold = false) => { doc.setFont(font, bold ? "bold" : "normal"); doc.setFontSize(size); return doc.splitTextToSize(T(s), width); };
  const lh = size => size * 0.5 + 2.4;

  const header = (tag) => {
    fill(MINT); doc.rect(0, 0, W, 26, "F");
    fill(SOFT); doc.circle(W - 52, 13, 5.5, "F"); fill(BORDER); doc.circle(W - 64, 8, 2.6, "F"); fill(SOFT); doc.circle(W - 70, 19, 1.8, "F");
    fill(GREEN); doc.rect(0, 26, W, 1.6, "F");
    fill(GREEN); doc.circle(mx + 5, 13, 5.2, "F"); txt("n", mx + 5, 15.4, 12, { bold: true, color: WHITE, align: "center" });
    txt("nooracademy", mx + 13, 15, 15, { bold: true, color: GREEN });
    // tag pill
    doc.setFont(font, "bold"); doc.setFontSize(8.5); const w = doc.getTextWidth(T(tag)) + 9;
    fill(GREEN); doc.roundedRect(W - mx - w, 8, w, 9, 4.5, 4.5, "F"); txt(tag, W - mx - w / 2, 14, 8.5, { bold: true, color: WHITE, align: "center" });
    y = 40;
  };
  const newPage = tag => { doc.addPage(); header(tag); };
  const need = (h, tag) => { if (y + h > H - 20) newPage(tag); };

  const chip = (label, x) => {
    doc.setFont(font, "bold"); doc.setFontSize(9); const w = doc.getTextWidth(T(label)) + 10;
    fill(MINT); stroke(BORDER); doc.setLineWidth(0.3); doc.roundedRect(x, y, w, 8, 4, 4, "FD"); txt(label, x + w / 2, y + 5.5, 9, { bold: true, color: GREEN, align: "center" });
    return x + w + 3;
  };
  const sectionLabel = (label, color = TEAL) => { fill(color); doc.roundedRect(mx, y - 3.2, 3, 4.6, 1.2, 1.2, "F"); txt(label, mx + 6, y + 0.6, 9.5, { bold: true, color }); y += 8; };

  // ---------- page 1: the task ----------
  const TAG1 = `ANALOG · ${qNum}-savol`;
  header(TAG1);
  txt("Analog misol", mx, y, 22, { bold: true, color: GREEN }); y += 10;
  let cx = mx; cx = chip(`${teacher.name}`, cx); cx = chip(`${variant}-variant`, cx); cx = chip(`${qNum}-savol`, cx);
  if (topic) chip(topic, cx);
  y += 18;

  sectionLabel("SAVOL");
  const parsed = splitOptions(analog.savol), stem = parsed ? parsed.stem : analog.savol, qLines = wrap(stem, 12.5, tw - 14);
  const qh = qLines.length * lh(12.5) + 10;
  need(qh + 6, TAG1);
  fill(WHITE); stroke(LINE); doc.setLineWidth(0.4); doc.roundedRect(mx, y, tw, qh, 3, 3, "FD");
  fill(TEAL); doc.roundedRect(mx, y, 3.2, qh, 1.6, 1.6, "F");
  qLines.forEach((l, i) => txt(l, mx + 9, y + 8 + i * lh(12.5), 12.5, { color: INK }));
  y += qh + 8;

  if (parsed) {
    sectionLabel("VARIANTLAR");
    const cw = (tw - 6) / 2;
    for (let r = 0; r < 2; r++) {
      const pair = [["A", "B"], ["C", "D"]][r].map(L => ({ L, ls: wrap(parsed.opts[L], 11.5, cw - 18) }));
      const h = Math.max(...pair.map(p => p.ls.length)) * lh(11.5) + 8;
      need(h + 4, TAG1);
      pair.forEach((p, i) => {
        const x = mx + i * (cw + 6);
        fill(WHITE); stroke(BORDER); doc.setLineWidth(0.5); doc.roundedRect(x, y, cw, h, 3, 3, "FD");
        fill(MINT); doc.circle(x + 8, y + h / 2, 4.4, "F"); txt(p.L, x + 8, y + h / 2 + 1.6, 10.5, { bold: true, color: GREEN, align: "center" });
        const top = y + (h - p.ls.length * lh(11.5)) / 2 + 4.6; p.ls.forEach((l, k) => txt(l, x + 16, top + k * lh(11.5), 11.5, { color: INK }));
      });
      y += h + 4;
    }
    y += 6;
  }


  // footer on every page
  const n = doc.getNumberOfPages();
  for (let i = 1; i <= n; i++) {
    doc.setPage(i); stroke(LINE); doc.setLineWidth(0.3); doc.line(mx, H - 14, W - mx, H - 14);
    txt("nooracademy", mx, H - 8.5, 8.5, { bold: true, color: GREEN }); txt(`${i} / ${n}`, W - mx, H - 8.5, 8.5, { color: GRAY, align: "right" });
  }
}
