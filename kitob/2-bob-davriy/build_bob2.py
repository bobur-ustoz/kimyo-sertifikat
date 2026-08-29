# -*- coding: utf-8 -*-
"""2-bob (Davriy qonun) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I2A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I2B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#14507a", "#0d3550", "#eef4f8", "#b03a2e"

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
            f'{km}<path d="{p}" fill="none" stroke="#00695c" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.2 figuralari (teal-koral palitrasi) ----------
T1, T2, TD, TP, TG = "#00695c", "#d35400", "#004d40", "#eef7f5", "#cde5e0"

def fig_radius_line():
    """B: 3-davr atom radiuslari (pm) — chiziq + markerlar."""
    data = [("Na", 190), ("Mg", 160), ("Al", 143), ("Si", 118), ("P", 110), ("S", 104), ("Cl", 99)]
    def X(i): return 44 + i * 29
    def Y(r): return 138 - (r - 80) * 1.05
    path = "M" + " L".join(f"{X(i):.0f},{Y(r):.0f}" for i, (e, r) in enumerate(data))
    mk = "".join(f'<circle cx="{X(i):.0f}" cy="{Y(r):.0f}" r="3" fill="{T2}" stroke="#fff" stroke-width="1"/>'
                 f'<text x="{X(i):.0f}" y="{Y(r)-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{r}</text>'
                 f'<text x="{X(i):.0f}" y="152" text-anchor="middle" class="lb">{e}</text>'
                 for i, (e, r) in enumerate(data))
    return ('<svg width="260" height="160" viewBox="0 0 260 160">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{TD}}}</style>'
            f'<rect x="30" y="6" width="222" height="134" rx="5" fill="{TP}" stroke="{TD}" stroke-width="1.2"/>'
            + "".join(f'<line x1="32" y1="{Y(r):.0f}" x2="250" y2="{Y(r):.0f}" stroke="{TG}" stroke-width="0.9"/>'
                      for r in [100, 130, 160, 190])
            + f'<path d="{path}" fill="none" stroke="{T1}" stroke-width="2.4" stroke-linejoin="round"/>'
            + mk +
            '<text x="4" y="16" class="lb">r, pm</text>'
            f'<text x="176" y="22" class="lb" font-weight="bold">3-davr</text></svg>')

def fig_em_bars():
    """B: 2-davr elektromanfiyliklari — ustunlar."""
    data = [("Li", 1.0), ("Be", 1.5), ("B", 2.0), ("C", 2.5), ("N", 3.0), ("O", 3.5), ("F", 4.0)]
    bars = ""
    for i, (e, v) in enumerate(data):
        x = 42 + i * 30; h = v * 28; y = 130 - h
        vv = str(v).replace(".", ",")
        bars += (f'<rect x="{x}" y="{y:.0f}" width="20" height="{h:.0f}" rx="2" fill="{T1}" opacity="0.85" '
                 f'stroke="{TD}" stroke-width="0.9"/>'
                 f'<text x="{x+10}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{vv}</text>'
                 f'<text x="{x+10}" y="143" text-anchor="middle" class="lb">{e}</text>')
    return ('<svg width="260" height="152" viewBox="0 0 260 152">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{TD}}}</style>'
            f'<rect x="30" y="4" width="226" height="126" rx="4" fill="{TP}" stroke="{TG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="32" y1="{130-g*28:.0f}" x2="254" y2="{130-g*28:.0f}" stroke="{TG}" stroke-width="0.9"/>'
                      f'<text x="18" y="{133-g*28:.0f}" class="lb">{g}</text>' for g in [1, 2, 3, 4])
            + bars +
            f'<line x1="30" y1="130" x2="256" y2="130" stroke="{TD}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">EM</text>'
            f'<text x="180" y="18" class="lb" font-weight="bold">2-davr</text></svg>')

def fig_pt_fragment():
    """Davriy jadval fragmenti: markazda X (P), atrofida qo'shnilar."""
    cells = [("C", 0, 0, "#fff"), ("N", 1, 0, "#fff"), ("O", 2, 0, "#fff"),
             ("Si", 0, 1, "#fff"), ("X", 1, 1, "#ffe4d1"), ("S", 2, 1, "#fff"),
             ("Ge", 0, 2, "#fff"), ("As", 1, 2, "#fff"), ("Se", 2, 2, "#fff")]
    s = ""
    for lab, c, r, bg in cells:
        x, y = 66 + c * 44, 16 + r * 36
        bold = 'font-weight="bold"' if lab == "X" else ""
        col = T2 if lab == "X" else TD
        s += (f'<rect x="{x}" y="{y}" width="40" height="32" rx="3" fill="{bg}" stroke="{TD}" stroke-width="1.2"/>'
              f'<text x="{x+20}" y="{y+21}" text-anchor="middle" font-size="12" font-family="Georgia" '
              f'fill="{col}" {bold}>{lab}</text>')
    return ('<svg width="260" height="140" viewBox="0 0 260 140">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{TD}}}</style>'
            + s +
            '<text x="18" y="36" class="lb">2-davr →</text>'
            '<text x="18" y="72" class="lb">3-davr →</text>'
            '<text x="18" y="108" class="lb">4-davr →</text>'
            '<text x="66" y="136" class="lb" font-weight="bold">davriy jadval fragmenti</text></svg>')

