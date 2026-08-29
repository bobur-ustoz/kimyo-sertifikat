# -*- coding: utf-8 -*-
"""2-bob A-varianti: Davriy qonun va davriy sistema (I.2) — O'RGATUVCHI ★★.
Hayotiy sahnalar: geliy shari, yod antiseptigi, alyuminiy folga, sut-kalsiy."""
import json, random

OUT = "mavzu_I2A.json"
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
  "Davriy sistemada elementlar qanday tartibda joylashtirilgan?",
  "yadro zaryadi (tartib raqami) ortib borishi bo'yicha",
  [("alifbo bo'yicha", "kimyoviy asos yo'q bo'lardi"),
   ("zichligi bo'yicha", "zichlik davriy emas"),
   ("kashf etilgan sanasi bo'yicha", "tarixiy tartib emas")],
  "Z = 1 (H) dan boshlab ketma-ket.",
  dict(arch="tartib_oddiy"))

# 2 (2)
q(2, "quyi",
  "Davriy jadvaldagi GORIZONTAL qator nima deb ataladi?",
  "davr", [("guruh", "guruh — vertikal ustun"), ("oila", "alohida tushuncha"), ("qavat", "atom tuzilishiga oid")],
  "Gorizontal — davr; vertikal — guruh.",
  dict(arch="davr_guruh_tarif"))

# 3 (2)
q(2, "o'rta",
  "Bir GURUHDAGI elementlar nimasi bilan o'xshash?",
  "tashqi qavatdagi elektronlar soni (valentligi) bilan",
  [("qavatlar soni bilan", "bu davrga xos"), ("atom massalari bilan", "massalar keskin farq qiladi"),
   ("izotoplar soni bilan", "bog'liq emas")],
  "I A: hammada tashqi 1 e → xossalari o'xshash (ishqoriy metallar).",
  dict(arch="guruh_oxshash"))

# 4 (2) — SAHNA: yod
q(2, "o'rta",
  "Rasmda dorixona yodi (jarohatga surtiladigan qo'ng'ir eritma). Yod elementi davriy jadvalning "
  "qaysi guruhida joylashgan?",
  "VII A — galogenlar",
  [("I A — ishqoriy metallar", "yod metall emas"),
   ("VIII A — inert gazlar", "yod faol metallmas"),
   ("II A", "kalsiy guruhi")],
  "I — galogen (F, Cl, Br, I qatori); antiseptik xossasi oksidlovchiligidan.",
  dict(arch="yod_sahna"), fig="iodine")

# 5 (2)
q(2, "o'rta",
  "Metallar davriy jadvalning qaysi qismida ko'proq joylashgan?",
  "chap va pastki qismida",
  [("o'ng yuqori burchagida", "u yerda metallmaslar"), ("faqat o'rtasida", "chap-past asosiy hudud"),
   ("faqat 1-davrda", "1-davrda H va He")],
  "Chap-past — metallar; o'ng-yuqori — metallmaslar; chegarada — yarim metallar.",
  dict(arch="metall_joy"))

# 6 (3)
q(3, "o'rta",
  "Natriy (3-davr, I A) atomining qavatlari va tashqi elektronlari soni qancha?",
  "3 qavat, 1 e", [("1 qavat, 3 e", "teskari olingan"), ("3 qavat, 8 e", "I A — 1 valent e"),
                    ("11 qavat, 1 e", "11 — jami e, qavat emas")],
  "Davr = 3 qavat; guruh I A = tashqi 1 e.",
  dict(arch="orin_oqish"))

# 7 (2)
q(2, "o'rta",
  "Ishqoriy metallar (I A) suv bilan reaksiyada qaysi gaz ajratadi?",
  "vodorod", [("kislorod", "suvdan O₂ ajralmaydi bu holda"), ("azot", "manba yo'q"), ("xlor", "tarkibda yo'q")],
  "2Na + 2H₂O → 2NaOH + H₂↑.",
  dict(arch="ia_suv"))

