# -*- coding: utf-8 -*-
"""16-bob (Laboratoriya amaliyoti) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_IV1A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_IV1B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#1565c0", "#0d47a1", "#eef5fd", "#c62828"

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
            f'{km}<path d="{p}" fill="none" stroke="#1565c0" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- IV.1 figuralari (laboratoriya ko'k + xavfsizlik qizil palitrasi) ----------
I1, I2, ID, IP, IG = "#1565c0", "#c62828", "#0d47a1", "#eef5fd", "#c9def5"

def fig_equip():
    """Jihozlar paneli: a) kolba, b) menzurka, c) probirka, d) quyg'ich."""
    return ('<svg width="270" height="130" viewBox="0 0 270 130">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # a) kolba
            f'<path d="M40,22 v22 l-14,34 a8,8 0 0 0 8,10 h24 a8,8 0 0 0 8,-10 l-14,-34 v-22 z" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            '<text x="46" y="118" text-anchor="middle" class="lb" font-weight="bold">a)</text>'
            # b) menzurka
            f'<path d="M96,30 h30 v56 a6,6 0 0 1 -6,6 h-18 a6,6 0 0 1 -6,-6 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            + "".join(f'<line x1="98" y1="{40+i*10}" x2="108" y2="{40+i*10}" stroke="{I1}" stroke-width="1"/>'
                      for i in range(5))
            + '<text x="111" y="118" text-anchor="middle" class="lb" font-weight="bold">b)</text>'
            # c) probirka
            f'<path d="M158,26 v56 a10,10 0 0 0 20,0 v-56" fill="none" stroke="{ID}" stroke-width="1.8"/>'
            '<text x="168" y="118" text-anchor="middle" class="lb" font-weight="bold">c)</text>'
            # d) quyg'ich (voronka)
            f'<path d="M208,30 h44 l-17,26 v26 h-10 v-26 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            '<text x="230" y="118" text-anchor="middle" class="lb" font-weight="bold">d)</text></svg>')

def fig_filter():
    """Filtrlash: voronka + filtr qog'oz + kolba."""
    return ('<svg width="240" height="140" viewBox="0 0 240 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M70,24 h60 l-24,34 v18 h-12 v-18 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M76,26 h48 l-24,30 z" fill="#fff" stroke="{I1}" stroke-width="1.1"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#8d6e63"/>' for x, y in [(95, 34), (103, 38), (99, 44)])
            + f'<path d="M100,78 v10" stroke="{I1}" stroke-width="2" stroke-dasharray="2,3"/>'
            f'<path d="M74,92 v26 a10,10 0 0 0 10,10 h32 a10,10 0 0 0 10,-10 v-26" fill="none" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="78" y="108" width="44" height="16" rx="4" fill="{I1}" opacity="0.2"/>'
            '<text x="142" y="34" class="lb" font-weight="bold">filtr qog\'oz</text>'
            '<text x="142" y="48" class="lb">cho\'kma qoladi</text>'
            '<text x="142" y="106" class="lb" font-weight="bold">filtrat</text>'
            '<text x="142" y="118" class="lb">(tiniq eritma)</text>'
            '<text x="60" y="136" class="lb" font-weight="bold">filtrlash</text></svg>')

def fig_distill():
    """Haydash apparati: kolba + termometr + sovutgich + qabul kolba."""
    return ('<svg width="270" height="140" viewBox="0 0 270 140">'
            f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<circle cx="56" cy="88" r="24" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M56,90 a20,14 0 0 0 20,10" fill="none"/>'
            f'<rect x="40" y="88" width="32" height="18" rx="8" fill="{I1}" opacity="0.25"/>'
            f'<path d="M52,64 v-26 h6 v26" fill="none" stroke="{ID}" stroke-width="1.4"/>'
            f'<circle cx="55" cy="34" r="4" fill="{I2}"/>'
            f'<path d="M66,70 l44,-18 h60" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<path d="M108,44 h56 v14 h-56 z" fill="{IP}" stroke="{I1}" stroke-width="1.4"/>'
            f'<path d="M170,52 q22,8 26,34" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<path d="M186,96 v18 a8,8 0 0 0 8,8 h12 a8,8 0 0 0 8,-8 v-18" fill="none" stroke="{ID}" stroke-width="1.6"/>'
            f'<rect x="189" y="106" width="22" height="12" rx="3" fill="{I1}" opacity="0.25"/>'
            '<text x="20" y="128" class="lb" font-weight="bold">qizdirish kolbasi</text>'
            '<text x="104" y="38" class="lb" font-weight="bold">sovutgich (suvli)</text>'
            '<text x="64" y="30" class="lb">termometr</text>'
            '<text x="216" y="112" class="lb">qabul kolba</text>'
            '<text x="180" y="134" class="lb" font-weight="bold">haydash (distillash)</text></svg>')

