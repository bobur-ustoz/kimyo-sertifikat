# -*- coding: utf-8 -*-
"""Organik 5-bob A-varianti: Aldegidlar va ketonlar (III.5) — O'RGATUVCHI ★★.
Hayotiy sahnalar: muzey preparati (formalin), lak ketkazuvchi (aseton), fanera yelimi, termos ko'zgusi."""
import json, random

OUT = "mavzu_III5A.json"
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
  "Aldegidlarning funksional guruhi qaysi?",
  "–CHO (aldegid guruhi)", [("–OH", "u spirtlarda"), ("–COOH", "u karbon kislotalarda"),
                             ("–O–", "u efirlarda")],
  "Karbonil C=O ga bitta H birikkan: R–CHO.",
  dict(arch="cho_guruh"))

# 2 (2)
q(2, "quyi",
  "Ketonlarda karbonil guruh (C=O) qanday joylashgan?",
  "ikkita uglevodorod radikali orasida",
  [("zanjir oxirida", "u holda aldegid bo'lardi"),
   ("benzol halqasida", "bu fenolga o'xshash gap"),
   ("kislorod bilan zanjir orasida", "u efir bog'i")],
  "R–CO–R′: shuning uchun keton oksidlanishga chidamli.",
  dict(arch="keton_tuzilish"))

# 3 (2)
q(2, "quyi",
  "Eng oddiy aldegid qaysi?",
  "metanal HCHO", [("etanal CH₃CHO", "u ikkinchi vakil"), ("aseton", "u keton"),
                    ("metanol", "u spirt")],
  "Formaldegid — bitta ugleroddan iborat aldegid.",
  dict(arch="metanal"))

# 4 (2) — SAHNA: muzey
q(2, "o'rta",
  "Rasmda muzeydagi biologik preparat: banka «formalin» bilan to'ldirilgan. Preparat nega yillar "
  "davomida buzilmaydi?",
  "formaldegid oqsillarni qotiradi va mikroblarni nobud qiladi",
  [("banka havo o'tkazmaydi, xolos", "asosiy ish — kimyoda"),
   ("formalin muzlatib qo'yadi", "harorat oddiy"),
   ("preparat tuzlangan", "tuz emas, aldegid eritmasi")],
  "HCHO oqsil molekulalarini «tikib» qo'yadi — chirish to'xtaydi.",
  dict(arch="muzey_sahna"), fig="museum")

# 5 (2)
q(2, "quyi",
  "Sirka aldegidining (etanalning) formulasi qaysi?",
  "CH₃CHO", [("HCHO", "u metanal"), ("CH₃COCH₃", "u aseton"), ("C₂H₅OH", "u etanol")],
  "Ikki uglerodli aldegid.",
  dict(arch="etanal_formula"))

# 6 (2)
q(2, "o'rta",
  "IUPAC bo'yicha aldegidlar va ketonlar nomiga qanday qo'shimcha qo'shiladi?",
  "aldegidga «-al», ketonga «-on»",
  [("ikkalasiga «-ol»", "u spirtlar qo'shimchasi"),
   ("aldegidga «-on», ketonga «-al»", "teskari"),
   ("ikkalasiga «-an»", "u alkanlar")],
  "Masalan: etanAL, propanON.",
  dict(arch="al_on_nom"))

# 7 (2)
q(2, "o'rta",
  "«Kumush ko'zgu» reaksiyasi qaysi sinf moddalarga xos sifat reaksiyasi?",
  "aldegidlarga", [("ketonlarga", "ular Ag₂O bilan reaksiyaga kirishmaydi"),
                    ("spirtlarga", "ularga CuO sinovi mos"),
                    ("alkanlarga", "ular juda sust")],
  "R–CHO + Ag₂O (ammiakli) → R–COOH + 2Ag↓ — devorda ko'zgu.",
  dict(arch="kumush_kozgu"))

