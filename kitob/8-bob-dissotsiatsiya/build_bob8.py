# -*- coding: utf-8 -*-
"""8-bob (Dissotsiatsiya/pH) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I8A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I8B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="#c2185b" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.8 figuralari (pushti-qizil «indikator» palitrasi) ----------
R1, R2, RD, RP, RG = "#c2185b", "#00838f", "#6d1b45", "#fdf5f8", "#f3d9e6"

def fig_cond_curve():
    """B: H2SO4 + Ba(OH)2 — o'tkazuvchanlik U-egri chizig'i, minimal M nuqta."""
    def X(v): return 38 + v * 1.9      # qo'shilgan hajm 0..100
    def Y(g): return 140 - g * 1.15    # o'tkazuvchanlik 0..110
    pts = [(0, 100), (15, 72), (30, 44), (45, 16), (50, 8), (55, 16), (70, 40), (85, 62), (100, 82)]
    path = "M" + " L".join(f"{X(v):.0f},{Y(g):.0f}" for v, g in pts)
    return ('<svg width="234" height="158" viewBox="0 0 240 158">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{RD}}}'
            f'.dsh{{stroke:{R2};stroke-width:1;stroke-dasharray:3,3}}</style>'
            f'<rect x="38" y="4" width="196" height="136" rx="5" fill="{RP}" stroke="{RD}" stroke-width="1.2"/>'
            + "".join(f'<line x1="40" y1="{Y(g):.0f}" x2="230" y2="{Y(g):.0f}" stroke="{RG}" stroke-width="0.9"/>'
                      for g in [25, 50, 75, 100]) +
            f'<line x1="{X(50)}" y1="{Y(8)}" x2="{X(50)}" y2="140" class="dsh"/>'
            f'<circle cx="{X(50)}" cy="{Y(8)}" r="3.4" fill="{R2}" stroke="#fff" stroke-width="1.2"/>'
            f'<text x="{X(50)+6}" y="{Y(8)+3}" class="lb" font-weight="bold" fill="{R2}">M</text>'
            f'<path d="{path}" fill="none" stroke="{R1}" stroke-width="2.6" stroke-linejoin="round"/>'
            f'<line x1="38" y1="140" x2="236" y2="140" stroke="{RD}" stroke-width="1.5"/>'
            f'<polygon points="238,140 231,137 231,143" fill="{RD}"/>'
            f'<line x1="38" y1="140" x2="38" y2="4" stroke="{RD}" stroke-width="1.5"/>'
            f'<polygon points="38,2 35,9 41,9" fill="{RD}"/>'
            '<text x="120" y="153" class="lb">V(Ba(OH)₂ qo\'shildi) →</text>'
            '<text x="6" y="14" class="lb">tok</text>'
            f'<text x="150" y="26" class="lb">H₂SO₄ + Ba(OH)₂</text>'
            '</svg>')

def fig_ph_bars():
    """A: kundalik moddalarning pH ustunlari (rangli gradiyent)."""
    data = [("limon", 2, "#d32f2f"), ("sirka", 3, "#e5715a"), ("sut", 6.5, "#c8b64b"),
            ("suv", 7, "#5aa45a"), ("sovun", 10, "#3f6fb5")]
    bars = ""
    for i, (lab, v, col) in enumerate(data):
        x = 52 + i * 38; h = v * 8.6; y = 128 - h
        vv = str(v).replace(".", ",")
        bars += (f'<rect x="{x}" y="{y:.0f}" width="24" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{RD}" stroke-width="0.9"/>'
                 f'<text x="{x+12}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{vv}</text>'
                 f'<text x="{x+12}" y="141" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="150" viewBox="0 0 250 150">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{RD}}}</style>'
            f'<rect x="40" y="4" width="204" height="124" rx="4" fill="{RP}" stroke="#ecc7da" stroke-width="1.1"/>'
            + "".join(f'<line x1="42" y1="{128-g*8.6:.0f}" x2="242" y2="{128-g*8.6:.0f}" stroke="{RG}" stroke-width="0.9"/>'
                      f'<text x="28" y="{131-g*8.6:.0f}" class="lb">{g}</text>' for g in [7, 14])
            + f'<line x1="42" y1="{128-7*8.6:.0f}" x2="242" y2="{128-7*8.6:.0f}" stroke="#5aa45a" stroke-width="1.2" stroke-dasharray="5,3"/>'
            + bars +
            f'<line x1="40" y1="128" x2="244" y2="128" stroke="{RD}" stroke-width="1.5"/>'
            '<text x="6" y="14" class="lb">pH</text>'
            '<text x="200" y="66" class="lb" fill="#5aa45a">neytral</text></svg>')

def fig_ph_scale():
    """pH shkalasi: 0-14 rangli lenta, A (pH=11) belgisi."""
    stops = ["#c62828", "#e5533c", "#ef8a3c", "#f4c542", "#c3d24b", "#7cb95a", "#43a047",
             "#4a9d8f", "#3f8ac2", "#3f6fb5", "#4a5cae", "#5e4b9e", "#6d3f96", "#7a338c", "#822b85"]
    cells = "".join(f'<rect x="{16+i*15}" y="34" width="15" height="18" fill="{stops[i]}"/>' for i in range(15))
    nums = "".join(f'<text x="{23+i*15}" y="66" text-anchor="middle" class="lb">{i}</text>' for i in range(0, 15, 2))
    return ('<svg width="250" height="96" viewBox="0 0 250 96">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{RD}}}</style>'
            + cells + nums +
            f'<rect x="16" y="34" width="225" height="18" fill="none" stroke="{RD}" stroke-width="1.2"/>'
            '<text x="16" y="82" class="lb" font-weight="bold">← kislotali</text>'
            '<text x="106" y="82" class="lb">neytral (7)</text>'
            '<text x="186" y="82" class="lb" font-weight="bold">ishqoriy →</text></svg>')

def fig_soap():
    """Sovun va ko'pik."""
    bubbles = "".join(f'<circle cx="{150+(i*23)%70}" cy="{28+(i*17)%42}" r="{5+(i%3)*3}" '
                      f'fill="none" stroke="{R2}" stroke-width="1.3" opacity="0.7"/>' for i in range(9))
    return ('<svg width="240" height="122" viewBox="0 0 240 122">'
            f'<style>.lb{{font-size:9px;font-family:Georgia,serif;fill:{RD}}}</style>'
            f'<rect x="30" y="48" width="86" height="40" rx="12" fill="{R1}" opacity="0.8" stroke="{RD}" stroke-width="1.6"/>'
            '<ellipse cx="73" cy="48" rx="43" ry="9" fill="#e879a8" stroke="#6d1b45" stroke-width="1.2"/>'
            '<text x="52" y="72" class="lb" fill="#fff" font-weight="bold">SOVUN</text>'
            + bubbles +
            "<text x='146' y='90' class='lb'>ko'pik sirg'anadi</text>"
            '<text x="30" y="112" class="lb" font-weight="bold">universal indikator: ko\'k (pH ≈ 10)</text></svg>')

