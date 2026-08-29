# -*- coding: utf-8 -*-
"""5-bob: Kimyoviy reaksiya tezligi (I.5) — 43 talik mavzulashtirilgan variant.
Manbalar: Tongotarov 11-bob (javob kaliti bilan solishtirildi), MS/DTM tezlik banki,
DIM format namunalari. Barcha sonli javoblar mustaqil qayta hisoblanadi."""
import json, random

OUT = "mavzu_I5.json"
CHECKS = []
def check(name, got, expected, tol=1e-6):
    ok = abs(got - expected) <= tol
    CHECKS.append((name, got, expected, ok))
    return ok

Y1 = []
def q(d, k, savol, correct, distractors, yechim, params=None, svg=None):
    Y1.append(dict(qiyinlik=d, kognitiv=k, savol=savol, correct=correct,
                   distractors=distractors, yechim=yechim,
                   parametrlar=params or {}, svg=svg))

# 1 (2,quyi) — Tongotarov 11.1/A-1 (kalit: B=0,2 — mos ✓)
check("q1", (6-2)/(2*10), 0.2)
q(2, "quyi",
  "Hajmi 2 l bo'lgan idish 6 mol A gaz bilan to'ldirildi. 10 sekunddan keyin idishda 2 mol A gaz qoldi. "
  "Reaksiyaning o'rtacha tezligini [mol/(l·s)] aniqlang.",
  "0,2", [("0,4", "hajmga bo'lish unutilgan (4/10)"), ("0,3", "qolgan miqdor ishlatilgan"),
           ("0,1", "o'zgarish 2 mol deb olingan")],
  "Δn = 6 − 2 = 4 mol; Δc = 4/2 = 2 mol/l; v = 2/10 = 0,2 mol/(l·s).",
  dict(arch="ortacha_tezlik", V=2, n1=6, n2=2, t=10, manba="Tongotarov 11-bob, kalit bilan mos"))

# 2 (3,yuqori) — Tongotarov 11.1/A-7 (kalit: A=1/30 ✓) — birliklar tuzog'i bilan
check("q2", (8.4-5.9)/5/15, 1/30)
q(3, "yuqori",
  "Hajmi 0,005 m³ bo'lgan reaktorda reaksiya borishi natijasida 0,25 minutda modda miqdori 8,4 moldan "
  "5,9 molgacha kamaydi. Reaksiyaning o'rtacha tezligini [mol/(l·s)] hisoblang.",
  "1/30", [("1/6", "hajm 1 l deb olingan yoki minut sekundga aylantirilmagan"),
            ("2", "Δc/Δt o'rniga Δn/Δt(min) hisoblangan"),
            ("10", "birliklar butunlay aralashtirilgan")],
  "V = 0,005 m³ = 5 l; Δc = 2,5/5 = 0,5 mol/l; t = 0,25 min = 15 s; v = 0,5/15 = 1/30 mol/(l·s).",
  dict(arch="ortacha_tezlik_birlik", V=5, dn=2.5, t=15, manba="Tongotarov 11-bob, kalit mos"))

# 3 (3,yuqori) — Tongotarov 11.1/A-5 (kalit: A=0,01 ✓)
check("q3", (12.4-4.3)/10/81, 0.01, tol=1e-4)
q(3, "yuqori",
  "Hajmi 10 litr bo'lgan reaktorda reaksiya borishi natijasida 1,35 minut davomida modda miqdori 12,4 moldan "
  "4,3 molgacha kamaysa, shu reaksiyaning o'rtacha tezligini [mol/(l·s)] hisoblang.",
  "0,01", [("0,10", "hajmga bo'lish unutilgan"), ("0,64", "vaqt sekundga aylantirilmagan (0,81/1,35 xato yaxlitlangan)"),
            ("6,4", "ham hajm, ham vaqt e'tibordan chetda qolgan")],
  "Δc = (12,4 − 4,3)/10 = 0,81 mol/l; t = 1,35 min = 81 s; v = 0,81/81 = 0,01 mol/(l·s).",
  dict(arch="ortacha_tezlik", V=10, n1=12.4, n2=4.3, t=81, manba="Tongotarov 11-bob, kalit mos"))

# 4 (3,yuqori) — GRAFIK: reagent c(t)
q(3, "yuqori",
  "Reaksiya davomida REAGENT konsentratsiyasining vaqtga bog'liq o'zgarishini qaysi grafik to'g'ri ifodalaydi?",
  "kamayib boruvchi, asta-sekin sekinlashuvchi egri chiziq",
  [("to'g'ri chiziq bo'ylab ortib boruvchi", "bu mahsulot uchun ham noto'g'ri — tezlik o'zgaradi"),
   ("o'zgarmas gorizontal chiziq", "reagent sarflanadi — konsentratsiya kamayadi"),
   ("avval kamayib, so'ng ortib boruvchi", "reagent qaytib hosil bo'lmaydi")],
  "Reagent sarflangani sari konsentratsiya va u bilan birga tezlik kamayadi — egri chiziq tobora yassilanib boradi (asimptotik pasayish).",
  svg=dict(correct="fall", d1="rise", d2="flat", d3="u", xlab="t, s", ylab="c"))

# 5 (2,yuqori) — omillar (tuzoqli: gomogen uchun sirt yuzasi)
q(2, "yuqori",
  "GOMOGEN gaz fazadagi reaksiya tezligiga quyidagi omillardan qaysi biri TA'SIR QILMAYDI?\n"
  "1) harorat; 2) reagentlar konsentratsiyasi; 3) qattiq devor sirtining kattaligi; 4) katalizator; 5) bosim.",
  "faqat 3",
  [("3 va 5", "gaz reaksiyasida bosim konsentratsiyani o'zgartiradi — ta'sir qiladi"),
   ("faqat 5", "bosim gazlar uchun asosiy omillardan"),
   ("4 va 5", "katalizator har qanday reaksiyaga ta'sir qiladi")],
  "Sirt yuzasi faqat GETEROGEN reaksiyalar uchun omil; gomogen gaz reaksiyasida harorat, konsentratsiya, bosim va katalizator ta'sir qiladi.")

