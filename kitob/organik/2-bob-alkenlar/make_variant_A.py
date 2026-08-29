# -*- coding: utf-8 -*-
"""Organik 2-bob A-varianti: Alkenlar, alkadiyenlar, alkinlar (III.2) — O'RGATUVCHI ★★.
Hayotiy sahnalar: pishgan mevalar (etilen), payvandlash, polietilen paket, avtomobil shinasi."""
import json, random

OUT = "mavzu_III2A.json"
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
  "Alkenlarning umumiy formulasi qaysi?",
  "CₙH₂ₙ", [("CₙH₂ₙ₊₂", "bu alkanlar"), ("CₙH₂ₙ₋₂", "bu alkinlar/alkadiyenlar"),
             ("CₙH₂ₙ₊₁", "bu radikal")],
  "Bitta qo'shbog' ikki vodorodni «yeydi»: eten C₂H₄, propen C₃H₆.",
  dict(arch="alken_formula"))

# 2 (2)
q(2, "quyi",
  "Alkenlar molekulasidagi o'ziga xos bog' qanday?",
  "bitta C=C qo'shbog'",
  [("faqat yakka bog'lar", "u alkanlarda"), ("uchbog'", "u alkinlarda"),
   ("ion bog'", "organikada kovalent")],
  "Qo'shbog' = sigma + pi: pi-bog' bo'shroq — reaksiyalar «eshigi».",
  dict(arch="qoshbog"))

# 3 (2)
q(2, "o'rta",
  "Eng sodda alken qaysi?",
  "etilen (C₂H₄)", [("metilen", "erkin holda barqaror emas"), ("propen", "u ikkinchi vakil"),
                     ("atsetilen", "u alkin")],
  "CH₂=CH₂ — dunyoda eng ko'p ishlab chiqariladigan organik modda.",
  dict(arch="etilen"))

# 4 (2) — SAHNA: pishgan mevalar
q(2, "o'rta",
  "Rasmda banan va pomidorlar birga qo'yilgan: bananlar tezroq pishyapti. Buning «aybdori» qaysi "
  "gaz?",
  "etilen — mevalarning tabiiy pishish gormoni",
  [("metan", "pishishga ta'siri yo'q"), ("karbonat angidrid", "CO₂ pishirmaydi"),
   ("ammiak", "u meva gazi emas")],
  "Pishgan meva C₂H₄ ajratadi — u qo'shnilarini ham «uyg'otadi». Omborlarda etilen nazorat qilinadi.",
  dict(arch="meva_sahna"), fig="fruits")

# 5 (2)
q(2, "o'rta",
  "Alkenlar nomlarida qaysi qo'shimcha ishlatiladi?",
  "-en", [("-an", "alkanlarda"), ("-in", "alkinlarda"), ("-ol", "spirtlarda")],
  "Etan → eten; propan → propen: qo'shbog' «-en» bilan belgilanadi.",
  dict(arch="en_qoshimcha"))

# 6 (2)
q(2, "o'rta",
  "To'yinmagan uglevodorodni aniqlashning eng oddiy sinovi qaysi?",
  "bromli suvni rangsizlantirishi",
  [("lakmusni qizartirishi", "uglevodorod kislota emas"),
   ("alanga rangi", "alanga sinfni aniq ko'rsatmaydi"),
   ("hidi", "hid ishonchli belgi emas")],
  "Qo'shbog' Br₂ ni biriktiradi: sariq rang yo'qoladi — «to'yinmaganlik testi».",
  dict(arch="brom_test"))

# 7 (2)
q(2, "o'rta",
  "Alkinlarning umumiy formulasi qaysi?",
  "CₙH₂ₙ₋₂", [("CₙH₂ₙ", "alkenlar"), ("CₙH₂ₙ₊₂", "alkanlar"), ("CₙHₙ", "maxsus holat")],
  "Uchbog' to'rt vodorod «yeydi»: atsetilen C₂H₂.",
  dict(arch="alkin_formula"))

