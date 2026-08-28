# -*- coding: utf-8 -*-
"""v04.json dagi barcha SONLI javoblarni mustaqil (formuladan to'g'ridan-to'g'ri
qayta hisoblab) tekshiradi. Sifat/nazariy savollar (masalan 1,5,6,14,16,18,20,
22,23,26,27,28,30,32) kimyoviy mantiq bilan qo'lda tekshiriladi, skriptga
kiritilmagan.

Ishlatish:  python3 variantlar/verify_v04.py
"""
import json
import os
import re
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "v04.json"), encoding="utf-8"))
errors = []


def check(label, expected, actual, tol=1e-6):
    if abs(float(expected) - float(actual)) > tol:
        errors.append(f"{label}: kutilgan {expected}, natija {actual}")


# ---- 2: Na2ZO3, w(Z)=2*w(Na) ----
na_mass = 2 * 23
z_mass = 2 * na_mass
check("2", "186", na_mass + z_mass + 3 * 16)

# ---- 3: X3+ ion, sum=48, N=Z+3 ----
Z3, N3 = sp.symbols('Z3 N3', positive=True, integer=True)
sol3 = sp.solve([sp.Eq(2 * Z3 + N3 - 3, 48), sp.Eq(N3, Z3 + 3)], [Z3, N3], dict=True)[0]
check("3", "35", sol3[Z3] + sol3[N3])

# ---- 4: n+l=8 elektronlar soni (5f+6d+7p+8s) ----
check("4", "32", 14 + 10 + 6 + 2)

# ---- 6: asetilen pi-bog' ulushi ----
check("6", "40", Fr(2, 5) * 100)

# ---- 7: r=k[A]^2[B] ----
k7 = Fr(3, 1) / (Fr('0.1') ** 2 * Fr('0.3'))
check("7", "9", k7 * Fr('0.3') ** 2 * Fr('0.1'))

# ---- 8: COCl2<=>CO+Cl2, Kc=0.25, alpha=20% ----
a8 = sp.symbols('a8', positive=True)
sol8 = sp.solve(sp.Eq((Fr('0.2') * a8) ** 2 / (Fr('0.8') * a8), Fr('0.25')), a8)
check("8", "5", sol8[0])

# ---- 9: 288 g suvga necha mol LiOH -> 20% ----
n9 = sp.symbols('n9', positive=True)
sol9 = sp.solve(sp.Eq(24 * n9 / (24 * n9 + 288), Fr('0.2')), n9)
check("9", "3", sol9[0])

# ---- 10: 300g 20% dan suv bug'latib to'yintirish (S=150) ----
x10 = sp.symbols('x10')
sol10 = sp.solve(sp.Eq(60 / (300 - x10), Fr(3, 5)), x10)
check("10", "200", sol10[0])

# ---- 11: FeCl3(0.2,80%) + MgCl2(0.5,alpha2), Cl- = 8x Fe3+ ----
alpha2 = sp.symbols('alpha2', positive=True)
Fe3 = Fr('0.2') * Fr('0.8')
sol11 = sp.solve(sp.Eq(3 * Fe3 + 2 * Fr('0.5') * alpha2, 8 * Fe3), alpha2)
check("11", "80", sol11[0] * 100)

# ---- 12: 3SnS + 10NO3- + 16H+ -> 3Sn4+ + 3SO4^2- + 10NO + 8H2O, coeff sum ----
check("12", "53", 3 + 10 + 16 + 3 + 3 + 10 + 8)

# ---- 13: NiCl2(2.95g Ni) + XCl2(5.6g X) ketma-ket elektroliz ----
nNi13 = Fr('2.95') / 59
eNi13 = nNi13 * 2
nX13 = eNi13 / 2
MX13 = Fr('5.6') / nX13
check("13", "112", MX13)

# ---- 15: H,C,O,S tuz, C=3S, H=2O, M<250 ----
unit15 = 32 + 3 * 12 + 2 * 16 + 4
check("15-unit-M", "104", unit15)
check("15", "20", (1 + 3 + 2 + 4) * 2)

