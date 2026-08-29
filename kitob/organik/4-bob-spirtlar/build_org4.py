# -*- coding: utf-8 -*-
"""Organik 4-bob (Spirtlar va fenollar) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_III4A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_III4B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#00838f", "#005662", "#e9f5f6", "#d81b60"

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
            f'{km}<path d="{p}" fill="none" stroke="#00838f" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- III.4 figuralari (feruza + pushti palitrasi) ----------
I1, I2, ID, IP, IG = "#00838f", "#d81b60", "#00494f", "#e9f5f6", "#c2dfe2"

def fig_bp_spirt():
    """Spirtlar qaynash haroratlari — chiziqli grafik (berilgan ma'lumot)."""
    data = [("CH₃OH", 65), ("C₂H₅OH", 78), ("C₃H₇OH", 97), ("C₄H₉OH", 117)]
    lo, hi = 50, 130
    pts = []; marks = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 56; y = 118 - (v - lo) / (hi - lo) * 100
        pts.append(f"{x},{y:.0f}")
        marks += (f'<circle cx="{x}" cy="{y:.0f}" r="3.4" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
                  f'<text x="{x}" y="{y-7:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}°</text>'
                  f'<text x="{x}" y="136" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="40" y="4" width="224" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{I1}" stroke-width="2.2"/>'
            + marks +
            f'<line x1="40" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">t qayn, °C</text>'
            '<text x="86" y="147" class="lb">zanjir uzunligi ortishi →</text></svg>')

def fig_bar_antiseptic():
    """Spirt konsentratsiyasi va antiseptik samaradorlik — ustunlar (berilgan ma'lumot)."""
    data = [("40 %", 55), ("70 %", 90), ("96 %", 65)]
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 64 + i * 66; h = v / 100 * 104; y = 122 - h
        col = I2 if i == 1 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="38" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+19}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+19}" y="135" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="270" height="148" viewBox="0 0 270 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="218" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{122-g/100*104:.0f}" x2="262" y2="{122-g/100*104:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="30" y="{125-g/100*104:.0f}" class="lb">{g}</text>' for g in [25, 50, 75])
            + bars +
            f'<line x1="46" y1="122" x2="264" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">samara, shartli birlik</text></svg>')

def fig_dehydro():
    """B: laboratoriya degidratatsiyasi — kolba + H2SO4, gaz naychasi, suv ustida yig'ish."""
    return ('<svg width="280" height="140" viewBox="0 0 280 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # kolba
            f'<path d="M56,26 v26 l-20,34 a8,8 0 0 0 7,12 h44 a8,8 0 0 0 7,-12 l-20,-34 v-26" '
            f'fill="none" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M42,88 a30,16 0 0 0 46,0 l-12,-20 h-22 z" fill="{I1}" opacity="0.30"/>'
            '<text x="65" y="84" text-anchor="middle" class="lb" font-weight="bold">C₂H₅OH +</text>'
            '<text x="65" y="94" text-anchor="middle" class="lb" font-weight="bold">H₂SO₄</text>'
            # gorelka
            f'<path d="M58,112 q7,-10 14,0 q-7,6 -14,0z" fill="{I2}"/>'
            f'<rect x="56" y="116" width="18" height="8" rx="2" fill="#8d99a6"/>'
            '<text x="86" y="122" class="lb">t &gt; 170 °C</text>'
            # naycha
            f'<path d="M65,26 v-10 h96 v52" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            # kristallizator + probirka
            f'<path d="M138,110 h84 v14 a6,6 0 0 1 -6,6 h-72 a6,6 0 0 1 -6,-6 z" fill="{I1}" opacity="0.25" '
            f'stroke="{ID}" stroke-width="1.4"/>'
            f'<rect x="152" y="52" width="20" height="66" rx="6" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="154" y="88" width="16" height="28" fill="{I1}" opacity="0.35"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="none" stroke="{I2}" stroke-width="1"/>'
                      for x, y in [(160, 80), (166, 70), (161, 60)])
            + f'<text x="182" y="66" class="lb" font-weight="bold" fill="{I2}">C₂H₄</text>'
            '<text x="182" y="78" class="lb">suv ustida</text>'
            '<text x="182" y="90" class="lb">yig\'iladi</text>'
            '<text x="30" y="12" class="lb" font-weight="bold">etanolni degidratatsiyalash</text></svg>')

