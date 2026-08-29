# -*- coding: utf-8 -*-
"""11-bob (Anorganik moddalar sinflari va genetik bog'lanish) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_II1A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_II1B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#0e7490", "#0b4f5c", "#eef8fa", "#c05621"

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
            f'{km}<path d="{p}" fill="none" stroke="#0e7490" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- II.1 figuralari (petrol-moviy palitrasi) ----------
I1, I2, ID, IP, IG = "#0e7490", "#c05621", "#0b4f5c", "#f0f9fb", "#cfe8ee"

def fig_aloh():
    """AlCl3 + NaOH: cho'kma massasi grafigi — ko'tarilib, so'ng erib tushadi (amfoterlik)."""
    return ('<svg width="260" height="150" viewBox="0 0 260 150">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="34" y="6" width="216" height="132" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="34" y1="138" x2="252" y2="138" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="34" y1="138" x2="34" y2="8" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M36,136 L128,38 L216,132" fill="none" stroke="{I1}" stroke-width="2.4" '
            'stroke-linejoin="round"/>'
            f'<line x1="128" y1="38" x2="128" y2="138" stroke="{IG}" stroke-width="1" stroke-dasharray="3,3"/>'
            f'<circle cx="128" cy="38" r="3" fill="{I2}"/>'
            f'<text x="96" y="30" class="lb" font-weight="bold" fill="{I2}">maksimum</text>'
            f'<text x="48" y="80" class="lb" font-weight="bold">cho\'kma</text>'
            f'<text x="48" y="92" class="lb" font-weight="bold">ortadi</text>'
            f'<text x="166" y="80" class="lb" font-weight="bold">cho\'kma</text>'
            f'<text x="166" y="92" class="lb" font-weight="bold">eriydi</text>'
            f'<text x="6" y="16" class="lb">m(cho\'kma)</text>'
            '<text x="168" y="148" class="lb">qo\'shilgan NaOH</text></svg>')

def fig_bar_ogit():
    """Azotli o'g'itlardagi azot ulushi (%) — ustunlar."""
    data = [("NH₄NO₃", 35), ("(NH₄)₂SO₄", 21), ("KNO₃", 14)]
    mx = 40
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 62; h = v / mx * 112; y = 128 - h
        col = I1 if i != 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+18}" y="141" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="260" height="150" viewBox="0 0 260 150">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="208" height="124" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{128-g/40*112:.0f}" x2="250" y2="{128-g/40*112:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="32" y="{131-g/40*112:.0f}" class="lb">{g}</text>' for g in [10, 20, 30])
            + bars +
            f'<line x1="46" y1="128" x2="252" y2="128" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ω(N), %</text></svg>')

def fig_limewater():
    """Asbob: CO2 gaz naychadan ohakli suvga o'tkazilmoqda."""
    return ('<svg width="260" height="140" viewBox="0 0 260 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # gaz manbai (kolba)
            f'<path d="M40,54 v18 l-12,26 a8,8 0 0 0 8,10 h28 a8,8 0 0 0 8,-10 l-12,-26 v-18 z" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            '<text x="50" y="98" text-anchor="middle" class="lb">CaCO₃+HCl</text>'
            # naycha
            f'<path d="M50,54 v-16 h110 v40" fill="none" stroke="{I2}" stroke-width="2.4"/>'
            f'<text x="86" y="32" class="lb" font-weight="bold" fill="{I2}">CO₂ →</text>'
            # probirka ohakli suv
            f'<path d="M144,58 v54 a16,14 0 0 0 32,0 v-54" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="146" y="74" width="28" height="40" rx="8" fill="{I1}" opacity="0.18"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="none" stroke="{I1}" stroke-width="1"/>'
                      for x, y in [(156, 104), (164, 94), (158, 84)])
            + '<text x="186" y="80" class="lb">ohakli suv</text>'
            '<text x="186" y="92" class="lb">Ca(OH)₂</text>'
            '<text x="186" y="110" class="lb" font-weight="bold">loyqa → tiniq?</text>'
            '<text x="40" y="132" class="lb" font-weight="bold">CO₂ ni ohakli suvdan o\'tkazish</text></svg>')

