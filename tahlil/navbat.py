# -*- coding: utf-8 -*-
"""Mavzulashtirilgan 43 talik testlarni QAYSI TARTIBDA yozish kerakligini
hisoblaydi (PROMT_MAVZU_VARIANT.md bo'yicha, har mazmun elementiga bitta test).

Tartib uchta o'lchovdan chiqadi — hammasi ko'rinadigan qilib chiqariladi,
"qora quti" ball emas:

  1. IMTIHON OG'IRLIGI  — v01 da shu elementdan nechta savol chiqqan
                          (tahlil/v01.json, chastota.py bilan bir xil manba)
  2. QIYINLIK           — o'sha savollarning o'rtacha qiyinligi (1-3)
  3. DARSLIK BO'SHLIG'I — maktab darsligi shu mavzuni qanchalik qoplaydi
                          (tahlil/darslik/*.json): yo'q=2, yuzaki=1, tanish=0.
                          "tanish, lekin imtihon darajasidan past to'xtaydi"
                          holati ham 1 ball oladi (darslik/README 2-topilma).
  4. YOZMA ISH          — v01 da shu element 25 ballik 41/42/43 topshirig'ini
                          bergan bo'lsa qo'shimcha vazn (eng qimmat savollar).

Ishlatish:  python3 tahlil/navbat.py
"""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

# --- 1-3: manba fayllardan o'qiladi -----------------------------------------
v01 = json.load(open(os.path.join(HERE, "v01.json"), encoding="utf-8"))["savollar"]

MAVZU = {}
ogirlik = defaultdict(int)
qiyinlik_yigindi = defaultdict(int)
yozma_beruvchi = set()

for s in v01:
    el = s["element"]
    ogirlik[el] += 1
    qiyinlik_yigindi[el] += s["qiyinlik"]
    MAVZU.setdefault(el, s.get("mavzu", ""))
    if s["n"] in (41, 42, 43):
        yozma_beruvchi.add(el)
    for q in s.get("qamrov", []):
        if q != el:
            ogirlik[q] += 1

# darslik qoplamasi
CHUQURLIK_BALL = {"yoq": 2, "yuzaki": 1, "tanish": 0}
qoplama = defaultdict(lambda: "yoq")
for sinf in (7, 8):
    p = os.path.join(HERE, "darslik", f"s{sinf:02d}.json")
    if not os.path.exists(p):
        continue
    for bob in json.load(open(p, encoding="utf-8")).get("boblar", []):
        for mv in bob.get("mavzular", []):
            el, ch = mv.get("element"), mv.get("chuqurlik", "yoq")
            if not el:
                continue
            # eng yaxshi (eng chuqur) qoplama saqlanadi
            if CHUQURLIK_BALL.get(ch, 2) < CHUQURLIK_BALL.get(qoplama[el], 2):
                qoplama[el] = ch

# darslik/README 2-topilma: "tanish", lekin imtihon darajasidan past to'xtaydi
PAST_TOXTAYDI = {"I.3", "I.4", "I.5", "I.6", "I.9"}

# spetsifikatsiyadagi 27 element (mavzu nomlari chastota.py bilan bir xil)
ELEMENTLAR = [
    ("I.1", "Asosiy tushunchalar: mol, valentlik, allotropiya"),
    ("I.2", "Asosiy qonunlar: gaz qonunlari, Avogadro, ekvivalent"),
    ("I.3", "Atom tuzilishi, davriy sistema, kvant sonlar"),
    ("I.4", "Kimyoviy bog'lanish, gibridlanish, panjara"),
    ("I.5", "Reaksiya tezligi"),
    ("I.6", "Kimyoviy muvozanat, Le-Shatelye"),
    ("I.7", "Eritmalar, konsentratsiya, eruvchanlik"),
    ("I.8", "Dissotsiatsiya, pH, gidroliz"),
    ("I.9", "Oksidlanish darajasi, OQR"),
    ("I.10", "Elektroliz, Faradey"),
    ("II.1", "Anorganik sinflar, genetik bog'lanish"),
    ("II.2", "Oksid, asos, kislota, tuzlar"),
    ("II.3", "Metallar, IA guruh"),
    ("II.4", "IIA, IIIA, d-metallar, suv qattiqligi"),
    ("II.5", "Metallmaslar, vodorod, o'g'itlar"),
    ("III.1", "Tuzilish nazariyasi, izomeriya, alkanlar"),
    ("III.2", "Alkenlar, alkadiyenlar, alkinlar"),
    ("III.3", "Arenlar, neft, gaz"),
    ("III.4", "Spirtlar, fenollar"),
    ("III.5", "Aldegid va ketonlar"),
    ("III.6", "Karbon kislotalar"),
    ("III.7", "Efirlar, sovunlar, yog'lar"),
    ("III.8", "Uglevodlar"),
    ("III.9", "Aminlar, aminokislotalar, oqsillar"),
    ("III.10", "Polimerlar"),
    ("IV.1", "Laboratoriya jihozlari, ajratish usullari"),
    ("IV.2", "Sifat reaksiyalari, tajribalar"),
]