def fig_separator():
    """Ajratuvchi voronka: ikki qatlam va jo'mrak."""
    return ('<svg width="230" height="140" viewBox="0 0 230 140">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M84,20 h40 l-6,14 -4,44 q-10,10 -20,0 l-4,-44 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M88,40 l3,36 q9,9 18,0 l3,-36 z" fill="#f6d47a" opacity="0.8"/>'
            f'<path d="M91,60 l0,16 q9,9 18,0 l0,-16 z" fill="{I1}" opacity="0.35"/>'
            f'<line x1="104" y1="82" x2="104" y2="98" stroke="{ID}" stroke-width="2.6"/>'
            f'<rect x="98" y="96" width="12" height="8" rx="2" fill="{I2}"/>'
            f'<path d="M104,106 v14" stroke="{I1}" stroke-width="2" stroke-dasharray="2,3"/>'
            '<text x="136" y="50" class="lb" font-weight="bold">benzin (ustki)</text>'
            '<text x="136" y="72" class="lb" font-weight="bold">suv (pastki)</text>'
            '<text x="118" y="102" class="lb">jo\'mrak</text>'
            '<text x="66" y="134" class="lb" font-weight="bold">ajratuvchi voronka</text></svg>')

def fig_heat_curve():
    """Qizdirish egri chiziqlari: toza modda (plato) va aralashma."""
    return ('<svg width="260" height="150" viewBox="0 0 260 150">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="36" y="6" width="216" height="124" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="36" y1="130" x2="252" y2="130" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="36" y1="130" x2="36" y2="8" stroke="{ID}" stroke-width="1.4"/>'
            f'<path d="M38,124 L110,48 L200,48 L246,30" fill="none" stroke="{I1}" stroke-width="2.4"/>'
            f'<path d="M38,124 C110,70 190,44 246,22" fill="none" stroke="{I2}" stroke-width="1.8" stroke-dasharray="5,3"/>'
            f'<line x1="38" y1="48" x2="246" y2="48" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<text x="120" y="42" class="lb" font-weight="bold" fill="{I1}">toza modda: plato (qaynash)</text>'
            f'<text x="90" y="94" class="lb" font-weight="bold" fill="{I2}">aralashma: plato yo\'q</text>'
            f'<text x="6" y="16" class="lb">t, °C</text>'
            '<text x="212" y="144" class="lb">vaqt</text></svg>')

def fig_bar_zichlik():
    """Suyuqliklar zichligi: yog', suv, simob."""
    data = [("yog'", 0.9), ("suv", 1.0), ("simob", 13.6)]
    mx = 15.0
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 62; h = max(v / mx * 108, 6); y = 124 - h
        col = I2 if i == 2 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="36" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+18}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+18}" y="137" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="260" height="148" viewBox="0 0 260 148">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="48" y="4" width="206" height="120" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="50" y1="{124-g/15*108:.0f}" x2="252" y2="{124-g/15*108:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="36" y="{127-g/15*108:.0f}" class="lb">{g}</text>' for g in [5, 10])
            + bars +
            f'<line x1="48" y1="124" x2="254" y2="124" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">ρ, g/mL</text></svg>')

