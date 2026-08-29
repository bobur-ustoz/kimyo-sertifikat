# -*- coding: utf-8 -*-
"""14-bob (IIA, IIIA va d-metallar. Suv qattiqligi) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_II4A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_II4B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#4b6043", "#33432c", "#f2f6f0", "#b7410e"

SVG_CURVES = {
    "rise":      ("M22,82 C55,68 95,40 126,22", None),
    "flat":      ("M22,44 L126,44", None),
    "fall":      ("M22,22 C55,36 95,64 126,82", None),
    "rise_flat": ("M22,82 L70,34 L126,34", (70, 34)),
    "fall_flat": ("M22,26 L70,70 L126,70", (70, 70)),
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
            f'{km}<path d="{p}" fill="none" stroke="#4b6043" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- II.4 figuralari (mox-yashil + zang-qizil palitrasi) ----------
I1, I2, ID, IP, IG = "#4b6043", "#b7410e", "#33432c", "#f2f6f0", "#d7e2d2"

def fig_hardness_curve():
    """Qaynatishda Ca(HCO3)2 miqdori: kamayib, past sathda to'xtaydi."""
    return ('<svg width="260" height="146" viewBox="0 0 260 146">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="36" y="6" width="216" height="122" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="36" y1="128" x2="252" y2="128" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="36" y1="128" x2="36" y2="8" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M38,26 C90,30 120,96 158,102 L248,102" fill="none" stroke="{I1}" stroke-width="2.4"/>'
            f'<line x1="38" y1="102" x2="248" y2="102" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<text x="42" y="20" class="lb" font-weight="bold">erigan Ca(HCO₃)₂</text>'
            f'<text x="96" y="66" class="lb" fill="{I2}" font-weight="bold">CaCO₃↓ cho\'kadi</text>'
            f'<text x="166" y="96" class="lb" font-weight="bold">doimiy qattiqlik ulushi</text>'
            f'<text x="6" y="16" class="lb">C</text>'
            '<text x="196" y="140" class="lb">qaynatish vaqti</text></svg>')

def fig_bar_hardness():
    """Uch suv namunasining qattiqligi — ustunlar."""
    data = [("quduq", 9), ("daryo", 3), ("distillangan", 0.1)]
    mx = 11
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 62; h = max(v / mx * 108, 2); y = 124 - h
        col = I2 if i == 0 else I1
        vt = "≈0" if v < 1 else str(v)
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{vt}</text>'
                 f'<text x="{x+18}" y="137" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="48" y="4" width="214" height="120" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="50" y1="{124-g/11*108:.0f}" x2="260" y2="{124-g/11*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="36" y="{127-g/11*108:.0f}" class="lb">{g}</text>' for g in [3, 6, 9])
            + bars +
            f'<line x1="48" y1="124" x2="262" y2="124" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">mg-ekv/L</text></svg>')

def fig_termit():
    """Alyumotermiya: tigel, uchqunlar, suyuq temir oqimi, rels."""
    return ('<svg width="250" height="140" viewBox="0 0 250 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M84,22 h56 l-8,34 h-40 z" fill="#9e9e9e" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M92,26 h40 l-4,14 h-32 z" fill="{I2}" opacity="0.6"/>'
            + "".join(f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y-8}" stroke="#f4a942" stroke-width="1.6"/>'
                      for x, y, dx in [(96, 22, -8), (112, 18, 0), (128, 22, 8), (104, 16, -4), (120, 16, 5)])
            + f'<path d="M112,56 v22" stroke="{I2}" stroke-width="5"/>'
            f'<path d="M96,86 h32 v10 h-32 z M88,96 h48 v8 h-48 z" fill="#78909c" stroke="{ID}" stroke-width="1.2"/>'
            f'<text x="150" y="34" class="lb" font-weight="bold">tigel: Fe₂O₃ + Al</text>'
            f'<text x="150" y="50" class="lb" fill="{I2}" font-weight="bold">~3000 °C</text>'
            f'<text x="150" y="70" class="lb">suyuq temir</text>'
            f'<path d="M148,66 q-18,4 -30,4" fill="none" stroke="{IG}" stroke-width="1.1"/>'
            '<text x="150" y="96" class="lb">rels choki</text>'
            '<text x="60" y="128" class="lb" font-weight="bold">alyumotermiya — relslarni payvandlash</text></svg>')

