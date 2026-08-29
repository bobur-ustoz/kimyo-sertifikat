# -*- coding: utf-8 -*-
"""13-bob A-varianti: IA guruh metallari (II.3) — O'RGATUVCHI ★★.
Hayotiy sahnalar: sariq ko'cha chiroqi, kerosindagi natriy, muzli yo'lga tuz, kaliyli o'g'it."""
import json, random

OUT = "mavzu_II3A.json"
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
  "IA guruh (ishqoriy) metallari atomlarining tashqi qavatida nechta elektron bor?",
  "1", [("2", "bu IIA guruh"), ("7", "bu VII A — galogenlar"), ("8", "bu inert gazlar")],
  "ns¹ — bitta valent elektron; shu bois ular +1 zaryadli ion beradi.",
  dict(arch="tashqi_e"))

# 2 (2)
q(2, "quyi",
  "IA guruhda yuqoridan pastga (Li → Na → K → Rb → Cs) metallik faolligi qanday o'zgaradi?",
  "ortadi", [("kamayadi", "radius ortgani sari e oson beriladi"), ("o'zgarmaydi", "radius o'zgaradi-ku"),
              ("avval ortib, keyin kamayadi", "monoton ortadi")],
  "Radius kattalashadi → tashqi elektron yadrodan uzoq → osonroq beriladi.",
  dict(arch="faollik_yonalish"))

# 3 (2)
q(2, "o'rta",
  "Natriy metali laboratoriyada qanday saqlanadi?",
  "kerosin ostida", [("suv ostida", "suv bilan portlab reaksiyaga kirishadi!"),
                      ("ochiq havoda", "havoda tez oksidlanadi"),
                      ("spirt ichida", "spirt bilan ham reaksiyaga kirishadi")],
  "Kerosin havodagi O₂ va namlikdan himoya qiladi.",
  dict(arch="na_saqlash"))

# 4 (2) — SAHNA: ko'cha chiroqi
q(2, "o'rta",
  "Rasmda tungi yo'ldagi TO'Q SARIQ chiroqlar: ular natriy bug'ili lampalar. Sariq rang qayerdan "
  "keladi?",
  "qo'zg'algan natriy atomlari o'ziga xos sariq nur taratadi",
  [("lampa shishasi sariq bo'yalgan", "rang Na atomlarining nuridan"),
   ("lampada olov yonadi", "yonish yo'q — elektr razryad"),
   ("sariq gaz — xlor bor", "xlor lampada ishlatilmaydi")],
  "Elektr toki Na atomlarini qo'zg'atadi; qaytishda 589 nm li sariq nur chiqadi — alanga testidagi rang.",
  dict(arch="chiroq_sahna"), fig="streetlamp")

# 5 (2)
q(2, "o'rta",
  "Natriy suv bilan reaksiyaga kirishganda qanday moddalar hosil bo'ladi?",
  "NaOH va H₂", [("Na₂O va H₂", "suvli muhitda gidroksid hosil bo'ladi"),
                  ("NaH va O₂", "kislorod ajralmaydi"),
                  ("faqat NaOH", "vodorod ham ajraladi")],
  "2Na + 2H₂O → 2NaOH + H₂↑ — shiddatli, issiqlik bilan.",
  dict(arch="na_suv"))

# 6 (2)
q(2, "quyi",
  "Ishqoriy metallarning qattiqligi haqida qaysi fikr to'g'ri?",
  "yumshoq — pichoq bilan kesiladi",
  [("juda qattiq — olmosdek", "aksincha, eng yumshoq metallar"),
   ("mo'rt — chinniday sinadi", "ular plastik, mo'rt emas"),
   ("kesib bo'lmaydi", "laboratoriyada pichoq bilan kesiladi")],
  "Metall panjarasi bo'sh — Na, K yangi kesilganda kumushdek yaltiraydi.",
  dict(arch="yumshoqlik"))

# 7 (2)
q(2, "quyi",
  "IA guruh metallari nega «ishqoriy metallar» deb ataladi?",
  "suv bilan reaksiyada ishqor hosil qilgani uchun",
  [("ishqorlarda erigani uchun", "metall ishqorda erimaydi"),
   ("achchiq ta'mi uchun", "metallar tatib ko'rilmaydi"),
   ("ishqor rangida bo'lgani uchun", "ishqorning rangi yo'q")],
  "Me + H₂O → MeOH (ishqor) + H₂ — nomi shu xossadan.",
  dict(arch="nom_sababi"))

