# -*- coding: utf-8 -*-
"""3-bob A-varianti: Kimyoviy reaksiya turlari va issiqlik effekti (I.3) — O'RGATUVCHI ★★.
Hayotiy sahnalar: sham, muzlatuvchi paket, qo'l isitgich, non-soda."""
import json, random

OUT = "mavzu_I3A.json"
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

# 1 (2)
q(2, "quyi",
  "Kimyoviy reaksiyaning asosiy belgisi nima?",
  "yangi modda hosil bo'lishi",
  [("moddaning maydalanishi", "maydalanish — fizik hodisa"),
   ("agregat holat o'zgarishi", "erish/qaynash — fizik hodisa"),
   ("harakat tezligining o'zgarishi", "mexanik hodisa")],
  "Reaksiyada moddalar tarkibi o'zgarib, YANGI xossali moddalar hosil bo'ladi.",
  dict(arch="belgi_oddiy"))

# 2 (2)
q(2, "quyi",
  "Birikish reaksiyasi deb qanday reaksiyaga aytiladi?",
  "ikki yoki bir necha moddadan BITTA modda hosil bo'lishiga",
  [("bitta moddadan bir nechta modda hosil bo'lishiga", "bu parchalanish"),
   ("moddalar o'z qismlarini almashishiga", "bu almashinish"),
   ("oddiy modda murakkab moddadan atomni siqib chiqarishiga", "bu o'rin olish")],
  "A + B → AB ko'rinishi: masalan, 2Mg + O₂ → 2MgO.",
  dict(arch="birikish_tarif"))

# 3 (2)
q(2, "o'rta",
  "2H₂O → 2H₂ + O₂ reaksiyasi qaysi turga kiradi?",
  "parchalanish", [("birikish", "bitta moddadan IKKITA hosil bo'ldi"),
                    ("o'rin olish", "oddiy modda reaksiyaga kirmagan"),
                    ("almashinish", "ikki murakkab modda yo'q")],
  "AB → A + B: bitta murakkab moddadan ikkita oddiy modda.",
  dict(arch="parchalanish_misol"))

# 4 (2) — SAHNA: sham
q(2, "o'rta",
  "Rasmga qarang: yonayotgan sham xonani yoritadi va isitadi. Sham yonishi qanday reaksiya?",
  "ekzotermik — issiqlik va yorug'lik ajraladi",
  [("endotermik — issiqlik yutiladi", "sham atrofni ISITADI, sovutmaydi"),
   ("fizik hodisa", "parafin kislorod bilan reaksiyaga kirishib CO₂ va suv beradi"),
   ("faqat erish jarayoni", "erish ham bor, lekin yonish — kimyoviy jarayon")],
  "Yonish — deyarli har doim ekzotermik: energiya issiqlik va yorug'lik ko'rinishida chiqadi.",
  dict(arch="sham_sahna"), fig="candle")

# 5 (2)
q(2, "o'rta",
  "Zn + CuSO₄ → ZnSO₄ + Cu reaksiyasi qaysi turga kiradi?",
  "o'rin olish", [("almashinish", "oddiy modda (Zn) qatnashyapti"),
                   ("birikish", "mahsulot bitta emas"),
                   ("parchalanish", "moddalar soni kamaymadi")],
  "Oddiy modda (Zn) murakkab modda tarkibidagi Cu ni siqib chiqardi.",
  dict(arch="orin_misol"))

# 6 (2)
q(2, "o'rta",
  "AgNO₃ + NaCl → AgCl↓ + NaNO₃ reaksiyasi qaysi turga kiradi?",
  "almashinish", [("o'rin olish", "oddiy modda qatnashmayapti"),
                   ("birikish", "ikki modda ikkita mahsulot berdi"),
                   ("parchalanish", "moddalar parchalanmadi")],
  "Ikki murakkab modda o'z tarkibiy qismlarini almashdi: AB + CD → AD + CB.",
  dict(arch="almashinish_misol"))

