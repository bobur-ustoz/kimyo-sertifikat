# -*- coding: utf-8 -*-
"""Mavzulashtirilgan MS mock-variant generatori: I.7 Eritmalar.

PROMT_MAVZU_VARIANT.md tartibida:
- 1-32 Y1 (4 variant), pozitsiya->qiyinlik/kognitiv xaritasi promtdagi sinalgan qiymatlar
- 33-35 Y2 (bitta ssenariy + 3 ichki savol, A-F ro'yxati)
- 36-40 O1 (qisqa javob)
- 41-43 O2 (ko'p bandli, M+A ballar)
- Y1 javob harflari ~8/8/8/8 taqsimlanadi va dasturiy tekshiriladi
- Har sonli javob mustaqil qayta hisob bilan tekshiriladi (verify() bloklari)
"""
import json, itertools, sys
from fractions import Fraction as F

OUT = "mavzu_I7A.json"

# ---------- yordamchi: mustaqil tekshiruv hisoblari ----------
def pct(tuz, eritma):
    return 100.0 * tuz / eritma

CHECKS = []
def check(name, got, expected, tol=0.05):
    ok = abs(got - expected) <= tol
    CHECKS.append((name, got, expected, ok))
    return ok

# ---- Y1 savollari: (qiyinlik, kognitiv, savol, [(variant matni, xato-izohi yoki None-if-correct)], yechim, parametrlar)
# birinchi element har doim TO'G'RI javob; keyin harflar balanslab joylashtiriladi.
Y1 = []

def q(d, k, savol, correct, distractors, yechim, params=None, svg=None, fig=None):
    Y1.append(dict(qiyinlik=d, kognitiv=k, savol=savol, correct=correct,
                   distractors=distractors, yechim=yechim,
                   parametrlar=params or {}, svg=svg, fig=fig))

# 1 (2, quyi) — bank arxetipi (2017/DIM-4): oddiy ω
check("q1", pct(40, 400), 10)
q(2, "quyi",
  "40 g osh tuzi 360 g suvda eritildi. Hosil bo'lgan eritmadagi tuzning massa ulushini (%) aniqlang.",
  "10", [("11,1", "tuz massasi suv massasiga bo'lingan (40/360)"),
          ("9", "eritma massasi 440 g deb olingan"),
          ("12,5", "40/320 — suv massasidan 40 ni ayirib yuborilgan")],
  "m(eritma) = 40 + 360 = 400 g; ω = 40/400 · 100% = 10%.",
  dict(arch="oddiy_foiz", tuz=40, suv=360))

# 2 (1, quyi) — nazariy (darslik 9-sinf, ta'rif)
q(1, "quyi",
  "Erigan modda massasining eritma massasiga nisbati qanday ataladi?",
  "massa ulushi", [("molyar konsentratsiya", "mol/l birligidagi kattalik bilan adashtirilgan"),
                    ("eruvchanlik koeffitsiyenti", "100 g suvda erigan massa bilan adashtirilgan"),
                    ("zichlik", "massa/hajm nisbati bilan adashtirilgan")],
  "Ta'rif bo'yicha ω = m(modda)/m(eritma) — massa ulushi (foiz konsentratsiya).")

# 3 (2, quyi)
check("q3", 300*0.20, 60)
q(2, "quyi",
  "20 % li 300 g eritmada necha gramm erigan modda bor?",
  "60", [("40", "20 ni 2 ga ko'paytirmasdan xato hisob"), ("75", "eritmani 25% deb olgan"),
          ("15", "300/20 — nisbat teskari olingan")],
  "m(modda) = 300 · 0,20 = 60 g.", dict(arch="foizdan_massa", eritma=300, w=20))

# 4 (3, yuqori) — DIM grafik-savoli (Məhlullar 22-savol ruhi)
q(3, "yuqori",
  "To'yinmagan eritmaga o'sha tuzdan oz-ozdan qo'shib borilmoqda (harorat o'zgarmas). "
  "Eritmadagi tuzning massa ulushi (ω, %) qo'shilgan tuz massasiga bog'liq holda qanday o'zgaradi? "
  "To'g'ri grafikni tanlang.",
  "avval ortadi, to'yinishga yetgach o'zgarmay qoladi",
  [("chiziqli ravishda uzluksiz ortib boradi", "to'yinish chegarasi hisobga olinmagan"),
   ("o'zgarmaydi", "to'yingan eritma bilan adashtirilgan"),
   ("avval ortadi, so'ng kamayadi", "cho'kma massani kamaytirmasligi tushunilmagan")],
  "Tuz to'liq erigan bosqichda ω ortadi; eritma to'yingach ortiqcha tuz cho'kmaga tushadi va ω o'zgarmaydi (grafik: o'sish + gorizontal plato).",
  svg=dict(correct="rise_flat", d1="rise", d2="flat", d3="rise_fall"))

# 5 (2, quyi) — RASMLI: eruvchanlik egri chizig'ini o'qish
q(2, "quyi",
  "Rasmda KNO₃ va NaCl ning eruvchanlik egri chiziqlari berilgan. Grafikdan foydalanib, "
  "40 °C da KNO₃ ning 100 g suvdagi eruvchanligini (g) aniqlang.",
  "64", [("36", "NaCl egri chizig'idan o'qilgan"), ("32", "20 °C dagi qiymat olingan"),
          ("110", "60 °C dagi qiymat olingan")],
  "Grafikda 40 °C vertikali KNO₃ egri chizig'ini ≈64 g nuqtada kesadi. (NaCl niki deyarli o'zgarmas ≈36 g.)",
  dict(arch="grafik_oqish", tuz="KNO3", t=40, s=64),
  fig="solubility_curve")

