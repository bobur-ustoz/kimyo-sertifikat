# -*- coding: utf-8 -*-
"""6-bob (Kimyoviy muvozanat) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I6A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I6B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="#1e8449" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.6 figuralari ----------
def fig_ct_eq():
    """B-variant hisob grafigi (6-bob uslubi: yashil, soya-fill, dumaloq markerlar)."""
    G1, G2 = "#1e8449", "#b9770e"
    def X(t): return 40 + t * 3.0
    def Y(c): return 146 - c * 150
    n2o4 = [(0, 0.6), (10, 0.42), (20, 0.30), (30, 0.235), (40, 0.21), (50, 0.2), (60, 0.2)]
    no2 = [(0, 0.0), (10, 0.36), (20, 0.60), (30, 0.73), (40, 0.78), (50, 0.8), (60, 0.8)]
    def path(pts):
        return "M" + " L".join(f"{X(t):.0f},{Y(c):.0f}" for t, c in pts)
    area = path(no2) + f" L{X(60):.0f},{Y(0):.0f} L{X(0):.0f},{Y(0):.0f} Z"
    yt = "".join(f'<line x1="36" y1="{Y(c):.0f}" x2="222" y2="{Y(c):.0f}" class="gr"/>'
                 f'<text x="12" y="{Y(c)+3:.0f}" class="lb">{c:.1f}</text>'.replace(".", ",")
                 for c in [0.2, 0.4, 0.6, 0.8])
    xt = "".join(f'<line x1="{X(t)}" y1="146" x2="{X(t)}" y2="150" stroke="#1b4332" stroke-width="1.1"/>'
                 f'<text x="{X(t)-6}" y="160" class="lb">{t}</text>' for t in range(0, 61, 20))
    mk1 = "".join(f'<circle cx="{X(t)}" cy="{Y(c):.0f}" r="2.8" fill="#fff" stroke="{G1}" stroke-width="1.6"/>'
                  for t, c in no2 if t % 20 == 0)
    mk2 = "".join(f'<circle cx="{X(t)}" cy="{Y(c):.0f}" r="2.8" fill="{G2}"/>' for t, c in n2o4 if t % 20 == 0)
    return ('<svg width="230" height="170" viewBox="0 0 236 170">'
            '<style>.gr{stroke:#cfe3d6;stroke-width:0.8;stroke-dasharray:1.5,2.5}'
            '.lb{font-size:9px;font-family:Georgia,serif;fill:#1b4332}</style>'
            '<rect x="36" y="4" width="190" height="142" rx="5" fill="#f4faf5" stroke="#1b4332" stroke-width="1.3"/>'
            f'{yt}{xt}'
            f'<path d="{area}" fill="{G1}" opacity="0.10" stroke="none"/>'
            f'<path d="{path(no2)}" fill="none" stroke="{G1}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<path d="{path(n2o4)}" fill="none" stroke="{G2}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'{mk1}{mk2}'
            f'<rect x="150" y="12" width="70" height="26" rx="3" fill="#fff" stroke="#cfe3d6"/>'
            f'<circle cx="159" cy="20" r="3" fill="#fff" stroke="{G1}" stroke-width="1.6"/>'
            f'<text x="166" y="23" class="lb" font-weight="bold">NO₂</text>'
            f'<circle cx="159" cy="31" r="3" fill="{G2}"/>'
            f'<text x="166" y="34" class="lb" font-weight="bold">N₂O₄</text>'
            '<text x="196" y="166" class="lb">t, s</text><text x="8" y="14" class="lb">c, mol/l</text>'
            '</svg>')

def fig_vt_eq():
    """A-variant: to'g'ri (1, pasayuvchi) va teskari (2, o'suvchi) tezliklar t1 da tenglashadi."""
    def X(t): return 34 + t * 4.5
    def Y(v): return 130 - v
    p1 = "M" + " L".join(f"{X(t):.0f},{Y(v):.0f}" for t, v in
                         [(0, 110), (8, 78), (16, 60), (24, 50), (30, 46), (40, 46)])
    p2 = "M" + " L".join(f"{X(t):.0f},{Y(v):.0f}" for t, v in
                         [(0, 0), (8, 22), (16, 34), (24, 42), (30, 46), (40, 46)])
    return ('<svg width="230" height="150" viewBox="0 0 236 150">'
            '<style>.ax{stroke:#222;stroke-width:1.4}.lb{font-size:9px;font-family:Georgia,serif;fill:#333}'
            '.dsh{stroke:#999;stroke-width:0.9;stroke-dasharray:3,3}</style>'
            '<line x1="34" y1="130" x2="222" y2="130" class="ax"/><polygon points="222,130 215,127 215,133" fill="#222"/>'
            '<line x1="34" y1="130" x2="34" y2="6" class="ax"/><polygon points="34,6 31,13 37,13" fill="#222"/>'
            f'<line x1="{X(30)}" y1="{Y(46)}" x2="{X(30)}" y2="130" class="dsh"/>'
            f'<text x="{X(30)-4}" y="143" class="lb" font-weight="bold">t₁</text>'
            '<text x="198" y="144" class="lb">t</text><text x="38" y="12" class="lb">v</text>'
            f'<path d="{p1}" fill="none" stroke="#1e8449" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<path d="{p2}" fill="none" stroke="#b9770e" stroke-width="2.4" stroke-dasharray="6,3" stroke-linejoin="round"/>'
            f'<text x="{X(4)}" y="{Y(96)}" class="lb" fill="#1e8449" font-weight="bold">1 · to\'g\'ri</text>'
            f'<text x="{X(10)}" y="{Y(14)}" class="lb" fill="#b9770e" font-weight="bold">2 · teskari</text>'
            f'<text x="{X(32)}" y="{Y(56)}" class="lb">muvozanat</text>'
            '</svg>')

def fig_soda():
    """Gazli ichimlik: yopiq va ochilgan shisha."""
    def bottle(x, opened, bub):
        cap = ('<rect x="%d" y="14" width="18" height="8" rx="2" fill="#c0392b" stroke="#8e2418"/>' % (x + 11)) \
            if not opened else \
            ('<rect x="%d" y="2" width="18" height="8" rx="2" fill="#c0392b" stroke="#8e2418" transform="rotate(24 %d 6)"/>' % (x + 30, x + 39))
        bubbles = "".join(f'<circle cx="{x+12+(i*7)%16}" cy="{54+(i*13)%44}" r="{1.3+(i%3)*0.6:.1f}" '
                          f'fill="none" stroke="#5b8bab" stroke-width="0.9"/>' for i in range(bub))
        fizz = ""
        if opened:
            fizz = "".join(f'<circle cx="{x+16+(i*5)%10}" cy="{16-(i*6)%12}" r="{1.2+(i%2)*0.6:.1f}" '
                           f'fill="none" stroke="#95a5a6" stroke-width="0.9"/>' for i in range(6))
        return (f'<g>{cap}{fizz}'
                f'<path d="M{x+13},22 v8 q-9,7 -9,18 v44 q0,6 7,6 h18 q7,0 7,-6 v-44 q0,-11 -9,-18 v-8 z" '
                f'fill="#dcebf5" stroke="#5b8bab" stroke-width="1.6"/>'
                f'{bubbles}</g>')
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + bottle(30, False, 5)
            + '<text x="18" y="116" class="lb" font-weight="bold">yopiq · P katta</text>'
            + '<line x1="106" y1="60" x2="136" y2="60" stroke="#556" stroke-width="1.6"/>'
            + '<polygon points="140,60 132,56 132,64" fill="#556"/>'
            + '<text x="104" y="52" class="lb">ochildi</text>'
            + bottle(150, True, 14)
            + '<text x="138" y="116" class="lb" font-weight="bold">ochiq · «vish-sh!»</text></svg>')