# 8 (2) — SAHNA: payvandlash
q(2, "o'rta",
  "Rasmda gaz payvandlash: ishchi po'latni atsetilen alangasi bilan kesyapti. Nega aynan atsetilen?",
  "kislorodda yonganda ~3000 °C harorat beradi",
  [("u eng arzon gaz", "asosiy sabab — alanga harorati"),
   ("u xavfsiz gaz", "aksincha, ehtiyotkorlik talab qiladi"),
   ("alanga rangi chiroyli", "rang emas, harorat muhim")],
  "2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O + Q: kislorod-atsetilen alangasi metallni eritadi.",
  dict(arch="payvand_sahna"), fig="welding")

# 9 (2)
q(2, "o'rta",
  "Atsetilen laboratoriya va texnikada qanday olinadi?",
  "kalsiy karbidga suv ta'sir ettirib",
  [("ohaktoshni kuydirib", "u CO₂ beradi"), ("metanni suvda eritib", "erish reaksiya emas"),
   ("rux va kislotadan", "u H₂ beradi")],
  "CaC₂ + 2H₂O → C₂H₂↑ + Ca(OH)₂ — «karbid» usuli.",
  dict(arch="karbid_usul"))

# 10 (3)
check("q10", 5.6/28*2*22.4, 8.96)
q(3, "o'rta",
  "C₂H₄ + 3O₂ → 2CO₂ + 2H₂O. 5,6 g etilen yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(M(C₂H₄)=28)",
  "8,96 L", [("4,48 L", "koeffitsiyent 2"), ("22,4 L", "1 mol uchun"), ("2,24 L", "hisob xato")],
  "n = 0,2 mol → n(CO₂) = 0,4 → V = 8,96 L.",
  dict(arch="etilen_yonish_hisob"))

# 11 (2)
q(2, "o'rta",
  "POLIMERLANISH reaksiyasi nima?",
  "ko'p mayda molekulalarning yirik zanjirga birlashishi",
  [("molekulaning parchalanishi", "aksincha — birikish"),
   ("suv ajralib chiqishi bilan borish", "u polikondensatsiya"),
   ("yonish turi", "yonishga aloqasi yo'q")],
  "nCH₂=CH₂ → (–CH₂–CH₂–)ₙ: qo'shbog'lar ochilib zanjir «tikiladi».",
  dict(arch="polimerlanish_tarif"))

# 12 (3)
check("q12", 28, 28)
q(3, "o'rta",
  "Molyar massasi 28 g/mol bo'lgan alkenni aniqlang.",
  "eten (C₂H₄)", [("propen", "M = 42"), ("buten", "M = 56"), ("etan", "u alkan (M=30)")],
  "14n = 28 → n = 2.",
  dict(arch="m_dan_alken"))

# 13 (2) — SAHNA: polietilen paket
q(2, "o'rta",
  "Rasmda polietilen paket. U qaysi moddadan olinadi?",
  "etilenning polimerlanishidan",
  [("metandan bevosita", "metan polimerlanmaydi"),
   ("sellyulozadan", "u qog'oz asosi"),
   ("kauchukdan", "kauchuk — dien polimeri")],
  "PE — eng ko'p ishlab chiqariladigan plastik: paketlar, quvurlar, plyonkalar.",
  dict(arch="paket_sahna"), fig="bag")

# 14 (2)
q(2, "o'rta",
  "Alkadiyenlar molekulasida nechta qo'shbog' bor?",
  "2 ta", [("1 ta", "bitta — alkenlarda"), ("3 ta", "trienlarda"), ("qo'shbog' yo'q", "diyen — «ikki en»")],
  "Butadien CH₂=CH–CH=CH₂ — kauchuk «g'ishti».",
  dict(arch="dien_tarif"))

