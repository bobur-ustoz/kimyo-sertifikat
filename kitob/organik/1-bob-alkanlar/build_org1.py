# -*- coding: utf-8 -*-
"""Organik 1-bob (Organik kimyo nazariyasi. Alkanlar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_III1A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_III1B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#00796b", "#004d43", "#eef8f6", "#ef6c00"

SVG_CURVES = {
    "rise":      ("M22,82 C55,68 95,40 126,22", None),
    "flat":      ("M22,44 L126,44", None),
    "fall":      ("M22,22 C55,36 95,64 126,82", None),
    "rise_flat": ("M22,82 L70,34 L126,34", (70, 34)),
    "rise_fall": ("M22,78 Q74,10 126,78", None),
    "u":         ("M22,26 Q74,92 126,26", None),
}
def svg(curve, xlab="t", ylab="v"):
    p, knee = SVG_CURVES[curve]
    grid = "".join(f'<line x1="{x}" y1="16" x2="{x}" y2="86" class="gr"/>' for x in range(43, 127, 21)) + \
           "".join(f'<line x1="22" y1="{y}" x2="126" y2="{y}" class="gr"/>' for y in range(16, 86, 17))
    km = ""
    if knee:
        kx, ky = knee
        km = (f'<line x1="{kx}" y1="{ky}" x2="{kx}" y2="86" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>'
              f'<circle cx="{kx}" cy="{ky}" r="2.6" fill="{ACCENT}"/>')
    return ('<svg width="118" height="86" viewBox="0 0 152 100">'
            '<style>.gr{stroke:#e3e3e3;stroke-width:0.7}.ax{stroke:#222;stroke-width:1.4}'
            '.lb{font-size:10px;font-family:Georgia,serif;fill:#222}</style>'
            f'{grid}'
            '<line x1="22" y1="86" x2="132" y2="86" class="ax"/><polygon points="132,86 125,83 125,89" fill="#222"/>'
            '<line x1="22" y1="86" x2="22" y2="8" class="ax"/><polygon points="22,8 19,15 25,15" fill="#222"/>'
            f'<text x="4" y="14" class="lb">{ylab}</text><text x="98" y="98" class="lb">{xlab}</text>'
            f'{km}<path d="{p}" fill="none" stroke="#00796b" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- III.1 figuralari (feruza + apelsin palitrasi) ----------
I1, I2, ID, IP, IG = "#00796b", "#ef6c00", "#004d43", "#eef8f6", "#c6e5e0"

def fig_bp_alkan():
    """Alkanlar qaynash haroratlari — chiziqli grafik."""
    data = [("CH₄", -162), ("C₂H₆", -89), ("C₃H₈", -42), ("C₄H₁₀", -0.5), ("C₅H₁₂", 36)]
    lo, hi = -190, 60
    pts = []; marks = ""
    for i, (lab, v) in enumerate(data):
        x = 56 + i * 48; y = 118 - (v - lo) / (hi - lo) * 100
        pts.append(f"{x},{y:.0f}")
        vt = str(int(v)) if float(v).is_integer() else str(v)
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{vt}</text>'
                  f'<text x="{x}" y="136" text-anchor="middle" class="lb">{lab}</text>')
    y0 = 118 - (0 - lo) / (hi - lo) * 100
    return ('<svg width="280" height="146" viewBox="0 0 280 146">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="4" width="236" height="116" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="42" y1="{y0:.0f}" x2="274" y2="{y0:.0f}" stroke="{IG}" stroke-width="1" stroke-dasharray="4,3"/>'
            f'<text x="246" y="{y0-4:.0f}" class="lb">0 °C</text>'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="40" y1="120" x2="276" y2="120" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">t(qayn.), °C</text></svg>')

def fig_bar_gas():
    """Tabiiy gaz tarkibi — ustunlar."""
    data = [("CH₄", 93), ("C₂H₆", 4), ("boshqalar", 3)]
    mx = 100
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 62; h = max(v / mx * 108, 4); y = 124 - h
        col = I2 if i == 0 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.88" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+18}" y="137" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="260" height="148" viewBox="0 0 260 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="48" y="4" width="206" height="120" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="50" y1="{124-g/100*108:.0f}" x2="252" y2="{124-g/100*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="34" y="{127-g/100*108:.0f}" class="lb">{g}</text>' for g in [25, 50, 75])
            + bars +
            f'<line x1="48" y1="124" x2="254" y2="124" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ulush, %</text></svg>')

def fig_isomers():
    """C5H12 uch izomeri: n-pentan, izopentan, neopentan (chiziqli sxema)."""
    def chain(x0, y0, pts, branches=""):
        s = ""
        for i in range(len(pts) - 1):
            s += f'<line x1="{pts[i][0]}" y1="{pts[i][1]}" x2="{pts[i+1][0]}" y2="{pts[i+1][1]}" stroke="{ID}" stroke-width="1.8"/>'
        for px, py in pts:
            s += f'<circle cx="{px}" cy="{py}" r="3.2" fill="{I1}"/>'
        return s + branches
    # 1) n-pentan
    p1 = [(24 + i * 18, 40 + (8 if i % 2 else 0)) for i in range(5)]
    # 2) izopentan (4 zanjir + metil 2-da)
    p2 = [(140 + i * 18, 40 + (8 if i % 2 else 0)) for i in range(4)]
    b2 = (f'<line x1="{p2[1][0]}" y1="{p2[1][1]}" x2="{p2[1][0]}" y2="{p2[1][1]-20}" stroke="{ID}" stroke-width="1.8"/>'
          f'<circle cx="{p2[1][0]}" cy="{p2[1][1]-20}" r="3.2" fill="{I2}"/>')
    # 3) neopentan (markaziy C + 4 metil)
    cx, cy = 76, 102
    b3 = ""
    for dx, dy in [(-18, 0), (18, 0), (0, -18), (0, 18)]:
        b3 += (f'<line x1="{cx}" y1="{cy}" x2="{cx+dx}" y2="{cy+dy}" stroke="{ID}" stroke-width="1.8"/>'
               f'<circle cx="{cx+dx}" cy="{cy+dy}" r="3.2" fill="{I2}"/>')
    b3 += f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{I1}"/>'
    return ('<svg width="270" height="140" viewBox="0 0 270 140">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + chain(0, 0, p1) + '<text x="30" y="70" class="lb" font-weight="bold">1) n-pentan</text>'
            + chain(0, 0, p2, b2) + '<text x="140" y="70" class="lb" font-weight="bold">2) izopentan</text>'
            + b3 + '<text x="120" y="106" class="lb" font-weight="bold">3) neopentan</text>'
            + '<text x="120" y="118" class="lb">(2,2-dimetilpropan)</text>'
            '<text x="8" y="14" class="lb" font-weight="bold">C₅H₁₂ izomerlari (• — uglerod)</text></svg>')

def fig_scheme38():
    """B O1-38: noma'lum alkan yonish sxemasi."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="6" y="22" width="80" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="46" y="38" text-anchor="middle" class="lb" font-weight="bold">CₓH? · 6,72 L</text>'
            '<text x="46" y="50" text-anchor="middle" class="lb">noma\'lum alkan</text>'
            f'<line x1="86" y1="39" x2="116" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="120,39 112,35 112,43" fill="{I2}"/>'
            f'<text x="88" y="29" class="lb" fill="{I2}">+O₂, yonish</text>'
            f'<rect x="122" y="22" width="70" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="157" y="42" text-anchor="middle" class="lb" font-weight="bold">0,9 mol CO₂</text>'
            f'<line x1="192" y1="39" x2="218" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="222,39 214,35 214,43" fill="{I2}"/>'
            f'<rect x="224" y="22" width="52" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="250" y="42" text-anchor="middle" class="lb" font-weight="bold">M = ?</text></svg>')

