# -*- coding: utf-8 -*-
"""3-bob (Kimyoviy reaksiya turlari va issiqlik effekti) — kitob dizaynidagi bob-PDF: pasport + A-variant + B-variant, har biri kaliti bilan."""
import json, html

data_A = json.load(open("mavzu_I3A.json", encoding="utf-8"))
data_B = json.load(open("mavzu_I3B.json", encoding="utf-8"))
ACCENT, DARK, TINT, ACCENT2 = "#a93226", "#78281f", "#fdf3f0", "#1f618d"

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
            f'{km}<path d="{p}" fill="none" stroke="#a93226" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ---------- I.3 figuralari (g'isht-qizil palitrasi) ----------
I1, I2, ID, IP, IG = "#a93226", "#1f618d", "#78281f", "#fdf5f2", "#edd6d0"

def fig_profile():
    """Energiya diagrammasi: reagent 200, cho'qqi 350, mahsulot 120 kJ (ekzo)."""
    def y(E): return 140 - E * 0.31
    yr, yp, ym = y(200), y(350), y(120)
    return ('<svg width="260" height="158" viewBox="0 0 260 158">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="30" y="6" width="220" height="140" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            f'<line x1="30" y1="146" x2="252" y2="146" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="30" y1="146" x2="30" y2="8" stroke="{ID}" stroke-width="1.4"/>'
            f'<line x1="34" y1="{yr:.0f}" x2="86" y2="{yr:.0f}" stroke="{I1}" stroke-width="2.6"/>'
            f'<path d="M86,{yr:.0f} C120,{yp+4:.0f} 128,{yp:.0f} 144,{yp+8:.0f} C166,{yp+26:.0f} 172,{ym:.0f} 196,{ym:.0f}" '
            f'fill="none" stroke="{I1}" stroke-width="2" stroke-dasharray="1,0"/>'
            f'<line x1="196" y1="{ym:.0f}" x2="246" y2="{ym:.0f}" stroke="{I2}" stroke-width="2.6"/>'
            f'<line x1="34" y1="{yr:.0f}" x2="246" y2="{yr:.0f}" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<line x1="140" y1="{yp+6:.0f}" x2="246" y2="{yp+6:.0f}" stroke="{IG}" stroke-width="0.9" stroke-dasharray="3,3"/>'
            f'<text x="36" y="{yr-4:.0f}" class="lb" font-weight="bold">reagentlar · 200 kJ</text>'
            f'<text x="160" y="{ym+12:.0f}" class="lb" font-weight="bold" fill="{I2}">mahsulotlar · 120 kJ</text>'
            f'<text x="96" y="{yp-2:.0f}" class="lb" font-weight="bold">cho\'qqi · 350 kJ</text>'
            f'<text x="8" y="16" class="lb">E</text>'
            '<text x="168" y="156" class="lb">reaksiya yo\'nalishi</text></svg>')

def fig_bar_yonish():
    """Yonish issiqliklari (kJ/mol): CH4, C2H6, C3H8 — ustunlar."""
    data = [("CH₄", 890), ("C₂H₆", 1560), ("C₃H₈", 2220)]
    mx = 2400
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 58; h = v / mx * 116; y = 130 - h
        col = I1 if i % 2 == 0 else I2
        bars += (f'<rect x="{x}" y="{y:.0f}" width="34" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+17}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+17}" y="143" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="152" viewBox="0 0 250 152">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="198" height="126" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{130-g/2400*116:.0f}" x2="242" y2="{130-g/2400*116:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      for g in [800, 1600])
            + bars +
            f'<line x1="46" y1="130" x2="244" y2="130" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">Q, kJ/mol</text></svg>')