def fig_scheme2():
    """B O1-38: sxema — X metall + suv → ishqor + gaz."""
    return ('<svg width="260" height="92" viewBox="0 0 260 92">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{TD}}}</style>'
            f'<rect x="8" y="24" width="64" height="40" rx="4" fill="{TP}" stroke="{T1}" stroke-width="1.6"/>'
            '<text x="40" y="41" text-anchor="middle" class="lb" font-weight="bold">X (3-davr,</text>'
            '<text x="40" y="54" text-anchor="middle" class="lb" font-weight="bold">I A) · ? g</text>'
            f'<line x1="72" y1="44" x2="106" y2="44" stroke="{T2}" stroke-width="2"/>'
            f'<polygon points="110,44 102,40 102,48" fill="{T2}"/>'
            '<text x="76" y="36" class="lb">+ H₂O</text>'
            f'<rect x="112" y="24" width="70" height="40" rx="4" fill="{TP}" stroke="{T1}" stroke-width="1.6"/>'
            '<text x="147" y="41" text-anchor="middle" class="lb" font-weight="bold">XOH eritmasi</text>'
            '<text x="147" y="54" text-anchor="middle" class="lb">(ishqor)</text>'
            f'<line x1="182" y1="44" x2="214" y2="44" stroke="{TD}" stroke-width="1.6"/>'
            f'<polygon points="218,44 210,40 210,48" fill="{TD}"/>'
            '<text x="220" y="40" class="lb" font-weight="bold">gaz ↑</text>'
            '<text x="220" y="52" class="lb">3,36 l (n.sh.)</text></svg>')

def fig_iodine():
    """Dorixona yodi flakoni."""
    return ('<svg width="200" height="122" viewBox="0 0 200 122">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{TD}}}</style>'
            '<rect x="66" y="10" width="22" height="14" rx="3" fill="#37474f"/>'
            '<path d="M62,24 h30 l8,18 v56 q0,8 -8,8 h-30 q-8,0 -8,-8 v-56 z" '
            'fill="#6d3b12" stroke="#4a2408" stroke-width="1.8"/>'
            '<rect x="60" y="52" width="34" height="26" rx="3" fill="#fff" stroke="#c9b8a8"/>'
            '<text x="66" y="68" font-size="10" font-family="Georgia" fill="#4a2408" font-weight="bold">YOD</text>'
            # tomchi va paxta
            '<circle cx="130" cy="82" r="10" fill="#f0e6da" stroke="#c9b8a8" stroke-width="1.2"/>'
            '<circle cx="132" cy="80" r="4" fill="#8a4a12" opacity="0.8"/>'
            '<text x="108" y="106" class="lb">paxtaga tomizildi</text>'
            '<text x="40" y="118" class="lb" font-weight="bold">antiseptik — yod (VII A)</text></svg>')

def fig_balloon():
    """Geliy sharlari."""
    return ('<svg width="220" height="130" viewBox="0 0 220 130">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{TD}}}</style>'
            '<ellipse cx="70" cy="44" rx="26" ry="32" fill="#e74c3c" opacity="0.85"/>'
            '<path d="M70,76 q-3,6 0,10" stroke="#8e2418" stroke-width="1.4" fill="none"/>'
            '<path d="M70,86 q-8,22 -14,34" stroke="#556" stroke-width="1" fill="none"/>'
            '<ellipse cx="120" cy="36" rx="24" ry="30" fill="#f4c542" opacity="0.9"/>'
            '<path d="M120,66 q3,6 0,10" stroke="#b7950b" stroke-width="1.4" fill="none"/>'
            '<path d="M120,76 q6,26 0,44" stroke="#556" stroke-width="1" fill="none"/>'
            '<ellipse cx="164" cy="50" rx="22" ry="28" fill="#26a69a" opacity="0.85"/>'
            '<path d="M164,78 q-3,5 0,9" stroke="#00695c" stroke-width="1.4" fill="none"/>'
            '<path d="M164,87 q-4,20 -8,33" stroke="#556" stroke-width="1" fill="none"/>'
            '<text x="46" y="52" font-size="11" fill="#fff" font-family="Georgia" font-weight="bold">He</text>'
            '<text x="30" y="126" class="lb" font-weight="bold">geliy sharlari — yonmaydi, xavfsiz</text></svg>')