# 8 (2) — SAHNA: geliy shari
q(2, "o'rta",
  "Rasmda geliy bilan to'ldirilgan bayram sharlari. Nega sharlarga vodorod emas, geliy solinadi?",
  "geliy inert — yonmaydi va portlamaydi",
  [("geliy vodoroddan yengil", "aksincha, biroz og'irroq"),
   ("geliy arzonroq", "aksincha, qimmatroq"),
   ("geliy rangli", "geliy rangsiz")],
  "He — VIII A: qavati to'la, hech narsa bilan reaksiyaga kirishmaydi. H₂ esa portlovchi.",
  dict(arch="geliy_sahna"), fig="balloon")

# 9 (2)
q(2, "o'rta",
  "Galogenlar (VII A) tashqi qavatida nechta elektron bor?",
  "7", [("1", "I A uchun"), ("8", "inert gazlar"), ("17", "Cl ning jami e soni")],
  "VII A → 7 valent e; bitta e yetishmaydi → faol metallmaslar.",
  dict(arch="galogen_e"))

# 10 (3)
q(3, "o'rta",
  "Davr bo'ylab chapdan o'ngga atom radiusi qanday o'zgaradi va nega?",
  "kichrayadi — yadro zaryadi ortib, elektronlarni kuchliroq tortadi",
  [("kattalashadi — elektronlar ko'payadi", "qavat soni o'zgarmaydi, tortish kuchayadi"),
   ("o'zgarmaydi", "Z ortishi ta'sir qiladi"),
   ("avval kattalashadi, keyin kichrayadi", "monoton kichrayadi")],
  "Qavatlar soni bir xil, yadro zaryadi ortadi → tortish kuchayadi → radius ↓.",
  dict(arch="radius_davr"))

# 11 (2)
q(2, "o'rta",
  "Qaysi element ISHQORIY METALL?",
  "K", [("Ca", "II A — ishqoriy-yer metall"), ("Fe", "d-element"), ("Cl", "galogen")],
  "I A: Li, Na, K, Rb, Cs.",
  dict(arch="ia_tanlash"))

# 12 (3)
q(3, "o'rta",
  "Element 2-davr, IV A guruhda joylashgan. Bu qaysi element?",
  "C", [("Si", "3-davrda"), ("N", "V A"), ("B", "III A")],
  "2-davr, 4 valent e → uglerod.",
  dict(arch="orin_element"))

# 13 (2) — SAHNA: alyuminiy folga
q(2, "o'rta",
  "Rasmda oshxona folgasi (alyuminiy). Al davriy jadvalda 3-davr, III A guruhda. Uning atomida "
  "nechta valent elektron bor?",
  "3", [("13", "bu jami elektronlar"), ("8", "qavat sig'imi bilan chalkashuv"), ("1", "I A emas")],
  "III A → tashqi qavatda 3 e (3s²3p¹); shu bois Al³⁺ ion beradi.",
  dict(arch="folga_sahna"), fig="foil")

# 14 (3)
q(3, "o'rta",
  "Guruhda yuqoridan pastga metallik xossasi qanday o'zgaradi?",
  "kuchayadi", [("kuchsizlanadi", "radius ortadi — e berish osonlashadi"),
                 ("o'zgarmaydi", "radius o'zgaradi"), ("davriy tebranadi", "monoton kuchayadi")],
  "Li → Cs: radius ↑, tashqi e osonroq beriladi → metallik ↑.",
  dict(arch="metallik_guruh"))

# 15 (2)
q(2, "o'rta",
  "Eng faol METALLMAS element qaysi?",
  "F", [("Cl", "ftordan keyin"), ("O", "ikkinchi o'rin"), ("Na", "bu faol METALL")],
  "Ftor — o'ng yuqori burchak, EM = 4,0.",
  dict(arch="faol_metallmas"))

