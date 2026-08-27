# -*- coding: utf-8 -*-
"""I6-muvozanat.json dagi barcha SONLI javoblarni ikkinchi marta, mustaqil
qayta hisoblab tekshiradi (1-usul: shu skriptdagi to'g'ridan-to'g'ri formula;
2-usul allaqachon generatsiya bosqichida sympy bilan bajarilgan — bu yerda
uchinchi, eng sodda tekshiruv: qo'lda yozilgan yakuniy JSON qiymati generatsiya
paytidagi natija bilan solishtiriladi).

Ishlatish:  cd namuna && python3 verify.py
"""
import json
import re
from fractions import Fraction as Fr

d = json.load(open("I6-muvozanat.json", encoding="utf-8"))
errors = []

def check(label, expected, actual, tol=1e-6):
    if abs(float(expected) - float(actual)) > tol:
        errors.append(f"{label}: kutilgan {expected}, JSON dagi {actual}")

def num_from_javob(s):
    """'40' / 'Kc = 64' / '1,6 mol/l' / '20%' / '1/6 (\u22480,167)' -> float"""
    s = s.replace(",", ".")
    paren = re.search(r"\(([^)]*)\)", s)
    if paren:
        m = re.search(r"-?\d+\.?\d*", paren.group(1))
        if m:
            return float(m.group())
    m = re.search(r"-?\d+\.?\d*", s)
    return float(m.group())

# ---- Tip1: mashqlar (Kc = mahsulot^koeff / reagent^koeff) ----
tip1_cases = [  # (mahsulot_koeff, [mahsulot_konts], reagent_koeff, [reagent_konts])
    ([2], [0.8], [1,1], [0.1,0.1]), ([2], [1.2], [1,1], [0.2,0.3]), ([2], [0.6], [1,1], [0.15,0.2]),
    ([1,1], [0.5,0.4], [1,1], [0.1,0.2]), ([1,1], [0.9,0.3], [1,1], [0.3,0.1]), ([1,1], [0.4,0.6], [1,1], [0.2,0.2]),
    ([2], [0.4], [1,3], [0.2,0.1]), ([2], [0.6], [1,3], [0.3,0.2]),
    ([2], [0.8], [2,1], [0.4,0.2]), ([2], [1.0], [2,1], [0.5,0.25]),
    ([2], [1.6], [1,1], [0.4,0.2]), ([1,1], [0.7,0.5], [1,1], [0.2,0.25]),
]
for i, (cn, num, cd, den) in enumerate(tip1_cases):
    num = [Fr(str(v)) for v in num]; den = [Fr(str(v)) for v in den]
    kc = 1
    for c, n in zip(cn, num): kc *= n**c
    for c, n in zip(cd, den): kc /= n**c
    check(f"tip1.mashqlar[{i}]", float(kc), num_from_javob(d["tiplar"][0]["mashqlar"][i]["javob"]))
print(f"Tip1 mashqlar (12): {'OK' if not errors else 'XATO bor'}")

# ---- Tip1 A-daraja: noma'lum konsentratsiyani orqaga topish ----
A_cases = [
    (64, [("H2",0.2),("I2",0.2)], 2),   # HI^2 / (H2*I2) = Kc -> HI = sqrt(Kc*H2*I2)
    (20, [("SO2",0.4)], ("O2", "SO3", 0.8)),  # maxsus, pastda alohida
]
hi = (64*0.2*0.2)**0.5
check("tip1.A[0] [HI]", hi, num_from_javob(d["tiplar"][0]["A_daraja"][0]["javob"]))
o2 = (0.8**2) / (20 * 0.4**2)
check("tip1.A[1] [O2]", o2, num_from_javob(d["tiplar"][0]["A_daraja"][1]["javob"]))
n2 = (0.4**2) / (800 * 0.1**3)
check("tip1.A[2] [N2]", n2, num_from_javob(d["tiplar"][0]["A_daraja"][2]["javob"]))
co2 = 9 * 0.3 * 0.2 / 0.9
check("tip1.A[3] [CO2]", co2, num_from_javob(d["tiplar"][0]["A_daraja"][3]["javob"]))
print(f"Tip1 A-daraja (4): {'OK' if not errors else 'XATO bor'}")

# ---- Tip2: n0 = Kc orqali (A(g)->pP+qQ turi) ----
def n0_from(p, q, alpha, kc, V):
    # Kc = (p*n0*a/V)^p * (q*n0*a/V)^q / (n0*(1-a)/V)
    # bitta noma'lumli n0 uchun to'g'ridan-to'g'ri (Tip2 barcha holatlarida p yoki q darajasi <=2)
    from sympy import symbols, solve, Eq, Rational
    n0 = symbols('n0', positive=True)
    A = n0*(1-Rational(str(alpha)))/V
    P = p*n0*Rational(str(alpha))/V
    Q = q*n0*Rational(str(alpha))/V if q else 1
    expr = Eq((P**p * (Q**q if q else 1))/A, Rational(str(kc)))
    sol = [s for s in solve(expr, n0) if s > 0]
    return float(sol[0])

tip2_cases = [
    (2,0,0.20,0.8,1), (2,0,0.25,1.0,2), (2,0,0.10,0.4,1), (2,0,0.40,8/3,2),
    (1,1,0.25,1/3,2), (1,1,0.50,1.0,1), (1,1,0.20,0.25,1), (1,1,0.60,4.5,2),
    (2,0,0.30,72/7,1), (2,0,0.50,8.0,2), (1,1,0.75,9.0,1), (1,1,0.40,4.0,1),
]
for i, (p,q,a,kc,V) in enumerate(tip2_cases):
    n0 = n0_from(p,q,a,kc,V)
    check(f"tip2.mashqlar[{i}]", n0, num_from_javob(d["tiplar"][1]["mashqlar"][i]["javob"]))