# 8 (2) — SAHNA: lak ketkazuvchi
q(2, "o'rta",
  "Rasmda tirnoq lakini ketkazuvchi suyuqlik: asosi — aseton. U lakni qanday «yengadi»?",
  "lak qatlamini eritib yuboradi — kuchli organik erituvchi",
  [("lak bilan reaksiyaga kirishib gaz beradi", "kimyoviy emas, fizik jarayon"),
   ("lakni kuydiradi", "hech narsa yonmaydi"),
   ("faqat namlaydi", "suvdan farqi ham shu — eritadi")],
  "Aseton ko'p organik moddalarni yaxshi eritadi va tez bug'lanadi.",
  dict(arch="lak_sahna"), fig="nailpolish")

# 9 (2)
q(2, "o'rta",
  "Aseton qaysi sinfga mansub va IUPAC nomi qanday?",
  "keton; propanon", [("aldegid; propanal", "aseton zanjir o'rtasida C=O tutadi"),
                       ("spirt; propanol", "OH guruhi yo'q"),
                       ("efir; metoksietan", "C–O–C bog'i yo'q")],
  "CH₃–CO–CH₃ — eng oddiy keton.",
  dict(arch="aseton_sinf"))

# 10 (3)
check("q10", 8.8/44, 0.2)
q(3, "o'rta",
  "8,8 g sirka aldegidi necha mol bo'ladi? (M(CH₃CHO)=44)",
  "0,2", [("2", "gramm-mol adashuvi"), ("0,1", "yarmi"), ("0,4", "ikki baravar")],
  "n = 8,8/44 = 0,2 mol.",
  dict(arch="etanal_mol"))

# 11 (2)
q(2, "o'rta",
  "Kucherov reaksiyasida atsetilenga suv biriktirilganda nima hosil bo'ladi?",
  "sirka aldegidi CH₃CHO", [("etanol", "alkenga suv qo'shilsa spirt bo'lardi"),
                              ("etan", "bu gidrogenlash"),
                              ("sirka kislota", "u keyingi oksidlanish bosqichi")],
  "C₂H₂ + H₂O →(Hg²⁺) CH₃CHO.",
  dict(arch="kucherov"))

# 12 (3)
check("q12", 30, 30)
q(3, "o'rta",
  "Molyar massasi 30 g/mol bo'lgan aldegidni aniqlang.",
  "metanal HCHO", [("etanal", "M = 44"), ("propanal", "M = 58"), ("metanol", "u spirt, M = 32")],
  "12 + 2 + 16 = 30.",
  dict(arch="m30"))

# 13 (2) — SAHNA: fanera
q(2, "o'rta",
  "Rasmda fanera qatlamlari: ular fenol-formaldegid smola bilan yelimlangan. Bu smolaning "
  "afzalligi nimada?",
  "qotgach issiqqa va namga chidamli, mustahkam bo'ladi",
  [("suvda oson eriydi", "aksincha, suvga chidamli"),
   ("past haroratda eriydi", "termoreaktiv — qayta erimaydi"),
   ("elektr tokini o'tkazadi", "u izolyator")],
  "Fenol + HCHO → to'rsimon polimer: fanera, DSP, elektr rozetkalar.",
  dict(arch="fanera_sahna"), fig="plywood")

# 14 (2)
q(2, "o'rta",
  "Aldegid vodorod bilan qaytarilganda qaysi sinf moddasi hosil bo'ladi?",
  "birlamchi spirt", [("karbon kislota", "u oksidlanish mahsuloti"),
                       ("keton", "keton boshqa yo'l bilan"),
                       ("alkan", "C=O butunlay uzilmaydi")],
  "R–CHO + H₂ → R–CH₂OH (katalizator Ni).",
  dict(arch="qaytarilish"))

# 15 (3)
check("q15", 0.1*2*108, 21.6)
q(3, "o'rta",
  "0,1 mol etanal «kumush ko'zgu» reaksiyasiga to'liq kirishganda ajralgan kumush massasini "
  "toping. (M(Ag)=108)",
  "21,6 g", [("10,8 g", "koeffitsiyent 2 unutildi"), ("43,2 g", "ikki baravar ko'p"),
              ("5,4 g", "hisob xato")],
  "1 mol aldegid → 2 mol Ag: m = 0,2·108 = 21,6 g.",
  dict(arch="ag_hisob"))

