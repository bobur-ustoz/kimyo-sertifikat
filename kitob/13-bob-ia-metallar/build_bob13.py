# -*- coding: utf-8 -*-
"""13-bob (IA guruh metallari) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_II3A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_II3B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#546e7a", "#37474f", "#f2f5f7", "#8e24aa"

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
            f'{km}<path d="{p}" fill="none" stroke="#546e7a" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- II.3 figuralari (po'lat-kulrang + binafsha palitrasi) ----------
I1, I2, ID, IP, IG = "#546e7a", "#8e24aa", "#37474f", "#f2f5f7", "#d8e0e5"

def fig_melting():
    """IA metallar suyuqlanish haroratlari — chiziqli grafik."""
    data = [("Li", 181), ("Na", 98), ("K", 64), ("Rb", 39), ("Cs", 28)]
    mx = 200
    pts = []
    marks = ""
    for i, (lab, v) in enumerate(data):
        x = 56 + i * 46; y = 126 - v / mx * 108
        pts.append(f"{x},{y:.0f}")
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                  f'<text x="{x}" y="140" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="150" viewBox="0 0 270 150">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="4" width="222" height="122" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="42" y1="{126-g/200*108:.0f}" x2="258" y2="{126-g/200*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="26" y="{129-g/200*108:.0f}" class="lb">{g}</text>' for g in [50, 100, 150])
            + f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="40" y1="126" x2="260" y2="126" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">t, °C</text></svg>')

def fig_bar_water():
    """1 g Li/Na/K suv bilan: ajralgan H2 hajmi — ustunlar."""
    data = [("Li", 1.6), ("Na", 0.49), ("K", 0.29)]
    mx = 2.0
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 64 + i * 62; h = v / mx * 108; y = 124 - h
        col = I2 if i == 0 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} L</text>'
                 f'<text x="{x+18}" y="137" text-anchor="middle" class="lb">1 g {lab}</text>')
    return ('<svg width="260" height="148" viewBox="0 0 260 148">'
            f'<style>.lb{{font-size:8.3px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="48" y="4" width="206" height="120" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="50" y1="{124-g/2*108:.0f}" x2="252" y2="{124-g/2*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="34" y="{127-g/2*108:.0f}" class="lb">{g}</text>' for g in [0.5, 1.0, 1.5])
            + bars +
            f'<line x1="48" y1="124" x2="254" y2="124" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">V(H₂), L</text></svg>')

def fig_sodium_cut():
    """Natriy bilan ishlash: pinset, filtr qog'oz, pichoq."""
    return ('<svg width="260" height="120" viewBox="0 0 260 120">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="28" y="70" width="90" height="8" rx="2" fill="#fff" stroke="{IG}" stroke-width="1.2"/>'
            f'<rect x="52" y="52" width="26" height="18" rx="3" fill="#cfd8dc" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="90" y1="30" x2="70" y2="52" stroke="{ID}" stroke-width="2.6"/>'
            f'<line x1="96" y1="34" x2="80" y2="54" stroke="{ID}" stroke-width="2.6"/>'
            f'<rect x="128" y="40" width="52" height="7" rx="2" fill="#90a4ae" stroke="{ID}" stroke-width="1"/>'
            f'<rect x="178" y="38" width="22" height="11" rx="2" fill="#6d4c41"/>'
            '<text x="30" y="94" class="lb">filtr qog\'oz</text>'
            '<text x="96" y="24" class="lb">pinset</text>'
            '<text x="132" y="30" class="lb">pichoq</text>'
            f'<text x="46" y="48" class="lb" font-weight="bold" fill="{I2}">Na</text>'
            '<text x="28" y="112" class="lb" font-weight="bold">natriy: faqat pinset va quruq asboblar bilan</text></svg>')

def fig_scheme38():
    """B O1-38: NaCl → (elektroliz) → Na → (+H2O) → NaOH."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="6" y="22" width="72" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="42" y="42" text-anchor="middle" class="lb" font-weight="bold">11,7 g NaCl</text>'
            f'<line x1="78" y1="39" x2="106" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="110,39 102,35 102,43" fill="{I2}"/>'
            f'<text x="76" y="29" class="lb" fill="{I2}">elektroliz</text>'
            f'<rect x="112" y="22" width="46" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="135" y="42" text-anchor="middle" class="lb" font-weight="bold">Na</text>'
            f'<line x1="158" y1="39" x2="186" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="190,39 182,35 182,43" fill="{I2}"/>'
            f'<text x="160" y="29" class="lb" fill="{I2}">+H₂O</text>'
            f'<rect x="192" y="22" width="76" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="230" y="42" text-anchor="middle" class="lb" font-weight="bold">NaOH · ? g</text></svg>')

def fig_streetlamp():
    """Tungi yo'l va sariq natriy chiroqlari."""
    return ('<svg width="240" height="126" viewBox="0 0 240 126">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            '<rect x="14" y="10" width="212" height="76" rx="6" fill="#1b2340"/>'
            '<line x1="50" y1="80" x2="50" y2="36" stroke="#90a4ae" stroke-width="3"/>'
            '<path d="M50,36 q14,-8 26,0" fill="none" stroke="#90a4ae" stroke-width="3"/>'
            '<ellipse cx="78" cy="38" rx="9" ry="6" fill="#ffd54f"/>'
            + "".join(f'<circle cx="78" cy="38" r="{r}" fill="none" stroke="#ffd54f" stroke-width="0.8" opacity="{o}"/>'
                      for r, o in [(14, 0.5), (20, 0.3)])
            + '<line x1="150" y1="80" x2="150" y2="36" stroke="#90a4ae" stroke-width="3"/>'
            '<path d="M150,36 q14,-8 26,0" fill="none" stroke="#90a4ae" stroke-width="3"/>'
            '<ellipse cx="178" cy="38" rx="9" ry="6" fill="#ffd54f"/>'
            '<rect x="14" y="80" width="212" height="6" fill="#37474f"/>'
            '<text x="26" y="102" class="lb" font-weight="bold">natriy bug\'ili lampalar — to\'q sariq nur</text>'
            '<text x="26" y="116" class="lb">qo\'zg\'algan Na atomlarining chiqarishi (589 nm)</text></svg>')