# 7 (2)
q(2, "quyi",
  "Ekzotermik reaksiya deb qanday reaksiyaga aytiladi?",
  "issiqlik AJRALIB chiqishi bilan boradigan reaksiyaga",
  [("issiqlik yutilishi bilan boradigan", "bu endotermik"),
   ("faqat yorug'likda boradigan", "yorug'lik sharti boshqa tushuncha"),
   ("katalizator ishtirokida boradigan", "katalitik reaksiya boshqa belgi")],
  "Ekzo — «tashqariga»: energiya sistemadan chiqadi (+Q).",
  dict(arch="ekzo_tarif"))

# 8 (2) — SAHNA: muzlatuvchi paket
q(2, "o'rta",
  "Rasmda sport jarohatiga qo'yiladigan «muzlatuvchi paket»: ichidagi ammiakli selitra suvda "
  "eriganda paket keskin SOVIYDI. Bu qanday jarayon?",
  "endotermik — erish issiqlik yutadi",
  [("ekzotermik — issiqlik ajraladi", "paket sovuqni beradi, issiqni emas"),
   ("yonish reaksiyasi", "hech narsa yonmayapti"),
   ("muzlash jarayoni", "suv muzlamaydi — issiqlik eritmaga yutiladi")],
  "NH₄NO₃ erishi issiqlikni atrofdan (jarohat joyidan) yutadi — paket soviydi.",
  dict(arch="coldpack_sahna"), fig="coldpack")

# 9 (2)
q(2, "o'rta",
  "Termokimyoviy tenglamada «+Q» belgisi nimani bildiradi?",
  "reaksiyada issiqlik ajralishini (ekzotermik)",
  [("issiqlik yutilishini", "yutilish «−Q» bilan yoziladi"),
   ("bosim ortishini", "Q — issiqlik, bosim emas"),
   ("reaksiya tezligini", "tezlik boshqa kattalik")],
  "A + B → C + Q — issiqlik mahsulotlar tomonida: ajralib chiqadi.",
  dict(arch="plusq_belgi"))

# 10 (3)
check("q10", 890*2, 1780)
q(3, "o'rta",
  "CH₄ + 2O₂ → CO₂ + 2H₂O + 890 kJ. 2 mol metan yonganda qancha issiqlik ajraladi?",
  "1780 kJ", [("890 kJ", "bu 1 mol uchun"), ("445 kJ", "ikkiga bo'lib yuborilgan"),
               ("3560 kJ", "to'rt baravar — xato")],
  "Q = 2 · 890 = 1780 kJ — issiqlik mol soniga proporsional.",
  dict(arch="metan_q_hisob"))

# 11 (2)
q(2, "o'rta",
  "Quyidagi jarayonlardan qaysi biri ENDOTERMIK?",
  "ohaktoshning parchalanishi (CaCO₃ → CaO + CO₂)",
  [("ko'mirning yonishi", "yonish — ekzotermik"),
   ("kislota va ishqor neytrallanishi", "neytrallanish issiqlik beradi"),
   ("temirning zanglashi", "sekin oksidlanish ham ekzotermik")],
  "Ohaktoshni parchalash uchun uzluksiz qizdirish kerak — issiqlik YUTILADI.",
  dict(arch="endo_misol"))

# 12 (3)
check("q12", 393*0.5, 196.5)
q(3, "o'rta",
  "C + O₂ → CO₂ + 393 kJ. 6 g uglerod yonganda qancha issiqlik ajraladi? (M(C)=12)",
  "196,5 kJ", [("393 kJ", "bu 12 g (1 mol) uchun"), ("786 kJ", "ikki baravar — xato"),
                ("98 kJ", "chorak olingan")],
  "n = 6/12 = 0,5 mol → Q = 0,5 · 393 = 196,5 kJ.",
  dict(arch="uglerod_q"))

# 13 (2) — SAHNA: qo'l isitgich
q(2, "o'rta",
  "Rasmda qishki «qo'l isitgich» xaltachasi: ichidagi temir kukuni havo kislorodi bilan sekin "
  "reaksiyaga kirishib, xaltacha bir necha soat iliq turadi. Bunda qanday jarayon boradi?",
  "temirning sekin oksidlanishi — ekzotermik reaksiya",
  [("temirning erishi", "temir erimaydi — kimyoviy o'zgaradi"),
   ("endotermik parchalanish", "issiqlik AJRALYAPTI, yutilmayapti"),
   ("fizik ishqalanish issiqligi", "ishqalanmasdan ham isiydi — reaksiya manbai")],
  "4Fe + 3O₂ → 2Fe₂O₃ + Q: zanglashning tezlashtirilgan varianti — issiqlik manbai.",
  dict(arch="handwarmer_sahna"), fig="handwarmer")

