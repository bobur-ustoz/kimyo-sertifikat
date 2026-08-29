# -*- coding: utf-8 -*-
"""5-bob (Tezlik) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I5A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I5.json", encoding="utf-8"))
data = data_B  # eski kod mosligi uchun
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

def fig_energy():
    """Energiya diagrammasi: katalizatorsiz (1) va katalizatorli (2) yo'llar."""
    return (
        '<svg width="240" height="150" viewBox="0 0 250 155">'
        '<style>.ax{stroke:#222;stroke-width:1.4}.lb{font-size:10px;font-family:Georgia,serif;fill:#333}'
        '.dsh{stroke:#999;stroke-width:0.9;stroke-dasharray:3,3}</style>'
        '<line x1="26" y1="132" x2="240" y2="132" class="ax"/><polygon points="240,132 233,129 233,135" fill="#222"/>'
        '<line x1="26" y1="132" x2="26" y2="8" class="ax"/><polygon points="26,8 23,15 29,15" fill="#222"/>'
        '<text x="4" y="14" class="lb">E</text><text x="168" y="146" class="lb">reaksiya yo\'li</text>'
        # boshlang'ich va oxirgi sathlar
        '<line x1="26" y1="70" x2="60" y2="70" stroke="#333" stroke-width="2"/>'
        '<line x1="200" y1="105" x2="238" y2="105" stroke="#333" stroke-width="2"/>'
        '<line x1="60" y1="70" x2="200" y2="70" class="dsh"/>'
        # 1-egri (katalizatorsiz, baland cho'qqi)
        f'<path d="M60,70 C95,18 165,18 200,105" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>'
        # 2-egri (katalizatorli, past cho'qqi)
        f'<path d="M60,70 C100,44 160,44 200,105" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-dasharray="6,3"/>'
        # Ea belgilar
        '<line x1="128" y1="31" x2="128" y2="70" class="dsh"/>'
        f'<text x="132" y="46" class="lb" fill="{ACCENT2}">Ea₁</text>'
        '<line x1="112" y1="50" x2="112" y2="70" class="dsh"/>'
        f'<text x="88" y="62" class="lb" fill="{ACCENT}">Ea₂</text>'
        f'<text x="98" y="26" class="lb" fill="{ACCENT2}" font-weight="bold">1</text>'
        f'<text x="140" y="56" class="lb" fill="{ACCENT}" font-weight="bold">2</text>'
        '<text x="30" y="66" class="lb">reagentlar</text><text x="200" y="118" class="lb">mahsulotlar</text>'
        '</svg>')

def fig_ct_read():
    """c-t grafigi: qiymat o'qish uchun (c: 0-2,0; t: 0-50)."""
    def X(t): return 34 + t * 3.6      # t 0..50 -> 34..214
    def Y(c): return 138 - c * 60      # c 0..2  -> 138..18
    pts = [(0, 2.0), (10, 1.4), (20, 1.0), (30, 0.8), (40, 0.7), (50, 0.65)]
    path = "M" + " L".join(f"{X(t):.0f},{Y(c):.0f}" for t, c in pts)
    grid = "".join(f'<line x1="{X(t)}" y1="14" x2="{X(t)}" y2="138" class="gr"/>' for t in range(10, 51, 10)) + \
           "".join(f'<line x1="34" y1="{Y(c):.0f}" x2="214" y2="{Y(c):.0f}" class="gr"/>' for c in
                   [0.4, 0.8, 1.2, 1.6, 2.0])
    xt = "".join(f'<text x="{X(t)-6}" y="150" class="lb">{t}</text>' for t in range(0, 51, 10))
    yt = "".join(f'<text x="8" y="{Y(c)+3:.0f}" class="lb">{c:.1f}</text>'.replace(".", ",") for c in
                 [0.4, 0.8, 1.2, 1.6, 2.0])
    guides = (f'<line x1="{X(20)}" y1="{Y(1.0)}" x2="{X(20)}" y2="138" class="dsh"/>'
              f'<line x1="34" y1="{Y(1.0)}" x2="{X(20)}" y2="{Y(1.0)}" class="dsh"/>'
              f'<circle cx="{X(20)}" cy="{Y(1.0)}" r="2.6" fill="{ACCENT}"/>')
    return ('<svg width="230" height="158" viewBox="0 0 236 158">'
            '<style>.gr{stroke:#e3e3e3;stroke-width:0.7}.ax{stroke:#222;stroke-width:1.4}'
            '.lb{font-size:9px;font-family:Georgia,serif;fill:#333}.dsh{stroke:#999;stroke-width:0.9;stroke-dasharray:3,3}</style>'
            f'{grid}'
            '<line x1="34" y1="138" x2="222" y2="138" class="ax"/><polygon points="222,138 215,135 215,141" fill="#222"/>'
            '<line x1="34" y1="138" x2="34" y2="6" class="ax"/><polygon points="34,6 31,13 37,13" fill="#222"/>'
            f'{xt}{yt}{guides}'
            '<text x="196" y="134" class="lb">t, s</text><text x="38" y="12" class="lb">c, mol/l</text>'
            f'<path d="{path}" fill="none" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>'
            '</svg>')

