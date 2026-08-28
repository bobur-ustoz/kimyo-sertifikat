# -*- coding: utf-8 -*-
"""variantlar/v02.json (yoki xuddi shu sxemadagi boshqa variant) dan
PDF ga tayyor, o'zi yetarli (self-contained) HTML yasaydi.

Ishlatish:
    python3 variantlar/pdf/build.py [variant.json] [chiqish.html]

    # PDF ga aylantirish (Chrome/Chromium kerak):
    chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \\
        --print-to-pdf=variant.pdf --run-all-compositor-stages-before-draw \\
        --virtual-time-budget=10000 "file://$(pwd)/exam_full.html"

    Diqqat: --print-to-pdf-no-header EMAS — bu Chrome tomonidan e'tiborsiz
    qoldiriladi va sarlavha/sana/URL footer PDF ga chiqib qoladi. To'g'ri
    flag: --no-pdf-header-footer.
"""
import json
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
ASSETS = os.path.join(REPO, "namuna", "assets")


def e(s):
    return html.escape(str(s), quote=False)


def split_o2_matn(matn):
    """s['matn'] ba'zan uchta qismdan iborat: kirish matni (prose),
    reaksiya sxemasi (bitta $\\ce{...->[n]...}$ qatori) va/yoki
    tajriba-natija jadvali (pipe '|' bilan ajratilgan qatorlar).
    Ularni alohida render qilish uchun ajratamiz."""
    intro, scheme, table_rows = [], [], []
    for raw in matn.split("\n"):
        ls = raw.strip()
        if not ls:
            continue
        if "|" in ls:
            table_rows.append(ls)
        elif "->[" in ls:
            scheme.append(ls)
        else:
            intro.append(ls)
    return intro, scheme, table_rows


