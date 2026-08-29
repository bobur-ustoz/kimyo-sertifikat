# -*- coding: utf-8 -*-
"""10-bob (Elektroliz) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I10A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I10B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="#b7950b" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.10 figuralari ----------
def _bath(x, w, liq, label):
    return (f'<rect x="{x}" y="52" width="{w}" height="48" rx="3" fill="{liq}"/>'
            f'<path d="M{x},44 V100 h{w} V44" fill="none" stroke="#556" stroke-width="1.8"/>'
            f'<text x="{x+w/2:.0f}" y="116" text-anchor="middle" class="lb" font-weight="bold">{label}</text>')

def fig_jewelry():
    """Zargarlik: kumushlash vannasi — uzuk katodda."""
    return ('<svg width="250" height="126" viewBox="0 0 250 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # manba
            '<rect x="96" y="6" width="58" height="16" rx="3" fill="#eef4f8" stroke="#556" stroke-width="1.2"/>'
            '<text x="104" y="18" class="lb" font-weight="bold">— manba +</text>'
            + _bath(50, 150, "#e8f0fe", "AgNO₃ eritmasi")
            # katod (uzuk)
            + '<line x1="102" y1="22" x2="86" y2="60" stroke="#556" stroke-width="1.6"/>'
            '<circle cx="86" cy="72" r="11" fill="none" stroke="#c9a227" stroke-width="4"/>'
            '<text x="60" y="44" class="lb" font-weight="bold">uzuk (−)</text>'
            # anod (Ag plastinka)
            '<line x1="148" y1="22" x2="166" y2="56" stroke="#556" stroke-width="1.6"/>'
            '<rect x="160" y="56" width="10" height="36" fill="#d9dfe3" stroke="#8a9aa5" stroke-width="1.2"/>'
            '<text x="176" y="48" class="lb" font-weight="bold">Ag (+)</text>'
            '<text x="96" y="94" class="lb">Ag⁺ →</text>'
            '</svg>')

def fig_aluminum():
    """Alyuminiy zavodi: elektroliz vannasi suyuqlanma bilan."""
    return ('<svg width="260" height="126" viewBox="0 0 260 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # vanna
            '<rect x="40" y="50" width="180" height="52" rx="4" fill="#f5b041"/>'
            '<rect x="40" y="88" width="180" height="14" fill="#e67e22"/>'
            '<path d="M36,42 V106 h188 V42" fill="none" stroke="#4d5656" stroke-width="2.4"/>'
            # uglerod anodlar
            "".join(f'<rect x="{68+i*44}" y="18" width="14" height="44" fill="#2c3e50"/>' for i in range(3)) +
            '<line x1="60" y1="14" x2="200" y2="14" stroke="#556" stroke-width="2"/>'
            '<text x="206" y="18" class="lb" font-weight="bold">+</text>'
            '<text x="44" y="120" class="lb" font-weight="bold">Al₂O₃ suyuqlanmasi (kriolitda, ~950 °C)</text>'
            '<text x="120" y="99" class="lb" fill="#fff" font-weight="bold">suyuq Al (katod −)</text>'
            '<text x="228" y="80" class="lb">CO₂↑</text>'
            '</svg>')

def fig_carbattery():
    """Avtomobil akkumulyatori zaryadda."""
    return ('<svg width="240" height="120" viewBox="0 0 240 120">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            '<rect x="40" y="40" width="120" height="60" rx="6" fill="#2c3e50" stroke="#1b2631" stroke-width="2"/>'
            '<rect x="56" y="30" width="14" height="10" fill="#c0392b"/><rect x="130" y="30" width="14" height="10" fill="#2471a3"/>'
            '<text x="56" y="26" class="lb" font-weight="bold">+</text><text x="134" y="26" class="lb" font-weight="bold">−</text>'
            '<text x="62" y="76" class="lb" fill="#fff" font-weight="bold">12 V · Pb / PbO₂ / H₂SO₄</text>'
            # zaryadlovchi
            '<rect x="186" y="34" width="44" height="30" rx="4" fill="#eef4f8" stroke="#556" stroke-width="1.4"/>'
            '<text x="192" y="52" class="lb" font-weight="bold">zaryad</text>'
            '<path d="M186,42 h-16 q-8,0 -8,-6 v-2" fill="none" stroke="#c0392b" stroke-width="2.4"/>'
            '<path d="M186,56 q-30,10 -42,-14" fill="none" stroke="#2471a3" stroke-width="2.4"/>'
            '<text x="52" y="114" class="lb" font-weight="bold">zaryadlanish = elektroliz (majburiy OQR)</text>'
            '</svg>')

def fig_hoffman():
    """Hoffman apparati: ikki naycha, H2 (2V) va O2 (1V)."""
    def tube(x, gas_h, label, sub):
        return (f'<rect x="{x}" y="14" width="26" height="88" rx="6" fill="#dcebf5" stroke="#5b8bab" stroke-width="1.8"/>'
                f'<rect x="{x+2}" y="16" width="22" height="{gas_h}" rx="4" fill="#f7fbfe"/>'
                f'<line x1="{x}" y1="{16+gas_h}" x2="{x+26}" y2="{16+gas_h}" stroke="#5b8bab" stroke-width="1.2" stroke-dasharray="3,2"/>'
                f'<text x="{x+13}" y="{30}" text-anchor="middle" class="lb" font-weight="bold">{label}</text>'
                f'<text x="{x+13}" y="120" text-anchor="middle" class="lb">{sub}</text>')
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # asos idish
            '<path d="M60,102 h110" stroke="#5b8bab" stroke-width="10"/>'
            + tube(60, 48, "H₂", "katod (−)")
            + tube(144, 24, "O₂", "anod (+)")
            + '<circle cx="115" cy="30" r="12" fill="none" stroke="#5b8bab" stroke-width="1.8"/>'
            '<line x1="103" y1="30" x2="86" y2="30" stroke="#5b8bab" stroke-width="1.8"/>'
            '<line x1="127" y1="30" x2="144" y2="30" stroke="#5b8bab" stroke-width="1.8"/>'
            '<text x="106" y="34" class="lb">suv</text>'
            '<text x="58" y="12" class="lb" font-weight="bold">V(H₂) : V(O₂) = 2 : 1</text>'
            '</svg>')

def fig_mt_graph():
    """B-variant: m(Ag) ~ Q(F) grafigi."""
    def X(f): return 38 + f * 480      # F 0..0,4
    def Y(m): return 138 - m * 2.8     # m 0..45
    pts = [(0, 0), (0.1, 10.8), (0.2, 21.6), (0.3, 32.4), (0.4, 43.2)]
    path = "M" + " L".join(f"{X(f):.0f},{Y(m):.0f}" for f, m in pts)
    grid = "".join(f'<line x1="{X(f)}" y1="8" x2="{X(f)}" y2="138" class="gr"/>' for f in [0.1, 0.2, 0.3, 0.4]) + \
           "".join(f'<line x1="38" y1="{Y(m):.0f}" x2="230" y2="{Y(m):.0f}" class="gr"/>' for m in [10.8, 21.6, 32.4, 43.2])
    xt = "".join(f'<text x="{X(f)-8}" y="150" class="lb">{f:.1f}</text>'.replace(".", ",") for f in [0.1, 0.2, 0.3, 0.4])
    yt = "".join(f'<text x="8" y="{Y(m)+3:.0f}" class="lb">{m}</text>'.replace(".", ",") for m in [10.8, 21.6, 32.4, 43.2])
    guides = (f'<line x1="{X(0.2)}" y1="{Y(21.6)}" x2="{X(0.2)}" y2="138" class="dsh"/>'
              f'<line x1="38" y1="{Y(21.6)}" x2="{X(0.2)}" y2="{Y(21.6)}" class="dsh"/>'
              f'<circle cx="{X(0.2)}" cy="{Y(21.6)}" r="2.6" fill="{ACCENT}"/>'
              f'<circle cx="{X(0.3)}" cy="{Y(32.4)}" r="2.6" fill="{ACCENT}"/>')
    S1, S2 = "#b7950b", "#34495e"
    grid_h = "".join(f'<line x1="38" y1="{Y(m):.0f}" x2="230" y2="{Y(m):.0f}" stroke="#d6dbdf" stroke-width="0.9"/>'
                     for m in [10.8, 21.6, 32.4, 43.2])
    tick_x = "".join(f'<line x1="{X(f)}" y1="138" x2="{X(f)}" y2="142" stroke="{S2}" stroke-width="1.2"/>'
                     for f in [0.1, 0.2, 0.3, 0.4])
    mk = "".join(f'<polygon points="{X(f):.0f},{Y(m)-4:.0f} {X(f)-4:.0f},{Y(m)+3:.0f} {X(f)+4:.0f},{Y(m)+3:.0f}" '
                 f'fill="{S1}" stroke="{S2}" stroke-width="0.9"/>' for f, m in pts if f > 0)
    return ('<svg width="234" height="158" viewBox="0 0 240 158">'
            '<style>.ax{stroke:#34495e;stroke-width:1.6}'
            '.lb{font-size:8.6px;font-family:Georgia,serif;fill:#34495e}.dsh{stroke:#b7950b;stroke-width:1;stroke-dasharray:4,2}</style>'
            '<rect x="38" y="4" width="192" height="134" fill="#fcfbf4"/>'
            '<rect x="38" y="4" width="192" height="10" fill="#34495e" opacity="0.12"/>'
            f'{grid_h}{tick_x}'
            '<line x1="38" y1="138" x2="236" y2="138" class="ax"/><polygon points="236,138 229,135 229,141" fill="#34495e"/>'
            '<line x1="38" y1="138" x2="38" y2="4" class="ax"/><polygon points="38,4 35,11 41,11" fill="#34495e"/>'
            f'{xt}{yt}{guides}'
            '<text x="196" y="134" class="lb">Q, F</text><text x="42" y="12" class="lb">m(Ag), g</text>'
            f'<path d="{path}" fill="none" stroke="{S1}" stroke-width="2.6"/>'
            f'{mk}'
            f'<text x="52" y="26" class="lb" font-weight="bold">▲ katoddagi kumush</text>'
            '</svg>')

def fig_cell():
    """Elektrolizyor sxemasi: manba, 1(−) va 2(+) elektrodlar."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            '<rect x="86" y="6" width="60" height="16" rx="3" fill="#eef4f8" stroke="#556" stroke-width="1.2"/>'
            '<text x="94" y="18" class="lb" font-weight="bold">−  manba  +</text>'
            + _bath(46, 140, "#e8f0fe", "elektrolit eritmasi")
            + '<line x1="94" y1="22" x2="80" y2="56" stroke="#556" stroke-width="1.6"/>'
            '<rect x="74" y="56" width="10" height="38" fill="#b0bec5" stroke="#546e7a" stroke-width="1.2"/>'
            '<text x="62" y="50" class="lb" font-weight="bold">1</text>'
            '<line x1="138" y1="22" x2="152" y2="56" stroke="#556" stroke-width="1.6"/>'
            '<rect x="148" y="56" width="10" height="38" fill="#b0bec5" stroke="#546e7a" stroke-width="1.2"/>'
            '<text x="164" y="50" class="lb" font-weight="bold">2</text>'
            '</svg>')