# 6 (3,yuqori) — Vant-Goff, kasr daraja (tuzoqli)
check("q6", 4**0.5, 2)
q(3, "yuqori",
  "Temperatura koeffitsiyenti 4 bo'lgan reaksiya tezligini 2 marta KAMAYTIRISH uchun haroratni necha gradusga pasaytirish kerak?",
  "5", [("10", "bitta to'liq qadam deb olingan (u 4 marta kamaytiradi)"),
         ("20", "kvadrat qadam — 16 marta kamaytiradi"),
         ("2,5", "chiziqli proporsiya xatosi")],
  "4^(Δt/10) = 2 → Δt/10 = 1/2 → Δt = 5 °C. (4 ning kvadrat ildizi 2 ekanidan.)",
  dict(arch="vant_goff_kasr", g=4, marta=2))

# 7 (2,yuqori) — RASMLI: ikki stakanli tajriba (bo'lak vs kukun)
q(2, "yuqori",
  "Rasmda bir xil massadagi rux BIR XIL konsentratsiyali xlorid kislota eritmasiga ikki ko'rinishda solingan: "
  "1-idishda — yaxlit bo'lak, 2-idishda — kukun. Kuzatilayotgan farqning sababini ko'rsating.",
  "2-idishda gaz jadal ajraladi — kukunning to'qnashuv sirti katta",
  [("1-idishda tezroq — bo'lak zichroq va og'irroq", "zichlik geterogen tezlikni belgilamaydi"),
   ("farq bo'lmaydi — massa va kislota bir xil", "geterogen reaksiyada sirt yuzasi hal qiluvchi omil"),
   ("2-idishda tezroq — kukun kislota konsentratsiyasini oshiradi", "kukun konsentratsiyani o'zgartirmaydi, sirtni oshiradi")],
  "Geterogen reaksiya tezligi fazalar chegarasi yuzasiga proporsional: kukunda sirt ancha katta — H₂ pufakchalari jadal ajraladi.",
  params=dict(arch="rasm_ikki_idish"))
Y1[-1]["fig"] = "beakers2"

# 8 (2,yuqori) — RASMLI: c–t grafigidan qiymat o'qish
check("q8", (2.0-1.0)/20, 0.05)
q(2, "yuqori",
  "Rasmda reagent konsentratsiyasining vaqtga bog'liq o'zgarish grafigi berilgan. Grafikdan foydalanib, "
  "0–20 s oralig'idagi o'rtacha reaksiya tezligini [mol/(l·s)] aniqlang.",
  "0,05", [("0,1", "faqat birinchi 10 s bo'yicha hisoblangan (Δc=1,0 deb)"),
            ("0,025", "Δc o'rniga yakuniy qiymat (1,0)/40 olingan"),
            ("0,07", "0–30 s oralig'i olingan (1,2/30 xato yaxlitlash bilan)")],
  "Grafikdan: c(0) = 2,0; c(20) = 1,0 mol/l → v = (2,0 − 1,0)/20 = 0,05 mol/(l·s).",
  dict(arch="grafik_oqish_ct", c0=2.0, c20=1.0))
Y1[-1]["fig"] = "ct_read"

# 9 (2,yuqori) — katalizator: noto'g'ri fikrni topish
q(2, "yuqori",
  "Katalizator haqidagi fikrlardan qaysi biri NOTO'G'RI?",
  "katalizator muvozanatni mahsulotlar tomonga siljitadi",
  [("katalizator faollanish energiyasini pasaytiradi", "bu to'g'ri fikr"),
   ("katalizator to'g'ri va teskari reaksiyani barobar tezlashtiradi", "bu to'g'ri — shuning uchun muvozanat siljimaydi"),
   ("katalizator reaksiya oxirida miqdoran o'zgarmay qoladi", "bu to'g'ri fikr")],
  "Katalizator muvozanat HOLATINI o'zgartirmaydi — u ikkala yo'nalishni teng tezlashtirib, muvozanatga yetish vaqtinigina qisqartiradi.")

# 10 (3,yuqori) — ikki omilli konsentratsiya
check("q10", 3*(2**2), 12)
q(3, "yuqori",
  "A + 2B → C gomogen reaksiyada A ning konsentratsiyasi 3 marta, B niki 2 marta oshirildi. Reaksiya tezligi necha marta ortadi?",
  "12", [("6", "B ning kvadrati hisoblanmagan (3·2)"), ("9", "faqat A ta'siri kvadratlangan"),
          ("36", "ikkala ko'paytma ham kvadratlangan")],
  "v = k[A][B]² → 3 · 2² = 12 marta.",
  dict(arch="konsentratsiya_ikki", kA=3, kB=2, stex="A+2B"))

# 11 (2,yuqori) — bosim
check("q11", 2**3, 8)
q(2, "yuqori",
  "2A(g) + B(g) → C(g) reaksiyada sistemaning bosimi 2 marta oshirilsa, reaksiya tezligi necha marta ortadi?",
  "8", [("4", "faqat A ning kvadrati hisoblangan"), ("2", "bosim barcha konsentratsiyalarni oshirishi unutilgan"),
         ("6", "darajalar qo'shilmasdan ko'paytirilgan (2·3 xato talqin)")],
  "Bosim 2 marta ortsa, barcha gaz konsentratsiyalari 2 marta ortadi: v = k[A]²[B] → 2²·2 = 8 marta.",
  dict(arch="bosim", stex="2A+B"))

