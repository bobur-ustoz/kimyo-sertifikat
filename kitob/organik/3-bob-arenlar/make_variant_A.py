# -*- coding: utf-8 -*-
"""Organik 3-bob A-varianti: Aromatik uglevodorodlar. Neft, gaz, ko'mir (III.3) — O'RGATUVCHI ★★.
Hayotiy sahnalar: AZS (benzin), asfalt yotqizish, naftalin (kuya tabletkasi), koks pechi."""
import json, random

OUT = "mavzu_III3A.json"
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
  "Aromatik uglevodorodlarning (arenlarning) eng sodda vakili qaysi?",
  "benzol (C₆H₆)", [("metan", "u alkan"), ("atsetilen", "u alkin"), ("toluol", "u ikkinchi vakil")],
  "Olti burchakli «aromatik halqa» — arenlar asosi.",
  dict(arch="benzol_vakil"))

# 2 (2)
q(2, "quyi",
  "Benzol molekulasida nechta uglerod va vodorod atomi bor?",
  "6 ta C va 6 ta H", [("6 C va 12 H", "u siklogeksan"), ("6 C va 14 H", "u geksan"),
                        ("5 C va 6 H", "halqa olti a'zoli")],
  "C₆H₆ — halqadagi har C ga bittadan H.",
  dict(arch="benzol_formula"))

# 3 (2) — RASMLI: benzol halqasi
q(2, "o'rta",
  "Rasmda benzol molekulasining zamonaviy tasviri (halqa ichida doira). Doira nimani bildiradi?",
  "olti elektronning halqa bo'ylab TENG taqsimlanganini",
  [("uchta oddiy qo'shbog'ni", "bog'lar «o'rtachalashgan», almashinmaydigan"),
   ("halqa ichidagi bo'shliqni", "geometrik emas, elektron ma'no"),
   ("kislorod atomini", "molekulada O yo'q")],
  "Aromatik tizim: 6 pi-elektron umumiy «bulut» — barcha C–C bog'lari bir xil (140 pm).",
  dict(arch="halqa_oqish"), fig="benzene")

# 4 (2) — SAHNA: AZS
q(2, "o'rta",
  "Rasmda yoqilg'i quyish shoxobchasi. Benzin neftdan qanday jarayonda olinadi?",
  "haydash (rektifikatsiya) va krekingda",
  [("filtrlashda", "fraksiyalar filtrda ajralmaydi"),
   ("muzlatishda", "sovutish usul emas bu yerda"),
   ("elektrolizda", "tok bilan olinmaydi")],
  "Neft kolonnada fraksiyalarga bo'linadi; og'ir fraksiyalar krekingda «maydalanadi».",
  dict(arch="azs_sahna"), fig="azs")

# 5 (2)
q(2, "o'rta",
  "Benzol oddiy sharoitda qanday modda?",
  "rangsiz, o'ziga xos hidli, zaharli suyuqlik",
  [("rangsiz gaz", "suyuqlik (t_qayn = 80 °C)"), ("qattiq kristall", "u naftalin"),
   ("hidsiz suyuqlik", "hidi aynan «aromatik»")],
  "Suvda erimaydi, o'zi yaxshi erituvchi; bug'lari zaharli — ehtiyot bo'linadi.",
  dict(arch="benzol_xossa"))

# 6 (2)
q(2, "o'rta",
  "Arenlarning umumiy formulasi qaysi?",
  "CₙH₂ₙ₋₆", [("CₙH₂ₙ", "alkenlar"), ("CₙH₂ₙ₋₂", "alkinlar"), ("CₙH₂ₙ₊₂", "alkanlar")],
  "Benzol C₆H₆ (n=6), toluol C₇H₈ (n=7).",
  dict(arch="aren_formula"))

# 7 (2)
q(2, "o'rta",
  "Benzolning eng yaqin gomologi qaysi?",
  "toluol (C₆H₅–CH₃)", [("fenol", "unda OH bor — boshqa sinf"), ("stirol", "unda qo'shbog'li zanjir"),
                          ("naftalin", "u ikki halqali")],
  "Metilbenzol — bo'yoq va portlovchi moddalar xomashyosi.",
  dict(arch="toluol"))