def fig_scheme38():
    """B O1-38: temir+qum+tuz ajratish ketma-ketligi."""
    steps = [("30 g\naralashma", None), ("magnit", "− 6 g Fe"), ("filtrlash", "− 9 g qum"),
             ("bug'latish", "tuz · ? g")]
    H = [f'<svg width="286" height="80" viewBox="0 0 286 80">'
         f'<style>.lb{{font-size:8px;font-family:Georgia,serif;fill:{ID}}}</style>']
    x = 4
    labels = ["30 g aralashma", "magnit", "filtrlash", "bug'latish"]
    subs = [None, "− 6 g Fe", "− 9 g qum", "tuz = ? g"]
    for i, lab in enumerate(labels):
        w = 74 if i == 0 else 60
        H.append(f'<rect x="{x}" y="24" width="{w}" height="30" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
                 f'<text x="{x+w/2}" y="42" text-anchor="middle" class="lb" font-weight="bold">{lab}</text>')
        if subs[i]:
            H.append(f'<text x="{x+w/2}" y="68" text-anchor="middle" class="lb" fill="{I2}" font-weight="bold">{subs[i]}</text>')
        x += w
        if i < 3:
            H.append(f'<line x1="{x+2}" y1="39" x2="{x+14}" y2="39" stroke="{I2}" stroke-width="2"/>'
                     f'<polygon points="{x+18},39 {x+10},35 {x+10},43" fill="{I2}"/>')
            x += 22
    H.append('</svg>')
    return "".join(H)

def fig_teabag():
    """Choy xaltasi damlanmoqda."""
    return ('<svg width="220" height="122" viewBox="0 0 220 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M44,36 h56 l-5,58 a7,7 0 0 1 -7,6 h-32 a7,7 0 0 1 -7,-6 z" fill="{IP}" stroke="{ID}" stroke-width="1.6"/>'
            f'<path d="M47,54 h50 l-4,40 a5,5 0 0 1 -5,4 h-32 a5,5 0 0 1 -5,-4 z" fill="#c98d4b" opacity="0.55"/>'
            f'<rect x="58" y="58" width="24" height="28" rx="3" fill="#fdfdf6" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#6d4c41"/>' for x, y in [(64, 68), (72, 74), (68, 80), (76, 66)])
            + f'<line x1="70" y1="58" x2="82" y2="30" stroke="{ID}" stroke-width="1.2"/>'
            f'<rect x="78" y="22" width="14" height="9" rx="2" fill="{I2}"/>'
            '<text x="112" y="50" class="lb" font-weight="bold">xaltacha = filtr</text>'
            '<text x="112" y="66" class="lb">moddalar eriydi,</text>'
            '<text x="112" y="78" class="lb">barglar o\'tmaydi</text>'
            '<text x="42" y="116" class="lb" font-weight="bold">choy damlash «kimyosi»</text></svg>')

def fig_safety():
    """Himoya ko'zoynagi."""
    return ('<svg width="220" height="110" viewBox="0 0 220 110">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M40,44 q30,-14 60,0 q8,20 -6,30 q-24,10 -48,0 q-14,-10 -6,-30z" '
            f'fill="{IP}" stroke="{ID}" stroke-width="1.8" opacity="0.9"/>'
            f'<path d="M46,50 q24,-10 48,0" fill="none" stroke="{I1}" stroke-width="1.2"/>'
            f'<path d="M100,52 q10,-4 16,0" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            f'<path d="M40,52 q-12,2 -14,10" fill="none" stroke="{ID}" stroke-width="2.2"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="{I2}"/>' for x, y in [(140, 36), (150, 46), (144, 56)])
            + f'<text x="156" y="40" class="lb" font-weight="bold" fill="{I2}">sachrash!</text>'
            '<text x="128" y="78" class="lb">ko\'zoynak to\'sadi</text>'
            '<text x="38" y="102" class="lb" font-weight="bold">himoya ko\'zoynagi — doimo</text></svg>')