# 8 (2) — SAHNA: kerosindagi natriy
q(2, "o'rta",
  "Rasmda kerosinli bankada saqlanayotgan natriy bo'laklari. Nega natriyni OCHIQ havoda qoldirib "
  "bo'lmaydi?",
  "havo kislorodi va namlik bilan tez reaksiyaga kirishib buziladi",
  [("bug'lanib ketadi", "metall xona haroratida bug'lanmaydi"),
   ("rangini yo'qotadi, xolos", "gap faqat rangda emas — modda o'zgaradi"),
   ("changga aylanadi", "mexanik emas, kimyoviy o'zgarish")],
  "Yangi kesim havoda darrov xiralashadi: oksid/gidroksid/karbonat qatlami hosil bo'ladi.",
  dict(arch="kerosin_sahna"), fig="kerosene")

# 9 (2)
q(2, "o'rta",
  "Alanga testida natriy va kaliy qanday ranglar beradi?",
  "Na — sariq, K — binafsha",
  [("Na — binafsha, K — sariq", "teskari"), ("ikkalasi ham qizil", "qizil — Li, Sr"),
   ("ikkalasi ham yashil", "yashil — Cu, Ba")],
  "Alanga ranglari — IA metallarni farqlashning eng oson usuli.",
  dict(arch="alanga_ranglar"))

# 10 (3)
check("q10", 4.6/23/2*22.4, 2.24)
q(3, "o'rta",
  "2Na + 2H₂O → 2NaOH + H₂. 4,6 g natriy suv bilan reaksiyaga kirishganda ajralgan vodorod hajmini "
  "(n.sh.) toping. (M(Na)=23)",
  "2,24 L", [("4,48 L", "koeffitsiyent: H₂ ikki barobar kam"), ("22,4 L", "1 mol uchun"),
              ("1,12 L", "yana ikkiga bo'lingan")],
  "n(Na) = 0,2 mol → n(H₂) = 0,1 mol → V = 2,24 L.",
  dict(arch="na_h2_hisob"))

# 11 (2)
q(2, "o'rta",
  "NaOH ning texnik nomi qaysi?",
  "kaustik soda (o'yuvchi natriy)",
  [("ichimlik sodasi", "u — NaHCO₃"), ("kir sodasi", "u — Na₂CO₃"), ("potash", "u — K₂CO₃")],
  "«Kaustik» — kuydiruvchi: teri va matolarni yemiradi.",
  dict(arch="naoh_nom"))

# 12 (3)
check("q12", 0.5*138, 69)
q(3, "o'rta",
  "0,5 mol potash (K₂CO₃) necha gramm bo'ladi? (M(K₂CO₃)=138)",
  "69 g", [("138 g", "1 mol uchun"), ("34,5 g", "chorak olingan"), ("276 g", "ikki baravar")],
  "m = 0,5 · 138 = 69 g.",
  dict(arch="potash_massa"))

# 13 (2) — SAHNA: muzli yo'l
q(2, "o'rta",
  "Rasmda qishda muzlagan yo'lga tuz sepilmoqda. Osh tuzi muzni nega eritadi?",
  "tuz eritmasining muzlash harorati toza suvnikidan past",
  [("tuz muz bilan reaksiyaga kirishib issiqlik beradi", "kimyoviy reaksiya bormaydi"),
   ("tuz muzni qirib tashlaydi", "mexanik emas — fizik-kimyoviy hodisa"),
   ("tuz quyosh nurini tortadi", "kechasi ham ishlaydi-ku")],
  "NaCl + muz aralashmasi −21 °C gacha suyuq qoladi — muz «eriydi».",
  dict(arch="muzyol_sahna"), fig="icyroad")

# 14 (3)
q(3, "o'rta",
  "«Ichimlik sodasi» va «kir sodasi» mos ravishda qaysi moddalar?",
  "NaHCO₃ va Na₂CO₃",
  [("Na₂CO₃ va NaHCO₃", "teskari"), ("NaOH va NaCl", "bular soda emas"),
   ("K₂CO₃ va KOH", "kaliy birikmalari soda deb atalmaydi")],
  "NaHCO₃ — oshxonada; Na₂CO₃ — kir yuvishda ishlatilgan.",
  dict(arch="sodalar_farqi"))