# 8 (2) — SAHNA: asfalt
q(2, "o'rta",
  "Rasmda yo'lga asfalt yotqizilmoqda. Asfalt tarkibidagi bog'lovchi qora modda nima?",
  "bitum — neft haydashning eng og'ir qoldig'i",
  [("ko'mir kukuni", "ko'mir emas, neft mahsuloti"),
   ("qora bo'yoq", "bo'yoq bog'lamaydi"),
   ("kauchuk", "asosi bitum, qo'shimchalar bo'lishi mumkin")],
  "Mazutdan keyin qoladigan bitum shag'alni «yelimlab» yo'l qoplamasini beradi.",
  dict(arch="asfalt_sahna"), fig="asphalt")

# 9 (2)
q(2, "o'rta",
  "Neftni haydashda fraksiyalar nimaga qarab ajraladi?",
  "qaynash haroratlari oralig'iga qarab",
  [("rangiga qarab", "rang mezon emas"), ("hidiga qarab", "hid ham emas"),
   ("zichligiga qarab faqat", "asosiy mezon — t_qayn")],
  "Kolonnaning pastida og'ir (yuqori t), tepasida yengil (past t) fraksiyalar.",
  dict(arch="fraksiya_mezon"))

# 10 (3)
check("q10", 7.8/78*6*22.4, 13.44)
q(3, "o'rta",
  "2C₆H₆ + 15O₂ → 12CO₂ + 6H₂O. 7,8 g benzol yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(M(C₆H₆)=78)",
  "13,44 L", [("2,24 L", "koeffitsiyent 6"), ("22,4 L", "1 mol uchun"), ("6,72 L", "hisob xato")],
  "n = 0,1 → n(CO₂) = 0,6 mol → V = 13,44 L.",
  dict(arch="benzol_yonish"))

# 11 (2)
q(2, "o'rta",
  "KREKING jarayonining mohiyati nimada?",
  "og'ir uglevodorodlarni yuqori haroratda maydalab, benzin olish",
  [("neftni suv bilan aralashtirish", "aralashtirish o'zgartirmaydi"),
   ("gazni suyultirish", "u fizik jarayon"),
   ("benzinni tozalash", "tozalash emas, YARATISH")],
  "C₁₆H₃₄ → C₈H₁₈ + C₈H₁₆: benzin unumini 2-3 barobar oshiradi.",
  dict(arch="kreking_tarif"))

# 12 (3)
check("q12", 78, 78)
q(3, "o'rta",
  "Molyar massasi 78 g/mol bo'lgan aromatik uglevodorodni aniqlang.",
  "benzol (C₆H₆)", [("toluol", "M = 92"), ("geksan", "M = 86, aromatik emas"),
                     ("siklogeksan", "M = 84, aromatik emas")],
  "12·6 + 6 = 78.",
  dict(arch="m78"))

# 13 (2) — SAHNA: naftalin
q(2, "o'rta",
  "Rasmda kiyim shkafi uchun «kuya tabletkalari» (naftalin). Naftalin qanday modda?",
  "ikki halqali aromatik uglevodorod (C₁₀H₈), oson sublimatlanadi",
  [("mineral tuz", "organik modda"), ("polimer", "kichik molekula"),
   ("spirt", "tarkibida OH yo'q")],
  "Uchuvchan kristallar hidi kuyani qochiradi; qattiqdan to'g'ri bug'ga o'tadi.",
  dict(arch="naftalin_sahna"), fig="mothball")

# 14 (2)
q(2, "o'rta",
  "Benzol uchun qaysi reaksiya turi XOS?",
  "halqani saqlagan holda O'RIN OLISH",
  [("oson birikish", "aromatik tizim «buzilishni yoqtirmaydi»"),
   ("polimerlanish", "halqa polimerlanmaydi"),
   ("parchalanish oson", "halqa juda barqaror")],
  "Aromatiklik halqani himoya qiladi: Br₂/HNO₃ H o'rnini oladi, halqa buzilmaydi.",
  dict(arch="orin_olish_aren"))

