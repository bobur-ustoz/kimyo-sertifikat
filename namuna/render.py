# -*- coding: utf-8 -*-
"""Bob JSON faylini (Bobning JSON tuzilmasi sxemasi bo'yicha) o'z ichiga KaTeX +
mhchem bilan to'liq render qiladigan, ikki ustunli, o'zi yetarli (self-contained)
HTML sahifasiga aylantiradi. Internet kerak emas — barcha shrift/JS/CSS
assets/ papkasida inline holda saqlangan.

Ishlatish:
    python3 namuna/render.py namuna/I6-muvozanat.json  [chiqish.html]

Agar chiqish fayli ko'rsatilmasa, <bob>.preview.html nomi bilan saqlanadi.
"""
import sys
import json
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")


def e(s):
    return html.escape(str(s), quote=False)


def build_content(d):
    out = []

    def add(s):
        out.append(s)

    add(f'<div class="eyebrow">{e(d.get("bolim",""))} &middot; {e(d.get("element",""))} '
        f'&middot; savol o&#39;rni: {e(", ".join(d.get("savol_orni", [])))}</div>')
    add(f'<h1>{e(d["mavzu"])}</h1>')

    add('<h2 class="colspan">Ma&#39;ruza</h2>')
    for para in d.get("maruza", []):
        add(f'<p>{para}</p>')

    if d.get("asosiy_formulalar"):
        add('<h2 class="colspan">Asosiy formulalar</h2>')
        add('<table class="formulas"><tbody>')
        for fi in d["asosiy_formulalar"]:
            add(f'<tr><td class="fexpr">{fi["f"]}</td>'
                f'<td class="fnote">{e(fi["izoh"])}<span class="funit">{e(fi["birlik"])}</span></td></tr>')
        add('</tbody></table>')

    if d.get("tenglamalar"):
        add('<h2 class="colspan">Reaksiya tenglamalari</h2>')
        add('<ul class="eqlist">')
        for t in d["tenglamalar"]:
            add(f'<li>{t["tenglama"]} <span class="eqnote">&mdash; {e(t["sharoit"])}: {e(t["izoh"])}</span></li>')
        add('</ul>')

    if d.get("sifat_reaksiyalari"):
        add('<h2 class="colspan">Sifat reaksiyalari</h2>')
        add('<table class="formulas"><tbody>')
        for sr in d["sifat_reaksiyalari"]:
            add(f'<tr><td class="fexpr">{e(sr["reagent"])}</td>'
                f'<td class="fnote">{e(sr["belgi"])} &mdash; {sr.get("tenglama","")}</td></tr>')
        add('</tbody></table>')

    if d.get("eslatmalar"):
        add('<h2 class="colspan">Eslatmalar</h2>')
        add('<ul class="notes">')
        for n in d["eslatmalar"]:
            add(f'<li><b>{e(n["joy"])}.</b> {n["matn"]}</li>')
        add('</ul>')

    if d.get("xatolar"):
        add('<h2 class="colspan">Xatolar</h2>')
        add('<table class="errors"><thead><tr><th>Xato</th><th>Tuzatish</th></tr></thead><tbody>')
        for x in d["xatolar"]:
            add(f'<tr><td>{x["xato"]}</td><td>{x["tuzatish"]}</td></tr>')
        add('</tbody></table>')

    for ti, tip in enumerate(d.get("tiplar", []), 1):
        add(f'<h2 class="colspan tip-head">TIP {ti}. {e(tip["nom"])}</h2>')
        add(f'<p><b>Qoida:</b> {tip["qoida"]}</p>')
        add(f'<p><b>Formula:</b> {tip["formula"]}</p>')
        add(f'<p class="tez"><b>Tez yechish ({tip["vaqt_soniya"]} soniya):</b> {tip["tez_yechish"]}</p>')
        nm = tip["namuna"]
        add('<div class="namuna"><div class="namuna-head">NAMUNA</div>')
        add(f'<p>{nm["savol"]}</p>')
        add('<ol class="qadamlar">')
        for q in nm["qadamlar"]:
            add(f'<li>{q}</li>')
        add('</ol>')
        add(f'<p class="javob-line"><b>Javob:</b> {nm["javob"]}</p>')
        add(f'<p class="diqqat"><b>Diqqat.</b> {nm["izoh"]}</p></div>')
        add(f'<div class="mashq-label">MASHQLAR &mdash; {e(tip["topshiriq"])}</div>')
        add('<ol class="mashqlar">')
        for m in tip["mashqlar"]:
            add(f'<li>{m["savol"]} <span class="j">{m["javob"]}</span></li>')
        add('</ol>')
        if tip.get("A_daraja"):
            add('<div class="mashq-label astar">A DARAJA &#9733;</div>')
            add('<ol class="mashqlar astar">')
            for m in tip["A_daraja"]:
                add(f'<li>{m["savol"]} <span class="j">{m["javob"]}</span></li>')
            add('</ol>')

    if d.get("grafik_tahlil"):
        add('<h2 class="colspan">Grafik va jadval tahlili</h2>')
        for g in d["grafik_tahlil"]:
            add('<div class="grafik">')
            add(f'<p>{g["savol"]}</p>')
            add('<table class="datatable"><tbody>')
            for row in g["jadval"]:
                add('<tr>' + "".join(f'<td>{e(c)}</td>' for c in row) + '</tr>')
            add('</tbody></table>')
            add(f'<p class="javob-line"><b>Javob:</b> {g["javob"]}</p></div>')

    if d.get("yozma_ish"):
        yi = d["yozma_ish"]
        add(f'<h2 class="colspan">Yozma ish mashqi &mdash; {yi["tur"]}-topshiriq formatida</h2>')
        add(f'<p class="yozma-matn">{yi["matn"]}</p>')
        add('<table class="yozma"><thead><tr><th>Band</th><th>Yechim</th><th>M</th><th>A</th></tr></thead><tbody>')
        for b in yi["bandlar"]:
            steps = "<br>".join(b["yechim"])
            add(f'<tr><td class="band-q">{b["savol"]}</td><td class="band-y">{steps}</td>'
                f'<td class="pt">{b["M"]}</td><td class="pt">{b["A"]}</td></tr>')
        add(f'<tr class="jami-row"><td colspan="2">Jami</td>'
            f'<td class="pt">{sum(b["M"] for b in yi["bandlar"])}</td>'
            f'<td class="pt">{sum(b["A"] for b in yi["bandlar"])}</td></tr>')
        add('</tbody></table>')
        add(f'<p class="rasmiy"><b>Rasmiylashtirish.</b> {yi["rasmiylashtirish"]}</p>')

    if d.get("mashqlar_banki"):
        n = len(d["mashqlar_banki"])
        add(f'<h2 class="colspan">Mavzuviy mashqlar banki &mdash; {n} ta</h2>')
        add('<ol class="bank" start="1">')
        for m in d["mashqlar_banki"]:
            add(f'<li>{m["savol"]} <span class="j">{m["javob"]}</span></li>')
        add('</ol>')

    if d.get("xotira_kartalari"):
        add('<h2 class="colspan">Xotira kartalari</h2>')
        add('<ul class="xotira">')
        for x in d["xotira_kartalari"]:
            add(f'<li>{x}</li>')
        add('</ul>')

    if d.get("test"):
        note = d.get("test_izoh", "")
        add(f'<h2 class="colspan">Yakuniy test <span class="test-note">({e(note)})</span></h2>')
        for i, t in enumerate(d["test"], 1):
            add('<div class="testq">')
            add(f'<p><b>{i}.</b> {t["matn"]}</p>')
            if t.get("variantlar"):
                add('<div class="variantlar">')
                for j, v in enumerate(t["variantlar"]):
                    letter = chr(65 + j)
                    cls = "correct" if letter == t["javob"] else ""
                    add(f'<span class="opt {cls}">{letter}) {v}</span>')
                add('</div>')
            else:
                add(f'<p class="javob-line"><b>Javob:</b> {t["javob"]}</p>')
            if t.get("chalgituvchilar"):
                add('<ul class="chalg">')
                for c in t["chalgituvchilar"]:
                    add(f'<li><b>{c["variant"]})</b> {c["xato"]}</li>')
                add('</ul>')
            add(f'<p class="yechim-line">{t["yechim"]}</p></div>')

    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    json_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else (
        os.path.splitext(json_path)[0] + ".preview.html"
    )

    d = json.load(open(json_path, encoding="utf-8"))
    content = build_content(d)

    shell = open(os.path.join(ASSETS, "page_shell.html"), encoding="utf-8").read()
    katex_css = open(os.path.join(ASSETS, "katex.inline.css"), encoding="utf-8").read()
    katex_js = open(os.path.join(ASSETS, "katex.min.js"), encoding="utf-8").read()
    mhchem_js = open(os.path.join(ASSETS, "mhchem.min.js"), encoding="utf-8").read()
    autorender_js = open(os.path.join(ASSETS, "auto-render.min.js"), encoding="utf-8").read()

    note = d.get("izoh_holat") or (
        f'Promtdagi (<code>PROMT_KIMYO.md</code>) "Kitob formati" bo\'yicha yozilgan bob: '
        f'{e(d.get("element",""))} &mdash; {e(d["mavzu"])}. Barcha sonli javoblar mustaqil '
        f'usullar bilan tekshirilgan.'
    )

    out = (shell
           .replace("__CONTENT__", content)
           .replace("__TOPBAR_NOTE__", note)
           .replace("__KATEX_CSS__", katex_css)
           .replace("__KATEX_JS__", katex_js)
           .replace("__MHCHEM_JS__", mhchem_js)
           .replace("__AUTORENDER_JS__", autorender_js))

    open(out_path, "w", encoding="utf-8").write(out)
    print(f"Yozildi: {out_path} ({len(out)/1024/1024:.2f} MB)")
    print("Diqqat: bu faylni to'g'ridan-to'g'ri ochsangiz (file://), brauzer "
          "<!doctype> yo'qligi sababli 'quirks mode'ga o'tib, KaTeX ishlamay "
          "qolishi mumkin. Artifact sifatida nashr qilinganda muammo yo'q "
          "(harness o'zi <!doctype html> bilan o'raydi); mahalliy tekshirish "
          "uchun faylni <!doctype html><html><head>"
          "<meta charset=\"utf-8\"></head><body>...</body></html> ichiga "
          "vaqtincha o'rab ko'ring.")


if __name__ == "__main__":
    main()