# 14 (3)
check("q14", 572/2, 286)
q(3, "o'rta",
  "2H₂ + O₂ → 2H₂O + 572 kJ. 1 mol vodorod yonganda qancha issiqlik ajraladi?",
  "286 kJ", [("572 kJ", "bu 2 mol H₂ uchun"), ("1144 kJ", "ikki baravar ko'p"),
              ("143 kJ", "yana ikkiga bo'lingan")],
  "Q = 572/2 = 286 kJ (tenglamada 2 mol H₂ bor).",
  dict(arch="h2_q"))

# 15 (2)
q(2, "o'rta",
  "Qaysi tenglama BIRIKISH reaksiyasiga misol bo'ladi?",
  "S + O₂ → SO₂",
  [("2HgO → 2Hg + O₂", "parchalanish"), ("Fe + CuCl₂ → FeCl₂ + Cu", "o'rin olish"),
   ("HCl + NaOH → NaCl + H₂O", "almashinish")],
  "Ikki moddadan bitta mahsulot: birikish.",
  dict(arch="birikish_tanlov"))

# 16 (2)
q(2, "o'rta",
  "Kislota bilan ishqor orasidagi neytrallanish reaksiyasi qaysi turga kiradi?",
  "almashinish", [("birikish", "ikkita mahsulot (tuz va suv) hosil bo'ladi"),
                   ("parchalanish", "moddalar parchalanmaydi"),
                   ("o'rin olish", "oddiy modda qatnashmaydi")],
  "HCl + NaOH → NaCl + H₂O: ion qismlar almashinadi (va issiqlik ajraladi).",
  dict(arch="neytrallanish_tur"))

# 17 (2)
q(2, "o'rta",
  "Jadvaldagi «?» kataklarni mos ravishda to'ldiring:\n"
  "[JADVAL] Reaksiya | Turi ;; 2Mg + O₂ → 2MgO | ? ;; CaCO₃ → CaO + CO₂ | ?",
  "birikish; parchalanish",
  [("parchalanish; birikish", "tartib teskari"), ("birikish; almashinish", "CaCO₃ bitta moddaga ajraldi"),
   ("o'rin olish; parchalanish", "MgO ikki moddadan hosil bo'ldi")],
  "Mg + O₂ → bitta mahsulot (birikish); CaCO₃ → ikki mahsulot (parchalanish).",
  dict(arch="tur_jadval"))

# 18 (2) — SAHNA: non-soda
q(2, "o'rta",
  "Rasmda novvoyxona: xamirga qo'shilgan ichimlik sodasi qizdirilganda 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂↑ "
  "reaksiyasi boradi. Xamirni nima «ko'pchitadi» va bu qaysi tur reaksiya?",
  "ajralgan CO₂ gazi; parchalanish",
  [("suv bug'i; birikish", "asosiy ko'pchitgich — CO₂; tur ham noto'g'ri"),
   ("Na₂CO₃; almashinish", "tuz qattiq qoladi, gaz emas"),
   ("kislorod; o'rin olish", "reaksiyada O₂ ajralmaydi")],
  "Qizdirishda soda parchalanadi, CO₂ pufakchalari xamirni g'ovak qiladi.",
  dict(arch="soda_sahna"), fig="bread")

# 19 (3)
check("q19", 4/2*286, 572)
q(3, "o'rta",
  "2H₂ + O₂ → 2H₂O + 572 kJ. 4 g vodorod yonganda qancha issiqlik ajraladi? (M(H₂)=2)",
  "572 kJ", [("286 kJ", "bu 1 mol (2 g) uchun"), ("1144 kJ", "4 mol deb olingan"),
              ("143 kJ", "asossiz bo'lish")],
  "n = 4/2 = 2 mol H₂ → aynan tenglamadagi miqdor: 572 kJ.",
  dict(arch="h2_massa_q"))

