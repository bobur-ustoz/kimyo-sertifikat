# -*- coding: utf-8 -*-
"""Organik 3-bob (Arenlar. Neft, gaz, ko'mir) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_III3A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_III3B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#6a1b9a", "#4a1268", "#f8f2fb", "#f9a825"

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
            f'{km}<path d="{p}" fill="none" stroke="#6a1b9a" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- III.3 figuralari (binafsha + oltin palitrasi) ----------
I1, I2, ID, IP, IG = "#6a1b9a", "#f9a825", "#4a1268", "#f8f2fb", "#e2d1ee"

def fig_benzene():
    """Benzol halqasi: Kekule va doirali tasvir."""
    import math
    def hexpts(cx, cy, r):
        return [(cx + r*math.cos(math.radians(60*i-90)), cy + r*math.sin(math.radians(60*i-90))) for i in range(6)]
    p1 = hexpts(70, 62, 30); p2 = hexpts(180, 62, 30)
    s = ""
    for i in range(6):
        a, b = p1[i], p1[(i+1) % 6]
        s += f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{ID}" stroke-width="1.8"/>'
        if i % 2 == 0:
            mx, my = (a[0]+b[0])/2, (a[1]+b[1])/2
            fx, fy = 70 + (mx-70)*0.78, 62 + (my-62)*0.78
            ax, ay = 70 + (a[0]-70)*0.78, 62 + (a[1]-62)*0.78
            bx, by = 70 + (b[0]-70)*0.78, 62 + (b[1]-62)*0.78
            s += f'<line x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{I1}" stroke-width="1.4"/>'
    for i in range(6):
        a, b = p2[i], p2[(i+1) % 6]
        s += f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{ID}" stroke-width="1.8"/>'
    s += f'<circle cx="180" cy="62" r="17" fill="none" stroke="{I1}" stroke-width="1.8"/>'
    return ('<svg width="260" height="126" viewBox="0 0 260 126">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + s +
            '<text x="70" y="112" text-anchor="middle" class="lb" font-weight="bold">Kekule (1865)</text>'
            '<text x="180" y="112" text-anchor="middle" class="lb" font-weight="bold">zamonaviy tasvir</text>'
            '<text x="66" y="12" class="lb" font-weight="bold">benzol C₆H₆ — ikki tasvir</text></svg>')

def fig_column():
    """Rektifikatsion kolonna: fraksiyalar chiqishi."""
    fracs = [("benzin", 24), ("kerosin", 46), ("dizel", 68), ("mazut", 96)]
    s = ""
    for lab, y in fracs:
        s += (f'<line x1="118" y1="{y}" x2="150" y2="{y}" stroke="{I2}" stroke-width="2.2"/>'
              f'<polygon points="154,{y} 146,{y-4} 146,{y+4}" fill="{I2}"/>'
              f'<text x="158" y="{y+3}" class="lb" font-weight="bold">{lab}</text>')
    return ('<svg width="250" height="140" viewBox="0 0 250 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="82" y="14" width="36" height="104" rx="10" fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            + "".join(f'<line x1="86" y1="{y}" x2="114" y2="{y}" stroke="{IG}" stroke-width="1.2"/>'
                      for y in range(30, 112, 14))
            + s +
            f'<path d="M50,118 h32" stroke="{I1}" stroke-width="3"/>'
            f'<text x="18" y="112" class="lb" font-weight="bold">qizigan</text>'
            f'<text x="18" y="123" class="lb" font-weight="bold">neft →</text>'
            '<text x="86" y="10" class="lb">salqin</text>'
            '<text x="70" y="136" class="lb" font-weight="bold">rektifikatsion kolonna</text></svg>')

def fig_bar_oil():
    """1 t neftdan mahsulotlar — ustunlar."""
    data = [("dizel", 32), ("benzin", 25), ("mazut+", 20), ("kerosin", 8)]
    mx = 40
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 54 + i * 52; h = v / mx * 104; y = 120 - h
        col = I1 if i != 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="32" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+16}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+16}" y="133" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="146" viewBox="0 0 270 146">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="42" y="4" width="222" height="116" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="44" y1="{120-g/40*104:.0f}" x2="262" y2="{120-g/40*104:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="28" y="{123-g/40*104:.0f}" class="lb">{g}</text>' for g in [10, 20, 30])
            + bars +
            f'<line x1="42" y1="120" x2="264" y2="120" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ulush, %</text></svg>')

def fig_scheme38():
    """B O1-38: CaC2 → C2H2 → C6H6."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="22" width="86" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="51" y="42" text-anchor="middle" class="lb" font-weight="bold">12,8 g CaC₂</text>'
            f'<line x1="94" y1="39" x2="124" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="128,39 120,35 120,43" fill="{I2}"/>'
            f'<text x="96" y="29" class="lb" fill="{I2}">+H₂O</text>'
            f'<rect x="130" y="22" width="56" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="158" y="42" text-anchor="middle" class="lb" font-weight="bold">C₂H₂</text>'
            f'<line x1="186" y1="39" x2="216" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="220,39 212,35 212,43" fill="{I2}"/>'
            f'<text x="186" y="29" class="lb" fill="{I2}">600°C, C(akt.)</text>'
            f'<rect x="222" y="22" width="52" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="248" y="38" text-anchor="middle" class="lb" font-weight="bold">C₆H₆</text>'
            '<text x="248" y="50" text-anchor="middle" class="lb">? g</text></svg>')

