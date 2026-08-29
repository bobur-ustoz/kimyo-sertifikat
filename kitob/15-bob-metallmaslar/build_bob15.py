# -*- coding: utf-8 -*-
"""15-bob (Metallmaslar. Vodorod. Mineral o'g'itlar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_II5A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_II5B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#827717", "#5d5410", "#fbfbe9", "#5e35b1"

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
            f'{km}<path d="{p}" fill="none" stroke="#827717" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- II.5 figuralari (xantal-zaytun + binafsha palitrasi) ----------
I1, I2, ID, IP, IG = "#827717", "#5e35b1", "#5d5410", "#fbfbee", "#e6e4c3"

def fig_bp_line():
    """Galogenlar qaynash haroratlari — chiziqli grafik."""
    data = [("F₂", -188), ("Cl₂", -34), ("Br₂", 59), ("I₂", 184)]
    lo, hi = -220, 220
    pts = []; marks = ""
    for i, (lab, v) in enumerate(data):
        x = 60 + i * 56; y = 122 - (v - lo) / (hi - lo) * 104
        pts.append(f"{x},{y:.0f}")
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                  f'<text x="{x}" y="138" text-anchor="middle" class="lb">{lab}</text>')
    y25 = 122 - (25 - lo) / (hi - lo) * 104
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="42" y="4" width="220" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="44" y1="{y25:.0f}" x2="260" y2="{y25:.0f}" stroke="{I2}" stroke-width="0.9" stroke-dasharray="4,3"/>'
            f'<text x="212" y="{y25-4:.0f}" class="lb" fill="{I2}">25 °C</text>'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="42" y1="122" x2="262" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">t(qayn.), °C</text></svg>')

def fig_bar_havo():
    """Quruq havo tarkibi — ustunlar."""
    data = [("N₂", 78), ("O₂", 21), ("Ar+boshqa", 1)]
    mx = 90
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 62; h = max(v / mx * 108, 3); y = 124 - h
        col = I1 if i != 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+18}" y="137" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="260" height="148" viewBox="0 0 260 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="48" y="4" width="206" height="120" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="50" y1="{124-g/90*108:.0f}" x2="252" y2="{124-g/90*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="34" y="{127-g/90*108:.0f}" class="lb">{g}</text>' for g in [25, 50, 75])
            + bars +
            f'<line x1="48" y1="124" x2="254" y2="124" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ulush, %</text></svg>')

def fig_fountain():
    """Ammiak favvorasi: kolba, naycha, suvli idish."""
    return ('<svg width="250" height="150" viewBox="0 0 250 150">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<circle cx="96" cy="44" r="27" fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            '<text x="96" y="40" text-anchor="middle" class="lb" font-weight="bold">NH₃ gazi</text>'
            f'<line x1="96" y1="71" x2="96" y2="112" stroke="{ID}" stroke-width="3"/>'
            f'<path d="M60,112 h72 v22 a8,8 0 0 1 -8,8 h-56 a8,8 0 0 1 -8,-8 z" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="62" y="120" width="68" height="20" rx="4" fill="{I2}" opacity="0.22"/>'
            f'<path d="M96,108 q-5,-16 -1,-34 M96,108 q5,-14 2,-30" fill="none" stroke="{I2}" stroke-width="1.8"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="{I2}"/>' for x, y in [(92, 60), (100, 56), (96, 50)])
            + '<text x="140" y="46" class="lb" font-weight="bold">bosim pasayadi</text>'
            '<text x="140" y="60" class="lb">(NH₃ suvda eriydi)</text>'
            '<text x="140" y="96" class="lb" font-weight="bold" fill="' + I2 + '">suv otilib chiqadi</text>'
            '<text x="140" y="126" class="lb">suv + fenolftalein</text>'
            '<text x="56" y="148" class="lb" font-weight="bold">«ammiak favvorasi» tajribasi</text></svg>')

def fig_scheme38():
    """B O1-38: NH3 → NO → NO2 → HNO3 zanjiri."""
    boxes = [("4,48 L NH₃", "+O₂, kat."), ("NO", "+O₂"), ("NO₂", "+O₂+H₂O"), ("HNO₃ · ? g", None)]
    H = [f'<svg width="286" height="72" viewBox="0 0 286 72">'
         f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>']
    x = 4
    for i, (lab, arr) in enumerate(boxes):
        w = 66 if i in (0, 3) else 42
        H.append(f'<rect x="{x}" y="22" width="{w}" height="30" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
                 f'<text x="{x+w/2}" y="40" text-anchor="middle" class="lb" font-weight="bold">{lab}</text>')
        x += w
        if arr:
            H.append(f'<line x1="{x+2}" y1="37" x2="{x+16}" y2="37" stroke="{I2}" stroke-width="2"/>'
                     f'<polygon points="{x+20},37 {x+12},33 {x+12},41" fill="{I2}"/>'
                     f'<text x="{x}" y="26" class="lb" fill="{I2}">{arr}</text>')
            x += 24
    H.append('</svg>')
    return "".join(H)

def fig_matches():
    """Gugurt cho'pi va qutisi."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="30" y="58" width="80" height="34" rx="3" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="30" y="74" width="80" height="8" fill="#a1887f"/>'
            f'<rect x="60" y="30" width="64" height="7" rx="3" fill="#e6cfa3" transform="rotate(-18 92 34)"/>'
            f'<circle cx="126" cy="22" r="7" fill="#c62828"/>'
            f'<path d="M126,14 q-5,-8 0,-13 q5,5 0,13" fill="#f4a942" stroke="#d35400" stroke-width="1"/>'
            '<text x="142" y="24" class="lb" font-weight="bold">boshcha: S + KClO₃</text>'
            '<text x="142" y="40" class="lb">ishqalanish → alanga</text>'
            '<text x="118" y="82" class="lb">qutida: qizil fosfor</text>'
            f'<path d="M116,80 q-8,0 -12,-2" fill="none" stroke="{IG}" stroke-width="1.1"/>'
            '<text x="30" y="112" class="lb" font-weight="bold">gugurt kimyosi</text></svg>')