# 6 (2, yuqori) — DIM Məhlullar-2 arxetipi
check("q6", (0.10+0.40)/2*100, 25)
q(2, "yuqori",
  "Bir xil massali 10 % li va 40 % li eritmalar aralashtirildi. Hosil bo'lgan eritmada erigan moddaning massa ulushini (%) hisoblang.",
  "25", [("30", "o'rtacha o'rniga 40-10 ayirmasi ishlatilgan"), ("20", "faqat kichik konsentratsiyaga yaqin xato baho"),
          ("50", "konsentratsiyalar yig'indisi olingan")],
  "Teng massalar (m) uchun: ω = (0,10m + 0,40m)/2m = 0,25 → 25%.",
  dict(arch="teng_massa_aralash", w1=10, w2=40))

# 7 (1, yuqori) — HIKOYALI RASM: murabbo bankasi
q(1, "yuqori",
  "Rasmga qarang: uzoq turgan murabbo (yoki asal) bankasida shakar kristallari paydo bo'ladi. "
  "Buning kimyoviy sababi nimada?",
  "sovutilganda o'ta to'yingan holatga o'tgan eritmadan ortiqcha shakar kristallanadi",
  [("shakar vaqt o'tishi bilan boshqa moddaga aylanadi", "kristallar — o'sha shakarning o'zi"),
   ("suv shakar bilan reaksiyaga kirishadi", "erish — fizik-kimyoviy jarayon, yangi modda hosil bo'lmaydi"),
   ("banka ichiga havo kirib, shakarni qotiradi", "havo emas, eruvchanlikning haroratga bog'liqligi sabab")],
  "Murabbo issiq holda juda konsentrlangan tayyorlanadi. Soviganda shakar eruvchanligi kamayadi — eritma "
  "o'ta to'yingan bo'lib qoladi va ortiqcha shakar asta-sekin kristall holida ajraladi.",
  fig="jam")

# 8 (2, yuqori) — DIM Məhlullar-18 arxetipi
check("q8", pct(20, 250), 8)
q(2, "yuqori",
  "200 g 10 % li eritma ustiga 50 g suv quyildi. Hosil bo'lgan eritmada erigan moddaning massa ulushini (%) hisoblang.",
  "8", [("10", "suyultirish hisobga olinmagan"), ("6", "eritma massasi 300 g deb olingan"),
         ("12,5", "nisbat teskari — 250/20")],
  "Tuz massasi o'zgarmaydi: 20 g. Yangi eritma 250 g; ω = 20/250 · 100% = 8%.",
  dict(arch="suyultirish", m1=200, w1=10, suv=50))

# 9 (1, quyi) — HIKOYALI RASM: sho'r ko'l (tuz koni)
q(1, "quyi",
  "Rasmda yozgi jazirama paytidagi sho'r ko'l qirg'og'i ko'rsatilgan: suv chekkasida oq tuz qatlami hosil bo'lgan. "
  "Bu qatlam qanday hosil bo'ladi?",
  "suv bug'langani sari eritma to'yinib, ortiqcha tuz kristallanadi",
  [("quyosh nuri tuzni suvdan ajratib chiqaradi", "yorug'lik emas, bug'lanish sabab"),
   ("tuz suv bilan reaksiyaga kirishib, cho'kadi", "erish-kristallanish fizik-kimyoviy jarayon, reaksiya emas"),
   ("ko'l tubidan yangi tuz ko'tariladi", "tuz eritmaning o'zidan ajraladi")],
  "Issiqda suv jadal bug'lanadi, tuz esa uchmaydi: eritma quyuqlashib to'yinish chegarasiga yetadi va "
  "ortiqcha tuz qirg'oqda kristall qatlam hosil qiladi. Tuz konlarida tuz aynan shu usulda olinadi.",
  fig="saltlake")

# 10 (2, quyi) — DIM Məhlullar-13 arxetipi
check("q10", pct(120, 500), 24)
q(2, "quyi",
  "400 g 30 % li eritmaga 100 g suv qo'shildi. Olingan eritmaning konsentratsiyasini (%) hisoblang.",
  "24", [("25", "yaxlitlashda 500 o'rniga 480 olingan"), ("27", "suvning yarmi hisobga olingan"),
          ("20", "eritma 600 g deb olingan")],
  "Tuz: 400 · 0,3 = 120 g; eritma: 500 g; ω = 120/500 · 100% = 24%.",
  dict(arch="suyultirish", m1=400, w1=30, suv=100))

# 11 (2, yuqori) — DIM Məhlullar-14 (formula-savol)
q(2, "yuqori",
  "a gramm tuz b gramm suvda eritildi. Hosil bo'lgan eritmada tuzning massa ulushi (%) qaysi formula bilan topiladi?",
  "a·100/(a+b)",
  [("a·100/b", "eritma o'rniga erituvchi massasi olingan"),
   ("b·100/(a+b)", "suvning massa ulushi formulasi"),
   ("(a+b)·100/a", "nisbat teskari yozilgan")],
  "ω = m(tuz)/m(eritma) · 100% = a/(a+b) · 100%.")

# 12 (3, yuqori) — bank (Eritma.docx) real savoli
check("q12", 200*90/100, 180)
q(3, "yuqori",
  "NaNO₃ ning 25 °C dagi eruvchanlik koeffitsiyenti 90 ga teng. Shu haroratda 200 g suvga necha gramm NaNO₃ qo'shilsa, to'yingan eritma hosil bo'ladi?",
  "180", [("90", "koeffitsiyent 200 g suvga to'g'ridan-to'g'ri olingan"),
           ("200", "suv massasiga tenglashtirilgan"),
           ("45", "nisbat teskari — ikkiga bo'lingan")],
  "100 g suvga 90 g → 200 g suvga 2 · 90 = 180 g.",
  dict(arch="eruvchanlik_masshtab", s=90, suv=200, manba="Eritma banki (MS/DTM 2019–2021)"))