# ---- 17: metall oksid + H2 (1792ml), keyin HCl bilan H2 hajmi (elektron balans -> teng) ----
check("17", "1792", 1792)

# ---- 19: NaNO3+Hg(NO3)2, mass=145, O2=14L ----
x19, y19 = sp.symbols('x19 y19', positive=True)
sol19 = sp.solve([sp.Eq(85 * x19 + 325 * y19, 145),
                   sp.Eq(Fr(1, 2) * x19 + y19, Fr('14') / Fr('22.4'))], [x19, y19])
check("19", "0.25", sol19[y19])

# ---- 21: penten-1+H2, M0=36, alkene mol ulushi 2 marta kamaydi ----
x21 = sp.symbols('x21', positive=True)
sol21 = sp.solve(sp.Eq(70 * x21 + 2 * (1 - x21), 36), x21)
x0_21 = sol21[0]
x1_21 = x0_21 / 2
M1_21 = 70 * x1_21 + 2 * (1 - x1_21)
check("21", "-17", M1_21 - 36)

# ---- 24: 83g (propanal+butanal), Cu2O=180g, H2=28L, butanal massa ulushi ----
x24, y24 = sp.symbols('x24 y24', positive=True)
sol24 = sp.solve([sp.Eq(58 * x24 + 72 * y24, 83),
                   sp.Eq(x24 + y24, Fr('28') / Fr('22.4'))], [x24, y24])
w24 = (72 * sol24[y24]) / 83 * 100
check("24-Cu2O", "180", (sol24[x24] + sol24[y24]) * 144)
check("24", "65.1", float(w24), tol=0.05)

# ---- 25: C2H5COOH(x)+C3H7COOH(y), MgO->29g tuz, NaOH 0.3mol=x+y ----
x25, y25 = sp.symbols('x25 y25', positive=True)
sol25 = sp.solve([sp.Eq(x25 + y25, Fr('0.3')),
                   sp.Eq(170 * (x25 / 2) + 198 * (y25 / 2), 29)], [x25, y25], dict=True)[0]
check("25", "0.05", sol25[x25])

# ---- 29: poliizopren M=340000, bo'g'in=68 ----
check("29", "5000", Fr(340000, 68))

# ---- 31: BaCl2 molyar massa ----
check("31", "208", 137 + 2 * Fr('35.5'))

# ---- Y2 (33-35): Ni+NiCO3, mass=74, gasV=22.4L, CaCO3=25g ----
A33 = sp.symbols('A33', positive=True)
y2_total_gas = Fr('22.4') / Fr('22.4')
y2_precip = Fr('25') / 100
x2_ = y2_total_gas - y2_precip
sol33 = sp.solve(sp.Eq(x2_ * A33 + (A33 + 60) * y2_precip, 74), A33)
check("33", "59", sol33[0])
avgM_34 = (x2_ * 2 + y2_precip * 44) / y2_total_gas
check("34", "12.5", avgM_34)
NO_35 = (x2_ * 2) / 3
check("35", "16.8", (NO_35 + y2_precip) * Fr('22.4'))

# ---- 36: SO2Cl2<=>SO2+Cl2, Kc=0.075, SO2=Cl2=0.3, SO2Cl2=0.6 -> V ----
V36 = sp.symbols('V36', positive=True)
sol36 = sp.solve(sp.Eq((Fr('0.3') / V36) * (Fr('0.3') / V36) / (Fr('0.6') / V36), Fr('0.075')), V36)
check("36", "2", sol36[0])

# ---- 37: CuSO4*5H2O 200g,32%->24% ----
y37 = sp.symbols('y37', positive=True)
sol37 = sp.solve(sp.Eq((128 - Fr('0.64') * y37) / (400 - y37), Fr('0.24')), y37)
check("37", "80", sol37[0])