def fig_plant():
    """Ammiak zavodi: reaktor kolonnasi, quvurlar."""
    return ('<svg width="260" height="126" viewBox="0 0 260 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # reaktor kolonnasi
            '<rect x="104" y="18" width="40" height="80" rx="12" fill="#aab7c4" stroke="#5d6d7e" stroke-width="1.8"/>'
            '<line x1="104" y1="44" x2="144" y2="44" stroke="#5d6d7e" stroke-width="1"/>'
            '<line x1="104" y1="70" x2="144" y2="70" stroke="#5d6d7e" stroke-width="1"/>'
            '<text x="110" y="60" class="lb" font-weight="bold">Fe kat.</text>'
            '<text x="107" y="34" class="lb">450 °C</text><text x="106" y="90" class="lb">250 atm</text>'
            # kiruvchi quvurlar
            '<path d="M20,36 h60 q10,0 12,8" fill="none" stroke="#2980b9" stroke-width="4"/>'
            '<text x="18" y="28" class="lb" font-weight="bold">N₂</text>'
            '<path d="M20,86 h60 q10,0 12,-8" fill="none" stroke="#16a085" stroke-width="4"/>'
            '<text x="18" y="104" class="lb" font-weight="bold">H₂</text>'
            # chiquvchi
            '<path d="M144,58 h50 q8,0 8,8 v30" fill="none" stroke="#e67e22" stroke-width="4"/>'
            '<text x="206" y="112" class="lb" font-weight="bold">NH₃</text>'
            # tutun/minora dekor
            '<rect x="176" y="14" width="10" height="30" fill="#95a5a6"/>'
            '<circle cx="181" cy="10" r="4" fill="none" stroke="#bdc3c7" stroke-width="1.4"/>'
            '<circle cx="187" cy="5" r="5" fill="none" stroke="#bdc3c7" stroke-width="1.4"/>'
            '<text x="82" y="122" class="lb">N₂ + 3H₂ ⇌ 2NH₃ + Q</text></svg>')