def fig_flower():
    """Gidrangeya: kislotali tuproqda ko'k, ishqoriyda pushti."""
    def bloom(cx, col1, col2):
        import math
        pet = ""
        for i in range(8):
            a = i * 45 * math.pi / 180
            px, py = cx + 14 * math.cos(a), 44 + 14 * math.sin(a)
            pet += f'<circle cx="{px:.0f}" cy="{py:.0f}" r="9" fill="{col1}" stroke="{col2}" stroke-width="1"/>'
        pet += f'<circle cx="{cx}" cy="44" r="8" fill="{col2}"/>'
        return pet
    return ('<svg width="250" height="128" viewBox="0 0 250 128">'
            f'<style>.lb{{font-size:9px;font-family:Georgia,serif;fill:{RD}}}</style>'
            + bloom(66, "#7fa8d9", "#3f6fb5")
            + '<rect x="62" y="64" width="7" height="30" fill="#4c8a4c"/>'
            '<rect x="30" y="94" width="72" height="14" rx="3" fill="#7a5230"/>'
            '<text x="34" y="122" class="lb" font-weight="bold">kislotali tuproq → ko\'k</text>'
            + bloom(184, "#eb9ec1", "#c2185b")
            + '<rect x="180" y="64" width="7" height="30" fill="#4c8a4c"/>'
            '<rect x="148" y="94" width="72" height="14" rx="3" fill="#a8865e"/>'
            '<text x="148" y="122" class="lb" font-weight="bold">ishqoriy tuproq → pushti</text></svg>')

def fig_stomach():
    """Oshqozon konturi + antatsid tabletka."""
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            f'<style>.lb{{font-size:9px;font-family:Georgia,serif;fill:{RD}}}</style>'
            '<path d="M96,16 q-4,22 12,34 q22,16 20,38 q-2,22 -26,24 q-26,2 -34,-18 q-6,-16 6,-26" '
            f'fill="#f4b8cd" stroke="{R1}" stroke-width="2.2"/>'
            '<path d="M80,86 q14,10 30,4" stroke="#fff" stroke-width="1.6" fill="none"/>'
            f'<text x="60" y="52" class="lb" font-weight="bold">HCl · pH ≈ 1–2</text>'
            # tabletka
            f'<circle cx="176" cy="36" r="13" fill="#fff" stroke="{R2}" stroke-width="2"/>'
            f'<line x1="167" y1="36" x2="185" y2="36" stroke="{R2}" stroke-width="1.6"/>'
            '<text x="152" y="62" class="lb">antatsid</text>'
            f'<path d="M172,50 q-14,14 -34,16" stroke="{R2}" stroke-width="1.4" fill="none" stroke-dasharray="4,3"/>'
            f'<polygon points="136,68 144,64 142,72" fill="{R2}"/>'
            '<text x="44" y="120" class="lb" font-weight="bold">Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O</text></svg>')

