# -*- coding: utf-8 -*-
"""12-bob (Sinflarning xossalari va olinishi) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_II2A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_II2B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#6d4c41", "#4e342e", "#f7f2ef", "#2e7d32"

SVG_CURVES = {
    "rise":      ("M22,82 C55,68 95,40 126,22", None),
    "flat":      ("M22,44 L126,44", None),
    "fall":      ("M22,22 C55,36 95,64 126,82", None),
    "rise_flat": ("M22,82 L70,34 L126,34", (70, 34)),
    "fall_flat": ("M22,26 L70,70 L126,70", (70, 70)),
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
            f'{km}<path d="{p}" fill="none" stroke="#6d4c41" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- II.2 figuralari (qahva-jigarrang palitrasi) ----------
I1, I2, ID, IP, IG = "#6d4c41", "#2e7d32", "#4e342e", "#f7f2ef", "#e2d5cd"

def fig_kipp():
    """Kipp apparati: uch shar, marmar, kislota, jo'mrak."""
    return ('<svg width="250" height="160" viewBox="0 0 250 160">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # yuqori shar (kislota zaxirasi)
            f'<circle cx="90" cy="34" r="22" fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            f'<rect x="86" y="6" width="8" height="10" fill="{IP}" stroke="{ID}" stroke-width="1.4"/>'
            # o'rta shar (marmar)
            f'<circle cx="90" cy="86" r="26" fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="{IG}" stroke="{I1}" stroke-width="1"/>'
                      for x, y in [(80, 82), (92, 78), (100, 88), (84, 94), (95, 96)])
            # pastki shar (kislota)
            + f'<path d="M64,118 a26,20 0 1 0 52,0 a26,20 0 1 0 -52,0" fill="{IP}" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M66,122 a24,15 0 0 0 48,0 v6 a24,12 0 0 1 -48,0 z" fill="{I2}" opacity="0.25"/>'
            # bo'yin va jo'mrak
            f'<line x1="90" y1="56" x2="90" y2="60" stroke="{ID}" stroke-width="3"/>'
            f'<line x1="116" y1="86" x2="152" y2="86" stroke="{ID}" stroke-width="3.4"/>'
            f'<rect x="140" y="80" width="10" height="12" rx="2" fill="{I2}"/>'
            f'<text x="156" y="90" class="lb" font-weight="bold" fill="{I2}">jo\'mrak → gaz</text>'
            '<text x="126" y="36" class="lb">kislota</text>'
            f'<path d="M124,34 q-10,0 -14,-2" fill="none" stroke="{IG}" stroke-width="1"/>'
            '<text x="128" y="66" class="lb">marmar (CaCO₃)</text>'
            '<text x="126" y="126" class="lb">kislota yig\'iladi</text>'
            '<text x="48" y="154" class="lb" font-weight="bold">Kipp apparati — gaz olish qurilmasi</text></svg>')

def fig_mass_curve():
    """NaHCO3 qizdirish: massa-vaqt egri — kamayib platoga chiqadi."""
    return ('<svg width="250" height="140" viewBox="0 0 250 140">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="36" y="6" width="206" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="36" y1="124" x2="244" y2="124" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="36" y1="124" x2="36" y2="8" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M38,28 L80,28 C120,32 130,80 160,88 L238,88" fill="none" stroke="{I1}" stroke-width="2.4"/>'
            f'<line x1="38" y1="28" x2="238" y2="28" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<line x1="38" y1="88" x2="238" y2="88" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<text x="42" y="22" class="lb" font-weight="bold">boshlang\'ich massa (NaHCO₃)</text>'
            f'<text x="166" y="102" class="lb" font-weight="bold" fill="{I2}">qoldiq (Na₂CO₃)</text>'
            f'<text x="104" y="62" class="lb" fill="{I2}">H₂O va CO₂ chiqadi</text>'
            f'<text x="6" y="16" class="lb">m</text>'
            '<text x="210" y="136" class="lb">t (qizdirish)</text></svg>')