def build_test_html(S):
    out = []
    add = out.append
    for s in S:
        n = s["n"]
        tur = s["tur"]
        if tur == "Y1":
            add(f'<div class="q"><span class="qn">{n}.</span> <span class="qtext">{s["savol"]}</span>')
            add('<div class="opts">')
            for i, v in enumerate(s["variantlar"]):
                letter = chr(65 + i)
                add(f'<span class="opt">{letter}) {v}</span>')
            add('</div></div>')
        elif tur == "Y2":
            last = n + len(s["savollar_ichki"]) - 1
            add('<div class="q y2block">')
            add(f'<div class="y2-instr">{n} &ndash; {last}-test topshiriqlariga mos keluvchi javob variantlarini (A &ndash; F) tanlang.</div>')
            add('<table class="y2table"><tbody>')
            opts_html = "<br>".join(s["javoblar_royxati"])
            rowspan = 1 + len(s["savollar_ichki"])
            add(f'<tr><td class="y2-scenario">{s["matn_umumiy"]}</td>'
                f'<td class="y2-opts" rowspan="{rowspan}">{opts_html}</td></tr>')
            for line in s["savollar_ichki"]:
                add(f'<tr><td class="y2-q">{line}</td></tr>')
            add('</tbody></table>')
            add('</div>')
        elif tur == "O1":
            add(f'<div class="q"><span class="qn">{n}.</span> <span class="qtext">{s["savol"]}</span>')
            add('<div class="blank">Javob: _______________________</div></div>')
        elif tur == "O2":
            intro, scheme, table_rows = split_o2_matn(s["matn"])
            add(f'<div class="q o2block"><span class="qn">{n}-topshiriq.</span> '
                f'<span class="qtext">{"<br>".join(intro)}</span>')
            if scheme:
                add(f'<div class="o2-scheme">{"<br>".join(scheme)}</div>')
            if table_rows:
                add('<table class="o2-table"><tbody>')
                for i, row in enumerate(table_rows):
                    cells = [c.strip() for c in row.split("|")]
                    tag = "th" if i == 0 else "td"
                    add('<tr>' + "".join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
                add('</tbody></table>')
            add('<ol class="o2list">')
            for b in s["bandlar"]:
                add(f'<li>{b["savol"]}</li>')
            add('</ol></div>')
    return "\n".join(out)


def build_answers_html(S):
    out = []
    add = out.append

    add('<h2>Javoblar kaliti</h2>')
    add('<table class="keytable"><thead><tr><th>№</th><th>Javob</th><th>№</th><th>Javob</th></tr></thead><tbody>')
    keys = []
    for s in S:
        if s["tur"] in ("Y1", "O1"):
            keys.append((s["n"], s["javob"]))
        elif s["tur"] == "Y2":
            for k, v in s["javoblar"].items():
                keys.append((int(k), v))
        elif s["tur"] == "O2":
            keys.append((s["n"], f'{s["jami"]} ball (bandlarga qarang)'))
    keys.sort()
    half = (len(keys) + 1) // 2
    for i in range(half):
        left = keys[i]
        right = keys[i + half] if i + half < len(keys) else None
        rtd = f'<td>{right[0]}</td><td>{right[1]}</td>' if right else '<td></td><td></td>'
        add(f'<tr><td>{left[0]}</td><td>{left[1]}</td>{rtd}</tr>')
    add('</tbody></table>')

    add("<h2>To'liq yechimlar va tekshiruv izohlari</h2>")
    for s in S:
        n = s["n"]
        tur = s["tur"]
        add(f'<div class="sol"><div class="sol-head">{n}-topshiriq ({tur}) — '
            f'{e(s.get("bolim",""))} bo\'limi, {e(s.get("element","") or "")}</div>')
        if tur == "Y1":
            add(f'<div class="sol-javob"><b>To\'g\'ri javob: {s["javob"]}</b></div>')
            add(f'<div class="sol-yechim">{s["yechim"]}</div>')
            add('<div class="sol-chalg"><b>Chalg\'ituvchilar:</b><ul>')
            for c in s["chalgituvchilar"]:
                add(f'<li><b>{c["variant"]})</b> {e(c["xato"])}</li>')
            add('</ul></div>')
        elif tur == "Y2":
            jj = s["javoblar"]
            add(f'<div class="sol-javob"><b>Javoblar: {n}-{jj[str(n)]}, {n+1}-{jj[str(n+1)]}, {n+2}-{jj[str(n+2)]}</b></div>')
            add(f'<div class="sol-yechim">{s["yechim"]}</div>')
        elif tur == "O1":
            add(f'<div class="sol-javob"><b>Javob: {s["javob"]}</b></div>')
            add(f'<div class="sol-yechim">{s["yechim"]}</div>')
        elif tur == "O2":
            add('<table class="bandtable"><thead><tr><th>Band</th><th>Yechim</th><th>M</th><th>A</th></tr></thead><tbody>')
            for b in s["bandlar"]:
                steps = "<br>".join(b["yechim"])
                add(f'<tr><td>{b["savol"]}</td><td>{steps}</td><td>{b["M"]}</td><td>{b["A"]}</td></tr>')
            m_sum = sum(b["M"] for b in s["bandlar"])
            a_sum = sum(b["A"] for b in s["bandlar"])
            add(f'<tr class="jami"><td colspan="2">Jami</td><td>{m_sum}</td><td>{a_sum}</td></tr>')
            add('</tbody></table>')
            add(f'<div class="sol-rasmiy"><b>Rasmiylashtirish:</b> {e(s["rasmiylashtirish"])}</div>')
        add('</div>')
    return "\n".join(out)


def main():
    json_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "variantlar", "v02.json")
    out_path = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(json_path)[0] + ".exam.html"

    d = json.load(open(json_path, encoding="utf-8"))
    S = d["savollar"]

    raw_name = d.get("variant", "variant")
    m = re.fullmatch(r"v0*(\d+)", raw_name)
    if m:
        display_name = f"{int(m.group(1))}-VARIANT"
    else:
        display_name = raw_name.replace("_", " ").replace("-", " ").upper()
    verify_script = f"verify_{raw_name.replace('-', '_')}.py" if raw_name else "verify_v02.py"

    counts = {"Y1": 0, "Y2": 0, "O1": 0, "O2": 0}
    for s in S:
        counts[s["tur"]] = counts.get(s["tur"], 0) + (3 if s["tur"] == "Y2" else 1)

    shell = open(os.path.join(HERE, "exam_shell.html"), encoding="utf-8").read()
    katex_css = open(os.path.join(ASSETS, "katex.inline.css"), encoding="utf-8").read()
    katex_js = open(os.path.join(ASSETS, "katex.min.js"), encoding="utf-8").read()
    mhchem_js = open(os.path.join(ASSETS, "mhchem.min.js"), encoding="utf-8").read()
    autorender_js = open(os.path.join(ASSETS, "auto-render.min.js"), encoding="utf-8").read()

    out = (shell
           .replace("__VARIANT_NAME__", e(display_name))
           .replace("__STRUCT__", f'{counts["Y1"]} Y1 &middot; {counts["Y2"]} Y2 &middot; {counts["O1"]} O1 &middot; {counts["O2"]} O2')
           .replace("__SRC__", e(os.path.relpath(json_path, REPO)))
           .replace("__VERIFY_SCRIPT__", e(verify_script))
           .replace("__TEST_CONTENT__", build_test_html(S))
           .replace("__ANSWERS_CONTENT__", build_answers_html(S))
           .replace("__KATEX_CSS__", katex_css)
           .replace("__KATEX_JS__", katex_js)
           .replace("__MHCHEM_JS__", mhchem_js)
           .replace("__AUTORENDER_JS__", autorender_js))

    open(out_path, "w", encoding="utf-8").write(out)
    print(f"Yozildi: {out_path} ({len(out)/1024/1024:.2f} MB)")
    print("PDF ga aylantirish uchun:")
    print(f'  chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \\')
    print(f'    --print-to-pdf=natija.pdf --run-all-compositor-stages-before-draw \\')
    print(f'    --virtual-time-budget=10000 "file://$(pwd)/{os.path.basename(out_path)}"')


if __name__ == "__main__":
    main()