def fig_stove():
    """Gaz plita ko'k alangasi."""
    return ('<svg width="220" height="118" viewBox="0 0 220 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="36" y="76" width="120" height="10" rx="3" fill="#546e7a"/>'
            f'<rect x="80" y="66" width="32" height="10" rx="3" fill="#37474f"/>'
            + "".join(f'<path d="M{x},64 q-4,-10 0,-18 q4,8 0,18" fill="#42a5f5" stroke="#1565c0" stroke-width="0.8"/>'
                      for x in [84, 92, 100, 108])
            + '<text x="130" y="40" class="lb" font-weight="bold">ko\'k alanga —</text>'
            '<text x="130" y="52" class="lb">to\'liq yonish</text>'
            '<text x="36" y="104" class="lb">CH₄ + 2O₂ → CO₂ + 2H₂O</text>'
            '<text x="36" y="116" class="lb" font-weight="bold">gaz plita</text></svg>')

def fig_balloon_gas():
    """Propan-butan balloni."""
    return ('<svg width="220" height="120" viewBox="0 0 220 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="52" y="30" width="44" height="70" rx="14" fill="#ef9a9a" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="66" y="18" width="16" height="14" rx="3" fill="#8d6e63"/>'
            f'<rect x="60" y="54" width="28" height="18" rx="2" fill="#fff" stroke="{IG}" stroke-width="0.8"/>'
            '<text x="74" y="66" text-anchor="middle" class="lb" font-size="6.4">C₃H₈+C₄H₁₀</text>'
            '<text x="110" y="42" class="lb" font-weight="bold">bosim ostida</text>'
            '<text x="110" y="54" class="lb">suyultirilgan gaz</text>'
            '<text x="110" y="72" class="lb">kam hajm —</text>'
            '<text x="110" y="84" class="lb">ko\'p energiya</text>'
            '<text x="50" y="116" class="lb" font-weight="bold">propan-butan balloni</text></svg>')