def fig_scheme38():
    """B O1-38: Fe2O3 --Al--> Fe --HCl--> FeCl2."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="6" y="22" width="76" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="44" y="42" text-anchor="middle" class="lb" font-weight="bold">16 g Fe₂O₃</text>'
            f'<line x1="82" y1="39" x2="112" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="116,39 108,35 108,43" fill="{I2}"/>'
            f'<text x="84" y="29" class="lb" fill="{I2}">+Al, t°</text>'
            f'<rect x="118" y="22" width="46" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="141" y="42" text-anchor="middle" class="lb" font-weight="bold">Fe</text>'
            f'<line x1="164" y1="39" x2="194" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="198,39 190,35 190,43" fill="{I2}"/>'
            f'<text x="166" y="29" class="lb" fill="{I2}">+HCl</text>'
            f'<rect x="200" y="22" width="74" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="237" y="42" text-anchor="middle" class="lb" font-weight="bold">FeCl₂ · ? g</text></svg>')

def fig_statue():
    """Kislotali yomg'ir ostidagi marmar haykal."""
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + "".join(f'<line x1="{x}" y1="{12+i%2*4}" x2="{x-6}" y2="{30+i%2*4}" stroke="#7fa8c4" stroke-width="1.4"/>'
                      for i, x in enumerate([120, 140, 160, 180, 200]))
            + f'<circle cx="74" cy="42" r="12" fill="#efece4" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M62,56 q12,-8 24,0 l6,36 h-36 z" fill="#efece4" stroke="{ID}" stroke-width="1.4"/>'
            f'<rect x="52" y="92" width="46" height="12" rx="2" fill="#d9d4c6" stroke="{ID}" stroke-width="1.2"/>'
            f'<path d="M86,34 q6,-6 10,-2" fill="none" stroke="{I2}" stroke-width="1.2"/>'
            '<text x="112" y="52" class="lb" font-weight="bold">kislotali yomg\'ir</text>'
            '<text x="112" y="66" class="lb">CaCO₃ + H₂SO₄ →</text>'
            '<text x="112" y="78" class="lb">CaSO₄ + H₂O + CO₂</text>'
            '<text x="50" y="120" class="lb" font-weight="bold">marmar haykal yemirilishi</text></svg>')

def fig_plane():
    """Samolyot — alyuminiy qotishmalari."""
    return ('<svg width="240" height="118" viewBox="0 0 240 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M28,58 q60,-10 150,-4 q20,2 26,8 q-6,6 -26,8 q-90,6 -150,-4 q-8,-4 0,-8z" '
            f'fill="#cfd8dc" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M96,56 l-26,-26 h14 l30,24 z" fill="#b0bec5" stroke="{ID}" stroke-width="1.2"/>'
            f'<path d="M96,66 l-20,22 h12 l26,-20 z" fill="#b0bec5" stroke="{ID}" stroke-width="1.2"/>'
            + "".join(f'<circle cx="{x}" cy="60" r="1.8" fill="#78909c"/>' for x in range(120, 190, 12))
            + '<text x="150" y="30" class="lb" font-weight="bold">Al qotishmalari</text>'
            '<text x="150" y="94" class="lb">yengil (2,7 g/sm³) +</text>'
            '<text x="150" y="106" class="lb">Al₂O₃ himoya parda</text>'
            '<text x="28" y="112" class="lb" font-weight="bold">aviatsiya metali</text></svg>')

