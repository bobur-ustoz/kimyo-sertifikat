# -*- coding: utf-8 -*-
"""4-bob (Bog'lanish) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I4A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I4B.json", encoding="utf-8"))
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

# ---------- I.4 figuralari ----------
def fig_salt():
    """Osh tuzi: kub kristallar va panjara sxemasi."""
    ions = ""
    for r in range(3):
        for c in range(3):
            x, y = 150 + c * 24, 34 + r * 24
            col = "#5b8bab" if (r + c) % 2 == 0 else "#c0392b"
            sign = "+" if (r + c) % 2 == 0 else "−"
            ions += (f'<circle cx="{x}" cy="{y}" r="9" fill="{col}" opacity="0.85"/>'
                     f'<text x="{x}" y="{y+3.5}" text-anchor="middle" fill="#fff" font-size="10" '
                     f'font-family="Georgia">{sign}</text>')
            if c < 2: ions += f'<line x1="{x+9}" y1="{y}" x2="{x+15}" y2="{y}" stroke="#889" stroke-width="1.2"/>'
            if r < 2: ions += f'<line x1="{x}" y1="{y+9}" x2="{x}" y2="{y+15}" stroke="#889" stroke-width="1.2"/>'
    return ('<svg width="250" height="126" viewBox="0 0 250 126">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # kub kristallar
            '<g stroke="#8a9aa5" stroke-width="1.4" fill="#eef4f8">'
            '<rect x="26" y="46" width="34" height="34"/><path d="M26,46 l9,-9 h34 l-9,9 M60,46 l9,-9 v34 l-9,9"/>'
            '<rect x="66" y="66" width="26" height="26"/><path d="M66,66 l7,-7 h26 l-7,7 M92,66 l7,-7 v26 l-7,7"/></g>'
            '<text x="24" y="112" class="lb" font-weight="bold">tuz kristallari</text>'
            + ions +
            '<text x="142" y="118" class="lb" font-weight="bold">Na⁺ va Cl⁻ panjarasi</text></svg>')

def fig_pencil():
    """Qalam (grafit) va olmos uzuk."""
    return ('<svg width="250" height="120" viewBox="0 0 250 120">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # qalam
            '<rect x="20" y="40" width="80" height="16" rx="2" fill="#f4d03f" stroke="#b7950b" stroke-width="1.4"/>'
            '<polygon points="100,40 118,48 100,56" fill="#e8d5a3" stroke="#b7950b" stroke-width="1.2"/>'
            '<polygon points="112,45 118,48 112,51" fill="#2c3e50"/>'
            # grafit qatlamlari
            '<g stroke="#5d6d7e" stroke-width="1.4">'
            '<line x1="30" y1="76" x2="86" y2="76"/><line x1="34" y1="84" x2="90" y2="84"/>'
            '<line x1="30" y1="92" x2="86" y2="92"/></g>'
            '<text x="24" y="112" class="lb" font-weight="bold">grafit — qatlamlar sirg\'aladi</text>'
            # uzuk
            '<circle cx="185" cy="72" r="22" fill="none" stroke="#c9a227" stroke-width="6"/>'
            '<polygon points="185,30 176,44 194,44" fill="#d6ecf7" stroke="#5b8bab" stroke-width="1.4"/>'
            '<polygon points="176,44 194,44 185,56" fill="#eef7fc" stroke="#5b8bab" stroke-width="1.4"/>'
            '<text x="150" y="112" class="lb" font-weight="bold">olmos — atom to\'ri</text>'
            '<text x="106" y="24" class="lb">ikkalasi ham C!</text></svg>')

def fig_snowflake():
    """Olti nurli qor parchasi."""
    import math
    arms = ""
    for i in range(6):
        a = i * 60 * math.pi / 180
        x2, y2 = 120 + 44 * math.cos(a), 60 + 44 * math.sin(a)
        arms += f'<line x1="120" y1="60" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#5b8bab" stroke-width="2.6" stroke-linecap="round"/>'
        for f in (0.5, 0.75):
            bx, by = 120 + 44 * f * math.cos(a), 60 + 44 * f * math.sin(a)
            for da in (-30, 30):
                b = a + da * math.pi / 180
                ex, ey = bx + 10 * math.cos(b), by + 10 * math.sin(b)
                arms += f'<line x1="{bx:.0f}" y1="{by:.0f}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="#7fb3d3" stroke-width="1.6" stroke-linecap="round"/>'
    return ('<svg width="240" height="120" viewBox="0 0 240 120">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            + arms + '<circle cx="120" cy="60" r="4" fill="#5b8bab"/>'
            '<text x="10" y="30" class="lb" font-weight="bold">qor parchasi —</text>'
            '<text x="10" y="42" class="lb" font-weight="bold">doim 6 burchakli</text></svg>')

def fig_wire():
    """Mis sim va elektron gazi sxemasi."""
    cations = "".join(f'<circle cx="{146+c*22}" cy="{40+r*20}" r="7" fill="#e67e22" opacity="0.9"/>'
                      f'<text x="{146+c*22}" y="{43+r*20}" text-anchor="middle" fill="#fff" font-size="8" font-family="Georgia">+</text>'
                      for r in range(3) for c in range(4))
    electrons = "".join(f'<circle cx="{138+(i*17)%92}" cy="{34+(i*13)%54}" r="2" fill="#2471a3"/>' for i in range(12))
    return ('<svg width="250" height="120" viewBox="0 0 250 120">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            # sim
            '<path d="M14,50 q30,-24 56,0 q22,20 44,4" fill="none" stroke="#b5651d" stroke-width="8" stroke-linecap="round"/>'
            '<path d="M14,50 q30,-24 56,0 q22,20 44,4" fill="none" stroke="#e67e22" stroke-width="4" stroke-linecap="round"/>'
            '<text x="16" y="84" class="lb" font-weight="bold">mis sim</text>'
            # panjara
            + cations + electrons +
            '<rect x="132" y="24" width="100" height="72" fill="none" stroke="#8a9aa5" stroke-width="1" stroke-dasharray="4,3"/>'
            '<text x="132" y="112" class="lb" font-weight="bold">kationlar + erkin e⁻ «gazi»</text></svg>')

def fig_em_axis():
    """Delta-EM shkalasi: bog' turlari zonalari."""
    def X(v): return 24 + v * 60  # 0..3,5
    return ('<svg width="250" height="86" viewBox="0 0 250 86">'
            '<style>.lb{font-size:8.6px;font-family:Georgia,serif;fill:#333}</style>'
            f'<rect x="{X(0)}" y="30" width="{X(1.7)-X(0)}" height="18" fill="#dcebf5"/>'
            f'<rect x="{X(1.7)}" y="30" width="{X(3.5)-X(1.7)}" height="18" fill="#f9e0dc"/>'
            f'<line x1="{X(0)}" y1="48" x2="{X(3.5)+8}" y2="48" stroke="#222" stroke-width="1.4"/>'
            f'<polygon points="{X(3.5)+12},48 {X(3.5)+4},44 {X(3.5)+4},52" fill="#222"/>'
            + "".join(f'<line x1="{X(v)}" y1="45" x2="{X(v)}" y2="51" stroke="#222" stroke-width="1.2"/>'
                      f'<text x="{X(v)-6}" y="62" class="lb">{str(v).replace(".", ",")}</text>'
                      for v in [0, 1.7, 3.5]) +
            f'<text x="{X(0.25)}" y="42" class="lb" font-weight="bold">kovalent</text>'
            f'<text x="{X(0.1)}" y="26" class="lb">qutbsiz→qutbli</text>'
            f'<text x="{X(2.2)}" y="42" class="lb" font-weight="bold">ion</text>'
            f'<text x="{X(2.9)}" y="62" class="lb">ΔEM</text>'
            '<text x="24" y="80" class="lb">ΔEM ortishi bilan bog\' ionlilik xarakteri kuchayadi</text></svg>')