# 12 (3,yuqori) — bank real savoli (javob mustaqil: 0,5)
check("q12", 8/2**4, 0.5)
q(3, "yuqori",
  "Kimyoviy reaksiya tezligi 8 mol/(l·min) ga teng bo'lgan reaksiyaning temperatura koeffitsiyenti ikkiga teng. "
  "Harorat 40 °C ga tushirilsa, keyingi reaksiya tezligi [mol/(l·min)] nechaga teng bo'ladi?",
  "0,5", [("16", "harorat KO'TARILGANDAGI hisob"), ("32", "ko'paytirish xatosi"),
           ("1/16", "tezlik nisbatini javob deb olish")],
  "v₂ = v₁/γ^(Δt/10) = 8/2⁴ = 0,5 mol/(l·min).",
  dict(arch="vant_goff_qiymat", v1=8, g=2, dt=-40, manba="MS/DTM tezlik banki, javob mustaqil tekshirildi"))

# 13 (3,yuqori) — DIM uslubi: parametrli (harfli) savol
q(3, "yuqori",
  "4NH₃ + 5O₂ → 4NO + 6H₂O reaksiyasida ammiakning sarflanish tezligi a, kislorodniki b bilan belgilangan. "
  "Suvning hosil bo'lish tezligini ifodalovchi TO'G'RI ifodalarni ko'rsating.\n"
  "I. 1,5a    II. 1,2b    III. 1,5b    IV. 1,2a",
  "I va II",
  [("III va IV", "koeffitsiyentlar almashib ketgan (6/4 va 6/5 teskari)"),
   ("faqat I", "b orqali ham ifodalash mumkin: 6/5·b = 1,2b"),
   ("I va III", "1,5b xato — b uchun nisbat 6/5")],
  "v(H₂O)/6 = v(NH₃)/4 = v(O₂)/5 → v(H₂O) = 6/4·a = 1,5a va v(H₂O) = 6/5·b = 1,2b → I va II to'g'ri.",
  dict(arch="parametrli_stex", manba="DIM parametrli savol uslubi (a-b-c), mazmun original"))

# 14 (2,yuqori) — birlik aylantirish
check("q14", 0.003*60, 0.18)
q(2, "yuqori",
  "Reaksiya tezligi 0,003 mol/(l·s) ga teng. Uni mol/(l·min) birligida ifodalang.",
  "0,18", [("0,00005", "60 ga bo'lib yuborilgan"), ("1,8", "o'nlik xatosi"),
            ("0,003", "birlik aylantirilmagan")],
  "1 min = 60 s → v = 0,003 · 60 = 0,18 mol/(l·min).",
  dict(arch="birlik_aylantirish", v=0.003))

# 15 (2,yuqori) — stexiometrik nisbat (mahsulotdan reagentga)
check("q15", 0.4*3/2, 0.6)
q(2, "yuqori",
  "N₂ + 3H₂ → 2NH₃ reaksiyasida ammiakning hosil bo'lish tezligi 0,4 mol/(l·min). Vodorodning sarflanish tezligini [mol/(l·min)] toping.",
  "0,6", [("0,27", "nisbat teskari qo'llangan (0,4·2/3)"), ("1,2", "3 ga to'g'ridan-to'g'ri ko'paytirilgan"),
           ("0,2", "azot tezligi hisoblangan")],
  "v(H₂)/3 = v(NH₃)/2 → v(H₂) = 0,4·3/2 = 0,6 mol/(l·min).",
  dict(arch="stexiometrik", vNH3=0.4))

# 16 (2,yuqori) — Vant-Goff kasr koeffitsiyent
check("q16", 2.5**2, 6.25)
q(2, "yuqori",
  "Temperatura koeffitsiyenti 2,5 bo'lgan reaksiyaning harorati 20 °C ga ko'tarildi. Tezlik necha marta ortadi?",
  "6,25", [("5", "γ ikkiga ko'paytirilgan (2,5·2)"), ("2,5", "faqat bitta qadam olingan"),
            ("12,5", "kvadrat o'rniga 2,5·5 hisoblangan")],
  "v₂/v₁ = 2,5² = 6,25 marta.",
  dict(arch="vant_goff", g=2.5, dt=20))

# 17 (3,yuqori) — JADVAL: tartiblarni aniqlash (Tongotarov 8-savol formati)
q(3, "yuqori",
  "xA + yB → C reaksiya uchun tajriba natijalari jadvalda berilgan (T = const):\n"
  "[JADVAL] № | [A], mol/l | [B], mol/l | v, mol/(l·s) ;; 1 | 1 | 1 | 2 ;; 2 | 2 | 1 | 8 ;; 3 | 1 | 2 | 4\n"
  "x va y ni aniqlang.",
  "x = 2, y = 1",
  [("x = 1, y = 2", "qatorlar almashib ketgan"), ("x = 2, y = 2", "3-tajribada v 4 marta emas, 2 marta ortgan"),
   ("x = 1, y = 1", "2-tajribada v 2 emas, 4 marta ortgan")],
  "1→2: [A] 2× → v 4× = 2ˣ → x = 2. 1→3: [B] 2× → v 2× = 2ʸ → y = 1.",
  dict(arch="jadval_tartib", data=[[1,1,2],[2,1,8],[1,2,4]], manba="Tongotarov formati, mazmun original"))