# 15 (2)
q(2, "o'rta",
  "Toshko'mirni havosiz qizdirish (kokslash) mahsulotlariga nima kiradi?",
  "koks, toshko'mir smolasi, koks gazi",
  [("faqat kul", "kul — yonish qoldig'i"), ("benzin va kerosin", "ular neftdan"),
   ("sof uglerod faqat", "smola va gaz ham chiqadi")],
  "Koks — metallurgiya uchun; smola — aromatik moddalar manbai.",
  dict(arch="kokslash"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Fraksiya | Qo'llanishi ;; benzin | ? ;; kerosin | ? ;; mazut | ?",
  "avtomobil; aviatsiya; qozonxona yoqilg'isi",
  [("aviatsiya; avtomobil; asfalt", "birinchi ikkisi almashgan"),
   ("qozonxona; avtomobil; aviatsiya", "tartib chalkash"),
   ("avtomobil; asfalt; aviatsiya", "kerosin — reaktiv yoqilg'i")],
  "Benzin — avtomobillar; kerosin — samolyotlar; mazut — issiqlik energetikasi.",
  dict(arch="fraksiya_jadval"))

# 17 (2)
q(2, "o'rta",
  "Benzol qayerda ishlatiladi?",
  "bo'yoqlar, dorilar, plastmassalar sintezida xomashyo sifatida",
  [("ichimlik sifatida", "o'ta zaharli!"), ("oziq-ovqat qo'shimchasi", "taqiqlangan"),
   ("o'g'it sifatida", "organik sintez xomashyosi")],
  "«Aromatik daraxt»ning ildizi: anilin, stirol, fenol — barchasi benzoldan.",
  dict(arch="benzol_qollash"))

# 18 (2) — SAHNA: koks pechi
q(2, "o'rta",
  "Rasmda koks batareyasi: ko'mir 1000 °C da havosiz qizdirilmoqda. Nega havosiz?",
  "havo bo'lsa ko'mir yonib ketadi — maqsad esa parchalash",
  [("harorat ko'tarilmasligi uchun", "aksincha, yuqori harorat kerak"),
   ("hid chiqmasligi uchun", "asosiy sabab kimyoviy"),
   ("shunchaki an'ana", "texnologik zarurat")],
  "Piroliz: kislorodsiz muhitda modda yonmay, qismlarga ajraladi.",
  dict(arch="koks_sahna"), fig="cokeoven")

# 19 (3)
check("q19", 0.2*78, 15.6)
q(3, "o'rta",
  "0,2 mol benzolning massasini toping. (M(C₆H₆)=78)",
  "15,6 g", [("78 g", "1 mol uchun"), ("7,8 g", "0,1 mol emas"), ("31,2 g", "ikki baravar")],
  "m = 0,2·78 = 15,6 g.",
  dict(arch="benzol_massa"))

# 20 (2)
q(2, "o'rta",
  "Tabiiy gaz, neft va ko'mir birgalikda qanday nomlanadi?",
  "qazilma (uglevodorod) yoqilg'ilari",
  [("mineral o'g'itlar", "ular boshqa sinf"), ("qayta tiklanuvchi manbalar", "aksincha — tugaydigan"),
   ("sun'iy yoqilg'ilar", "tabiiy qazilmalar")],
  "Millionlab yillik organik qoldiqlar — energiya va kimyo xomashyosi.",
  dict(arch="qazilma_yoqilgi"))

# 21 (2)
q(2, "o'rta",
  "Benzol suvga qo'shilsa nima kuzatiladi?",
  "aralashmaydi — yengil qatlam bo'lib suzadi",
  [("to'liq eriydi", "erimaydi"), ("cho'kadi", "zichligi 0,88 — suvdan yengil"),
   ("reaksiyaga kirishadi", "oddiy sharoitda suv bilan reaksiya yo'q")],
  "Organik erituvchi: o'zi suvda erimay, moy-yog'larni eritadi.",
  dict(arch="benzol_suv"))

# 22 (2)
q(2, "o'rta",
  "Stirol qaysi mashhur polimerning monomeri?",
  "polistirol (penoplast)",
  [("polietilen", "u etilendan"), ("kauchuk", "u butadiendan"), ("PVX", "u vinilxloriddan")],
  "C₆H₅–CH=CH₂ → penoplast, bir martalik idishlar.",
  dict(arch="stirol"))

# 23 (3)
check("q23", 92, 92)
q(3, "o'rta",
  "Toluolning (C₇H₈) molyar massasini toping.",
  "92 g/mol", [("78 g/mol", "bu benzol"), ("84 g/mol", "hisob xato"), ("106 g/mol", "bu ksilol")],
  "12·7 + 8 = 92.",
  dict(arch="toluol_m"))

# 24 (2)
q(2, "o'rta",
  "Neftning «quruq qoldiq»qa qadar haydalgan eng og'ir mahsuloti bo'lgan mazutdan yana nima olinadi?",
  "moylash moylari, parafin, bitum",
  [("benzin bevosita ko'p miqdorda", "benzin uchun kreking kerak"),
   ("tabiiy gaz", "gaz alohida qazilma"),
   ("koks", "koks ko'mirdan")],
  "Mazut vakuumda qayta haydaladi — «og'ir» boyliklar ajratiladi.",
  dict(arch="mazut"))

# 25 (3)
q(3, "o'rta",
  "Zanjirdagi X moddani aniqlang: CH₄ → C₂H₂ → X (uch molekula birikishi).",
  "benzol", [("etilen", "trimerlanish mahsuloti emas"), ("geksan", "to'yingan modda hosil bo'lmaydi"),
              ("siklogeksan", "u benzoldan gidrogenlashda")],
  "3C₂H₂ → C₆H₆ — Zelinskiy trimerlanishi.",
  dict(arch="zanjir_benzol"))

# 26 (3) — RASMLI: neft mahsulotlari
q(3, "o'rta",
  "Diagrammada 1 tonna neftdan olinadigan asosiy mahsulotlar berilgan. Qaysi mahsulot ulushi "
  "eng katta?",
  "dizel yoqilg'isi", [("benzin", "ikkinchi o'rinda"), ("mazut va boshqalar", "uchinchi"),
                        ("kerosin", "eng kichik ulush")],
  "Zamonaviy zavodda: dizel ≈ 32 %, benzin ≈ 25 %, kerosin ≈ 8 %.",
  dict(arch="bar_neft_oqish"), fig="bar_oil")

# 27 (3)
check("q27", 15.6/78*6*18/2/18, 0.6, tol=0.01)
q(3, "o'rta",
  "2C₆H₆ + 15O₂ → 12CO₂ + 6H₂O. 15,6 g benzol yonganda necha mol suv hosil bo'ladi? (M(C₆H₆)=78)",
  "0,6", [("0,2", "nisbat 2:6 = 1:3"), ("1,2", "ikki baravar"), ("6", "1 mol... koeffitsiyent adashuvi")],
  "n = 0,2 mol → n(H₂O) = 0,6 mol.",
  dict(arch="benzol_suv_hisob"))

# 28 (2) — RASMLI: kolonna
q(2, "o'rta",
  "Rasmdagi rektifikatsion kolonnada BENZIN qayerdan chiqadi?",
  "yuqori qismidan — u eng yengil fraksiyalardan",
  [("pastidan", "pastda og'ir mazut"), ("o'rtasidan faqat", "o'rtada kerosin-dizel"),
   ("istalgan joyidan", "har fraksiyaning o'z «qavati» bor")],
  "Yengil bug'lar yuqoriga ko'tarilib kondensatlanadi.",
  dict(arch="kolonna_oqish"), fig="column")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Neft fraksiyalarida molekula kattalashgani sari qaynash harorati qanday o'zgaradi? Grafikni "
  "tanlang.",
  "ortib boradi",
  [("kamayadi", "og'ir molekula qiyin bug'lanadi"), ("o'zgarmaydi", "benzin 40°, mazut 350°+ farq bor"),
   ("avval kamayib keyin ortadi", "monoton ortadi")],
  "Molekulalararo kuchlar zanjir uzunligi bilan o'sadi.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="u", xlab="C soni", ylab="t(qayn.)"),
  params=dict(arch="fraksiya_grafik"))