def fig_scheme38():
    """B O1-38: etanol → etilen sxemasi."""
    return ('<svg width="280" height="76" viewBox="0 0 280 76">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="22" width="92" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="54" y="38" text-anchor="middle" class="lb" font-weight="bold">9,2 g C₂H₅OH</text>'
            '<text x="54" y="50" text-anchor="middle" class="lb">etanol</text>'
            f'<line x1="100" y1="39" x2="140" y2="39" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="144,39 136,35 136,43" fill="{I2}"/>'
            f'<text x="102" y="20" class="lb" fill="{I2}">H₂SO₄ (kons.),</text>'
            f'<text x="102" y="31" class="lb" fill="{I2}">t&gt;170 °C, −H₂O</text>'
            f'<rect x="146" y="22" width="80" height="34" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="186" y="38" text-anchor="middle" class="lb" font-weight="bold">C₂H₄</text>'
            '<text x="186" y="50" text-anchor="middle" class="lb">? L (n.sh.)</text>'
            f'<line x1="226" y1="39" x2="250" y2="39" stroke="{ID}" stroke-width="1.4"/>'
            '<text x="254" y="43" class="lb">etilen</text></svg>')

def fig_sanitizer():
    """A: qo'l antiseptigi — flakon va tomchi."""
    return ('<svg width="220" height="120" viewBox="0 0 220 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="52" y="34" width="40" height="62" rx="6" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="62" y="20" width="20" height="14" rx="2" fill="{I1}"/>'
            f'<rect x="70" y="10" width="14" height="8" rx="2" fill="{I1}"/>'
            f'<rect x="58" y="52" width="28" height="30" rx="3" fill="#fff" stroke="{IG}"/>'
            '<text x="72" y="64" text-anchor="middle" class="lb" font-weight="bold">70 %</text>'
            '<text x="72" y="76" text-anchor="middle" class="lb">etanol</text>'
            f'<path d="M104,34 q6,10 0,14 q-6,-4 0,-14z" fill="{I1}" opacity="0.7"/>'
            f'<path d="M120,58 q16,-10 34,0 q10,6 8,16 q-24,10 -44,-2 q-4,-8 2,-14z" '
            f'fill="#f7d9c4" stroke="#c9a084" stroke-width="1.2"/>'
            '<text x="120" y="98" class="lb">mikroblarga qarshi</text>'
            '<text x="46" y="114" class="lb" font-weight="bold">qo\'l antiseptigi</text></svg>')

