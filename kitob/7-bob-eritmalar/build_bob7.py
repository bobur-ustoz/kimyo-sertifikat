# -*- coding: utf-8 -*-
"""7-bob (Eritmalar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I7A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I7B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="{ACCENT2}" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.7 laboratoriya figuralari (A-variant) ----------
def fig_solubility_curve():
    """KNO3/NaCl eruvchanlik egri chiziqlari: t 0-80, s 0-180 g."""
    def X(t): return 34 + t * 2.25
    def Y(s): return 150 - s * 0.8
    kno3 = [(0, 13), (20, 32), (40, 64), (60, 110), (80, 169)]
    nacl = [(0, 35), (20, 36), (40, 36.5), (60, 37), (80, 38)]
    def path(pts):
        return "M" + " L".join(f"{X(t):.0f},{Y(s):.0f}" for t, s in pts)
    grid = "".join(f'<line x1="{X(t)}" y1="6" x2="{X(t)}" y2="150" class="gr"/>' for t in range(10, 81, 10)) + \
           "".join(f'<line x1="34" y1="{Y(s):.0f}" x2="214" y2="{Y(s):.0f}" class="gr"/>' for s in range(20, 181, 20))
    xt = "".join(f'<text x="{X(t)-6}" y="162" class="lb">{t}</text>' for t in range(0, 81, 20))
    yt = "".join(f'<text x="10" y="{Y(s)+3:.0f}" class="lb">{s}</text>' for s in range(0, 181, 40))
    return ('<svg width="228" height="172" viewBox="0 0 236 176">'
            '<style>.gr{stroke:#e3e3e3;stroke-width:0.7}.ax{stroke:#222;stroke-width:1.4}'
            '.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            f'{grid}'
            '<line x1="34" y1="150" x2="222" y2="150" class="ax"/><polygon points="222,150 215,147 215,153" fill="#222"/>'
            '<line x1="34" y1="150" x2="34" y2="2" class="ax"/><polygon points="34,2 31,9 37,9" fill="#222"/>'
            f'{xt}{yt}'
            '<text x="196" y="146" class="lb">t, °C</text><text x="38" y="10" class="lb">s, g/100 g suv</text>'
            f'<path d="{path(kno3)}" fill="none" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<path d="{path(nacl)}" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<text x="150" y="52" class="lb" fill="{ACCENT2}" font-weight="bold">KNO₃</text>'
            f'<text x="170" y="112" class="lb" fill="{ACCENT}" font-weight="bold">NaCl</text>'
            '</svg>')

def _beaker(x, label, sub, precipitate, fill_h=44):
    prec = (f'<path d="M{x+10},92 q6,-7 12,0 q6,-7 12,0 q6,-7 12,0 q6,-7 12,-1 l0,3 q-24,4 -48,0 z" '
            f'fill="#9db4c4" stroke="#7a93a5" stroke-width="0.8"/>') if precipitate else ""
    return (f'<g><rect x="{x+8}" y="{92-fill_h}" width="50" height="{fill_h}" rx="2" fill="#dcebf5"/>'
            f'{prec}'
            f'<path d="M{x+8},34 V90 q0,6 8,6 h34 q8,0 8,-6 V34" fill="none" stroke="#556" stroke-width="1.6"/>'
            f'<line x1="{x+4}" y1="34" x2="{x+62}" y2="34" stroke="#556" stroke-width="1.6"/>'
            f'<text x="{x+33}" y="112" text-anchor="middle" class="lb" font-weight="bold">{label}</text>'
            f'<text x="{x+33}" y="124" text-anchor="middle" class="lb">{sub}</text></g>')

def fig_beaker_sat():
    return ('<svg width="120" height="132" viewBox="0 0 90 132">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + _beaker(10, "eritma", "cho'kma tubida", True) + "</svg>")

def fig_beakers3():
    s = '<svg width="300" height="136" viewBox="0 0 300 136"><style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
    for i, (tuz, prec) in enumerate([("+20 g tuz", False), ("+36 g tuz", False), ("+50 g tuz", True)]):
        x = 6 + i * 100
        s += _beaker(x, f"{i+1}-idish", f"{tuz} · 100 g H₂O", prec)
        s += (f'<line x1="{x+33}" y1="8" x2="{x+33}" y2="26" stroke="#556" stroke-width="1.2"/>'
              f'<polygon points="{x+33},30 {x+30},22 {x+36},22" fill="#556"/>')
    return s + "</svg>"

# ---------- I.7 hayotiy sahnalar (A-variant · o'rgatuvchi) ----------
def fig_jam():
    """Murabbo bankasi: sovutilganda tubida shakar kristallari."""
    return ('<svg width="240" height="128" viewBox="0 0 240 128">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # issiq banka (chap)
            '<rect x="26" y="30" width="52" height="76" rx="7" fill="#e67e22" opacity="0.85" stroke="#a04000" stroke-width="1.6"/>'
            '<rect x="22" y="20" width="60" height="12" rx="3" fill="#7f8c8d" stroke="#566"/>'
            '<path d="M36,44 q8,-5 16,0 q8,5 16,0" stroke="#fff" stroke-width="1.4" fill="none" opacity="0.7"/>'
            '<text x="30" y="16" font-size="12">♨</text><text x="44" y="16" font-size="12">♨</text>'
            '<text x="28" y="122" class="lb" font-weight="bold">qaynoq · 100 °C</text>'
            # strelka
            '<line x1="96" y1="66" x2="130" y2="66" stroke="#556" stroke-width="1.6"/>'
            '<polygon points="134,66 126,62 126,70" fill="#556"/>'
            '<text x="96" y="58" class="lb">sovutish</text>'
            # sovuq banka (o'ng) — tubida kristallar
            '<rect x="150" y="30" width="52" height="76" rx="7" fill="#d35400" opacity="0.6" stroke="#a04000" stroke-width="1.6"/>'
            '<rect x="146" y="20" width="60" height="12" rx="3" fill="#7f8c8d" stroke="#566"/>'
            + "".join(f'<rect x="{156+i*7}" y="{95-(i%2)*4}" width="5" height="5" rx="1" '
                      f'fill="#fdf2e0" stroke="#c9a86a" stroke-width="0.7" transform="rotate({(i*23)%40-20} {158+i*7} {97-(i%2)*4})"/>'
                      for i in range(6)) +
            '<text x="146" y="122" class="lb" font-weight="bold">sovuq · kristallar!</text></svg>')

def fig_saltlake():
    """Sho'r ko'l: quyosh, bug'lanish, qirg'oqda tuz qatlami."""
    return ('<svg width="260" height="120" viewBox="0 0 260 120">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # quyosh
            '<circle cx="42" cy="26" r="12" fill="#f4d03f" stroke="#d4ac0d" stroke-width="1.4"/>'
            + "".join(f'<line x1="{42+18*dx}" y1="{26+18*dy}" x2="{42+24*dx}" y2="{26+24*dy}" stroke="#d4ac0d" stroke-width="1.6"/>'
                      for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(0.7,0.7),(-0.7,0.7),(0.7,-0.7),(-0.7,-0.7)]) +
            # bug' chiziqlari
            '<path d="M120,52 q4,-7 0,-14 M140,50 q4,-7 0,-14 M160,52 q4,-7 0,-14" '
            'stroke="#95a5a6" stroke-width="1.5" fill="none" stroke-linecap="round"/>'
            '<text x="172" y="42" class="lb">bug\'lanish</text>'
            # ko'l suvi
            '<path d="M60,78 q70,-16 150,0 l-8,22 q-66,12 -134,0 z" fill="#7fb3d3" stroke="#5b8bab" stroke-width="1.4"/>'
            # tuz qirg'og'i
            '<path d="M40,84 q12,-8 24,-5 l-4,24 q-14,3 -26,-2 z" fill="#f7f4ea" stroke="#c8c2a8" stroke-width="1.2"/>'
            '<path d="M216,82 q14,-4 26,2 l2,20 q-16,4 -30,-2 z" fill="#f7f4ea" stroke="#c8c2a8" stroke-width="1.2"/>'
            + "".join(f'<circle cx="{48+(i*9)%18}" cy="{92+(i*5)%10}" r="1.2" fill="#d5cfb6"/>' for i in range(5))
            + "".join(f'<circle cx="{224+(i*9)%18}" cy="{92+(i*5)%10}" r="1.2" fill="#d5cfb6"/>' for i in range(5)) +
            '<text x="96" y="116" class="lb" font-weight="bold">sho\'r ko\'l · qirg\'oqda tuz qatlami</text></svg>')

def fig_aquarium():
    """Akvarium: iliq suvda baliqlar yuzaga ko'tarilgan."""
    return ('<svg width="250" height="126" viewBox="0 0 250 126">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # akvarium
            '<rect x="30" y="24" width="190" height="80" rx="4" fill="#d6ecf7" stroke="#5b8bab" stroke-width="2"/>'
            '<line x1="30" y1="36" x2="220" y2="36" stroke="#5b8bab" stroke-width="1.2" stroke-dasharray="4,3"/>'
            # isitgich
            '<rect x="200" y="40" width="7" height="42" rx="3" fill="#e74c3c" stroke="#a93226"/>'
            '<text x="182" y="96" class="lb">isitgich</text>'
            # suv o'ti
            '<path d="M46,102 q-4,-14 2,-26 q6,10 2,26 M56,102 q-2,-10 3,-20 q4,9 1,20" '
            'fill="#58d68d" stroke="#28b463" stroke-width="1"/>'
            # baliqlar yuza yaqinida
            + "".join(
                f'<g transform="translate({x},{y})"><ellipse cx="0" cy="0" rx="10" ry="5" fill="#f39c12" stroke="#ca8a0a"/>'
                f'<polygon points="-10,0 -16,-5 -16,5" fill="#f39c12" stroke="#ca8a0a"/>'
                f'<circle cx="5" cy="-1.4" r="1.1" fill="#222"/></g>'
                for x, y in [(90, 44), (128, 42), (160, 46)])
            # havo pufakchalari yuzada
            + "".join(f'<circle cx="{80+i*18}" cy="31" r="{1.6+(i%2)*0.6}" fill="none" stroke="#5b8bab" stroke-width="0.9"/>'
                      for i in range(7)) +
            '<text x="52" y="120" class="lb" font-weight="bold">iliq akvarium · baliqlar suv yuzasida</text></svg>')

