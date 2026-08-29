# -*- coding: utf-8 -*-
"""9-bob B-varianti: Oksidlanish-qaytarilish reaksiyalari (I.9) — HAQIQIY MS MUHITI ★★★.
Elektron balans, koeffitsiyentlar yig'indisi, mol-massa hisoblari, disproporsiya.
Tongotarov OQR banki arxetiplari — barcha javoblar mustaqil qayta hisoblangan."""
import json, random

OUT = "mavzu_I9B.json"
CHECKS = []
def check(name, got, expected, tol=0.05):
    ok = abs(got - expected) <= tol
    CHECKS.append((name, got, expected, ok))
    return ok

Y1 = []
def q(d, k, savol, correct, distractors, yechim, params=None, svg=None, fig=None):
    Y1.append(dict(qiyinlik=d, kognitiv=k, savol=savol, correct=correct,
                   distractors=distractors, yechim=yechim,
                   parametrlar=params or {}, svg=svg, fig=fig))

# 1 (3) — o'ng koeffitsiyentlar yig'indisi (Cr2O7/H2S)
check("q1", 1+3+1+7, 12)
q(3, "yuqori",
  "H₂S + H₂SO₄ + K₂Cr₂O₇ → Cr₂(SO₄)₃ + S + K₂SO₄ + H₂O reaksiyasi tenglashtirilganda O'NG tomondagi "
  "koeffitsiyentlar yig'indisini aniqlang.",
  "12", [("8", "chap tomon yig'indisi"), ("17", "xato balans (suvni 12 olib)"),
          ("7", "suv koeffitsiyenti unutilgan holda")],
  "Balans: K₂Cr₂O₇ + 3H₂S + 4H₂SO₄ → Cr₂(SO₄)₃ + 3S + K₂SO₄ + 7H₂O. O'ng: 1+3+1+7 = 12. "
  "(Cr⁺⁶+3e ×2; S⁻²−2e ×3.)",
  dict(arch="koeff_ong", summa=12))

# 2 (3) — jami koeffitsiyentlar (KMnO4+HCl)
check("q2", 2+16+2+2+5+8, 35)
q(3, "yuqori",
  "KMnO₄ + HCl(kons) → KCl + MnCl₂ + Cl₂ + H₂O reaksiyasi tenglashtirilganda BARCHA "
  "koeffitsiyentlar yig'indisini toping.",
  "35", [("18", "faqat chap tomon"), ("17", "faqat o'ng tomon"),
          ("33", "Cl₂ oldida 4 olingan xato balans")],
  "2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O. Jami: 2+16+2+2+5+8 = 35. (Mn⁺⁷+5e ×2; 2Cl⁻−2e ×5.)",
  dict(arch="koeff_jami", summa=35))

# 3 (2) — oksidlanish darajasi
q(2, "yuqori",
  "K₂Cr₂O₇ birikmasida xromning oksidlanish darajasini aniqlang.",
  "+6", [("+3", "Cr₂(SO₄)₃ dagi qiymat"), ("+7", "guruh raqami bilan chalkashuv (Mn kabi)"),
          ("+2", "kaliy koeffitsiyentidan chalkashuv")],
  "2(+1) + 2x + 7(−2) = 0 → 2x = 12 → x = +6.",
  dict(arch="daraja_aniqlash"))

# 4 (3) — 1-2-3: qaysi jarayonlar OQR
q(3, "yuqori",
  "Quyidagi jarayonlarning qaysilari oksidlanish-qaytarilish reaksiyalariga mansub?\n"
  "1) elektroliz;  2) gidroliz;  3) yonish;  4) neytrallanish;  5) korroziya.",
  "1, 3 va 5",
  [("1, 2 va 4", "gidroliz va neytrallanishda darajalar o'zgarmaydi"),
   ("2, 4 va 5", "gidroliz/neytrallanish OQR emas, 1 va 3 esa OQR"),
   ("faqat 3 va 5", "elektroliz ham elektrodlardagi OQR jarayonidir")],
  "Elektroliz, yonish, korroziya — darajalar o'zgaradi (OQR); gidroliz va neytrallanish — almashinish.",
  dict(arch="oqr_tanlov"))

# 5 (3) — JADVALLI: darajalar jadvalidan qaytaruvchini topish
q(3, "yuqori",
  "Reaksiyada uch element darajalarining o'zgarishi jadvalda berilgan:\n"
  "[JADVAL] Element | S | Mn | N ;; boshlang'ich | −2 | +7 | +3 ;; oxirgi | 0 | +2 | +5\n"
  "Qaysi element(lar) QAYTARUVCHI bo'lgan?",
  "S va N", [("faqat Mn", "Mn daraja pasaytirgan — u oksidlovchi"),
              ("faqat S", "N ham e bergan (+3 → +5)"),
              ("Mn va N", "Mn e olgan, qaytaruvchi emas")],
  "Qaytaruvchi — e beruvchi (daraja ortadi): S(−2→0) va N(+3→+5). Mn(+7→+2) — oksidlovchi.",
  dict(arch="jadval_daraja"))