# 18 (3,yuqori) — RASMLI: energiya diagrammasi (DIM sxema-diagramma ruhida)
q(3, "yuqori",
  "Rasmda bir reaksiyaning ikki xil sharoitdagi energiya diagrammasi berilgan: 1-egri — katalizatorsiz, "
  "2-egri — katalizator ishtirokida. Diagramma asosida TO'G'RI xulosani tanlang.",
  "katalizator faollanish energiyasini Ea₁ dan Ea₂ ga kamaytirgan, reaksiyaning issiqlik effekti esa o'zgarmagan",
  [("katalizator issiqlik effektini (ΔH) ham kamaytirgan", "boshlang'ich va oxirgi sathlar ikkala egrida bir xil — ΔH o'zgarmaydi"),
   ("2-egri endotermik jarayonni bildiradi", "ikkala egri ham bir xil ΔH li jarayon — turi o'zgarmagan"),
   ("katalizator mahsulot energiyasini pasaytirgan", "mahsulot sathi ikkala holatda bir xil")],
  "Katalizator faqat cho'qqi balandligini (faollanish energiyasini) pasaytiradi; boshlang'ich va oxirgi energiya sathlari, demak ΔH — o'zgarmaydi.",
  params=dict(arch="energiya_diagramma", manba="DIM diagramma-savollari ruhida, original"),
  svg=None)
Y1[-1]["fig"] = "energy"

# 19 (3,yuqori) — kombinatsiya
check("q19", (3**2)*2, 18)
q(3, "yuqori",
  "A + B → C (birinchi tartibli A bo'yicha) reaksiyada harorat 20 °C ga oshirildi (γ = 3) va bir vaqtda A ning "
  "konsentratsiyasi 2 marta oshirildi. Reaksiya tezligi jami necha marta ortadi?",
  "18", [("11", "ta'sirlar qo'shilgan (9+2)"), ("6", "γ darajaga ko'tarilmagan (3·2)"),
          ("9", "konsentratsiya ta'siri unutilgan")],
  "Harorat: 3² = 9 marta; konsentratsiya: 2 marta. Jami: 9 · 2 = 18 marta.",
  dict(arch="kombinatsiya", g=3, dt=20, ck=2))

# 20 (2,yuqori) — katalizator mexanizmi
q(2, "yuqori",
  "Katalizator reaksiya tezligini qanday yo'l bilan oshiradi?",
  "faollanish energiyasini pasaytirib, reaksiyani yangi yo'ldan olib boradi",
  [("moddalar konsentratsiyasini oshirib", "katalizator konsentratsiyani o'zgartirmaydi"),
   ("sistema haroratini ko'tarib", "katalizator issiqlik manbai emas"),
   ("muvozanatni mahsulot tomonga siljitib", "katalizator muvozanat holatini siljitmaydi")],
  "Katalizator oraliq birikmalar orqali faollanish energiyasi pastroq bo'lgan yangi yo'l ochadi — faol to'qnashuvlar ulushi ortadi.")

# 21 (3,yuqori) — Ismoilov 2017/v3-19 arxetipi (mustaqil yechildi)
check("q21", 9**0.5, 3)
q(3, "yuqori",
  "Harorat 25 °C dan 55 °C gacha ko'tarilganda reaksiya tezligi 9 marta oshdi. Ushbu reaksiya tezligi harorat "
  "har 15 °C ga oshganda necha marta ortadi?",
  "3", [("9", "butun oraliq uchun qiymat olingan"), ("4,5", "9 ni 2 ga bo'lish xatosi"),
         ("2", "asossiz baho")],
  "30 °C = 2 · 15 °C. k² = 9 → k = 3 marta (har 15 °C uchun).",
  dict(arch="oraliq_koeff", dt=30, marta=9, manba="Ismoilov 2017 arxetipi, mustaqil yechildi"))

# 22 (3,yuqori) — Tongotarov 11.1/A-8 (kalit: A=0,05 ✓)
check("q22", 2/(2*20), 0.05)
q(3, "yuqori",
  "Hajmi 2 l bo'lgan idishda 4,5 mol modda miqdori 20 sekund o'tgandan so'ng 2,5 molgacha kamaygan bo'lsa, "
  "reaksiyaning o'rtacha tezligi [mol/(l·s)] qanchaga teng bo'ladi?",
  "0,05", [("0,10", "hajmga bo'lish unutilgan"), ("0,20", "qo'shimcha ikkilantirish"),
            ("0,50", "vaqtga bo'lish unutilgan")],
  "Δc = (4,5 − 2,5)/2 = 1 mol/l; v = 1/20 = 0,05 mol/(l·s).",
  dict(arch="ortacha_tezlik", V=2, n1=4.5, n2=2.5, t=20, manba="Tongotarov 11-bob, kalit mos"))

# 23 (3,yuqori) — mahsulot orqali
check("q23", 0.04/10/2, 0.002)
q(3, "yuqori",
  "N₂ + 3H₂ → 2NH₃ reaksiyasida 10 minut davomida ammiak konsentratsiyasi 0,04 mol/l ga ortdi. "
  "Azotning sarflanish tezligini [mol/(l·min)] toping.",
  "0,002", [("0,004", "NH₃ hosil bo'lish tezligi olingan"), ("0,008", "nisbat teskari qo'llangan"),
             ("0,012", "vodorod tezligi hisoblangan")],
  "v(NH₃) = 0,04/10 = 0,004; v(N₂) = v(NH₃)/2 = 0,002 mol/(l·min).",
  dict(arch="stexiometrik_teskari", dNH3=0.04, t=10))

