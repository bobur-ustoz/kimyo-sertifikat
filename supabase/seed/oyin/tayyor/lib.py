import json, subprocess, sys, os
def C(p, ok, no, w, uses=None, trap=None):
    v = {"p": p, "ok": ok, "no": no, "w": w}
    if uses: v["uses"] = uses
    if trap: v["trap"] = {"opt": trap[0], "why": trap[1]}
    return v
def W(p, re, pr, ans, w, uses=None, chain=None, bundle=None):
    v = {"p": p, "re": re, "pr": pr, "ans": ans, "w": w}
    if chain: v["chain"] = chain
    if bundle: v["bundle"] = bundle
    if uses: v["uses"] = uses
    return v
S = lambda slot, group, type, lvl, variants, bg=None: {"slot": slot, "group": group, "type": type, "lvl": lvl, **({"bundleGroup": bg} if bg else {}), "variants": variants}

def save(day, topic, substances, slots, n=None):
    d = {"version": 2, "day": day, "topic": topic, "substances": substances, "slots": slots}
    f = "kun_%02d.json" % day
    json.dump(d, open(f, "w"), ensure_ascii=False, indent=1)
    print(f, len(slots), "slots")
