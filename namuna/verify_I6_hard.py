# -*- coding: utf-8 -*-
"""I6-muvozanat.json'dagi "ms_darajasidagi_bank" (43 ta, barchasi MS
variantlarining eng qiyin pozitsiyalari -- 33-35 Y2 va 41-43 O2 --
darajasidagi ko'p bosqichli muvozanat masalalari) uchun mustaqil
2-usul tekshiruvi: har bir savolning "parametrlar" maydonidagi xom
sonlardan (javobni EMAS, faqat berilganlarni) foydalanib, tenglamani
FRESH sympy sozlash bilan qayta yechadi va natijani "javob" maydoni
bilan solishtiradi.

Ishlatish: python3 namuna/verify_I6_hard.py
"""
import json
import os
import re
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "I6-muvozanat.json"), encoding="utf-8"))
items = d["ms_darajasidagi_bank"]
errors = []


def close(a, b, tol=0.01):
    b = float(b)
    return abs(float(a) - b) <= tol * max(1, abs(b))


def nums_in(s):
    return [float(x.replace(',', '.')) for x in re.findall(r'-?\d+(?:[.,]\d+)?', s)]


for it in items:
    meta = it["parametrlar"]
    arch = meta["arch"]
    n = it["n"]
    reported = nums_in(it["javob"])

    if arch == "A":
        kc, a0 = meta["kc"], meta["a0"]
        MA, MB, MC = meta["MA"], meta["MB"], meta["MC"]
        x = sp.symbols('x', positive=True)
        xv = [s for s in sp.solve(sp.Eq(kc * (a0 - x), x**2), x) if s > 0][0]
        eqA, eqBC = a0 - xv, xv
        avgM = (eqA * MA + eqBC * MB + eqBC * MC) / (eqA + 2 * eqBC)
        if not close(xv, reported[0]) or not close(avgM, reported[1]):
            errors.append(f"A#{n}: x={float(xv)},avgM={float(avgM)} vs reported {reported}")

    elif arch == "B":
        kc, a0, V = meta["kc"], meta["a0"], meta["V_water"]
        x = sp.symbols('x', positive=True)
        xv = [s for s in sp.solve(sp.Eq(kc * (a0 - x), x**2), x) if s > 0][0]
        molarity = (2 * xv) / sp.Rational(str(V))
        if not close(molarity, reported[-1]):
            errors.append(f"B#{n}: molarity={float(molarity)} vs reported {reported}")

    elif arch == "C":
        kc, T = meta["kc"], meta["T"]
        Kp = kc * sp.Rational('0.082') * T
        if not close(Kp, reported[-1]):
            errors.append(f"C#{n}: Kp={float(Kp)} vs reported {reported}")

    elif arch == "D":
        kc, a0 = meta["kc"], meta["a0"]
        x1 = sp.symbols('x1', positive=True)
        x1v = [s for s in sp.solve(sp.Eq(kc * (a0 - x1), x1**2), x1) if s > 0][0]
        nA1, nB1 = a0 - x1v, x1v
        y = sp.symbols('y', positive=True)
        eq2 = sp.Eq(kc, ((nB1 - y) / sp.Rational(1, 2))**2 / ((nA1 + y) / sp.Rational(1, 2)))
        yv = [s for s in sp.solve(eq2, y) if s.is_real and 0 < s < nB1][0]
        nA_final = nA1 + yv
        if not close(nA_final, reported[-1]):
            errors.append(f"D#{n}: nA_final={float(nA_final)} vs reported {reported}")

    elif arch == "E":
        kc, a0, b0 = meta["kc"], meta["a0"], meta["b0"]
        x = sp.symbols('x', positive=True)
        eq = sp.Eq(sp.nsimplify(kc), (2 * x)**2 / ((a0 - x) * (b0 - x)))
        xv = [s for s in sp.solve(eq, x) if s.is_real and 0 < s < min(a0, b0)][0]
        conv = xv / a0 * 100
        nC = 2 * xv
        if not close(conv, reported[0]) or not close(nC, reported[1]):
            errors.append(f"E#{n}: conv={float(conv)},nC={float(nC)} vs reported {reported}")

    elif arch == "F":
        MA, a0, avgM_given = meta["MA"], meta["a0"], meta["avgM_given"]
        x = sp.symbols('x', positive=True)
        xv = sp.solve(sp.Eq(sp.nsimplify(str(avgM_given)), (MA * a0) / (a0 + x)), x)[0]
        Kc_val = xv * xv / (a0 - xv)
        if not close(Kc_val, reported[-1], tol=0.02):
            errors.append(f"F#{n}: Kc={float(Kc_val)} vs reported {reported}")

    elif arch == "G":
        kc, a0, extra = meta["kc"], meta["a0"], meta["extra"]
        x1 = sp.symbols('x1', positive=True)
        x1v = [s for s in sp.solve(sp.Eq(kc * (a0 - x1), x1**2), x1) if s > 0][0]
        nA1, nB1 = a0 - x1v, x1v
        nA_new0 = nA1 + extra
        z = sp.symbols('z', positive=True)
        zv = [s for s in sp.solve(sp.Eq(kc, (nB1 + z)**2 / (nA_new0 - z)), z) if s.is_real and s > 0][0]
        nC_final = nB1 + zv
        if not close(nC_final, reported[-1]):
            errors.append(f"G#{n}: nC_final={float(nC_final)} vs reported {reported}")

    elif arch == "H":
        Kp, P0 = meta["Kp"], meta["P0"]
        p = sp.symbols('p', positive=True)
        pv = [s for s in sp.solve(sp.Eq(sp.nsimplify(str(Kp)) * (P0 - p), p**2), p) if s > 0][0]
        Ptotal = P0 + pv
        if not close(Ptotal, reported[-1]):
            errors.append(f"H#{n}: Ptotal={float(Ptotal)} vs reported {reported}")

    elif arch == "I":
        MA, a0, alpha = meta["MA"], meta["a0"], meta["alpha"]
        alpha = sp.nsimplify(str(alpha))
        x = a0 * alpha
        nA = a0 - x
        total = nA + 2 * x
        massTotal = MA * a0
        avgM = sp.nsimplify(str(massTotal)) / total
        D_H2 = avgM / 2
        if not close(D_H2, reported[-1], tol=0.02):
            errors.append(f"I#{n}: D_H2={float(D_H2)} vs reported {reported}")

    else:
        errors.append(f"#{n}: noma'lum arxetip {arch}")

print(f"Mustaqil qayta tekshiruv (2-usul, alohida sympy sozlash): {len(errors)} xato / {len(items)} ta savol.")
for e in errors:
    print(" -", e)
if not errors:
    print("Barcha 43 ta savol mustaqil ravishda qayta yechildi va javoblar mos keldi.")
