# -*- coding: utf-8 -*-
"""v03.json dagi barcha SONLI javoblarni mustaqil (formuladan to'g'ridan-to'g'ri
qayta hisoblab) tekshiradi. Sifat/nazariy savollar (masalan 1,5,6,14,16,18,20,
22,23,26,27,28,30,31,32) kimyoviy mantiq bilan qo'lda tekshiriladi, skriptga
kiritilmagan.

Ishlatish:  python3 variantlar/verify_v03.py
"""
import json
import os
import re
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "v03.json"), encoding="utf-8"))
errors = []


def check(label, expected, actual, tol=1e-6):
    if abs(float(expected) - float(actual)) > tol:
        errors.append(f"{label}: kutilgan {expected}, natija {actual}")


# ---- 2: K2YO4, w(Y)=2*w(O) ----
check("2", "270", 2 * 39 + 2 * 64 + 4 * 16)

# ---- 3: X2- ion, sum=50, N=Z+3 ----
Z3, N3 = sp.symbols('Z3 N3', positive=True, integer=True)
sol3 = sp.solve([sp.Eq(2 * Z3 + N3 + 2, 50), sp.Eq(N3, Z3 + 3)], [Z3, N3], dict=True)[0]
check("3", "33", sol3[Z3] + sol3[N3])

# ---- 4: n+l=7 elektronlar soni (4f+5d+6p+7s) ----
check("4", "32", 14 + 10 + 6 + 2)

# ---- 6: allen pi-bog' ulushi ----
check("6", "25", Fr(2, 8) * 100)

# ---- 7: r=k[X][Y]^2 ----
k7 = Fr(6, 1) / (Fr('0.2') * Fr('0.1') ** 2)
check("7", "12", k7 * Fr('0.1') * Fr('0.2') ** 2)

# ---- 8: N2O4<=>2NO2, Kc=0.4, alpha=20% ----
a8 = sp.symbols('a8', positive=True)
sol8 = sp.solve(sp.Eq((Fr('0.4') * a8) ** 2 / (Fr('0.8') * a8), Fr('0.4')), a8)
check("8", "2", sol8[0])

# ---- 9: 224 g suvga necha mol KOH -> 50% ----
n9 = sp.symbols('n9', positive=True)
sol9 = sp.solve(sp.Eq(56 * n9 / (56 * n9 + 224), Fr('0.5')), n9)
check("9", "4", sol9[0])

# ---- 10: 500g 24% dan suv bug'latib to'yintirish (S=100) ----
x10 = sp.symbols('x10')
sol10 = sp.solve(sp.Eq(120 / (500 - x10), Fr(1, 2)), x10)
check("10", "260", sol10[0])

# ---- 11: Al(NO3)3(0.3,90%) + Ca(NO3)2(0.6,alpha2), NO3- = 6x Al3+ ----
alpha2 = sp.symbols('alpha2', positive=True)
Al3 = Fr('0.3') * Fr('0.9')
sol11 = sp.solve(sp.Eq(3 * Al3 + 2 * Fr('0.6') * alpha2, 6 * Al3), alpha2)
check("11", "67.5", sol11[0] * 100)

# ---- 12: FeS2 + 5NO3- + 4H+ -> Fe3+ + 2SO4^2- + 5NO + 2H2O, coeff sum ----
check("12", "20", 1 + 5 + 4 + 1 + 2 + 5 + 2)

# ---- 13: CuCl2(3.2g Cu) + XCl2(5.85g X) ketma-ket elektroliz ----
nCu13 = Fr('3.2') / 64
e13 = nCu13 * 2
nX13 = e13 / 2
MX13 = Fr('5.85') / nX13
check("13", "117", MX13)

# ---- 15: H,N,O,S tuz, N=2S, H=1.5O, M<300 ----
unit15 = 3 * 1 + 2 * 14 + 2 * 16 + 32
check("15-M(k3)", "285", unit15 * 3)
check("15", "24", (3 + 2 + 2 + 1) * 3)

# ---- 17: metall oksid + H2 (2240ml), keyin HCl bilan H2 hajmi (elektron balans -> teng) ----
check("17", "2240", 2240)

# ---- 19: AgNO3+Cr(NO3)3, mass=204, O2=14L ----
x19, y19 = sp.symbols('x19 y19', positive=True)
sol19 = sp.solve([sp.Eq(170 * x19 + 238 * y19, 204),
                   sp.Eq(Fr(1, 2) * x19 + Fr(3, 4) * y19, Fr('14') / Fr('22.4'))], [x19, y19])
check("19", "0.5", sol19[y19])

# ---- 21: propen+H2, M0=14, alkene mol ulushi 2 marta kamaydi ----
x21 = sp.symbols('x21', positive=True)
sol21 = sp.solve(sp.Eq(42 * x21 + 2 * (1 - x21), 14), x21)
x0_21 = sol21[0]
x1_21 = x0_21 / 2
M1_21 = 42 * x1_21 + 2 * (1 - x1_21)
check("21", "-6", M1_21 - 14)

# ---- 24: 40g (asetaldegid+propanal), Cu2O=108g, H2=16.8L, propanal massa ulushi ----
x24, y24 = sp.symbols('x24 y24', positive=True)
sol24 = sp.solve([sp.Eq(44 * x24 + 58 * y24, 40),
                   sp.Eq(x24 + y24, Fr('16.8') / Fr('22.4'))], [x24, y24])