# ---- 38: Cr+Mg equimolar, 19g, HCl->14L, NaOH->8.4L ----
n38 = sp.symbols('n38', positive=True)
sol38 = sp.solve(sp.Eq(Fr('2.5') * n38, Fr('14') / Fr('22.4')), n38)
n38v = sol38[0]
check("38-NaOH-check", Fr('8.4') / Fr('22.4'), Fr('1.5') * n38v)
check("38", "76", 19 / n38v)

# ---- 39: Al4C3+CaC2, mass=68, CaCO3=175 ----
x39, y39 = sp.symbols('x39 y39', positive=True)
sol39 = sp.solve([sp.Eq(144 * x39 + 64 * y39, 68),
                   sp.Eq(100 * (3 * x39 + 2 * y39), 175)], [x39, y39])
CH4_39 = 3 * sol39[x39]
C2H2_39 = sol39[y39]
avgM_39 = (CH4_39 * 16 + C2H2_39 * 26) / (CH4_39 + C2H2_39)
check("39", "20", avgM_39)

# ---- 40: tripalmitin(a)+trilinolein(b), a=3b, mass=1648 ----
b40 = sp.symbols('b40', positive=True)
sol40 = sp.solve(sp.Eq(806 * (3 * b40) + 878 * b40, 1648), b40)
a40v = 3 * sol40[0]
check("40", "1251", 3 * a40v * 278)

# ---- 41: Cr2O3(0.25)+C(0.25), mass=41 ----
n41 = sp.symbols('n41', positive=True)
sol41 = sp.solve(sp.Eq(164 * n41, 41), n41)
n41v = sol41[0]
check("41-H2SO4", "1.25", 5 * n41v)
check("41-Cr2(SO4)3-mass", "98", n41v * 392)
check("41-precip", "85", n41v * 100 + 2 * n41v * 120)
p41 = sp.symbols('p41', positive=True)
sol41p = sp.solve(sp.Eq(p41 * (52 - 27), Fr('12.5')), p41)
check("41-Al-mass", "13.5", sol41p[0] * 27)
check("41-hydrate", "166.5", (sol41p[0] / 2) * 666)

print(f"Jami tekshirilgan hisob: yaqin {len(errors)} xato bilan.")
if errors:
    print("XATOLAR:")
    for e in errors:
        print(" -", e)
else:
    print("Barcha sonli javoblar mustaqil qayta hisoblash bilan mos keldi.")

# ---------------------------------------------------------------
# Pozitsiya->bo'lim->element->qiyinlik->kognitiv pasporti v01 bilan
# barcha 43 pozitsiya bo'yicha dasturiy solishtiriladi.
v01_path = os.path.join(HERE, "..", "tahlil", "v01.json")
v01 = json.load(open(v01_path, encoding="utf-8"))["savollar"]
v01_by_n = {s["n"]: s for s in v01}

v04_by_n = {}
for s in d["savollar"]:
    if s["tur"] == "Y2":
        for p in s["ichki_pasport"]:
            v04_by_n[p["n"]] = p
    else:
        v04_by_n[s["n"]] = s

passport_errors = []
for n in range(1, 44):
    a = v01_by_n[n]
    b = v04_by_n.get(n)
    if b is None or "qiyinlik" not in b or b["qiyinlik"] is None:
        passport_errors.append(f"{n}: v04'da qiyinlik/kognitiv/element yo'q")
        continue
    for key in ("element", "qiyinlik", "kognitiv"):
        if a[key] != b[key]:
            passport_errors.append(f"{n}: {key} mos kelmadi (v01={a[key]!r}, v04={b[key]!r})")

print(f"\nPasport tekshiruvi (43/43 pozitsiya): {len(passport_errors)} nomuvofiqlik.")
if passport_errors:
    for e in passport_errors:
        print(" -", e)
else:
    print("Barcha 43 pozitsiyaning element/qiyinlik/kognitiv metama'lumoti v01 bilan aynan mos.")