# allaqachon yozilgan testlar (variantlar/mavzu_*.json -> "mavzu_I6" = "I.6")
def fayl_nomidan_element(nom):
    """'I6' -> 'I.6', 'II4' -> 'II.4', 'III10' -> 'III.10'"""
    harf = "".join(c for c in nom if c.isalpha()).upper()
    raqam = "".join(c for c in nom if c.isdigit())
    return f"{harf}.{raqam}" if harf and raqam else nom.upper()


TAYYOR = set()
vdir = os.path.join(HERE, "..", "variantlar")
if os.path.isdir(vdir):
    for f in os.listdir(vdir):
        if f.startswith("mavzu_") and f.endswith(".json"):
            TAYYOR.add(fayl_nomidan_element(f[len("mavzu_"):-len(".json")]))

rows = []
for el, mavzu in ELEMENTLAR:
    w = ogirlik.get(el, 0)
    q = (qiyinlik_yigindi[el] / ogirlik[el]) if ogirlik.get(el) else 0.0
    ch = qoplama[el]
    bosh = CHUQURLIK_BALL.get(ch, 2)
    if bosh == 0 and el in PAST_TOXTAYDI:
        bosh = 1  # "tanish", lekin imtihon darajasiga yetmaydi

    # Bitta variantda chiqmagan element "chiqmaydi" degani EMAS: n=1 da
    # tanlanma xatosi juda katta. Spetsifikatsiyada bor, demak imtihonda
    # chiqishi mumkin -- shuning uchun nol emas, minimal bitta savol va
    # o'sha bo'limning o'rtacha qiyinligi bilan hisoblanadi.
    tanlanmagan = (w == 0)
    if tanlanmagan:
        w = 1
        bolim = el.split(".")[0]
        oxsash = [r for e, r in qiyinlik_yigindi.items()
                  if e.split(".")[0] == bolim and ogirlik.get(e)]
        q = (sum(oxsash) / sum(ogirlik[e] for e in ogirlik
                               if e.split(".")[0] == bolim)) if oxsash else 2.0

    yozma = 1 if el in yozma_beruvchi else 0
    ball = 2 * w + 1.5 * q + 2 * bosh + 3 * yozma
    rows.append({
        "el": el, "mavzu": mavzu, "savol": w, "qiyinlik": q,
        "qoplama": ch, "bosh": bosh, "yozma": yozma, "ball": ball,
        "tanlanmagan": tanlanmagan,
    })

rows.sort(key=lambda r: (-r["ball"], r["el"]))

print("MAVZULASHTIRILGAN 43 TALIK TESTLAR — YOZISH NAVBATI")
print("(v01 kalibrlashi + 7-8-sinf darsligi qoplamasi asosida)\n")
print(f"{'#':<3} {'Element':<7} {'Savol':>5} {'Qiy.':>5} {'Darslik':>8} {'Yozma':>6} {'Ball':>6}  Mavzu")
print("-" * 112)
for i, r in enumerate(rows, 1):
    belgi = " ✅ tayyor" if r["el"] in TAYYOR else (" ⚠ v01 da chiqmagan" if r["tanlanmagan"] else "")
    savol = f"~{r['savol']}" if r["tanlanmagan"] else str(r["savol"])
    print(f"{i:<3} {r['el']:<7} {savol:>5} {r['qiyinlik']:>5.1f} "
          f"{r['qoplama']:>8} {('ha' if r['yozma'] else '-'):>6} {r['ball']:>6.1f}  {r['mavzu']}{belgi}")

print("\nBALL = 2×savol + 1,5×qiyinlik + 2×darslik_bo'shlig'i + 3×yozma_ish")
print("Darslik bo'shlig'i: yo'q=2 · yuzaki=1 · tanish=0 (past to'xtasa 1)")
print("⚠ = v01 da chiqmagan; n=1 tanlanma bo'lgani uchun nol emas, ~1 savol deb olindi")
if TAYYOR:
    print(f"\n✅ tayyor: {', '.join(sorted(TAYYOR))}")
print(f"Qolgan: {len(rows) - len([r for r in rows if r['el'] in TAYYOR])} ta test")
