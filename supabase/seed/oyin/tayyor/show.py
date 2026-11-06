import json, re, sys, html
d = json.load(open(sys.argv[1]))
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
def rich(s):
    s = html.escape(s).replace("&lt;sub&gt;", "<sub>").replace("&lt;/sub&gt;", "</sub>")
    return re.sub(r"[₀-₉]+", lambda m: "<sub>" + m.group(0).translate(SUB) + "</sub>", s)
def eq(s):
    out, prev, sub = "", "", False
    for ch in s:
        if ch.isdigit():
            sub = bool(re.match(r"[A-Za-z)]", prev)) or (sub and prev.isdigit())
            out += f"<sub>{ch}</sub>" if sub else ch
        else:
            sub = False; out += (" " + ch + " ") if ch in "+→" else ch
        prev = ch
    return out
lv = {1: "1-daraja", 2: "2-daraja", 3: "3-daraja"}
h = [f"<html><head><meta charset=utf-8><style>body{{font:13px/1.45 Helvetica,Arial,sans-serif;margin:28px;color:#111}}h1{{font-size:22px}}h2{{font-size:15px;margin:22px 0 6px;color:#0056D2;border-bottom:1px solid #ccd;padding-bottom:3px}}.s{{margin:8px 0 12px;page-break-inside:avoid}}.sh{{font-weight:bold;font-size:12px;color:#555}}.v{{margin:4px 0 6px 12px;padding:6px 10px;border-left:3px solid #bcd}}.ok{{color:#0a7a3a;font-weight:bold}}.no{{color:#555}}.w{{color:#555;font-size:12px;margin-top:3px}}.t{{color:#a05a00;font-size:12px}}.q{{font-weight:bold}}</style></head><body><h1>{d['day']}-kun · {d['topic']}</h1><p>{len(d['slots'])} o'rin, har birida 2–3 variant (o'quvchiga bittasi tushadi). Yashil = to'g'ri javob.</p>"]
cur = None
for s in d["slots"]:
    if s["group"] != cur:
        cur = s["group"]; h.append(f"<h2>{html.escape(cur)}</h2>")
    h.append(f"<div class=s><div class=sh>{s['slot']} · {lv[s['lvl']]} · {'tanlov' if s['type']=='choice' else 'yozma' if s['type']=='write' else 'yig‘ish'}</div>")
    for v in s["variants"]:
        h.append(f"<div class=v><div class=q>{rich(v['p'])}</div>")
        if s["type"] == "choice":
            h.append(f"<div class=ok>✔ {rich(v['ok'])}</div><div class=no>✘ " + " &nbsp;·&nbsp; ".join(rich(x) for x in v["no"]) + "</div>")
            if v.get("trap"): h.append(f"<div class=t>Tuzoq: «{rich(v['trap']['opt'])}» — {rich(v['trap']['why'])}</div>")
        elif s["type"] == "write":
            h.append(f"<div class=ok>✔ {eq(v['ans'])}</div>")
        else:
            h.append(f"<div class=ok>✔ {rich(v['build'])}</div>")
        h.append(f"<div class=w>{rich(v['w'])}</div></div>")
    h.append("</div>")
h.append("</body></html>")
open(sys.argv[2], "w").write("".join(h))