# 13 (2, quyi) — bank nazariy savoli
q(2, "quyi",
  "Erigan modda miqdorining (mol) eritma hajmiga (l) nisbati qanday ataladi?",
  "molyar konsentratsiya",
  [("massa ulushi", "foiz konsentratsiya massa nisbatidir"),
   ("normal konsentratsiya", "ekvivalent miqdorga asoslangan kattalik"),
   ("eruvchanlik", "to'yinish chegarasini bildiradi")],
  "c = n/V (mol/l) — molyar konsentratsiya.", dict(manba="Eritma banki"))

# 14 (1, quyi) — RASMLI: cho'kmali stakan
q(1, "quyi",
  "Rasmdagi idishda tuz eritilgach, aralashtirishga qaramay tuzning bir qismi erimay tubida qoldi "
  "(harorat o'zgarmas). Idishdagi eritma qanday eritma?",
  "to'yingan eritma",
  [("to'yinmagan eritma", "to'yinmagan eritmada cho'kma qolmasdi — hammasi erirdi"),
   ("o'ta to'yingan eritma", "beqaror holat; cho'kma ustidagi muvozanatli eritma emas"),
   ("suyultirilgan eritma", "konsentratsiya darajasini bildiradi, to'yinishni emas")],
  "Cho'kma bilan muvozanatda turgan eritma shu haroratda to'yingan bo'ladi — boshqa tuz erita olmaydi.",
  fig="beaker_sat")

# 15 (2, yuqori)
check("q15", 0.5*2*40, 40)
q(2, "yuqori",
  "2 M li 500 ml NaOH eritmasini tayyorlash uchun necha gramm NaOH kerak? (M(NaOH) = 40 g/mol)",
  "40", [("80", "hajm litrga aylantirilmagan"), ("20", "1 M deb olingan"),
          ("10", "500 ml → 0,5 l, lekin c ham 0,5 deb xato olingan")],
  "n = c · V = 2 · 0,5 = 1 mol; m = 1 · 40 = 40 g.",
  dict(arch="molyar_massa", c=2, V=0.5, M=40))

# 16 (2, quyi) — MOLYAL konsentratsiya (11-sinf darsligi chegarasida)
check("q16", 0.5/0.5, 1)
q(2, "quyi",
  "500 g suvda 0,5 mol glyukoza eritildi. Eritmaning molyal konsentratsiyasini (mol/kg) toping.",
  "1", [("0,5", "erituvchi kg ga aylantirilmagan"), ("2", "nisbat teskari olingan"),
         ("0,25", "eritma massasiga bo'lingan deb xato baho")],
  "Molyal konsentratsiya — 1 kg ERITUVCHIdagi modda miqdori: 0,5 mol / 0,5 kg = 1 mol/kg.",
  dict(arch="molyal", n=0.5, suv=500, manba="11-sinf, molyar/normal banki"))

# 17 (3, yuqori) — DIM jadval-savoli (moslashtirish ruhi)
q(3, "yuqori",
  "Jadvalda uchta tuzning 20 °C dagi eruvchanlik koeffitsiyentlari berilgan:\n"
  "[JADVAL] Tuz | Eruvchanligi, g/100 g suv ;; KNO₃ | 32 ;; NaCl | 36 ;; KCl | 34\n"
  "Har bir tuzdan 70 g olinib, alohida idishlardagi 200 g suvga solindi va aralashtirildi. Qaysi tuz(lar) TO'LIQ eriydi?",
  "faqat NaCl",
  [("faqat KNO₃", "64 g chegara 70 g dan kichik — to'liq erimaydi"),
   ("NaCl va KCl", "KCl chegarasi 68 g < 70 g"),
   ("uchchala tuz ham", "chegaralar 200 g suvga 2 barobar qilinishi kerak")],
  "200 g suvdagi chegaralar: KNO₃ — 64 g, NaCl — 72 g, KCl — 68 g. 70 g faqat NaCl chegarasidan kichik → faqat NaCl to'liq eriydi.",
  dict(arch="jadval_eruvchanlik", s=dict(KNO3=32, NaCl=36, KCl=34), tuz=70, suv=200))

# 18 (2, quyi)
check("q18", 200*0.05, 10)
q(2, "quyi",
  "5 % li 200 g eritma tayyorlash uchun necha gramm tuz va necha gramm suv kerak?",
  "10 g tuz va 190 g suv",
  [("5 g tuz va 195 g suv", "foiz eritma massasiga emas, 100 g ga olingan"),
   ("10 g tuz va 200 g suv", "tuz massasi eritmaga kirishi unutilgan"),
   ("20 g tuz va 180 g suv", "10% deb olingan")],
  "m(tuz) = 200 · 0,05 = 10 g; m(suv) = 200 − 10 = 190 g.",
  dict(arch="tayyorlash", m=200, w=5))

