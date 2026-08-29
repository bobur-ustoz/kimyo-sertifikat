# -*- coding: utf-8 -*-
"""5-bob A-varianti: Kimyoviy reaksiya tezligi (I.5) — IMTIHON DARAJASI (rasmiy MS xaritasi).
Sonlar B-variantdan butunlay farq qiladi; arxetiplar imtihon taqsimotida."""
import json, random

OUT = "mavzu_I5A.json"
CHECKS = []
def check(name, got, expected, tol=1e-6):
    ok = abs(got - expected) <= tol
    CHECKS.append((name, got, expected, ok))
    return ok

Y1 = []
def q(d, k, savol, correct, distractors, yechim, params=None, svg=None, fig=None):
    Y1.append(dict(qiyinlik=d, kognitiv=k, savol=savol, correct=correct,
                   distractors=distractors, yechim=yechim,
                   parametrlar=params or {}, svg=svg, fig=fig))

# 1 (2,quyi)
check("q1", (8-3)/4/10, 0.125)
q(2, "quyi",
  "Hajmi 4 l bo'lgan idishdagi gaz miqdori 10 sekundda 8 moldan 3 molgacha kamaydi. Reaksiyaning o'rtacha tezligini [mol/(l·s)] aniqlang.",
  "0,125", [("0,5", "hajmga bo'lish unutilgan"), ("0,05", "qolgan miqdor bilan hisoblangan"),
             ("0,25", "Δn = 10 deb olingan")],
  "Δc = (8 − 3)/4 = 1,25 mol/l; v = 1,25/10 = 0,125 mol/(l·s).",
  dict(arch="ortacha_tezlik", V=4, n1=8, n2=3, t=10))

# 2 (1,quyi)
q(1, "quyi",
  "Kimyoviy reaksiya tezligi deb nimaga aytiladi?",
  "vaqt birligi ichida modda konsentratsiyasining o'zgarishiga",
  [("reaksiya to'liq tugashi uchun ketgan vaqtga", "bu davomiylik, tezlik emas"),
   ("hosil bo'lgan mahsulotning umumiy massasiga", "miqdor, tezlik emas"),
   ("reaksiyada ajralgan issiqlik miqdoriga", "bu issiqlik effekti")],
  "v = ±Δc/Δt; birligi mol/(l·s) yoki mol/(l·min).")

# 3 (2,quyi)
check("q3", (2.4-1.2)/6, 0.2)
q(2, "quyi",
  "Reagent konsentratsiyasi 6 sekund ichida 2,4 mol/l dan 1,2 mol/l gacha kamaydi. O'rtacha tezlikni [mol/(l·s)] toping.",
  "0,2", [("0,4", "ikkilantirish xatosi"), ("0,1", "Δc = 0,6 deb olingan"),
           ("1,2", "vaqtga bo'lish unutilgan")],
  "v = (2,4 − 1,2)/6 = 0,2 mol/(l·s).", dict(arch="ortacha_tezlik_c", c1=2.4, c2=1.2, t=6))