# 20 (2)
q(2, "quyi",
  "Reaksiyaning issiqlik effekti (Q) qaysi birlikda o'lchanadi?",
  "kJ (kilojoul)", [("g (gramm)", "massa birligi"), ("mol", "modda miqdori birligi"),
                     ("°C (gradus)", "harorat birligi — issiqlik miqdori emas")],
  "Issiqlik — energiya turi: J, kJ (ko'pincha kJ/mol).",
  dict(arch="q_birlik"))

# 21 (3)
check("q21", 180/2, 90)
q(3, "o'rta",
  "N₂ + O₂ → 2NO − 180 kJ. Bu reaksiya haqida qaysi fikr TO'G'RI?",
  "endotermik: 1 mol NO hosil bo'lishida 90 kJ yutiladi",
  [("ekzotermik: 180 kJ ajraladi", "«−» ishorasi yutilishni bildiradi"),
   ("endotermik: 1 mol NO uchun 180 kJ yutiladi", "180 kJ — 2 mol NO uchun"),
   ("issiqlik effekti yo'q", "Q = −180 kJ ko'rsatilgan")],
  "«−Q» — yutilish; 180/2 = 90 kJ har mol NO uchun. Shu bois NO faqat yuqori haroratda hosil bo'ladi.",
  dict(arch="no_endo"))

# 22 (2)
q(2, "o'rta",
  "Yonish reaksiyalari haqida qaysi fikr to'g'ri?",
  "deyarli barchasi ekzotermik",
  [("barchasi endotermik", "yonish issiqlik BERADI"),
   ("issiqlik effekti bo'lmaydi", "gulxan yonida buni his qilish oson"),
   ("faqat metallar yonishi issiqlik beradi", "metan, ko'mir ham issiqlik beradi")],
  "Yonish — yoqilg'idan energiya olishning asosiy usuli: doim +Q.",
  dict(arch="yonish_ekzo"))

# 23 (3)
check("q23", 0.2*3/2, 0.3)
q(3, "o'rta",
  "2KClO₃ → 2KCl + 3O₂. 0,2 mol bertole tuzi parchalanganda necha mol kislorod ajraladi?",
  "0,3", [("0,2", "nisbat 2:3 — teng emas"), ("0,6", "uch baravar emas, 1,5 baravar"),
           ("0,1", "nisbat teskari olingan")],
  "n(O₂) = 0,2 · 3/2 = 0,3 mol.",
  dict(arch="kclo3_mol"))

# 24 (2) — RASMLI: energiya diagrammasi
q(2, "o'rta",
  "Rasmdagi energiya diagrammasida mahsulotlarning energiyasi boshlang'ich moddalarnikidan PAST. "
  "Bu qanday reaksiya?",
  "ekzotermik — energiya farqi issiqlik sifatida ajraladi",
  [("endotermik — issiqlik yutiladi", "yutilishda mahsulot energiyasi YUQORI bo'lardi"),
   ("issiqlik effektsiz", "sathlar farqi aynan issiqlik effekti"),
   ("fizik jarayon", "diagramma kimyoviy reaksiya uchun")],
  "Sistema pastroq energiyaga tushdi — ortiqcha energiya issiqlik bo'lib chiqdi.",
  dict(arch="profil_oqish_oddiy"), fig="profile")

# 25 (3)
q(3, "o'rta",
  "Temir mixni mis(II) sulfat eritmasiga tushirsak, mix qizil g'ubor bilan qoplanadi. "
  "Bu qaysi tur reaksiya va g'ubor nima?",
  "o'rin olish; metall mis",
  [("almashinish; mis oksidi", "oddiy modda (Fe) qatnashyapti; g'ubor — Cu"),
   ("birikish; zang", "zang emas — mis ajralyapti"),
   ("parchalanish; mis sulfidi", "hech narsa parchalanmayapti")],
  "Fe + CuSO₄ → FeSO₄ + Cu: faolroq temir misni siqib chiqaradi.",
  dict(arch="fe_cuso4"))