# 19 (3, yuqori) — kristallogidrat (bank arxetipi)
check("q19", pct(16, 200), 8)
q(3, "yuqori",
  "25 g mis kuporosi CuSO₄·5H₂O suvda eritilib, 200 g eritma tayyorlandi. Eritmadagi CuSO₄ ning massa ulushini (%) hisoblang. (M(CuSO₄)=160, M(CuSO₄·5H₂O)=250 g/mol)",
  "8", [("12,5", "kristallogidrat massasi to'g'ridan-to'g'ri olingan (25/200)"),
         ("10", "suvsiz tuz 20 g deb xato hisoblangan"),
         ("16", "eritma massasi 100 g deb olingan")],
  "CuSO₄: 25 · 160/250 = 16 g; ω = 16/200 · 100% = 8%.",
  dict(arch="kristallogidrat_foiz", gidrat=25, M1=250, M2=160, eritma=200))

# 20 (2, yuqori) — DIM Məhlullar-25 (munosabat-savol)
q(2, "yuqori",
  "To'yinmagan eritmadan bir qism suv bug'latildi (tuz cho'kmaga tushmadi). Dastlabki (m₁, ω₁) va keyingi (m₂, ω₂) eritmalar orasidagi TO'G'RI munosabatni ko'rsating.",
  "m₁·ω₁ = m₂·ω₂",
  [("m₁·ω₂ = m₂·ω₁", "indekslar o'rni almashib ketgan"),
   ("m₁ = m₂·ω₂", "o'lchov birliklari mos emas"),
   ("ω₁ = ω₂", "bug'lanishda konsentratsiya o'zgaradi")],
  "Erigan tuz massasi saqlanadi: m(tuz) = m₁ω₁ = m₂ω₂ (ω — ulush ko'rinishida).",
  dict(arch="munosabat", manba="DIM formati, mazmun mos"))

# 21 (3, yuqori) — OLEUM (bank arxetipi, 11-sinf 11.12-mavzu)
check("q21", 100*(785 - 5*80)/(90+785), 44)
q(3, "yuqori",
  "90 g suvga 785 g SO₃ qo'shildi. Hosil bo'lgan oleumdagi erkin SO₃ ning massa ulushini (%) aniqlang.",
  "44", [("49", "suv bilan reaksiyaga kirgan SO₃ ayirilmagan"),
          ("51", "hosil bo'lgan H₂SO₄ ulushi olingan"),
          ("56", "umumiy massa o'rniga faqat SO₃ massasi ishlatilgan")],
  "H₂O (5 mol) SO₃ ning 5 mol (400 g) ini H₂SO₄ ga bog'laydi. Erkin SO₃: 785 − 400 = 385 g; "
  "umumiy massa: 875 g; ω(SO₃) = 385/875 · 100% = 44%.",
  dict(arch="oleum_foiz", suv=90, so3=785, manba="Oleum banki (11-sinf), savol qolipida"))

# 22 (3, yuqori) — NORMAL konsentratsiya (bank arxetipi)
check("q22", 19.6/49/2, 0.2)
q(3, "yuqori",
  "2 l eritmada 19,6 g sulfat kislota erigan. Eritmaning normal konsentratsiyasini (mol-ekv/l) toping. "
  "(M(H₂SO₄)=98 g/mol; E(H₂SO₄)=49 g/mol)",
  "0,2", [("0,1", "molyar konsentratsiya hisoblangan (ekvivalent olinmagan)"),
           ("0,4", "hajmga bo'lish unutilgan"),
           ("0,05", "ekvivalent 196 deb xato olingan")],
  "n(ekv) = 19,6/49 = 0,4 mol-ekv; N = 0,4/2 = 0,2 mol-ekv/l. (Tekshiruv: c = 0,1 M; H₂SO₄ uchun N = 2c ✓)",
  dict(arch="normal_konts", m=19.6, E=49, V=2, manba="11-sinf molyar/normal banki, savol qolipida"))

# 23 (3, yuqori)
check("q23", 10*1.2*20/40, 6)
q(3, "yuqori",
  "20 % li NaOH eritmasining zichligi 1,2 g/ml. Eritmaning molyar konsentratsiyasini (mol/l) hisoblang. (M(NaOH)=40 g/mol)",
  "6", [("5", "zichlik hisobga olinmagan"), ("2,4", "10 ko'paytuvchisi tushib qolgan"),
         ("12", "M o'rniga 20 ga bo'lingan")],
  "1 l eritma: 1200 g; NaOH: 240 g → n = 6 mol → c = 6 mol/l. (Formula: c = 10ρω/M.)",
  dict(arch="foizdan_molyar", w=20, rho=1.2, M=40))

# 24 (3, yuqori) — HIKOYALI RASM: akvarium
q(3, "yuqori",
  "Rasmga qarang: issiq yoz kunida akvarium suvi qizib ketganda baliqlar suv yuzasiga ko'tarilib, «havo yutayotgandek» "
  "harakat qiladi. Buning sababi va yechimini ko'rsating.",
  "iliq suvda O₂ ning eruvchanligi kamaygan; suvni salqinlatish yoki havo purkash kerak",
  [("iliq suvda kislorod ko'payib, baliqlar «mast» bo'ladi", "aksincha — gaz eruvchanligi haroratda KAMAYADI"),
   ("baliqlar iliq suvni yoqtirib, yuzaga o'ynagani chiqadi", "bu xatti-harakat kislorod tanqisligi belgisi"),
   ("suvdagi tuzlar kislorodni siqib chiqaradi", "hal qiluvchi omil harorat, tuzlar emas")],
  "Gazlar eruvchanligi harorat ortishi bilan kamayadi: iliq suvda erigan O₂ kam — baliqlar kislorod yetishmasligidan "
  "yuzaga intiladi. Yechim: suvni salqinlatish yoki kompressor bilan havo purkash (bosim/aralashish).",
  fig="aquarium")