# 24 (3,yuqori) — I/II/III/IV, inert gaz tuzog'i bilan
q(3, "yuqori",
  "H₂(g) + I₂(g) → 2HI(g) reaksiyasi yopiq idishda bormoqda. Quyidagi tadbirlardan qaysi biri reaksiya tezligini OSHIRMAYDI?\n"
  "I. Hajmni kichraytirish. II. Haroratni ko'tarish. III. Katalizator qo'shish. IV. O'zgarmas hajmda idishga argon yuborish.",
  "faqat IV",
  [("I va IV", "hajm kichrayishi konsentratsiyalarni oshiradi — tezlik ortadi"),
   ("faqat I", "aksincha, I tezlikni oshiradi"),
   ("III va IV", "katalizator tezlikni oshiradi")],
  "V = const da inert gaz qo'shilsa, H₂ va I₂ ning KONSENTRATSIYALARI o'zgarmaydi — tezlik ham o'zgarmaydi. "
  "Qolgan uchala tadbir tezlikni oshiradi.",
  dict(arch="inert_gaz_tuzoq"))

# 25 (3,yuqori) — γ topish
check("q25", 16**0.25, 2)
q(3, "yuqori",
  "Harorat 40 °C ga ko'tarilganda reaksiya tezligi 16 marta ortdi. Reaksiyaning temperatura koeffitsiyentini toping.",
  "2", [("4", "16 ning kvadrat ildizi olingan (2 o'rniga 4 daraja)"), ("3", "asossiz baho"),
         ("1,5", "chiziqli taqsimlash xatosi")],
  "γ⁴ = 16 → γ = 2.",
  dict(arch="gamma_topish", dt=40, marta=16))

# 26 (3,yuqori) — harorat topish
check("q26", 3**3, 27)
q(3, "yuqori",
  "Temperatura koeffitsiyenti 3 bo'lgan reaksiya tezligini 27 marta oshirish uchun haroratni necha gradusga ko'tarish kerak?",
  "30", [("27", "marta bilan gradus almashtirilgan"), ("90", "3·27 ko'paytirish xatosi"),
          ("20", "3² = 9 bilan chalkashtirilgan")],
  "3^(Δt/10) = 27 = 3³ → Δt/10 = 3 → Δt = 30 °C.",
  dict(arch="harorat_topish", g=3, marta=27))

# 27 (2,yuqori) — GRAFIK: v(T)
q(2, "yuqori",
  "Reaksiya tezligining haroratga bog'liqligini qaysi grafik to'g'ri ifodalaydi?",
  "tobora tezlashib o'suvchi egri chiziq",
  [("gorizontal to'g'ri chiziq", "harorat tezlikni kuchli oshiradi"),
   ("kamayib boruvchi egri chiziq", "harorat ortishi tezlikni oshiradi, kamaytirmaydi"),
   ("avval ortib, keyin kamayuvchi egri", "oddiy reaksiyalarda bunday maksimum yo'q")],
  "Vant-Goff bo'yicha bog'liqlik darajali (eksponensial): har +10 °C tezlikni γ marta oshiradi — egri chiziq tik ko'tarilib boradi.",
  svg=dict(correct="rise", d1="flat", d2="fall", d3="rise_fall", xlab="t, °C", ylab="v"))

# 28 (1,quyi) — ingibitor
q(1, "quyi",
  "Reaksiya tezligini sekinlashtiradigan modda qanday ataladi?",
  "ingibitor", [("katalizator", "katalizator tezlashtiradi"), ("promotor", "promotor katalizator faolligini oshiradi"),
                 ("indikator", "indikator muhitni ko'rsatadi, tezlikka ta'sir qilmaydi")],
  "Ingibitor — reaksiyani sekinlashtiruvchi modda (masalan, korroziyaga qarshi qo'shimchalar).")

# 29 (3,yuqori) — Tongotarov 11.1/A-13 (kalit: C='10 marta tez' ✓)
check("q29", 2.0/(0.1*2), 10)
q(3, "yuqori",
  "Ikkita har xil reaksiya natijasida vodorod ajralib chiqdi. Ularning birida 1 minutda 2,24 litr (n.sh.), "
  "ikkinchisida esa 2,00 g vodorod ajralgan. Ikkinchi reaksiya tezligi birinchisiga nisbatan qanday farq qilishini aniqlang.",
  "10 marta tez", [("5 marta tez", "2,24 l ni 0,224 g deb xato baholash"),
                    ("10 marta sekin", "nisbat teskari olingan"),
                    ("5 marta sekin", "ikkala xato birga")],
  "1-reaksiya: 2,24 l = 0,1 mol = 0,2 g/min. 2-reaksiya: 2,0 g/min. Nisbat: 2,0/0,2 = 10 marta tez.",
  dict(arch="taqqoslash_mol_massa", manba="Tongotarov 11-bob, kalit mos"))

# 30 (3,yuqori) — Tongotarov 11.1/A-16 (kalit: D=40 ✓)
check("q30", (2-0.8)/0.03, 40)
q(3, "yuqori",
  "A + B → AB gomogen reaksiyaning o'rtacha tezligi 0,03 mol/(l·s). Necha sekunddan keyin A moddaning "
  "konsentratsiyasi 2 mol/l dan 0,8 mol/l gacha kamayadi?",
  "40", [("30", "Δc = 0,9 deb xato olingan"), ("20", "Δc ni 2 ga bo'lish xatosi"),
          ("10", "0,3 tezlik bilan hisoblangan")],
  "t = Δc/v = (2 − 0,8)/0,03 = 1,2/0,03 = 40 s.",
  dict(arch="vaqt_topish", c1=2, c2=0.8, v=0.03, manba="Tongotarov 11-bob, kalit mos"))