def fig_scheme38():
    """B O1-38: Ca → CaO → Ca(OH)2 → CaCO3 zanjiri."""
    boxes = [("20 g Ca", "+O₂"), ("CaO", "+H₂O"), ("Ca(OH)₂", "+CO₂"), ("CaCO₃ · ? g", None)]
    H = [f'<svg width="280" height="70" viewBox="0 0 280 70">'
         f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>']
    x = 6
    for i, (lab, arr) in enumerate(boxes):
        w = 62 if i in (0, 3) else 52
        H.append(f'<rect x="{x}" y="20" width="{w}" height="28" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
                 f'<text x="{x+w/2}" y="37" text-anchor="middle" class="lb" font-weight="bold">{lab}</text>')
        x += w
        if arr:
            H.append(f'<line x1="{x+2}" y1="34" x2="{x+18}" y2="34" stroke="{I2}" stroke-width="2"/>'
                     f'<polygon points="{x+22},34 {x+14},30 {x+14},38" fill="{I2}"/>'
                     f'<text x="{x+2}" y="24" class="lb" fill="{I2}">{arr}</text>')
            x += 24
    H.append('</svg>')
    return "".join(H)

def fig_antacid():
    """Antatsid: tabletka stakanga tushmoqda, me'da belgisi."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M40,34 h56 l-6,64 a8,8 0 0 1 -8,7 h-28 a8,8 0 0 1 -8,-7 z" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="44" y="58" width="48" height="42" rx="4" fill="{I1}" opacity="0.15"/>'
            f'<circle cx="68" cy="44" r="7" fill="#fff" stroke="{I2}" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="none" stroke="{I2}" stroke-width="1"/>'
                      for x, y in [(58, 78), (72, 88), (64, 96), (78, 72)])
            + f'<text x="106" y="42" class="lb" font-weight="bold">Mg(OH)₂ tabletka</text>'
            '<text x="106" y="58" class="lb">me\'dada: Mg(OH)₂ +</text>'
            '<text x="106" y="70" class="lb">2HCl → MgCl₂ + 2H₂O</text>'
            '<text x="40" y="116" class="lb" font-weight="bold">antatsid — kislotani neytrallaydi</text></svg>')

def fig_kettle():
    """Choynak qasqoni: choynak + sirka quyilmoqda, pufakchalar."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M46,52 a34,30 0 1 0 68,0 q0,-10 -8,-14 h-52 q-8,4 -8,14" transform="translate(0,14)" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M44,72 q-14,-2 -12,-16 l8,2" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<path d="M112,66 q16,-6 12,-18" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<rect x="60" y="96" width="40" height="5" rx="2" fill="{I1}" opacity="0.5"/>'
            '<text x="80" y="92" text-anchor="middle" class="lb">qasqon (CaCO₃)</text>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{I2}" stroke-width="1.2"/>'
                      for x, y, r in [(74, 74, 2.4), (86, 68, 3), (80, 58, 2)])
            + f'<text x="128" y="40" class="lb" font-weight="bold" fill="{I2}">sirka kislota</text>'
            '<text x="128" y="54" class="lb">CaCO₃ + kislota →</text>'
            '<text x="128" y="66" class="lb">tuz + H₂O + CO₂↑</text>'
            '<text x="40" y="118" class="lb" font-weight="bold">qasqonni kislota bilan tozalash</text></svg>')