# 15 (2)
q(2, "o'rta",
  "Litiy haqida qaysi fikr TO'G'RI?",
  "eng yengil metall — zamonaviy akkumulyatorlarda ishlatiladi",
  [("eng og'ir metall", "aksincha — zichligi 0,53 g/sm³"),
   ("suyuq metall", "suyuq metall — simob"),
   ("radioaktiv metall", "tabiiy Li barqaror")],
  "Li-ion batareyalar: telefondan elektromobilgacha.",
  dict(arch="litiy_fakt"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Element | Alanga rangi ;; Na | ? ;; K | ? ;; Li | qizil",
  "sariq; binafsha",
  [("binafsha; sariq", "teskari"), ("yashil; qizil", "yashil IA ga xos emas"),
   ("sariq; sariq", "K — binafsha")],
  "Na — sariq, K — binafsha, Li — qirmizi-qizil.",
  dict(arch="alanga_jadval"))

# 17 (2)
q(2, "o'rta",
  "IA metallarning tuzlari suvda qanday eriydi?",
  "deyarli barchasi yaxshi eriydi",
  [("hech biri erimaydi", "eruvchanlik jadvalida Na⁺, K⁺ ustunlari to'liq «E»"),
   ("faqat xloridlari eriydi", "karbonat, sulfat, nitratlari ham eriydi"),
   ("faqat issiq suvda eriydi", "sovuqda ham eriydi")],
  "Na⁺ va K⁺ tuzlari — eruvchanlik jadvalining «muammosiz» qatorlari.",
  dict(arch="tuz_eruvchanlik"))

# 18 (2) — SAHNA: kaliyli o'g'it
q(2, "o'rta",
  "Rasmda «Kaliy xlorid» yozuvli o'g'it qopi. O'simliklarga kaliy nima uchun kerak?",
  "hosil pishishi va o'simlikning qurg'oqchilik-sovuqqa chidamliligi uchun",
  [("faqat rang berish uchun", "kaliy fiziologik jarayonlarda qatnashadi"),
   ("zararkunandalarni qo'rqitish uchun", "o'g'it insektitsid emas"),
   ("tuproqni yumshatish uchun", "mexanik emas, oziqlanish elementi")],
  "K — o'simlikning uch asosiy oziq elementidan biri (N, P, K).",
  dict(arch="ogit_sahna"), fig="potash")

# 19 (3)
check("q19", 0.3*40, 12)
q(3, "o'rta",
  "0,3 mol natriy gidroksidning massasini toping. (M(NaOH)=40)",
  "12 g", [("40 g", "1 mol uchun"), ("6 g", "yarmi olingan"), ("24 g", "ikki baravar")],
  "m = 0,3 · 40 = 12 g.",
  dict(arch="naoh_massa"))

# 20 (2)
q(2, "o'rta",
  "Ishqoriy metallar tabiatda qanday holda uchraydi?",
  "faqat birikmalar holida",
  [("sof metall holida", "juda faol — darrov reaksiyaga kirishadi"),
   ("faqat gaz holida", "ular qattiq metallar"),
   ("umuman uchramaydi", "NaCl, KCl konlari juda ko'p")],
  "Faolligi tufayli erkin holda saqlanolmaydi: NaCl, silvin KCl va h.k.",
  dict(arch="tabiatda"))

# 21 (3)
q(3, "o'rta",
  "Bir xil sharoitda natriy va kaliy suv bilan reaksiyaga kiritilsa, qaysi biri SHIDDATLIROQ "
  "reaksiyaga kirishadi?",
  "K — hattoki ajralgan vodorod alangalanadi",
  [("Na — u faolroq", "guruhda pastga faollik ortadi: K > Na"),
   ("ikkalasi bir xil", "faollik farqi aniq ko'rinadi"),
   ("hech biri kirishmaydi", "ikkalasi ham shiddatli kirishadi")],
  "K faolroq: reaksiya issiqligi H₂ ni yondiradi (binafsha alanga).",
  dict(arch="na_k_shiddat"))

# 22 (2)
q(2, "o'rta",
  "Na₂O suv bilan reaksiyaga kirishganda nima hosil bo'ladi?",
  "NaOH", [("NaH", "gidrid suvdan hosil bo'lmaydi"), ("Na₂O₂", "peroksid yonishda hosil bo'ladi"),
            ("Na", "oksiddan metall ajralmaydi")],
  "Na₂O + H₂O → 2NaOH — asosli oksid + suv → ishqor.",
  dict(arch="na2o_suv"))

# 23 (3)
check("q23", 7.8/39/2*22.4, 2.24)
q(3, "o'rta",
  "2K + 2H₂O → 2KOH + H₂. 7,8 g kaliy suvga tashlanganda ajralgan vodorod hajmini (n.sh.) toping. "
  "(M(K)=39)",
  "2,24 L", [("4,48 L", "H₂ koeffitsiyenti unutilgan"), ("22,4 L", "1 mol uchun"),
              ("11,2 L", "hisob xato")],
  "n(K) = 0,2 mol → n(H₂) = 0,1 mol → V = 2,24 L.",
  dict(arch="k_h2_hisob"))

# 24 (2)
q(2, "quyi",
  "Qaysi modda «ichimlik sodasi» nomi bilan sotiladi?",
  "NaHCO₃", [("Na₂CO₃", "bu kir soda"), ("NaOH", "o'yuvchi — oziq-ovqatga mumkin emas"),
              ("NaCl", "bu osh tuzi")],
  "Natriy gidrokarbonat — xamir ko'pchitgich, me'da uchun vosita.",
  dict(arch="ichimlik_soda"))

# 25 (3)
q(3, "o'rta",
  "Genetik qatordagi X moddani aniqlang: Na → NaOH → X → NaCl (X karbonatlar sinfidan).",
  "Na₂CO₃", [("Na₂O", "oksid NaOH dan KEYIN kelmaydi — u NaOH dan oldingi bosqich"),
              ("NaNO₃", "nitrat karbonat emas"), ("Na₂SO₄", "sulfat ham emas")],
  "NaOH + CO₂ → Na₂CO₃; Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂.",
  dict(arch="genetik_na"))

# 26 (3) — RASMLI: suyuqlanish grafigi
q(3, "o'rta",
  "Grafikda IA metallarining suyuqlanish haroratlari berilgan. Qaysi metall ENG OSON suyuqlanadi?",
  "Cs", [("Li", "aksincha — eng yuqori harorat (181 °C)"), ("Na", "98 °C — o'rtada"),
          ("K", "64 °C — Cs dan yuqori")],
  "Grafikdan: guruhda pastga suyuqlanish harorati pasayadi — Cs ≈ 28 °C.",
  dict(arch="suyuqlanish_oqish"), fig="melting")

# 27 (3)
q(3, "o'rta",
  "Sof natriy metali sanoatda qanday olinadi?",
  "suyuqlantirilgan NaCl ni elektroliz qilib",
  [("NaCl eritmasidan temir bilan siqib chiqarib", "Na har qanday metalldan faol"),
   ("NaOH ni qizdirib", "ishqor metallga parchalanmaydi"),
   ("tabiiy konlardan qazib", "tabiatda sof Na yo'q")],
  "2NaCl (suyuql.) → elektroliz → 2Na (katodda) + Cl₂ (anodda).",
  dict(arch="na_olinish"))

# 28 (2) — RASMLI: grafik o'qish
q(2, "o'rta",
  "26-savol grafigidan: qaysi ishqoriy metallning suyuqlanish harorati ENG YUQORI?",
  "Li", [("Cs", "eng past (28 °C)"), ("K", "64 °C"), ("Rb", "39 °C")],
  "Li — 181 °C: guruh boshida eng «chidamli».",
  dict(arch="suyuqlanish_max"), fig="melting")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "IA guruhda yuqoridan pastga suv bilan reaksiya SHIDDATI qanday o'zgaradi? Grafikni tanlang.",
  "ortib boradi",
  [("kamayadi", "faollik pastga ortadi"), ("o'zgarmaydi", "Li bilan Cs farqi juda katta"),
   ("avval ortib, so'ng kamayadi", "monoton ortadi")],
  "Li — sekin, Na — yugurib, K — alanga bilan, Rb/Cs — portlash bilan.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="rise_fall", xlab="Li→Cs", ylab="shiddat"),
  params=dict(arch="shiddat_grafik"))