# 31 (3,yuqori) — stexiometriya + konsentratsiya birga
check("q31", 0.15*2, 0.3); check("q31b", 0.3*20, 6)
q(3, "yuqori",
  "2SO₂ + O₂ → 2SO₃ reaksiyasida kislorodning sarflanish tezligi 0,15 mol/(l·min). 20 minut ichida SO₃ "
  "konsentratsiyasi qanchaga (mol/l) ortadi?",
  "6", [("3", "SO₃ tezligi O₂ nikiga teng deb olingan"), ("12", "to'rt barobar qilingan"),
         ("1,5", "vaqtga ko'paytirish o'rniga bo'lingan")],
  "v(SO₃) = 2·v(O₂) = 0,3 mol/(l·min); Δc(SO₃) = 0,3·20 = 6 mol/l.",
  dict(arch="stexiometrik_vaqt", vO2=0.15, t=20))

# 32 (2,yuqori) — RASMLI: V(H₂)–t qo'sh egri (bir xil plato)
q(2, "yuqori",
  "Rasmda TENG massadagi rux bilan bir xil kislotada o'tkazilgan ikki tajribaning V(H₂)–t grafiklari berilgan. "
  "Grafik asosida TO'G'RI xulosani tanlang.",
  "2-egri — rux kukuni: tezlik yuqori, lekin yakuniy gaz hajmi bir xil",
  [("2-egri — rux bo'lagi: bo'lak tezroq eriydi", "tikroq egri katta sirtga (kukunga) mos"),
   ("2-egri — kukun, va u ko'proq gaz beradi", "gaz miqdori modda MIQDORIGA bog'liq — plato bir xil"),
   ("egrilar har xil moddalarga tegishli", "shart bo'yicha modda bir xil, faqat maydalanganlik farq qiladi")],
  "Kukun (2) sirt yuzasi katta bo'lgani uchun tezroq reaksiyaga kirishadi — egri tik ko'tarilib, platoga erta chiqadi. "
  "Yakuniy V(H₂) esa rux MIQDORI bilan aniqlanadi — ikkala tajribada bir xil (plato ustma-ust).",
  params=dict(arch="vt_qosh_egri"))
Y1[-1]["fig"] = "vt_two"

assert len(Y1) == 32

# ---------- Y2 (33-35) ----------
check("y2_vB", (6-4.5)/25, 0.06)
check("y2_A", 3 - (2/3)*1.5, 2.0)
check("y2_vC", (1.5/3)/25, 0.02)
Y2 = dict(
  n=33, tur="Y2", element="I.5",
  ichki_pasport=[dict(n=33, element="I.5", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.5", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("2A + 3B → C gomogen reaksiyada boshlang'ich konsentratsiyalar: [A] = 3 mol/l, [B] = 6 mol/l. "
               "Reaksiya boshlangandan 25 sekund o'tgach [B] = 4,5 mol/l bo'ldi. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. B modda bo'yicha o'rtacha tezlik [mol/(l·s)] qancha?",
    "34. Shu paytdagi A ning konsentratsiyasi (mol/l) qancha?",
    "35. C mahsulotning hosil bo'lish tezligi [mol/(l·s)] qancha?"],
  javoblar_royxati=["A) 0,06", "B) 0,02", "C) 2", "D) 0,04", "E) 1,5", "F) 0,09"],
  javoblar={"33": "A", "34": "C", "35": "B"},
  chalgituvchilar=[dict(variant="D", xato="v(A) — savol A emas, C haqida (2/3 nisbat bilan chalg'itish)"),
                   dict(variant="E", xato="sarflangan B (1,5) konsentratsiya deb olingan"),
                   dict(variant="F", xato="v(B)·3/2 — nisbat teskari qo'llangan")],
  yechim=("v(B) = (6 − 4,5)/25 = 0,06 (33 → A). Sarflangan A = (2/3)·1,5 = 1 mol/l → [A] = 2 mol/l (34 → C). "
          "v(C) = v(B)/3 = 0,02 (35 → B)."),
  parametrlar=dict(arch="stexiometrik_ssenariy", stex="2A+3B->C", cA0=3, cB0=6, cB=4.5, t=25))

# ---------- O1 (36-40) ----------
check("o36", 36 + 30, 66)
check("o37", (3-1.2)/(5*30), 0.012)
check("o38", 3**4, 81)
check("o39", 3*(3**3), 81)
check("o40", (3**2)*(2**2), 36)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Temperatura koeffitsiyenti 2 bo'lgan reaksiya 36 °C da bormoqda. Tezlikni 8 marta oshirish uchun "
            "haroratni necha gradusgacha (°C) ko'tarish kerak?",
      javob="66", yechim="2^(Δt/10) = 8 = 2³ → Δt = 30 °C → 36 + 30 = 66 °C. (Diqqat: 'necha gradusGACHA' so'ralgan.)",
      parametrlar=dict(arch="harorat_gacha", t0=36, g=2, marta=8)),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="5 l idishdagi modda miqdori 30 sekundda 3 moldan 1,2 molgacha kamaydi. Reaksiyaning o'rtacha tezligini [mol/(l·s)] toping.",
      javob="0,012", yechim="Δc = 1,8/5 = 0,36 mol/l; v = 0,36/30 = 0,012 mol/(l·s).",
      parametrlar=dict(arch="ortacha_tezlik", V=5, n1=3, n2=1.2, t=30)),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Temperatura koeffitsiyenti 3 bo'lgan reaksiya tezligini 81 marta oshirish uchun haroratni necha gradusga ko'tarish kerak?",
      javob="40", yechim="3^(Δt/10) = 81 = 3⁴ → Δt = 40 °C.", parametrlar=dict(arch="harorat_topish", g=3, marta=81)),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="A(g) + 3B(g) → 2C(g) reaksiyada sistemaning bosimi 3 marta oshirildi. Reaksiya tezligi necha marta ortadi?",
      javob="81", yechim="Barcha konsentratsiyalar 3 marta ortadi: v = k[A][B]³ → 3·3³ = 81 marta.",
      parametrlar=dict(arch="bosim", stex="A+3B", p=3)),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="2A(g) → B(g) reaksiyada harorat 20 °C ga ko'tarildi (γ = 3) va bir vaqtda idish hajmi 2 marta kichraytirildi. Tezlik jami necha marta ortadi?",
      javob="36", yechim="Harorat: 3² = 9; hajm 2 marta kichraysa [A] 2 marta ortadi → v = 2² = 4. Jami: 9·4 = 36.",
      parametrlar=dict(arch="kombinatsiya", g=3, dt=20, v_kichray=2, stex=2)),
]