def fig_kerosene():
    """Kerosinli bankadagi natriy."""
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="26" width="64" height="80" rx="6" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="44" y="18" width="68" height="10" rx="3" fill="{I1}"/>'
            f'<rect x="48" y="40" width="60" height="64" rx="4" fill="#fff3cd" opacity="0.7"/>'
            + "".join(f'<rect x="{x}" y="{y}" width="18" height="12" rx="3" fill="#cfd8dc" stroke="{I1}" stroke-width="1.2"/>'
                      for x, y in [(58, 84), (80, 74), (62, 62)])
            + '<text x="120" y="42" class="lb" font-weight="bold">kerosin</text>'
            '<text x="120" y="58" class="lb">Na bo\'laklari</text>'
            '<text x="120" y="78" class="lb">havo O₂ va namlikdan</text>'
            '<text x="120" y="90" class="lb">himoya qiladi</text>'
            '<text x="44" y="122" class="lb" font-weight="bold">natriyni saqlash</text></svg>')

def fig_icyroad():
    """Muzli yo'lga tuz sepish."""
    return ('<svg width="240" height="118" viewBox="0 0 240 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="16" y="66" width="208" height="22" rx="3" fill="#b3d4e8" opacity="0.8"/>'
            f'<path d="M16,66 q28,-4 52,0 t52,0 t52,0 t52,0" fill="none" stroke="#7fb3d4" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff" stroke="{IG}" stroke-width="0.6"/>'
                      for x, y in [(90, 50), (104, 42), (118, 52), (132, 40), (146, 50), (112, 60)])
            + f'<path d="M60,26 h34 l6,16 h-46 z" fill="{IP}" stroke="{ID}" stroke-width="1.4"/>'
            '<text x="108" y="30" class="lb" font-weight="bold">tuz (NaCl)</text>'
            '<text x="150" y="80" class="lb" font-weight="bold" fill="#1b5e77">muz → sho\'r suv</text>'
            '<text x="16" y="104" class="lb">tuzli aralashma −21 °C gacha muzlamaydi</text>'
            '<text x="16" y="116" class="lb" font-weight="bold">qishda yo\'llarga tuz sepish</text></svg>')

def fig_potash():
    """Kaliyli o'g'it qopi va o'simlik."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M44,34 h52 v56 a6,6 0 0 1 -6,6 h-40 a6,6 0 0 1 -6,-6 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M44,34 q26,10 52,0" fill="none" stroke="{ID}" stroke-width="1.4"/>'
            f'<text x="70" y="62" text-anchor="middle" class="lb" font-weight="bold" fill="{I2}">KCl</text>'
            '<text x="70" y="76" text-anchor="middle" class="lb">o\'g\'it</text>'
            f'<line x1="150" y1="96" x2="150" y2="56" stroke="#2e7d32" stroke-width="2.4"/>'
            f'<path d="M150,70 q-14,-4 -18,-16 q14,2 18,16 M150,60 q14,-4 18,-16 q-14,2 -18,16" fill="#66bb6a"/>'
            f'<rect x="128" y="96" width="44" height="10" rx="2" fill="#8d6e63" opacity="0.7"/>'
            '<text x="182" y="70" class="lb">K — hosil va</text>'
            '<text x="182" y="82" class="lb">chidamlilik</text>'
            '<text x="42" y="118" class="lb" font-weight="bold">kaliyli o\'g\'it</text></svg>')

FIGS = dict(melting=fig_melting, bar_water=fig_bar_water, sodium_cut=fig_sodium_cut,
            scheme38=fig_scheme38, streetlamp=fig_streetlamp, kerosene=fig_kerosene,
            icyroad=fig_icyroad, potash=fig_potash)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #ccd7dd; border-radius:2pt;
                  background:#f2f5f7; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>13-bob — IA guruh metallari</title><style>{css}</style>"]

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
  <div class="chapnum">13</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 13-bob · Mavzu pasporti (II.3)</div>
  <h1>IA guruh metallari</h1>
  <div class="lead">ishqoriy metallar: tuzilishi va faolligi · suv va kislorod bilan reaksiyalar ·
  peroksidlar · muhim birikmalar (sodalar, ishqorlar) · alanga testlari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>guruh qonuniyatlari: faollik, radius, suyuqlanish</li>
      <li>suv bilan reaksiya hisoblari (A: 10, 23; B: 10, 23)</li>
      <li>noma'lum metall va aralashma masalalari (B: 2, 4, 36)</li>
      <li>peroksid/superoksid va havo regeneratsiyasi (B: 3, 29)</li>
      <li>kristallogidrat va nisbat masalalari (B: 11, 13, 40)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>suyuqlanish haroratlari grafigi (A: 26, 28, 32; B: 28, 32)</li>
      <li>teng massa — H₂ ustunlari (B: 5, 26)</li>
      <li>natriy bilan ishlash va zanjir-sxema (B: 19, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>H₂ koeffitsiyentini (½) unutish</li>
      <li>Na yonishida Na₂O deb yozish (Na₂O₂!)</li>
      <li>alanga ranglarini chalkashtirish</li>
      <li>eritma va suyuqlanma elektrolizini aralashtirish</li></ul></div>
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
