# -*- coding: utf-8 -*-
"""variantlar/mavzu_I6.json dagi barcha SONLI javoblarni mustaqil
(formuladan to'g'ridan-to'g'ri qayta hisoblab) tekshiradi. Sifat/nazariy
savollar (6,7,8,14,15,20,27,28,30,31,32, Y2 yo'q, O2#43 hammasi sifat)
kimyoviy mantiq bilan qo'lda tekshiriladi, skriptga kiritilmagan.

Ishlatish: python3 variantlar/verify_mavzu_I6.py
"""
import json
import os
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "mavzu_I6.json"), encoding="utf-8"))
S = {s["n"]: s for s in d["savollar"] if s["tur"] == "Y1"}
errors = []


def check(label, expected, actual, tol=1e-6):
    if abs(float(expected) - float(actual)) > tol:
        errors.append(f"{label}: kutilgan {expected}, natija {actual}")


def javob_text(n):
    s = S[n]
    return s["variantlar"][ord(s["javob"]) - ord("A")]


# ---- 1: N2+3H2<=>2NH3 ----
check("1", "1800", Fr('0.6')**2 / (Fr('0.2') * Fr('0.1')**3))
# ---- 2: H2+I2<=>2HI ----
check("2", "16", Fr('0.4')**2 / (Fr('0.1') * Fr('0.1')))
# ---- 3: 2SO2+O2<=>2SO3 ----
check("3", "40", Fr('0.4')**2 / (Fr('0.2')**2 * Fr('0.1')))
# ---- 4: PCl5<=>PCl3+Cl2, a0=6,Kc=1 -> eqA ----
x = sp.symbols('x', positive=True)
x4 = [s for s in sp.solve(sp.Eq(1 * (6 - x), x**2), x) if s > 0][0]
check("4", "4", 6 - x4)
# ---- 5: CO+H2O<=>CO2+H2 ----
check("5", "0.4", 4 * Fr('0.2') * Fr('0.3') / Fr('0.6'))
# ---- 9: 2NO<=>N2+O2 ----
check("9", "4", (Fr('0.4') * Fr('0.4')) / Fr('0.2')**2)
# ---- 10: N2O4<=>2NO2, 40% dissoc, [NO2]=0.8 -> a0 ----
a0 = sp.symbols('a0', positive=True)
check("10", "1", sp.solve(sp.Eq(2 * Fr('0.4') * a0, Fr('0.8')), a0)[0])
# ---- 11: Kc=2,T=100 -> Kp ----
check("11", "16.4", 2 * Fr('0.082') * 100)
# ---- 12: H2+I2<=>2HI, 2+2mol,Kc=4 -> conversion% ----
xE = sp.symbols('xE', positive=True)
x12 = [s for s in sp.solve(sp.Eq(4, (2 * xE)**2 / ((2 - xE) * (2 - xE))), xE) if s.is_real and 0 < s < 2][0]
check("12", "50", x12 / 2 * 100)
# ---- 13: 2NOCl<=>2NO+Cl2 ----
check("13", "0.2", (Fr('0.4')**2 * Fr('0.2')) / Fr('0.4')**2)
# ---- 16: H2+Br2<=>2HBr ----
check("16", "8", Fr('0.4')**2 / (Fr('0.1') * Fr('0.2')))
# ---- 17: SO2Cl2<=>SO2+Cl2, a0=3, avgM=81, MA=135 -> Kc ----
xF = sp.symbols('xF', positive=True)
x17 = sp.solve(sp.Eq(sp.Rational(81), (135 * 3) / (3 + xF)), xF)[0]
check("17", "4", x17**2 / (3 - x17))
# ---- 18: PCl5<=>PCl3+Cl2 ----
check("18", "1.2", (Fr('0.6') * Fr('0.6')) / Fr('0.3'))
# ---- 19: COCl2<=>CO+Cl2, a0=6,Kc=1 -> Cl2, then HCl in 2L ----
x19 = [s for s in sp.solve(sp.Eq(1 * (6 - x), x**2), x) if s > 0][0]
check("19", "2", (2 * x19) / 2)
# ---- 21: PCl5<=>PCl3+Cl2, a0=3,Kc=1, +3mol added -> Cl2 final ----
x1v = [s for s in sp.solve(sp.Eq(1 * (3 - x), x**2), x) if s > 0][0]
nA1, nB1 = 3 - x1v, x1v
nA_new0 = nA1 + 3
z = sp.symbols('z', positive=True)
zv = [s for s in sp.solve(sp.Eq(1, (nB1 + z)**2 / (nA_new0 - z)), z) if s.is_real and s > 0][0]
check("21", "2", nB1 + zv)
# ---- 22: Kp=4,P0=8 -> total pressure ----
p = sp.symbols('p', positive=True)
pv = [s for s in sp.solve(sp.Eq(4 * (8 - p), p**2), p) if s > 0][0]
check("22", "12", 8 + pv)
# ---- 23: PCl5(M=208.5), a0=4, alpha=50% -> D(H2) ----
xI = 4 * Fr(1, 2)
nA = 4 - xI
total = nA + 2 * xI
avgM = Fr('208.5') * 4 / total
check("23", "69.5", avgM / 2)
# ---- 24: PCl5<=>PCl3+Cl2, a0=6,Kc=1, V halved -> PCl5 final ----
x1b = [s for s in sp.solve(sp.Eq(1 * (6 - x), x**2), x) if s > 0][0]
nA1b, nB1b = 6 - x1b, x1b
y = sp.symbols('y', positive=True)
eq2 = sp.Eq(1, ((nB1b - y) / sp.Rational(1, 2))**2 / ((nA1b + y) / sp.Rational(1, 2)))
yv = [s for s in sp.solve(eq2, y) if s.is_real and 0 < s < nB1b][0]
check("24", "4.5", nA1b + yv)
# ---- 25: N2+O2<=>2NO, a0=b0=3,Kc=9 -> conversion% ----
xE2 = sp.symbols('xE2', positive=True)
x25 = [s for s in sp.solve(sp.Eq(9, (2 * xE2)**2 / ((3 - xE2)**2)), xE2) if s.is_real and 0 < s < 3][0]
check("25", "60", x25 / 3 * 100)
# ---- 26: Kc=2,T=200 -> Kp ----
check("26", "32.8", 2 * Fr('0.082') * 200)
# ---- 29: 2NO2<=>N2O4 ----
check("29", "15", Fr('0.6') / Fr('0.2')**2)