# 30 (2)
q(2, "o'rta",
  "Benzol bug'lari bilan ishlashda qanday ehtiyot chorasi SHART?",
  "tortish shkafida ishlash — bug'lari zaharli",
  [("hidlab tekshirish", "qat'iyan mumkin emas"), ("ochiq olov yonida ishlash", "yonuvchan!"),
   ("hech qanday", "kanserogen modda")],
  "Benzol — kanserogen: faqat yopiq tizim va ventilyatsiya.",
  dict(arch="benzol_xavf"))

# 31 (3)
check("q31", 39/78, 0.5)
q(3, "o'rta",
  "39 g benzol necha mol bo'ladi? (M(C₆H₆)=78)",
  "0,5", [("2", "teskari bo'lingan"), ("0,39", "birlik adashuvi"), ("1", "78 g bo'lardi")],
  "n = 39/78 = 0,5 mol.",
  dict(arch="benzol_mol"))

# 32 (3) — RASMLI: neft hisob
check("q32", 1000*0.25, 250)
q(3, "o'rta",
  "26-savol diagrammasidan: 1000 kg neftdan taxminan qancha benzin olinadi (ulush 25 %)?",
  "250 kg", [("25 kg", "nol adashgan"), ("320 kg", "bu dizel ulushi"), ("500 kg", "yarmi emas")],
  "m = 1000·0,25 = 250 kg.",
  dict(arch="bar_neft_hisob"), fig="bar_oil")