# 26 (3) — RASMLI: yonish issiqliklari ustunlari
q(3, "o'rta",
  "Diagrammada uch gazning 1 mol uchun yonish issiqliklari berilgan. Qaysi gaz 1 MOL hisobida "
  "eng ko'p issiqlik beradi?",
  "propan (C₃H₈)", [("metan (CH₄)", "890 kJ — eng past ustun"),
                     ("etan (C₂H₆)", "1560 kJ — o'rtada"),
                     ("hammasi teng", "ustunlar balandligi har xil")],
  "Diagrammadan: C₃H₈ ≈ 2220 kJ/mol — molekulada atomlar ko'p, yonish issiqligi katta.",
  dict(arch="bar_yonish_oqish"), fig="bar_yonish")

# 27 (3)
check("q27", 148.5/0.5, 297)
q(3, "o'rta",
  "0,5 mol oltingugurt yonganda 148,5 kJ issiqlik ajraldi. 1 mol uchun issiqlik effektini toping.",
  "297 kJ", [("148,5 kJ", "bu 0,5 mol uchun"), ("74 kJ", "yana ikkiga bo'lingan"),
              ("594 kJ", "to'rt baravar — xato")],
  "Q = 148,5/0,5 = 297 kJ/mol: S + O₂ → SO₂ + 297 kJ.",
  dict(arch="s_teskari_oddiy"))

# 28 (2)
q(2, "o'rta",
  "Fotosintez jarayoni (6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂) qanday reaksiya?",
  "endotermik — quyosh energiyasi yutiladi",
  [("ekzotermik — issiqlik ajraladi", "aksincha: yorug'liksiz bormaydi"),
   ("issiqlik effektsiz", "energiya glyukozada «saqlanadi»"),
   ("fizik jarayon", "yangi modda (glyukoza) hosil bo'ladi")],
  "O'simlik yorug'lik energiyasini yutib, uni glyukozaning kimyoviy energiyasiga aylantiradi.",
  dict(arch="fotosintez"))

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Metan yonishida ajraladigan issiqlik yoqilgan metan MASSASIGA qanday bog'liq? Grafikni tanlang.",
  "to'g'ri proporsional ortadi",
  [("o'zgarmaydi", "har mol metan o'z 890 kJ ini beradi"),
   ("kamayadi", "ko'proq yoqilg'i — ko'proq issiqlik"),
   ("avval ortib, keyin to'xtaydi", "kislorod yetarli bo'lsa chegara yo'q")],
  "Q = n · 890 = (m/16) · 890 — massaga chiziqli bog'liq.",
  svg=dict(correct="rise", d1="flat", d2="fall", d3="rise_flat", xlab="m(CH₄)", ylab="Q"),
  params=dict(arch="q_massa_grafik"))

# 30 (2)
q(2, "o'rta",
  "Quyidagilardan qaysi biri FIZIK hodisa?",
  "muzning erishi",
  [("gugurtning yonishi", "yangi moddalar (CO₂, kul) hosil bo'ladi"),
   ("sutning achishi", "yangi modda — sut kislotasi"),
   ("temirning zanglashi", "yangi modda — zang (Fe₂O₃)")],
  "Muz erishida modda o'zgarmaydi: H₂O qattiqdan suyuqqa o'tadi, xolos.",
  dict(arch="fizik_hodisa"))

# 31 (3)
check("q31", 4450/890, 5)
q(3, "o'rta",
  "Qozonxonaga 4450 kJ issiqlik kerak. Buning uchun necha mol metan yoqish lozim? (Q = 890 kJ/mol)",
  "5", [("4450", "molga aylantirilmagan"), ("0,2", "nisbat teskari olingan"),
         ("10", "ikki baravar ko'p")],
  "n = 4450/890 = 5 mol (≈ 112 L gaz).",
  dict(arch="metan_teskari_mol"))