print(f"Jami tekshirilgan hisob (Y1, 1-32): yaqin {len(errors)} xato bilan.")
if errors:
    for e in errors:
        print(" -", e)
else:
    print("Barcha sonli Y1 javoblari mustaqil qayta hisoblash bilan mos keldi.")

# ---------------------------------------------------------------
# Javob HARFI to'g'ri variantga ishora qilishini ham tekshiramiz
# (ya'ni variantlar[javob-A] matni yuqoridagi hisoblangan songa mos).
import re


def num_in(s):
    nums = re.findall(r'-?\d+(?:,\d+)?', s)
    return float(nums[0].replace(',', '.')) if nums else None


letter_errors = []
expected_by_n = {
    1: 1800, 2: 16, 3: 40, 4: 4, 5: 0.4, 9: 4, 10: 1, 11: 16.4, 12: 50,
    13: 0.2, 16: 8, 17: 4, 18: 1.2, 19: 2, 21: 2, 22: 12, 23: 69.5,
    24: 4.5, 25: 60, 26: 32.8, 29: 15,
}
for n, exp in expected_by_n.items():
    got = num_in(javob_text(n))
    if got is None or abs(got - exp) > 0.05 * max(1, abs(exp)):
        letter_errors.append(f"{n}: javob harfi '{S[n]['javob']}' -> '{javob_text(n)}' (kutilgan {exp})")

print(f"\nJavob-harfi tekshiruvi: {len(letter_errors)} nomuvofiqlik.")
if letter_errors:
    for e in letter_errors:
        print(" -", e)
else:
    print("Barcha javob harflari (A/B/C/D) to'g'ri variantga ishora qiladi.")

