# -*- coding: utf-8 -*-
"""1-bob (Atom tuzilishi) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I1A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I1B.json", encoding="utf-8"))
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
            f'{km}<path d="{p}" fill="none" stroke="#283593" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.1 figuralari (indigo-amber palitrasi) ----------
I1, I2, ID, IP, IG = "#283593", "#ef6c00", "#1a237e", "#f2f4fb", "#d8ddf0"

def fig_ion_energy():
    """B: ketma-ket ionlanish energiyalari — E3-E4 orasida sakrash (III A element)."""
    vals = [("E₁", 578), ("E₂", 1817), ("E₃", 2745), ("E₄", 11578)]
    mx = 12000
    bars = ""
    for i, (lab, v) in enumerate(vals):
        x = 58 + i * 45; h = v / mx * 112; y = 130 - h
        col = I2 if i == 3 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="28" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+14}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+14}" y="143" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="152" viewBox="0 0 250 152">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="44" y="4" width="200" height="126" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<path d="M190,44 q10,-16 22,-20" fill="none" stroke="{I2}" stroke-width="1.4" stroke-dasharray="4,3"/>'
            f'<text x="146" y="20" class="lb" font-weight="bold" fill="{I2}">keskin sakrash!</text>'
            + bars +
            f'<line x1="44" y1="130" x2="246" y2="130" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">E, kJ/mol</text></svg>')

def fig_isotope_bars():
    """Mg izotoplari ulushlari — ustunli diagramma."""
    data = [("²⁴Mg", 79), ("²⁵Mg", 10), ("²⁶Mg", 11)]
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 58; h = v * 1.4; y = 128 - h
        bars += (f'<rect x="{x}" y="{y:.0f}" width="34" height="{h:.0f}" rx="2" fill="{I1}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+17}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v} %</text>'
                 f'<text x="{x+17}" y="141" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="150" viewBox="0 0 250 150">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="198" height="124" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{128-g*1.4:.0f}" x2="242" y2="{128-g*1.4:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="30" y="{131-g*1.4:.0f}" class="lb">{g}</text>' for g in [25, 50, 75])
            + bars +
            f'<line x1="46" y1="128" x2="244" y2="128" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="6" y="14" class="lb">ulush, %</text></svg>')

def fig_atom_model():
    """Bor modeli: yadro + 2,8,1 qavatlar (natriy)."""
    import math
    rings = ""
    shells = [(20, 2), (34, 8), (48, 1)]
    for r, ne in shells:
        rings += f'<circle cx="120" cy="66" r="{r}" fill="none" stroke="{I1}" stroke-width="1.2" stroke-dasharray="3,3"/>'
        for k in range(ne):
            a = k * (360 / ne) * math.pi / 180
            ex, ey = 120 + r * math.cos(a), 66 + r * math.sin(a)
            rings += f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="3" fill="{I2}" stroke="#fff" stroke-width="0.8"/>'
    return ('<svg width="240" height="132" viewBox="0 0 240 132">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            + rings +
            f'<circle cx="120" cy="66" r="9" fill="{I1}"/>'
            '<text x="120" y="69" text-anchor="middle" fill="#fff" font-size="7" font-family="Georgia">p+n</text>'
            '<text x="176" y="24" class="lb" font-weight="bold">qavatlar: 2, 8, 1</text>'
            f'<text x="176" y="38" class="lb">● — elektron</text>'
            '<text x="14" y="120" class="lb" font-weight="bold">Bor modeli</text></svg>')

def fig_scheme38():
    """B O1-38: sxema — Mg ionlashuvi, elektronlar Ag+ ga."""
    return ('<svg width="260" height="96" viewBox="0 0 260 96">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="10" y="26" width="66" height="40" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="43" y="43" text-anchor="middle" class="lb" font-weight="bold">0,1 mol Mg</text>'
            '<text x="43" y="56" text-anchor="middle" class="lb">Mg − 2e → Mg²⁺</text>'
            f'<line x1="76" y1="46" x2="116" y2="46" stroke="{I2}" stroke-width="2"/>'
            f'<polygon points="120,46 112,42 112,50" fill="{I2}"/>'
            f'<text x="82" y="38" class="lb" font-weight="bold" fill="{I2}">e⁻ oqimi</text>'
            f'<rect x="122" y="26" width="72" height="40" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="158" y="43" text-anchor="middle" class="lb" font-weight="bold">Ag⁺ eritmasi</text>'
            '<text x="158" y="56" text-anchor="middle" class="lb">Ag⁺ + e → Ag</text>'
            f'<line x1="194" y1="46" x2="228" y2="46" stroke="{ID}" stroke-width="1.6"/>'
            f'<polygon points="232,46 224,42 224,50" fill="{ID}"/>'
            '<text x="234" y="50" class="lb" font-weight="bold">? g Ag</text></svg>')

def fig_flame():
    """Alanga testi: gorelka + sariq alanga + tuz qoshig'i."""
    return ('<svg width="230" height="126" viewBox="0 0 230 126">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            '<rect x="66" y="86" width="36" height="26" rx="4" fill="#78909c" stroke="#455a64" stroke-width="1.4"/>'
            '<rect x="80" y="62" width="8" height="26" fill="#90a4ae" stroke="#455a64"/>'
            # ko'k asosiy alanga
            '<path d="M84,62 q-9,-13 0,-26 q9,13 0,26" fill="#5c8fd6" opacity="0.7"/>'
            # sariq rang (Na)
            '<path d="M84,44 q-7,-12 0,-24 q7,12 0,24" fill="#f4c542" stroke="#ef6c00" stroke-width="1"/>'
            # qoshiqcha tuz bilan
            '<line x1="150" y1="34" x2="96" y2="30" stroke="#455a64" stroke-width="2.4"/>'
            '<ellipse cx="94" cy="30" rx="9" ry="4" fill="#fff" stroke="#90a4ae"/>'
            '<text x="152" y="30" class="lb">NaCl namunasi</text>'
            '<text x="112" y="58" class="lb" font-weight="bold" fill="#ef6c00">sariq alanga!</text>'
            '<text x="40" y="122" class="lb" font-weight="bold">alanga testi (Na — sariq)</text></svg>')