# 4 (3,yuqori) — GRAFIK: mahsulot c(t)
q(3, "yuqori",
  "Reaksiya davomida MAHSULOT konsentratsiyasining vaqtga bog'liq o'zgarishini qaysi grafik to'g'ri ifodalaydi?",
  "ortib boruvchi, asta-sekin sekinlashuvchi egri chiziq",
  [("kamayib boruvchi egri chiziq", "bu reagent grafigi"),
   ("o'zgarmas gorizontal chiziq", "mahsulot to'planib boradi"),
   ("avval ortib, so'ng kamayuvchi egri", "mahsulot qaytib sarflanmaydi")],
  "Mahsulot to'planadi: boshida tez, reagentlar kamaygani sari sekinroq — egri chiziq yassilanib boradi.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="rise_fall", xlab="t, s", ylab="c"))

# 5 (2,quyi) — HIKOYALI RASM: muzlatgich
q(2, "quyi",
  "Rasmga qarang: bir xil sut va olma muzlatgichda (+4 °C) xona haroratidagiga (+25 °C) qaraganda ancha uzoq "
  "saqlanadi. Buning kimyoviy sababi nimada?",
  "past haroratda buzilish reaksiyalarining tezligi keskin kichik bo'ladi",
  [("muzlatgich ichida mikroblar umuman bo'lmaydi", "mikroblar bor, faqat past haroratda biokimyoviy jarayonlari sekin"),
   ("muzlatgichda yorug'lik yo'qligi buzilishni to'xtatadi", "asosiy omil yorug'lik emas, harorat"),
   ("sovuq havo mahsulotni qattiq qilib qo'yadi", "qotish tezlikni belgilamaydi")],
  "Vant-Goff qoidasi teskarisiga ham ishlaydi: harorat ~20 °C past bo'lsa, buzilish (oksidlanish, mikrob "
  "biokimyosi) reaksiyalari tezligi taxminan γ² marta kamayadi — mahsulot uzoq saqlanadi.",
  fig="fridge")

# 6 (2,yuqori)
check("q6", 2**3, 8)
q(2, "yuqori",
  "Temperatura koeffitsiyenti 2 bo'lgan reaksiyaning harorati 30 °C ga ko'tarildi. Tezlik necha marta ortadi?",
  "8", [("6", "2·3 — daraja o'rniga ko'paytma"), ("16", "4 qadam deb olingan"),
         ("2", "bitta qadam hisoblangan")],
  "v₂/v₁ = 2^(30/10) = 2³ = 8 marta.", dict(arch="vant_goff", g=2, dt=30))

# 7 (1,yuqori) — RASMLI (A: marmar + HCl, kukun 1-idishda!)
q(1, "yuqori",
  "Rasmda bir xil massadagi marmar (CaCO₃) bir xil xlorid kislotaga ikki ko'rinishda solingan: 1-idishda kukun, "
  "2-idishda yaxlit bo'lak. Nega 1-idishda CO₂ jadalroq ajralmoqda?",
  "kukunning to'qnashuv sirti katta",
  [("kukun kislota konsentratsiyasini oshiradi", "kukun konsentratsiyani o'zgartirmaydi"),
   ("kukunning harorati yuqori", "harorat bir xil"),
   ("bo'lak kislotani sekin shimadi", "gap shimishda emas, sirt yuzasida")],
  "Geterogen reaksiya tezligi fazalar chegarasi yuzasiga bog'liq — kukunda sirt ancha katta, CO₂ jadal ajraladi.",
  fig="beakers2_m")

# 8 (2,yuqori)
check("q8", 3**2, 9)
q(2, "yuqori",
  "Temperatura koeffitsiyenti 3 bo'lgan reaksiyaning harorati 20 °C ga pasaytirildi. Tezlik qanday o'zgaradi?",
  "9 marta kamayadi", [("9 marta ortadi", "pasayishda tezlik KAMAYADI"),
                        ("6 marta kamayadi", "3·2 ko'paytma xatosi"),
                        ("3 marta kamayadi", "bitta qadam hisoblangan")],
  "v kamayadi: 3^(20/10) = 9 marta.", dict(arch="vant_goff_pasayish", g=3, dt=20))

# 9 (1,quyi) — HIKOYALI RASM: avtomobil neytralizatori
q(1, "quyi",
  "Rasmda avtomobilning katalitik neytralizatori ko'rsatilgan: undagi platina-rodiy qatlami zararli CO va NOₓ "
  "gazlarini zararsiz CO₂ va N₂ ga aylantiradi. Bu qatlamning kimyoviy vazifasi nima?",
  "zararsizlantirish reaksiyalarini tezlashtirish — o'zi esa sarflanmaydi",
  [("zararli gazlarni g'ovaklarida filtrlab ushlab qolish", "u filtr emas — gazlar reaksiyaga KIRIB chiqadi"),
   ("chiqindi gazlar haroratini pasaytirish", "sovutish emas, katalizatorlik vazifasi"),
   ("reaksiyada o'zi sarflanib, gazlar bilan birikish", "katalizator sarflanmaydi — shu bois yillab xizmat qiladi")],
  "Pt–Rh qatlami tipik katalizator: CO va NOₓ ning zararsiz moddalarga aylanish reaksiyalari faollanish "
  "energiyasini pasaytirib, ularni ming marta tezlashtiradi; o'zi jarayonda sarflanmaydi.",
  fig="car_cat")

# 10 (2,quyi)
check("q10", 3, 3)
q(2, "quyi",
  "A + B → C gomogen reaksiyada A ning konsentratsiyasi 3 marta oshirilsa (qolganlari o'zgarmas), tezlik qanday o'zgaradi?",
  "3 marta ortadi", [("9 marta ortadi", "koeffitsiyent 1 — kvadrat kerak emas"),
                      ("o'zgarmaydi", "ta'sir etuvchi massalar qonuniga zid"),
                      ("3 marta kamayadi", "ortish o'rniga kamayish deb olingan")],
  "v = k[A][B] → 3 marta ortadi.", dict(arch="konsentratsiya", kA=3))

# 11 (2,yuqori)
check("q11", 3*(3**2), 27)
q(2, "yuqori",
  "A(g) + 2B(g) → C(g) reaksiyada sistemaning bosimi 3 marta oshirilsa, tezlik necha marta ortadi?",
  "27", [("9", "A ning ulushi hisobga olinmagan"), ("6", "darajalar qo'shilmagan (3+3)"),
          ("81", "to'rtinchi daraja olingan")],
  "Barcha konsentratsiyalar 3× → v = k[A][B]² → 3·3² = 27 marta.",
  dict(arch="bosim", stex="A+2B", p=3))

# 12 (3,yuqori)
check("q12", 6/2**3, 0.75)
q(3, "yuqori",
  "Tezligi 6 mol/(l·min) bo'lgan reaksiyaning temperatura koeffitsiyenti 2 ga teng. Harorat 30 °C ga tushirilsa, yangi tezlik [mol/(l·min)] qancha bo'ladi?",
  "0,75", [("48", "harorat ko'tarilgandagi hisob"), ("2", "6/3 chiziqli xato"),
            ("1,5", "ikki qadamgina olingan")],
  "v₂ = 6/2³ = 0,75 mol/(l·min).", dict(arch="vant_goff_qiymat", v1=6, g=2, dt=-30))

# 13 (2,quyi) — HIKOYALI RASM: kema va ingibitor
q(2, "quyi",
  "Rasmda dengiz kemasining suv ostidagi qismi maxsus — tarkibida INGIBITOR bo'lgan bo'yoq bilan qoplangani "
  "ko'rsatilgan. Ingibitorning vazifasi nima?",
  "temirning sho'r suvdagi korroziya reaksiyasi tezligini keskin sekinlashtirish",
  [("korroziya reaksiyasini tezlashtirish", "bu katalizator ta'siri bo'lardi — aksincha kerak"),
   ("kema korpusini og'irlashtirib, muvozanat berish", "bo'yoq massasi ahamiyatsiz"),
   ("suvning sho'rligini kamaytirish", "bo'yoq dengiz tarkibini o'zgartira olmaydi")],
  "Sho'r suv — elektrolit, temir korroziyasi unda juda tez boradi. Ingibitor qo'shilgan qoplama shu "
  "reaksiyaning tezligini minglab marta kamaytiradi — kema 20–30 yil xizmat qiladi.",
  fig="ship")

# 14 (1,quyi)
q(1, "quyi",
  "Gomogen reaksiya tezligining o'lchov birligini ko'rsating.",
  "mol/(l·s)", [("mol/l", "konsentratsiya birligi"), ("l/mol", "teskari kattalik"),
                 ("g/ml", "zichlik birligi")],
  "Tezlik = konsentratsiya o'zgarishi / vaqt: mol/(l·s).")

# 15 (2,yuqori)
check("q15", 0.2*3, 0.6)
q(2, "yuqori",
  "N₂ + 3H₂ → 2NH₃ reaksiyasida azotning sarflanish tezligi 0,2 mol/(l·min). Vodorodning sarflanish tezligini [mol/(l·min)] toping.",
  "0,6", [("0,2", "koeffitsiyent hisobga olinmagan"), ("0,4", "NH₃ koeffitsiyenti ishlatilgan"),
           ("0,067", "nisbat teskari")],
  "v(H₂) = 3·v(N₂) = 0,6 mol/(l·min).", dict(arch="stexiometrik", vN2=0.2))

# 16 (2,quyi)
q(2, "quyi",
  "Vant-Goff qoidasiga ko'ra, harorat har 10 °C ga ko'tarilganda ko'pchilik reaksiyalarning tezligi qanday o'zgaradi?",
  "2–4 marta ortadi",
  [("10 marta ortadi", "gradusga tenglashtirish xatosi"),
   ("o'zgarmaydi", "harorat asosiy omil"),
   ("2–4 marta kamayadi", "ko'tarilishda ORTADI")],
  "γ odatda 2–4: har +10 °C da tezlik γ marta ortadi.")

# 17 (3,yuqori) — jadval: vaqt-konsentratsiya o'qish va solishtirish (B dagi tartib-jadvalidan farqli tur)
check("q17a", (1.8-1.2)/10, 0.06); check("q17b", (1.2-0.9)/10, 0.03)
q(3, "yuqori",
  "Jadvalda reagent konsentratsiyasining vaqt bo'yicha o'lchangan qiymatlari berilgan:\n"
  "[JADVAL] t, s | 0 | 10 | 20 ;; [A], mol/l | 1,8 | 1,2 | 0,9\n"
  "0–10 s va 10–20 s oraliqlardagi o'rtacha tezliklar nisbatini (v₁ : v₂) toping.",
  "2 : 1",
  [("3 : 2", "konsentratsiyalar nisbati olingan (1,8:1,2)"),
   ("1 : 2", "nisbat teskari yozilgan"),
   ("4 : 3", "asossiz baho")],
  "v₁ = (1,8−1,2)/10 = 0,06; v₂ = (1,2−0,9)/10 = 0,03 → v₁:v₂ = 2:1.",
  dict(arch="jadval_vaqt_oqish", data=[[0,1.8],[10,1.2],[20,0.9]]))

# 18 (2,quyi) — HIKOYALI RASM: gulxan
q(2, "quyi",
  "Rasmga qarang: gulxan yoqishda avval mayda cho'plar tutashtiriladi (2), yaxlit g'o'la (1) esa juda qiyin "
  "yonib ketadi. Buning sababi nimada?",
  "mayda cho'plarning umumiy sirt yuzasi katta — kislorod bilan to'qnashuv ko'p",
  [("mayda cho'plarning namligi kam bo'ladi", "namlik teng deb olinadi — gap sirt yuzasida"),
   ("g'o'laning zichligi olov o'tkazmaydi", "zichlik emas, sirt yuzasi hal qiluvchi"),
   ("mayda cho'plarda uglerod ko'proq", "kimyoviy tarkib bir xil — yog'och")],
  "Yonish — geterogen reaksiya (qattiq yog'och + havo kislorodi): tezlik fazalar chegarasi yuzasiga bog'liq. "
  "Teng massada mayda cho'plarning sirti g'o'lanikidan yuzlab marta katta.",
  fig="campfire")

# 19 (3,yuqori)
check("q19", (2**2)*3, 12)
q(3, "yuqori",
  "A + B → C (A bo'yicha birinchi tartibli) reaksiyada harorat 20 °C ga oshirildi (γ = 2) va A ning konsentratsiyasi 3 marta oshirildi. Tezlik jami necha marta ortadi?",
  "12", [("7", "ta'sirlar qo'shilgan (4+3)"), ("6", "γ darajaga ko'tarilmagan"),
          ("4", "konsentratsiya unutilgan")],
  "Harorat: 2² = 4; konsentratsiya: 3. Jami: 12 marta.",
  dict(arch="kombinatsiya", g=2, dt=20, ck=3))

# 20 (2,yuqori)
q(2, "yuqori",
  "Katalizator reaksiya tezligini qanday yo'l bilan oshiradi?",
  "faollanish energiyasini pasaytirib, reaksiyani yangi yo'ldan olib boradi",
  [("moddalar konsentratsiyasini oshirib", "konsentratsiyani o'zgartirmaydi"),
   ("sistema haroratini ko'tarib", "issiqlik manbai emas"),
   ("muvozanatni mahsulot tomonga siljitib", "muvozanatni siljitmaydi")],
  "Katalizator Ea pastroq yangi yo'l ochadi — faol to'qnashuvlar ulushi ortadi.")

# 21 (3,yuqori)
check("q21", 8**(1/3), 2)
q(3, "yuqori",
  "Harorat 30 °C dan 60 °C gacha ko'tarilganda reaksiya tezligi 8 marta oshdi. Har 10 °C ga necha marta ortadi (γ)?",
  "2", [("8", "butun oraliq qiymati olingan"), ("2,7", "8/3 chiziqli xato"),
         ("4", "ikki qadam deb olingan")],
  "30° = 3 qadam; γ³ = 8 → γ = 2.", dict(arch="gamma_topish", dt=30, marta=8))

# 22 (3,yuqori) — teskari masala: tezlikdan miqdorni topish (yangi arxetip)
check("q22", 0.02*25*3, 1.5)
q(3, "yuqori",
  "3 l idishdagi gomogen reaksiyaning o'rtacha tezligi 0,02 mol/(l·s). 25 sekund davomida necha mol reagent sarflanadi?",
  "1,5", [("0,5", "idish hajmiga ko'paytirish unutilgan"), ("0,17", "bo'lish-ko'paytirish almashgan"),
           ("2,5", "hajm o'rniga vaqtga yana ko'paytirilgan")],
  "Δc = v·t = 0,02·25 = 0,5 mol/l; Δn = 0,5·3 = 1,5 mol.",
  dict(arch="miqdor_topish", v=0.02, t=25, V=3))

# 23 (3,yuqori)
check("q23", 0.3/2, 0.15)
q(3, "yuqori",
  "2SO₂ + O₂ → 2SO₃ reaksiyasida SO₂ ning sarflanish tezligi 0,3 mol/(l·min). Kislorodning sarflanish tezligini toping.",
  "0,15", [("0,3", "koeffitsiyent e'tiborsiz"), ("0,6", "nisbat teskari"),
            ("0,075", "to'rtga bo'lingan")],
  "v(O₂) = v(SO₂)/2 = 0,15 mol/(l·min).", dict(arch="stexiometrik", vSO2=0.3))

# 24 (3,yuqori)
q(3, "yuqori",
  "N₂(g) + 3H₂(g) → 2NH₃(g) reaksiyasining tezligini qaysi tadbirlar oshiradi?\n"
  "I. Bosimni oshirish. II. Haroratni ko'tarish. III. Katalizator qo'shish.",
  "I, II va III",
  [("faqat I va II", "katalizator ham oshiradi"), ("faqat II va III", "gaz reaksiyasida bosim ishlaydi"),
   ("faqat II", "uchalasi ham ishlaydi")],
  "Bosim (gazlar uchun), harorat va katalizator — uchalasi tezlikni oshiradi.")

# 25 (3,yuqori)
check("q25", 27**(1/3), 3)
q(3, "yuqori",
  "Harorat 30 °C ga ko'tarilganda reaksiya tezligi 27 marta ortdi. Temperatura koeffitsiyentini toping.",
  "3", [("9", "kvadrat ildiz olingan"), ("2", "asossiz baho"), ("27", "marta bilan γ almashgan")],
  "γ³ = 27 → γ = 3.", dict(arch="gamma_topish", dt=30, marta=27))

# 26 (3,yuqori)
check("q26", 2**5, 32)
q(3, "yuqori",
  "Temperatura koeffitsiyenti 2 bo'lgan reaksiya tezligini 32 marta oshirish uchun haroratni necha gradusga ko'tarish kerak?",
  "50", [("32", "marta bilan gradus almashgan"), ("40", "2⁴ = 16 bilan chalkashuv"),
          ("25", "yarim qiymat")],
  "2^(Δt/10) = 32 = 2⁵ → Δt = 50 °C.", dict(arch="harorat_topish", g=2, marta=32))

# 27 (2,yuqori) — ikki idish taqqoslash (grafiksiz, B dagi v-T grafigidan farqli tur)
check("q27", 0.3/0.1, 3)
q(2, "yuqori",
  "Bir xil o'lchamdagi rux bo'laklari 0,1 M li va 0,3 M li xlorid kislota eritmalariga solindi (harorat bir xil, "
  "reaksiya H⁺ bo'yicha birinchi tartibli). Boshlang'ich tezliklar nisbatini (konsentrlangan : suyultirilgan) toping.",
  "3 : 1",
  [("9 : 1", "kvadratga ko'tarilgan"), ("1 : 1", "geterogen deb konsentratsiya ta'sirsiz deyilgan — H⁺ eritmada"),
   ("1 : 3", "nisbat teskari")],
  "v ∝ [H⁺] → 0,3/0,1 = 3 marta tez.",
  dict(arch="ikki_idish_taqqos", c1=0.1, c2=0.3))

# 28 (1,quyi)
q(1, "quyi",
  "Reaksiya tezligini sekinlashtiradigan modda qanday ataladi?",
  "ingibitor", [("katalizator", "u tezlashtiradi"), ("promotor", "katalizator faolligini oshiradi"),
                 ("indikator", "muhitni ko'rsatadi")],
  "Ingibitor — reaksiyani sekinlashtiruvchi modda.")

# 29 (2,quyi)
q(2, "quyi",
  "Tirik organizmlardagi kimyoviy jarayonlarni tezlashtiruvchi biologik katalizatorlar qanday ataladi?",
  "fermentlar", [("gormonlar", "signal moddalar"), ("vitaminlar", "ko'pincha ferment tarkibida, o'zi katalizator emas"),
                  ("ingibitorlar", "sekinlashtiradi")],
  "Fermentlar (enzimlar) — oqsil tabiatli biologik katalizatorlar.")

# 30 (1,quyi)
q(1, "quyi",
  "Cho'g'lanib turgan ko'mir toza kislorodda havodagiga qaraganda tezroq yonadi. Sababi nimada?",
  "kislorod konsentratsiyasi yuqoriligida",
  [("kislorod haroratining yuqoriligida", "harorat bir xil"),
   ("azotning katalizatorlik ta'sirida", "azot suyultiruvchi, xolos"),
   ("bosimning pastligida", "bosim asosiy omil emas")],
  "Toza kislorodda konsentratsiya ~5 marta yuqori — tezlik mos ravishda ortadi.")

# 31 (2,yuqori)
check("q31", 0.3/2, 0.15)
q(2, "yuqori",
  "N₂ + 3H₂ → 2NH₃ reaksiyasida ammiakning hosil bo'lish tezligi 0,3 mol/(l·min). Azotning sarflanish tezligini toping.",
  "0,15", [("0,3", "koeffitsiyent e'tiborsiz"), ("0,6", "nisbat teskari"),
            ("0,45", "3/2 nisbat ishlatilgan (vodorod)")],
  "v(N₂) = v(NH₃)/2 = 0,15 mol/(l·min).", dict(arch="stexiometrik", vNH3=0.3))

# 32 (2,yuqori) — RASMLI: V(CO₂)-t qo'sh egri (A: kukun — 1-egri!)
q(2, "yuqori",
  "Rasmda teng massadagi marmar bilan ikki tajribaning V(CO₂)–t grafiklari berilgan. Qaysi egri chiziq marmar KUKUNI bilan o'tkazilgan tajribaga mos?",
  "1-egri — u tikroq ko'tarilib, platoga erta chiqadi",
  [("2-egri — kukun sekinroq eriydi", "kukun sirt katta — TEZROQ eriydi; 2-egri sekin"),
   ("ikkalasi ham bir xil moddaga mos, farqlab bo'lmaydi", "tezliklar farqi grafikda aniq ko'rinadi"),
   ("1-egri, chunki u ko'proq gaz bergan", "plato bir xil — gaz miqdori teng, farq faqat tezlikda")],
  "Kukun (1) sirt yuzasi katta — tezlik yuqori, egri tik; yakuniy hajm (plato) ikkalasida bir xil.",
  fig="vt_two_a")

assert len(Y1) == 32

# B-variant bilan pozitsion arxetip mosligini sindirish: bir xil (qiyinlik, kognitiv)
# juftliklarning o'rni almashtiriladi
for i, j in [(12, 22), (15, 27), (23, 25), (11, 20), (19, 26)]:
    assert (Y1[i-1]["qiyinlik"], Y1[i-1]["kognitiv"]) == (Y1[j-1]["qiyinlik"], Y1[j-1]["kognitiv"]), (i, j)
    Y1[i-1], Y1[j-1] = Y1[j-1], Y1[i-1]

# ---------- Y2 (A: Vant-Goff ssenariysi — B dagi stexiometrik ssenariydan farqli tur) ----------
check("y2_40", 0.2*4, 0.8)
check("y2_50", 0.2*8, 1.6)
check("y2_t", 6.4/0.2, 32); check("y2_t2", 20+50, 70)
Y2 = dict(
  n=33, tur="Y2", element="I.5",
  ichki_pasport=[dict(n=33, element="I.5", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.5", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=35, element="I.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Gomogen reaksiyaning 20 °C dagi tezligi 0,2 mol/(l·min), temperatura koeffitsiyenti γ = 2. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. 40 °C da reaksiya tezligi [mol/(l·min)] qancha bo'ladi?",
    "34. 50 °C da reaksiya tezligi [mol/(l·min)] qancha bo'ladi?",
    "35. Qanday haroratda (°C) tezlik 6,4 mol/(l·min) ga yetadi?"],
  javoblar_royxati=["A) 1,6", "B) 70", "C) 0,8", "D) 3,2", "E) 0,4", "F) 60"],
  javoblar={"33": "C", "34": "A", "35": "B"},
  chalgituvchilar=[dict(variant="D", xato="60 °C dagi tezlik (bitta qadam ortiqcha)"),
                   dict(variant="E", xato="30 °C dagi qiymat — bitta qadam kam"),
                   dict(variant="F", xato="6,4 uchun harorat xato: 2⁴ = 16 deb olib 60 °C chiqarish")],
  yechim=("40 °C: 0,2·2² = 0,8 (33 → C). 50 °C: 0,2·2³ = 1,6 (34 → A). "
          "6,4/0,2 = 32 = 2⁵ → Δt = 50 → 70 °C (35 → B)."),
  parametrlar=dict(arch="vant_goff_ssenariy", v20=0.2, g=2))

# ---------- O1 ----------
check("o36", 2**2, 4)
check("o37", 0.04*30*2, 2.4)
check("o38", 81**0.25, 3)
check("o39", 0.05*2, 0.1)
check("o40", 64/2**3, 8)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="Temperatura koeffitsiyenti 2 bo'lgan reaksiyaning harorati 20 °C ga ko'tarildi. Tezlik necha marta ortadi?",
      javob="4", yechim="2² = 4 marta.", parametrlar=dict(arch="vant_goff", g=2, dt=20)),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="2 l idishdagi gomogen reaksiyaning o'rtacha tezligi 0,04 mol/(l·s). 30 sekund davomida necha mol reagent sarflanadi?",
      javob="2,4", yechim="Δc = 0,04·30 = 1,2 mol/l; Δn = 1,2·2 = 2,4 mol.",
      parametrlar=dict(arch="miqdor_topish", v=0.04, t=30, V=2)),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Harorat 25 °C dan 65 °C gacha ko'tarilganda reaksiya tezligi 81 marta ortdi. Temperatura koeffitsiyentini toping.",
      javob="3", yechim="Δt = 40 °C = 4 qadam; γ⁴ = 81 → γ = 3.",
      parametrlar=dict(arch="gamma_topish", dt=40, marta=81)),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="CH₄ + 2O₂ → CO₂ + 2H₂O reaksiyasida metanning sarflanish tezligi 0,05 mol/(l·s). Kislorodning sarflanish tezligini toping.",
      javob="0,1", yechim="v(O₂) = 2·v(CH₄) = 0,1 mol/(l·s).", parametrlar=dict(arch="stexiometrik", vCH4=0.05)),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Reaksiya 50 °C da 64 sekundda tugaydi (γ = 2). 80 °C da reaksiya necha sekundda tugaydi?",
      javob="8", yechim="Δt = 30 °C → tezlik 2³ = 8 marta ortadi → vaqt: 64/8 = 8 s.",
      parametrlar=dict(arch="vant_goff_vaqt", t1=64, g=2, dt=30)),
]