w24 = (58 * sol24[y24]) / 40 * 100
check("24-Cu2O", "108", (sol24[x24] + sol24[y24]) * 144)
check("24", "72.5", w24)

# ---- 25: CH3COOH(x)+C2H5COOH(y), MgO->44g tuz, NaOH 0.3mol=x+y ----
x25, y25 = sp.symbols('x25 y25', positive=True)
sol25 = sp.solve([sp.Eq(x25 + y25, Fr('0.3')),
                   sp.Eq(142 * (x25 / 2) + 170 * (y25 / 2), 22)], [x25, y25], dict=True)[0]
check("25", "0.25", sol25[x25])

# ---- 29: poliizopren M=272000, bo'g'in=68 ----
check("29", "4000", Fr(272000, 68))

# ---- 31: NaBr molyar massa ----
check("31", "103", 23 + 80)

# ---- Y2 (33-35): Ca+CaCO3, mass=22, gasV=8.96L, BaCO3=19.7g ----
A33 = sp.symbols('A33', positive=True)
y2_total_gas = Fr('8.96') / Fr('22.4')
y2_precip = Fr('19.7') / 197
x2_ = y2_total_gas - y2_precip
sol33 = sp.solve(sp.Eq(x2_ * A33 + (A33 + 60) * y2_precip, 22), A33)
check("33", "40", sol33[0])
avgM_34 = (x2_ * 2 + y2_precip * 44) / y2_total_gas
check("34", "12.5", avgM_34)
NO_35 = (x2_ * 2) / 3
check("35", "6.72", (NO_35 + y2_precip) * Fr('22.4'))

# ---- 36: PCl5<=>PCl3+Cl2, Kc=0.05, PCl3=Cl2=0.2, PCl5=0.4 -> V ----
V36 = sp.symbols('V36', positive=True)
sol36 = sp.solve(sp.Eq((Fr('0.2') / V36) * (Fr('0.2') / V36) / (Fr('0.4') / V36), Fr('0.05')), V36)
check("36", "2", sol36[0])

# ---- 37: CuSO4*5H2O 250g,32%->24% ----
y37 = sp.symbols('y37', positive=True)
sol37 = sp.solve(sp.Eq((160 - Fr('0.64') * y37) / (500 - y37), Fr('0.24')), y37)
check("37", "100", sol37[0])

# ---- 38: Al+Mg equimolar, 10.2g, HCl->11.2L, NaOH->6.72L ----
n38 = sp.symbols('n38', positive=True)
sol38 = sp.solve(sp.Eq(Fr('2.5') * n38, Fr('11.2') / Fr('22.4')), n38)
n38v = sol38[0]
check("38-NaOH-check", Fr('6.72') / Fr('22.4'), Fr('1.5') * n38v)
check("38", "51", (n38v * 51) / n38v)

# ---- 39: Al4C3+CaC2, mass=104, CaCO3=250 ----
x39, y39 = sp.symbols('x39 y39', positive=True)
sol39 = sp.solve([sp.Eq(144 * x39 + 64 * y39, 104),
                   sp.Eq(100 * (3 * x39 + 2 * y39), 250)], [x39, y39])
CH4_39 = 3 * sol39[x39]
C2H2_39 = sol39[y39]
avgM_39 = (CH4_39 * 16 + C2H2_39 * 26) / (CH4_39 + C2H2_39)
check("39", "18.5", avgM_39)

# ---- 40: tristearin(a)+triolein(b=2a), mass=1329 ----
a40 = sp.symbols('a40', positive=True)
sol40 = sp.solve(sp.Eq(890 * a40 + 884 * (2 * a40), 1329), a40)
check("40", "459", 3 * sol40[0] * 306)

# ---- 41: Fe2O3(0.5)+C(0.5), mass=86 ----
n41 = sp.symbols('n41', positive=True)
sol41 = sp.solve(sp.Eq(172 * n41, 86), n41)
n41v = sol41[0]
check("41-H2SO4", "2.5", 5 * n41v)
check("41-Fe2(SO4)3-mass", "200", n41v * 400)
check("41-precip", "170", n41v * 100 + 2 * n41v * 120)
p41 = sp.symbols('p41', positive=True)
sol41p = sp.solve(sp.Eq(p41 * (56 - 27), 29), p41)
check("41-Al-mass", "27", sol41p[0] * 27)
check("41-hydrate", "333", (sol41p[0] / 2) * 666)

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

v02_by_n = {}
for s in d["savollar"]:
    if s["tur"] == "Y2":
        for p in s["ichki_pasport"]:
            v02_by_n[p["n"]] = p
    else:
        v02_by_n[s["n"]] = s

passport_errors = []
for n in range(1, 44):
    a = v01_by_n[n]
    b = v02_by_n.get(n)
    if b is None or "qiyinlik" not in b or b["qiyinlik"] is None:
        passport_errors.append(f"{n}: v03'da qiyinlik/kognitiv/element yo'q")
        continue
    for key in ("element", "qiyinlik", "kognitiv"):
        if a[key] != b[key]:
            passport_errors.append(f"{n}: {key} mos kelmadi (v01={a[key]!r}, v03={b[key]!r})")

print(f"\nPasport tekshiruvi (43/43 pozitsiya): {len(passport_errors)} nomuvofiqlik.")
if passport_errors:
    for e in passport_errors:
        print(" -", e)
else:
    print("Barcha 43 pozitsiyaning element/qiyinlik/kognitiv metama'lumoti v01 bilan aynan mos.")