def _beaker_solid(x, label, powder, color="#7a8a95", edge="#5b6a75", nbub=12):
    if powder:
        solid = "".join(f'<circle cx="{x+16+i*5}" cy="{88-(i%2)*3}" r="1.7" fill="{color}" stroke="{edge}" stroke-width="0.4"/>' for i in range(8))
        bubbles = "".join(f'<circle cx="{x+14+(i*7)%40}" cy="{50+(i*11)%32}" r="{1.5+(i%3)*0.7:.1f}" '
                          f'fill="none" stroke="#5b8bab" stroke-width="0.9"/>' for i in range(nbub))
    else:
        solid = f'<rect x="{x+24}" y="80" width="18" height="11" rx="2" fill="{color}" stroke="{edge}" stroke-width="0.8"/>'
        bubbles = "".join(f'<circle cx="{x+30+(i*9)%12}" cy="{62+(i*9)%22}" r="1.6" '
                          f'fill="none" stroke="#5b8bab" stroke-width="0.9"/>' for i in range(3))
    return (f'<g><rect x="{x+8}" y="46" width="50" height="46" rx="2" fill="#dcebf5"/>'
            f'{solid}{bubbles}'
            f'<path d="M{x+8},34 V90 q0,6 8,6 h34 q8,0 8,-6 V34" fill="none" stroke="#556" stroke-width="1.6"/>'
            f'<line x1="{x+4}" y1="34" x2="{x+62}" y2="34" stroke="#556" stroke-width="1.6"/>'
            f'<text x="{x+33}" y="112" text-anchor="middle" class="lb" font-weight="bold">{label}</text></g>')

def fig_beakers2():          # B-variant: rux + HCl
    return ('<svg width="220" height="122" viewBox="0 0 220 122">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + _beaker_solid(20, "1-idish · Zn bo'lagi", False)
            + _beaker_solid(120, "2-idish · Zn kukuni", True) + "</svg>")

def fig_beakers2_m():        # A-variant: marmar (oq CaCO3) + HCl, kukun CHAPDA
    return ('<svg width="220" height="122" viewBox="0 0 220 122">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + _beaker_solid(20, "1-idish · marmar kukuni", True, color="#e8e2d2", edge="#b8ad92", nbub=14)
            + _beaker_solid(120, "2-idish · marmar bo'lagi", False, color="#e8e2d2", edge="#b8ad92") + "</svg>")

def _vt_two(c1, c2, plateau, gas, steep_label_pos, slow_label_pos):
    def X(t): return 34 + t * 4.5
    def Y(v): return 130 - v
    def path(pts):
        return "M" + " L".join(f"{X(t):.0f},{Y(v):.0f}" for t, v in pts)
    return ('<svg width="230" height="150" viewBox="0 0 236 150">'
            '<style>.ax{stroke:#222;stroke-width:1.4}.lb{font-size:9px;font-family:Georgia,serif;fill:#333}'
            '.dsh{stroke:#999;stroke-width:0.9;stroke-dasharray:3,3}</style>'
            '<line x1="34" y1="130" x2="222" y2="130" class="ax"/><polygon points="222,130 215,127 215,133" fill="#222"/>'
            '<line x1="34" y1="130" x2="34" y2="6" class="ax"/><polygon points="34,6 31,13 37,13" fill="#222"/>'
            f'<line x1="34" y1="{Y(plateau)}" x2="214" y2="{Y(plateau)}" class="dsh"/>'
            f'<text x="6" y="{Y(plateau)+3}" class="lb">V(oxirgi)</text>'
            f'<text x="196" y="144" class="lb">t, s</text><text x="38" y="12" class="lb">V({gas})</text>'
            f'<path d="{path(c1)}" fill="none" stroke="{ACCENT2}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<path d="{path(c2)}" fill="none" stroke="{ACCENT}" stroke-width="2.2" stroke-dasharray="6,3" stroke-linejoin="round"/>'
            f'<text x="{X(steep_label_pos[0])}" y="{Y(steep_label_pos[1])}" class="lb" fill="{ACCENT2}" font-weight="bold">1</text>'
            f'<text x="{X(slow_label_pos[0])}" y="{Y(slow_label_pos[1])}" class="lb" fill="{ACCENT}" font-weight="bold">2</text>'
            '</svg>')

