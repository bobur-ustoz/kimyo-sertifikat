# -*- coding: utf-8 -*-
"""Organik 2-bob (Alkenlar, alkadiyenlar, alkinlar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_III2A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_III2B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#c62828", "#7f1d1d", "#fdf2f2", "#1976d2"

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
            f'{km}<path d="{p}" fill="none" stroke="#c62828" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- III.2 figuralari (qizil + ko'k palitrasi) ----------
I1, I2, ID, IP, IG = "#c62828", "#1976d2", "#7f1d1d", "#fdf2f2", "#f0cfcf"

def fig_bond_len():
    """C-C, C=C, C#C bog' uzunliklari — chiziqli grafik."""
    data = [("C–C", 154), ("C=C", 134), ("C≡C", 120)]
    lo, hi = 110, 165
    pts = []; marks = ""
    for i, (lab, v) in enumerate(data):
        x = 70 + i * 70; y = 118 - (v - lo) / (hi - lo) * 100
        pts.append(f"{x},{y:.0f}")
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3.4" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-8:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} pm</text>'
                  f'<text x="{x}" y="136" text-anchor="middle" class="lb" font-weight="bold">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="4" width="222" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="40" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">uzunlik, pm</text>'
            '<text x="70" y="146" class="lb">bog\' karraligi ortishi →</text></svg>')

def fig_bar_polymer():
    """Jahon plastiklari ulushi — ustunlar."""
    data = [("PE", 31), ("PP", 25), ("PVX", 13), ("boshqa", 31)]
    mx = 40
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 56 + i * 52; h = v / mx * 104; y = 122 - h
        col = I1 if i == 0 else (I2 if i % 2 else "#8d6e63")
        bars += (f'<rect x="{x}" y="{y:.0f}" width="32" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+16}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+16}" y="135" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="44" y="4" width="220" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="46" y1="{122-g/40*104:.0f}" x2="262" y2="{122-g/40*104:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="30" y="{125-g/40*104:.0f}" class="lb">{g}</text>' for g in [10, 20, 30])
            + bars +
            f'<line x1="44" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ulush, %</text></svg>')

def fig_bromtest():
    """Ikki probirka: etan (sariq qoladi) va etilen (rangsizlandi)."""
    return ('<svg width="260" height="140" viewBox="0 0 260 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # 1-probirka (etan)
            f'<path d="M60,20 v64 a11,11 0 0 0 22,0 v-64" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M62,52 v32 a9,9 0 0 0 18,0 v-32 z" fill="#f6c445" opacity="0.85"/>'
            f'<line x1="71" y1="12" x2="71" y2="48" stroke="{I2}" stroke-width="2" stroke-dasharray="3,3"/>'
            '<text x="71" y="120" text-anchor="middle" class="lb" font-weight="bold">+ C₂H₆</text>'
            '<text x="71" y="132" text-anchor="middle" class="lb">rang QOLDI</text>'
            # 2-probirka (etilen)
            f'<path d="M150,20 v64 a11,11 0 0 0 22,0 v-64" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M152,52 v32 a9,9 0 0 0 18,0 v-32 z" fill="#eef4fb" opacity="0.9"/>'
            f'<line x1="161" y1="12" x2="161" y2="48" stroke="{I2}" stroke-width="2" stroke-dasharray="3,3"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="none" stroke="{I2}" stroke-width="1"/>'
                      for x, y in [(158, 74), (165, 66), (160, 58)])
            + '<text x="161" y="120" text-anchor="middle" class="lb" font-weight="bold">+ C₂H₄</text>'
            '<text x="161" y="132" text-anchor="middle" class="lb" fill="' + I1 + '">RANGSIZLANDI</text>'
            '<text x="196" y="50" class="lb">bromli</text>'
            '<text x="196" y="62" class="lb">suv</text>'
            '<text x="54" y="10" class="lb" font-weight="bold">to\'yinmaganlik sinovi</text></svg>')

def fig_scheme38():
    """B O1-38: etilen → etanol zanjiri."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="22" width="86" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="51" y="38" text-anchor="middle" class="lb" font-weight="bold">4,48 L C₂H₄</text>'
            '<text x="51" y="50" text-anchor="middle" class="lb">etilen</text>'
            f'<line x1="94" y1="39" x2="130" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="134,39 126,35 126,43" fill="{I2}"/>'
            f'<text x="96" y="29" class="lb" fill="{I2}">+H₂O, kat.</text>'
            f'<rect x="136" y="22" width="86" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="179" y="38" text-anchor="middle" class="lb" font-weight="bold">C₂H₅OH</text>'
            '<text x="179" y="50" text-anchor="middle" class="lb">? g</text>'
            f'<line x1="222" y1="39" x2="248" y2="39" stroke="{ID}" stroke-width="1.4"/>'
            '<text x="252" y="43" class="lb">spirt</text></svg>')

def fig_fruits():
    """Banan va pomidor — etilen gazi."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M36,58 q30,34 66,26 q8,-2 8,4 q0,6 -8,8 q-46,6 -74,-32 q-4,-6 2,-8 q4,-1 6,2z" '
            'fill="#f4c542" stroke="#c49000" stroke-width="1.4"/>'
            f'<circle cx="140" cy="76" r="18" fill="#e53935" stroke="#8e1c1c" stroke-width="1.4"/>'
            f'<path d="M134,60 q6,-6 12,0 l-6,4 z" fill="#43a047"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="none" stroke="{I2}" stroke-width="1"/>'
                      for x, y in [(96, 44, ), (106, 36), (116, 46), (100, 30)])
            + f'<text x="126" y="30" class="lb" font-weight="bold" fill="{I2}">C₂H₄</text>'
            '<text x="160" y="46" class="lb">pishish «gormoni»</text>'
            '<text x="34" y="112" class="lb" font-weight="bold">etilen mevalarni pishiradi</text></svg>')

