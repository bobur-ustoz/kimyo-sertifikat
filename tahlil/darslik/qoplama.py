#!/usr/bin/env python3
"""Maktab darsliklari 27 ta mazmun elementini qay darajada qoplashini ko'rsatadi.

Ishlatish:  python3 tahlil/darslik/qoplama.py
Yangi sinf darsligi kelganda sNN.json qo'shiladi — skript qolganini o'zi qiladi.
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chastota import ELEMENTLAR, TARTIB, yukla as yukla_variantlar, hisobla  # noqa: E402

DARAJA = {"tanish": 2, "yuzaki": 1, "yoq": 0}
BELGI = {2: "tanish", 1: "yuzaki", 0: "YO'Q"}


def yukla_sinflar(katalog):
    sinflar = []
    for f in sorted(glob.glob(os.path.join(katalog, "s*.json"))):
        with open(f, encoding="utf-8") as fh:
            sinflar.append(json.load(fh))
    return sinflar


def qoplama(sinflar):
    """element -> {sinf: eng yuqori chuqurlik}"""
    q = {e: {} for e in TARTIB}
    for d in sinflar:
        s = d["sinf"]
        yozuvlar = [m for b in d["boblar"] for m in b["mavzular"]]
        yozuvlar += d.get("laboratoriya", [])
        for m in yozuvlar:
            e = m["element"]
            if e not in q:
                continue
            yangi = DARAJA.get(m.get("chuqurlik", "tanish"), 2)
            q[e][s] = max(q[e].get(s, 0), yangi)
    return q


def main():
    katalog = os.path.dirname(os.path.abspath(__file__))
    sinflar = yukla_sinflar(katalog)
    if not sinflar:
        raise SystemExit("sNN.json topilmadi")
    bor = sorted(d["sinf"] for d in sinflar)
    yoq = [s for s in (7, 8, 9, 10, 11) if s not in bor]
    print(f"Darsliklar: {bor}" + (f"  |  yetishmaydi: {yoq}" if yoq else ""))

    variantlar = yukla_variantlar(os.path.dirname(katalog))
    asosiy, qamrov, _, _ = hisobla(variantlar) if variantlar else ({}, {}, {}, {})

    q = qoplama(sinflar)
    print()
    print("Element".ljust(7) + "".join(f"{s}-s".rjust(8) for s in bor)
          + "Imtihon".rjust(9) + "  Mavzu")
    print("-" * 100)
    xavf = []
    for e in TARTIB:
        hujayralar = "".join(BELGI[q[e].get(s, 0)].rjust(8) for s in bor)
        savol = asosiy.get(e, 0)
        print(f"{e:<7}{hujayralar}{savol:>9}  {ELEMENTLAR[e]}")
        if savol and max(q[e].values() or [0]) == 0:
            xavf.append((e, savol))
    if xavf:
        print("\nXAVF — imtihonda bor, mavjud darsliklarda umuman yo'q:")
        for e, savol in sorted(xavf, key=lambda x: -x[1]):
            print(f"  {e:<7} {savol} ta savol   {ELEMENTLAR[e]}")
        print("\n  (Bu elementlar yetishmayotgan sinf darsliklarida bo'lishi mumkin.)")


if __name__ == "__main__":
    main()