# 32 (3) — RASMLI: diagramma strelkasi
q(3, "o'rta",
  "24-savoldagi diagrammada reaksiyaning issiqlik effektiga qaysi kesma mos keladi?",
  "boshlang'ich va mahsulot sathlari orasidagi farq",
  [("egri chiziqning eng yuqori nuqtasi", "bu — aktivlanish energiyasi cho'qqisi"),
   ("boshlang'ich sath bilan cho'qqi orasidagi farq", "bu — aktivlanish energiyasi"),
   ("vaqt o'qi uzunligi", "issiqlik o'qlar farqidan o'qiladi")],
  "Q = E(boshlang'ich) − E(mahsulot): sathlar orasidagi vertikal farq.",
  dict(arch="profil_strelka"), fig="profile")

# ---------- Y2: oshxona ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.3",
  ichki_pasport=[dict(n=33, element="I.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Oshxonada uch jarayon kuzatildi: X — gaz plitada metan yonmoqda; Y — muzlatgichda suv "
               "muzga aylanmoqda; Z — xamirdagi soda qizdirilganda parchalanib, gaz ajratmoqda. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X jarayon qanday reaksiya?",
    "34. Y jarayonning tabiati qanday?",
    "35. Z jarayonda ajralayotgan gaz qaysi?"],
  javoblar_royxati=["A) ekzotermik yonish", "B) fizik hodisa", "C) CO₂",
                    "D) endotermik parchalanish", "E) O₂", "F) kimyoviy almashinish"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="D — Z jarayonga mos tavsif, X ga emas"),
                   dict(variant="E", xato="soda parchalanishida kislorod ajralmaydi"),
                   dict(variant="F", xato="muzlash — kimyoviy emas, agregat holat o'zgarishi")],
  yechim=("X: CH₄ yonishi — ekzotermik (A). Y: muzlash — fizik hodisa (B). "
          "Z: 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂↑ — gaz CO₂ (C)."),
  parametrlar=dict(arch="oshxona_ssenariy"))