# 30 (2)
q(2, "o'rta",
  "Natriy bilan ishlashda qaysi xavfsizlik qoidasi SHART?",
  "pinset bilan olish, suvdan uzoq tutish, ko'zoynak taqish",
  [("qo'lda ushlab kesish", "teridagi nam bilan reaksiyaga kirishadi — kuyish!"),
   ("suvda yuvib ishlatish", "suv bilan portlaydi"),
   ("og'izda saqlash", "qat'iyan taqiqlanadi")],
  "Na terining namligi bilan ham ishqor hosil qiladi — faqat pinset va quruq asboblar.",
  dict(arch="na_xavfsizlik"))

# 31 (3)
check("q31", 5.3/106*22.4, 1.12)
q(3, "o'rta",
  "Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂. 5,3 g kir soda kislota bilan to'liq reaksiyaga kirishganda "
  "ajralgan gaz hajmini (n.sh.) toping. (M(Na₂CO₃)=106)",
  "1,12 L", [("2,24 L", "0,1 mol deb olingan"), ("22,4 L", "1 mol uchun"), ("0,56 L", "yarmi")],
  "n = 5,3/106 = 0,05 mol → V(CO₂) = 1,12 L.",
  dict(arch="soda_hcl_hisob"))

# 32 (3) — RASMLI: grafik hisob
check("q32", 98-64, 34)
q(3, "o'rta",
  "26-savol grafigidan foydalanib, natriy va kaliy suyuqlanish haroratlari FARQINI toping.",
  "34 °C", [("62 °C", "bu boshqa juftlikning farqi"), ("98 °C", "bu Na ning o'zi"),
             ("134 °C", "yig'indini emas, farqni so'rayapti")],
  "98 − 64 = 34 °C.",
  dict(arch="suyuqlanish_farq"), fig="melting")