def fig_vt_two():            # B-variant: H2, 2-egri (punktir) tik — kukun
    return _vt_two([(0,0),(10,64),(20,96),(30,112),(40,112)],
                   [(0,0),(5,80),(10,104),(15,112),(40,112)], 112, "H₂", (14,70), (4,88))

def fig_vt_two_a():          # A-variant: CO2, 1-egri (uzluksiz) tik — kukun, plato 96
    return _vt_two([(0,0),(5,68),(10,88),(15,96),(40,96)],
                   [(0,0),(10,52),(20,80),(30,96),(40,96)], 96, "CO₂", (5,76), (16,58))

def fig_fridge():
    """Muzlatgich vs xona harorati — rangli o'rgatuvchi sahna."""
    return ('<svg width="250" height="130" viewBox="0 0 250 130">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # muzlatgich
            '<rect x="18" y="14" width="62" height="100" rx="6" fill="#dbeefc" stroke="#5b8bab" stroke-width="2"/>'
            '<line x1="18" y1="48" x2="80" y2="48" stroke="#5b8bab" stroke-width="1.6"/>'
            '<rect x="70" y="24" width="4" height="16" rx="2" fill="#5b8bab"/>'
            '<rect x="70" y="56" width="4" height="22" rx="2" fill="#5b8bab"/>'
            '<text x="28" y="38" font-size="15">❄</text>'
            '<rect x="28" y="66" width="12" height="20" rx="2" fill="#fff" stroke="#9bb"/>'
            '<circle cx="56" cy="78" r="7" fill="#e74c3c"/>'
            '<text x="24" y="126" class="lb" font-weight="bold">+4 °C</text>'
            # xona stoli
            '<rect x="150" y="86" width="80" height="6" rx="2" fill="#b98b4e"/>'
            '<rect x="156" y="92" width="6" height="24" fill="#a0783f"/><rect x="218" y="92" width="6" height="24" fill="#a0783f"/>'
            '<rect x="168" y="64" width="14" height="22" rx="2" fill="#fff" stroke="#9bb"/>'
            '<circle cx="202" cy="78" r="8" fill="#c0392b"/>'
            '<text x="150" y="30" font-size="15">☀</text>'
            '<text x="170" y="126" class="lb" font-weight="bold">+25 °C</text>'
            '<text x="96" y="70" class="lb" font-size="13">?</text></svg>')

def fig_car_cat():
    """Avtomobil katalitik neytralizatori."""
    return ('<svg width="270" height="118" viewBox="0 0 270 118">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # kuzov
            '<path d="M40,70 q6,-24 34,-26 l30,-2 q14,-14 34,-14 h28 q22,2 30,18 l6,24 z" fill="#e67e22" stroke="#b35c0e" stroke-width="1.6"/>'
            '<rect x="112" y="34" width="30" height="18" rx="3" fill="#d6ecf7" stroke="#b35c0e"/>'
            '<circle cx="76" cy="76" r="13" fill="#2c3e50"/><circle cx="76" cy="76" r="6" fill="#95a5a6"/>'
            '<circle cx="176" cy="76" r="13" fill="#2c3e50"/><circle cx="176" cy="76" r="6" fill="#95a5a6"/>'
            # chiqindi trubasi va katalizator
            '<rect x="20" y="88" width="34" height="14" rx="4" fill="#7f8c8d" stroke="#566"/>'
            '<line x1="54" y1="95" x2="66" y2="95" stroke="#566" stroke-width="4"/>'
            '<text x="20" y="115" class="lb" font-weight="bold">katalizator (Pt, Rh)</text>'
            '<text x="120" y="104" class="lb">CO, NOₓ →</text>'
            '<text x="2" y="86" class="lb">→ CO₂, N₂</text></svg>')