def fig_antifreeze():
    """A: antifriz kanistri va radiator."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M46,34 h34 l10,10 v50 a4,4 0 0 1 -4,4 h-40 a4,4 0 0 1 -4,-4 v-56 a4,4 0 0 1 4,-4z" '
            f'fill="{I1}" opacity="0.28" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="52" y="24" width="14" height="10" rx="2" fill="{ID}"/>'
            '<text x="64" y="66" text-anchor="middle" class="lb" font-weight="bold">antifriz</text>'
            '<text x="64" y="78" text-anchor="middle" class="lb">C₂H₄(OH)₂</text>'
            f'<rect x="124" y="44" width="60" height="44" rx="4" fill="{IP}" stroke="{ID}" stroke-width="1.5"/>'
            + "".join(f'<line x1="{130+i*8}" y1="48" x2="{130+i*8}" y2="84" stroke="{IG}" stroke-width="2"/>'
                      for i in range(7))
            + f'<text x="154" y="100" text-anchor="middle" class="lb">radiator</text>'
            f'<path d="M196,30 l0,16 m-8,-8 l16,0 m-13,-6 l10,12 m0,-12 l-10,12" stroke="{I2}" '
            'stroke-width="1.6" fill="none"/>'
            '<text x="182" y="60" class="lb" fill="' + I2 + '">−40 °C</text>'
            '<text x="42" y="114" class="lb" font-weight="bold">qishda muzlamaydi</text></svg>')

def fig_cream():
    """A: glitserinli krem bankasi va tomchi-namlik."""
    return ('<svg width="220" height="116" viewBox="0 0 220 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="52" y="46" width="56" height="44" rx="8" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="48" y="34" width="64" height="14" rx="5" fill="{I2}" opacity="0.75"/>'
            '<text x="80" y="66" text-anchor="middle" class="lb" font-weight="bold">KREM</text>'
            '<text x="80" y="78" text-anchor="middle" class="lb">glitserinli</text>'
            + "".join(f'<path d="M{x},{y} q5,8 0,11 q-5,-3 0,-11z" fill="{I1}" opacity="0.7"/>'
                      for x, y in [(134, 44), (148, 60), (138, 78)])
            + '<text x="158" y="52" class="lb">namlikni</text>'
            '<text x="158" y="64" class="lb">ushlab</text>'
            '<text x="158" y="76" class="lb">turadi</text>'
            '<text x="48" y="110" class="lb" font-weight="bold">C₃H₅(OH)₃ — namlovchi</text></svg>')

def fig_warning():
    """A: metanol xavfi yorlig'i."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M74,16 l40,70 h-80 z" fill="#fff3cd" stroke="{I2}" stroke-width="2.4" '
            'stroke-linejoin="round"/>'
            f'<circle cx="74" cy="52" r="7" fill="none" stroke="{I2}" stroke-width="2"/>'
            f'<circle cx="71" cy="50" r="1.4" fill="{I2}"/><circle cx="77" cy="50" r="1.4" fill="{I2}"/>'
            f'<path d="M70,56 q4,3 8,0" stroke="{I2}" stroke-width="1.4" fill="none"/>'
            f'<path d="M64,64 l-6,8 m32,-8 l6,8" stroke="{I2}" stroke-width="1.8"/>'
            '<text x="74" y="80" text-anchor="middle" class="lb" font-weight="bold" fill="' + I2 + '">CH₃OH</text>'
            '<text x="130" y="40" class="lb" font-weight="bold">metanol — kuchli zahar!</text>'
            '<text x="130" y="54" class="lb">ozgina miqdori ham</text>'
            '<text x="130" y="66" class="lb">ko\'rlik va o\'limga</text>'
            '<text x="130" y="78" class="lb">olib keladi</text>'
            '<text x="52" y="112" class="lb" font-weight="bold">yorliqni doim o\'qing</text></svg>')

FIGS = dict(bp_spirt=fig_bp_spirt, bar_antiseptic=fig_bar_antiseptic, dehydro=fig_dehydro,
            scheme38=fig_scheme38, sanitizer=fig_sanitizer, antifreeze=fig_antifreeze,
            cream=fig_cream, warning=fig_warning)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bfe0e3; border-radius:2pt;
                  background:#e9f5f6; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>Organik 4-bob — Spirtlar va fenollar</title><style>{css}</style>"]

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
  <div class="chapnum">4</div>
  <div class="kicker">2-kitob · Organik kimyo · 4-bob · Mavzu pasporti (III.4)</div>
  <h1>Spirtlar va fenollar</h1>
  <div class="lead">OH funksional guruhi · bir va ko'p atomli spirtlar · vodorod bog'i ·
  degidratatsiya va oksidlanish · fenol kislotaliligi va sifat sinovlari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>izomeriya va nomenklatura (B: 1, 2, 20, 24, 43)</li>
      <li>Na, NaOH, Br&#8322; bilan reaksiya hisoblari (B: 10, 12, 13, 29, 31)</li>
      <li>degidratatsiya va CuO oksidlanishi (B: 4, 8, 19, 28, 38)</li>
      <li>teskari masalalar — M topish (B: 6, 26, 43)</li>
      <li>sifat sinovlari: Cu(OH)&#8322;, FeCl&#8323;, bromli suv (B: 7, 30, 33–35)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>qaynash haroratlari grafigi (A: 28)</li>
      <li>antiseptik samaradorlik diagrammasi (A: 26, 32)</li>
      <li>degidratatsiya tajribasi (B: 4, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>fenolni «oddiy spirt» deb o'qish</li>
      <li>Na bilan reaksiyada H&#8322; koeffitsiyentini unutish</li>
      <li>ko'p atomli spirtda OH sonini hisobga olmaslik</li>
      <li>140 °C va 170 °C mahsulotlarini chalkashtirish</li></ul></div>
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