FIGS = dict(jewelry=fig_jewelry, aluminum=fig_aluminum, carbattery=fig_carbattery,
            hoffman=fig_hoffman, mt_graph=fig_mt_graph, cell=fig_cell)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #d9ce9a; border-radius:2pt;
                  background:#fcfbf4; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>10-bob — Elektroliz</title><style>{css}</style>"]

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
  <div class="chapnum">10</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 10-bob · Mavzu pasporti (I.10)</div>
  <h1>Elektroliz</h1>
  <div class="lead">eritma va suyuqlanma elektrolizi · katod-anod jarayonlari · Faradey qonuni ·
  galvanostegiya va rafinlash · sanoat qo'llanilishlari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>eritma/suyuqlanma mahsulotlarini aniqlash</li>
      <li>Faradey hisoblari: m, V, Q, t</li>
      <li>ikki bosqichli katod (Cu²⁺ tugagach H₂)</li>
      <li>teskari (X %, necha F) masalalar</li>
      <li>rafinlash, galvanostegiya, ketma-ket vannalar</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>m–Q grafigi bilan ishlash (B: 5, 27)</li>
      <li>elektrolizyor sxemasini o'qish (B: 28; A: 4, 18)</li>
      <li>mahsulotlar jadvali (A: 17; B: 17; O2-43)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>eritmada aktiv metall ajraladi deb o'ylash</li>
      <li>elektron sonini (n) unutib M ni to'g'ridan olish</li>
      <li>anodda sulfat/nitrat oksidlanadi deb olish</li>
      <li>katod-anod qutblarini chalkashtirish</li></ul></div>
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