def fig_gips():
    """Tibbiy gips — qo'l va bint."""
    return ('<svg width="230" height="116" viewBox="0 0 230 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M36,60 q30,-16 66,-8 l36,10 q8,3 6,10 q-2,7 -10,6 l-38,-6 q-32,-2 -60,6 z" '
            f'fill="#fdfdf6" stroke="{ID}" stroke-width="1.6"/>'
            + "".join(f'<path d="M{x},52 q6,10 -2,20" fill="none" stroke="{IG}" stroke-width="1.4"/>'
                      for x in [58, 74, 90, 106])
            + f'<text x="150" y="38" class="lb" font-weight="bold">gips bog\'lami</text>'
            '<text x="150" y="56" class="lb">CaSO₄ asosi:</text>'
            '<text x="150" y="68" class="lb">suv bilan qorilib</text>'
            '<text x="150" y="80" class="lb">tez QOTADI</text>'
            '<text x="36" y="110" class="lb" font-weight="bold">singan suyakni qotirish</text></svg>')

def fig_washer():
    """Kir mashina TENi va qasqon."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="30" y="24" width="76" height="76" rx="8" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<circle cx="68" cy="62" r="26" fill="#e3f2fd" stroke="{I1}" stroke-width="2"/>'
            f'<circle cx="68" cy="62" r="16" fill="none" stroke="{IG}" stroke-width="1.4"/>'
            f'<path d="M118,92 q20,6 40,0 q10,-3 10,-12" fill="none" stroke="{ID}" stroke-width="3.6"/>'
            f'<path d="M120,90 q18,5 36,0" fill="none" stroke="#e0dcc8" stroke-width="7" opacity="0.8"/>'
            '<text x="126" y="40" class="lb" font-weight="bold">TEN (qizdirgich)</text>'
            '<text x="126" y="56" class="lb">oq qatlam — qasqon:</text>'
            '<text x="126" y="68" class="lb">CaCO₃, MgCO₃</text>'
            f'<path d="M148,74 q-4,8 -8,12" fill="none" stroke="{IG}" stroke-width="1.2"/>'
            '<text x="28" y="116" class="lb" font-weight="bold">qattiq suv va kir mashina</text></svg>')

FIGS = dict(hardness_curve=fig_hardness_curve, bar_hardness=fig_bar_hardness, termit=fig_termit,
            scheme38=fig_scheme38, statue=fig_statue, plane=fig_plane, gips=fig_gips, washer=fig_washer)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #c9d8c2; border-radius:2pt;
                  background:#f2f6f0; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>14-bob — IIA, IIIA va d-metallar</title><style>{css}</style>"]

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
  <div class="chapnum">14</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 14-bob · Mavzu pasporti (II.4)</div>
  <h1>IIA, IIIA va d-metallar. Suv qattiqligi</h1>
  <div class="lead">kalsiy va magniy · alyuminiy va amfoterlik · temir, mis, rux, xrom ·
  vaqtinchalik va doimiy qattiqlik · alyumotermiya</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>Ca/Mg birikmalari: ohak, gips, karbonatlar zanjiri</li>
      <li>Al amfoterligi: ishqorda erish hisoblari (B: 4, 11, 17, 40)</li>
      <li>temir zanjirlari va oksidlanish darajalari (B: 6, 14, 37)</li>
      <li>suv qattiqligi: turlari, mg-ekv hisob (B: 21, 39, 41)</li>
      <li>alyumotermiya va aralashma masalalari (B: 10, 19, 32, 36)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>qattiqlik-qaynatish egri chizig'i (B: 5, 28)</li>
      <li>suv namunalari ustunlari (A: 26, 28, 32; B: 26)</li>
      <li>alyumotermiya va zanjir-sxema (B: 19, 32, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>«Al ishqorda erimaydi» deb o'ylash</li>
      <li>Fe + HCl da FeCl₃ yozish</li>
      <li>doimiy qattiqlikni qaynatib «yo'qotish»</li>
      <li>mg-ekv da zaryadni unutish</li></ul></div>
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