def fig_magnet():
    """Magnit temirni ajratmoqda."""
    return ('<svg width="220" height="112" viewBox="0 0 220 112">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M60,26 h22 v20 h-22 a10,10 0 0 1 0,-20 z M104,26 h-22 M104,46 h-22" transform="rotate(28 84 40)"'
            f' fill="{I2}" stroke="{ID}" stroke-width="1.4"/>'
            + "".join(f'<rect x="{x}" y="{y}" width="5" height="2.4" rx="1" fill="#555" transform="rotate({r} {x} {y})"/>'
                      for x, y, r in [(96, 58, 20), (104, 64, -12), (98, 70, 42), (108, 54, 8)])
            + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#f4d03f" stroke="#b7950b" stroke-width="0.7"/>'
                      for x, y in [(60, 92), (72, 96), (84, 92), (96, 98), (108, 94), (120, 97), (66, 100)])
            + '<text x="132" y="40" class="lb" font-weight="bold">temir yopishadi</text>'
            '<text x="132" y="92" class="lb">oltingugurt qoladi</text>'
            '<text x="56" y="110" class="lb" font-weight="bold">magnit bilan ajratish</text></svg>')

def fig_evap():
    """Chinni kosachada bug'latish."""
    return ('<svg width="220" height="116" viewBox="0 0 220 116">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M50,58 a34,18 0 0 0 68,0 z" fill="#fdfdf6" stroke="{ID}" stroke-width="1.8"/>'
            f'<path d="M56,58 a28,12 0 0 0 56,0 z" fill="{I1}" opacity="0.2"/>'
            + "".join(f'<path d="M{x},50 q4,-6 0,-12 q-4,-6 0,-12" fill="none" stroke="{IG}" stroke-width="1.6"/>'
                      for x in [70, 84, 98])
            + f'<path d="M74,84 q-6,-8 0,-14 q6,6 0,14" fill="#f4a942" stroke="#d35400" stroke-width="1.1" transform="translate(10,8)"/>'
            f'<line x1="64" y1="96" x2="104" y2="96" stroke="{ID}" stroke-width="2"/>'
            + "".join(f'<rect x="{x}" y="62" width="3.6" height="3.6" fill="#fff" stroke="{IG}" stroke-width="0.6"/>'
                      for x in [62, 70, 100, 108])
            + '<text x="128" y="40" class="lb" font-weight="bold">suv uchadi</text>'
            '<text x="128" y="66" class="lb">tuz kristallari</text>'
            '<text x="128" y="78" class="lb">devorda qoladi</text>'
            '<text x="48" y="112" class="lb" font-weight="bold">bug\'latish kosachasi</text></svg>')

FIGS = dict(equip=fig_equip, filter=fig_filter, distill=fig_distill, separator=fig_separator,
            heat_curve=fig_heat_curve, bar_zichlik=fig_bar_zichlik, scheme38=fig_scheme38,
            teabag=fig_teabag, safety=fig_safety, magnet=fig_magnet, evap=fig_evap)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #bcd6f0; border-radius:2pt;
                  background:#eef5fd; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>16-bob — Laboratoriya amaliyoti</title><style>{css}</style>"]

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
  <div class="chapnum">16</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 16-bob · Mavzu pasporti (IV.1)</div>
  <h1>Laboratoriya amaliyoti</h1>
  <div class="lead">jihozlar va xavfsizlik · aralashmalarni ajratish usullari · eritma tayyorlash ·
  gazlar bilan ishlash · o'lchash aniqligi</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>jihozlarni tanish va to'g'ri ishlatish (A: 1, 17, 27)</li>
      <li>usul tanlash: filtr/bug'latish/haydash/voronka/magnit</li>
      <li>usul tuzoqlari: nima bilan ajratib BO'LMAYDI (B: 1, 7)</li>
      <li>eritma hisoblari: aralashtirish, suyultirish (B: 2, 15, 21, 27)</li>
      <li>ko'p bosqichli ajratish (B: 23, 36, 38)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>jihozlar paneli va apparatlar (A: 1, 15, 21; B: 19, 28)</li>
      <li>qizdirish egri chiziqlari (A: 26; B: 5, 26, 32)</li>
      <li>zichlik ustunlari va ajratish sxemasi (A: 28, 32; B: 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>eritmani filtrlash bilan «ajratish»</li>
      <li>suyultirishda eritma massasini unutish</li>
      <li>NH₃/HCl ni suv ustida yig'ish</li>
      <li>foizlarni to'g'ridan-to'g'ri qo'shish</li></ul></div>
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