def fig_oilrig():
    """Neft qudug'i (nasos)."""
    return ('<svg width="220" height="120" viewBox="0 0 220 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<line x1="40" y1="96" x2="120" y2="96" stroke="{ID}" stroke-width="2"/>'
            f'<path d="M70,96 l14,-40 l14,40" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<line x1="56" y1="52" x2="116" y2="60" stroke="{ID}" stroke-width="3"/>'
            f'<path d="M52,50 a7,9 0 1 0 8,6" fill="{I2}"/>'
            f'<line x1="114" y1="60" x2="114" y2="88" stroke="{ID}" stroke-width="1.8"/>'
            f'<ellipse cx="114" cy="94" rx="9" ry="4" fill="#3e2723"/>'
            '<text x="132" y="46" class="lb" font-weight="bold">neft —</text>'
            '<text x="132" y="58" class="lb">uglevodorodlar</text>'
            '<text x="132" y="70" class="lb">aralashmasi</text>'
            '<text x="40" y="114" class="lb" font-weight="bold">neft qudug\'i</text></svg>')

def fig_gasleak():
    """Gaz hidi — odorant haqida."""
    return ('<svg width="220" height="116" viewBox="0 0 220 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<circle cx="64" cy="44" r="16" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<circle cx="58" cy="40" r="2" fill="{ID}"/><circle cx="70" cy="40" r="2" fill="{ID}"/>'
            f'<path d="M58,52 q6,-4 12,0" fill="none" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M60,26 q2,-6 8,-6" fill="none" stroke="{ID}" stroke-width="1.2"/>'
            + "".join(f'<path d="M{x},64 q4,-6 0,-12 q-4,-6 0,-12" fill="none" stroke="{I2}" stroke-width="1.6" transform="rotate(90 {x} 52)"/>'
                      for x in [104, 116, 128])
            + '<text x="104" y="34" class="lb" font-weight="bold" fill="' + I2 + '">«gaz hidi»</text>'
            '<text x="104" y="78" class="lb">merkaptan-odorant:</text>'
            '<text x="104" y="90" class="lb">sizishni sezdiradi</text>'
            '<text x="42" y="110" class="lb" font-weight="bold">metan aslida hidsiz!</text></svg>')

FIGS = dict(bp_alkan=fig_bp_alkan, bar_gas=fig_bar_gas, isomers=fig_isomers, scheme38=fig_scheme38,
            stove=fig_stove, balloon_gas=fig_balloon_gas, oilrig=fig_oilrig, gasleak=fig_gasleak)