# ---------- B-variant hisob grafigi ----------
def fig_solubility_b():
    """X tuzi eruvchanligi: t 0-80, s 0-44 g — hisob uchun o'qiladigan egri."""
    def X(t): return 38 + t * 2.3
    def Y(s): return 148 - s * 3.1
    pts = [(0, 4), (20, 8), (40, 15), (60, 25), (80, 40)]
    path = "M" + " L".join(f"{X(t):.0f},{Y(s):.0f}" for t, s in pts)
    grid = "".join(f'<line x1="{X(t)}" y1="8" x2="{X(t)}" y2="148" class="gr"/>' for t in range(10, 81, 10)) + \
           "".join(f'<line x1="38" y1="{Y(s):.0f}" x2="222" y2="{Y(s):.0f}" class="gr"/>' for s in range(5, 45, 5))
    xt = "".join(f'<text x="{X(t)-6}" y="160" class="lb">{t}</text>' for t in range(0, 81, 20))
    yt = "".join(f'<text x="16" y="{Y(s)+3:.0f}" class="lb">{s}</text>' for s in range(0, 45, 10))
    guides = ""
    for t, s in [(20, 8), (80, 40)]:
        guides += (f'<line x1="{X(t)}" y1="{Y(s)}" x2="{X(t)}" y2="148" class="dsh"/>'
                   f'<line x1="38" y1="{Y(s)}" x2="{X(t)}" y2="{Y(s)}" class="dsh"/>'
                   f'<circle cx="{X(t)}" cy="{Y(s)}" r="2.6" fill="{ACCENT}"/>')
    return ('<svg width="232" height="168" viewBox="0 0 238 168">'
            '<style>.gr{stroke:#e3e3e3;stroke-width:0.7}.ax{stroke:#222;stroke-width:1.4}'
            '.lb{font-size:9px;font-family:Georgia,serif;fill:#333}.dsh{stroke:#999;stroke-width:0.9;stroke-dasharray:3,3}</style>'
            f'{grid}'
            '<line x1="38" y1="148" x2="230" y2="148" class="ax"/><polygon points="230,148 223,145 223,151" fill="#222"/>'
            '<line x1="38" y1="148" x2="38" y2="4" class="ax"/><polygon points="38,4 35,11 41,11" fill="#222"/>'
            f'{xt}{yt}{guides}'
            '<text x="204" y="144" class="lb">t, °C</text><text x="42" y="12" class="lb">s, g/100 g suv</text>'
            f'<path d="{path}" fill="none" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<text x="176" y="34" class="lb" fill="{ACCENT2}" font-weight="bold">X tuzi</text>'
            '</svg>')

