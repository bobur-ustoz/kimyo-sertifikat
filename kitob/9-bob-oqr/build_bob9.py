# -*- coding: utf-8 -*-
"""9-bob (OQR) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I9A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I9B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="#6c3483" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.9 figuralari ----------
def fig_apple():
    """Kesilgan olma: yangi (och) va qoraygan bo'lak."""
    def half(x, flesh, spots):
        s = "".join(f'<circle cx="{x+18+(i*11)%26}" cy="{52+(i*17)%30}" r="{2.5+(i%2):.0f}" fill="#8d6e3f" opacity="0.7"/>'
                    for i in range(spots))
        return (f'<g><ellipse cx="{x+30}" cy="60" rx="30" ry="34" fill="{flesh}" stroke="#c62828" stroke-width="3"/>'
                f'<ellipse cx="{x+30}" cy="60" rx="8" ry="12" fill="none" stroke="#a1887f" stroke-width="1.2"/>'
                f'<ellipse cx="{x+30}" cy="56" rx="1.6" ry="4" fill="#5d4037"/>'
                f'<ellipse cx="{x+30}" cy="64" rx="1.6" ry="4" fill="#5d4037"/>'
                f'<path d="M{x+30},26 q4,-10 10,-12" stroke="#5d4037" stroke-width="2.4" fill="none"/>{s}</g>')
    return ('<svg width="240" height="126" viewBox="0 0 240 126">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + half(20, "#fff8e1", 0)
            + '<text x="24" y="116" class="lb" font-weight="bold">hozir kesildi</text>'
            + '<line x1="98" y1="60" x2="128" y2="60" stroke="#556" stroke-width="1.6"/>'
            + '<polygon points="132,60 124,56 124,64" fill="#556"/>'
            + '<text x="94" y="50" class="lb">15 daqiqa</text><text x="100" y="74" class="lb">havoda</text>'
            + half(140, "#e8d5a3", 8)
            + '<text x="150" y="116" class="lb" font-weight="bold">qoraydi</text></svg>')

def fig_firework():
    """Bengal olovi / otashin: uchqunlar sochayotgan tayoqcha."""
    import math
    sparks = ""
    for i in range(16):
        ang = i * 22.5 * 3.14159 / 180
        r1, r2 = 12, 26 + (i % 3) * 8
        x1, y1 = 120 + r1 * math.cos(ang), 46 + r1 * math.sin(ang)
        x2, y2 = 120 + r2 * math.cos(ang), 46 + r2 * math.sin(ang)
        sparks += (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
                   f'stroke="{"#f4d03f" if i%2 else "#f39c12"}" stroke-width="1.8" stroke-linecap="round"/>')
        if i % 3 == 0:
            sparks += f'<circle cx="{x2:.0f}" cy="{y2:.0f}" r="1.8" fill="#fff3c4"/>'
    return ('<svg width="240" height="126" viewBox="0 0 240 126">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            '<rect x="117" y="52" width="6" height="60" rx="2" fill="#7f8c8d" stroke="#4d5656"/>'
            '<circle cx="120" cy="46" r="9" fill="#fff3c4" stroke="#f39c12" stroke-width="2"/>'
            + sparks +
            '<text x="30" y="30" class="lb" font-weight="bold">2Mg + O₂ → 2MgO</text>'
            '<text x="30" y="44" class="lb">yorqin oq alanga</text>'
            '<text x="72" y="120" class="lb" font-weight="bold">bayram otashini (bengal olovi)</text></svg>')

def fig_fence():
    """Zanglagan temir panjara va yomg'ir."""
    rust = "".join(f'<circle cx="{34+(i*23)%160}" cy="{56+(i*13)%40}" r="{2+(i%3):.0f}" fill="#b5651d" opacity="0.75"/>'
                   for i in range(14))
    rain = "".join(f'<line x1="{30+i*26}" y1="{10+(i%2)*4}" x2="{26+i*26}" y2="{22+(i%2)*4}" '
                   f'stroke="#7fb3d3" stroke-width="1.6" stroke-linecap="round"/>' for i in range(8))
    bars = "".join(f'<rect x="{36+i*32}" y="36" width="7" height="66" rx="2" fill="#95a5a6" stroke="#5d6d7e"/>'
                   f'<polygon points="{39.5+i*32},26 {33+i*32},38 {46+i*32},38" fill="#95a5a6" stroke="#5d6d7e"/>'
                   for i in range(6))
    return ('<svg width="240" height="126" viewBox="0 0 240 126">'
            '<style>.lb{font-size:9.5px;font-family:Georgia,serif;fill:#333}</style>'
            + rain + bars +
            '<rect x="24" y="52" width="192" height="7" fill="#95a5a6" stroke="#5d6d7e"/>'
            '<rect x="24" y="88" width="192" height="7" fill="#95a5a6" stroke="#5d6d7e"/>'
            + rust +
            '<text x="52" y="120" class="lb" font-weight="bold">yomg\'irda zanglagan panjara</text></svg>')