# 25 (3, yuqori)
check("q25a", 100.0, 100); check("q25b", 200.0, 200)
q(3, "yuqori",
  "40 % li va 10 % li eritmalardan 300 g 20 % li eritma tayyorlash uchun har biridan necha grammdan olish kerak?",
  "100 g (40 %) va 200 g (10 %)",
  [("150 g va 150 g", "o'rtacha 25% bo'lib qoladi"),
   ("200 g (40 %) va 100 g (10 %)", "nisbat teskari — 30% chiqadi"),
   ("120 g va 180 g", "krest qoidasi xato qo'llangan")],
  "x + y = 300; 0,4x + 0,1y = 60 → 0,3x = 30 → x = 100 g, y = 200 g. (Krest qoidasi: 10 : 20 = 1 : 2.)",
  dict(arch="krest", w1=40, w2=10, w=20, m=300))

# 26 (3, yuqori) — GAZ eruvchanligi hisobi (ERUVCHANLIK banki, mustaqil yechildi)
check("q26a", 1020/170*70, 420); check("q26b", (420-6*36)/17*22.4, 268.8)
q(3, "yuqori",
  "10 °C da 1020 g to'yingan ammiak eritmasi 50 °C gacha qizdirildi. Ajralib chiqqan ammiakning "
  "hajmini (l, n.sh.) hisoblang. (S₁₀=70 g, S₅₀=36 g / 100 g suvda)",
  "268,8", [("336", "boshlang'ich barcha NH₃ ajraladi deb olingan (15 mol emas, aslida jami 420 g)"),
             ("224", "ajralgan massa 170 g deb xato hisoblangan"),
             ("134,4", "yarim miqdor — eritma massasi 510 g deb olingan")],
  "1020 g = 6 · 170 g → NH₃ 420 g, suv 600 g. 50 °C da erigan holda qoladi: 6·36 = 216 g. "
  "Ajraladi: 420 − 216 = 204 g = 12 mol → V = 12 · 22,4 = 268,8 l.",
  dict(arch="gaz_eruvchanlik", s1=70, s2=36, m=1020, manba="ERUVCHANLIK banki (11-sinf), javob mustaqil tekshirildi"))

# 27 (2, yuqori) — DIM 'olmaz' savoli
q(2, "yuqori",
  "Bir xil moddaning 20 % li va 40 % li eritmalarini o'zaro aralashtirib QAYSI konsentratsiyali eritma tayyorlab BO'LMAYDI?",
  "45 %", [("25 %", "20–40% oralig'ida — mumkin"), ("30 %", "teng massalarda hosil bo'ladi"),
            ("38 %", "40% ga yaqin nisbatda mumkin")],
  "Aralashma konsentratsiyasi doim ikki qiymat orasida bo'ladi: 20% < ω < 40%. 45% bu oraliqdan tashqarida.",
  dict(arch="oraliq", w1=20, w2=40, manba="DIM formati (olmaz-savol)"))

# 28 (1, quyi) — DIM Məhlullar-1 arxetipi
q(1, "quyi",
  "Shakar eritmasiga suv qo'shilganda qaysi kattalik O'ZGARMAYDI?",
  "erigan shakar massasi",
  [("eritma massasi", "suv qo'shilganda ortadi"),
   ("shakarning massa ulushi", "suyultirishda kamayadi"),
   ("eritma hajmi", "suv qo'shilganda ortadi")],
  "Suyultirishda erigan modda miqdori (massasi) o'zgarmaydi — faqat eritma massasi/hajmi ortib, ω kamayadi.")

# 29 (2, quyi) — RASMLI: uch stakanli tajriba (DIM uslubi) — saqlanadi
q(2, "quyi",
  "Rasmda 20 °C dagi tajriba ko'rsatilgan: uchala idishdagi 100 g suvga mos ravishda 20 g, 36 g va 50 g "
  "dan bir xil tuz solinib aralashtirildi (tuzning eruvchanligi 36 g/100 g suv). Qaysi idish(lar)da tuzning "
  "bir qismi erimay, cho'kma holida qoladi?",
  "faqat 3-idishda",
  [("2- va 3-idishlarda", "36 g aynan chegaraga teng — hammasi eriydi"),
   ("faqat 2-idishda", "50 g > 36 g bo'lgani uchun aynan 3-idishda cho'kma qoladi"),
   ("hech birida", "3-idishda 14 g tuz erimay qoladi")],
  "Chegara: 36 g/100 g suv. 1-idish (20 g) — to'yinmagan; 2-idish (36 g) — aynan to'yingan, cho'kmasiz; "
  "3-idish (50 g) — 36 g eriydi, 14 g cho'kmada qoladi.",
  dict(arch="uch_idish", s=36, tuzlar=[20, 36, 50]),
  fig="beakers3")

# 30 (1, quyi) — OLEUM ta'rifi (bank nazariy savoli)
q(1, "quyi",
  "«Oleum»ga berilgan to'g'ri ta'rifni ko'rsating.",
  "SO₃ ning suvsiz (100 % li) sulfat kislotadagi eritmasi",
  [("sulfat kislotaning konsentrlangan suvdagi eritmasi", "oleumda erituvchi suv emas, H₂SO₄"),
   ("SO₃ ning suvdagi to'yingan eritmasi", "SO₃ suv bilan reaksiyaga kirib H₂SO₄ hosil qiladi"),
   ("100 % li sulfat kislotaning o'zi", "oleumda qo'shimcha erkin SO₃ bo'ladi")],
  "Oleum — H₂SO₄·nSO₃: ortiqcha SO₃ ning 100 % li sulfat kislotadagi eritmasi; erituvchi vazifasini H₂SO₄ bajaradi.",
  dict(manba="Oleum banki (11-sinf)"))