# ---------- O2 (41-43) ----------
check("o41a", 0.8/2, 0.4); check("o41a2", 0.6/2, 0.3)
check("o41b", 2.5*0.4**2*0.3, 0.12)
check("o41c", 0.3-0.1, 0.2); check("o41c2", 0.4-0.2, 0.2)
check("o41d", 2.5*0.2**2*0.2, 0.02); check("o41d2", 0.12/0.02, 6)
check("o41e", 0.02*2**3, 0.16); check("o41e2", 0.16/0.12, 4/3, tol=0.01)
check("o42a", 4*2**6, 256)
check("o42b", 256/32, 8); check("o42b2", 20+30, 50)
check("o43a", 64/10, 6.4)
check("o43b", (112-96)/10, 1.6)
check("o43d", 0.112/22.4, 0.005); check("o43d2", 0.005*65, 0.325)
O2 = [
 dict(n=41, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Hajmi 2 litr bo'lgan yopiq idishga 0,8 mol NO va 0,6 mol O₂ yuborildi. Idishda "
            "2NO(g) + O₂(g) → 2NO₂(g) reaksiyasi bormoqda; tezlik qonuni v = k[NO]²[O₂], "
            "k = 2,5 l²/(mol²·s). Har bir band oldingi band natijasiga tayanadi."),
      bandlar=[
        dict(savol="a) Moddalarning boshlang'ich konsentratsiyalarini (mol/l) hisoblang.",
             yechim=["[NO] = 0,8/2 = 0,4 mol/l; [O₂] = 0,6/2 = 0,3 mol/l"], M=2, A=1),
        dict(savol="b) Reaksiyaning boshlang'ich tezligini [mol/(l·s)] hisoblang.",
             yechim=["v₁ = k[NO]²[O₂] = 2,5·(0,4)²·0,3 = 0,12 mol/(l·s)"], M=3, A=2),
        dict(savol="c) 0,2 mol O₂ reaksiyaga kirishgan paytdagi har ikki reagent konsentratsiyasini toping.",
             yechim=["Δ[O₂] = 0,2/2 = 0,1 mol/l → [O₂] = 0,2 mol/l",
                     "Δ[NO] = 2·0,1 = 0,2 mol/l → [NO] = 0,2 mol/l"], M=3, A=2),
        dict(savol="d) Shu paytdagi tezlikni hisoblang va u boshlang'ich tezlikdan necha marta kichikligini toping.",
             yechim=["v₂ = 2,5·(0,2)²·0,2 = 0,02 mol/(l·s)", "v₁/v₂ = 0,12/0,02 = 6 marta"], M=3, A=3),
        dict(savol="e) Aynan shu holatda harorat 30 °C ga ko'tarilsa (γ = 2), yangi tezlik boshlang'ich (b-banddagi) "
                   "tezlikdan katta bo'ladimi? Hisob bilan asoslang.",
             yechim=["v₃ = 0,02·2³ = 0,16 mol/(l·s)", "v₃/v₁ = 0,16/0,12 = 4/3 ≈ 1,33 — ha, boshlang'ichdan katta:",
                     "harorat ta'siri konsentratsiya kamayishini ortig'i bilan qoplagan."], M=4, A=2),
      ],
      rasmiylashtirish="5 bandlik zanjirli 41-topshiriq (DTM mezoni): M jami 15, A jami 10; har band oldingisiz yechilmaydi.",
      parametrlar=dict(arch="tezlik_qonuni_zanjir", V=2, nNO=0.8, nO2=0.6, k=2.5)),
 dict(n=42, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Reaksiya 80 °C da 4 sekundda tugaydi. Temperatura koeffitsiyenti γ = 2. "
            "Bandlar ketma-ket yechiladi: b-band a-band natijasiga tayanadi."),
      bandlar=[
        dict(savol="a) Xuddi shu reaksiya 20 °C da necha sekundda tugashini aniqlash yo'lini yozing va hisoblang.",
             yechim=["Δt = 60 °C → tezlik 2⁶ = 64 marta kichik → vaqt 64 marta katta:",
                     "t(20°) = 4·64 = 256 sekund"], M=13, A=0),
        dict(savol="b) Qanday haroratda (°C) reaksiya 32 sekundda tugaydi?",
             yechim=["256/32 = 8 = 2³ marta tezlashishi kerak → Δt = 30 °C → t = 20 + 30 = 50 °C"], M=9, A=0),
        dict(savol="c) Ushbu hisoblar qanday faraz asosida bajarildi? Qisqacha yozing.",
             yechim=["γ butun 20–80 °C oralig'ida o'zgarmas deb faraz qilindi (Vant-Goff — taxminiy empirik qoida)."], M=3, A=0),
      ],
      rasmiylashtirish="42-topshiriq (DTM mezoni): faqat usul (M), 3 zanjirli band: M13+M9+M3 = 25.",
      parametrlar=dict(arch="vant_goff_ikki_bosqich", t80=4, g=2)),
 dict(n=43, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada ortiqcha xlorid kislotaga rux bo'lagi tashlandi va ajralgan vodorod hajmi (n.sh.ga "
            "keltirilgan) har 10 sekundda o'lchab borildi:\n"
            "[JADVAL] t, s | 0 | 10 | 20 | 30 | 40 ;; V(H₂), ml | 0 | 64 | 96 | 112 | 112\n"
            "Jadval ma'lumotlari asosida quyidagi bandlarni bajaring (bandlar ketma-ket yechiladi)."),
      bandlar=[
        dict(savol="a) 0–10 s oralig'idagi o'rtacha reaksiya tezligini (ml H₂ / s hisobida) toping.",
             yechim=["v₁ = 64/10 = 6,4 ml/s"], M=2, A=2),
        dict(savol="b) 20–30 s oralig'idagi o'rtacha tezlikni toping va uning a-banddagidan kichikligi sababini yozing.",
             yechim=["v₃ = (112 − 96)/10 = 1,6 ml/s", "sabab: HCl sarflangani sari konsentratsiyasi kamayadi"], M=3, A=2),
        dict(savol="c) Reaksiya qaysi vaqt oralig'ida tugaganini jadvaldan aniqlang va buni qanday bilganingizni yozing.",
             yechim=["30–40 s oralig'ida: V(H₂) o'zgarmay qoldi (112 ml) — gaz ajralishi to'xtagan"], M=3, A=1),
        dict(savol="d) Reaksiyaga kirishgan rux massasini (g) hisoblang. (Zn = 65)",
             yechim=["n(H₂) = 0,112/22,4 = 0,005 mol", "Zn + 2HCl → ZnCl₂ + H₂ → n(Zn) = 0,005 mol",
                     "m(Zn) = 0,005·65 = 0,325 g"], M=4, A=3),
        dict(savol="e) Xuddi shu tajriba teng massadagi rux KUKUNI bilan takrorlansa, V(H₂)–t grafigi qanday "
                   "o'zgaradi va yakuniy hajm qancha bo'ladi? Asoslang.",
             yechim=["Egri chiziq boshida ancha tikroq ko'tarilib, platoga tezroq chiqadi (sirt yuzasi katta —",
                     "tezlik yuqori); yakuniy hajm esa O'ZGARMAYDI — 112 ml (modda miqdori bir xil)."], M=3, A=2),
      ],
      rasmiylashtirish="Tajriba-tahlil formatidagi 43-topshiriq (kimyoviy tahlil ruhida): jadvalni o'qish + hisob + xulosa; M15+A10 = 25.",
      parametrlar=dict(arch="tajriba_jadval_kinetika", V=[0, 64, 96, 112, 112], dt=10)),
]