# ---------- Y2: oshxona-lab ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.3",
  ichki_pasport=[dict(n=33, element="II.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="II.3", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="II.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch idishda oq moddalar bor: X — osh tuzi, Y — ichimlik sodasi, Z — o'yuvchi natriy "
               "donachalari. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Y ga sirka tomizilsa nima kuzatiladi?",
    "34. Z ning eritmasida fenolftalein qanday rang oladi?",
    "35. X ning alanga testidagi rangi qanday?"],
  javoblar_royxati=["A) gaz pufakchalari", "B) pushti", "C) sariq", "D) o'zgarish yo'q",
                    "E) rangsiz qoladi", "F) binafsha"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="NaHCO₃ + kislota CO₂ beradi — o'zgarish bor"),
                   dict(variant="E", xato="NaOH kuchli ishqor — fenolftalein pushti bo'ladi"),
                   dict(variant="F", xato="binafsha — kaliy; NaCl da natriy bor")],
  yechim=("Y: NaHCO₃ + CH₃COOH → CO₂↑ (A). Z: NaOH — pushti (B). X: Na — sariq alanga (C)."),
  parametrlar=dict(arch="oq_moddalar_ssenariy"))

# ---------- O1 ----------
check("o36", 0.1*40, 4)
check("o37", 9.2/23, 0.4)
check("o38", 10.6/106*22.4, 2.24)
check("o39", 9.4/94*2*56, 11.2)
check("o40", 0.15/2*22.4, 1.68)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,1 mol natriy gidroksidning massasini (g) toping. (M(NaOH)=40)",
      javob="4", yechim="m = 0,1·40 = 4 g.",
      parametrlar=dict(arch="naoh_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="9,2 g natriy necha mol bo'ladi? (M(Na)=23)",
      javob="0,4", yechim="n = 9,2/23 = 0,4 mol.",
      parametrlar=dict(arch="na_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="10,6 g Na₂CO₃ ortiqcha kislota bilan reaksiyaga kirishganda ajralgan CO₂ hajmini "
            "(n.sh., L) toping. (M(Na₂CO₃)=106)",
      javob="2,24", yechim="n = 0,1 mol → V = 2,24 L.",
      parametrlar=dict(arch="soda_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="K₂O + H₂O → 2KOH. 9,4 g kaliy oksididan olingan ishqor massasini (g) toping. "
            "(M: K₂O=94, KOH=56)",
      javob="11,2", yechim="n = 0,1 mol → KOH 0,2 mol → 11,2 g.",
      parametrlar=dict(arch="k2o_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="0,15 mol natriy suv bilan reaksiyaga kirishganda ajralgan vodorod hajmini (n.sh., L) toping.",
      javob="1,68", yechim="n(H₂) = 0,075 mol → V = 0,075·22,4 = 1,68 L.",
      parametrlar=dict(arch="na_h2_o1")),
]

# ---------- O2 ----------
check("o41b", 2.3/23/2*22.4, 1.12)
check("o41c", 0.1*40, 4)
O2 = [
 dict(n=41, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("2,3 g natriy suvga tashlandi. Bandlar ketma-ket yechiladi — har biri keyingisiga asos "
            "bo'ladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing va kuzatiladigan hodisalarni tavsiflang.",
             yechim=["2Na + 2H₂O → 2NaOH + H₂↑; metall suv yuzasida yugurib eriydi, gaz ajraladi."], M=4, A=2),
        dict(savol="b) Ajralgan vodorod hajmini (n.sh.) hisoblang.",
             yechim=["n(Na) = 0,1 mol → n(H₂) = 0,05 → V = 1,12 L."], M=4, A=3),
        dict(savol="c) Hosil bo'lgan ishqor massasini toping.",
             yechim=["n(NaOH) = 0,1 mol → m = 4 g."], M=4, A=3),
        dict(savol="d) Eritmaga fenolftalein tomizilsa nima kuzatiladi? Sababini yozing.",
             yechim=["Pushti rang — eritmada NaOH (ishqoriy muhit) bor."], M=3, A=2),
      ],
      rasmiylashtirish="Na-suv zanjiri: tenglama → gaz → ishqor → indikator; M15+A10.",
      parametrlar=dict(arch="na_suv_zanjir")),
 dict(n=42, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Ishqoriy metallar bilan ishlash qoidalari o'rganilmoqda. Quyidagilarga MULOHAZA yuritib "
            "javob yozing."),
      bandlar=[
        dict(savol="a) Nega ishqoriy metallar tabiatda faqat birikma holida uchraydi va laboratoriyada "
                   "kerosin ostida saqlanadi? Ikkala faktni bitta xossa orqali bog'lab tushuntiring.",
             yechim=["Sabab bitta — o'ta yuqori faollik: havo, suv, hatto namlik bilan darhol reaksiyaga",
                     "kirishadi. Tabiatda hamma «erkin» atomlar allaqachon birikkan; kerosin esa havo/namdan to'sadi."], M=13, A=0),
        dict(savol="b) Nega kesilgan natriy bo'lagining yuzasi bir necha soniyada xiralashadi?",
             yechim=["Yuzada Na₂O, NaOH, so'ng Na₂CO₃ pardasi hosil bo'ladi (havo O₂, H₂O, CO₂ bilan)."], M=9, A=0),
        dict(savol="c) Rb va Cs qanday idishlarda saqlanadi?",
             yechim=["Vakuumlangan shisha ampulalarda — ular kerosin ostida ham xavfli darajada faol."], M=3, A=0),
      ],
      rasmiylashtirish="Faollik-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="faollik_mulohaza")),
 dict(n=43, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch «oq modda» jadvalda solishtiriladi:\n"
            "[JADVAL] Modda | Formula ;; osh tuzi | NaCl ;; ichimlik sodasi | NaHCO₃ ;; "
            "o'yuvchi natriy | NaOH\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir moddaning sinfini aniqlang.",
             yechim=["NaCl — o'rta tuz; NaHCO₃ — nordon tuz; NaOH — asos (ishqor)."], M=4, A=2),
        dict(savol="b) Qaysilari xlorid kislota bilan reaksiyaga kirishadi? Tenglamalarini yozing.",
             yechim=["NaHCO₃ + HCl → NaCl + H₂O + CO₂↑; NaOH + HCl → NaCl + H₂O. NaCl kirishmaydi."], M=4, A=3),
        dict(savol="c) Qaysi birini qizdirish o'zgartiradi? Tenglama yozing.",
             yechim=["2NaHCO₃ → Na₂CO₃ + H₂O + CO₂ (NaCl va NaOH termik barqaror)."], M=4, A=3),
        dict(savol="d) Uchchala eritmani indikatorlar yordamida qanday farqlash mumkin?",
             yechim=["NaOH — fenolftalein pushti; NaHCO₃ — kuchsiz ishqoriy (lakmus ko'kish); NaCl — neytral."], M=3, A=2),
      ],
      rasmiylashtirish="Oq moddalar jadvali: sinf → reaksiya → qizdirish → indikator; M15+A10.",
      parametrlar=dict(arch="oq_moddalar_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261303)
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
    d = dict(n=n, tur="Y1", element="II.3", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II3-A", daraja="A", bob=13, bob_nomi="IA guruh metallari",
    manba=("MS spetsifikatsiyasi II.3; 9-sinf darslik ishqoriy metallar bo'limi — savollar yangi "
           "tuzilgan, hayotiy sahnalar (ko'cha chiroqi, kerosin, muzli yo'l, kaliyli o'g'it) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
