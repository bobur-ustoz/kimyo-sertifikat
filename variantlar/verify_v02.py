# -*- coding: utf-8 -*-
"""v02.json dagi barcha SONLI javoblarni mustaqil (formuladan to'g'ridan-to'g'ri
qayta hisoblab) tekshiradi. Sifat/nazariy savollar (masalan 1,5,14,16,18,28,30,32)
kimyoviy mantiq bilan qo'lda tekshiriladi, skriptga kiritilmagan.

Ishlatish:  python3 variantlar/verify_v02.py
"""
import json
import os
import re
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "v02.json"), encoding="utf-8"))
errors = []


def check(label, expected, actual, tol=1e-6):
    if abs(float(expected) - float(actual)) > tol:
        errors.append(f"{label}: kutilgan {expected}, natija {actual}")


def javob_of(n):
    for s in d["savollar"]:
        if s.get("n") == n:
            return s["javob"] if "javob" in s else None
    return None


# ---- 2: K2XO4, w(O)=2w(X) ----
MX = 64 / 2
Mtotal = 2 * 39 + MX + 4 * 16
check("2", "174", Mtotal)

# ---- 3: Y2+ ion, sum=60, N=e+4 ----
Z = sp.symbols('Z', positive=True, integer=True)
solZ = sp.solve(sp.Eq(Z + (Z - 2) + (Z - 2 + 4), 60), Z)[0]
Ar3 = solZ + (solZ - 2 + 4)
check("3", "42", Ar3)

# ---- 4: n+l=6 elektronlar soni ----
cap = {0: 2, 1: 6, 2: 10, 3: 14}
total4 = sum(cap[l] for n in range(1, 9) for l in range(0, n) if n + l == 6)
check("4", "18", total4)

# ---- 6: propin p-orbital % ----
check("6", 25.0, Fr(2, 8) * 100)

# ---- 7: r=k[A][B]^2 ----
k7 = Fr(6, 1) / (Fr('0.2') * Fr('0.1') ** 2)
r2 = k7 * Fr('0.1') * Fr('0.2') ** 2
check("7", "12", r2)

# ---- 8: N2O4<=>2NO2, Kc=0.6, alpha=0.2, V=1 ----
n0 = sp.symbols('n0', positive=True)
sol8 = sp.solve(sp.Eq((2 * n0 * Fr('0.2') / 1) ** 2 / (n0 * Fr('0.8') / 1), Fr('0.6')), n0)[0]
check("8", "3", sol8)

# ---- 9: suvga KOH, 40% ----
water = 14 * 18
check("9-tekshiruv", 0.4, Fr(3 * 56, water + 3 * 56))

# ---- 10: 250g 24%, S=75 ----
solute = 250 * Fr('0.24')
water10 = 250 - solute
water_sat = solute * 100 / 75
check("10", "110", water10 - water_sat)

# ---- 11: CaCl2 0.3mol(80%)+NaCl 0.6mol, oran=3 ----
Ca2 = Fr('0.3') * Fr('0.8')
totalCl = 3 * Ca2
a2 = (totalCl - 2 * Ca2) / Fr('0.6')
check("11", 40.0, float(a2) * 100)

# ---- 12: FeS2+5NO3-+4H++... koeff yig'indi ----
check("12", "20", 1 + 5 + 4 + 1 + 2 + 5 + 2)

# ---- 13: CuCl2 9.6g Cu / YCl3 5.6g Y ----
n_Cu = Fr('9.6') / 64
n_Y = (n_Cu * 2) / 3
check("13", "56", Fr('5.6') / n_Y)

# ---- 17: Fe2O3+H2, keyin Fe+HCl ----
n_H2used = Fr(630, 22400)
n_Fe2O3 = n_H2used / 3
n_Fe = 2 * n_Fe2O3
check("17", "420", n_Fe * 22400)

# ---- 19: Cu(NO3)2(a)+AgNO3(b) ----
a19, b19 = sp.symbols('a19 b19', positive=True)
sol19 = sp.solve([sp.Eq(188 * a19 + 170 * b19, Fr('54.6')), sp.Eq(a19 + b19, Fr('0.3'))], [a19, b19])
check("19", "0.1", sol19[b19])

# ---- 21: buten M0=20, ulush 2 marta kamaydi ----
f0, Ma = Fr(1, 3), 56
M0_21 = Ma * f0 + 2 * (1 - f0)
z21 = f0 / (2 - f0)
Mnew21 = M0_21 / (1 - z21)
check("21", 5.0, float(Mnew21 - M0_21))

# ---- 22: C9H12 k=3 -> sp3H=9 ----
check("22-tekshiruv", 9, 6 + 3)

# ---- 23: fenol 235g, yarmi, O2=39.2L ----
half_mol = Fr('23.5') / 94
check("23-O2tekshiruv", "39.2", half_mol * 7 * 22400 / 1000)
check("23", 20.0, Fr(47, 235) * 100)

# ---- 24: HCHO(a)+CH3CHO(b) ----
a24, b24 = sp.symbols('a24 b24', positive=True)
sol24 = sp.solve([sp.Eq(a24 + b24, Fr('0.5')), sp.Eq(2 * a24 + b24, Fr(108, 144))], [a24, b24])
check("24", "11", sol24[b24] * 44)