def fig_azs():
    """Yoqilg'i shoxobchasi."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="34" width="44" height="66" rx="5" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="46" y="40" width="32" height="18" rx="2" fill="#fff" stroke="{IG}" stroke-width="1"/>'
            '<text x="62" y="52" text-anchor="middle" class="lb" font-size="6.8">AI-92</text>'
            f'<path d="M84,52 q16,0 16,14 v20" fill="none" stroke="{ID}" stroke-width="2.6"/>'
            f'<path d="M96,86 a6,6 0 1 0 8,2" fill="{I2}"/>'
            '<text x="118" y="46" class="lb" font-weight="bold">benzin —</text>'
            '<text x="118" y="58" class="lb">neft fraksiyasi</text>'
            '<text x="118" y="74" class="lb">(haydash + kreking)</text>'
            '<text x="38" y="116" class="lb" font-weight="bold">yoqilg\'i shoxobchasi</text></svg>')

def fig_asphalt():
    """Asfalt yotqizish."""
    return ('<svg width="230" height="116" viewBox="0 0 230 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="30" y="78" width="170" height="16" rx="2" fill="#3e3e3e"/>'
            f'<rect x="30" y="74" width="90" height="6" rx="2" fill="#616161"/>'
            f'<circle cx="70" cy="66" r="14" fill="#78909c" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="84" y="48" width="34" height="18" rx="3" fill="#90a4ae" stroke="{ID}" stroke-width="1.2"/>'
            + "".join(f'<path d="M{x},44 q3,-6 0,-12" fill="none" stroke="{IG}" stroke-width="1.4"/>' for x in [96, 106])
            + '<text x="130" y="40" class="lb" font-weight="bold">issiq asfalt:</text>'
            '<text x="130" y="54" class="lb">shag\'al + bitum</text>'
            '<text x="130" y="68" class="lb">(neft qoldig\'i)</text>'
            '<text x="30" y="112" class="lb" font-weight="bold">yo\'l qoplamasi</text></svg>')

def fig_mothball():
    """Naftalin tabletkalari va kuya."""
    return ('<svg width="230" height="114" viewBox="0 0 230 114">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#fdfdf6" stroke="{IG}" stroke-width="1.4"/>'
                      for x, y in [(56, 66), (78, 76), (70, 52)])
            + f'<path d="M140,40 q-8,-10 -16,-2 q8,2 10,8 M140,40 q8,-10 16,-2 q-8,2 -10,8" fill="{I1}" opacity="0.5"/>'
            f'<circle cx="140" cy="46" r="3" fill="{ID}"/>'
            + "".join(f'<path d="M{x},46 q3,-5 0,-10" fill="none" stroke="{IG}" stroke-width="1.2"/>' for x in [90, 100])
            + '<text x="120" y="70" class="lb">naftalin C₁₀H₈ —</text>'
            '<text x="120" y="82" class="lb">sublimatlanuvchi aren</text>'
            '<text x="46" y="106" class="lb" font-weight="bold">kuyaga qarshi tabletkalar</text></svg>')

def fig_cokeoven():
    """Koks pechi."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="40" width="80" height="56" rx="4" fill="#8d6e63" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="52" y="56" width="56" height="40" rx="3" fill="#3e2723"/>'
            + "".join(f'<path d="M{x},36 q4,-7 0,-14" fill="none" stroke="{I2}" stroke-width="1.8"/>' for x in [60, 78, 96])
            + '<text x="130" y="46" class="lb" font-weight="bold">1000 °C,</text>'
            '<text x="130" y="58" class="lb" font-weight="bold">havosiz</text>'
            '<text x="130" y="76" class="lb">ko\'mir → koks +</text>'
            '<text x="130" y="88" class="lb">smola + gaz</text>'
            '<text x="38" y="114" class="lb" font-weight="bold">koks pechi (piroliz)</text></svg>')

FIGS = dict(benzene=fig_benzene, column=fig_column, bar_oil=fig_bar_oil, scheme38=fig_scheme38,
            azs=fig_azs, asphalt=fig_asphalt, mothball=fig_mothball, cokeoven=fig_cokeoven)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #dcc8ec; border-radius:2pt;
                  background:#f8f2fb; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>Organik 3-bob — Arenlar va neft</title><style>{css}</style>"]

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
  <div class="chapnum">3</div>
  <div class="kicker">2-kitob · Organik kimyo · 3-bob · Mavzu pasporti (III.3)</div>
  <h1>Aromatik uglevodorodlar. Neft, gaz, ko'mir</h1>
  <div class="lead">benzol va aromatiklik · o'rin olish reaksiyalari · toluol va gomologlar ·
  neftni qayta ishlash: haydash, kreking, riforming · kokslash</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>aromatiklik va halqa barqarorligi (B: 1, 26, 32)</li>
      <li>nitrolash/bromlash hisoblari (B: 2, 3, 10, 37, 41)</li>
      <li>kreking balansi va fraksiyalar (B: 4, 5, 19, 23)</li>
      <li>trimer va zanjir hisoblari (B: 11, 21, 36, 38)</li>
      <li>toluol oksidlanishi — aren detektivi (B: 6, 40, 43)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>benzol halqasi tasvirlari (A: 3; B: 26, 28, 32)</li>
      <li>rektifikatsion kolonna (A: 28; B: 5, 19)</li>
      <li>neft mahsulotlari ustunlari (A: 26, 32)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>benzolni «uch qo'shbog'li alken» deb o'qish</li>
      <li>trimerlanishda 3 ga bo'lishni unutish</li>
      <li>toluol oksidlanishida halqani «kuydirish»</li>
      <li>fraksiyalar tartibini chalkashtirish</li></ul></div>
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