# 6 (3) — mol nisbat (elektron balans orqali)
check("q6", 0.5*5/2, 1.25)
q(3, "yuqori",
  "KNO₂ + KMnO₄ + H₂SO₄ → KNO₃ + MnSO₄ + K₂SO₄ + H₂O reaksiyasida 0,5 mol oksidlovchi ishtirok etgan "
  "bo'lsa, sarflangan qaytaruvchining miqdorini (mol) toping.",
  "1,25", [("0,75", "nisbat 3:2 deb olingan"), ("2,5", "5 mol qaytaruvchi 1 mol oksidlovchiga deb olingan"),
            ("0,2", "teskari nisbat")],
  "Balans: 5KNO₂ + 2KMnO₄ + 3H₂SO₄ → ... (N: −2e ×5; Mn: +5e ×2). 0,5·5/2 = 1,25 mol KNO₂.",
  dict(arch="mol_nisbat", oks=0.5))

# 7 (3) — massa hisobi (qaytaruvchidan oksidlovchi)
check("q7", 1*2/5*158, 63.2)
q(3, "yuqori",
  "Yuqoridagi (6-savoldagi) reaksiyada 1 mol qaytaruvchi ishtirok etgan bo'lsa, sarflangan "
  "oksidlovchining massasini (g) aniqlang. (M(KMnO₄)=158)",
  "63,2", [("158", "1:1 nisbat olingan"), ("31,6", "0,2 mol deb olingan"),
            ("395", "5:2 nisbat teskari qo'llangan")],
  "KMnO₄ = 1·2/5 = 0,4 mol → 0,4·158 = 63,2 g.",
  dict(arch="massa_oks", qay=1))

# 8 (2) — faqat qaytaruvchi zarracha
q(2, "yuqori",
  "Quyidagi zarrachalardan qaysi biri FAQAT qaytaruvchi bo'la oladi?",
  "S²⁻", [("SO₄²⁻ (S⁺⁶)", "eng yuqori daraja — faqat oksidlovchi"),
           ("SO₃²⁻ (S⁺⁴)", "oraliq daraja — ikkala vazifada ham"),
           ("S⁰", "oraliq daraja — ikkala vazifada ham")],
  "S²⁻ — oltingugurtning eng past darajasi: faqat e berishi (oksidlanishi) mumkin.",
  dict(arch="faqat_qaytaruvchi"))

# 9 (2) — disproporsiya turi
q(2, "yuqori",
  "Cl₂ + 2KOH(sovuq) → KCl + KClO + H₂O reaksiyasi qaysi turga mansub?",
  "disproporsiya (o'z-o'zidan oksidlanish-qaytarilish)",
  [("molekulyararo OQR", "oksidlovchi ham, qaytaruvchi ham bitta element — Cl⁰"),
   ("ichki molekulyar OQR", "bir molekula ichidagi ikki xil element emas"),
   ("almashinish reaksiyasi", "darajalar o'zgaryapti: 0 → −1 va +1")],
  "Cl⁰ ning bir qismi −1 ga (qaytarildi), bir qismi +1 ga (oksidlandi) o'tdi — disproporsiya.",
  dict(arch="disproporsiya_turi"))

# 10 (3) — elektron soni (Na birligida)
check("q10", 0.2*3, 0.6)
q(3, "yuqori",
  "0,2 mol alyuminiy to'liq oksidlanib Al³⁺ ga o'tganda nechta elektron beradi?",
  "0,6·Nₐ", [("0,2·Nₐ", "har atom 3 tadan e berishi unutilgan"), ("1,8·Nₐ", "3² xato ko'paytirilgan"),
              ("3·Nₐ", "mol soni e'tiborga olinmagan")],
  "n(e) = 0,2·3 = 0,6 mol → 0,6·Nₐ ta elektron.",
  dict(arch="elektron_soni", mol=0.2, n=3))

# 11 (3) — alkan-elektron (bank arxetipi)
check("q11", (76/2 - 2)/6, 6, tol=0.001)  # 2(6n+2)=76 -> n=6
q(3, "yuqori",
  "Diagrammada ba'zi alkanlarning 1 moli to'liq yonganda oksidlovchiga beradigan elektron mollari "
  "ko'rsatilgan. 2 mol noma'lum alkan yondirilganda oksidlovchi qaytaruvchidan 76·Nₐ ta elektron "
  "olgan bo'lsa, diagrammadan foydalanib alkanni aniqlang.",
  "geksan", [("pentan", "diagrammada 32: 2·32=64 ≠ 76"), ("geptan", "diagrammada 44: 2·44=88 ≠ 76"),
              ("oktan", "diagrammada 50: 2·50=100 ≠ 76")],
  "1 mol uchun 76/2 = 38 mol e kerak — diagrammada 38 geksanga mos. (Tekshiruv: 6n+2=38 → n=6.)",
  dict(arch="alkan_elektron", e=76, mol=2), fig="bar_alkan")