# 16 (2)
q(2, "o'rta",
  "Aldegid yangi cho'ktirilgan Cu(OH)₂ bilan qizdirilganda nima kuzatiladi?",
  "qizil-g'isht rangli Cu₂O cho'kmasi tushadi",
  [("ko'k rang saqlanadi", "u ko'p atomli spirt belgisi"),
   ("binafsha rang", "u fenol-FeCl₃"),
   ("gaz ajraladi", "cho'kma reaksiyasi bu")],
  "R–CHO + 2Cu(OH)₂ → R–COOH + Cu₂O↓ + 2H₂O — ikkinchi sifat sinovi.",
  dict(arch="cu2o_sinov"))

# 17 (2)
q(2, "quyi",
  "Formalin nima?",
  "formaldegidning ~40 % li suvdagi eritmasi",
  [("sof suyuq formaldegid", "HCHO — gaz, eritma ishlatiladi"),
   ("asetonning eritmasi", "aseton alohida modda"),
   ("spirt-suv aralashmasi", "spirt emas, aldegid")],
  "Dezinfeksiya va preparatlar saqlash uchun ishlatiladi.",
  dict(arch="formalin"))

# 18 (2) — SAHNA: termos
q(2, "o'rta",
  "Rasmda termos kolbasi kesimi: ichki shisha devor yaltiroq kumush qatlam bilan qoplangan. "
  "Bu qatlam qanday reaksiya bilan hosil qilinadi?",
  "aldegid yordamida «kumush ko'zgu» reaksiyasi bilan",
  [("kumushni eritib quyish bilan", "shisha bunga chidamaydi"),
   ("elektroliz bilan", "shisha tok o'tkazmaydi"),
   ("kumush bo'yoq surtish bilan", "bo'yoq emas, kimyoviy cho'kma")],
  "Ammiakli Ag₂O eritmasi + glyukoza/aldegid → tekis Ag qatlami; u issiqlik nurini qaytaradi.",
  dict(arch="termos_sahna"), fig="thermos")

# 19 (3)
check("q19", 4.4/44*2*22.4, 4.48)
q(3, "o'rta",
  "2CH₃CHO + 5O₂ → 4CO₂ + 4H₂O. 4,4 g etanal yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping.",
  "4,48 L", [("2,24 L", "koeffitsiyent 2 unutildi"), ("22,4 L", "1 mol uchun"),
              ("8,96 L", "ikki baravar ko'p")],
  "n = 0,1 mol → n(CO₂) = 0,2 mol → V = 4,48 L.",
  dict(arch="etanal_yonish"))

# 20 (2)
q(2, "o'rta",
  "Etanol qizdirilgan CuO ustidan o'tkazilganda qaysi aldegid hosil bo'ladi?",
  "sirka aldegidi (etanal)", [("metanal", "uglerod soni saqlanadi"),
                               ("propanal", "uglerod ortmaydi"),
                               ("benzaldegid", "halqa yo'q")],
  "C₂H₅OH + CuO → CH₃CHO + Cu + H₂O.",
  dict(arch="etanol_oksidlanish"))

# 21 (2)
q(2, "o'rta",
  "Nega aseton «kumush ko'zgu» reaksiyasini bermaydi?",
  "karbonil uglerodida vodorod yo'q — oson oksidlanmaydi",
  [("asetonda kislorod yo'q", "C=O bor-ku"),
   ("aseton gaz bo'lgani uchun", "u suyuqlik"),
   ("kumush bilan portlaydi", "bunday emas")],
  "Ketonlar yumshoq oksidlovchilarga chidamli — aldegiddan farqi shu.",
  dict(arch="keton_chidamli"))

# 22 (3)
check("q22", 0.5*30, 15)
q(3, "o'rta",
  "0,5 mol formaldegidning massasini toping. (M=30)",
  "15 g", [("30 g", "1 mol uchun"), ("7,5 g", "chorak mol"), ("60 g", "2 mol uchun")],
  "m = 0,5·30 = 15 g.",
  dict(arch="hcho_massa"))

# 23 (2)
q(2, "quyi",
  "Aseton kundalik hayotda asosan qanday ishlatiladi?",
  "laklar va bo'yoqlar uchun erituvchi sifatida",
  [("ichimlik sifatida", "zaharli!"),
   ("o'g'it sifatida", "azot-fosfor yo'q"),
   ("yoqilg'i qo'shimchasi sifatida faqat", "asosiy ishi — erituvchi")],
  "Tez bug'lanadi, ko'p organik moddani eritadi.",
  dict(arch="aseton_qollash"))