# ---------- O2 ----------
check("o41a", 0.36/0.04, 9); check("o41a2", 9**0.5, 3)
check("o41b", 0.36*9, 3.24)
check("o41c", 3**5, 243)
check("o41d", 90/9, 10)
check("o42a", 0.09/3, 0.03); check("o42a2", 0.09*2/3, 0.06)
check("o42b", 0.06*20, 1.2)
O2 = [
 dict(n=41, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Bir reaksiya ikki haroratda o'rganildi: 20 °C da tezlik 0,04 mol/(l·min), 40 °C da esa "
            "0,36 mol/(l·min) bo'ldi. Bandlar ketma-ket yechiladi — har biri oldingi natijaga tayanadi."),
      bandlar=[
        dict(savol="a) Reaksiyaning temperatura koeffitsiyentini (γ) toping.",
             yechim=["0,36/0,04 = 9 = γ² (Δt = 20 °C) → γ = 3"], M=3, A=2),
        dict(savol="b) 60 °C dagi tezlikni hisoblang.",
             yechim=["v(60°) = 0,36·3² = 3,24 mol/(l·min)"], M=3, A=2),
        dict(savol="c) Qanday haroratda tezlik boshlang'ichidan (20 °C) 243 marta katta bo'ladi?",
             yechim=["243 = 3⁵ → Δt = 50 °C → t = 70 °C"], M=3, A=2),
        dict(savol="d) 20 °C da reaksiya 90 sekundda tugasa, 40 °C da necha sekundda tugaydi?",
             yechim=["Tezlik 9 marta katta → vaqt 9 marta kichik: 90/9 = 10 s"], M=3, A=2),
        dict(savol="e) γ ning fizik ma'nosini va bu hisoblar qaysi farazga asoslanganini yozing.",
             yechim=["γ — harorat 10 °C ga ortganda tezlik necha marta ortishini ko'rsatadi;",
                     "hisoblar γ butun oraliqda o'zgarmas degan farazga asoslangan."], M=3, A=2),
      ],
      rasmiylashtirish="Tajriba-ma'lumotidan γ topish zanjiri: M15+A10. (B-variantdagi tezlik-qonuni zanjiridan farqli format.)",
      parametrlar=dict(arch="gamma_zanjir", v20=0.04, v40=0.36)),
 dict(n=42, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn="N₂ + 3H₂ → 2NH₃ reaksiyasida vodorodning sarflanish tezligi 0,09 mol/(l·min).",
      bandlar=[
        dict(savol="a) Azotning sarflanish va ammiakning hosil bo'lish tezliklarini aniqlash yo'lini yozing va hisoblang.",
             yechim=["v(N₂) = v(H₂)/3 = 0,03 mol/(l·min)", "v(NH₃) = 2·v(N₂) = 0,06 mol/(l·min)"], M=13, A=0),
        dict(savol="b) 20 minut davomida ammiak konsentratsiyasi qanchaga ortadi?",
             yechim=["Δc(NH₃) = 0,06·20 = 1,2 mol/l"], M=9, A=0),
        dict(savol="c) Nega bitta reaksiyada moddalarning tezliklari har xil? Qisqacha tushuntiring.",
             yechim=["Tezliklar stexiometrik koeffitsiyentlarga proporsional — moddalar turli",
                     "nisbatda sarflanadi/hosil bo'ladi."], M=3, A=0),
      ],
      rasmiylashtirish="42-topshiriq: faqat M, 3 band: M13+M9+M3 = 25. (B-variantdagi Vant-Goff formatidan farqli.)",
      parametrlar=dict(arch="stexiometrik_zanjir", vH2=0.09, t=20)),
 dict(n=43, tur="O2", element="I.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Zn + 2HCl → ZnCl₂ + H₂ reaksiyasi ustida 5 ta amal bajarildi. Har bir holat uchun reaksiya tezligi "
            "qanday o'zgarishini (ortadi / kamayadi / o'zgarmaydi) aniqlang va sababini yozing.\n"
            "[JADVAL] № | Holat ;; 1 | Kislota konsentratsiyasi oshirildi ;; "
            "2 | Eritma muzdek suvda sovutildi ;; 3 | Rux bo'lagi kukun holiga keltirildi ;; "
            "4 | Eritmaga suv qo'shildi ;; 5 | Idish ustidagi havo bo'shlig'i kattalashtirildi"),
      bandlar=[
        dict(savol="1-holat", yechim=["ORTADI — H⁺ konsentratsiyasi ortadi, to'qnashuvlar ko'payadi"], M=3, A=2),
        dict(savol="2-holat", yechim=["KAMAYADI — faol to'qnashuvlar ulushi kamayadi"], M=3, A=2),
        dict(savol="3-holat", yechim=["ORTADI — fazalar chegarasi yuzasi keskin ortadi"], M=3, A=2),
        dict(savol="4-holat", yechim=["KAMAYADI — HCl suyuladi, [H⁺] kamayadi"], M=3, A=2),
        dict(savol="5-holat", yechim=["O'ZGARMAYDI — reaksiya eritmada boradi; ustidagi gaz bo'shlig'i unga ta'sir qilmaydi"], M=3, A=2),
      ],
      rasmiylashtirish="Omillar-jadval formati: M15+A10. (B-variantdagi o'lchov-jadval formatidan farqli.)",
      parametrlar=dict(arch="omillar_jadval", reaksiya="Zn+2HCl")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260912)
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
    d = dict(n=n, tur="Y1", element="I.5", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
             savol=item["savol"], variantlar=variantlar, javob=javob,
             chalgituvchilar=chalg, yechim=item["yechim"], parametrlar=item["parametrlar"])
    if item.get("svg"): d["svg"] = item["svg"]
    if item.get("fig"): d["fig"] = item["fig"]
    final_y1.append(d)

dist = {c: sum(1 for x in final_y1 if x["javob"] == c) for c in letters}
print("A-variant harf taqsimoti:", dist)
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
print("O2 ballari: OK")

variant = dict(
    variant="mavzu-I5-A", daraja="A", bob=5, bob_nomi="Kimyoviy reaksiya tezligi",
    manba="Tongotarov 11-bob va MS/DTM tezlik banki arxetiplari (yangi sonlar bilan), nazariy savollar darslik chegarasida original",
    izoh="A-varianti — IMTIHON DARAJASI ★★: rasmiy MS qiyinlik xaritasi (5 oson, 15 o'rta, 12 qiyin). Sonlar B-variantdan farqli.",
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