# 12 (3) — reaksiyani davom ettirish
check("q12", 2+1+2+1+2, 8)
q(3, "yuqori",
  "FeCl₃ + H₂S → ... reaksiyasini davom ettiring va barcha koeffitsiyentlar yig'indisini aniqlang.",
  "8", [("6", "HCl koeffitsiyenti unutilgan"), ("5", "faqat chap tomon"),
         ("11", "Fe⁺³ Fe⁰ gacha qaytariladi deb olingan")],
  "2FeCl₃ + H₂S → 2FeCl₂ + S + 2HCl (Fe⁺³+1e ×2; S⁻²−2e ×1). Jami: 2+1+2+1+2 = 8.",
  dict(arch="davom_ettirish", summa=8))

# 13 (3) — qaytaruvchi va oksidlovchi koeffitsiyentlari
q(3, "yuqori",
  "K₂Cr₂O₇ + FeSO₄ + H₂SO₄ → K₂SO₄ + Cr₂(SO₄)₃ + Fe₂(SO₄)₃ + H₂O reaksiyasida QAYTARUVCHI va "
  "OKSIDLOVCHI oldidagi koeffitsiyentlarni mos ravishda aniqlang.",
  "6 va 1", [("1 va 6", "qaytaruvchi FeSO₄ (Fe⁺²), oksidlovchi K₂Cr₂O₇ — teskari olingan"),
              ("2 va 3", "elektron balans nisbatidan xato"), ("6 va 7", "7 — kislota koeffitsiyenti")],
  "Fe⁺²−1e ×6; Cr₂⁺⁶+6e ×1 → K₂Cr₂O₇ + 6FeSO₄ + 7H₂SO₄ → ... Qaytaruvchi 6, oksidlovchi 1.",
  dict(arch="qay_oks_koeff"))

# 14 (2) — 1-2-3: qaysi o'zgarishlar oksidlanish
q(2, "yuqori",
  "Quyidagi o'zgarishlarning qaysilari OKSIDLANISH jarayoniga mansub?\n"
  "1) S⁻² → S⁺⁴;  2) N⁺⁵ → N⁺²;  3) Al⁰ → Al⁺³;  4) Cu⁺² → Cu⁰.",
  "1 va 3",
  [("2 va 4", "bular qaytarilish (daraja pasayadi)"),
   ("1 va 2", "2-o'zgarishda daraja pasayadi — qaytarilish"),
   ("faqat 3", "1-o'zgarish ham oksidlanish (−2 → +4)")],
  "Oksidlanish — daraja ortishi: 1 (−2→+4) va 3 (0→+3). 2 va 4 — qaytarilish.",
  dict(arch="oksidlanish_tanlov"))

# 15 (3) — Cu + HNO3 suyultirilgan
check("q15", 3+8+3+2+4, 20)
q(3, "yuqori",
  "Cu + HNO₃(suyul.) → Cu(NO₃)₂ + NO + H₂O reaksiyasi tenglashtirilganda barcha koeffitsiyentlar "
  "yig'indisini toping.",
  "20", [("13", "kons. kislota (NO₂) balansi bilan chalkashuv"), ("11", "faqat chap tomon"),
          ("9", "faqat o'ng tomon")],
  "3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO + 4H₂O (Cu−2e ×3; N⁺⁵+3e ×2). Jami: 3+8+3+2+4 = 20.",
  dict(arch="cu_hno3_koeff"))

# 16 (2) — eng kuchli oksidlovchi galogen
q(2, "yuqori",
  "Galogenlar orasida ENG KUCHLI oksidlovchi qaysi?",
  "F₂", [("Cl₂", "elektromanfiyligi ftordan past"), ("Br₂", "davr bo'yicha oksidlovchilik pasayadi"),
          ("I₂", "eng kuchsiz oksidlovchi galogen")],
  "Ftor — eng elektromanfiy element: elektronni eng kuchli tortadi, faqat oksidlovchi bo'ladi.",
  dict(arch="oks_kuch"))

# 17 (3) — JADVALLI: elektron balans «?» kataklari
q(3, "yuqori",
  "Zn + HNO₃(juda suyul.) → Zn(NO₃)₂ + NH₄NO₃ + H₂O reaksiyasining elektron balansi jadvalda:\n"
  "[JADVAL] Yarim reaksiya | Ko'paytiruvchi ;; Zn⁰ − 2e → Zn⁺² | ? ;; N⁺⁵ + 8e → N⁻³ | ?\n"
  "«?» o'rnidagi ko'paytiruvchilarni mos ravishda aniqlang.",
  "4 va 1", [("1 va 4", "e soni teskari taqsimlangan"), ("2 va 8", "qisqartirilmagan nisbat"),
              ("8 va 2", "e sonlarining o'zi yozilgan")],
  "EKUK(2,8) = 8 → Zn uchun 8/2 = 4, N uchun 8/8 = 1. (4Zn + 10HNO₃ → 4Zn(NO₃)₂ + NH₄NO₃ + 3H₂O.)",
  dict(arch="balans_jadval"))