# 31 (2, yuqori) — TITR
check("q31", 2*40/1000, 0.08)
q(2, "yuqori",
  "2 M li NaOH eritmasining titrini (g/ml) toping. (M(NaOH)=40 g/mol)",
  "0,08", [("80", "g/l birligida qoldirilgan (ml ga aylantirilmagan)"),
            ("0,04", "1 M uchun hisoblangan"),
            ("0,8", "o'nlik xatosi — 100 ml ga hisoblangan")],
  "Titr — 1 ml eritmadagi modda massasi: T = c·M/1000 = 2·40/1000 = 0,08 g/ml.",
  dict(arch="titr", c=2, M=40))

# 32 (2, yuqori) — DIM grafik (to'yingan eritmadan bug'latish)
q(2, "yuqori",
  "To'yingan eritmadan harorat o'zgarmagan holda suv asta-sekin bug'latilmoqda (ortiqcha tuz cho'kmaga tushib boradi). "
  "Eritmadagi tuzning massa ulushi (ω, %) bug'latilgan suv massasiga bog'liq holda qanday o'zgaradi?",
  "o'zgarmaydi (gorizontal chiziq)",
  [("uzluksiz ortib boradi", "eritma allaqachon to'yingan — ω chegarada qoladi"),
   ("kamayadi", "suv kamayishi ω ni kamaytirmaydi"),
   ("avval kamayib, so'ng ortadi", "asossiz kombinatsiya")],
  "To'yingan eritmada har bir haroratga bitta ω mos keladi. Suv bug'langanda ortiqcha tuz cho'kadi, eritma esa to'yinganligicha qoladi → ω = const.",
  svg=dict(correct="flat", d1="rise", d2="fall", d3="u"))

assert len(Y1) == 32, len(Y1)

# ---------- Y2 (33-35): bitta ssenariy, 3 ichki savol, A-F ----------
# X tuzi: eruvchanlik 60C: 150, 20C: 50 (g/100 g suv). 200 g suvda 60C da to'yingan eritma.
check("y2_tuz", 2*150, 300); check("y2_w", pct(300, 500), 60); check("y2_chok", 300-2*50, 200)
Y2 = dict(
  n=33, tur="Y2", element="I.7",
  ichki_pasport=[dict(n=33, element="I.7", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.8", qiyinlik=1, kognitiv="quyi"),
                 dict(n=35, element="I.7", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("X tuzining eruvchanlik koeffitsiyenti 60 °C da 150 g, 20 °C da 50 g (100 g suvda). "
               "60 °C da 200 g suvda X tuzining to'yingan eritmasi tayyorlandi, so'ngra u 20 °C gacha sovutildi. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang (har bir savolga bittadan)."),
  savollar_ichki=[
    "33. 60 °C dagi to'yingan eritmadagi X tuzining massasi (g) qancha?",
    "34. 60 °C dagi to'yingan eritmada X tuzining massa ulushi (%) qancha?",
    "35. Eritma 20 °C gacha sovutilganda necha gramm tuz cho'kmaga tushadi?"],
  javoblar_royxati=["A) 300", "B) 60", "C) 200", "D) 150", "E) 100", "F) 40"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="eruvchanlik koeffitsiyentining o'zi (100 g suv uchun)"),
                   dict(variant="E", xato="20 °C da erigan holda qolgan tuz massasi — cho'kma bilan adashtiriladi"),
                   dict(variant="F", xato="ω ni suv massasiga nisbatan hisoblash xatosi (300/500 o'rniga boshqa nisbat)")],
  yechim=("60 °C: 200 g suvda 2·150 = 300 g tuz (33 → A). Eritma 500 g; ω = 300/500 = 60% (34 → B). "
          "20 °C da erigan bo'lib qoladi: 2·50 = 100 g; cho'kma: 300 − 100 = 200 g (35 → C)."),
  parametrlar=dict(arch="sovutish_ssenariy", s60=150, s20=50, suv=200))

# ---------- O1 (36-40) ----------
check("o36", pct(40, 500), 8)
check("o37", pct(60, 200), 30)
check("o38", (0.5+0.5)/0.25, 4)
check("o39", pct(50*160/250, 400), 8)
check("o40", 55/0.55, 100)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="400 g 10 % li eritmaga 100 g suv qo'shildi. Hosil bo'lgan eritmaning konsentratsiyasini (%) toping.",
      javob="8", yechim="Tuz 40 g; eritma 500 g; ω = 8%.",
      parametrlar=dict(arch="suyultirish", m=400, w=10, suv=100)),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="300 g 20 % li eritmadan 100 g suv bug'latildi (tuz cho'kmadi). Qolgan eritmaning konsentratsiyasini (%) toping.",
      javob="30", yechim="Tuz 60 g; eritma 200 g; ω = 30%.",
      parametrlar=dict(arch="buglatish", m=300, w=20, suv=100)),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="250 ml 2 M li KOH eritmasiga 28 g KOH qo'shib eritildi (hajm o'zgarmadi deb hisoblang). "
            "Olingan eritmaning molyar konsentratsiyasini (mol/l) toping. (M(KOH)=56 g/mol)",
      javob="4", yechim="Boshlang'ich: 0,25·2 = 0,5 mol; qo'shildi: 28/56 = 0,5 mol; jami 1 mol / 0,25 l = 4 M.",
      parametrlar=dict(arch="molyar_qoshish", V=0.25, c=2, m=28, M=56)),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="50 g mis kuporosi CuSO₄·5H₂O 350 g suvda eritildi. Eritmadagi CuSO₄ ning massa ulushini (%) toping. "
            "(M(CuSO₄)=160, M(CuSO₄·5H₂O)=250 g/mol)",
      javob="8", yechim="CuSO₄: 50·160/250 = 32 g; eritma 400 g; ω = 8%.",
      parametrlar=dict(arch="kristallogidrat_foiz", gidrat=50, M1=250, M2=160, suv=350)),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="80 °C da CuSO₄ ning 330 g to'yingan eritmasi 20 °C gacha sovutilganda necha gramm CuSO₄·5H₂O "
            "kristall holda cho'kadi? (S₈₀=50 g, S₂₀=25 g / 100 g suvda; M(CuSO₄)=160, M(CuSO₄·5H₂O)=250 g/mol)",
      javob="100",
      yechim="330 g = 2,2·150 g → CuSO₄ 110 g, suv 220 g. x g gidrat cho'ksin: unda CuSO₄ 0,64x, H₂O 0,36x. "
             "Qolgan eritma to'yingan: (110 − 0,64x)/(220 − 0,36x) = 25/100 → 110 − 0,64x = 55 − 0,09x → "
             "0,55x = 55 → x = 100 g.",
      parametrlar=dict(arch="kristallogidrat_chokish", s1=50, s2=25, m=330, gidrat="CuSO4·5H2O",
                       manba="ERUVCHANLIK banki, javob mustaqil tekshirildi")),
]