def fig_neon():
    """Neon reklama: tungi vitrina, rangli naychalar."""
    return ('<svg width="240" height="120" viewBox="0 0 240 120">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:#fff}}</style>'
            '<rect x="16" y="10" width="208" height="86" rx="6" fill="#151a3a"/>'
            '<path d="M40,56 q14,-26 28,0 q14,26 28,0" fill="none" stroke="#ff5252" stroke-width="4" stroke-linecap="round"/>'
            '<circle cx="150" cy="46" r="17" fill="none" stroke="#40c4ff" stroke-width="4"/>'
            '<line x1="180" y1="30" x2="196" y2="62" stroke="#69f0ae" stroke-width="4" stroke-linecap="round"/>'
            '<text x="40" y="86" class="lb">Ne — qizil</text>'
            '<text x="128" y="86" class="lb">Ar — ko\'k</text>'
            f'<text x="30" y="114" font-size="8.8" font-family="Georgia" fill="{ID}" font-weight="bold">tungi neon reklamalar — qo\'zg\'algan atomlar nuri</text></svg>')

def fig_xray():
    """Rentgen surati: qo'l panjasi soyasi."""
    fingers = ""
    for i, (dx, l) in enumerate([(0, 26), (14, 34), (28, 38), (42, 34), (56, 24)]):
        x = 84 + dx
        fingers += (f'<rect x="{x}" y="{66-l}" width="8" height="{l}" rx="4" fill="#e8eef8" opacity="0.9"/>'
                    f'<line x1="{x+4}" y1="{70-l}" x2="{x+4}" y2="62" stroke="#aab8d8" stroke-width="1" stroke-dasharray="2,3"/>')
    return ('<svg width="240" height="122" viewBox="0 0 240 122">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            '<rect x="60" y="8" width="120" height="100" rx="6" fill="#0d1230"/>'
            + fingers +
            '<ellipse cx="122" cy="84" rx="34" ry="20" fill="#e8eef8" opacity="0.9"/>'
            '<text x="8" y="40" class="lb" font-weight="bold">suyak (Ca) —</text>'
            '<text x="8" y="52" class="lb">nurni yutadi,</text>'
            '<text x="8" y="64" class="lb">oq ko\'rinadi</text>'
            '<text x="66" y="120" class="lb" font-weight="bold">tibbiy rentgen surati</text></svg>')

def fig_banana():
    """Banan — tabiiy K-40 radioizotopi haqida."""
    return ('<svg width="240" height="110" viewBox="0 0 240 110">'
            f'<style>.lb{{font-size:8.8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            '<path d="M40,36 q46,54 108,40 q10,-2 12,6 q2,8 -10,10 q-76,10 -120,-46 q-6,-8 2,-12 q6,-2 8,2 z" '
            'fill="#f4c542" stroke="#c49000" stroke-width="1.6"/>'
            '<path d="M40,36 q-6,-8 2,-12" fill="none" stroke="#7a5230" stroke-width="4" stroke-linecap="round"/>'
            f'<circle cx="180" cy="30" r="15" fill="none" stroke="{I2}" stroke-width="1.6"/>'
            f'<text x="180" y="34" text-anchor="middle" class="lb" font-weight="bold" fill="{I2}">⁴⁰K</text>'
            f'<path d="M168,42 q-14,12 -30,16" fill="none" stroke="{I2}" stroke-width="1.2" stroke-dasharray="3,3"/>'
            '<text x="120" y="104" class="lb" font-weight="bold" text-anchor="middle">banan tarkibida tabiiy ⁴⁰K izotopi bor (xavfsiz!)</text></svg>')

FIGS = dict(ion_energy=fig_ion_energy, isotope_bars=fig_isotope_bars, atom_model=fig_atom_model,
            scheme38=fig_scheme38, flame=fig_flame, neon=fig_neon, xray=fig_xray, banana=fig_banana)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #c9cfe8; border-radius:2pt;
                  background:#f2f4fb; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>1-bob — Atom tuzilishi</title><style>{css}</style>"]

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
  <div class="chapnum">1</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 1-bob · Mavzu pasporti (I.1)</div>
  <h1>Atom tuzilishi</h1>
  <div class="lead">elementar zarralar · izotoplar va o'rtacha atom massasi · elektron qavatlar va
  konfiguratsiyalar · ionlar · ionlanish energiyalari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>p, n, e sonlarini (ionlarda ham) aniqlash</li>
      <li>izotop hisoblari: o'rtacha massa va teskari masala</li>
      <li>konfiguratsiya ↔ element ↔ davr/guruh o'tishlari</li>
      <li>izoelektron zarralar, ion konfiguratsiyalari</li>
      <li>ko'p bosqichli mol-atom-zarra zanjirlari (36–40)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>ionlanish energiyalari diagrammasi (B: 5, 32)</li>
      <li>izotop ulushlari ustunlari (A: 26; B: 26)</li>
      <li>Bor modeli va sxema-masala (A: 28, 32; B: 28, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>massa soni bilan neytronlar sonini adashtirish</li>
      <li>ionda elektron sonini zaryadga qarab tuzatmaslik</li>
      <li>Fe²⁺ da 4s dan oldin 3d ni «yechish»</li>
      <li>o'rtacha massani oddiy o'rta arifmetik deb olish</li></ul></div>
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