# 18 (2) — NH4NO3 dagi ikkala azot
q(2, "yuqori",
  "NH₄NO₃ tarkibidagi azot atomlarining oksidlanish darajalarini aniqlang.",
  "−3 va +5", [("+3 va −5", "ishoralar teskari"), ("ikkalasi ham 0", "azotning erkin holati emas"),
                ("−3 va +3", "nitrat azoti +5 bo'ladi")],
  "NH₄⁺ da N = −3; NO₃⁻ da N = +5 — bitta tuzda ikki xil daraja.",
  dict(arch="ikki_daraja"))

# 19 (3) — massa hisobi (KMnO4 dan Cl2)
check("q19", 0.5*2/5*158, 31.6)
q(3, "yuqori",
  "2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O reaksiyasi bo'yicha 0,5 mol xlor olish uchun "
  "necha gramm KMnO₄ kerak? (M=158)",
  "31,6", [("79", "1:1 nisbat olingan"), ("63,2", "0,4 mol deb olingan"),
            ("15,8", "0,1 mol — nisbat teskari qo'llangan")],
  "n(KMnO₄) = 0,5·2/5 = 0,2 mol → 0,2·158 = 31,6 g.",
  dict(arch="massa_kmno4"))

# 20 (2) — ichki molekulyar OQR
q(2, "yuqori",
  "NH₄NO₃ →(t) N₂O + 2H₂O parchalanishi qaysi turdagi OQR?",
  "ichki molekulyar",
  [("molekulyararo", "oksidlovchi va qaytaruvchi bitta molekula ichida"),
   ("disproporsiya", "bir xil daraja ikkiga ajralmayapti — ikki xil N birlashyapti"),
   ("OQR emas", "N darajalari o'zgaradi: −3 va +5 → +1")],
  "Oksidlovchi (N⁺⁵) va qaytaruvchi (N⁻³) bitta molekula ichida — ichki molekulyar OQR.",
  dict(arch="ichki_molekulyar"))

# 21 (3) — As2S3 + HNO3 (murakkab balans)
check("q21", 0.3*22/3*63, 138.6)
q(3, "yuqori",
  "As₂S₃ + HNO₃ → H₃AsO₄ + SO₂ + NO₂ + H₂O reaksiyasida 0,3 mol SO₂ hosil bo'lgan bo'lsa, "
  "oksidlovchining massasini (g) toping. (M(HNO₃)=63)",
  "138,6", [("126", "20 mol nisbat olingan"), ("246", "N ning hammasi hisoblangan emas balans xato"),
             ("492", "ikki barobar xato")],
  "As₂S₃ 22 e beradi (As: 2e×2, S: 6e×3) → As₂S₃ + 22HNO₃ → 2H₃AsO₄ + 3SO₂ + 22NO₂ + 8H₂O. "
  "HNO₃ = 0,3·22/3 = 2,2 mol → 138,6 g.",
  dict(arch="murakkab_balans"))

# 22 (3) — 1-2-3: disproporsiya reaksiyalari
q(3, "yuqori",
  "Quyidagi reaksiyalarning qaysilari DISPROPORSIYAGA misol bo'ladi?\n"
  "1) Cl₂ + H₂O → HCl + HClO;  2) 3NO₂ + H₂O → 2HNO₃ + NO;\n"
  "3) Fe + CuSO₄ → FeSO₄ + Cu;  4) 4KClO₃ → 3KClO₄ + KCl.",
  "1, 2 va 4",
  [("1 va 3", "3 — molekulyararo OQR (ikki xil element)"),
   ("faqat 1", "2 da N⁺⁴ → +5 va +2; 4 da Cl⁺⁵ → +7 va −1 — ular ham disproporsiya"),
   ("2, 3 va 4", "3 disproporsiya emas; 1 esa disproporsiya")],
  "1: Cl⁰→−1/+1; 2: N⁺⁴→+5/+2; 4: Cl⁺⁵→+7/−1 — bir element ikkiga ajraladi. 3 — oddiy o'rin olish.",
  dict(arch="disprop_tanlov"))

# 23 (3) — parametrli (alkan + H2 aralashma)
check("q23", 0.2*(3+1)+0.2, 1.0)
q(3, "yuqori",
  "Teng mol nisbatda olingan alkan va vodoroddan iborat 0,4 mol aralashma yondirilganda 1 mol suv "
  "hosil bo'ldi. Alkanni aniqlang.",
  "propan", [("etan", "n=2: 0,2·3+0,2 = 0,8 mol suv"), ("metan", "n=1: 0,6 mol suv"),
              ("butan", "n=4: 1,2 mol suv")],
  "0,2 mol CₙH₂ₙ₊₂ + 0,2 mol H₂: suv = 0,2(n+1) + 0,2 = 1 → n = 3 → propan.",
  dict(arch="parametrli_alkan"))