# 15 (2)
q(2, "o'rta",
  "Tabiiy kauchukning asosi qaysi uglevodorod?",
  "izopren (2-metilbutadien-1,3)",
  [("etilen", "PE beradi, kauchuk emas"), ("atsetilen", "boshqa sinf"),
   ("benzol", "u aren")],
  "Geveya daraxti shirasi — poliizopren; sun'iy kauchuk butadiendan olinadi.",
  dict(arch="kauchuk_asos"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Modda | Formula ;; eten | ? ;; propin | ? ;; butadien-1,3 | ?",
  "C₂H₄; C₃H₄; C₄H₆",
  [("C₂H₆; C₃H₆; C₄H₈", "qo'shimchalar chalkash"), ("C₂H₄; C₃H₆; C₄H₆", "propIN — uchbog'li"),
   ("C₂H₂; C₃H₄; C₄H₆", "eten — alken")],
  "en → 2n; in → 2n−2; dien → 2n−2.",
  dict(arch="formula_jadval_2"))

# 17 (2)
q(2, "o'rta",
  "GIDROGENLASH reaksiyasida alkenga nima biriktiriladi?",
  "vodorod (H₂)", [("suv", "u gidratlanish"), ("brom", "u galogenlash"), ("kislorod", "u yonish")],
  "C₂H₄ + H₂ → C₂H₆ (katalizator) — margarin ham shu usulda «qattiqlashtiriladi».",
  dict(arch="gidrogenlash"))

# 18 (2) — SAHNA: shina
q(2, "o'rta",
  "Rasmda avtomobil shinasi. Uning asosiy materiali qanday olinadi?",
  "butadien kauchugini oltingugurt bilan vulkanizatsiya qilib",
  [("polietilendan quyib", "PE shinaga yaroqsiz — yumshoq"),
   ("sof neftdan", "neft — xomashyo, material emas"),
   ("metallni qoplab", "asos — rezina")],
  "Kauchuk + S → rezina: oltingugurt «ko'priklari» elastiklik va pishiqlik beradi.",
  dict(arch="shina_sahna"), fig="tire")

# 19 (3)
check("q19", 2.6/26*2, 0.2)
q(3, "o'rta",
  "2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O. 2,6 g atsetilen yonganda hosil bo'lgan CO₂ mol miqdorini toping. "
  "(M(C₂H₂)=26)",
  "0,2 mol", [("0,1 mol", "nisbat 2:4 = 1:2"), ("0,4 mol", "ikki baravar ko'p"), ("0,05 mol", "hisob xato")],
  "n = 0,1 → n(CO₂) = 0,2 mol.",
  dict(arch="atsetilen_hisob_a"))

# 20 (2)
q(2, "o'rta",
  "Alkenlarda izomeriya alkanlarga qaraganda qanday qo'shimcha turga ega?",
  "qo'shbog' HOLATI izomeriyasi",
  [("izotop izomeriyasi", "bunday atama yo'q"), ("hech qanday farq yo'q", "buten-1/buten-2 farqli-ku"),
   ("faqat halqa izomeriyasi", "halqa — sikloalkanlarda")],
  "Buten-1 va buten-2: qo'shbog' 1- yoki 2-holatda.",
  dict(arch="holat_izomeriya"))

# 21 (2)
q(2, "o'rta",
  "Atsetilen molekulasining tuzilishi qanday?",
  "H–C≡C–H (chiziqli)",
  [("H₂C=CH₂", "bu etilen"), ("H₃C–CH₃", "bu etan"), ("burchakli", "sp gibrid — chiziqli")],
  "Uchbog' — bitta sigma + ikkita pi; molekula «tayoqcha»day.",
  dict(arch="atsetilen_tuzilish"))

# 22 (2)
q(2, "o'rta",
  "Qaysi polimerdan suv quvurlari va oyna romlari tayyorlanadi?",
  "polivinilxlorid (PVX)",
  [("polietilen faqat", "PVX qattiqroq va olovbardosh"),
   ("kauchuk", "quvur uchun yumshoq"),
   ("shisha tola", "u polimer emas")],
  "nCH₂=CHCl → PVX — «plastik derazalar» materiali.",
  dict(arch="pvx"))

# 23 (3)
check("q23", 0.2*28, 5.6)
q(3, "o'rta",
  "0,2 mol etilenning massasini toping. (M(C₂H₄)=28)",
  "5,6 g", [("28 g", "1 mol uchun"), ("2,8 g", "0,1 mol emas"), ("11,2 g", "ikki baravar")],
  "m = 0,2·28 = 5,6 g.",
  dict(arch="etilen_massa"))

# 24 (2)
q(2, "o'rta",
  "Etilen suvni biriktirsa (gidratlanish) nima hosil bo'ladi?",
  "etil spirti (C₂H₅OH)",
  [("sirka kislota", "u boshqa bosqichda"), ("metan", "uglerod kamaymaydi"),
   ("glitserin", "uch atomli spirt boshqa yo'l bilan")],
  "C₂H₄ + H₂O → C₂H₅OH (katalizator) — sanoat usuli.",
  dict(arch="gidratlanish_a"))

# 25 (3)
q(3, "o'rta",
  "Quyidagi zanjirdagi X moddani aniqlang: CaC₂ → X → C₂H₄.",
  "C₂H₂ (atsetilen)",
  [("C₂H₆", "etan alkenga «qaytmaydi» bu zanjirda"), ("CH₄", "metan karbiddan olinmaydi"),
   ("CO₂", "organik zanjir uziladi")],
  "Karbid → atsetilen; C₂H₂ + H₂ → C₂H₄ (qisman gidrogenlash).",
  dict(arch="zanjir_x_2"))

# 26 (3) — RASMLI: polimerlar diagrammasi
q(3, "o'rta",
  "Diagrammada jahon plastik ishlab chiqarishida polimerlar ulushi berilgan. Yetakchi polimer qaysi?",
  "polietilen (PE)", [("PVX", "uchinchi o'rinlarda"), ("polipropilen (PP)", "ikkinchi"),
                       ("kauchuk", "u plastik emas")],
  "PE — paketdan quvurgacha: eng universal plastik.",
  dict(arch="bar_polimer_oqish"), fig="bar_polymer")

# 27 (3)
check("q27", 42, 42)
q(3, "o'rta",
  "Molyar massasi 42 g/mol bo'lgan alkenni aniqlang.",
  "propen (C₃H₆)", [("eten", "M = 28"), ("buten", "M = 56"), ("propan", "alkan, M = 44")],
  "14n = 42 → n = 3.",
  dict(arch="m42_alken"))

# 28 (2) — RASMLI: bog' uzunliklari
q(2, "o'rta",
  "Grafikda C–C, C=C va C≡C bog' uzunliklari berilgan. Bog' karrali ortgani sari uzunlik qanday "
  "o'zgaradi?",
  "qisqaradi", [("uzayadi", "aksincha"), ("o'zgarmaydi", "154 → 134 → 120 pm"),
                 ("tartibsiz", "monoton qisqaradi")],
  "Ko'proq elektron jufti atomlarni kuchliroq «tortadi» — bog' kaltaroq va mustahkamroq.",
  dict(arch="bog_uzunlik_oqish"), fig="bond_len")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Bromli suvga asta-sekin etilen yuborilmoqda. Eritma rangining INTENSIVLIGI qanday o'zgaradi? "
  "Grafikni tanlang.",
  "kamayib, nolga tushadi",
  [("o'zgarmaydi", "brom biriktirilib sarflanadi"), ("ortadi", "rang yo'qoladi, kuchaymaydi"),
   ("avval ortib keyin kamayadi", "boshidanoq kamayadi")],
  "C₂H₄ + Br₂ → C₂H₄Br₂: sariq Br₂ rangsiz birikmaga o'tadi.",
  svg=dict(correct="fall", d1="rise", d2="flat", d3="rise_fall", xlab="V(C₂H₄)", ylab="rang"),
  params=dict(arch="brom_grafik"))