def fig_pool():
    """Basseyn: suv, zinapoya, pH testeri."""
    waves = "".join(f'<path d="M{34+i*44},64 q11,-6 22,0 q11,6 22,0" stroke="#5aa5c9" stroke-width="1.6" fill="none"/>'
                    for i in range(4))
    return ('<svg width="250" height="120" viewBox="0 0 250 120">'
            f'<style>.lb{{font-size:9px;font-family:Georgia,serif;fill:{RD}}}</style>'
            '<rect x="26" y="56" width="198" height="44" rx="6" fill="#bfe3f2" stroke="#5aa5c9" stroke-width="2"/>'
            + waves +
            '<rect x="196" y="34" width="6" height="42" fill="#8a9aa5"/><rect x="184" y="40" width="18" height="4" fill="#8a9aa5"/>'
            '<rect x="184" y="52" width="18" height="4" fill="#8a9aa5"/>'
            # pH testeri
            f'<rect x="46" y="18" width="52 " height="26" rx="4" fill="#fff" stroke="{R1}" stroke-width="1.6"/>'
            f'<text x="52" y="36" class="lb" font-weight="bold" fill="{R1}">pH 7,4</text>'
            f'<path d="M72,44 v10" stroke="{R1}" stroke-width="1.4" stroke-dasharray="3,2"/>'
            '<text x="60" y="114" class="lb" font-weight="bold">basseyn suvi: pH 7,2–7,6 nazoratda</text></svg>')


def fig_burette():
    """Titrlash: shtativdagi byuretka + konussimon kolba (pushti-qizil)."""
    return ('<svg width="200" height="150" viewBox="0 0 200 150">'
            '<style>.lb{font-size:8.6px;font-family:Georgia,serif;fill:#6d1b45}</style>'
            '<rect x="30" y="8" width="6" height="132" fill="#8a9aa5"/>'
            '<rect x="18" y="138" width="70" height="6" rx="2" fill="#8a9aa5"/>'
            '<line x1="36" y1="30" x2="66" y2="30" stroke="#8a9aa5" stroke-width="4"/>'
            '<rect x="64" y="10" width="10" height="74" rx="3" fill="#fdf5f8" stroke="#6d1b45" stroke-width="1.6"/>'
            '<rect x="66" y="12" width="6" height="40" fill="#c9dff0"/>'
            + "".join(f'<line x1="64" y1="{18+i*10}" x2="68" y2="{18+i*10}" stroke="#6d1b45" stroke-width="0.8"/>' for i in range(7))
            + '<polygon points="66,84 72,84 69,94" fill="#fdf5f8" stroke="#6d1b45" stroke-width="1.2"/>'
            '<circle cx="69" cy="100" r="1.6" fill="#c9dff0"/>'
            '<path d="M56,132 l13,-26 l13,26 q-13,8 -26,0 z" fill="#fdf5f8" stroke="#c2185b" stroke-width="1.8"/>'
            '<path d="M60,128 q9,5 18,0 l-4,-9 q-5,3 -10,0 z" fill="#f4b8cd" opacity="0.8"/>'
            '<text x="92" y="24" class="lb" font-weight="bold">byuretka: NaOH</text>'
            '<text x="92" y="120" class="lb" font-weight="bold">kolba: HCl +</text>'
            '<text x="92" y="132" class="lb">indikator</text></svg>')

FIGS = dict(cond_curve=fig_cond_curve, burette=fig_burette, ph_bars=fig_ph_bars, ph_scale=fig_ph_scale,
            soap=fig_soap, flower=fig_flower, stomach=fig_stomach, pool=fig_pool)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #ecc7da; border-radius:2pt;
                  background:#fdf5f8; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>8-bob — Elektrolitik dissotsiatsiya va pH</title><style>{css}</style>"]

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
  <div class="chapnum">8</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 8-bob · Mavzu pasporti (I.8)</div>
  <h1>Elektrolitik dissotsiatsiya va pH</h1>
  <div class="lead">kuchli va kuchsiz elektrolitlar · dissotsiatsiya darajasi · ion almashinish
  reaksiyalari · vodorod ko'rsatkichi (pH) va indikatorlar</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>dissotsiatsiya tenglamalari va ionlar sonini hisoblash</li>
      <li>pH ↔ [H⁺] ↔ [OH⁻] o'tishlari (Kw = 10⁻¹⁴)</li>
      <li>molekulyar / to'liq ion / qisqa ion tenglamalar</li>
      <li>aralashtirish va suyultirishda pH hisobi</li>
      <li>tuz eritmalarining muhiti (soda — ishqoriy)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>o'tkazuvchanlik U-egri chizig'i (B: 5, 32)</li>
      <li>pH shkalasi va ustunli diagramma (A: 26, 32; B: 28)</li>
      <li>lampochka/indikator jadvallari (A: 17; B: 14, 17)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>pH bilan [H⁺] ni tenglashtirib yuborish</li>
      <li>kuchsiz elektrolitni ion holida yozish</li>
      <li>«pH birligi = 10 barobar» ekanini unutish</li>
      <li>ion soni hisobida indekslarni tushirib qoldirish</li></ul></div>
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