# 24 (2) — qaytaruvchini topish
q(2, "yuqori",
  "MnO₂ + 4HCl → MnCl₂ + Cl₂ + 2H₂O reaksiyasida QAYTARUVCHI vazifasini qaysi zarracha bajaradi?",
  "HCl tarkibidagi Cl⁻",
  [("MnO₂", "Mn⁺⁴ e oladi — u oksidlovchi"), ("H⁺", "vodorod darajasi o'zgarmaydi (+1)"),
   ("H₂O", "mahsulot qaytaruvchi bo'la olmaydi")],
  "Cl⁻(−1) → Cl₂(0): e berdi — qaytaruvchi. Mn⁺⁴ → Mn⁺²: e oldi — oksidlovchi.",
  dict(arch="qaytaruvchi_topish"))

# 25 (3) — atom soni hisobi (AuCl3 + H2O2)
check("q25", 13.44/22.4*2/3, 0.4)
q(3, "yuqori",
  "2AuCl₃ + 3H₂O₂ + 6KOH → 2Au + 3O₂ + 6KCl + 6H₂O reaksiyasida 13,44 l (n.sh.) gaz ajraldi. "
  "Qaytarilgan oltin atomlarining sonini aniqlang.",
  "2,408·10²³", [("6,02·10²³", "1 mol deb olingan"), ("9,03·10²²", "0,15 mol xato nisbat"),
                  ("1,204·10²³", "O₂ bilan 1:1 nisbat olingan")],
  "O₂ = 0,6 mol → Au = 0,6·2/3 = 0,4 mol → 0,4·6,02·10²³ = 2,408·10²³ ta atom.",
  dict(arch="atom_soni"))

# 26 (3) — disproporsiya hisobi (KClO3)
check("q26", 0.4*3/4, 0.3)
q(3, "yuqori",
  "4KClO₃ →(t) 3KClO₄ + KCl disproporsiya reaksiyasida 0,4 mol KClO₃ dan necha mol KClO₄ hosil bo'ladi?",
  "0,3", [("0,4", "1:1 nisbat olingan"), ("0,1", "KCl miqdori topilgan"),
           ("1,2", "nisbat teskari ko'paytirilgan")],
  "Nisbat 4:3 → 0,4·3/4 = 0,3 mol KClO₄.",
  dict(arch="disprop_hisob"))

# 27 (3) — RASMLI: grafikdan metallni aniqlash
check("q27", 0.6/0.2, 3)
q(3, "yuqori",
  "Rasmda metall oksidlanayotganda bergan elektron mollari metall mol soniga bog'liq holda "
  "ko'rsatilgan. Grafikdan foydalanib, metallning valentligini va mos metallni aniqlang.",
  "3; alyuminiy", [("2; magniy", "grafikda 0,2 mol → 0,6 mol e (nisbat 3)"),
                    ("1; natriy", "nisbat 3 ekani e'tiborga olinmagan"),
                    ("3; temir (faqat +3)", "grafik istalgan +3 metall deydi, lekin Fe odatda aralash; eng mosi Al")],
  "Grafikdan: 0,2 mol metall → 0,6 mol e → n = 3. Doimiy +3 valentli yengil metall — Al.",
  dict(arch="grafik_metall"), fig="e_graph")

# 28 (2) — RASMLI: Cu + HNO3 kons (qo'ng'ir gaz)
q(2, "yuqori",
  "Rasmda mis parchasi konsentrlangan nitrat kislotaga tushirilganda qo'ng'ir gaz ajralishi "
  "ko'rsatilgan. Bu gaz va undagi azotning oksidlanish darajasi qaysi javobda to'g'ri?",
  "NO₂; +4", [("NO; +2", "NO — rangsiz gaz, suyultirilgan kislotada ajraladi"),
               ("N₂O; +1", "«kuldiruvchi gaz» rangsiz"), ("NH₃; −3", "ammiak kislotada ajralib chiqmaydi")],
  "Kons. HNO₃ misni oksidlaganda qo'ng'ir NO₂ (N⁺⁴) ajraladi: Cu + 4HNO₃ → Cu(NO₃)₂ + 2NO₂ + 2H₂O.",
  dict(arch="qongir_gaz"), fig="cu_hno3")