def fig_bar_fuel():
    """1 g yoqilg'i uchun issiqlik (kJ/g): ko'mir, metan, vodorod."""
    data = [("ko'mir", 33), ("metan", 55), ("vodorod", 143)]
    mx = 160
    bars = ""
    for i, (lab, v) in enumerate(data):
        x = 62 + i * 58; h = v / mx * 116; y = 130 - h
        col = I2 if i == 2 else I1
        bars += (f'<rect x="{x}" y="{y:.0f}" width="34" height="{h:.0f}" rx="2" fill="{col}" opacity="0.85" '
                 f'stroke="{ID}" stroke-width="0.9"/>'
                 f'<text x="{x+17}" y="{y-4:.0f}" text-anchor="middle" class="lb" font-weight="bold">{v}</text>'
                 f'<text x="{x+17}" y="143" text-anchor="middle" class="lb">{lab}</text>')
    return ('<svg width="250" height="152" viewBox="0 0 250 152">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="46" y="4" width="198" height="126" rx="4" fill="{IP}" stroke="{IG}" stroke-width="1.1"/>'
            + "".join(f'<line x1="48" y1="{130-g/160*116:.0f}" x2="242" y2="{130-g/160*116:.0f}" stroke="{IG}" stroke-width="0.9"/>'
                      f'<text x="30" y="{133-g/160*116:.0f}" class="lb">{g}</text>' for g in [50, 100, 150])
            + bars +
            f'<line x1="46" y1="130" x2="244" y2="130" stroke="{ID}" stroke-width="1.5"/>'
            '<text x="4" y="14" class="lb">kJ/g</text></svg>')

def fig_calorimeter():
    """Kalorimetr: tashqi idish, suvli stakan, termometr, aralashtirgich, yoqilg'i idishi."""
    return ('<svg width="250" height="150" viewBox="0 0 250 150">'
            f'<style>.lb{{font-size:8.2px;font-family:Georgia,serif;fill:{ID}}}</style>'
            # tashqi idish
            f'<rect x="52" y="30" width="104" height="104" rx="6" fill="none" stroke="{ID}" stroke-width="2"/>'
            # ichki stakan suv bilan
            f'<rect x="66" y="44" width="76" height="86" rx="4" fill="none" stroke="{I1}" stroke-width="1.6"/>'
            f'<rect x="68" y="66" width="72" height="62" fill="{I2}" opacity="0.18"/>'
            f'<line x1="68" y1="66" x2="140" y2="66" stroke="{I2}" stroke-width="1.2"/>'
            # yoqilg'i kosachasi va alanga
            f'<rect x="94" y="112" width="20" height="10" rx="2" fill="{IP}" stroke="{I1}" stroke-width="1.2"/>'
            f'<path d="M104,110 q-5,-8 0,-14 q5,6 0,14" fill="{I1}"/>'
            # termometr
            f'<line x1="88" y1="14" x2="88" y2="96" stroke="{ID}" stroke-width="3.6"/>'
            f'<circle cx="88" cy="98" r="4.6" fill="{I1}"/>'
            # aralashtirgich
            f'<line x1="122" y1="16" x2="122" y2="88" stroke="{I2}" stroke-width="2.4"/>'
            f'<path d="M114,88 h16" stroke="{I2}" stroke-width="2.4"/>'
            # yorliqlar
            '<text x="162" y="26" class="lb" font-weight="bold">termometr</text>'
            f'<path d="M160,23 q-30,-6 -66,-4" fill="none" stroke="{IG}" stroke-width="1"/>'
            '<text x="162" y="60" class="lb">aralashtirgich</text>'
            '<text x="162" y="90" class="lb">suv (500 g)</text>'
            '<text x="162" y="120" class="lb">yoqilg\'i namunasi</text>'
            '<text x="52" y="146" class="lb" font-weight="bold">kalorimetr</text></svg>')

def fig_scheme38():
    """B O1-38: sxema — metan yonishi → issiqlik → suvni isitish."""
    return ('<svg width="270" height="96" viewBox="0 0 270 96">'
            f'<style>.lb{{font-size:8.4px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="8" y="26" width="76" height="42" rx="4" fill="{IP}" stroke="{I1}" stroke-width="1.6"/>'
            '<text x="46" y="43" text-anchor="middle" class="lb" font-weight="bold">yonish kamerasi</text>'
            '<text x="46" y="56" text-anchor="middle" class="lb">CH₄ + 2O₂ → ...</text>'
            f'<line x1="84" y1="47" x2="122" y2="47" stroke="{I1}" stroke-width="2"/>'
            f'<polygon points="126,47 118,43 118,51" fill="{I1}"/>'
            f'<text x="88" y="39" class="lb" font-weight="bold" fill="{I1}">issiqlik</text>'
            f'<rect x="128" y="26" width="86" height="42" rx="4" fill="{IP}" stroke="{I2}" stroke-width="1.6"/>'
            '<text x="171" y="43" text-anchor="middle" class="lb" font-weight="bold">5 kg suv</text>'
            '<text x="171" y="56" text-anchor="middle" class="lb">20 °C → 62,4 °C</text>'
            f'<line x1="214" y1="47" x2="244" y2="47" stroke="{ID}" stroke-width="1.6"/>'
            f'<polygon points="248,47 240,43 240,51" fill="{ID}"/>'
            '<text x="222" y="39" class="lb" font-weight="bold">? L CH₄</text></svg>')