def fig_cave():
    """G'or: stalaktit, tomchi, stalagmit."""
    return ('<svg width="240" height="126" viewBox="0 0 240 126">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            # g'or shifti va poli
            '<path d="M10,16 h220 v6 q-40,4 -70,2 q-50,-3 -80,1 q-40,4 -70,-2 z" fill="#8d6e63" stroke="#5d4037" stroke-width="1.4"/>'
            '<path d="M10,112 h220 v8 h-220 z" fill="#8d6e63" stroke="#5d4037" stroke-width="1.4"/>'
            # stalaktitlar
            '<path d="M70,22 l7,34 l7,-34 z" fill="#d7ccc8" stroke="#a1887f" stroke-width="1.2"/>'
            '<path d="M110,22 l5,22 l5,-22 z" fill="#d7ccc8" stroke="#a1887f" stroke-width="1.2"/>'
            '<path d="M150,22 l6,28 l6,-28 z" fill="#d7ccc8" stroke="#a1887f" stroke-width="1.2"/>'
            # tomchi
            '<circle cx="77" cy="66" r="2.6" fill="#7fb3d3"/>'
            '<circle cx="77" cy="80" r="2.2" fill="#7fb3d3"/>'
            # CO2 chiqishi
            '<path d="M95,74 q4,-6 0,-12 M104,72 q4,-6 0,-12" stroke="#95a5a6" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
            '<text x="112" y="66" class="lb">CO₂↑</text>'
            # stalagmit
            '<path d="M63,112 l14,-30 l14,30 z" fill="#d7ccc8" stroke="#a1887f" stroke-width="1.2"/>'
            '<text x="30" y="124" class="lb" font-weight="bold">stalaktit va stalagmit o\'sishi</text></svg>')

def fig_no2():
    """Ikki probirka: issiq (to'q qo'ng'ir NO2) va sovuq (och)."""
    def tube(x, color, label, sub):
        return (f'<rect x="{x+6}" y="30" width="22" height="56" rx="10" fill="{color}" stroke="#556" stroke-width="1.6"/>'
                f'<line x1="{x+2}" y1="30" x2="{x+32}" y2="30" stroke="#556" stroke-width="1.6"/>'
                f'<text x="{x+17}" y="118" text-anchor="middle" class="lb" font-weight="bold">{label}</text>'
                f'<text x="{x+17}" y="128" text-anchor="middle" class="lb">{sub}</text>')
    return ('<svg width="230" height="132" viewBox="0 0 230 132">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # issiq stakan
            '<rect x="28" y="66" width="60" height="36" rx="3" fill="#fdebd0" stroke="#e67e22" stroke-width="1.4"/>'
            '<text x="34" y="62" font-size="11">♨</text><text x="48" y="62" font-size="11">♨</text>'
            + tube(40, "#7B3F00", "issiq suvda", "to'q qo'ng'ir")
            # muzli stakan
            + '<rect x="140" y="66" width="60" height="36" rx="3" fill="#d6ecf7" stroke="#5b8bab" stroke-width="1.4"/>'
            + '<text x="146" y="62" font-size="11">❄</text><text x="160" y="62" font-size="11">❄</text>'
            + tube(152, "#d9b38c", "muzda", "och rangli")
            + '</svg>')