# 30 (2)
q(2, "o'rta",
  "Karbid bilan ishlashda qanday ehtiyotkorlik zarur?",
  "namlikdan saqlash — suv bilan yonuvchan gaz beradi",
  [("issiqdan saqlash faqat", "asosiy xavf — nam"),
   ("yorug'likdan saqlash", "yorug'lik ta'sir qilmaydi"),
   ("hech qanday", "C₂H₂ portlovchan!")],
  "Nam havoda ham CaC₂ atsetilen ajratadi — zich yopiq idishda saqlanadi.",
  dict(arch="karbid_xavf"))

# 31 (3)
check("q31", 28000/28, 1000)
q(3, "o'rta",
  "O'rtacha molyar massasi 28 000 g/mol bo'lgan polietilen zanjirida nechta etilen zvenosi bor?",
  "1000", [("100", "28000/28"), ("28", "bu monomer massasi"), ("10000", "nol ortiqcha")],
  "n = 28000/28 = 1000.",
  dict(arch="polimer_n"))

# 32 (3) — RASMLI: bog' uzunligi hisob
check("q32", 154-120, 34)
q(3, "o'rta",
  "28-savol grafigidan: C–C va C≡C bog' uzunliklari orasidagi farqni toping (pm).",
  "34", [("20", "134−120 xato juftlik"), ("14", "154−134? yo'q, C–C va C≡C"), ("120", "bu C≡C ning o'zi")],
  "154 − 120 = 34 pm.",
  dict(arch="bog_farq"), fig="bond_len")