# 24 (2)
q(2, "o'rta",
  "Metanal xona haroratida qanday agregat holatda bo'ladi?",
  "gaz", [("suyuqlik", "qaynashi −19 °C"), ("qattiq", "juda past haroratda"),
           ("plazma", "bunday holat oddiy sharoitda yo'q")],
  "Shuning uchun u eritma — formalin ko'rinishida saqlanadi.",
  dict(arch="metanal_gaz"))

# 25 (3)
q(3, "o'rta",
  "Zanjirdagi X moddani aniqlang: C₂H₂ → X → C₂H₅OH.",
  "CH₃CHO", [("C₂H₄", "etilendan spirt to'g'ridan-to'g'ri olinadi, lekin bu Kucherov zanjiri"),
              ("CH₃COOH", "kislota spirtga qaytarilmaydi bu sharoitda"),
              ("C₂H₆", "etan inert")],
  "Kucherov: C₂H₂ + H₂O → CH₃CHO; so'ng CH₃CHO + H₂ → C₂H₅OH.",
  dict(arch="zanjir_x_5"))

# 26 (3) — RASMLI: bar o'qish
q(3, "o'rta",
  "Diagrammada formaldegid ishlatilish yo'nalishlari berilgan. Uning eng katta qismi qayerga "
  "sarflanadi?",
  "smolalar va plastmassalar olishga",
  [("dezinfeksiyaga", "ulushi ancha kichik"),
   ("preparat saqlashga", "eng kichik ulush"),
   ("hammasiga teng", "ustunlar teng emas")],
  "Diagrammada smolalar ustuni 65 % — qolganlaridan ancha baland.",
  dict(arch="bar_formalin_oqish"), fig="bar_formalin")

# 27 (3)
check("q27", 44, 44)
q(3, "o'rta",
  "Molyar massasi 44 g/mol bo'lgan to'yingan aldegidni aniqlang.",
  "etanal CH₃CHO", [("metanal", "M = 30"), ("propanal", "M = 58"),
                     ("karbonat angidrid", "CO₂ ham 44, lekin u aldegid emas")],
  "24 + 4 + 16 = 44.",
  dict(arch="m44"))

# 28 (2) — RASMLI: qaynash grafigi
q(2, "o'rta",
  "Grafikda aldegidlar qaynash haroratlari: metanal −19°, etanal 21°, propanal 49 °C. Qator "
  "bo'ylab qaynash qanday o'zgaradi?",
  "ortib boradi", [("kamayadi", "grafik ko'tarilyapti"), ("o'zgarmaydi", "nuqtalar har xil"),
                    ("tartibsiz", "monoton o'sish")],
  "Molekula kattalashgani sari molekulalararo tortishuv kuchayadi.",
  dict(arch="ald_bp_oqish"), fig="bp_ald")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Ochiq idishdagi aseton massasi vaqt o'tishi bilan qanday o'zgaradi? Grafikni tanlang.",
  "kamayib boradi",
  [("ortadi", "hech narsa qo'shilmayapti"), ("o'zgarmaydi", "aseton uchuvchan-ku"),
   ("avval ortib keyin kamayadi", "boshidanoq kamayadi")],
  "Aseton juda tez bug'lanadi — massa uzluksiz kamayadi.",
  svg=dict(correct="fall", d1="rise", d2="flat", d3="rise_fall", xlab="vaqt", ylab="m(aseton)"),
  params=dict(arch="buglanish_grafik_5"))

# 30 (2)
q(2, "o'rta",
  "Yangi mebel (DSP) ba'zan o'tkir hidli gaz ajratadi. Bu qaysi modda va nima qilish kerak?",
  "formaldegid; xonani tez-tez shamollatish kerak",
  [("aseton; hech narsa qilinmaydi", "hid formaldegiddan"),
   ("metan; gaz xizmatini chaqirish", "metan hidsiz"),
   ("kislorod; zarari yo'q", "kislorod hidsiz va foydali")],
  "Smoladan ajralgan HCHO — zaharli; shamollatish va sifatli mebel tanlash himoya qiladi.",
  dict(arch="dsp_xavf"))