def fig_battery():
    """Cho'ntak batareykasi kesimi: Zn g'ilof, uglerod sterjen."""
    return ('<svg width="220" height="126" viewBox="0 0 220 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # korpus (Zn)
            '<rect x="60" y="26" width="56" height="84" rx="6" fill="#cfd8dc" stroke="#546e7a" stroke-width="2.4"/>'
            # ichki pasta
            '<rect x="68" y="34" width="40" height="70" rx="4" fill="#37474f"/>'
            # uglerod sterjen
            '<rect x="84" y="18" width="8" height="82" rx="3" fill="#212121"/>'
            '<rect x="80" y="12" width="16" height="8" rx="2" fill="#b0bec5" stroke="#546e7a"/>'
            '<text x="124" y="26" class="lb">+ qutb (C sterjen)</text>'
            '<text x="124" y="66" class="lb">Zn g\'ilof — qaytaruvchi</text>'
            '<text x="124" y="80" class="lb">Zn⁰ − 2e → Zn⁺²</text>'
            '<line x1="120" y1="62" x2="112" y2="62" stroke="#556" stroke-width="1.2"/>'
            '<text x="52" y="122" class="lb" font-weight="bold">cho\'ntak batareykasi (kesim)</text></svg>')

def fig_activity():
    """Metallar aktivlik qatori — chiziqli lenta, H2 belgisi bilan."""
    metals = ["K", "Na", "Ca", "Mg", "Al", "Zn", "Fe", "Ni", "Sn", "Pb", "H₂", "Cu", "Hg", "Ag", "Au"]
    cells = ""
    for i, m in enumerate(metals):
        x = 8 + i * 15
        hl = (m == "H₂")
        cells += (f'<rect x="{x}" y="30" width="14" height="20" rx="2" '
                  f'fill="{"#f9e79f" if hl else "#dcebf5"}" stroke="#5b8bab" stroke-width="0.9"/>'
                  f'<text x="{x+7}" y="44" text-anchor="middle" class="lb" '
                  f'font-weight="{"bold" if hl else "normal"}">{m}</text>')
    return ('<svg width="245" height="86" viewBox="0 0 245 86">'
            '<style>.lb{font-size:7.6px;font-family:Georgia,serif;fill:#333}</style>'
            + cells +
            '<line x1="8" y1="62" x2="232" y2="62" stroke="#556" stroke-width="1.4"/>'
            '<polygon points="236,62 228,58 228,66" fill="#556"/>'
            '<text x="8" y="76" class="lb" font-weight="bold">aktivlik kamayadi →</text>'
            '<text x="8" y="24" class="lb">metallarning aktivlik qatori</text></svg>')