def table_from_markup(text):
    if "[JADVAL]" not in text:
        return html.escape(text).replace("\n", "<br>"), ""
    before, tbl = text.split("[JADVAL]", 1)
    rest = ""
    if "\n" in tbl:
        tbl, rest = tbl.split("\n", 1)
    rows = [r.strip() for r in tbl.split(";;")]
    h = ['<table class="jt">']
    for i, r in enumerate(rows):
        cells = [c.strip() for c in r.split("|")]
        tag = "th" if i == 0 else "td"
        h.append("<tr>" + "".join(f"<{tag}>{html.escape(c)}</{tag}>" for c in cells) + "</tr>")
    h.append("</table>")
    out = html.escape(before.strip()).replace("\n", "<br>")
    tail = html.escape(rest.strip()).replace("\n", "<br>") if rest.strip() else ""
    return out, "".join(h) + (f"<p class='tt'>{tail}</p>" if tail else "")

css = f"""
@page {{ size: A4; margin: 15mm 14mm 17mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: 'DejaVu Serif', Georgia, serif; font-size: 9.6pt; line-height: 1.36; color:#1c1c1c; margin:0; }}
.page {{ height: 263.5mm; page-break-after: always; position: relative; overflow: hidden; }}
.chap {{ background: linear-gradient(180deg, {TINT} 0 46mm, #fff 46mm); }}
.chap .chapnum {{ font-family:'DejaVu Sans',Arial,sans-serif; font-size: 64pt; font-weight: bold;
                  color:{ACCENT}; opacity: 0.18; position:absolute; top: 4mm; right: 12mm;}}
.chap .kicker {{ font-family:'DejaVu Sans',Arial,sans-serif; letter-spacing:2.5px; font-size:9.5pt;
                 color:{ACCENT}; text-transform:uppercase; font-weight:bold; margin-top: 6mm;}}
.chap h1 {{ font-size: 30pt; margin: 2mm 0 2mm; color:#12222e;}}
.chap .lead {{ font-size: 11pt; font-style: italic; color:#456; margin-bottom: 10mm;}}
.pass {{ display:flex; gap: 5mm; }}
.pass .card {{ flex:1; border: 0.9pt solid #c8d8e4; border-radius: 2mm; padding: 3.5mm 4mm; background:#fff;}}
.pass .card h3 {{ font-family:'DejaVu Sans',Arial,sans-serif; font-size: 9.6pt; color:{ACCENT};
                  margin: 0 0 1.6mm; text-transform: uppercase; letter-spacing: 0.8px;}}
.pass .card ul {{ margin: 0; padding-left: 4.5mm; font-size: 9.1pt;}}
.pass .card li {{ margin: 0.9mm 0; }}
.chap table.spec {{ border-collapse: collapse; margin-top: 7mm; width:100%;}}
.chap table.spec td, .chap table.spec th {{ border: 0.8pt solid #9db4c4; padding: 1.9mm 3.5mm; font-size: 9.3pt; text-align:center;}}
.chap table.spec th {{ background:{ACCENT}; color:#fff; font-family:'DejaVu Sans',Arial,sans-serif;}}
.sec {{ column-span: all; background:{ACCENT}; color:#fff; font-family:'DejaVu Sans',Arial,sans-serif;
        font-weight:bold; font-size: 10.6pt; padding: 2mm 4mm; border-radius: 1.2mm;
        margin: 0 0 3mm; page-break-after: avoid; letter-spacing:0.4px;}}
.sec small {{ font-weight:normal; opacity:0.85; }}
.cols {{ column-count: 2; column-gap: 7mm; column-rule: 0.6pt solid #d5dde3; }}
.q {{ margin: 0 0 3mm; page-break-inside: avoid; break-inside: avoid; }}
.qn {{ font-family:'DejaVu Sans',Arial,sans-serif; font-weight: bold; color:{ACCENT}; }}
.opts {{ margin: 0.8mm 0 0 3.5mm; }}
.opts div {{ margin: 0.3mm 0; }}
.opts-inline {{ margin: 0.8mm 0 0 3.5mm; }}
.opts b, .opts-inline b {{ font-family:'DejaVu Sans',Arial,sans-serif; font-size:8.8pt; color:#333;}}
.gopts {{ display:flex; gap:3mm; margin:1.6mm 0 0.5mm; flex-wrap: wrap;}}
.gopts .go {{ text-align:center; font-family:'DejaVu Sans',Arial,sans-serif; font-weight:bold; font-size:9pt;}}
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bcded8; border-radius:2pt;
                  background:#eef8f6; padding:1mm;}}
table.jt {{ border-collapse: collapse; margin: 1.6mm 0; }}
table.jt th, table.jt td {{ border: 0.8pt solid #9db4c4; padding: 0.8mm 2.4mm; font-size: 9pt; text-align:center;}}
table.jt th {{ background:#e8eff5; font-family:'DejaVu Sans',Arial,sans-serif; font-size:8.6pt;}}
.tt {{ margin: 1mm 0; }}
.scen {{ background:{TINT}; border-left: 2.5pt solid {ACCENT}; padding: 2.5mm 3.5mm; margin: 0 0 2.5mm;
         border-radius: 0 1.5mm 1.5mm 0; page-break-inside: avoid;}}
.ansrow {{ font-family:'DejaVu Sans',Arial,sans-serif; font-size: 9pt; margin: 1mm 0 3mm;}}
.o1line {{ border-bottom: 0.8pt dotted #999; display:inline-block; min-width: 22mm;}}
.band {{ margin: 1mm 0 1mm 4mm; }}
.chip {{ font-family:'DejaVu Sans',Arial,sans-serif; font-size: 7.8pt; background:{TINT}; color:{ACCENT};
         border: 0.7pt solid #b9cad6; padding: 0.2mm 1.8mm; border-radius: 8mm; white-space:nowrap;}}
.o2 {{ border: 0.9pt solid #c8d2da; border-radius: 2mm; padding: 3mm 3.5mm; margin-bottom: 3.5mm; page-break-inside: avoid;}}
.o2 .head {{ font-family:'DejaVu Sans',Arial,sans-serif; font-weight:bold; color:{ACCENT}; margin-bottom: 1.5mm; font-size: 10pt;}}
.anss {{ border-collapse: collapse; margin: 2mm 0;}}
.anss td, .anss th {{ border: 0.8pt solid #9db4c4; padding: 0.9mm 2.1mm; font-size: 9pt; text-align:center;}}
.anss th {{ background:{ACCENT}; color:#fff; font-family:'DejaVu Sans',Arial,sans-serif; font-size:8.4pt;}}
.sol {{ font-size: 8.9pt; margin: 0 0 1.9mm; }}
.sol b.n {{ color:{ACCENT}; font-family:'DejaVu Sans',Arial,sans-serif;}}
.small {{ font-size: 8.2pt; color:#555;}}
h2.fm {{ font-family:'DejaVu Sans',Arial,sans-serif; color:{ACCENT}; font-size: 16pt; margin: 0 0 5mm;
         border-bottom: 1.4pt solid {ACCENT}; padding-bottom: 2mm;}}
"""