def fig_welding():
    """Payvandlash: gorelka va uchqunlar."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="84" width="120" height="10" rx="2" fill="#78909c"/>'
            f'<rect x="118" y="30" width="34" height="10" rx="4" fill="#455a64" transform="rotate(38 135 35)"/>'
            f'<path d="M116,52 q-8,10 -14,26" fill="none" stroke="#455a64" stroke-width="3"/>'
            f'<path d="M104,76 q-4,8 -2,10 q4,2 8,-4" fill="#fff" stroke="#42a5f5" stroke-width="1.4"/>'
            + "".join(f'<line x1="102" y1="84" x2="{102+dx}" y2="{84+dy}" stroke="#f4a942" stroke-width="1.6"/>'
                      for dx, dy in [(-12, -8), (12, -10), (-8, 8), (14, 6), (2, -14)])
            + '<text x="160" y="40" class="lb" font-weight="bold">C₂H₂ + O₂</text>'
            '<text x="160" y="54" class="lb">~3000 °C</text>'
            '<text x="40" y="114" class="lb" font-weight="bold">atsetilen payvandlash</text></svg>')

def fig_bag():
    """Polietilen paket."""
    return ('<svg width="220" height="116" viewBox="0 0 220 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M52,36 h56 v56 a6,6 0 0 1 -6,6 h-44 a6,6 0 0 1 -6,-6 z" fill="{I2}" opacity="0.18"/>'
            f'<path d="M52,36 h56 v56 a6,6 0 0 1 -6,6 h-44 a6,6 0 0 1 -6,-6 z" fill="none" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M62,36 v-8 a8,8 0 0 1 16,0 v8 M84,36 v-8 a8,8 0 0 1 16,0 v8" fill="none" stroke="{ID}" stroke-width="1.6"/>'
            '<text x="80" y="70" text-anchor="middle" class="lb" font-weight="bold">PE</text>'
            '<text x="122" y="46" class="lb">nCH₂=CH₂ →</text>'
            '<text x="122" y="58" class="lb">(–CH₂–CH₂–)ₙ</text>'
            '<text x="50" y="112" class="lb" font-weight="bold">polietilen paket</text></svg>')

def fig_tire():
    """Avtomobil shinasi."""
    return ('<svg width="220" height="118" viewBox="0 0 220 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<circle cx="76" cy="64" r="34" fill="#37474f"/>'
            f'<circle cx="76" cy="64" r="18" fill="#eceff1" stroke="#90a4ae" stroke-width="2"/>'
            + "".join(f'<rect x="{74}" y="{28}" width="4" height="8" rx="1" fill="#eceff1" transform="rotate({a} 76 64)"/>'
                      for a in range(0, 360, 30))
            + '<text x="122" y="48" class="lb" font-weight="bold">rezina =</text>'
            '<text x="122" y="60" class="lb">kauchuk + S</text>'
            '<text x="122" y="76" class="lb">(vulkanizatsiya)</text>'
            '<text x="44" y="112" class="lb" font-weight="bold">shina — dien polimeri</text></svg>')

FIGS = dict(bond_len=fig_bond_len, bar_polymer=fig_bar_polymer, bromtest=fig_bromtest,
            scheme38=fig_scheme38, fruits=fig_fruits, welding=fig_welding, bag=fig_bag, tire=fig_tire)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #ecc7c7; border-radius:2pt;
                  background:#fdf2f2; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>Organik 2-bob — Alkenlar va alkinlar</title><style>{css}</style>"]

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
  <div class="kicker">2-kitob · Organik kimyo · 2-bob · Mavzu pasporti (III.2)</div>
  <h1>Alkenlar, alkadiyenlar, alkinlar</h1>
  <div class="lead">qo'shbog' va uchbog' · birikish reaksiyalari va Markovnikov qoidasi ·
  sifat sinovlari · polimerlanish · atsetilen kimyosi</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>umumiy formulalar va sinflararo izomeriya (B: 7, 14)</li>
      <li>sifat sinovlari: Br₂ suvi, KMnO₄ (A: 6; B: 1, 5, 12)</li>
      <li>Markovnikov va birikish hisoblari (B: 3, 10, 13, 23)</li>
      <li>aralashma tahlili brom orqali (B: 11, 21, 39)</li>
      <li>karbid, gidratlanish, polimer hisoblari (B: 4, 15, 27, 36–40)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>brom-test tajribasi (B: 5, 19, 32)</li>
      <li>bog' uzunliklari grafigi (A: 28, 32; B: 28)</li>
      <li>polimerlar diagrammasi va zanjir-sxema (A: 26; B: 26, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>alkin va dienni (2n−2) farqlamaslik</li>
      <li>Markovnikovda H yo'nalishini teskari olish</li>
      <li>atsetilenning 2 mol Br₂ olishini unutish</li>
      <li>birikish va o'rin olishni aralashtirish</li></ul></div>
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