# 31 (3)
check("q31", 4.4/44*46, 4.6)
q(3, "o'rta",
  "4,4 g etanal vodorod bilan to'liq qaytarilganda hosil bo'lgan etanol massasini toping. "
  "(M(C₂H₅OH)=46)",
  "4,6 g", [("9,2 g", "0,2 mol deb olindi"), ("2,3 g", "yarim hisob"), ("4,4 g", "M lar farq qiladi")],
  "n = 0,1 mol → m(spirt) = 0,1·46 = 4,6 g.",
  dict(arch="qaytarilish_hisob"))

# 32 (3) — RASMLI: bar hisob
check("q32", 200*0.65, 130)
q(3, "o'rta",
  "26-diagramma bo'yicha: zavod yiliga 200 ming tonna formaldegid ishlab chiqarsa, smolalarga "
  "necha ming tonna sarflanadi?",
  "130 ming t", [("65 ming t", "bu foizning o'zi"), ("70 ming t", "boshqa ustun olindi"),
                  ("200 ming t", "hammasi emas, 65 %i")],
  "m = 200·0,65 = 130 ming t.",
  dict(arch="bar_formalin_hisob"), fig="bar_formalin")

# ---------- Y2: uch idish ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.5",
  ichki_pasport=[dict(n=33, element="III.5", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="III.5", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="III.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch idishda uch suyuqlik bor: X — muzey preparatlarini saqlashda ishlatiladigan "
               "eritma; Y — tirnoq lakini ketkazuvchi erituvchi; Z — Kucherov reaksiyasining "
               "mahsuloti. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X suyuqlik qaysi?",
    "34. Y suyuqlik qaysi?",
    "35. Z ga ammiakli Ag₂O eritmasi qo'shib qizdirilsa nima kuzatiladi?"],
  javoblar_royxati=["A) formalin", "B) aseton", "C) probirka devorida kumush ko'zgu",
                    "D) etanol", "E) etanal", "F) qizil cho'kma tushmaydi, o'zgarish yo'q"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="etanol lak ketkazuvchi asosi emas"),
                   dict(variant="E", xato="Z ning o'zi etanal, lekin savol REAKSIYA natijasi haqida"),
                   dict(variant="F", xato="etanal aldegid — ko'zgu albatta hosil bo'ladi")],
  yechim=("X — formalin (A), Y — aseton (B). Z — etanal: Ag₂O bilan «kumush ko'zgu» beradi (C)."),
  parametrlar=dict(arch="uch_idish_ssenariy"))