def fig_ship():
    """Kema korpusi va ingibitorli qoplama."""
    return ('<svg width="260" height="120" viewBox="0 0 260 120">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            '<path d="M30,74 h190 l-26,26 h-138 z" fill="#c0392b" stroke="#8e2418" stroke-width="1.6"/>'
            '<rect x="96" y="46" width="70" height="28" rx="2" fill="#ecf0f1" stroke="#95a5a6"/>'
            '<rect x="118" y="28" width="12" height="18" fill="#e74c3c"/>'
            '<circle cx="112" cy="60" r="3.4" fill="#5b8bab"/><circle cx="132" cy="60" r="3.4" fill="#5b8bab"/><circle cx="152" cy="60" r="3.4" fill="#5b8bab"/>'
            '<path d="M8,102 q14,-8 28,0 q14,8 28,0 q14,-8 28,0 q14,8 28,0 q14,-8 28,0 q14,8 28,0 q14,-8 28,0 q14,8 28,0" '
            'fill="none" stroke="#2980b9" stroke-width="2.6"/>'
            '<path d="M52,80 h146" stroke="#f4d03f" stroke-width="3" stroke-dasharray="8,4"/>'
            '<text x="60" y="118" class="lb" font-weight="bold">ingibitorli bo\'yoq qatlami</text></svg>')

def fig_campfire():
    """Yirik o'tin vs mayda cho'plar."""
    def flame(cx, base, s):
        return (f'<path d="M{cx},{base} q{-7*s},{-9*s} {-2*s},{-17*s} q{3*s},{-6*s} {2*s},{-11*s} '
                f'q{6*s},{7*s} {3*s},{14*s} q{5*s},{-2*s} {4*s},{5*s} q{-1*s},{7*s} {-7*s},{9*s} z" '
                f'fill="#f39c12" stroke="#d35400" stroke-width="1"/>'
                f'<path d="M{cx},{base} q{-3*s},{-5*s} {-1*s},{-9*s} q{3*s},{4*s} {2*s},{6*s} z" fill="#f9e79f"/>')
    return ('<svg width="260" height="120" viewBox="0 0 260 120">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # 1: yaxlit g'o'la — kichik alanga
            '<rect x="22" y="86" width="76" height="16" rx="8" fill="#8d5a2b" stroke="#6e451f" stroke-width="1.4"/>'
            + flame(62, 86, 0.9) +
            '<text x="30" y="116" class="lb" font-weight="bold">1 · yaxlit g\'o\'la</text>'
            # 2: mayda cho'plar — katta alanga
            '<g stroke="#8d5a2b" stroke-width="4" stroke-linecap="round">'
            '<line x1="158" y1="98" x2="196" y2="88"/><line x1="166" y1="88" x2="204" y2="98"/>'
            '<line x1="172" y1="100" x2="210" y2="92"/><line x1="162" y1="92" x2="200" y2="102"/></g>'
            + flame(184, 84, 1.5) +
            '<text x="152" y="116" class="lb" font-weight="bold">2 · mayda cho\'plar</text></svg>')

FIGS = dict(energy=fig_energy, ct_read=fig_ct_read, beakers2=fig_beakers2, vt_two=fig_vt_two,
            beakers2_m=fig_beakers2_m, vt_two_a=fig_vt_two_a,
            fridge=fig_fridge, car_cat=fig_car_cat, ship=fig_ship, campfire=fig_campfire)

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
H = [f"<meta charset='utf-8'><title>5-bob — Kimyoviy reaksiya tezligi</title><style>{css}</style>"]

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
  <div class="chapnum">5</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 5-bob · Mavzu pasporti (I.5)</div>
  <h1>Kimyoviy reaksiya tezligi</h1>
  <div class="lead">o'rtacha tezlik · ta'sir etuvchi omillar · Vant-Goff qoidasi · stexiometrik tezlik
  nisbatlari · katalizator va ingibitor</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>v = Δc/Δt bo'yicha o'rtacha tezlik hisobi</li>
      <li>Vant-Goff: γ, Δt, marta — uchalasini topish</li>
      <li>tezliklarning stexiometrik nisbatlari</li>
      <li>bosim/konsentratsiya ta'siri (darajali qonun)</li>
      <li>omillarni birgalikda qo'llash (kombinatsiya)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>c–t grafigini o'qish va tanlash (4, 32)</li>
      <li>v–T bog'liqlik grafigi (27)</li>
      <li>tajriba jadvalidan tartiblarni aniqlash (17)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>hajmga bo'lishni unutish (mol ≠ mol/l)</li>
      <li>γ ni darajaga ko'tarmasdan ko'paytirish</li>
      <li>stexiometrik koeffitsiyentni e'tiborsiz qoldirish</li>
      <li>harorat pasayishida ham "ortadi" deb olish</li></ul></div>
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