# ---------- harflarni balanslash ----------
letters = "ABCD"
rng = random.Random(20260905)
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
    rest = opts[1:]
    slots = [j for j in range(4) if j != ti]
    for s, o in zip(slots, rest):
        arranged[s] = o
    variantlar = [o[0] for o in arranged]
    javob = letters[variantlar.index(item["correct"])]
    assert javob == target
    chalg = [dict(variant=letters[j], xato=arranged[j][1]) for j in range(4) if arranged[j][1]]
    d = dict(n=n, tur="Y1", element="I.5", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
             savol=item["savol"], variantlar=variantlar, javob=javob,
             chalgituvchilar=chalg, yechim=item["yechim"], parametrlar=item["parametrlar"])
    if item.get("svg"):
        d["svg"] = item["svg"]
    if item.get("fig"):
        d["fig"] = item["fig"]
    final_y1.append(d)

dist = {c: sum(1 for x in final_y1 if x["javob"] == c) for c in letters}
print("Y1 harf taqsimoti:", dist)
assert all(v == 8 for v in dist.values()), dist
for x in final_y1:
    assert x["variantlar"][letters.index(x["javob"])] == Y1[x["n"]-1]["correct"]
print("Y1 javob-harf tekshiruvi: OK (32/32)")

bad = [c for c in CHECKS if not c[3]]
for name, got, exp, ok in CHECKS:
    if not ok:
        print("XATO:", name, got, exp)
assert not bad
print(f"Sonli tekshiruvlar: OK ({len(CHECKS)}/{len(CHECKS)})")

# O2 ball nazorati
for o in O2:
    M = sum(b["M"] for b in o["bandlar"]); A = sum(b["A"] for b in o["bandlar"])
    assert M + A == 25, (o["n"], M, A)
    print(f"O2-{o['n']}: M={M} A={A} jami=25 OK")

variant = dict(
    variant="mavzu-I5",
    bob=5, bob_nomi="Kimyoviy reaksiya tezligi",
    manba=("aralash: o'rtacha-tezlik arxetiplari Tongotarov 11-bobidan (rasmiy javob kaliti bilan solishtirildi), "
           "Vant-Goff arxetiplari MS/DTM tezlik bankidan; grafik/jadval formatlari DIM va Tongotarovdan; "
           "nazariy savollar 9-sinf darsligi chegarasida original"),
    izoh=("1-kitob (Anorganik kimyo) 5-bobi — KUCHAYTIRILGAN rejim: qiyinlik xaritasi yuqoriga surilgan "
          "(ta'rif-savollar o'rniga ko'p bosqichli hisoblar, birlik-tuzoqlari, inert gaz va kasr-darajali "
          "Vant-Goff holatlari). Barcha 43 topshiriq I.5 elementiga bag'ishlangan; MS strukturasi saqlangan."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT, "— yozuvlar:", len(variant["savollar"]))