def fig_candle():
    """Sham: alanga, erigan parafin, yorug'lik nurlari."""
    return ('<svg width="220" height="128" viewBox="0 0 220 128">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            '<rect x="86" y="52" width="26" height="60" rx="3" fill="#f7ead7" stroke="#c9b28a" stroke-width="1.2"/>'
            '<path d="M86,52 q13,6 26,0 v6 q-13,6 -26,0 z" fill="#eeddc0"/>'
            '<line x1="99" y1="52" x2="99" y2="42" stroke="#555" stroke-width="1.6"/>'
            f'<path d="M99,44 q-7,-11 0,-22 q7,11 0,22" fill="#f4c542" stroke="{I1}" stroke-width="1.2"/>'
            f'<path d="M99,40 q-3,-5 0,-10 q3,5 0,10" fill="{I1}" opacity="0.75"/>'
            + "".join(f'<line x1="{99+dx}" y1="{30+dy}" x2="{99+dx*1.8}" y2="{30+dy*1.8}" stroke="#f4c542" stroke-width="1.4"/>'
                      for dx, dy in [(-16, -4), (16, -4), (-11, -13), (11, -13), (0, -17)])
            + f'<text x="128" y="34" class="lb" font-weight="bold" fill="{I1}">issiqlik + yorug\'lik</text>'
            '<text x="128" y="47" class="lb">parafin + O₂ →</text>'
            '<text x="128" y="59" class="lb">CO₂ + H₂O + Q</text>'
            '<text x="52" y="124" class="lb" font-weight="bold">yonayotgan sham — ekzotermik jarayon</text></svg>')

def fig_coldpack():
    """Muzlatuvchi paket: xaltacha, qor uchqunlari, harorat pasayishi."""
    return ('<svg width="230" height="122" viewBox="0 0 230 122">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="30" y="26" width="84" height="66" rx="10" fill="#eaf2fb" stroke="{I2}" stroke-width="1.8"/>'
            f'<path d="M30,40 q42,10 84,0" fill="none" stroke="{I2}" stroke-width="1" stroke-dasharray="3,3"/>'
            '<text x="72" y="62" text-anchor="middle" class="lb" font-weight="bold">NH₄NO₃ + H₂O</text>'
            '<text x="72" y="76" text-anchor="middle" class="lb">erish · −Q</text>'
            + "".join(f'<text x="{x}" y="{y}" font-size="10" fill="#7fb3e0">❄</text>'
                      for x, y in [(36, 22), (104, 20), (120, 46), (20, 66), (118, 84)])
            + f'<line x1="150" y1="30" x2="150" y2="88" stroke="{ID}" stroke-width="3"/>'
            f'<circle cx="150" cy="92" r="5" fill="{I2}"/>'
            f'<polygon points="150,78 145,66 155,66" fill="{I2}"/>'
            '<text x="162" y="52" class="lb" font-weight="bold">harorat</text>'
            '<text x="162" y="64" class="lb" font-weight="bold">pasayadi</text>'
            '<text x="30" y="116" class="lb" font-weight="bold">muzlatuvchi paket — endotermik erish</text></svg>')