letters = "ABCD"
H = [f"<meta charset='utf-8'><title>Organik 1-bob — Alkanlar</title><style>{css}</style>"]

def render_variant(data, tag, star, izoh):
    qs = data["savollar"]
    y1 = [q for q in qs if q.get("tur") == "Y1"]
    y2 = next(q for q in qs if q.get("tur") == "Y2")
    o1 = [q for q in qs if q.get("tur") == "O1"]
    o2 = [q for q in qs if q.get("tur") == "O2"]

    H.append(f"<div style='page-break-before:always'></div>")
    H.append(f"<h2 class='fm'>{tag}-VARIANT · {star} <span style='font-size:10pt;color:#555;font-weight:normal'>— {izoh}</span></h2>")
    H.append(f"<div class='sec'>1-QISM · YOPIQ TEST <small>(1–32 · to'rt variantdan bittasi to'g'ri)</small></div>")
    H.append("<div class='cols'>")
    for q in y1:
        txt, tbl = table_from_markup(q["savol"])
        H.append(f"<div class='q'><span class='qn'>{q['n']}.</span> {txt}{tbl}")
        if q.get("fig"):
            H.append(f"<div style='text-align:center;margin:1.6mm 0'>{FIGS[q['fig']]()}</div>")
        if q.get("svg"):
            s = q["svg"]
            corr = q["javob"]
            d_iter = iter([s["d1"], s["d2"], s["d3"]])
            curves = {L: (s["correct"] if L == corr else next(d_iter)) for L in letters}
            H.append("<div class='gopts'>" + "".join(
                f"<div class='go'>{svg(curves[L], s.get('xlab','t'), s.get('ylab','v'))}{L})</div>" for L in letters) + "</div>")
        else:
            total = sum(len(v) for v in q["variantlar"])
            if total <= 24:
                H.append("<div class='opts-inline'>" + " &nbsp; ".join(
                    f"<b>{letters[i]})</b> {html.escape(v)}" for i, v in enumerate(q["variantlar"])) + "</div>")
            else:
                H.append("<div class='opts'>" + "".join(
                    f"<div><b>{letters[i]})</b> {html.escape(v)}</div>" for i, v in enumerate(q["variantlar"])) + "</div>")
        H.append("</div>")
    H.append("</div>")

    H.append("<div class='sec' style='margin-top:4mm'>2-QISM · GURUHLANGAN SAVOL <small>(33–35 · A–F ro'yxatidan tanlang)</small></div>")
    H.append(f"<div class='scen'>{html.escape(y2['matn_umumiy'])}</div>")
    if y2.get("fig"):
        H.append(f"<div style='text-align:center;margin:1.6mm 0'>{FIGS[y2['fig']]()}</div>")
    for s in y2["savollar_ichki"]:
        H.append(f"<div class='q'><b>{html.escape(s)}</b></div>")
    H.append("<div class='ansrow'><b>Javoblar ro'yxati:</b> &nbsp;" +
             " &nbsp;·&nbsp; ".join(html.escape(x) for x in y2["javoblar_royxati"]) + "</div>")

    H.append("<div class='sec' style='margin-top:4mm'>3-QISM · QISQA JAVOBLI SAVOLLAR <small>(36–40)</small></div>")
    for q in o1:
        H.append(f"<div class='q'><span class='qn'>{q['n']}.</span> {html.escape(q['savol'])} "
                 f"&nbsp; <i>Javob:</i> <span class='o1line'>&nbsp;</span>")
        if q.get("fig"):
            H.append(f"<div style='text-align:center;margin:1.6mm 0'>{FIGS[q['fig']]()}</div>")
        H.append("</div>")

    H.append("<div class='sec' style='margin-top:4mm'>4-QISM · YOZMA ISH <small>(41–43 · har biri 25 ball)</small></div>")
    for q in o2:
        txt, tbl = table_from_markup(q["matn"])
        H.append(f"<div class='o2'><div class='head'>{q['n']}-topshiriq</div><div>{txt}</div>{tbl}")
        if q.get("fig"):
            H.append(f"<div style='text-align:center;margin:1.6mm 0'>{FIGS[q['fig']]()}</div>")
        for b in q["bandlar"]:
            pts = b["M"] + b["A"]
            lab = f"M{b['M']}+A{b['A']}" if b["A"] else f"M{b['M']}"
            H.append(f"<div class='band'>{html.escape(b['savol'])} <span class='chip'>{pts} ball · {lab}</span></div>")
        H.append("</div>")

    # kalit
    H.append("<div style='page-break-before:always'></div>")
    H.append(f"<h2 class='fm'>{tag}-variant · Javoblar kaliti va yechimlar</h2>")
    H.append("<table class='anss'><tr><th>№</th>" + "".join(f"<td>{q['n']}</td>" for q in y1[:16]) + "</tr>"
             "<tr><th>Javob</th>" + "".join(f"<td><b>{q['javob']}</b></td>" for q in y1[:16]) + "</tr></table>")
    H.append("<table class='anss'><tr><th>№</th>" + "".join(f"<td>{q['n']}</td>" for q in y1[16:]) + "</tr>"
             "<tr><th>Javob</th>" + "".join(f"<td><b>{q['javob']}</b></td>" for q in y1[16:]) + "</tr></table>")
    jv = y2["javoblar"]
    H.append(f"<p class='ansrow'><b>33–35:</b> 33 → {jv['33']}, 34 → {jv['34']}, 35 → {jv['35']} &nbsp;·&nbsp; "
             "<b>36–40:</b> " + ", ".join(f"{q['n']} → {q['javob']}" for q in o1) + "</p>")
    H.append("<div class='cols'>")
    for q in y1:
        H.append(f"<div class='sol'><b class='n'>{q['n']}.</b> <b>({q['javob']})</b> {html.escape(q['yechim'])}</div>")
    H.append(f"<div class='sol'><b class='n'>33–35.</b> {html.escape(y2['yechim'])}</div>")
    for q in o1:
        H.append(f"<div class='sol'><b class='n'>{q['n']}.</b> {html.escape(q['yechim'])}</div>")
    H.append("</div>")
    for q in o2:
        H.append(f"<div class='sol' style='margin-top:2mm'><b class='n'>{q['n']}-topshiriq.</b> " + " ".join(
            f"<b>{html.escape(b['savol'])}</b> {html.escape('; '.join(b['yechim']))}." for b in q["bandlar"]) + "</div>")
    H.append(f"<p class='small'>Manba: {html.escape(data['manba'])}</p>")

