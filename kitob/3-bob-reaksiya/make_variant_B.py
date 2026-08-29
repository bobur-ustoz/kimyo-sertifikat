# -*- coding: utf-8 -*-
"""3-bob B-varianti: Kimyoviy reaksiya turlari va issiqlik effekti (I.3) — HAQIQIY MS MUHITI ★★★.
Termokimyoviy hisoblar, Gess qonuni, kalorimetr, teskari va aralashma masalalari.
Tongotarov/Spectrum arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_I3B.json"
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

# 1 (3) — 1-2-3: ekzotermik tanlov
q(3, "yuqori",
  "Quyidagi jarayonlardan qaysilari EKZOTERMIK?\n"
  "1) C + O₂ → CO₂;  2) CaCO₃ → CaO + CO₂;  3) HCl + NaOH → NaCl + H₂O;  4) N₂ + O₂ → 2NO.",
  "1 va 3",
  [("2 va 4", "bular endotermik — issiqlik yutiladi"),
   ("faqat 1", "neytrallanish ham issiqlik beradi (57,3 kJ/mol)"),
   ("1, 3 va 4", "NO hosil bo'lishi − 180 kJ — endotermik")],
  "Yonish va neytrallanish — ekzo; karbonat parchalanishi va NO sintezi — endo.",
  dict(arch="ekzo_tanlov123"))

# 2 (3) — teskari: Q dan massa
check("q2", 222.5/890*16, 4)
q(3, "yuqori",
  "Metan yonishida (Q = 890 kJ/mol) 222,5 kJ issiqlik ajraldi. Yoqilgan metan massasini toping.",
  "4 g", [("16 g", "1 mol deb olingan"), ("8 g", "0,5 mol — ikki baravar ko'p"),
           ("2 g", "yana ikkiga bo'lingan")],
  "n = 222,5/890 = 0,25 mol → m = 0,25 · 16 = 4 g.",
  dict(arch="metan_teskari_massa"))

# 3 (3) — Gess: C→CO
check("q3", 393.5-283, 110.5)
q(3, "yuqori",
  "Ma'lum: C + O₂ → CO₂ + 393,5 kJ va CO + ½O₂ → CO₂ + 283 kJ. "
  "C + ½O₂ → CO reaksiyasining issiqlik effektini toping.",
  "110,5 kJ", [("676,5 kJ", "ayirish o'rniga qo'shilgan"), ("283 kJ", "ikkinchi bosqich effekti"),
                ("−110,5 kJ", "reaksiya ekzotermik: ishora musbat")],
  "Gess qonuni: Q₁ = Q(umumiy) − Q₂ = 393,5 − 283 = 110,5 kJ.",
  dict(arch="hess_co"))

# 4 (3) — Al yonishi
check("q4", 5.4/27/2*1676, 167.6)
q(3, "yuqori",
  "4Al + 3O₂ → 2Al₂O₃ + 3352 kJ. 5,4 g alyuminiy yonganda qancha issiqlik ajraladi? (M(Al)=27)",
  "167,6 kJ", [("838 kJ", "1 mol Al uchun qiymat"), ("3352 kJ", "4 mol Al uchun"),
                ("335,2 kJ", "nol adashgan")],
  "n(Al) = 0,2 mol; 4 mol Al — 3352 kJ → 0,2 mol — 3352·0,2/4 = 167,6 kJ.",
  dict(arch="al_yonish"))

# 5 (3) — RASMLI: profil o'qish
check("q5", 200-120, 80)
q(3, "yuqori",
  "Rasmdagi energiya diagrammasidan reaksiyaning issiqlik effektini aniqlang.",
  "80 kJ ajraladi",
  [("80 kJ yutiladi", "mahsulot energiyasi PAST — issiqlik ajraladi"),
   ("150 kJ ajraladi", "bu aktivlanish energiyasi (cho'qqigacha)"),
   ("230 kJ ajraladi", "cho'qqi bilan mahsulot farqi — teskari reaksiya to'sig'i")],
  "Q = E(reagent) − E(mahsulot) = 200 − 120 = 80 kJ (+Q, ekzotermik).",
  dict(arch="profil_dH"), fig="profile")

# 6 (3) — almashinish tanlov
q(3, "yuqori",
  "Qaysi reaksiya ALMASHINISH turiga kiradi va oxirigacha boradi?",
  "BaCl₂ + H₂SO₄ → BaSO₄↓ + 2HCl",
  [("Zn + H₂SO₄ → ZnSO₄ + H₂", "o'rin olish (oddiy modda bor)"),
   ("SO₃ + H₂O → H₂SO₄", "birikish"),
   ("2H₂O₂ → 2H₂O + O₂", "parchalanish")],
  "Ikki murakkab modda qism almashdi; BaSO₄ cho'kmasi jarayonni oxirigacha yetkazadi.",
  dict(arch="almashinish_tanlov"))

# 7 (3) — 1-2-3: parchalanish
q(3, "yuqori",
  "Qaysi reaksiyalar PARCHALANISH turiga kiradi?\n"
  "1) 2KMnO₄ → K₂MnO₄ + MnO₂ + O₂;  2) NH₃ + HCl → NH₄Cl;  "
  "3) 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂;  4) Fe + S → FeS.",
  "1 va 3",
  [("2 va 4", "bular birikish reaksiyalari"),
   ("faqat 1", "soda parchalanishi ham shu tur"),
   ("1, 2 va 3", "NH₃ + HCl — ikki moddadan bitta: birikish")],
  "Bitta moddadan bir nechta mahsulot: KMnO₄ va NaHCO₃ parchalanishi.",
  dict(arch="parchalanish_tanlov123"))

# 8 (2)
q(2, "yuqori",
  "Termokimyoviy tenglamada «−Q» yozuvi nimani anglatadi?",
  "reaksiya issiqlik yutilishi bilan borishini (endotermik)",
  [("issiqlik ajralishini", "ajralish «+Q» bilan yoziladi"),
   ("reaksiya umuman bormasligini", "boradi, lekin energiya talab qiladi"),
   ("mahsulot miqdori kamligini", "Q miqdorga emas, energiyaga tegishli")],
  "−Q: sistema energiya yutadi — uzluksiz qizdirish talab etiladi.",
  dict(arch="minusq_belgi"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi reaksiyalarni turlari bilan TO'G'RI moslang:\n"
  "[JADVAL] Reaksiya | Tur ;; a) CuO + H₂ → Cu + H₂O | 1) birikish ;; "
  "b) 2SO₂ + O₂ → 2SO₃ | 2) o'rin olish ;; c) Cu(OH)₂ → CuO + H₂O | 3) parchalanish",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "H₂ oddiy modda Cu ni siqib chiqaradi — o'rin olish"),
   ("a—2, b—3, c—1", "SO₂ + O₂ dan bitta mahsulot — birikish"),
   ("a—3, b—1, c—2", "Cu(OH)₂ bitta moddadan ikkitaga ajraldi — parchalanish")],
  "a: oddiy H₂ kislorodni «tortib oldi» — o'rin olish; b: birikish; c: parchalanish.",
  dict(arch="tur_moslash_jadval"))

# 10 (3)
check("q10", 0.4/2*198, 39.6)
q(3, "yuqori",
  "2SO₂ + O₂ → 2SO₃ + 198 kJ. 0,4 mol SO₃ hosil bo'lganda qancha issiqlik ajraladi?",
  "39,6 kJ", [("198 kJ", "2 mol SO₃ uchun qiymat"), ("79,2 kJ", "ikki baravar ko'p"),
               ("19,8 kJ", "nisbat xato")],
  "2 mol SO₃ — 198 kJ → 0,4 mol — 198·0,4/2 = 39,6 kJ.",
  dict(arch="so3_q"))

# 11 (3) — Q dan gaz hajmi
check("q11", 44.4/2220*3*22.4, 1.344, tol=0.005)
q(3, "yuqori",
  "Propan yonishida (C₃H₈ + 5O₂ → 3CO₂ + 4H₂O + 2220 kJ) 44,4 kJ issiqlik ajraldi. "
  "Hosil bo'lgan CO₂ ning hajmini (n.sh., L) toping.",
  "1,344", [("0,448", "propanning o'zi hisoblangan"), ("4,48", "nol adashgan"),
             ("2,24", "CO₂ koeffitsiyenti unutilgan")],
  "n(C₃H₈) = 44,4/2220 = 0,02 mol → n(CO₂) = 0,06 mol → V = 0,06·22,4 = 1,344 L.",
  dict(arch="propan_co2_hajm"))

# 12 (2)
q(2, "yuqori",
  "Termokimyoviy tenglamaning oddiy tenglamadan farqi nimada?",
  "issiqlik effekti (Q) ko'rsatiladi",
  [("koeffitsiyentlar bo'lmaydi", "koeffitsiyentlar saqlanadi"),
   ("faqat gazlar uchun yoziladi", "har qanday moddalar uchun yoziladi"),
   ("strelka ishlatilmaydi", "strelka bor")],
  "Termokimyoviy tenglama: tenglama + issiqlik effekti (masalan, ... + 890 kJ).",
  dict(arch="termoteng_tarif"))

# 13 (3)
check("q13", 57.3*0.5, 28.65)
q(3, "yuqori",
  "Neytrallanish issiqligi 57,3 kJ/mol. 0,5 mol HCl to'liq neytrallanganda qancha issiqlik ajraladi?",
  "28,65 kJ", [("57,3 kJ", "1 mol uchun qiymat"), ("114,6 kJ", "ikki baravar ko'p"),
                ("14,3 kJ", "chorak olingan")],
  "Q = 0,5 · 57,3 = 28,65 kJ.",
  dict(arch="neytrallanish_q"))

# 14 (3) — JADVAL «?»
check("q14a", 890/2, 445); check("q14b", 393.5*2, 787)
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring (Q — ajralgan issiqlik):\n"
  "[JADVAL] Yoqilg'i | mol | Q, kJ ;; CH₄ (890 kJ/mol) | 0,5 | ? ;; C (393,5 kJ/mol) | 2 | ?",
  "445; 787",
  [("890; 393,5", "mol soniga ko'paytirilmagan"), ("445; 393,5", "ikkinchi qator 2 mol"),
   ("1780; 787", "birinchi qator 0,5 mol — kamayadi")],
  "CH₄: 0,5·890 = 445 kJ; C: 2·393,5 = 787 kJ.",
  dict(arch="q_jadval"))

# 15 (3) — solishtirma issiqlik
check("q15", 286/2, 143)
q(3, "yuqori",
  "Qaysi yoqilg'ining 1 GRAMMI yonganda eng ko'p issiqlik ajraladi? "
  "(H₂ — 286 kJ/mol; CH₄ — 890 kJ/mol; C — 393,5 kJ/mol)",
  "vodorod (143 kJ/g)",
  [("metan (55,6 kJ/g)", "890/16 ≈ 56 — vodoroddan kam"),
   ("ko'mir (32,8 kJ/g)", "393,5/12 ≈ 33 — eng kam"),
   ("hammasi teng", "molyar massalar farqli — gramm hisobida farq katta")],
  "1 g uchun: H₂ — 286/2 = 143; CH₄ — 55,6; C — 32,8 kJ/g. Shu bois H₂ — raketa yoqilg'isi.",
  dict(arch="solishtirma_issiqlik"))

# 16 (2)
q(2, "yuqori",
  "Gess qonuniga ko'ra reaksiyaning issiqlik effekti nimaga bog'liq?",
  "faqat boshlang'ich va oxirgi holatlarga",
  [("reaksiya bosqichlari soniga", "yo'l qanday bo'lmasin, effekt bir xil"),
   ("katalizator tabiatiga", "katalizator Q ni o'zgartirmaydi"),
   ("idish shakliga", "termodinamikaga aloqasi yo'q")],
  "Gess qonuni: Q oraliq bosqichlarga bog'liq emas — shu tufayli Q ni hisoblab topish mumkin.",
  dict(arch="hess_tarif"))

# 17 (3)
q(3, "yuqori",
  "Moddaning HOSIL BO'LISH issiqligi deb nimaga aytiladi?",
  "1 mol birikma ODDIY moddalardan hosil bo'lishidagi issiqlik effektiga",
  [("1 g modda yonishidagi issiqlikka", "bu solishtirma yonish issiqligi"),
   ("moddani parchalashga ketgan issiqlikka", "bu teskari jarayon effekti"),
   ("istalgan reaksiyaning issiqligiga", "aynan oddiy moddalardan 1 mol uchun")],
  "Masalan: H₂ + ½O₂ → H₂O + 286 kJ — suvning hosil bo'lish issiqligi 286 kJ/mol.",
  dict(arch="hosil_bolish_tarif"))

# 18 (2)
q(2, "yuqori",
  "Uglerod chala yonganda (kislorod yetishmasa) nima hosil bo'ladi va bu nima uchun xavfli?",
  "CO — zaharli is gazi",
  [("CO₂ — bo'g'uvchi gaz", "CO₂ to'liq yonishda hosil bo'ladi"),
   ("kul — chang", "kul mineral qoldiq, gaz emas"),
   ("H₂ — portlovchi gaz", "uglerod yonishida vodorod ajralmaydi")],
  "2C + O₂ → 2CO: rangsiz, hidsiz, gemoglobinni bog'laydi — pechlarni erta yopish xavfli.",
  dict(arch="chala_yonish"))

# 19 (3) — RASMLI: kalorimetr
check("q19", 500*4.2*40/1000, 84)
q(3, "yuqori",
  "Rasmdagi kalorimetrda yoqilg'i namunasi yondirildi: 500 g suv 20 °C dan 60 °C gacha isidi. "
  "Suvga o'tgan issiqlikni toping. (c = 4,2 J/(g·°C))",
  "84 kJ", [("8,4 kJ", "nol adashgan"), ("126 kJ", "Δt = 60 deb olingan"),
             ("42 kJ", "Δt = 20 deb olingan")],
  "Q = mcΔt = 500 · 4,2 · 40 = 84 000 J = 84 kJ.",
  dict(arch="kalorimetr_hisob"), fig="calorimeter")

# 20 (2)
q(2, "yuqori",
  "Termokimyoviy tenglamalarda koeffitsiyentlar KASR bo'lishi mumkinmi?",
  "mumkin — ular mol nisbatlarni bildiradi",
  [("mumkin emas — atomlar bo'linmaydi", "tenglama molekulalar emas, MOLLAR haqida"),
   ("faqat gazlarda mumkin", "istalgan moddada mumkin"),
   ("faqat endotermik reaksiyalarda", "issiqlik belgisiga bog'liq emas")],
  "H₂ + ½O₂ → H₂O + 286 kJ: ½ mol O₂ — bu 3,01·10²³ ta molekula, mantiqan to'g'ri.",
  dict(arch="kasr_koeff"))

# 21 (3)
check("q21", 10/2*92, 460)
q(3, "yuqori",
  "N₂ + 3H₂ → 2NH₃ + 92 kJ. 10 mol ammiak hosil bo'lganda qancha issiqlik ajraladi?",
  "460 kJ", [("920 kJ", "92 ni to'g'ridan-to'g'ri 10 ga ko'paytirilgan"),
              ("92 kJ", "2 mol uchun qiymat"), ("230 kJ", "yana ikkiga bo'lingan")],
  "2 mol NH₃ — 92 kJ → 10 mol — 92·10/2 = 460 kJ.",
  dict(arch="nh3_q"))

# 22 (3) — 1-2-3 qo'sh shart
q(3, "yuqori",
  "Qaysi reaksiyalar HAM o'rin olish, HAM ekzotermik?\n"
  "1) Zn + 2HCl → ZnCl₂ + H₂ + Q;  2) CaCO₃ → CaO + CO₂ − Q;  "
  "3) Fe + CuSO₄ → FeSO₄ + Cu + Q;  4) SO₃ + H₂O → H₂SO₄ + Q.",
  "1 va 3",
  [("1, 3 va 4", "SO₃ + H₂O — birikish, o'rin olish emas"),
   ("faqat 1", "Fe + CuSO₄ ham o'rin olish va issiqlik beradi"),
   ("2 va 4", "2 — parchalanish va endotermik")],
  "O'rin olish (oddiy modda + murakkab) va +Q: 1 va 3.",
  dict(arch="orin_ekzo_tanlov"))

# 23 (3) — aralashma
check("q23", 0.3*890 + 0.2*1560, 579)
q(3, "yuqori",
  "0,3 mol metan (890 kJ/mol) va 0,2 mol etan (1560 kJ/mol) aralashmasi to'liq yondirildi. "
  "Jami ajralgan issiqlikni toping.",
  "579 kJ", [("2450 kJ", "molyar qiymatlar shunchaki qo'shilgan"),
              ("445 kJ", "faqat metan hisoblangan"), ("312 kJ", "faqat etan hisoblangan")],
  "Q = 0,3·890 + 0,2·1560 = 267 + 312 = 579 kJ.",
  dict(arch="aralash_q"))

# 24 (2)
q(2, "yuqori",
  "Ekzotermik reaksiyada mahsulotlarning ichki energiyasi boshlang'ich moddalarnikiga nisbatan qanday?",
  "past — farq issiqlik sifatida ajraladi",
  [("yuqori", "yuqori bo'lsa issiqlik yutilardi (endo)"),
   ("teng", "teng bo'lsa Q = 0 bo'lardi"),
   ("avval yuqori, so'ng teng", "oxirgi holat baribir pastda")],
  "Energiya saqlanadi: sistemadan chiqqan issiqlik = sathlar farqi.",
  dict(arch="energiya_past"))

# 25 (3) — hosil bo'lish issiqliklaridan
check("q25", 393.5 + 2*286 - 75, 890.5)
q(3, "yuqori",
  "Hosil bo'lish issiqliklari: CO₂ — 393,5; H₂O — 286; CH₄ — 75 kJ/mol. "
  "Metanning yonish issiqligini hisoblang.",
  "890,5 kJ/mol",
  [("754,5 kJ/mol", "CH₄ ni ayirish o'rniga qo'shilgan: 393,5+2·286−75"),
   ("604,5 kJ/mol", "H₂O koeffitsiyenti (2) unutilgan"),
   ("358,5 kJ/mol", "hisob tartibsiz")],
  "Q(yonish) = [393,5 + 2·286] − 75 = 965,5 − 75 = 890,5 kJ/mol (Gess qonuni asosida).",
  dict(arch="hess_hosil_bolish"))

# 26 (3) — RASMLI: yoqilg'ilar 1 g (ustunlar)
check("q26", 10*55, 550)
q(3, "yuqori",
  "Diagrammada yoqilg'ilarning 1 g uchun yonish issiqliklari berilgan. 10 g metan yonganda "
  "qancha issiqlik ajraladi?",
  "550 kJ", [("890 kJ", "bu 1 mol (16 g) uchun"), ("330 kJ", "ko'mir ustuni olingan"),
              ("1430 kJ", "vodorod ustuni olingan")],
  "Diagrammadan CH₄ ≈ 55 kJ/g → Q = 10 · 55 = 550 kJ.",
  dict(arch="bar_fuel_hisob"), fig="bar_fuel")

# 27 (3)
check("q27", 50/100*178, 89)
q(3, "yuqori",
  "CaCO₃ → CaO + CO₂ − 178 kJ. 50 g ohaktoshni to'liq parchalash uchun qancha issiqlik kerak? "
  "(M(CaCO₃)=100)",
  "89 kJ", [("178 kJ", "1 mol (100 g) uchun"), ("356 kJ", "ikki baravar ko'p"),
             ("44,5 kJ", "chorak olingan")],
  "n = 0,5 mol → Q = 0,5 · 178 = 89 kJ yutiladi.",
  dict(arch="caco3_endo_q"))

# 28 (2) — RASMLI: aktivlanish energiyasi
q(2, "yuqori",
  "5-savoldagi diagrammada boshlang'ich sath bilan egri chiziq CHO'QQISI orasidagi farq nimani bildiradi?",
  "aktivlanish energiyasini",
  [("issiqlik effektini", "Q — boshlang'ich va OXIRGI sathlar farqi"),
   ("mahsulot energiyasini", "mahsulot sathi — o'ng pastda"),
   ("reaksiya tezligini", "tezlik diagrammada bevosita ko'rinmaydi")],
  "Cho'qqigacha «to'siq» — reaksiya boshlanishi uchun kerakli minimal energiya (Eₐ).",
  dict(arch="aktivlanish_oqish"), fig="profile")

# 29 (3)
check("q29", 5.6/56*64, 6.4)
q(3, "yuqori",
  "5,6 g temir mis(II) sulfat eritmasi bilan to'liq reaksiyaga kirishdi. Ajralgan mis massasini toping. "
  "(M(Fe)=56, M(Cu)=64)",
  "6,4 g", [("5,6 g", "massalar teng emas — M lar farqli"), ("3,2 g", "ikkiga bo'lingan"),
             ("12,8 g", "ikki baravar ko'p")],
  "Fe + CuSO₄ → FeSO₄ + Cu: n = 0,1 mol → m(Cu) = 0,1·64 = 6,4 g.",
  dict(arch="fe_cu_massa"))

# 30 (2)
q(2, "yuqori",
  "Katalizator reaksiyaning issiqlik effektiga qanday ta'sir qiladi?",
  "o'zgartirmaydi — faqat aktivlanish energiyasini pasaytiradi",
  [("Q ni oshiradi", "Q holatlar farqi — katalizatorga bog'liq emas"),
   ("Q ni kamaytiradi", "Gess qonuniga zid bo'lardi"),
   ("reaksiyani endotermikka aylantiradi", "effekt tabiatini o'zgartira olmaydi")],
  "Katalizator yo'lni (to'siqni) o'zgartiradi, boshlang'ich/oxirgi holatlarni emas.",
  dict(arch="katalizator_q"))

# 31 (3)
check("q31", 5.6/22.4*1300, 325)
q(3, "yuqori",
  "Atsetilen yonishida 1 mol C₂H₂ dan 1300 kJ issiqlik ajraladi. 5,6 L (n.sh.) atsetilen yonganda "
  "qancha issiqlik ajraladi?",
  "325 kJ", [("1300 kJ", "22,4 L (1 mol) uchun"), ("650 kJ", "0,5 mol deb olingan"),
              ("162,5 kJ", "yana ikkiga bo'lingan")],
  "n = 5,6/22,4 = 0,25 mol → Q = 0,25·1300 = 325 kJ — shu bois payvandlashda ishlatiladi.",
  dict(arch="atsetilen_hajm_q"))

# 32 (3) — RASMLI: teskari reaksiya
q(3, "yuqori",
  "5-savoldagi diagrammadagi reaksiya uchun TESKARI reaksiyaning issiqlik effekti qanday bo'ladi?",
  "80 kJ yutiladi (endotermik)",
  [("80 kJ ajraladi", "teskari yo'nalishda ishorasi almashadi"),
   ("150 kJ yutiladi", "bu to'g'ri reaksiyaning aktivlanish energiyasi"),
   ("0 kJ", "energiya farqi yo'qolmaydi")],
  "To'g'ri reaksiya +80 kJ bersa, teskarisi −80 kJ: mahsulotdan reagentga «tepalikka chiqish».",
  dict(arch="teskari_reaksiya_q"), fig="profile")

# ---------- Y2: uch reaksiya ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.3",
  ichki_pasport=[dict(n=33, element="I.3", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.3", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch reaksiya berilgan: X — 2H₂ + O₂ → 2H₂O + 572 kJ; "
               "Y — CaCO₃ → CaO + CO₂ − 178 kJ; Z — Zn + 2HCl → ZnCl₂ + H₂ + Q. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Qaysi reaksiya endotermik va qaysi turga kiradi?",
    "34. X reaksiyada 0,5 mol O₂ sarflansa, qancha issiqlik ajraladi?",
    "35. Z reaksiyaning turi qanday?"],
  javoblar_royxati=["A) Y; parchalanish", "B) 286 kJ", "C) o'rin olish",
                    "D) X; birikish", "E) 572 kJ", "F) almashinish"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="X ekzotermik (+572 kJ) — endotermik emas"),
                   dict(variant="E", xato="572 kJ — 1 mol O₂ (2 mol H₂) uchun; 0,5 mol O₂ → yarmi"),
                   dict(variant="F", xato="Zn — oddiy modda: bu almashinish emas, o'rin olish")],
  yechim=("Y: −178 kJ, parchalanish (A). X da 1 mol O₂ — 572 kJ → 0,5 mol — 286 kJ (B). "
          "Z: oddiy modda murakkabdan vodorodni siqib chiqaradi — o'rin olish (C)."),
  parametrlar=dict(arch="uch_reaksiya_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36", 8/16*890 + 15/30*1560, 1225)
check("o37", 150.5/(1204/2)*24, 6)
check("o38", 5000*4.2*42.4/1000, 890.4, tol=0.5)
check("o39", (297 + 198/2)*0.5, 198)
check("o40a", 2*890-1176, 604); check("o40b", 604/(890-286), 1)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="8 g metan (890 kJ/mol) va 15 g etan (1560 kJ/mol) aralashmasi to'liq yondirildi. "
            "Jami ajralgan issiqlikni (kJ) toping. (M: CH₄=16, C₂H₆=30)",
      javob="1225", yechim="n(CH₄)=0,5; n(C₂H₆)=0,5 → Q = 0,5·890 + 0,5·1560 = 445 + 780 = 1225 kJ.",
      parametrlar=dict(arch="aralash_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="2Mg + O₂ → 2MgO + 1204 kJ. 150,5 kJ issiqlik olish uchun necha gramm magniy yoqish kerak? "
            "(M(Mg)=24)",
      javob="6", yechim="1 mol Mg — 602 kJ → n = 150,5/602 = 0,25 mol → m = 0,25·24 = 6 g.",
      parametrlar=dict(arch="mg_teskari_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi qurilmada metan yondirilib, ajralgan issiqlik YO'QOTISHSIZ 5 kg suvni 20 °C dan "
            "62,4 °C gacha isitdi (c = 4,2 J/(g·°C)). Sarflangan metan hajmini (n.sh., L) toping. "
            "(Q = 890 kJ/mol)",
      javob="22,4", yechim="Q = 5000·4,2·42,4 ≈ 890 kJ → n = 1 mol → V = 22,4 L.",
      parametrlar=dict(arch="sxema_suv_isitish"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Ma'lum: S + O₂ → SO₂ + 297 kJ va 2SO₂ + O₂ → 2SO₃ + 198 kJ. 0,5 mol oltingugurtdan "
            "SO₃ olinganda jami ajraladigan issiqlikni (kJ) toping.",
      javob="198", yechim="1 mol S → SO₃: 297 + 99 = 396 kJ → 0,5 mol: 198 kJ (Gess qonuni).",
      parametrlar=dict(arch="hess_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="44,8 L (n.sh.) vodorod va metan aralashmasi yondirilganda 1176 kJ issiqlik ajraldi. "
            "Aralashmadagi vodorod miqdorini (mol) toping. (H₂ — 286, CH₄ — 890 kJ/mol)",
      javob="1", yechim="x·286 + (2−x)·890 = 1176 → 1780 − 604x = 1176 → x = 1 mol (50 %).",
      parametrlar=dict(arch="aralash_teskari_zanjir")),
]

# ---------- O2 ----------
check("o41b", 6/12*393.5, 196.75)
check("o41c", 196750/(500*4.2), 93.7, tol=0.2)
check("o42c", 393.5-283, 110.5)
check("o43a", 286/2, 143); check("o43b", 890/16, 55.6, tol=0.1); check("o43c", 393.5/12, 32.8, tol=0.1)
check("o43d", 1000/143, 7, tol=0.05)
O2 = [
 dict(n=41, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Laboratoriyada kalorimetr yordamida ko'mirning yonish issiqligi tekshirilmoqda: "
            "C + O₂ → CO₂ + 393,5 kJ. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) 6 g ko'mir to'liq yonganda ajraladigan issiqlikni hisoblang.",
             yechim=["n = 6/12 = 0,5 mol → Q = 0,5·393,5 = 196,75 kJ."], M=4, A=2),
        dict(savol="b) Shu issiqlik kalorimetrdagi 500 g suvga yo'qotishsiz o'tsa, suv harorati "
                   "necha gradusga ko'tariladi? (c = 4,2 J/(g·°C))",
             yechim=["Δt = 196750/(500·4,2) ≈ 93,7 °C."], M=5, A=3),
        dict(savol="c) Tajribada harorat faqat 75 °C ga ko'tarildi. Foydali ish koeffitsiyentini "
                   "(issiqlikning suvga o'tgan ulushini, %) baholang.",
             yechim=["η = 75/93,7 · 100 ≈ 80 %."], M=3, A=3),
        dict(savol="d) Qolgan issiqlik qayerga ketganini izohlang.",
             yechim=["Kalorimetr devorlari, atrof havo isishi, chala yonish yo'qotishlari."], M=3, A=2),
      ],
      rasmiylashtirish="Kalorimetr zanjiri: hisob → Δt → FIK → tahlil; M15+A10.",
      parametrlar=dict(arch="kalorimetr_zanjir")),
 dict(n=42, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uglerodning CO gacha yonish issiqligini bevosita o'lchab bo'lmaydi. Ma'lum: "
            "C + O₂ → CO₂ + 393,5 kJ va CO + ½O₂ → CO₂ + 283 kJ. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Gess qonunidan foydalanib, C + ½O₂ → CO reaksiyasining issiqlik effektini "
                   "keltirib chiqarish yo'lini bosqichma-bosqich yozing.",
             yechim=["C → CO₂ yo'li ikki bosqichga ajratiladi: C → CO → CO₂.",
                     "393,5 = Q(C→CO) + 283 → Q(C→CO) = 393,5 − 283 = 110,5 kJ."], M=13, A=0),
        dict(savol="b) Nega bu effektni tajribada BEVOSITA o'lchash qiyin?",
             yechim=["Uglerod yonganda doim CO bilan birga CO₂ ham hosil bo'ladi —",
                     "«sof» C → CO jarayonini ajratib bo'lmaydi."], M=9, A=0),
        dict(savol="c) Topilgan qiymat asosida 2 mol CO hosil bo'lishidagi issiqlikni yozing.",
             yechim=["2 · 110,5 = 221 kJ."], M=3, A=0),
      ],
      rasmiylashtirish="Gess-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="hess_mulohaza")),
 dict(n=43, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Uch yoqilg'i taqqoslanadi:\n"
            "[JADVAL] Yoqilg'i | M, g/mol | Q, kJ/mol ;; H₂ | 2 | 286 ;; CH₄ | 16 | 890 ;; C (ko'mir) | 12 | 393,5\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir yoqilg'ining 1 GRAMM uchun yonish issiqligini hisoblang.",
             yechim=["H₂: 286/2 = 143; CH₄: 890/16 ≈ 55,6; C: 393,5/12 ≈ 32,8 kJ/g."], M=5, A=3),
        dict(savol="b) Massa birligi hisobida qaysi yoqilg'i eng samarali? Diagramma bilan solishtiring.",
             yechim=["Vodorod — 143 kJ/g: qolganlaridan 2,5–4 baravar yuqori."], M=3, A=2),
        dict(savol="c) 1000 kJ issiqlik olish uchun har bir yoqilg'idan necha gramm kerakligini toping.",
             yechim=["H₂: 1000/143 ≈ 7 g; CH₄: ≈ 18 g; C: ≈ 30,5 g."], M=4, A=3),
        dict(savol="d) Yonish mahsulotlari jihatidan qaysi yoqilg'i ekologik toza? Izohlang.",
             yechim=["H₂ — mahsuloti faqat suv; CH₄ va C esa CO₂ (issiqxona gazi) chiqaradi."], M=3, A=2),
      ],
      rasmiylashtirish="Yoqilg'i-taqqoslash: solishtirma issiqlik → samaradorlik → ekologiya; M15+A10.",
      parametrlar=dict(arch="yoqilgi_taqqos_o2"), fig="bar_fuel"),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260307)
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
    d = dict(n=n, tur="Y1", element="I.3", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I3-B", daraja="B", bob=3, bob_nomi="Kimyoviy reaksiya turlari va issiqlik effekti",
    manba=("Tongotarov variantlari arxetiplari (termokimyoviy hisoblar, 1-2-3 tanlovlar, teskari "
           "masalalar) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS spetsifikatsiyasi I.3"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: Gess qonuni, kalorimetr, aralashma va teskari "
          "masalalar, energiya diagrammasi."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