def fig_whitewash():
    """Devor oqlash: cho'tka, devor, CO2 belgilari."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="28" y="24" width="92" height="72" rx="3" fill="#fdfdf6" stroke="{IG}" stroke-width="1.4"/>'
            f'<rect x="28" y="24" width="46" height="72" fill="{I1}" opacity="0.10"/>'
            f'<rect x="86" y="40" width="10" height="34" rx="2" fill="#8d6e63" transform="rotate(24 91 57)"/>'
            f'<rect x="80" y="30" width="22" height="14" rx="3" fill="{I2}"/>'
            + "".join(f'<text x="{x}" y="{y}" font-size="9" fill="{I1}">CO₂</text>'
                      for x, y in [(134, 34), (150, 56), (136, 78)])
            + f'<path d="M132,38 q-8,8 -6,16 M148,60 q-10,6 -12,14" fill="none" stroke="{IG}" stroke-width="1.2"/>'
            '<text x="128" y="98" class="lb">Ca(OH)₂ + CO₂ →</text>'
            '<text x="128" y="110" class="lb">CaCO₃ + H₂O</text>'
            '<text x="28" y="114" class="lb" font-weight="bold">oqlangan devor «toshga» aylanadi</text></svg>')

def fig_sodadrink():
    """Gazli ichimlik: stakan, pufakchalar, CO2."""
    return ('<svg width="220" height="122" viewBox="0 0 220 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M44,26 h52 l-5,74 a7,7 0 0 1 -7,6 h-28 a7,7 0 0 1 -7,-6 z" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M47,44 h46 l-4,56 a5,5 0 0 1 -5,4 h-28 a5,5 0 0 1 -5,-4 z" fill="{I2}" opacity="0.22"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{I1}" stroke-width="1.1"/>'
                      for x, y, r in [(58, 92, 2), (70, 82, 2.6), (82, 92, 2), (64, 68, 2.2), (78, 60, 2.6), (70, 50, 2)])
            + '<text x="110" y="40" class="lb" font-weight="bold">CO₂ pufakchalari</text>'
            '<text x="110" y="56" class="lb">CO₂ + H₂O ⇄ H₂CO₃</text>'
            '<text x="110" y="70" class="lb">(kuchsiz kislota)</text>'
            '<text x="40" y="116" class="lb" font-weight="bold">gazli ichimlikdagi «o\'tkir» ta\'m</text></svg>')

FIGS = dict(aloh=fig_aloh, bar_ogit=fig_bar_ogit, limewater=fig_limewater, scheme38=fig_scheme38,
            antacid=fig_antacid, kettle=fig_kettle, whitewash=fig_whitewash, sodadrink=fig_sodadrink)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bcdde6; border-radius:2pt;
                  background:#f0f9fb; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>11-bob — Anorganik moddalar sinflari</title><style>{css}</style>"]

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
  <div class="chapnum">11</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 11-bob · Mavzu pasporti (II.1)</div>
  <h1>Anorganik moddalar sinflari va genetik bog'lanish</h1>
  <div class="lead">oksidlar (asosli, kislotali, amfoter, befarq) · asoslar va ishqorlar · kislotalar ·
  o'rta, nordon va asosli tuzlar · genetik zanjirlar</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>moddalarni sinflarga to'g'ri ajratish</li>
      <li>sinflararo reaksiyalar: nima nima bilan kirishadi</li>
      <li>nordon/asosli tuzlar va «necha xil tuz» (B: 1, 2)</li>
      <li>amfoterlik: ZnO, Al(OH)₃ (B: 5, 28, 32, 42)</li>
      <li>genetik zanjir va aralashma hisoblari (B: 11, 23, 36–40)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>amfoter cho'kma grafigi (B: 5, 28, 32)</li>
      <li>o'g'itlar diagrammasi (A: 26, 32; B: 26)</li>
      <li>ohakli suv asbobi va zanjir-sxema (B: 19, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>ZnO/Al₂O₃ ni oddiy asosli oksid deyish</li>
      <li>nordon tuzni kislota bilan adashtirish</li>
      <li>CO, NO ni kislotali oksid deb olish</li>
      <li>ishqor-kislota nisbatini tekshirmasdan tuz turini yozish</li></ul></div>
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