# ---------- Y2: uch material ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.2",
  ichki_pasport=[dict(n=33, element="III.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="III.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="III.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch buyum tekshirildi: X — polietilen plyonka; Y — avtomobil kamerasi (rezina); "
               "Z — payvandlash balloni gazi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X qaysi monomerdan olingan?",
    "34. Y materialning asosi qaysi sinf birikmasidan olingan?",
    "35. Z gaz qaysi va u qanday olinadi?"],
  javoblar_royxati=["A) etilen", "B) alkadiyendan", "C) atsetilen; karbiddan",
                    "D) metan", "E) alkanlardan", "F) etilen; havodan"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="metan polimer bermaydi"),
                   dict(variant="E", xato="kauchuk — butadien (dien) polimeri"),
                   dict(variant="F", xato="atsetilen havodan emas, karbiddan/metandan olinadi")],
  yechim=("X: nCH₂=CH₂ → PE (A). Y: kauchuk — butadien polimeri (B). "
          "Z: payvandda C₂H₂; CaC₂ + H₂O usuli (C)."),
  parametrlar=dict(arch="material_ssenariy"))

# ---------- O1 ----------
check("o36", 4.48/22.4, 0.2)
check("o37", 0.1*26, 2.6)
check("o38", 5.6/28*2*22.4, 8.96)
check("o39", 0.3*22.4, 6.72)
check("o40", 56000/28, 2000)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="4,48 L (n.sh.) etilen necha mol bo'ladi?",
      javob="0,2", yechim="n = 4,48/22,4 = 0,2 mol.",
      parametrlar=dict(arch="etilen_mol_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="0,1 mol atsetilenning massasini (g) toping. (M(C₂H₂)=26)",
      javob="2,6", yechim="m = 0,1·26 = 2,6 g.",
      parametrlar=dict(arch="atsetilen_massa_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="C₂H₄ + 3O₂ → 2CO₂ + 2H₂O. 5,6 g etilen yonganda hosil bo'lgan CO₂ hajmini (n.sh., L) "
            "toping. (M(C₂H₄)=28)",
      javob="8,96", yechim="n = 0,2 → CO₂ 0,4 mol → 8,96 L.",
      parametrlar=dict(arch="etilen_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="C₂H₄ + H₂ → C₂H₆. 0,3 mol etilenni to'liq gidrogenlash uchun zarur vodorod hajmini "
            "(n.sh., L) toping.",
      javob="6,72", yechim="n(H₂) = 0,3 mol → V = 6,72 L.",
      parametrlar=dict(arch="gidrogenlash_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Molyar massasi 56 000 g/mol bo'lgan polietilendagi zvenolar sonini toping.",
      javob="2000", yechim="n = 56000/28 = 2000.",
      parametrlar=dict(arch="polimer_o1")),
]

# ---------- O2 ----------
check("o41b", 12.8/64*22.4, 4.48)
check("o41c", 0.2*26, 5.2)
O2 = [
 dict(n=41, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Payvandlash uchun 12,8 g toza kalsiy karbid ishlatildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Atsetilen olinish tenglamasini yozing.",
             yechim=["CaC₂ + 2H₂O → C₂H₂↑ + Ca(OH)₂."], M=4, A=2),
        dict(savol="b) Ajralgan atsetilen hajmini (n.sh.) hisoblang. (M(CaC₂)=64)",
             yechim=["n = 0,2 mol → V = 4,48 L."], M=4, A=3),
        dict(savol="c) Shu gazning massasini toping. (M(C₂H₂)=26)",
             yechim=["m = 0,2·26 = 5,2 g."], M=4, A=3),
        dict(savol="d) Atsetilen alangasi nega juda yuqori haroratli? Izohlang.",
             yechim=["Uchbog'da katta energiya «jamlangan» — yonishda ko'p issiqlik ajraladi."], M=3, A=2),
      ],
      rasmiylashtirish="Karbid zanjiri: tenglama → hajm → massa → izoh; M15+A10.",
      parametrlar=dict(arch="karbid_zanjir_a")),
 dict(n=42, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Polimerlar dunyosi tahlil qilinadi. Quyidagilarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Nega aynan TO'YINMAGAN uglevodorodlar polimerlanadi, alkanlar esa yo'q?",
             yechim=["Qo'shbog'ning pi-qismi oson uziladi — bo'shagan «qo'llar» qo'shni molekulaga",
                     "ulanadi. Alkanda bunday «ochiladigan» bog' yo'q."], M=13, A=0),
        dict(savol="b) Polietilen paketlarning afzalligi va ekologik muammosi nimada?",
             yechim=["Afzallik: yengil, suv o'tkazmas, arzon. Muammo: tabiatda deyarli chirimaydi."], M=9, A=0),
        dict(savol="c) Bitta sun'iy polimer va uning monomerini yozing.",
             yechim=["PVX — vinilxlorid (yoki PP — propen)."], M=3, A=0),
      ],
      rasmiylashtirish="Polimer-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="polimer_mulohaza")),
 dict(n=43, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch gaz jadvalda berilgan:\n"
            "[JADVAL] № | Gaz | Formula ;; 1 | etan | C₂H₆ ;; 2 | etilen | C₂H₄ ;; 3 | atsetilen | C₂H₂\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir gazning sinfini va undagi C–C bog' turini yozing.",
             yechim=["Etan — alkan (yakka); etilen — alken (qo'shbog'); atsetilen — alkin (uchbog')."], M=5, A=2),
        dict(savol="b) Qaysi gazlar bromli suvni rangsizlantiradi?",
             yechim=["Etilen va atsetilen (to'yinmaganlar); etan — yo'q."], M=3, A=3),
        dict(savol="c) 2- va 3-gazlarning bromli suv bilan reaksiya tenglamalarini yozing.",
             yechim=["C₂H₄ + Br₂ → C₂H₄Br₂; C₂H₂ + 2Br₂ → C₂H₂Br₄."], M=4, A=3),
        dict(savol="d) Nega atsetilen ikki barobar ko'p brom biriktiradi?",
             yechim=["Uchbog'da IKKITA pi-bog' bor — ikkala bosqichda ochiladi."], M=3, A=2),
      ],
      rasmiylashtirish="Uch gaz jadvali: sinf → sinov → tenglamalar → izoh; M15+A10.",
      parametrlar=dict(arch="uch_gaz_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263203)
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
    d = dict(n=n, tur="Y1", element="III.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III2-A", daraja="A", bob=2, bob_nomi="Alkenlar, alkadiyenlar, alkinlar",
    manba=("MS spetsifikatsiyasi III.2; 10-sinf darslik — savollar yangi tuzilgan, hayotiy sahnalar "
           "(meva-etilen, payvandlash, PE paket, shina) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★ (Organik kimyo kitobi): soddaroq savollar, rasmli hayotiy "
          "misollar. B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
