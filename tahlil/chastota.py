#!/usr/bin/env python3
"""tahlil/v*.json fayllaridan chastota jadvalini yig'adi.

Ishlatish:  python3 tahlil/chastota.py
Yangi variant qo'shilganda faqat v0N.json qo'shiladi — skript qolganini o'zi qiladi.
"""
import glob
import json
import os
from collections import Counter, defaultdict

ELEMENTLAR = {
    "I.1": "Asosiy tushunchalar: mol, valentlik, allotropiya",
    "I.2": "Asosiy qonunlar: gaz qonunlari, Avogadro, ekvivalent",
    "I.3": "Atom tuzilishi, davriy sistema, kvant sonlar",
    "I.4": "Kimyoviy bog'lanish, gibridlanish, panjara",
    "I.5": "Reaksiya tezligi",
    "I.6": "Kimyoviy muvozanat, Le-Shatelye",
    "I.7": "Eritmalar, konsentratsiya, eruvchanlik",
    "I.8": "Dissotsiatsiya, pH, gidroliz",
    "I.9": "Oksidlanish darajasi, OQR",
    "I.10": "Elektroliz, Faradey",
    "II.1": "Anorganik sinflar, genetik bog'lanish",
    "II.2": "Oksid, asos, kislota, tuzlar",
    "II.3": "Metallar, IA guruh",
    "II.4": "IIA, IIIA, d-metallar, suv qattiqligi",
    "II.5": "Metallmaslar, vodorod, o'g'itlar",
    "III.1": "Tuzilish nazariyasi, izomeriya, alkanlar",
    "III.2": "Alkenlar, alkadiyenlar, alkinlar",
    "III.3": "Arenlar, neft, gaz",
    "III.4": "Spirtlar, fenollar",
    "III.5": "Aldegid va ketonlar",
    "III.6": "Karbon kislotalar",
    "III.7": "Efirlar, sovunlar, yog'lar",
    "III.8": "Uglevodlar",
    "III.9": "Aminlar, aminokislotalar, oqsillar",
    "III.10": "Polimerlar",
    "IV.1": "Laboratoriya jihozlari, ajratish usullari",
    "IV.2": "Sifat reaksiyalari, tajribalar",
}

TARTIB = list(ELEMENTLAR)


def yukla(katalog):
    fayllar = sorted(glob.glob(os.path.join(katalog, "v*.json")))
    variantlar = []
    for f in fayllar:
        with open(f, encoding="utf-8") as fh:
            variantlar.append(json.load(fh))
    return variantlar


def hisobla(variantlar):
    asosiy = Counter()
    qamrov = Counter()          # yozma ishlar orqali tegib o'tilgan mavzular
    orin = defaultdict(list)     # element -> savol raqamlari
    qiyinlik = defaultdict(list)
    for v in variantlar:
        for s in v["savollar"]:
            e = s["element"]
            asosiy[e] += 1
            orin[e].append(s["n"])
            qiyinlik[e].append(s["qiyinlik"])
            for q in s.get("qamrov", []):
                if q != e:
                    qamrov[q] += 1
    return asosiy, qamrov, orin, qiyinlik


def chiqar(variantlar):
    asosiy, qamrov, orin, qiyinlik = hisobla(variantlar)
    n = len(variantlar)
    print(f"Variantlar: {n}\n")
    sarlavha = "Element".ljust(7) + "Asosiy".rjust(8) + "Qo'shimcha".rjust(12) + "Qiyinlik".rjust(10) + "  Mavzu"
    print(sarlavha)
    print("-" * 96)
    for e in TARTIB:
        a = asosiy.get(e, 0)
        q = qamrov.get(e, 0)
        oq = sum(qiyinlik[e]) / len(qiyinlik[e]) if qiyinlik[e] else 0
        belgi = "  " if a else " !"
        print(f"{e:<7}{belgi}{a:>6} {q:>12} {oq:>10.1f}  {ELEMENTLAR[e]}")
    bosh = [e for e in TARTIB if not asosiy.get(e)]
    if bosh:
        print("\nBo'shliq — hech bir variantda asosiy mavzu sifatida chiqmagan:")
        for e in bosh:
            qq = f" (yozma ishda {qamrov[e]} marta tegib o'tilgan)" if qamrov.get(e) else ""
            print(f"  {e} — {ELEMENTLAR[e]}{qq}")
    print("\nSavol o'rinlari:")
    for e in TARTIB:
        if orin[e]:
            print(f"  {e:<7} {sorted(orin[e])}")


if __name__ == "__main__":
    katalog = os.path.dirname(os.path.abspath(__file__))
    vs = yukla(katalog)
    if not vs:
        raise SystemExit("v*.json topilmadi")
    chiqar(vs)