def fig_bar_gaz():
    """Uch tajribada yig'ilgan gaz hajmlari — ustunlar."""
    data = [("1) Zn+HCl", 2.24, "H₂"), ("2) CaCO₃+HCl", 4.48, "CO₂"), ("3) H₂O₂→", 3.36, "O₂")]
    mx = 5.5
    bars = ""
    for i, (lab, v, gas) in enumerate(data):
        x = 58 + i * 64; h = v / mx * 104; y = 122 - h
        col = I1 if i != 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="38" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+19}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} L</text>'
                 f'<text x="{x+19}" y="135" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="260" height="146" viewBox="0 0 260 146">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="44" y="4" width="210" height="118" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="46" y1="{122-g/5.5*104:.0f}" x2="252" y2="{122-g/5.5*104:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="32" y="{125-g/5.5*104:.0f}" class="lb">{g}</text>' for g in [2, 4])
            + bars +
            f'<line x1="44" y1="122" x2="254" y2="122" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">V, L (n.sh.)</text></svg>')

def fig_scheme38():
    """B O1-38: marmar + HCl → CaCl2 + CO2 sxemasi."""
    return ('<svg width="270" height="92" viewBox="0 0 270 92">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="26" width="80" height="40" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="48" y="43" text-anchor="middle" class="lb" font-weight="bold">10 g CaCO₃</text>'
            '<text x="48" y="56" text-anchor="middle" class="lb">(marmar)</text>'
            f'<line x1="88" y1="46" x2="126" y2="46" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="130,46 122,42 122,50" fill="{I2}"/>'
            f'<text x="92" y="38" class="lb" font-weight="bold" fill="{I2}">+ HCl</text>'
            f'<rect x="132" y="26" width="76" height="40" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="170" y="43" text-anchor="middle" class="lb" font-weight="bold">CaCl₂ · ? g</text>'
            '<text x="170" y="56" text-anchor="middle" class="lb">eritmada</text>'
            f'<line x1="170" y1="26" x2="170" y2="14" stroke="{ID}" stroke-width="1.4"/>'
            f'<polygon points="170,10 166,18 174,18" fill="{ID}"/>'
            '<text x="180" y="16" class="lb">CO₂↑</text></svg>')

def fig_extinguisher():
    """Ko'pikli o't o'chirgich."""
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="30" width="34" height="72" rx="10" fill="#c62828" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="54" y="20" width="8" height="12" fill="#555"/>'
            f'<path d="M62,22 q16,-6 26,4" fill="none" stroke="#555" stroke-width="3"/>'
            f'<path d="M88,26 q10,4 8,12" fill="none" stroke="#555" stroke-width="2.4"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{I2}" stroke-width="1.2"/>'
                      for x, y, r in [(104, 46, 3), (114, 54, 4), (124, 62, 3), (112, 40, 2.4)])
            + '<path d="M128,84 q-6,-14 4,-22 q2,10 10,12 q-2,12 -14,10" fill="#f4a942" stroke="#d35400" stroke-width="1.2"/>'
            f'<text x="150" y="40" class="lb" font-weight="bold" fill="{I2}">CO₂ ko\'pigi</text>'
            '<text x="150" y="56" class="lb">NaHCO₃ + kislota</text>'
            '<text x="150" y="68" class="lb">→ CO₂↑</text>'
            '<text x="44" y="120" class="lb" font-weight="bold">ko\'pikli o\'t o\'chirgich</text></svg>')