# 16 (3)
q(3, "o'rta",
  "Natriyning OLIY oksidi va unga mos gidroksid qaysi javobda to'g'ri?",
  "Na₂O va NaOH", [("NaO va NaOH", "natriy bir valentli: Na₂O"), ("Na₂O₂ va NaOH", "peroksid oliy oksid emas"),
                    ("Na₂O va NaH", "NaH — gidrid, gidroksid emas")],
  "I A → R₂O va ROH (kuchli ishqor).",
  dict(arch="na_oksid"))

# 17 (2)
q(2, "o'rta",
  "Jadvaldagi «?» katakni to'ldiring:\n"
  "[JADVAL] Guruh | I A | II A | VII A ;; Valent e | 1 | ? | 7",
  "2", [("4", "II A — 2 valent e"), ("8", "inert gazlarga xos"), ("12", "Mg ning jami e")],
  "II A (Be, Mg, Ca...): tashqi qavatda 2 e.",
  dict(arch="jadval_valent"))

# 18 (2) — SAHNA: sut-kalsiy
q(2, "o'rta",
  "Rasmda bir stakan sut — kalsiy manbai. Ca (II A) organizmda suyak to'qimasini mustahkamlaydi. "
  "Kalsiy qanday ion hosil qiladi?",
  "Ca²⁺ — 2 elektron beradi",
  [("Ca²⁻ — 2 elektron oladi", "metall e beradi, olmaydi"),
   ("Ca⁺ — 1 elektron beradi", "II A — ikkala valent e ketadi"),
   ("ion hosil qilmaydi", "faol metall — doim Ca²⁺")],
  "II A metallari 2 e berib, barqaror qavatga erishadi: Ca²⁺ (suyakdagi fosfatlar tarkibida).",
  dict(arch="sut_sahna"), fig="milk")

# 19 (3)
q(3, "o'rta",
  "Qaysi qatorda elementlar faolligi (metallik) KUCHAYIB boradi?",
  "Li → Na → K", [("K → Na → Li", "teskari"), ("F → Cl → Br", "bular metallmas"),
                   ("Al → Mg → ... aniqrog'i: Fe → Cu → Ag", "passivlashish qatori")],
  "I A da pastga faollik ortadi: kaliy suv bilan alanga olib reaksiyaga kirishadi.",
  dict(arch="faollik_qator"))

# 20 (2)
q(2, "o'rta",
  "Amfoter element qaysi?",
  "Al", [("Na", "tipik metall"), ("S", "tipik metallmas"), ("Ar", "inert gaz")],
  "Al birikmalari ham kislota, ham ishqor bilan reaksiyaga kirishadi.",
  dict(arch="amfoter_oddiy"))

# 21 (3)
check("q21", 8-2, 6)
q(3, "o'rta",
  "Elementning uchuvchan vodorodli birikmasi H₂R. U qaysi guruhda joylashgan?",
  "VI A", [("II A", "vodorodli birikma formulasi 8−guruh qoidasi bilan"), ("IV A", "RH₄ bo'lardi"),
            ("VII A", "HR bo'lardi")],
  "Vodorodlilar: guruh = 8 − H soni = 8 − 2 = 6 → VI A (H₂O, H₂S).",
  dict(arch="h2r_guruh"))

# 22 (3)
q(3, "o'rta",
  "3-davr elementlari oksidlari Na₂O, MgO, Al₂O₃, SO₃ ichida KISLOTALI oksid qaysi?",
  "SO₃", [("Na₂O", "asosli"), ("MgO", "asosli"), ("Al₂O₃", "amfoter")],
  "Metallmas oliy oksidi — kislotali: SO₃ + H₂O → H₂SO₄.",
  dict(arch="kislotali_oksid"))

