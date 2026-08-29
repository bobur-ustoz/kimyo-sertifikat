# -*- coding: utf-8 -*-
"""Organik 5-bob (Aldegidlar va ketonlar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_III5A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_III5B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#e64a19", "#a33210", "#fdf1ec", "#1a5276"

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
            f'{km}<path d="{p}" fill="none" stroke="#e64a19" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- III.5 figuralari (olov to'q sariq + moviy palitrasi) ----------
I1, I2, ID, IP, IG = "#e64a19", "#1a5276", "#7f2408", "#fdf1ec", "#f2d2c4"

def fig_bp_ald():
    """Aldegidlar qaynash haroratlari — chiziqli grafik (berilgan ma'lumot)."""
    data = [("HCHO", -19), ("CH₃CHO", 21), ("C₂H₅CHO", 49), ("C₃H₇CHO", 76)]
    lo, hi = -30, 90
    pts = []; marks = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 56; y = 118 - (v - lo) / (hi - lo) * 100
        pts.append(f"{x},{y:.0f}")
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3.4" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}°</text>'
                  f'<text x="{x}" y="136" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.0px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="4" width="224" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="40" y1="{118-(0-lo)/(hi-lo)*100:.0f}" x2="264" y2="{118-(0-lo)/(hi-lo)*100:.0f}" '
            f'stroke="{IG}" stroke-width="1" stroke-dasharray="4,3"/>'
            f'<text x="246" y="{115-(0-lo)/(hi-lo)*100:.0f}" class="lb">0 °C</text>'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="40" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">t qayn, °C</text>'
            '<text x="86" y="147" class="lb">zanjir uzunligi ortishi →</text></svg>')

def fig_bar_formalin():
    """Formaldegid ishlatilish yo'nalishlari — ustunlar (berilgan ma'lumot)."""
    data = [("smolalar", 65), ("dezinf.", 15), ("boshqa", 20)]
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 64 + i * 66; h = v / 70 * 104; y = 122 - h
        col = I1 if i == 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="38" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+19}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+19}" y="135" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="218" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{122-g/70*104:.0f}" x2="262" y2="{122-g/70*104:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="30" y="{125-g/70*104:.0f}" class="lb">{g}</text>' for g in [20, 40, 60])
            + bars +
            f'<line x1="46" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ulush, %</text></svg>')

def fig_agmirror():
    """B: kumush ko'zgu tajribasi — suv hammomidagi probirka."""
    return ('<svg width="280" height="140" viewBox="0 0 280 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # stakan (suv hammomi)
            f'<path d="M60,54 h110 v62 a8,8 0 0 1 -8,8 h-94 a8,8 0 0 1 -8,-8 z" fill="{I2}" opacity="0.15" '
            f'stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="64" y="70" width="102" height="48" fill="{I2}" opacity="0.20"/>'
            # gorelka
            f'<path d="M106,128 q7,-9 14,0 q-7,5 -14,0z" fill="{I1}"/>'
            # probirka ichida
            f'<path d="M104,26 v66 a11,11 0 0 0 22,0 v-66" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M107,50 v42 a8,8 0 0 0 16,0 v-42 z" fill="#eef3f8"/>'
            f'<path d="M107,58 v34 a8,8 0 0 0 16,0 v-34" fill="none" stroke="#aab7c4" stroke-width="3" opacity="0.9"/>'
            '<text x="150" y="34" class="lb" font-weight="bold">devorda yaltiroq</text>'
            '<text x="150" y="46" class="lb" font-weight="bold">Ag qatlami</text>'
            f'<text x="176" y="96" class="lb">iliq suv</text>'
            f'<text x="176" y="108" class="lb">hammomi</text>'
            '<text x="36" y="14" class="lb" font-weight="bold">«kumush ko\'zgu» sinovi: R–CHO + Ag₂O</text></svg>')