# BOB OCHUVCHI
H.append(f"""
<div class="page chap">
  <div class="chapnum">1</div>
  <div class="kicker">2-kitob · Organik kimyo · 1-bob · Mavzu pasporti (III.1)</div>
  <h1>Organik kimyo nazariyasi. Alkanlar</h1>
  <div class="lead">Butlerov nazariyasi · gomologiya va izomeriya · alkanlar: nomenklatura, xossalar,
  olinishi · sikloalkanlar · tabiiy gaz va neft</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>gomolog-izomer farqini bilish (A: 6, 7; B: 7)</li>
      <li>formula topish: M, zichlik, ω(C), yonish (B: 2, 3, 4, 38)</li>
      <li>IUPAC nomenklaturasi (A: 25; B: 13, 19)</li>
      <li>yonish hisoblari va aralashmalar (B: 11, 21, 23, 36)</li>
      <li>xlorlash va sanoat jarayonlari (B: 6, 17, 22, 25)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>izomerlar sxemasi (B: 5, 19, 28)</li>
      <li>qaynash haroratlari grafigi (A: 28; B: 26, 32)</li>
      <li>tabiiy gaz tarkibi ustunlari (A: 26, 32)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>gomolog bilan izomerni almashtirish</li>
      <li>CₙH₂ₙ₊₂ va CₙH₂ₙ ni chalkashtirish</li>
      <li>yonishda koeffitsiyentlarni unutish</li>
      <li>nomlashda raqamlashni katta uchidan boshlash</li></ul></div>
  </div>
  <table class="spec">
    <tr><th>Qism</th><th>Topshiriqlar</th><th>Turi</th><th>Vaqt</th></tr>
    <tr><td>1</td><td>1–32</td><td>Y1 — yopiq test (A–D)</td><td rowspan="3">100 daqiqa</td></tr>
    <tr><td>2</td><td>33–35</td><td>Y2 — moslashtirish (A–F)</td></tr>
    <tr><td>3</td><td>36–40</td><td>O1 — qisqa javob</td></tr>
    <tr><td>4</td><td>41–43</td><td>O2 — yozma ish (har biri 25 ball)</td><td>80 daqiqa</td></tr>
  </table>
</div>""")

render_variant(data_A, "A", "O'RGATUVCHI ★★", "soddaroq, rasm va hayotiy misollar bilan — mavzuni o'rgatadi")
render_variant(data_B, "B", "HAQIQIY MS MUHITI ★★★", "imtihon darajasi: ko'p bosqichli hisoblar va tuzoqlar")

open("bob.html", "w", encoding="utf-8").write("".join(H))
print("bob.html tayyor")