def fig_piston():
    """Porshenli idish: siqilishdan oldin va keyin (NO2/N2O4 rangi)."""
    def vessel(x, ph, color, label):
        # ph — porshen balandligi (gaz ustuni)
        top = 96 - ph
        return (f'<g><rect x="{x}" y="{top}" width="54" height="{ph}" fill="{color}"/>'
                f'<rect x="{x}" y="{top-9}" width="54" height="9" fill="#7f8c8d" stroke="#4d5656" stroke-width="1.2"/>'
                f'<line x1="{x+27}" y1="{top-9}" x2="{x+27}" y2="{top-30}" stroke="#4d5656" stroke-width="3.5"/>'
                f'<line x1="{x+17}" y1="{top-30}" x2="{x+37}" y2="{top-30}" stroke="#4d5656" stroke-width="3.5"/>'
                f'<path d="M{x},{top-9} V96 h54 V{top-9}" fill="none" stroke="#556" stroke-width="1.8"/>'
                f'<line x1="{x}" y1="96" x2="{x+54}" y2="96" stroke="#556" stroke-width="1.8"/>'
                f'<text x="{x+27}" y="112" text-anchor="middle" class="lb" font-weight="bold">{label}</text></g>')
    return ('<svg width="240" height="120" viewBox="0 0 240 120">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            + vessel(28, 58, "#c9884a", "V · och qo'ng'ir")
            + '<line x1="104" y1="66" x2="132" y2="66" stroke="#556" stroke-width="1.6"/>'
            + '<polygon points="136,66 128,62 128,70" fill="#556"/>'
            + '<text x="102" y="58" class="lb">siqildi</text>'
            + vessel(150, 29, "#8a5a28", "V/2 · rang?")
            + '</svg>')

FIGS = dict(ct_eq=fig_ct_eq, vt_eq=fig_vt_eq, soda=fig_soda, plant=fig_plant, cave=fig_cave, no2=fig_no2,
            piston=fig_piston)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bcd9c4; border-radius:2pt;
                  background:#f4faf5; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>6-bob — Kimyoviy muvozanat</title><style>{css}</style>"]

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
  <div class="chapnum">6</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 6-bob · Mavzu pasporti (I.6)</div>
  <h1>Kimyoviy muvozanat</h1>
  <div class="lead">qaytar reaksiyalar · muvozanat konstantasi va ICE jadvali · Le Chatelier prinsipi ·
  dissotsiatsiya darajasi · sanoat jarayonlarida optimal sharoit</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>Kc ifodasi va hisobi (bir jinsli/heterogen)</li>
      <li>ICE: boshlang'ich ↔ muvozanat konsentratsiyalari</li>
      <li>Le Chatelier: T, P, c, katalizator, inert gaz</li>
      <li>dissotsiatsiya darajasi va konversiya</li>
      <li>Kc–T bog'lanishidan termik xarakterni aniqlash</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>c–t va v–t grafiklarini o'qish (A: 26, 32; B: 4, 5, 32)</li>
      <li>jadvaldan muvozanat vaqtini aniqlash (A: 20; B: 17)</li>
      <li>hayotiy sahnalarni tahlil qilish (A: 4, 8, 13, 18)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>«muvozanatda konsentratsiyalar teng» degan xato tasavvur</li>
      <li>koeffitsiyentni daraja o'rniga ko'paytuvchi qilish</li>
      <li>katalizator/inert gaz muvozanatni siljitadi deb o'ylash</li>
      <li>sarflangan miqdor bilan muvozanat qiymatini adashtirish</li></ul></div>
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