def fig_foil():
    """Alyuminiy folga o'rami."""
    return ('<svg width="220" height="112" viewBox="0 0 220 112">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{TD}}}</style>'
            '<rect x="30" y="40" width="120" height="34" rx="17" fill="#b0bec5" stroke="#78909c" stroke-width="1.6"/>'
            '<ellipse cx="150" cy="57" rx="12" ry="17" fill="#cfd8dc" stroke="#78909c" stroke-width="1.4"/>'
            '<path d="M30,44 q30,10 60,0 q30,-10 58,2 l0,6 q-28,-10 -58,0 q-30,10 -60,0 z" fill="#eceff1" opacity="0.8"/>'
            '<path d="M150,40 h44 q10,0 8,12 l-6,22 h-30" fill="#e3e8ea" stroke="#90a4ae" stroke-width="1.2"/>'
            '<text x="160" y="60" font-size="10" font-family="Georgia" fill="#455a64" font-weight="bold">Al</text>'
            '<text x="34" y="100" class="lb" font-weight="bold">oshxona folgasi — alyuminiy (III A)</text></svg>')

def fig_milk():
    """Stakan sut — kalsiy manbai."""
    return ('<svg width="200" height="126" viewBox="0 0 200 126">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{TD}}}</style>'
            '<path d="M64,26 h56 l-6,74 q-1,8 -9,8 h-26 q-8,0 -9,-8 z" '
            'fill="#eef7f5" stroke="#78909c" stroke-width="1.8"/>'
            '<path d="M67,42 h50 l-4,52 q-1,7 -8,7 h-26 q-7,0 -8,-7 z" fill="#fffdf5" stroke="#e0d8c8"/>'
            '<ellipse cx="92" cy="42" rx="25" ry="5" fill="#fff" stroke="#e0d8c8"/>'
            f'<circle cx="146" cy="46" r="16" fill="none" stroke="{T2}" stroke-width="1.6"/>'
            f'<text x="146" y="50" text-anchor="middle" font-size="10" font-family="Georgia" fill="{T2}" font-weight="bold">Ca²⁺</text>'
            f'<path d="M132,56 q-12,10 -22,12" fill="none" stroke="{T2}" stroke-width="1.2" stroke-dasharray="3,3"/>'
            '<text x="42" y="120" class="lb" font-weight="bold">sut — kalsiy (II A) manbai</text></svg>')

FIGS = dict(radius_line=fig_radius_line, em_bars=fig_em_bars, pt_fragment=fig_pt_fragment,
            scheme2=fig_scheme2, iodine=fig_iodine, balloon=fig_balloon, foil=fig_foil, milk=fig_milk)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bcd9d1; border-radius:2pt;
                  background:#eef7f5; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>2-bob — Davriy qonun va davriy sistema</title><style>{css}</style>"]

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
  <div class="chapnum">2</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 2-bob · Mavzu pasporti (I.2)</div>
  <h1>Davriy qonun va davriy sistema</h1>
  <div class="lead">davr va guruh · xossalarning davriy o'zgarishi (radius, EM, metallik) ·
  oliy oksid va gidroksidlar · amfoterlik · %-dan elementni aniqlash</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>o'rin (davr/guruh) ↔ tuzilish ↔ xossa o'tishlari</li>
      <li>xossa qatorlarini (radius, EM, metallik) tartiblash</li>
      <li>oliy oksid / vodorodli birikma formulalari</li>
      <li>teskari masalalar: % dan elementni aniqlash</li>
      <li>amfoter elementlar va oksidlar xarakteri</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>radius chizig'i va EM ustunlari (B: 5, 26, 32)</li>
      <li>davriy jadval fragmentini o'qish (A: 32; B: 14, 28)</li>
      <li>sxema-masala va jadvallar (B: 17, 38; A: 17)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>davr va guruh yo'nalishlarini almashtirib yuborish</li>
      <li>vodorodli birikmada «8 − guruh» qoidasini unutish</li>
      <li>oliy oksidda valentlikni guruhdan olmaslik</li>
      <li>anion/kation radiusини atom bilan adashtirish</li></ul></div>
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