# 23 (2)
q(2, "o'rta",
  "Davriy jadvalda nechta guruh (asosiy) bor?",
  "8", [("7", "davrlar soni"), ("10", "yonaki bilan ham 8+8"), ("18", "IUPAC ustunlari")],
  "An'anaviy jadval: I A – VIII A.",
  dict(arch="guruh_soni"))

# 24 (3)
q(3, "o'rta",
  "Mg va Ca ni taqqoslang: qaysi biri faolroq va nega?",
  "Ca — radiusi katta, elektronlarini osonroq beradi",
  [("Mg — kichik, tez reaksiya", "kichik radius e ni mahkam ushlaydi"),
   ("bir xil — bitta guruh", "guruh ichida ham farq bor"),
   ("Mg — massasi kichik", "massa emas, radius hal qiladi")],
  "II A da pastga: Ca suv bilan sovuqda ham reaksiyaga kirishadi, Mg — qiyin.",
  dict(arch="mg_ca"))

# 25 (2)
q(2, "o'rta",
  "«Galogen» so'zining ma'nosi va guruhning tipik xossasi qaysi javobda to'g'ri?",
  "«tuz tug'diruvchi»; metallar bilan tuz hosil qiladi",
  [("«suv sevuvchi»; suvda erimaydi", "ma'no ham, xossa ham xato"),
   ("«nur taratuvchi»; shu'la beradi", "bunday ma'no yo'q"),
   ("«yengil»; uchuvchan metall", "galogenlar metallmas")],
  "NaCl, KBr... — galogenlar metallar bilan tipik tuzlar beradi.",
  dict(arch="galogen_manо"))

# 26 (3) — grafik tanlash
q(3, "o'rta",
  "I A guruhda yuqoridan pastga (Li → Cs) elementlarning FAOLLIGI qanday o'zgaradi? Grafikni tanlang.",
  "ortib boradi",
  [("kamayadi", "radius ortadi — e oson beriladi"), ("o'zgarmaydi", "radius o'zgaradi"),
   ("ortib, keyin kamayadi", "monoton ortadi")],
  "Cs — eng faol barqaror ishqoriy metall.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="rise_fall", xlab="Li→Cs", ylab="faollik"),
  params=dict(arch="faollik_grafik"))

# 27 (3)
check("q27", 62, 62)
q(3, "o'rta",
  "Na₂O ning molyar massasini toping. (M(Na)=23, M(O)=16)",
  "62", [("39", "bitta Na olingan"), ("78", "ikki O xato"), ("46", "O unutilgan")],
  "2·23 + 16 = 62 g/mol.",
  dict(arch="m_oddiy"))

# 28 (2)
q(2, "o'rta",
  "Davriy jadvalning o'ng yuqori burchagiga yaqinlashganda elementlar xossasi qanday o'zgaradi?",
  "metallmaslik kuchayadi",
  [("metallik kuchayadi", "metallik chap-pastga kuchayadi"),
   ("faollik yo'qoladi", "F — eng faol metallmas"),
   ("radius kattalashadi", "radius kichrayadi")],
  "O'ng-yuqori — metallmaslar «poytaxti» (F, O, Cl).",
  dict(arch="ong_yuqori"))

# 29 (3)
q(3, "o'rta",
  "Elementning oliy oksidi RO₂, o'zi 3-davrda. Elementni va oksidini ayting.",
  "Si; SiO₂", [("C; CO₂", "uglerod 2-davrda"), ("S; SO₂", "S ning oliy oksidi SO₃"),
                ("P; PO₂", "P ning oliy oksidi P₂O₅")],
  "RO₂ → IV A; 3-davr → kremniy (qum — SiO₂).",
  dict(arch="ro2_oddiy"))

# 30 (2)
q(2, "o'rta",
  "Davriy sistema haqidagi fikrlardan XATOSINI toping.",
  "bir davr elementlarining xossalari bir xil bo'ladi",
  [("guruhdoshlar o'xshash xossali", "to'g'ri fikr"),
   ("davr yangi qavat ochilishi bilan boshlanadi", "to'g'ri fikr"),
   ("metallar chap tomonda ko'p", "to'g'ri fikr")],
  "Davr ichida xossalar keskin O'ZGARADI (Na dan Cl gacha); o'xshashlik — guruhda.",
  dict(arch="xato_fikr"))