def fig_scheme38():
    """B O1-38: atsetilen → etanal (Kucherov) sxemasi."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="22" width="92" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="54" y="38" text-anchor="middle" class="lb" font-weight="bold">4,48 L C₂H₂</text>'
            '<text x="54" y="50" text-anchor="middle" class="lb">atsetilen (n.sh.)</text>'
            f'<line x1="100" y1="39" x2="140" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="144,39 136,35 136,43" fill="{I2}"/>'
            f'<text x="102" y="20" class="lb" fill="{I2}">+H₂O,</text>'
            f'<text x="102" y="31" class="lb" fill="{I2}">Hg²⁺ (Kucherov)</text>'
            f'<rect x="146" y="22" width="84" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="188" y="38" text-anchor="middle" class="lb" font-weight="bold">CH₃CHO</text>'
            '<text x="188" y="50" text-anchor="middle" class="lb">? g</text>'
            f'<line x1="230" y1="39" x2="252" y2="39" stroke="{ID}" stroke-width="1.4"/>'
            '<text x="256" y="43" class="lb">etanal</text></svg>')

def fig_museum():
    """A: muzey preparati — formalinli banka."""
    return ('<svg width="220" height="122" viewBox="0 0 220 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="56" y="28" width="52" height="66" rx="6" fill="{I2}" opacity="0.14" '
            f'stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="52" y="20" width="60" height="10" rx="3" fill="{ID}"/>'
            f'<path d="M70,56 q12,-14 24,0 q6,10 -4,18 q-8,6 -16,0 q-10,-8 -4,-18z" '
            f'fill="#c9a2b8" stroke="#8e6a80" stroke-width="1.2" opacity="0.9"/>'
            f'<rect x="66" y="98" width="32" height="10" rx="2" fill="#fff" stroke="{IG}"/>'
            '<text x="82" y="106" text-anchor="middle" class="lb" font-size="6.6">№ 12</text>'
            '<text x="120" y="46" class="lb" font-weight="bold">formalin</text>'
            '<text x="120" y="58" class="lb">(40 % HCHO)</text>'
            '<text x="120" y="74" class="lb">preparat yillab</text>'
            '<text x="120" y="86" class="lb">saqlanadi</text>'
            '<text x="48" y="120" class="lb" font-weight="bold">muzey preparati</text></svg>')

def fig_nailpolish():
    """A: aseton — lak ketkazuvchi flakon va paxta."""
    return ('<svg width="220" height="118" viewBox="0 0 220 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="56" y="40" width="36" height="54" rx="6" fill="{I1}" opacity="0.25" '
            f'stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="64" y="26" width="20" height="14" rx="3" fill="{I2}"/>'
            '<text x="74" y="66" text-anchor="middle" class="lb" font-weight="bold">aseton</text>'
            '<text x="74" y="78" text-anchor="middle" class="lb" font-size="7">CH₃COCH₃</text>'
            f'<ellipse cx="130" cy="86" rx="20" ry="10" fill="#fff" stroke="{IG}" stroke-width="1.4"/>'
            f'<path d="M120,82 q10,-6 20,0" stroke="#e8b4c8" stroke-width="3" fill="none"/>'
            + "".join(f'<path d="M{x},{y} q3,5 0,7 q-3,-2 0,-7z" fill="{I2}" opacity="0.55"/>'
                      for x, y in [(150, 48), (160, 60), (152, 70)])
            + '<text x="150" y="36" class="lb">tez bug\'lanadi</text>'
            '<text x="108" y="110" class="lb">paxta + lak</text>'
            '<text x="48" y="16" class="lb" font-weight="bold">lak ketkazuvchi</text></svg>')

def fig_plywood():
    """A: fanera qatlamlari — fenol-formaldegid smola."""
    return ('<svg width="230" height="116" viewBox="0 0 230 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + "".join(f'<path d="M44,{40+i*12} l70,-14 h76 l-70,14 z" fill="{"#d7a86e" if i%2==0 else "#b98a52"}" '
                      f'stroke="#8a6238" stroke-width="1"/>' for i in range(5))
            + f'<path d="M44,88 l70,-14 M44,100 v-60 l70,-14" stroke="#8a6238" stroke-width="1" fill="none"/>'
            + "".join(f'<line x1="46" y1="{42+i*12}" x2="112" y2="{28+i*12}" stroke="{I1}" '
                      'stroke-width="2" stroke-dasharray="3,4" opacity="0.8"/>' for i in range(1, 5))
            + '<text x="132" y="94" class="lb" font-weight="bold" fill="' + I1 + '">yelim qatlami:</text>'
            '<text x="132" y="106" class="lb">fenol-formaldegid smola</text>'
            '<text x="40" y="112" class="lb" font-weight="bold">fanera kesimi</text></svg>')

def fig_thermos():
    """A: termos kolbasi kesimi — kumush qatlam."""
    return ('<svg width="220" height="124" viewBox="0 0 220 124">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M64,24 h44 v10 q10,6 10,18 v46 a8,8 0 0 1 -8,8 h-48 a8,8 0 0 1 -8,-8 v-46 '
            f'q0,-12 10,-18 z" fill="{I2}" opacity="0.14" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M72,38 q-6,6 -6,14 v44 M100,38 q6,6 6,14 v44" fill="none" stroke="#aab7c4" '
            'stroke-width="3" opacity="0.95"/>'
            f'<rect x="76" y="52" width="20" height="46" rx="4" fill="{I1}" opacity="0.35"/>'
            f'<rect x="64" y="14" width="44" height="10" rx="3" fill="{ID}"/>'
            '<text x="126" y="48" class="lb" font-weight="bold">kumush</text>'
            '<text x="126" y="60" class="lb" font-weight="bold">qatlam</text>'
            '<text x="126" y="76" class="lb">issiqlik nurini</text>'
            '<text x="126" y="88" class="lb">qaytaradi</text>'
            '<text x="52" y="120" class="lb" font-weight="bold">termos kolbasi kesimi</text></svg>')

FIGS = dict(bp_ald=fig_bp_ald, bar_formalin=fig_bar_formalin, agmirror=fig_agmirror,
            scheme38=fig_scheme38, museum=fig_museum, nailpolish=fig_nailpolish,
            plywood=fig_plywood, thermos=fig_thermos)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #f0cbbb; border-radius:2pt;
                  background:#fdf1ec; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>Organik 5-bob — Aldegidlar va ketonlar</title><style>{css}</style>"]

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
  <div class="chapnum">5</div>
  <div class="kicker">2-kitob · Organik kimyo · 5-bob · Mavzu pasporti (III.5)</div>
  <h1>Aldegidlar va ketonlar</h1>
  <div class="lead">karbonil guruh C=O · metanal, etanal, aseton · Kucherov reaksiyasi ·
  «kumush ko'zgu» va Cu(OH)&#8322; sinovlari · oksidlanish-qaytarilish «ko'prigi»</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>aldegid/keton farqi va izomeriya (B: 1, 2, 12, 30)</li>
      <li>«kumush ko'zgu» hisoblari (B: 8, 10, 23, 31, 37, 43)</li>
      <li>Kucherov va unumli zanjirlar (B: 13, 28, 32, 38, 41)</li>
      <li>teskari masalalar — M topish (B: 6, 10, 26, 43)</li>
      <li>formalin ulush hisoblari (B: 21; A: 43)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>qaynash haroratlari grafigi (A: 28)</li>
      <li>formaldegid ishlatilishi diagrammasi (A: 26, 32)</li>
      <li>kumush ko'zgu tajribasi (B: 4, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>asetondan «ko'zgu» kutish</li>
      <li>Ag koeffitsiyentida 2 ni unutish</li>
      <li>C&#8323;H&#8326;O ni spirt deb o'qish</li>
      <li>oksidlash va qaytarish yo'nalishlarini chalkashtirish</li></ul></div>
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