def fig_tooth():
    """Tish emali va kislota hujumi."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M54,30 q20,-14 40,0 q6,22 -4,40 q-4,18 -10,18 q-5,0 -6,-16 q-1,-8 -5,-8 t-5,8 '
            f'q-1,16 -6,16 q-6,0 -10,-18 q-10,-18 6,-40z" fill="#fdfdf8" stroke="{ID}" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="{I2}"/>' for x, y in [(66, 26), (80, 22), (92, 28)])
            + f'<text x="104" y="30" class="lb" font-weight="bold" fill="{I2}">kislotalar</text>'
            f'<path d="M100,34 q-8,8 -14,10" fill="none" stroke="{IG}" stroke-width="1.2"/>'
            '<text x="116" y="54" class="lb">emal: kalsiy</text>'
            '<text x="116" y="66" class="lb">fosfat tuzlari</text>'
            '<text x="116" y="84" class="lb" font-weight="bold">kislota + tuz →</text>'
            '<text x="116" y="96" class="lb" font-weight="bold">yemirilish (karies)</text>'
            '<text x="44" y="114" class="lb" font-weight="bold">tish emali</text></svg>')

def fig_copperpan():
    """Qoraygan mis qozoncha va limon."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M40,50 h76 v30 a12,12 0 0 1 -12,12 h-52 a12,12 0 0 1 -12,-12 z" '
            f'fill="#c9863f" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M40,50 h76 v10 h-76 z" fill="#3e3e3e"/>'
            f'<line x1="116" y1="56" x2="140" y2="56" stroke="{ID}" stroke-width="3"/>'
            f'<circle cx="160" cy="86" r="13" fill="#f4d03f" stroke="#b7950b" stroke-width="1.4"/>'
            f'<circle cx="160" cy="86" r="6" fill="none" stroke="#b7950b" stroke-width="0.8"/>'
            '<text x="132" y="30" class="lb" font-weight="bold">qora qatlam — CuO</text>'
            f'<path d="M130,32 q-24,4 -50,20" fill="none" stroke="{IG}" stroke-width="1.2"/>'
            '<text x="146" y="110" class="lb">limon kislotasi</text>'
            '<text x="38" y="112" class="lb" font-weight="bold">qoraygan mis idish</text></svg>')

def fig_soil():
    """Kislotali tuproqqa ohak sepish."""
    return ('<svg width="230" height="116" viewBox="0 0 230 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="24" y="76" width="180" height="26" rx="3" fill="#8d6e63" opacity="0.7"/>'
            f'<path d="M24,76 q30,-8 60,0 t60,0 t60,0" fill="none" stroke="{I1}" stroke-width="1.6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="#fdfdf6" stroke="{IG}" stroke-width="0.6"/>'
                      for x, y in [(70, 56, ), (86, 48), (102, 58), (118, 46), (134, 56), (94, 66), (126, 66)])
            + f'<path d="M56,34 h30 l6,14 h-42 z" fill="{IP}" stroke="{ID}" stroke-width="1.4"/>'
            '<text x="130" y="30" class="lb" font-weight="bold">maydalangan ohak</text>'
            '<text x="130" y="42" class="lb">(CaCO₃ / Ca(OH)₂)</text>'
            f'<text x="30" y="96" class="lb" fill="#fff" font-weight="bold">nordon (kislotali) tuproq</text>'
            '<text x="24" y="112" class="lb" font-weight="bold">tuproqni ohaklash — neytrallash</text></svg>')

FIGS = dict(kipp=fig_kipp, mass_curve=fig_mass_curve, bar_gaz=fig_bar_gaz, scheme38=fig_scheme38,
            extinguisher=fig_extinguisher, tooth=fig_tooth, copperpan=fig_copperpan, soil=fig_soil)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #dcc9bf; border-radius:2pt;
                  background:#f7f2ef; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>12-bob — Sinflarning xossalari va olinishi</title><style>{css}</style>"]

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
  <div class="chapnum">12</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 12-bob · Mavzu pasporti (II.2)</div>
  <h1>Oksidlar, asoslar, kislotalar va tuzlarning xossalari</h1>
  <div class="lead">kimyoviy xossalar va olinish usullari · indikatorlar · faollik qatori ·
  ion almashinish shartlari · termik parchalanish · sifat reaksiyalari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>har sinf uchun olinish usullarini sanash (B: 1, 15)</li>
      <li>reaksiya boradimi: faollik qatori, almashinish shartlari</li>
      <li>cheklovchi reagent va aralashma hisoblari (B: 4, 23, 36, 40)</li>
      <li>indikatorlar va sifat reaksiyalari (A: 1, 2, 9; B: 12, 18, 43)</li>
      <li>termik parchalanish qatorlari (B: 3, 13, 19, 32)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>Kipp apparati (B: 5, 28)</li>
      <li>qizdirish massa-grafigi (B: 19, 32)</li>
      <li>gaz hajmlari ustunlari va sxema (A: 26, 32; B: 26, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>Cu ni kislotada «eritish»</li>
      <li>suvni kislotaga quyish deb yozish</li>
      <li>almashinish shartlarini (cho'kma/gaz/suv) unutish</li>
      <li>parchalanishda massa saqlanadi deb olish</li></ul></div>
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