# 29 (3) — JADVALLI: KMnO4 muhitga qarab
q(3, "yuqori",
  "Permanganat-ionning turli muhitlardagi qaytarilish mahsulotlari jadvalda berilgan:\n"
  "[JADVAL] Muhit | Mahsulot | Olingan e soni ;; kislotali | Mn²⁺ | ? ;; neytral | MnO₂ | ? ;; ishqoriy | MnO₄²⁻ | ?\n"
  "«?» o'rnidagi elektron sonlarini mos ravishda aniqlang.",
  "5, 3 va 1", [("3, 5 va 1", "kislotalida +7→+2 — bu 5e"), ("5, 3 va 2", "ishqoriyda +7→+6 — 1e"),
                 ("7, 4 va 6", "darajalarning o'zi emas, farqi olinadi")],
  "Mn⁺⁷ → Mn⁺² (5e); → Mn⁺⁴ (3e); → Mn⁺⁶ (1e).",
  dict(arch="muhit_jadval"))

# 30 (2) — H2O2 dagi kislorod
q(2, "yuqori",
  "Vodorod peroksid (H₂O₂) tarkibidagi kislorodning oksidlanish darajasi qanday?",
  "−1", [("−2", "oddiy oksidlardagi qiymat"), ("0", "erkin kisloroddagi qiymat"),
          ("+2", "faqat OF₂ da bo'ladi")],
  "Peroksid ko'prigi −O−O−: har bir O ning darajasi −1. Shu sababli H₂O₂ ham oksidlovchi, ham qaytaruvchi.",
  dict(arch="peroksid_daraja"))

# 31 (3) — elektron mollari hisobi
check("q31", 5.6/56*2, 0.2)
q(3, "yuqori",
  "5,6 g temir xlorid kislota bilan to'liq reaksiyaga kirishdi (Fe → Fe⁺²). Bunda temir bergan "
  "elektronlar sonini aniqlang.",
  "1,204·10²³", [("6,02·10²³", "1 mol e deb olingan"), ("2,408·10²³", "Fe⁺³ deb olingan (0,3 mol e xato ham emas: 1,806)"),
                  ("3,01·10²²", "0,05 mol e — massa xato")],
  "n(Fe) = 0,1 mol → e = 0,2 mol → 0,2·6,02·10²³ = 1,204·10²³ ta.",
  dict(arch="fe_elektron"))

# 32 (3) — RASMLI: shu grafikdan ikkinchi o'qish
check("q32", 0.3*3, 0.9)
q(3, "yuqori",
  "27-savoldagi grafikdan foydalaning: 0,3 mol metall to'liq oksidlanganda necha mol elektron beradi?",
  "0,9", [("0,3", "valentlik hisobga olinmagan"), ("0,6", "0,2 mol uchun qiymat"),
           ("1,2", "n=4 xato o'qilgan")],
  "Grafik nisbati 3 → 0,3·3 = 0,9 mol elektron.",
  dict(arch="grafik_oqish2"), fig="e_graph")

# ---------- Y2: Cu + HNO3 ikki tajriba ----------
check("y2_33", 0.3*8/3, 0.8)
check("y2_34", 0.3*2/3*22.4, 4.48)
check("y2_35", 0.3*2*22.4, 13.44)
Y2 = dict(
  n=33, tur="Y2", element="I.9",
  ichki_pasport=[dict(n=33, element="I.9", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.9", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.9", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Laboratoriyada 0,3 mol mis bilan ikki tajriba o'tkazildi: 1-tajribada u SUYULTIRILGAN "
               "(3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO + 4H₂O), 2-tajribada KONSENTRLANGAN "
               "(Cu + 4HNO₃ → Cu(NO₃)₂ + 2NO₂ + 2H₂O) nitrat kislotada to'liq eritildi. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. 1-tajribada necha mol kislota sarflangan?",
    "34. 1-tajribada ajralgan gazning hajmi (l, n.sh.) qancha?",
    "35. 2-tajribada ajralgan gazning hajmi (l, n.sh.) qancha?"],
  javoblar_royxati=["A) 4,48", "B) 0,8", "C) 6,72", "D) 13,44", "E) 0,6", "F) 0,4"],
  javoblar={"33": "B", "34": "A", "35": "D"},
  chalgituvchilar=[dict(variant="C", xato="0,3 mol NO deb hisoblash xatosi"),
                   dict(variant="E", xato="NO₂ mollari (0,6) hajmga aylantirilmagan"),
                   dict(variant="F", xato="kislota mollarini 4 ga bo'lish xatosi")],
  yechim=("33: HNO₃ = 0,3·8/3 = 0,8 mol (B). 34: NO = 0,2 mol → 4,48 l (A). "
          "35: NO₂ = 0,6 mol → 13,44 l (D)."),
  parametrlar=dict(arch="cu_hno3_ssenariy", cu=0.3))

# ---------- O1 ----------
check("o36", 4+2, 6)
check("o37", 0.1*5/2*22.4, 5.6)
check("o38", 6.2/31*5*22.4, 22.4)
check("o39", 5.4/(0.6/3), 27)
check("o40", 4+11+2+8, 25)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="S⁺⁴ → S⁻² o'zgarishida oltingugurt atomi nechta elektron biriktiradi?",
      javob="6", yechim="Daraja +4 dan −2 gacha pasaydi: 4 − (−2) = 6 e.",
      parametrlar=dict(arch="e_farq")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O. 0,1 mol KMnO₄ dan olinadigan xlorning "
            "hajmini (l, n.sh.) toping.",
      javob="5,6", yechim="Cl₂ = 0,1·5/2 = 0,25 mol → 0,25·22,4 = 5,6 l.",
      parametrlar=dict(arch="hajm_cl2")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="6,2 g fosfor konsentrlangan nitrat kislotada H₃PO₄ gacha oksidlandi (P − 5e). Ajralgan "
            "NO₂ ning hajmini (l, n.sh.) toping. (M(P)=31)",
      javob="22,4", yechim="P = 0,2 mol → e = 1 mol → NO₂ (1e) = 1 mol → 22,4 l.",
      parametrlar=dict(arch="p_hno3")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="5,4 g uch valentli metall to'liq oksidlanganda 0,6 mol elektron berdi. Metallning molyar "
            "massasini (g/mol) toping.",
      javob="27", yechim="n(Me) = 0,6/3 = 0,2 mol → M = 5,4/0,2 = 27 g/mol (Al).",
      parametrlar=dict(arch="metall_teskari")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="FeS₂ + O₂ → Fe₂O₃ + SO₂ reaksiyasi tenglashtirilganda barcha koeffitsiyentlar "
            "yig'indisini toping.",
      javob="25", yechim="4FeS₂ + 11O₂ → 2Fe₂O₃ + 8SO₂ (Fe⁺²→Fe⁺³, S⁻¹→S⁺⁴: 11e ×4; O₂ +4e ×11). "
            "Jami: 4+11+2+8 = 25.",
      parametrlar=dict(arch="fes2_koeff")),
]