# ---------- Y2: uch yoqilg'i-xomashyo ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.3",
  ichki_pasport=[dict(n=33, element="III.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="III.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="III.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch xomashyo solishtirildi: X — quduqdan chiqadigan qora suyuqlik; Y — qazilma "
               "qattiq yoqilg'i; Z — X ni haydashdan olingan, samolyotlarda ishlatiladigan fraksiya. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X xomashyo qaysi?",
    "34. Y dan havosiz qizdirishda olinadigan asosiy qattiq mahsulot qaysi?",
    "35. Z fraksiya qaysi?"],
  javoblar_royxati=["A) neft", "B) koks", "C) kerosin", "D) tabiiy gaz", "E) kul", "F) benzin"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="gaz suyuqlik emas"),
                   dict(variant="E", xato="kul — yonish qoldig'i; kokslash mahsuloti koks"),
                   dict(variant="F", xato="aviatsiya yoqilg'isi — kerosin")],
  yechim=("X — neft (A). Y (ko'mir) kokslanganda koks (B). Z — kerosin (C)."),
  parametrlar=dict(arch="xomashyo_ssenariy"))

# ---------- O1 ----------
check("o36", 0.1*78, 7.8)
check("o37", 15.6/78, 0.2)
check("o38", 4.6/92, 0.05)
check("o39", 0.3*3*22.4, 20.16)
check("o40", 500*0.32, 160)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,1 mol benzolning massasini (g) toping. (M(C₆H₆)=78)",
      javob="7,8", yechim="m = 0,1·78 = 7,8 g.",
      parametrlar=dict(arch="benzol_massa_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="15,6 g benzol necha mol bo'ladi?",
      javob="0,2", yechim="n = 15,6/78 = 0,2 mol.",
      parametrlar=dict(arch="benzol_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="4,6 g toluol necha mol bo'ladi? (M(C₇H₈)=92)",
      javob="0,05", yechim="n = 4,6/92 = 0,05 mol.",
      parametrlar=dict(arch="toluol_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="C₆H₆ + 3H₂ → C₆H₁₂. 0,3 mol benzolni to'liq gidrogenlash uchun zarur vodorod hajmini "
            "(n.sh., L) toping.",
      javob="20,16", yechim="n(H₂) = 0,9 mol → V = 20,16 L.",
      parametrlar=dict(arch="gidrogenlash_o1_3")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Zavod 500 t neft qayta ishladi; dizel unumi 32 %. Olingan dizel massasini (t) toping.",
      javob="160", yechim="m = 500·0,32 = 160 t.",
      parametrlar=dict(arch="dizel_o1")),
]

# ---------- O2 ----------
check("o41b", 15.6/78, 0.2); check("o41c", 0.2*12*22.4/2, 26.88)
O2 = [
 dict(n=41, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada 15,6 g benzol to'liq yondirildi (2C₆H₆ + 15O₂ → 12CO₂ + 6H₂O). "
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Benzol mol miqdorini toping.",
             yechim=["n = 15,6/78 = 0,2 mol."], M=4, A=2),
        dict(savol="b) Hosil bo'lgan CO₂ hajmini (n.sh.) hisoblang.",
             yechim=["n(CO₂) = 0,2·6 = 1,2 mol → V = 26,88 L."], M=4, A=3),
        dict(savol="c) Nega benzol tutab (qurumli) yonadi? Izohlang.",
             yechim=["ω(C) juda yuqori (92 %) — uglerod to'liq yonishga «ulgurmaydi»."], M=4, A=3),
        dict(savol="d) Benzol bilan ishlash xavfsizligi bo'yicha ikkita qoida yozing.",
             yechim=["Tortish shkafi/ventilyatsiya; ochiq olovdan uzoq, teri bilan kontaktsiz."], M=3, A=2),
      ],
      rasmiylashtirish="Benzol-yonish: mol → hajm → izoh → xavfsizlik; M15+A10.",
      parametrlar=dict(arch="benzol_yonish_zanjir")),
 dict(n=42, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("«Neft — faqat yoqilg'i emas» mavzusi tahlil qilinadi. Quyidagilarga MULOHAZA yuritib "
            "javob yozing."),
      bandlar=[
        dict(savol="a) Nega Mendeleyev «neftni yoqish — pechkani banknotalar bilan yoqish» degan? "
                   "Fikrni asoslang.",
             yechim=["Neft — minglab moddalar xomashyosi: plastmassa, dori, tola, bo'yoq.",
                     "Yoqilganda bu imkoniyatlar «tutunga» aylanadi — kimyoviy qiymat energiyadan yuqori."], M=13, A=0),
        dict(savol="b) Kreking jarayoni neftni qayta ishlashda nima uchun «inqilob» qildi?",
             yechim=["Og'ir fraksiyalardan qo'shimcha benzin — mahsulot unumi keskin oshdi."], M=9, A=0),
        dict(savol="c) Neftdan olinadigan uchta nooziq mahsulotni yozing.",
             yechim=["Polietilen, sintetik tola, dorivor moddalar (yoki bitum, moylar)."], M=3, A=0),
      ],
      rasmiylashtirish="Neft-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="neft_mulohaza")),
 dict(n=43, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch uglevodorod jadvalda berilgan:\n"
            "[JADVAL] № | Modda | Formula ;; 1 | geksan | C₆H₁₄ ;; 2 | siklogeksan | C₆H₁₂ ;; "
            "3 | benzol | C₆H₆\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har birining sinfini aniqlang.",
             yechim=["Geksan — alkan; siklogeksan — sikloalkan; benzol — aren."], M=4, A=2),
        dict(savol="b) Qaysi biri bromli suvni RANGSIZLANTIRMAYDI va nima uchun uchchalasi ham "
                   "shu sinovda «jim»?",
             yechim=["Uchchalasi ham: alkan/sikloalkan to'yingan, benzolda esa aromatik tizim oddiy "
                     "sharoitda birikishga bormaydi."], M=4, A=3),
        dict(savol="c) 3-moddaning vodorod biriktirish tenglamasini yozing.",
             yechim=["C₆H₆ + 3H₂ → (kat., t) C₆H₁₂ — siklogeksan."], M=4, A=3),
        dict(savol="d) Uchchala moddada ω(C) qaysi tartibda ortadi?",
             yechim=["Geksan (83,7 %) < siklogeksan (85,7 %) < benzol (92,3 %)."], M=3, A=2),
      ],
      rasmiylashtirish="C₆-uchlik: sinf → sinov → reaksiya → ω(C); M15+A10.",
      parametrlar=dict(arch="c6_uchlik_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263303)
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
    d = dict(n=n, tur="Y1", element="III.3", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III3-A", daraja="A", bob=3, bob_nomi="Aromatik uglevodorodlar. Neft, gaz, ko'mir",
    manba=("MS spetsifikatsiyasi III.3; 10-sinf darslik — savollar yangi tuzilgan, hayotiy sahnalar "
           "(AZS, asfalt, naftalin, koks pechi) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