FIGS = dict(solubility_curve=fig_solubility_curve, beaker_sat=fig_beaker_sat, beakers3=fig_beakers3,
            jam=fig_jam, saltlake=fig_saltlake, aquarium=fig_aquarium, solubility_b=fig_solubility_b)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #c8d2da; border-radius:2pt;
                  background:#fff; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>7-bob — Eritmalar</title><style>{css}</style>"]

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
                 f"&nbsp; <i>Javob:</i> <span class='o1line'>&nbsp;</span></div>")

    H.append("<div class='sec' style='margin-top:4mm'>4-QISM · YOZMA ISH <small>(41–43 · har biri 25 ball)</small></div>")
    for q in o2:
        txt, tbl = table_from_markup(q["matn"])
        H.append(f"<div class='o2'><div class='head'>{q['n']}-topshiriq</div><div>{txt}</div>{tbl}")
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
  <div class="chapnum">7</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 7-bob · Mavzu pasporti (I.7)</div>
  <h1>Eritmalar</h1>
  <div class="lead">eruvchanlik va uning haroratga bog'liqligi · foiz, molyar, normal, molyal konsentratsiya
  va titr · kristallogidratlar · oleum · aralashtirish va suyultirish</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>s (g/100 g suv) ↔ ω o'zaro o'tishlar</li>
      <li>ω, c(M), c(N), molyallik, titr — beshovi orasida o'tish</li>
      <li>kristallogidrat: foiz, eritish, sovutganda cho'kish</li>
      <li>oleum: SO₃ + suv hisoblari</li>
      <li>aralashtirish, suyultirish, «krest» qoidasi</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>eruvchanlik egri chizig'ini o'qish (A: 5, B: 5, 32)</li>
      <li>idishlardagi holatni tahlil qilish (to'yingan/cho'kma)</li>
      <li>jadval ma'lumotidan hisob (A: 17, B: 17)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>s ni ω bilan adashtirish (100 g suv ≠ 100 g eritma)</li>
      <li>kristallogidrat cho'kkanda suv ham chiqishini unutish</li>
      <li>oleumda SO₃ ning suv bilan reaksiyasini hisobga olmaslik</li>
      <li>normallikda ekvivalent sonini noto'g'ri olish</li></ul></div>
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