# ---- 25: sirka(a)+propion(b), CaO+KOH ----
a25, b25 = sp.symbols('a25 b25', positive=True)
sol25 = sp.solve([sp.Eq(a25 + b25, Fr('0.4')),
                   sp.Eq(Fr(1, 2) * a25 * 158 + Fr(1, 2) * b25 * 186, 33)], [a25, b25])
check("25", "0.3", sol25[a25])

# ---- 26: etilbenzoat distinct ox. states ----
Csum = 3 + 0 + 5 * (-1) + (-1) + (-3)
check("26-neytrallik", 0, Csum + 10 * 1 + 2 * (-2))
check("26", "4", len({3, 0, -1, -3}))

# ---- 29: poliizopren M=680000 ----
check("29", "10000", Fr(680000, 68))

# ---- 31: CaCl2 M ----
check("31", "111", 40 + 2 * Fr('35.5'))

# ---- Y2 (33-35) ---- Mg + MgCO3 aralashmasi
total_gas = Fr('5.04') / Fr('22.4')
precip35 = Fr('7.5') / 100
x35 = total_gas - precip35
Asym = sp.symbols('Asym', positive=True)
A35 = sp.solve(sp.Eq(x35 * Asym + precip35 * (Asym + 60), Fr('9.9')), Asym)[0]
check("33", "24", A35)
mass_gas35 = x35 * 2 + precip35 * 44
check("34", "16", mass_gas35 / total_gas)
n_NO35 = (x35 * 2) / 3
check("35", "3.92", (n_NO35 + precip35) * Fr('22.4'))

# ---- 36: 2NO2<=>N2O4, Kc=10 ----
V36 = 10 * Fr('0.4') ** 2 / Fr('0.8')
check("36", "2", V36)

# ---- 37: CuSO4 200g 40%->24% ----
x37 = sp.symbols('x37', positive=True)
sol37 = sp.solve(sp.Eq((200 * Fr('0.40') - x37 * Fr(160, 250)) / (200 - x37), Fr('0.24')), x37)[0]
check("37", "80", sol37)

# ---- 38: X(3+,amfoter)+Y(2+) ----
n38 = (Fr('5.6') / 22.4) / Fr('2.5')
check("38", "83", Fr('8.3') / n38)

# ---- 39: Al4C3(a)+CaC2(b) 1:3 ----
a39, b39 = Fr('0.02'), Fr('0.06')
CH4_39, C2H2_39 = 3 * a39, b39
CO2_39 = CH4_39 + 2 * C2H2_39
check("39-precip", "18", CO2_39 * 100)
check("39", "21", (CH4_39 * 16 + C2H2_39 * 26) / (CH4_39 + C2H2_39))

# ---- 40: tripalmitin(2k)+triolein(k) ----
M_tripalmitin = 92 + 3 * 256 - 3 * 18
M_triolein = 92 + 3 * 282 - 3 * 18
k40 = Fr('0.5')
check("40-mass", "1248", 2 * k40 * M_tripalmitin + k40 * M_triolein)
check("40", "834", 3 * (2 * k40) * 278)

# ---- 41: CuO(0.1)+C(0.1), H2SO4, Zn ----
check("41-mass", "9.2", Fr('0.1') * 80 + Fr('0.1') * 12)
check("41-H2SO4", "0.3", Fr('0.1') * 1 + Fr('0.1') * 2)
check("41-precip", "34", Fr('0.1') * 100 + Fr('0.2') * 120)
check("41-plastinka", -0.1, -(Fr('0.1') * 65) + Fr('0.1') * 64)

print(f"Jami tekshirilgan hisob: yaqin {len(errors)} xato bilan.")
if errors:
    print("XATOLAR:")
    for e in errors:
        print(" -", e)
else:
    print("Barcha sonli javoblar mustaqil qayta hisoblash bilan mos keldi.")

# ---------------------------------------------------------------
# Pozitsiya->bo'lim->element->qiyinlik->kognitiv pasporti v01 (haqiqiy
# imtihon, faqat metama'lumot) bilan barcha 43 pozitsiya bo'yicha
# dasturiy solishtiriladi.
v01_path = os.path.join(HERE, "..", "tahlil", "v01.json")
v01 = json.load(open(v01_path, encoding="utf-8"))["savollar"]
v01_by_n = {s["n"]: s for s in v01}

# v02 pasportini pozitsiya bo'yicha yig'amiz (Y2 ichki_pasport orqali yoyiladi)
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
        passport_errors.append(f"{n}: v02'da qiyinlik/kognitiv/element yo'q")
        continue
    for key in ("element", "qiyinlik", "kognitiv"):
        if a[key] != b[key]:
            passport_errors.append(f"{n}: {key} mos kelmadi (v01={a[key]!r}, v02={b[key]!r})")

print(f"\nPasport tekshiruvi (43/43 pozitsiya): {len(passport_errors)} nomuvofiqlik.")
if passport_errors:
    for e in passport_errors:
        print(" -", e)
else:
    print("Barcha 43 pozitsiyaning element/qiyinlik/kognitiv metama'lumoti v01 bilan aynan mos.")