def fig_e_graph():
    """B-variant: n(e) = 3·n(Me) grafigi — o'qiladigan nuqtalar bilan."""
    def X(n): return 38 + n * 480      # n 0..0,4 -> 38..230
    def Y(e): return 138 - e * 110     # e 0..1,2 -> 138..6
    pts = [(0, 0), (0.1, 0.3), (0.2, 0.6), (0.3, 0.9), (0.4, 1.2)]
    path = "M" + " L".join(f"{X(n):.0f},{Y(e):.0f}" for n, e in pts)
    grid = "".join(f'<line x1="{X(n)}" y1="8" x2="{X(n)}" y2="138" class="gr"/>' for n in [0.1, 0.2, 0.3, 0.4]) + \
           "".join(f'<line x1="38" y1="{Y(e):.0f}" x2="230" y2="{Y(e):.0f}" class="gr"/>' for e in [0.3, 0.6, 0.9, 1.2])
    xt = "".join(f'<text x="{X(n)-8}" y="150" class="lb">{n:.1f}</text>'.replace(".", ",") for n in [0.1, 0.2, 0.3, 0.4])
    yt = "".join(f'<text x="12" y="{Y(e)+3:.0f}" class="lb">{e:.1f}</text>'.replace(".", ",") for e in [0.3, 0.6, 0.9, 1.2])
    guides = (f'<line x1="{X(0.2)}" y1="{Y(0.6)}" x2="{X(0.2)}" y2="138" class="dsh"/>'
              f'<line x1="38" y1="{Y(0.6)}" x2="{X(0.2)}" y2="{Y(0.6)}" class="dsh"/>'
              f'<circle cx="{X(0.2)}" cy="{Y(0.6)}" r="2.6" fill="{ACCENT}"/>'
              f'<circle cx="{X(0.3)}" cy="{Y(0.9)}" r="2.6" fill="{ACCENT}"/>')
    P1 = "#6c3483"
    mk = "".join(f'<rect x="{X(n)-3:.0f}" y="{Y(e)-3:.0f}" width="6" height="6" fill="{P1}" stroke="#fff" stroke-width="1" '
                 f'transform="rotate(45 {X(n):.0f} {Y(e):.0f})"/>' for n, e in pts)
    return ('<svg width="232" height="158" viewBox="0 0 238 158">'
            '<style>.gr{stroke:#e2d5ec;stroke-width:0.9}.ax{stroke:#4a235a;stroke-width:1.5}'
            '.lb{font-size:9px;font-family:Georgia,serif;fill:#4a235a}.dsh{stroke:#6c3483;stroke-width:1;stroke-dasharray:2,3}</style>'
            '<rect x="38" y="4" width="192" height="134" rx="4" fill="#faf6fd" stroke="#c9b3d8" stroke-width="1"/>'
            f'{grid}'
            '<line x1="38" y1="138" x2="234" y2="138" class="ax"/><polygon points="234,138 227,135 227,141" fill="#4a235a"/>'
            '<line x1="38" y1="138" x2="38" y2="4" class="ax"/><polygon points="38,4 35,11 41,11" fill="#4a235a"/>'
            f'{xt}{yt}{guides}'
            '<text x="184" y="134" class="lb">n(Me), mol</text><text x="42" y="14" class="lb">n(e), mol</text>'
            f'<path d="{path}" fill="none" stroke="{P1}" stroke-width="2.4"/>'
            f'{mk}'
            '</svg>')

def fig_cu_hno3():
    """Probirka: mis + kons HNO3, qo'ng'ir gaz."""
    fumes = "".join(f'<circle cx="{104+(i*9)%22}" cy="{30-(i*8)%20}" r="{3+(i%3):.0f}" '
                    f'fill="#b5651d" opacity="{0.5-(i%3)*0.1:.1f}"/>' for i in range(8))
    bubbles = "".join(f'<circle cx="{100+(i*7)%22}" cy="{72+(i*9)%20}" r="{1.4+(i%2)*0.6:.1f}" '
                      f'fill="none" stroke="#8d5a2b" stroke-width="0.9"/>' for i in range(8))
    return ('<svg width="200" height="132" viewBox="0 0 200 132">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            + fumes +
            '<rect x="96" y="58" width="30" height="52" rx="12" fill="#d6ecf7" stroke="#556" stroke-width="1.6"/>'
            '<rect x="96" y="42" width="30" height="20" fill="none" stroke="#556" stroke-width="1.6"/>'
            '<line x1="92" y1="42" x2="130" y2="42" stroke="#556" stroke-width="1.6"/>'
            '<rect x="104" y="88" width="14" height="10" rx="2" fill="#d35400" stroke="#a04000"/>'
            + bubbles +
            '<text x="10" y="34" class="lb" font-weight="bold">qo\'ng\'ir gaz ↑</text>'
            '<text x="10" y="80" class="lb">HNO₃ (kons.)</text>'
            '<text x="10" y="96" class="lb">Cu parchasi →</text>'
            '<text x="46" y="126" class="lb" font-weight="bold">tajriba (mo\'rili shkafda!)</text></svg>')