# 31 (3)
check("q31", 40+16, 56)
q(3, "o'rta",
  "Kalsiyning oliy oksidi massasi 5,6 g. Uning mol miqdorini toping. (M(CaO)=56)",
  "0,1", [("1", "o'n barobar xato"), ("0,056", "grammda qoldirilgan"), ("0,2", "M=28 xato")],
  "n = 5,6/56 = 0,1 mol.",
  dict(arch="cao_mol"))

# 32 (3) — RASMLI: fragment o'qish (oddiy)
q(3, "o'rta",
  "Rasmdagi davriy jadval fragmentida X ning ustida N turibdi. X va N qaysi umumiy xossaga ega?",
  "ikkalasi V A guruhda — valent elektronlari 5 tadan",
  [("ikkalasi bir davrda", "ustma-ust — bitta GURUH"),
   ("ikkalasi metall", "ikkalasi metallmas"),
   ("hech qanday umumiylik yo'q", "guruhdoshlar o'xshash")],
  "Ustun bo'ylab joylashganlar guruhdosh: N va P (X) — V A, RH₃ va R₂O₅ beradi.",
  dict(arch="fragment_oddiy"), fig="pt_fragment")

# ---------- Y2: oshxona elementlari ----------
Y2 = dict(
  n=33, tur="Y2", element="I.2",
  ichki_pasport=[dict(n=33, element="I.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Oshxonadagi uch «kimyoviy qahramon»: osh tuzi tarkibidagi X metali, sut tarkibidagi "
               "Y metali va dorixona yodi — Z elementi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X elementi qaysi guruhda joylashgan?",
    "34. Y elementining ioni qanday zaryadli?",
    "35. Z elementining vodorodli birikmasi formulasi qanday?"],
  javoblar_royxati=["A) I A", "B) 2+", "C) HI", "D) VII A", "E) 1+", "F) HIO₄"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="VII A — yodning (Z) guruhi, natriyniki emas"),
                   dict(variant="E", xato="1+ — natriy ioni; savol kalsiy (Y) haqida"),
                   dict(variant="F", xato="HIO₄ — kislorodli kislota, vodorodli birikma emas")],
  yechim=("X = Na (NaCl) → I A (A). Y = Ca (sut) → Ca²⁺ (B). Z = I → HI (C)."),
  parametrlar=dict(arch="oshxona_ssenariy"))