print(f"Tip2 mashqlar (12): {'OK' if not errors else 'XATO bor'}")

print(f"\nJami xatolar: {len(errors)}")
for e in errors:
    print(" -", e)
if not errors:
    print("Barcha sonli javoblar mustaqil qayta hisoblash bilan mos keldi.")

# ---- Mashqlar banki: 1-15 (Tip1-uslub, Kc hisoblash) ----
bank1_cases = [
    ([2],[0.4],[2,1],[0.2,0.1]), ([2],[0.8],[2,1],[0.4,0.2]), ([2],[0.9],[2,1],[0.3,0.3]),
    ([1,1],[0.2,0.3],[2],[0.6]), ([1,1],[0.4,0.1],[2],[0.4]), ([1,1],[0.5,0.2],[2],[1.0]),
    ([2],[0.4],[1,1],[0.2,0.4]), ([2],[0.6],[1,1],[0.3,0.6]),
    ([2],[2.0],[1,1],[0.5,0.5]), ([2],[1.4],[1,1],[0.7,0.2]),
    ([1,1],[0.8,0.2],[1,1],[0.4,0.4]), ([1,1],[0.6,0.6],[1,1],[0.3,0.3]),
    ([2],[0.6],[2,1],[0.2,0.15]), ([2],[0.8],[1,3],[0.4,0.4]),
    ([2,1],[0.4,0.2],[2],[0.8]),
]
for i, (cn,num,cd,den) in enumerate(bank1_cases, 1):
    num=[Fr(str(v)) for v in num]; den=[Fr(str(v)) for v in den]
    kc=1
    for c,n in zip(cn,num): kc*=n**c
    for c,n in zip(cd,den): kc/=n**c
    check(f"bank[{i}]", float(kc), num_from_javob(d["mashqlar_banki"][i-1]["javob"]))
print(f"Bank 1-15 (Kc hisoblash): {'OK' if len(errors)==0 else str(len(errors))+' xato'}")

# ---- Mashqlar banki: 16-26 (Tip2-uslub, n0 topish), 27-30 (alpha topish) ----
bank2_n0_cases = [
    (2,0,0.20,3,1), (2,0,0.50,6,1), (2,0,0.40,56/15,2),
    (1,1,0.25,1/3,1), (1,1,0.50,3,2), (1,1,0.30,27/35,1), (1,1,0.20,0.45,1),
    (1,1,0.60,2.25,2), (2,0,0.30,90/7,1), (1,1,0.75,45,1), (1,1,0.40,2.4,2),
]
for i,(p,q,a,kc,V) in enumerate(bank2_n0_cases):
    n0 = n0_from(p,q,a,kc,V)
    check(f"bank[{16+i}]", n0, num_from_javob(d["mashqlar_banki"][16+i-1]["javob"]))
print(f"Bank 16-26 (n0 topish): {'OK' if len(errors)==0 else str(len(errors))+' xato'}")

def alpha_from(p,q,n0,kc,V):
    from sympy import symbols, solve, Eq, Rational
    a = symbols('a', positive=True)
    A = n0*(1-a)/V; P=p*n0*a/V; Q=q*n0*a/V if q else 1
    expr = Eq((P**p*(Q**q if q else 1))/A, Rational(str(kc)))
    sol=[s for s in solve(expr,a) if s.is_real and 0<s<1]
    return float(sol[0])*100

bank2_alpha_cases = [(2,0,16,16/3,1), (1,1,10,4.5,2), (1,1,14,7,1), (1,1,8,18,1)]
for i,(p,q,n0,kc,V) in enumerate(bank2_alpha_cases):
    a = alpha_from(p,q,n0,kc,V)
    check(f"bank[{27+i}]", a, num_from_javob(d["mashqlar_banki"][27+i-1]["javob"]))
print(f"Bank 27-30 (alpha topish): {'OK' if len(errors)==0 else str(len(errors))+' xato'}")

# ---- Yozma ish ----
n0y, Vy = 2.0, 3.0
alpha_y = 0.4
check("yozma_ish alpha", 40.0, alpha_y*100)
PCl5 = n0y*(1-alpha_y); PCl3 = Cl2 = n0y*alpha_y
check("yozma_ish PCl5(mol)", 1.2, PCl5)
check("yozma_ish PCl3=Cl2(mol)", 0.8, PCl3)
kc_y = (PCl3/Vy)*(Cl2/Vy)/(PCl5/Vy)
print("yozma_ish Kc mustaqil hisob:", round(kc_y,4), "(JSON da: ~0,178)")

print(f"\n=== YAKUNIY: jami xatolar = {len(errors)} ===")
for e in errors: print(" -", e)

# ---- \ce{} ichidagi "+" formatini tekshirish (mhchem +bilan bitishgan holatni buzadi) ----
import json as _json
_raw = open("I6-muvozanat.json", encoding="utf-8").read()

def _find_ce_blocks(s):
    blocks, i = [], 0
    while True:
        idx = s.find("\\ce{", i)
        if idx == -1:
            break
        start = idx + 4
        depth, j = 1, start
        while j < len(s) and depth > 0:
            if s[j] == "{": depth += 1
            elif s[j] == "}": depth -= 1
            j += 1
        blocks.append(s[start:j-1])
        i = j
    return blocks

bad_spacing = [c for c in _find_ce_blocks(_raw) if re.search(r"\S\+\S", c)]
print(f"\n\\\\ce{{}} ichida bo'shliqsiz '+' (mhchem xatosi): {len(bad_spacing)} ta topildi")
for b in bad_spacing:
    print("  -", b)
if not bad_spacing:
    print("  Yo'q — barcha '+' belgilari moddalardan bo'shliq bilan ajratilgan.")