def fig_bar_alkan():
    """Ustunli diagramma (binafsha): 1 mol alkan yonishida beriladigan elektron mollari."""
    P1 = "#6c3483"
    data = [("pentan", 32), ("geksan", 38), ("geptan", 44), ("oktan", 50)]
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 52 + i * 47; h = v * 2.1; y = 126 - h
        bars += (f'<rect x="{x}" y="{y:.0f}" width="28" height="{h:.0f}" rx="2" fill="{P1}" opacity="0.8" stroke="#4a235a" stroke-width="1"/>'
                 f'<text x="{x+14}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+14}" y="140" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="148" viewBox="0 0 250 148">'
            '<style>.lb{font-size:8.6px;font-family:Georgia,serif;fill:#4a235a}</style>'
            '<rect x="40" y="4" width="204" height="122" rx="4" fill="#faf6fd" stroke="#c9b3d8" stroke-width="1"/>'
            + "".join(f'<line x1="42" y1="{126-v*2.1:.0f}" x2="242" y2="{126-v*2.1:.0f}" stroke="#e2d5ec" stroke-width="0.9"/>'
                      f'<text x="26" y="{129-v*2.1:.0f}" class="lb">{v}</text>' for v in [20,40])
            + bars + '<line x1="40" y1="126" x2="244" y2="126" stroke="#4a235a" stroke-width="1.5"/>'
            '<text x="6" y="14" class="lb">n(e), mol</text></svg>')


def fig_gasrig():
    """Gaz olish qurilmasi: kolba + tomchi voronka + naycha + yig'ish silindri (binafsha)."""
    return ('<svg width="260" height="132" viewBox="0 0 260 132">'
            '<style>.lb{font-size:8.4px;font-family:Georgia,serif;fill:#4a235a}</style>'
            '<path d="M46,58 q-20,44 12,52 q34,8 44,-16 q6,-18 -8,-36 z" fill="#faf6fd" stroke="#4a235a" stroke-width="1.8"/>'
            '<rect x="58" y="94" width="30" height="12" fill="#c9b3d8" opacity="0.7"/>'
            '<text x="52" y="90" class="lb">KMnO\u2084</text>'
            '<path d="M62,58 v-22 h-6 l10,-14 l10,14 h-6 v22" fill="#fff" stroke="#4a235a" stroke-width="1.4"/>'
            '<text x="16" y="26" class="lb">HCl (kons.)</text>'
            '<line x1="88" y1="62" x2="170" y2="46" stroke="#4a235a" stroke-width="2.2"/>'
            '<rect x="176" y="40" width="40" height="76" rx="4" fill="#faf6fd" stroke="#4a235a" stroke-width="1.8"/>'
            '<rect x="178" y="42" width="36" height="34" fill="#cdd94b" opacity="0.5"/>'
            '<text x="222" y="60" class="lb" font-weight="bold" fill="#6c3483">Cl\u2082</text>'
            '<text x="46" y="128" class="lb" font-weight="bold">gaz olish qurilmasi (mo\'rili shkafda!)</text></svg>')

FIGS = dict(apple=fig_apple, gasrig=fig_gasrig, bar_alkan=fig_bar_alkan,  firework=fig_firework, fence=fig_fence, battery=fig_battery,
            activity=fig_activity, e_graph=fig_e_graph, cu_hno3=fig_cu_hno3)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #d5c3e2; border-radius:2pt;
                  background:#faf6fd; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>9-bob — Oksidlanish-qaytarilish</title><style>{css}</style>"]

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
  <div class="chapnum">9</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 9-bob · Mavzu pasporti (I.9)</div>
  <h1>Oksidlanish-qaytarilish reaksiyalari</h1>
  <div class="lead">oksidlanish darajasi · elektron balans va koeffitsiyentlar · oksidlovchi/qaytaruvchi ·
  OQR turlari (molekulyararo, ichki molekulyar, disproporsiya) · aktivlik qatori</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>darajani aniqlash (murakkab tuzlarda ham)</li>
      <li>elektron balans: koeffitsiyentlar yig'indisi</li>
      <li>mol-massa-hajm hisoblari e-balans orqali</li>
      <li>oksidlovchi/qaytaruvchini topish va tasniflash</li>
      <li>parametrli (alkan-elektron, teskari) masalalar</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>daraja/balans jadvallarini o'qish (A: 17; B: 5, 17, 29)</li>
      <li>n(e)–n(Me) grafigi bilan ishlash (B: 27, 32)</li>
      <li>aktivlik qatori va tajriba rasmlari (A: 32; B: 28)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>koeffitsiyent bilan indeksni adashtirish</li>
      <li>«e bergan — qaytariladi» degan teskari tasavvur</li>
      <li>disproporsiyani molekulyararo OQR bilan chalkashtirish</li>
      <li>HCl kabi moddaning ikki vazifasini (qaytaruvchi + muhit) unutish</li></ul></div>
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