# ---------- O1 ----------
check("o36", 0.3*58, 17.4)
check("o37", 6/30, 0.2)
check("o38", 0.2*2*108, 43.2)
check("o39", 11.2/22.4*44, 22)
check("o40", 0.25*22.4, 5.6)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,3 mol asetonning massasini (g) toping. (M=58)",
      javob="17,4", yechim="m = 0,3·58 = 17,4 g.",
      parametrlar=dict(arch="aseton_massa_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="6 g metanal necha mol bo'ladi? (M=30)",
      javob="0,2", yechim="n = 6/30 = 0,2 mol.",
      parametrlar=dict(arch="metanal_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="0,2 mol etanal «kumush ko'zgu» reaksiyasida ajratgan kumush massasini (g) toping. "
            "(M(Ag)=108)",
      javob="43,2", yechim="n(Ag) = 0,4 mol → m = 43,2 g.",
      parametrlar=dict(arch="ag_massa_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="11,2 L (n.sh.) atsetilen Kucherov reaksiyasiga to'liq kirishganda hosil bo'lgan "
            "etanal massasini (g) toping. (M=44)",
      javob="22", yechim="n = 0,5 mol → m = 0,5·44 = 22 g.",
      parametrlar=dict(arch="kucherov_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="HCHO + O₂ → CO₂ + H₂O. 0,25 mol metanal yonganda hosil bo'lgan CO₂ hajmini "
            "(n.sh., L) toping.",
      javob="5,6", yechim="n(CO₂) = 0,25 mol → V = 5,6 L.",
      parametrlar=dict(arch="metanal_yonish_o1")),
]

# ---------- O2 ----------
check("o41b", 8.8/44, 0.2); check("o41c", 0.4*108, 43.2)
check("o43a", 300*0.4, 120); check("o43b", 120/30, 4); check("o43c", 4*32, 128)
O2 = [
 dict(n=41, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada 8,8 g etanal bilan «kumush ko'zgu» tajribasi o'tkazildi. Bandlar "
            "ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing.",
             yechim=["CH₃CHO + Ag₂O →(NH₃) CH₃COOH + 2Ag↓."], M=4, A=2),
        dict(savol="b) Etanal mol miqdorini toping.",
             yechim=["n = 8,8/44 = 0,2 mol."], M=4, A=3),
        dict(savol="c) Ajralgan kumush massasini hisoblang.",
             yechim=["n(Ag) = 0,4 mol → m = 43,2 g."], M=4, A=3),
        dict(savol="d) Nega qatlam «ko'zgu» bo'lib tushadi? Izohlang.",
             yechim=["Ag sekin, tekis qaytariladi — shisha devorga yupqa yaltiroq parda bo'lib "
                     "o'tiradi."], M=3, A=2),
      ],
      rasmiylashtirish="Kumush ko'zgu: tenglama → mol → massa → izoh; M15+A10.",
      parametrlar=dict(arch="kozgu_zanjir_o2")),
 dict(n=42, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Aldegidlarning fizik xossalari tahlil qilinadi. Quyidagilarga MULOHAZA yuritib javob "
            "yozing."),
      bandlar=[
        dict(savol="a) Nega etanal (M=44) mos spirt — etanoldan (M=46) ancha past haroratda "
                   "qaynaydi (21 °C va 78 °C)? Batafsil tushuntiring.",
             yechim=["Aldegidda O–H bog'i yo'q — molekulalar o'zaro vodorod bog' hosil qilolmaydi,",
                     "spirtdagi kabi «tikilish» bo'lmagani uchun qaynash ancha oson."], M=13, A=0),
        dict(savol="b) Nega aldegidlar baribir mos alkanlardan yuqorida qaynaydi?",
             yechim=["C=O guruh qutbli — dipollar o'zaro tortishadi, alkanlarda bunday tortishuv "
                     "kuchsiz."], M=9, A=0),
        dict(savol="c) Quyi aldegidlarning suvda yaxshi erishini nima ta'minlaydi?",
             yechim=["C=O kislorodi suv molekulalari bilan vodorod bog' hosil qila oladi."], M=3, A=0),
      ],
      rasmiylashtirish="Qaynash-eruvchanlik mulohazasi (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="ald_bp_mulohaza")),
 dict(n=43, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Omborda 300 g 40 % li formalin bor. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Eritmadagi sof formaldegid massasini toping.",
             yechim=["m = 300·0,4 = 120 g."], M=4, A=2),
        dict(savol="b) Formaldegid mol miqdorini hisoblang. (M=30)",
             yechim=["n = 120/30 = 4 mol."], M=4, A=3),
        dict(savol="c) Shuncha formaldegidni metanolni oksidlab olish uchun necha gramm metanol "
                   "kerak? (M=32, chiqish 100 %)",
             yechim=["2CH₃OH + O₂ → 2HCHO + 2H₂O: n(CH₃OH) = 4 mol → m = 128 g."], M=4, A=3),
        dict(savol="d) Formalinning ikki qo'llanilishini yozing.",
             yechim=["Dezinfeksiya; biologik preparatlarni saqlash (smolalar olish ham)."], M=3, A=2),
      ],
      rasmiylashtirish="Formalin hisobi: ulush → mol → xomashyo → qo'llash; M15+A10.",
      parametrlar=dict(arch="formalin_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263503)
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
    d = dict(n=n, tur="Y1", element="III.5", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III5-A", daraja="A", bob=5, bob_nomi="Aldegidlar va ketonlar",
    manba=("MS spetsifikatsiyasi III.5; 10-sinf darslik — savollar yangi tuzilgan, hayotiy sahnalar "
           "(formalin-muzey, aseton, fanera, termos) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