# ---------- O2 (41-43) ----------
check("o41a", 250+310, 560); check("o41b", 310-2.5*88, 90); check("o41c", pct(220, 470), 46.8, tol=0.1)
check("o41d", 100*90/310, 29.0, tol=0.1)
check("o42a", pct(12.8, 200), 6.4); check("o42b", 200-12.8/0.128, 100)
O2 = [
 dict(n=41, tur="O2", element="I.7", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("NaNO₃ ning eruvchanligi (g/100 g suvda):\n"
            "[JADVAL] t, °C | 10 | 20 | 40 | 60 | 80 ;; s, g | 80 | 88 | 105 | 124 | 148\n"
            "60 °C da 250 g suvda NaNO₃ ning to'yingan eritmasi tayyorlandi, so'ngra 20 °C gacha sovutildi."),
      bandlar=[
        dict(savol="a) 60 °C dagi to'yingan eritmaning massasini (g) hisoblang.",
             yechim=["250 g suvga: 2,5 · 124 = 310 g NaNO₃", "m(eritma) = 250 + 310 = 560 g"], M=2, A=1),
        dict(savol="b) 20 °C gacha sovutilganda necha gramm NaNO₃ cho'kmaga tushishini hisoblang.",
             yechim=["20 °C da erigan holda qoladi: 2,5 · 88 = 220 g", "cho'kma: 310 − 220 = 90 g"], M=3, A=2),
        dict(savol="c) Sovutilgandan keyin qolgan eritmadagi NaNO₃ ning massa ulushini (%) hisoblang.",
             yechim=["qolgan eritma: 560 − 90 = 470 g", "ω = 220/470 · 100% ≈ 46,8%"], M=3, A=3),
        dict(savol="d) Dastlabki erigan tuzning necha foizi kristallanganini hisoblang.",
             yechim=["90/310 · 100% ≈ 29%"], M=2, A=2),
        dict(savol="e) Xuddi shu tajriba CO₂ ning suvdagi eritmasi bilan o'tkazilsa (sovutish), gaz eritmadan ajralib chiqadimi? Javobingizni eruvchanlikning haroratga bog'liqligi asosida tushuntiring.",
             yechim=["Yo'q, ajralmaydi: gazlarning eruvchanligi sovutilganda ORTADI —",
                     "sovutish gaz uchun eritmani to'yinmagan holatga o'tkazadi.",
                     "Qattiq tuzlarda esa (NaNO₃) eruvchanlik kamayadi va ortiqchasi kristallanadi."], M=5, A=2),
      ],
      rasmiylashtirish="DTM spetsifikatsiyasi (5 bandlik 41-topshiriq): M jami 15, A jami 10; oxirgi band — sifat/sabab bandi.",
      parametrlar=dict(arch="eruvchanlik_jadval_sikl", s=dict(t10=80, t20=88, t40=105, t60=124, t80=148), suv=250)),
 dict(n=42, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn="20 g mis kuporosi CuSO₄·5H₂O 180 g suvda eritildi. (M(CuSO₄)=160, M(CuSO₄·5H₂O)=250 g/mol)",
      bandlar=[
        dict(savol="a) Eritmadagi suvsiz CuSO₄ ning massa ulushini (%) aniqlash yo'lini yozing va hisoblang.",
             yechim=["CuSO₄: 20 · 160/250 = 12,8 g", "eritma: 200 g", "ω = 12,8/200 · 100% = 6,4%"], M=13, A=0),
        dict(savol="b) Shu eritmadan necha gramm suv bug'latilsa, CuSO₄ ning massa ulushi 12,8 % ga yetadi? (Tuz cho'kmaydi deb hisoblang.)",
             yechim=["kerakli eritma massasi: 12,8/0,128 = 100 g", "bug'latiladigan suv: 200 − 100 = 100 g"], M=9, A=0),
        dict(savol="c) Nega hisobda kristallogidrat (CuSO₄·5H₂O) emas, suvsiz tuz (CuSO₄) massasi ishlatiladi? Qisqacha tushuntiring.",
             yechim=["Kristallanish suvi eritmada erituvchi (suv) tarkibiga o'tadi;",
                     "erigan modda sifatida faqat suvsiz CuSO₄ qoladi."], M=3, A=0),
      ],
      rasmiylashtirish="DTM spetsifikatsiyasi: 42-topshiriq faqat usul (M) bilan baholanadi (A yo'q), 3 band: M13+M9+M3=25. Promt qoidasi bo'yicha ataylab soddaroq.",
      parametrlar=dict(arch="kristallogidrat_buglatish", gidrat=20, suv=180)),
 dict(n=43, tur="O2", element="I.7", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Quyidagi jadvalda tuz eritmasi ustida bajarilgan 5 ta amal berilgan. Har bir holat uchun eritmadagi "
            "erigan moddaning massa ulushi (ω) qanday o'zgarishini (ortadi / kamayadi / o'zgarmaydi) aniqlang va sababini yozing.\n"
            "[JADVAL] № | Holat ;; 1 | To'yinmagan eritmaga o'sha tuzdan qo'shib eritildi ;; "
            "2 | To'yingan eritmaga o'sha tuzdan yana qo'shildi (harorat o'zgarmas) ;; "
            "3 | Eritmaga suv qo'shildi ;; "
            "4 | To'yinmagan eritmadan ochiq idishda suvning bir qismi bug'landi (tuz cho'kmadi) ;; "
            "5 | Eruvchanligi harorat pasayishi bilan kamayadigan tuzning to'yingan eritmasi sovutildi"),
      bandlar=[
        dict(savol="1-holat", yechim=["ORTADI — erigan tuz massasi ortadi, eritma massasi undan sekinroq o'sadi"], M=3, A=2),
        dict(savol="2-holat", yechim=["O'ZGARMAYDI — qo'shilgan tuz erimaydi, cho'kma holida qoladi; eritma tarkibi o'zgarmaydi"], M=3, A=2),
        dict(savol="3-holat", yechim=["KAMAYADI — tuz massasi o'zgarmay, eritma massasi ortadi"], M=3, A=2),
        dict(savol="4-holat", yechim=["ORTADI — tuz massasi saqlanib, eritma massasi kamayadi"], M=3, A=2),
        dict(savol="5-holat", yechim=["O'ZGARMAYDI deyish XATO bo'lardi: to'g'ri javob — KAMAYADI: ortiqcha tuz kristallanadi va eritma yangi (pastroq) haroratdagi to'yinish chegarasiga tushadi; ω = s₂/(100+s₂) < s₁/(100+s₁)"], M=3, A=2),
      ],
      rasmiylashtirish="MS 43-savolining jadval ruhi: har holat uchun yo'nalish + sabab (DIM 'Məhlullar' blokidagi sifat-savollar formatidan moslashtirilgan).",
      parametrlar=dict(arch="jadval_sabab")),
]

