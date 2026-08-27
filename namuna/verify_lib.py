"""I.6 Kimyoviy muvozanat bobi uchun mashqlarni generatsiya qilish va IKKI MUSTAQIL
USUL bilan tekshirish: (1) sympy/Fraction bilan analitik yechim, (2) orqaga
qo'yish (natijani ICE jadvaliga qaytarib, Kc ni mustaqil qayta hisoblash).
"""
from fractions import Fraction as Fr
import sympy as sp

def tip1_kc(coeffs_num, concs_num, coeffs_den, concs_den):
    """Kc = prod(conc_num^coeff_num) / prod(conc_den^coeff_den) — Fraction bilan aniq."""
    num = Fr(1)
    for c, n in zip(coeffs_num, concs_num):
        num *= Fr(n) ** c
    den = Fr(1)
    for c, n in zip(coeffs_den, concs_den):
        den *= Fr(n) ** c
    kc = num / den
    return kc


def tip1_verify(coeffs_num, concs_num, coeffs_den, concs_den, kc):
    """2-usul: floatda mustaqil qayta hisoblash (boshqa yo'l — log yig'indisi orqali)."""
    import math
    log_num = sum(c * math.log(n) for c, n in zip(coeffs_num, concs_num))
    log_den = sum(c * math.log(n) for c, n in zip(coeffs_den, concs_den))
    kc_float = math.exp(log_num - log_den)
    return abs(kc_float - float(kc)) < 1e-9


def tip2_n0(p, q, alpha, Kc, V):
    """A(g) -> p*P(g) + q*Q(g), boshlang'ich faqat A, hajm V. n0 ni Kc dan topish."""
    n0 = sp.symbols('n0', positive=True)
    A = n0 * (1 - alpha) / V
    P = p * n0 * alpha / V
    Q = q * n0 * alpha / V if q else 1
    if q:
        expr = (P**p * Q**q) / A - Kc
    else:
        expr = (P**p) / A - Kc
    sol = sp.solve(sp.Eq(expr, 0), n0)
    sol = [s for s in sol if s.is_real and s > 0]
    assert len(sol) == 1, (p, q, alpha, Kc, V, sol)
    return sp.nsimplify(sol[0], rational=True)


def tip2_verify(p, q, alpha, Kc, V, n0):
    """2-usul: n0 ni ICE jadvaliga qo'yib, Kc ni mustaqil qayta hisoblash (orqaga qo'yish)."""
    n0 = float(n0)
    A = n0 * (1 - alpha) / V
    P = p * n0 * alpha / V
    Q = q * n0 * alpha / V
    kc_check = (P**p * (Q**q if q else 1)) / A
    ok_range = 0 < alpha < 1 and n0 > 0
    return abs(kc_check - Kc) < 1e-6 and ok_range


if __name__ == "__main__":
    # --- Tip 1 namunasi: H2 + I2 <=> 2HI ---
    kc = tip1_kc([2], [0.8], [1, 1], [0.1, 0.1])
    ok = tip1_verify([2], [0.8], [1, 1], [0.1, 0.1], kc)
    print("Tip1 namuna: Kc =", kc, "| tekshirildi:", ok)

    # --- Tip 2 namunasi (kalibrlash): PCl5 <=> PCl3 + Cl2, alpha=0.25, Kc=0.20, V=2 ---
    n0 = tip2_n0(p=1, q=1, alpha=0.25, Kc=Fr(20, 100), V=2)
    ok2 = tip2_verify(1, 1, 0.25, 0.20, 2, n0)
    print("Tip2 namuna: n0 =", n0, "mol | tekshirildi:", ok2)

    # --- Kalibrlash tasdig'i: N2O4 <=> 2NO2, alpha=0.10, Kc=0.4, V=1 (v01 8-savol qolipi) ---
    n0_calib = tip2_n0(p=2, q=0, alpha=0.10, Kc=Fr(2, 5), V=1)
    ok_calib = tip2_verify(2, 0, 0.10, 0.4, 1, n0_calib)
    print("Kalibrlash (v01 8-savol qolipi): n0 =", n0_calib, "| tekshirildi:", ok_calib,
          "| kutilgan javob 9 mol bilan mos:", abs(float(n0_calib) - 9) < 1e-6)