def fig_handwarmer():
    """Qo'l isitgich: xaltacha, Fe kukuni, iliqlik to'lqinlari."""
    return ('<svg width="230" height="120" viewBox="0 0 230 120">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<rect x="34" y="34" width="88" height="60" rx="12" fill="{IP}" stroke="{I1}" stroke-width="1.8"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#8d6e63"/>'
                      for x, y in [(56, 56), (70, 66), (86, 54), (98, 70), (62, 78), (92, 82), (78, 60)])
            + '<text x="78" y="48" text-anchor="middle" class="lb">Fe kukuni + O₂</text>'
            + "".join(f'<path d="M{x},30 q4,-6 0,-12 q-4,-6 0,-12" fill="none" stroke="{I1}" stroke-width="1.6" stroke-linecap="round"/>'
                      for x in [56, 78, 100])
            + f'<text x="136" y="46" class="lb" font-weight="bold" fill="{I1}">iliqlik (+Q)</text>'
            '<text x="136" y="60" class="lb">4Fe + 3O₂ →</text>'
            '<text x="136" y="72" class="lb">2Fe₂O₃ + Q</text>'
            '<text x="36" y="112" class="lb" font-weight="bold">qo\'l isitgich — sekin oksidlanish</text></svg>')

def fig_bread():
    """Novvoyxona: tandirdagi non va CO2 pufakchalari."""
    return ('<svg width="230" height="118" viewBox="0 0 230 118">'
            f'<style>.lb{{font-size:8.6px;font-family:Georgia,serif;fill:{ID}}}</style>'
            f'<path d="M34,92 a44,30 0 0 1 88,0 z" fill="#e8b04b" stroke="#b3762a" stroke-width="1.6"/>'
            '<path d="M52,78 q8,-6 16,0 M76,72 q8,-6 16,0" fill="none" stroke="#b3762a" stroke-width="1.4"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{I2}" stroke-width="1.2"/>'
                      for x, y, r in [(140, 54, 4), (152, 40, 5), (166, 28, 6)])
            + f'<text x="176" y="24" class="lb" font-weight="bold" fill="{I2}">CO₂</text>'
            '<text x="134" y="76" class="lb">2NaHCO₃ →</text>'
            '<text x="134" y="88" class="lb">Na₂CO₃+H₂O+CO₂</text>'
            '<text x="34" y="112" class="lb" font-weight="bold">soda xamirni CO₂ bilan ko\'pchitadi</text></svg>')

FIGS = dict(profile=fig_profile, bar_yonish=fig_bar_yonish, bar_fuel=fig_bar_fuel,
            calorimeter=fig_calorimeter, scheme38=fig_scheme38, candle=fig_candle,
            coldpack=fig_coldpack, handwarmer=fig_handwarmer, bread=fig_bread)

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
.gopts .go svg {{ display:block; margin: 0 auto 0.6mm; border:0.8pt solid #e0c4bd; border-radius:2pt;
                  background:#fdf5f2; padding:1mm;}}
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
H = [f"<meta charset='utf-8'><title>3-bob — Reaksiya turlari va issiqlik effekti</title><style>{css}</style>"]

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
  <div class="chapnum">3</div>
  <div class="kicker">1-kitob · Anorganik kimyo · 3-bob · Mavzu pasporti (I.3)</div>
  <h1>Kimyoviy reaksiya turlari va issiqlik effekti</h1>
  <div class="lead">birikish · parchalanish · o'rin olish · almashinish · ekzo/endotermik jarayonlar ·
  termokimyoviy tenglamalar va Gess qonuni</div>
  <div class="pass">
    <div class="card"><h3>Nimalarni tekshiradi</h3><ul>
      <li>reaksiya turini tenglamadan aniqlash</li>
      <li>termokimyoviy hisob: Q ↔ mol ↔ massa ↔ hajm</li>
      <li>teskari va aralashma masalalari (B: 2, 23, 40)</li>
      <li>Gess qonuni va hosil bo'lish issiqligi (B: 3, 25, 39)</li>
      <li>kalorimetrik hisob: Q = mcΔt (B: 19, 41)</li></ul></div>
    <div class="card"><h3>Vizual ko'nikmalar</h3><ul>
      <li>energiya diagrammasi: Q va Eₐ (A: 24, 32; B: 5, 28, 32)</li>
      <li>yonish issiqliklari ustunlari (A: 26; B: 26, 43)</li>
      <li>kalorimetr qurilmasi va sxema-masala (B: 19, 38)</li></ul></div>
    <div class="card"><h3>Tez-tez uchraydigan xatolar</h3><ul>
      <li>Q ni tenglama koeffitsiyentiga bo'lmaslik</li>
      <li>«−Q» ni ajralish deb o'qish</li>
      <li>o'rin olishni almashinish bilan adashtirish</li>
      <li>Eₐ ni issiqlik effekti deb olish</li></ul></div>
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