def fig_ammonia():
    """Nashatir spirti flakoni."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="52" y="34" width="40" height="60" rx="6" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="60" y="22" width="24" height="14" rx="3" fill="{I1}"/>'
            f'<rect x="58" y="52" width="28" height="30" rx="2" fill="#fff" stroke="{IG}" stroke-width="1"/>'
            '<text x="72" y="64" text-anchor="middle" class="lb" font-size="7">NH₃</text>'
            '<text x="72" y="74" text-anchor="middle" class="lb" font-size="7">10 %</text>'
            + "".join(f'<path d="M{x},30 q4,-5 0,-10" fill="none" stroke="{I2}" stroke-width="1.4"/>'
                      for x in [104, 112, 120])
            + f'<text x="130" y="34" class="lb" font-weight="bold" fill="{I2}">o\'tkir hid</text>'
            '<text x="106" y="58" class="lb">nafas retseptorlarini</text>'
            '<text x="106" y="70" class="lb">qo\'zg\'atadi</text>'
            '<text x="50" y="114" class="lb" font-weight="bold">nashatir spirti (NH₃ eritmasi)</text></svg>')

def fig_selitra():
    """Selitra granulalari va qop."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M40,32 h56 v56 a6,6 0 0 1 -6,6 h-44 a6,6 0 0 1 -6,-6 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<text x="68" y="56" text-anchor="middle" class="lb" font-weight="bold" fill="{I2}">NH₄NO₃</text>'
            '<text x="68" y="70" text-anchor="middle" class="lb">35 % N</text>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fdfdf6" stroke="{I1}" stroke-width="1"/>'
                      for x, y in [(120, 84), (132, 92), (144, 82), (126, 74), (140, 70), (152, 92)])
            + '<text x="120" y="40" class="lb" font-weight="bold">granulalar</text>'
            f'<path d="M126,44 q4,10 4,22" fill="none" stroke="{IG}" stroke-width="1.1"/>'
            '<text x="40" y="112" class="lb" font-weight="bold">ammiakli selitra — azotli o\'g\'it</text></svg>')

def fig_egg():
    """Buloq va tuxum hidi (H2S)."""
    return ('<svg width="230" height="116" viewBox="0 0 230 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M30,84 q30,-10 60,0 t60,0 t50,0 v14 h-170 z" fill="{I2}" opacity="0.18"/>'
            f'<path d="M30,84 q30,-10 60,0 t60,0 t50,0" fill="none" stroke="{I2}" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{I1}" stroke-width="1.1"/>'
                      for x, y, r in [(80, 74, 2.4), (92, 66, 3), (86, 56, 2)])
            + f'<ellipse cx="150" cy="34" rx="12" ry="15" fill="#fdfdf6" stroke="{ID}" stroke-width="1.4"/>'
            + "".join(f'<path d="M{x},48 q3,-5 0,-10" fill="none" stroke="{I1}" stroke-width="1.2"/>'
                      for x in [144, 152, 158])
            + '<text x="168" y="36" class="lb" font-weight="bold">H₂S hidi</text>'
            '<text x="46" y="46" class="lb">buloq suvi</text>'
            '<text x="30" y="110" class="lb" font-weight="bold">«palag\'da tuxum» hidi — vodorod sulfid</text></svg>')

FIGS = dict(bp_line=fig_bp_line, bar_havo=fig_bar_havo, fountain=fig_fountain, scheme38=fig_scheme38,
            matches=fig_matches, ammonia=fig_ammonia, selitra=fig_selitra, egg=fig_egg)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #ddd9b3; border-radius:2pt;
                  background:#fbfbee; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>15-bob — Metallmaslar va o'g'itlar</title><style>{css}</style>"]

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
  <div class="chapnum">15</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 15-bob · Mavzu pasporti (II.5)</div>
  <h1>Metallmaslar. Vodorod. Mineral o'g'itlar</h1>
  <div class="lead">galogenlar · kislorod va oltingugurt · azot va fosfor · uglerod va kremniy ·
  vodorod · ammiak va kislotalar sanoati · NPK o'g'itlar</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>metallmaslar xossalari va allotropiya</li>
      <li>gazlarni olish, yig'ish, tanish (A: 5, 15; B: 3, 7)</li>
      <li>sanoat zanjirlari: NH₃, HNO₃, H₂SO₄ (B: 4, 8, 27, 37, 38)</li>
      <li>cheklovchi reagent va unum (B: 11, 36)</li>
      <li>o'g'itlar: turlari va ω(N) hisoblari (B: 10, 23, 39, 43)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>galogenlar qaynash grafigi (A: 29; B: 26, 28, 32)</li>
      <li>havo tarkibi ustunlari (A: 26, 28, 32)</li>
      <li>ammiak favvorasi va zanjir-sxema (B: 5, 19, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>NH₃ ni kislotali gaz deb o'ylash</li>
      <li>cheklovchi reagentni tekshirmaslik</li>
      <li>ω(N) da azot sonini (2 ta) unutish</li>
      <li>galogen faolligini teskari olish</li></ul></div>
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