# ---------------------------------------------------------------
# Y2 (33-35)
Y2 = next(s for s in d["savollar"] if s["tur"] == "Y2")
xY2 = sp.symbols('xY2', positive=True)
xv = [s for s in sp.solve(sp.Eq(4 * xY2**2, 4 * (2 - xY2)), xY2) if s > 0][0]
y2_errors = []
if abs(float(2 - xv) - 1) > 1e-6:
    y2_errors.append("33: N2O4 remaining mismatch")
if abs(float((2 - xv) + 2 * xv) - 3) > 1e-6:
    y2_errors.append("34: total mol mismatch")
Kp35 = 4 * Fr('0.082') * 200
if abs(float(Kp35) - 65.6) > 1e-6:
    y2_errors.append("35: Kp mismatch")
print(f"\nY2 (33-35) tekshiruvi: {len(y2_errors)} xato.")
for e in y2_errors:
    print(" -", e)

# ---------------------------------------------------------------
# O1 (36-40)
o1_errors = []
V36 = sp.symbols('V36', positive=True)
sol36 = sp.solve(sp.Eq((Fr('0.3') / V36)**2 / (Fr('0.6') / V36), Fr('0.1')), V36)
if abs(float(sol36[0]) - 1.5) > 1e-6:
    o1_errors.append("36 mismatch")
x37 = [s for s in sp.solve(sp.Eq(3 * (6 - x), x**2), x) if s > 0][0]
if abs(float(2 * x37 / 3) - 2) > 1e-6:
    o1_errors.append("37 mismatch")
x1_38 = [s for s in sp.solve(sp.Eq(2 * (2 - x), x**2), x) if s > 0][0]
nA1_38, nB1_38 = 2 - x1_38, x1_38
nA_new0_38 = nA1_38 + 2
z38 = sp.symbols('z38', positive=True)
zv38 = [s for s in sp.solve(sp.Eq(2, (nB1_38 + z38)**2 / (nA_new0_38 - z38)), z38) if s.is_real and s > 0][0]
if abs(float(nB1_38 + zv38) - 2) > 1e-6:
    o1_errors.append("38 mismatch")
x39 = 5 * Fr('0.4')
nA39 = 5 - x39
total39 = nA39 + 2 * x39
avgM39 = 99 * 5 / total39
D39 = avgM39 / 2
if abs(float(D39) - 35.357142857142854) > 1e-6:
    o1_errors.append("39 mismatch")
x40 = sp.solve(sp.Eq(sp.Rational(108), (135 * 4) / (4 + x)), x)[0]
Kc40 = x40**2 / (4 - x40)
if abs(float(Kc40) - 1 / 3) > 1e-6:
    o1_errors.append("40 mismatch")
print(f"\nO1 (36-40) tekshiruvi: {len(o1_errors)} xato.")
for e in o1_errors:
    print(" -", e)

# ---------------------------------------------------------------
# O2 (41-43): faqat sonli bandlar
o2_errors = []
x41 = [s for s in sp.solve(sp.Eq(5 * (10 - x), x**2), x) if s > 0][0]
if abs(float(x41) - 5) > 1e-6:
    o2_errors.append("41-band1 mismatch")
if abs(float((10 - x41) + 2 * x41) - 15) > 1e-6:
    o2_errors.append("41-band2 mismatch")
if abs(float(2 * x41 / 5) - 2) > 1e-6:
    o2_errors.append("41-band3 mismatch")
x42 = [s for s in sp.solve(sp.Eq(2 * (12 - x), x**2), x) if s > 0][0]
if abs(float(x42) - 4) > 1e-6:
    o2_errors.append("42-band1 mismatch")
Kp42 = 2 * Fr('0.082') * 150
if abs(float(Kp42) - 24.6) > 1e-6:
    o2_errors.append("42-band3 mismatch")
print(f"\nO2 (41-43) sonli bandlar tekshiruvi: {len(o2_errors)} xato.")
for e in o2_errors:
    print(" -", e)

total_errors = len(errors) + len(letter_errors) + len(y2_errors) + len(o1_errors) + len(o2_errors)
print(f"\n=== YAKUNIY: jami xatolar = {total_errors} ===")