def fig_lattice():
    """Ikki panjara: 1 — ion (NaCl tipi), 2 — molekular (CO2)."""
    ion = ""
    for r in range(3):
        for c in range(3):
            x, y = 40 + c * 22, 34 + r * 22
            col = "#5b8bab" if (r + c) % 2 == 0 else "#c0392b"
            sign = "+" if (r + c) % 2 == 0 else "−"
            ion += (f'<circle cx="{x}" cy="{y}" r="8" fill="{col}" opacity="0.85"/>'
                    f'<text x="{x}" y="{y+3}" text-anchor="middle" fill="#fff" font-size="9" font-family="Georgia">{sign}</text>')
    mol = ""
    for r in range(2):
        for c in range(2):
            x, y = 158 + c * 44, 42 + r * 36
            mol += (f'<circle cx="{x-8}" cy="{y}" r="5" fill="#c0392b"/>'
                    f'<circle cx="{x}" cy="{y}" r="6" fill="#5d6d7e"/>'
                    f'<circle cx="{x+8}" cy="{y}" r="5" fill="#c0392b"/>')
    return ('<svg width="250" height="122" viewBox="0 0 250 122">'
            '<style>.lb{font-size:9px;font-family:Georgia,serif;fill:#333}</style>'
            + ion +
            '<text x="42" y="110" class="lb" font-weight="bold">1-panjara</text>'
            + mol +
            '<rect x="140" y="24" width="94" height="72" fill="none" stroke="#8a9aa5" stroke-width="1" stroke-dasharray="4,3"/>'
            '<text x="160" y="110" class="lb" font-weight="bold">2-panjara</text></svg>')

FIGS = dict(salt=fig_salt, pencil=fig_pencil, snowflake=fig_snowflake, wire=fig_wire,
            em_axis=fig_em_axis, lattice=fig_lattice)

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
H = [f"<meta charset='utf-8'><title>4-bob — Kimyoviy bog'lanish</title><style>{css}</style>"]

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
  <div class="chapnum">4</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 4-bob · Mavzu pasporti (I.4)</div>
  <h1>Kimyoviy bog'lanish</h1>
  <div class="lead">ion, kovalent (qutbli/qutbsiz), metall va vodorod bog'lanish · σ va π bog'lar ·
  elektromanfiylik · kristall panjaralar · bog' energiyasi va uzunligi qatorlari</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>bog' turini EM farqidan aniqlash</li>
      <li>σ/π va ion/kovalent bog'larni sanash</li>
      <li>panjara turi ↔ moddaning xossalari</li>
      <li>energiya-uzunlik-qutblilik qatorlari</li>
      <li>donor-akseptor mexanizmi (NH₄⁺)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>EM jadvali va shkalasi (B: 5, 27, 32; A: 32)</li>
      <li>panjara sxemalarini o'qish (B: 28; A: 4)</li>
      <li>xossa-jadvaldan panjara aniqlash (A: 17; B: 17; O2-43)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>ion va qutbli kovalent chegarasini bilmaslik</li>
      <li>karrali bog'da σ va π sonini adashtirish</li>
      <li>vodorod bog'ni ichki bog' deb o'ylash</li>
      <li>valentlik bilan oksidlanish darajasini tenglashtirish</li></ul></div>
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