# ---------- O1 ----------
check("o36", 12/12*393, 393)
check("o37", 2*286, 572)
check("o38", 0.25*890, 222.5)
check("o39", 0.6*2/3, 0.4)
check("o40", 286/2, 143)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="C + O₂ → CO₂ + 393 kJ. 12 g ko'mir yonganda ajraladigan issiqlikni (kJ) toping.",
      javob="393", yechim="n = 12/12 = 1 mol → 393 kJ.",
      parametrlar=dict(arch="komir_q_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Suvni parchalash uchun 1 mol H₂O ga 286 kJ energiya kerak. 2 mol suvni parchalashga "
            "qancha energiya (kJ) sarflanadi?",
      javob="572", yechim="Q = 2 · 286 = 572 kJ (endotermik jarayon).",
      parametrlar=dict(arch="suv_parchalash_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="CH₄ + 2O₂ → CO₂ + 2H₂O + 890 kJ. 0,25 mol metan yonganda ajraladigan issiqlikni (kJ) toping.",
      javob="222,5", yechim="Q = 0,25 · 890 = 222,5 kJ.",
      parametrlar=dict(arch="metan_q_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="2KClO₃ → 2KCl + 3O₂. 0,6 mol kislorod olish uchun necha mol KClO₃ kerak?",
      javob="0,4", yechim="n = 0,6 · 2/3 = 0,4 mol.",
      parametrlar=dict(arch="kclo3_teskari_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="2H₂ + O₂ → 2H₂O + 572 kJ. 1 g vodorod yonganda ajraladigan issiqlikni (kJ) toping.",
      javob="143", yechim="1 g = 0,5 mol H₂ → Q = 0,5 · 286 = 143 kJ.",
      parametrlar=dict(arch="h2_gramm_o1")),
]

# ---------- O2 ----------
check("o41b", 6/12*393, 196.5)
check("o41c", 196500/(500*4.2), 93.6, tol=0.2)
O2 = [
 dict(n=41, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Mang'alda ko'mir yoqilmoqda: C + O₂ → CO₂ + 393 kJ. Bandlar ketma-ket yechiladi — "
            "har biri keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) Bu reaksiyaning turini va issiqlik effekti belgisini aniqlang.",
             yechim=["Birikish reaksiyasi; +Q — ekzotermik."], M=3, A=2),
        dict(savol="b) 6 g ko'mir yonganda ajraladigan issiqlikni hisoblang.",
             yechim=["n = 6/12 = 0,5 mol → Q = 0,5·393 = 196,5 kJ."], M=4, A=2),
        dict(savol="c) Shu issiqlik 500 g suvni necha gradusga isitishi mumkin? (c = 4,2 J/(g·°C))",
             yechim=["Δt = 196500/(500·4,2) ≈ 94 °C."], M=4, A=3),
        dict(savol="d) Amalda suv bunchalik isimaydi. Sababini izohlang.",
             yechim=["Issiqlikning katta qismi havoga, idishga tarqaladi — yo'qotishlar bor."], M=4, A=3),
      ],
      rasmiylashtirish="O'rgatuvchi yonish-zanjiri: tur → hisob → amaliy baho; M15+A10.",
      parametrlar=dict(arch="komir_zanjir")),
 dict(n=42, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Alpinistlar sovuqda «qo'l isitgich» (temir kukunli xaltacha) va sport shifokorlari "
            "«muzlatuvchi paket» (ammiakli selitrali xaltacha) ishlatadi. Quyidagilarga MULOHAZA "
            "yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Ikki xaltachaning ishlash tamoyilini issiqlik effekti tushunchasi asosida "
                   "solishtirib tushuntiring.",
             yechim=["Isitgich: 4Fe + 3O₂ → 2Fe₂O₃ + Q — ekzotermik oksidlanish, issiqlik ajraladi.",
                     "Muzlatgich: NH₄NO₃ ning suvda erishi endotermik — issiqlik atrofdan yutiladi."], M=13, A=0),
        dict(savol="b) Nega isitgich xaltachasi ochilmaguncha «ishlamaydi»?",
             yechim=["Germetik xaltada kislorod yo'q; ochilgach havo O₂ si kirib, oksidlanish boshlanadi."], M=9, A=0),
        dict(savol="c) Har bir xaltachadagi jarayon uchun issiqlik effekti belgisini (+Q/−Q) yozing.",
             yechim=["Isitgich: +Q; muzlatuvchi paket: −Q."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="xaltacha_mulohaza")),
 dict(n=43, tur="O2", element="I.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("To'rt reaksiya jadvalda berilgan:\n"
            "[JADVAL] № | Reaksiya ;; 1 | 2Al + 3S → Al₂S₃ ;; 2 | 2HgO → 2Hg + O₂ ;; "
            "3 | Mg + 2HCl → MgCl₂ + H₂ ;; 4 | BaCl₂ + Na₂SO₄ → BaSO₄ + 2NaCl\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir reaksiyaning turini aniqlang.",
             yechim=["1 — birikish; 2 — parchalanish; 3 — o'rin olish; 4 — almashinish."], M=5, A=3),
        dict(savol="b) Qaysi reaksiyalarda oddiy modda ISHTIROK ETADI (reagent sifatida)?",
             yechim=["1 (Al, S) va 3 (Mg)."], M=3, A=2),
        dict(savol="c) Qaysi reaksiyada gaz, qaysinisida cho'kma hosil bo'ladi?",
             yechim=["Gaz: 2 (O₂) va 3 (H₂); cho'kma: 4 (BaSO₄↓)."], M=4, A=3),
        dict(savol="d) 2-reaksiya qizdirishni talab qiladi. Uning issiqlik effekti belgisini asoslang.",
             yechim=["Endotermik (−Q): uzluksiz issiqlik berilmasa parchalanish to'xtaydi."], M=3, A=2),
      ],
      rasmiylashtirish="Reaksiya-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="reaksiya_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260305)
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
assert sum(b["A"] for b in O2[1]["bandlar"]) == 0
print("O2 ballari: OK")

variant = dict(
    variant="mavzu-I3-A", daraja="A", bob=3, bob_nomi="Kimyoviy reaksiya turlari va issiqlik effekti",
    manba=("MS spetsifikatsiyasi I.3; darslik reaksiya turlari va termokimyo bo'limlari — savollar "
           "yangi tuzilgan, hayotiy sahnalar (sham, muzlatuvchi paket, qo'l isitgich, non-soda) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