# ---------- O2 ----------
check("o41b", 15.8/158*5/2, 0.25)
check("o41c", 0.25*22.4, 5.6)
check("o41d", 15.8/158*16/2*36.5, 29.2)
check("o43b", 13/65*64, 12.8)
check("o43c", 13/65*2, 0.4)
O2 = [
 dict(n=41, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada xlor olish uchun 15,8 g kaliy permanganat konsentrlangan xlorid kislota "
            "bilan reaksiyaga kiritildi: KMnO₄ + HCl → KCl + MnCl₂ + Cl₂ + H₂O. "
            "Bandlar ketma-ket yechiladi. (M(KMnO₄)=158, M(HCl)=36,5)"),
      bandlar=[
        dict(savol="a) Reaksiyani elektron balans usulida tenglashtiring.",
             yechim=["Mn⁺⁷+5e ×2; 2Cl⁻−2e ×5 → 2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O"], M=4, A=1),
        dict(savol="b) Hosil bo'ladigan xlorning miqdorini (mol) toping.",
             yechim=["n(KMnO₄) = 0,1 mol → Cl₂ = 0,1·5/2 = 0,25 mol"], M=3, A=2),
        dict(savol="c) Xlorning hajmini (l, n.sh.) hisoblang.",
             yechim=["V = 0,25·22,4 = 5,6 l"], M=2, A=2),
        dict(savol="d) Sarflangan kislotaning massasini (g) toping.",
             yechim=["HCl = 0,1·16/2 = 0,8 mol → 29,2 g"], M=3, A=3),
        dict(savol="e) Bu reaksiyada HCl qanday IKKI vazifani bajaradi? Izohlang.",
             yechim=["16 HCl dan 10 tasi qaytaruvchi (Cl⁻ → Cl₂), 6 tasi muhit — tuz hosil qiladi",
                     "(KCl, MnCl₂ tarkibiga kiradi)."], M=3, A=2),
      ],
      rasmiylashtirish="Elektron balans zanjiri: tenglashtirish → mol → hajm → massa → ikki vazifa izohi; M15+A10.",
      parametrlar=dict(arch="kmno4_zanjir", m=15.8)),
 dict(n=42, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Sxemadagi X₁ va X₂ moddalarni aniqlab, quyidagilarni bajaring:\n"
            "KMnO₄ —(+HCl kons.)→ X₁(sariq-yashil gaz) —(+KOH, sovuq)→ X₂ —(t°)→ KClO₃"),
      bandlar=[
        dict(savol="a) X₁ va X₂ ni aniqlab, 1- va 2-reaksiya tenglamalarini tenglashtirilgan holda yozing.",
             yechim=["X₁ = Cl₂, X₂ = KClO. 2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 5Cl₂ + 8H₂O;",
                     "Cl₂ + 2KOH → KCl + KClO + H₂O"], M=13, A=0),
        dict(savol="b) 3-reaksiya (X₂ → KClO₃) tenglamasini tenglashtirilgan holda yozing.",
             yechim=["3KClO →(t) 2KCl + KClO₃ (Cl⁺¹ → −1 va +5 — disproporsiya)"], M=9, A=0),
        dict(savol="c) Zanjirdagi qaysi reaksiyalar disproporsiyaga mansubligini ko'rsating.",
             yechim=["2- va 3-reaksiyalar: Cl⁰ → −1/+1 va Cl⁺¹ → −1/+5."], M=3, A=0),
      ],
      rasmiylashtirish="Sxema-zanjir formati (Tongotarov 42-uslubi, faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="sxema_zanjir")),
 dict(n=43, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("X, Y, Z metallarining xlorid kislota va mis (II) sulfat eritmasi bilan o'zaro ta'siri "
            "jadvalda berilgan («+» — reaksiya boradi, «−» — bormaydi):\n"
            "[JADVAL] Metall | HCl | CuSO₄ eritmasi ;; X | + | + ;; Y | − | + ;; Z | − | −\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X, Y, Z metallarini aktivlik qatorida joylashish tartibi bo'yicha yozing va asoslang.",
             yechim=["X > Y > Z: X vodoroddan oldin; Y — H bilan Cu orasida; Z — Cu dan keyin."], M=4, A=0),
        dict(savol="b) X = Zn bo'lsa, 13 g rux mo'l CuSO₄ eritmasidan necha gramm misni siqib chiqaradi?",
             yechim=["n(Zn) = 0,2 mol → Cu = 0,2 mol → 12,8 g"], M=4, A=3),
        dict(savol="c) Shu jarayonda nechta elektron almashinadi (Nₐ birligida)?",
             yechim=["e = 0,2·2 = 0,4 mol → 0,4·Nₐ (≈2,408·10²³) ta"], M=3, A=3),
        dict(savol="d) Nega Y metall kislota bilan reaksiyaga kirishmaydi-yu, CuSO₄ bilan kirishadi? Izohlang.",
             yechim=["Y aktivlik qatorida H dan keyin — H⁺ ni qaytara olmaydi; ammo Cu dan oldin —",
                     "Cu²⁺ ni qaytara oladi (masalan, Bi, Sb kabi)."], M=4, A=4),
      ],
      rasmiylashtirish="Jadval-tahlil (aktivlik qatori): M15+A10. 41/42 formatlaridan farqli.",
      parametrlar=dict(arch="aktivlik_jadval")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260915)