# ---------- O1 ----------
check("o38", 8-1, 7)
check("o39", 24+16, 40)
check("o40", 9.4/94, 0.1)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="4-davr, II A guruh elementini yozing.",
      javob="Ca", yechim="4-davr, 2 valent e → kalsiy.",
      parametrlar=dict(arch="orin_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="VII A guruh elementining oliy oksidi umumiy formulasini yozing.",
      javob="R₂O₇", yechim="Oliy valentlik = 7 → R₂O₇.",
      parametrlar=dict(arch="oksid_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="Elementning vodorodli birikmasi HR bo'lsa, tashqi qavatida nechta elektron bor?",
      javob="7", yechim="Guruh = 8 − 1 = 7 → 7 valent e (galogen).",
      parametrlar=dict(arch="hr_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Magniyning oliy oksidi molyar massasini toping. (M(Mg)=24)",
      javob="40", yechim="MgO: 24 + 16 = 40 g/mol.",
      parametrlar=dict(arch="mgo_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="9,4 g K₂O necha mol bo'ladi? (M(K₂O)=94)",
      javob="0,1", yechim="n = 9,4/94 = 0,1 mol.",
      parametrlar=dict(arch="k2o_o1")),
]

# ---------- O2 ----------
check("o41c", 0.1*40, 4)
check("o43b", 0.2*56, 11.2)
O2 = [
 dict(n=41, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Natriy elementi haqida bandlar ketma-ket yechiladi — har biri keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) Na ning davriy sistemadagi o'rnini (davr, guruh) va buning atom tuzilishi bilan "
                   "bog'liqligini yozing.",
             yechim=["3-davr (3 qavat), I A (tashqi 1 e): 2, 8, 1."], M=3, A=2),
        dict(savol="b) Oliy oksidi va gidroksidini yozing, xarakterini ayting.",
             yechim=["Na₂O — asosli oksid; NaOH — kuchli ishqor."], M=3, A=2),
        dict(savol="c) 0,1 mol NaOH ning massasini toping. (M=40)",
             yechim=["m = 0,1·40 = 4 g."], M=3, A=2),
        dict(savol="d) Na ning suv bilan reaksiya tenglamasini yozing.",
             yechim=["2Na + 2H₂O → 2NaOH + H₂↑."], M=3, A=2),
        dict(savol="e) K natriyga qaraganda suv bilan faolroq reaksiyaga kirishadi. Sababini yozing.",
             yechim=["K radiusi katta — tashqi e osonroq beriladi (guruhda pastga faollik ortadi)."], M=3, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi element-zanjiri: o'rin → birikmalar → hisob → xossa; M15+A10.",
      parametrlar=dict(arch="na_zanjir_a")),
 dict(n=42, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Alyuminiy — «qanotli metall»: samolyotlar, folga, idishlar. Quyidagi savollarga MULOHAZA "
            "yuritib javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) Al ning davriy sistemadagi o'rni (3-davr, III A) undan qanday xossalarni kutishga "
                   "asos beradi? Metall-metallmas «chegarasi» tushunchasi orqali yoriting.",
             yechim=["Chap-o'rta hudud — metall, lekin chegaraga yaqin: birikmalari amfoter;",
                     "3 valent e → Al³⁺; yengil va faol metall."], M=13, A=0),
        dict(savol="b) Nega faol metall bo'lgan alyuminiy havoda va idish sifatida chidamli?",
             yechim=["Yuzasi zich Al₂O₃ parda bilan qoplanib, ichkarini himoya qiladi (passivlanish)."], M=9, A=0),
        dict(savol="c) Al(OH)₃ ning amfoterligi nimada namoyon bo'ladi?",
             yechim=["Ham kislota, ham ishqor bilan reaksiyaga kirishadi."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="al_mulohaza")),
 dict(n=43, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch elementning davriy sistemadagi o'rni jadvalda berilgan:\n"
            "[JADVAL] Element | davr | guruh ;; X | 2 | VI A ;; Y | 4 | II A ;; Z | 3 | VII A\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X, Y, Z elementlarni aniqlang.",
             yechim=["X — O (kislorod); Y — Ca; Z — Cl."], M=4, A=2),
        dict(savol="b) Y ning oliy oksidi 0,2 molining massasini toping.",
             yechim=["CaO (M=56): 0,2·56 = 11,2 g."], M=4, A=3),
        dict(savol="c) X va Y hosil qiladigan birikma formulasi va bog' turini yozing.",
             yechim=["CaO — ion bog'lanish (metall + metallmas)."], M=4, A=3),
        dict(savol="d) Z ning vodorodli birikmasi eritmasi qanday muhitga ega? Nomini yozing.",
             yechim=["HCl — xlorid kislota; kuchli kislotali muhit."], M=3, A=2),
      ],
      rasmiylashtirish="O'rin-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="orin_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260315)
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
    d = dict(n=n, tur="Y1", element="I.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I2-A", daraja="A", bob=2, bob_nomi="Davriy qonun va davriy sistema",
    manba=("MS spetsifikatsiyasi I.2; darslik davriy qonun bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (yod, geliy, folga, sut) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