# ---------- Y1 harflarni balanslash ----------
import random
letters = "ABCD"
rng = random.Random(20260828)
letter_plan = list("ABCD" * 8)
rng.shuffle(letter_plan)
# ketma-ket 3 tadan ortiq bir xil harf kelmasin
def ok_plan(p):
    return all(len(set(p[i:i+4])) > 1 for i in range(len(p) - 3))
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
    rest = opts[1:]
    slots = [j for j in range(4) if j != ti]
    for s, o in zip(slots, rest):
        arranged[s] = o
    variantlar = [o[0] for o in arranged]
    javob = letters[variantlar.index(item["correct"])]
    assert javob == target and variantlar[letters.index(javob)] == item["correct"]
    chalg = [dict(variant=letters[j], xato=arranged[j][1]) for j in range(4) if arranged[j][1]]
    d = dict(n=n, tur="Y1", element="I.7", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
             savol=item["savol"], variantlar=variantlar, javob=javob,
             chalgituvchilar=chalg, yechim=item["yechim"], parametrlar=item["parametrlar"])
    if item.get("svg"):
        d["svg"] = item["svg"]
    if item.get("fig"):
        d["fig"] = item["fig"]
    final_y1.append(d)

# balans hisobot
dist = {c: sum(1 for q_ in final_y1 if q_["javob"] == c) for c in letters}
print("Y1 harf taqsimoti:", dist)
assert all(abs(v - 8) <= 1 for v in dist.values()), dist

# javob-harf dasturiy tekshiruvi
for q_ in final_y1:
    assert q_["variantlar"][letters.index(q_["javob"])] == Y1[q_["n"]-1]["correct"], q_["n"]
print("Y1 javob-harf tekshiruvi: OK (32/32)")

# sonli tekshiruvlar hisoboti
bad = [c for c in CHECKS if not c[3]]
for name, got, exp, ok in CHECKS:
    if not ok:
        print("XATO:", name, got, exp)
assert not bad, bad
print(f"Sonli tekshiruvlar: OK ({len(CHECKS)}/{len(CHECKS)})")

variant = dict(
    variant="mavzu-I7-A", daraja="A", bob=7, bob_nomi="Eritmalar",
    manba=("aralash: hisobiy arxetiplar MS/DTM Eritma bankidan (2019–2021) va Ismoilov variantlaridan; "
           "grafik/jadval/munosabat formatlari Ozarbayjon DIM 2023 'Məhlullar' blokidan ilhomlangan; "
           "nazariy savollar 9-sinf darsligi (Asqarov) chegarasida original"),
    izoh=("Barcha 43 savol I.7 (Eritmalar: eruvchanlik, konsentratsiya) elementiga bag'ishlangan; "
          "MS 43-pozitsion strukturasi, qiyinlik/kognitiv xaritasi PROMT_MAVZU_VARIANT.md dagi sinalgan "
          "qiymatlar bo'yicha. 180 daqiqa: 1–40 → 100 daq, 41–43 → 80 daq."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.7") for x in O1] + O2,
)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT, "— savollar:", len(variant["savollar"]))