letter_plan = list("ABCD" * 8)
def ok_plan(p):
    return all(len(set(p[i:i+4])) > 1 for i in range(len(p) - 3))
rng.shuffle(letter_plan)
while not ok_plan(letter_plan):
    rng.shuffle(letter_plan)

final_y1 = []
for i, item in enumerate(Y1):
    n = i + 1
    opts = [(item["correct"], None)] + [(t, x) for t, x in item["distractors"]]
    target = letter_plan[i]
    arranged = [None] * 4
    ti = letters.index(target)
    arranged[ti] = opts[0]
    slots = [j for j in range(4) if j != ti]
    for s, o in zip(slots, opts[1:]):
        arranged[s] = o
    variantlar = [o[0] for o in arranged]
    javob = letters[variantlar.index(item["correct"])]
    assert javob == target
    chalg = [dict(variant=letters[j], xato=arranged[j][1]) for j in range(4) if arranged[j][1]]
    d = dict(n=n, tur="Y1", element="I.9", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
             savol=item["savol"], variantlar=variantlar, javob=javob,
             chalgituvchilar=chalg, yechim=item["yechim"], parametrlar=item["parametrlar"])
    if item.get("svg"): d["svg"] = item["svg"]
    if item.get("fig"): d["fig"] = item["fig"]
    final_y1.append(d)

dist = {c: sum(1 for x in final_y1 if x["javob"] == c) for c in letters}
print("B-variant harf taqsimoti:", dist)
assert all(v == 8 for v in dist.values())
for x in final_y1:
    assert x["variantlar"][letters.index(x["javob"])] == Y1[x["n"]-1]["correct"]
print("Javob-harf tekshiruvi: OK (32/32)")
bad = [c for c in CHECKS if not c[3]]
for name, got, exp, ok in CHECKS:
    if not ok: print("XATO:", name, got, exp)
assert not bad
print(f"Sonli tekshiruvlar: OK ({len(CHECKS)}/{len(CHECKS)})")
for o in O2:
    M = sum(b["M"] for b in o["bandlar"]); A = sum(b["A"] for b in o["bandlar"])
    assert M + A == 25, (o["n"], M, A)
assert sum(b["A"] for b in O2[1]["bandlar"]) == 0
print("O2 ballari: OK")

variant = dict(
    variant="mavzu-I9-B", daraja="B", bob=9, bob_nomi="Oksidlanish-qaytarilish reaksiyalari",
    manba=("Tongotarov OQR banki (2019-2021) arxetiplari — javoblar elektron balans bilan mustaqil "
           "qayta hisoblangan; MS spetsifikatsiyasi I.9"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: elektron balans, koeffitsiyent yig'indilari, "
          "parametrli/teskari masalalar, 1-2-3 tanlovlar, jadval-grafik savollar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.9") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
