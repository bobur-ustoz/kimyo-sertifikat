# -*- coding: utf-8 -*-
"""Organik 5-bob B-varianti: Aldegidlar va ketonlar (III.5) — HAQIQIY MS MUHITI ★★★★.
1-2-3 tanlovlar, mosliklar, teskari masalalar, kumush-ko'zgu hisoblari, unumli zanjirlar."""
import json, random

OUT = "mavzu_III5B.json"
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

# 1 (3)
q(3, "yuqori",
  "«Kumush ko'zgu» reaksiyasini beradigan moddalarni tanlang: 1) metanal; 2) etanal; 3) aseton; "
  "4) metanol.",
  "1, 2", [("1, 2, 3", "keton yumshoq oksidlovchiga chidamli"), ("faqat 1", "etanal ham aldegid"),
            ("1, 2, 4", "spirt Ag₂O bilan reaksiyaga kirishmaydi")],
  "Sinov faqat –CHO guruhiga ishlaydi: metanal va etanal.",
  dict(arch="kozgu_tanlov_b"))

# 2 (2)
q(2, "o'rta",
  "Propanal va propanon qanday izomerlar hisoblanadi?",
  "sinflararo izomerlar (C₃H₆O)", [("zanjir izomerlari", "zanjir bir xil, guruh o'rni har xil"),
                                    ("gomologlar", "tarkiblari bir xil-ku"),
                                    ("izomer emas", "ikkalasi ham C₃H₆O")],
  "Bir xil formula — har xil sinf: aldegid va keton.",
  dict(arch="sinflararo_b5"))

# 3 (3)
q(3, "yuqori",
  "Moslikni toping: 1) metanal; 2) etanal; 3) propanon — a) 40 % li eritmasi «formalin»; "
  "b) Kucherov reaksiyasi mahsuloti; c) lak-bo'yoq erituvchisi.",
  "1–a, 2–b, 3–c", [("1–b, 2–a, 3–c", "Kucherov C₂H₂ dan etanal beradi"),
                     ("1–a, 2–c, 3–b", "erituvchi — keton"),
                     ("1–c, 2–b, 3–a", "formalin — metanal eritmasi")],
  "HCHO — formalin; CH₃CHO — Kucherov; CH₃COCH₃ — erituvchi.",
  dict(arch="moslik_b5"))

# 4 (3) — RASM: kumush ko'zgu tajribasi
q(3, "o'rta",
  "Rasmdagi tajriba: noma'lum suyuqlik ammiakli Ag₂O bilan iliq suv hammomida qizdirilganda "
  "probirka devorida yaltiroq qatlam paydo bo'ldi. Bu nimani isbotlaydi?",
  "moddada aldegid guruhi borligini",
  [("moddada OH guruhi borligini", "spirtlar bu sinovga javob bermaydi"),
   ("modda keton ekanligini", "keton ko'zgu bermaydi"),
   ("moddada azot borligini", "sinov azotga emas")],
  "Ag⁺ ionlarini faqat oson oksidlanadigan –CHO qaytara oladi.",
  dict(arch="kozgu_tajriba_b"), fig="agmirror")

# 5 (2)
q(2, "o'rta",
  "Birlamchi spirtdan aldegid olishning laboratoriya usuli qaysi?",
  "qizdirilgan CuO ustidan spirt bug'ini o'tkazish",
  [("spirtni Na bilan qo'shish", "u alkogolyat beradi"),
   ("spirtni suv bilan aralashtirish", "reaksiya bormaydi"),
   ("spirtni sovutish", "agregat holat o'zgaradi, sinf emas")],
  "R–CH₂OH + CuO → R–CHO + Cu + H₂O.",
  dict(arch="olinish_cuo_b"))

# 6 (3)
check("q6", 24/44, 0.545)
q(3, "yuqori",
  "To'yingan bir asosli aldegidda uglerodning massa ulushi 54,5 %. Aldegidni aniqlang.",
  "etanal CH₃CHO", [("metanal", "unda C 40 %"), ("propanal", "unda 62,1 %"),
                     ("butanal", "unda 66,7 %")],
  "CₙH₂ₙO: 12n/(14n+16) = 0,545 → n = 2 → M = 44.",
  dict(arch="c_ulush_teskari_b5"))

# 7 (3)
q(3, "yuqori",
  "Etanal haqidagi TO'G'RI fikrlarni tanlang: 1) Kucherov reaksiyasi bilan olinadi; 2) «kumush "
  "ko'zgu» beradi; 3) qaytarilsa etanol hosil bo'ladi; 4) NaOH bilan tuz hosil qiladi.",
  "1, 2, 3", [("1, 2, 3, 4", "aldegid kislota emas — ishqor bilan tuz bermaydi"),
               ("faqat 2", "olinishi va qaytarilishi ham to'g'ri"),
               ("2, 4", "Kucherov ham to'g'ri")],
  "Aldegidda kislotali H yo'q — 4-fikr xato.",
  dict(arch="etanal_tanlov_b"))

# 8 (3)
check("q8", 0.2*144, 28.8)
q(3, "yuqori",
  "0,2 mol etanal ortiqcha Cu(OH)₂ bilan qizdirilganda hosil bo'lgan Cu₂O cho'kmasi massasini "
  "toping. (M(Cu₂O)=144)",
  "28,8 g", [("14,4 g", "0,1 mol deb olindi"), ("57,6 g", "2 mol Cu₂O xatosi"),
              ("19,2 g", "M(CuO) ishlatildi")],
  "1 mol aldegid → 1 mol Cu₂O: m = 0,2·144 = 28,8 g.",
  dict(arch="cu2o_hisob_b"))

# 9 (3)
q(3, "yuqori",
  "Etanal (M=44) −(21 °C) va etanol (M=46) — (78 °C). Qaynash haroratlaridagi bu katta farqning "
  "sababi nima?",
  "aldegid molekulalari o'zaro vodorod bog' hosil qilolmaydi",
  [("aldegid yengilroq bo'lgani uchun", "massalar deyarli teng"),
   ("aldegidda kislorod yo'qligi uchun", "C=O bor-ku"),
   ("spirt suvda yaxshi erigani uchun", "eruvchanlik qaynashga aloqasiz bu yerda")],
  "O–H bo'lmagani uchun assotsiatsiya yo'q — qaynash oson.",
  dict(arch="bp_farq_b"))

# 10 (3)
check("q10a", 10.8/108/2, 0.05); check("q10b", 2.2/0.05, 44)
q(3, "yuqori",
  "2,2 g noma'lum to'yingan aldegid «kumush ko'zgu» reaksiyasida 10,8 g kumush ajratdi. "
  "Aldegidni aniqlang. (M(Ag)=108)",
  "etanal", [("metanal", "M = 30 chiqishi kerak edi"), ("propanal", "M = 58"),
              ("butanal", "M = 72")],
  "n(Ag) = 0,1 → n(ald) = 0,05 → M = 2,2/0,05 = 44 g/mol.",
  dict(arch="m_teskari_b5"))

# 11 (2)
q(2, "o'rta",
  "Formalin tibbiyot va biologiyada nima uchun ishlatiladi?",
  "dezinfeksiya va anatomik preparatlarni saqlash uchun",
  [("og'riq qoldirish uchun", "u og'riq qoldirmaydi, zaharli"),
   ("vitamin sifatida", "aksincha, zarar"),
   ("qon to'xtatish uchun", "bunday xossasi yo'q")],
  "Oqsillarni ivitadi — mikroblarni o'ldiradi, to'qimalarni qotiradi.",
  dict(arch="formalin_qollash_b"))

# 12 (3)
q(3, "yuqori",
  "C₃H₆O molekulyar formulaga mos keladigan moddalarni tanlang: 1) propanal; 2) propanon; "
  "3) propan-2-ol.",
  "1, 2", [("1, 2, 3", "propan-2-ol C₃H₈O — vodorodi ko'p"), ("faqat 1", "aseton ham C₃H₆O"),
            ("faqat 2", "propanal ham shu formulada")],
  "C₃H₆O — aldegid va keton; spirt C₃H₈O bo'ladi.",
  dict(arch="c3h6o_tanlov_b"))

# 13 (3)
check("q13", 6.72/22.4*44, 13.2)
q(3, "o'rta",
  "6,72 L (n.sh.) atsetilen Kucherov reaksiyasiga to'liq kirishganda hosil bo'lgan etanal "
  "massasini toping. (M=44)",
  "13,2 g", [("6,6 g", "yarim mol xatosi"), ("26,4 g", "2 mol deb olindi"),
              ("4,4 g", "0,1 mol xatosi")],
  "n = 0,3 mol → m = 0,3·44 = 13,2 g.",
  dict(arch="kucherov_hisob_b"))

# 14 (2)
q(2, "o'rta",
  "Asetonning suvga munosabati qanday?",
  "suv bilan istalgan nisbatda aralashadi",
  [("umuman erimaydi", "qutbli C=O suv bilan «do'st»"),
   ("faqat qizdirilganda eriydi", "sovuqda ham cheksiz"),
   ("suv bilan reaksiyaga kirishib gaz beradi", "reaksiya bormaydi")],
  "Shu xossasi uni universal erituvchi qiladi.",
  dict(arch="aseton_suv_b"))

# 15 (3)
check("q15", 15/30*32, 16)
q(3, "o'rta",
  "15 g metanal vodorod bilan to'liq qaytarilganda hosil bo'lgan metanol massasini toping. "
  "(M(CH₃OH)=32)",
  "16 g", [("15 g", "M lar farqi unutildi"), ("32 g", "1 mol uchun"), ("8 g", "yarim hisob")],
  "n = 0,5 mol → m = 0,5·32 = 16 g.",
  dict(arch="qaytarilish_hisob_b"))

# 16 (2)
q(2, "o'rta",
  "Moslikni toping: 1) butanal; 2) butanon; 3) butan-1-ol — a) C₃H₇CHO; b) CH₃COC₂H₅; "
  "c) C₄H₉OH.",
  "1–a, 2–b, 3–c", [("1–b, 2–a, 3–c", "-al oxiri aldegid formulasiga mos"),
                     ("1–a, 2–c, 3–b", "-ol — spirt"),
                     ("1–c, 2–b, 3–a", "aldegidda OH yo'q")],
  "Qo'shimchani formulaga «tarjima» qilish: -al → CHO, -on → CO, -ol → OH.",
  dict(arch="nom_formula_moslik_b"))

# 17 (2)
q(2, "o'rta",
  "Fenol-formaldegid smola qaysi ikki monomerdan olinadi?",
  "fenol va metanal", [("fenol va etanal", "metanal ishlatiladi"),
                        ("benzol va metanol", "ikkalasi ham boshqa sinf"),
                        ("etilen va fenol", "u polietilen beradi")],
  "Polikondensatlanish: fenol + HCHO → smola + suv.",
  dict(arch="ffs_monomer_b"))

# 18 (3)
q(3, "o'rta",
  "Sirka aldegididan sirka kislota olish uchun qanday jarayon kerak?",
  "oksidlash", [("qaytarish", "u spirt beradi"), ("degidratatsiya", "suvsizlanadigan OH yo'q"),
                 ("gidroliz", "murakkab efir emas")],
  "2CH₃CHO + O₂ → 2CH₃COOH (katalizator).",
  dict(arch="oksidlanish_yonalish_b"))

# 19 (3)
check("q19", 8.8/44*2*22.4, 8.96)
q(3, "o'rta",
  "8,8 g etanal to'liq yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping.",
  "8,96 L", [("4,48 L", "koeffitsiyent 2 unutildi"), ("22,4 L", "mol xato"),
              ("2,24 L", "hisob xato")],
  "n = 0,2 mol → n(CO₂) = 0,4 → V = 8,96 L.",
  dict(arch="yonish_hisob_b5"))

# 20 (2)
q(2, "quyi",
  "Metanalning 40 % li suvdagi eritmasi qanday nomlanadi?",
  "formalin", [("formiat", "u kislota tuzi"), ("ftorid", "ftorga aloqasi yo'q"),
                ("fenolyat", "u fenol tuzi")],
  "Nomi formaldegiddan olingan.",
  dict(arch="formalin_nom_b"))

# 21 (3)
check("q21", 250*0.4, 100)
q(3, "o'rta",
  "250 g 40 % li formalinda necha gramm sof formaldegid bor?",
  "100 g", [("40 g", "100 g uchun hisob"), ("150 g", "bu suv massasi"), ("250 g", "hammasi emas")],
  "m = 250·0,4 = 100 g.",
  dict(arch="formalin_ulush_b"))

# 22 (3)
q(3, "yuqori",
  "Nega ketonlar aldegidlarga o'xshab yumshoq oksidlovchilar (Ag₂O, Cu(OH)₂) bilan reaksiyaga "
  "kirishmaydi?",
  "karbonil uglerodida vodorod atomi yo'q",
  [("ularda C=O guruh yo'q", "bor, lekin o'rni boshqa"),
   ("ular gaz holatida", "aseton — suyuqlik"),
   ("ular suvda erimaydi", "aseton cheksiz eriydi")],
  "Oksidlanish uchun C–H (karbonildagi) kerak; ketonda u ikki radikal bilan band.",
  dict(arch="keton_sabab_b"))

# 23 (3)
check("q23", 5.8/58*2*108, 21.6)
q(3, "yuqori",
  "5,8 g propanal «kumush ko'zgu» reaksiyasiga to'liq kirishganda ajralgan kumush massasini "
  "toping. (M(C₂H₅CHO)=58, M(Ag)=108)",
  "21,6 g", [("10,8 g", "koeffitsiyent 2 unutildi"), ("43,2 g", "0,2 mol deb olindi"),
              ("5,4 g", "hisob xato")],
  "n = 0,1 mol → n(Ag) = 0,2 → m = 21,6 g.",
  dict(arch="propanal_ag_b"))

# 24 (2)
q(2, "o'rta",
  "Quyidagi karbonil birikmalardan qaysi biri xona haroratida GAZ holatida bo'ladi?",
  "metanal", [("etanal", "21 °C da qaynaydi — chegarada suyuq"), ("propanal", "49 °C"),
               ("aseton", "56 °C")],
  "HCHO −19 °C da qaynaydi.",
  dict(arch="agregat_b5"))

# 25 (3)
q(3, "o'rta",
  "Formaldegid ishlatilishi haqidagi TO'G'RI fikrlarni tanlang: 1) fenol-formaldegid smolalar "
  "olish; 2) dezinfeksiyalovchi vositalar; 3) biologik preparatlarni saqlash; 4) oziq-ovqat "
  "konservanti sifatida qo'shish.",
  "1, 2, 3", [("1, 2, 3, 4", "oziq-ovqatga qo'shish qat'iyan taqiqlangan — zaharli"),
               ("faqat 1", "tibbiy qo'llanishlari ham bor"), ("2, 4", "smolalar — asosiy yo'nalish")],
  "HCHO kuchli zahar — oziq-ovqatda ishlatilmaydi.",
  dict(arch="hcho_qollash_tanlov_b"))

# 26 (3)
check("q26", 0.3*22.4, 6.72)
q(3, "yuqori",
  "0,1 mol to'yingan bir asosli aldegid to'liq yonganda 6,72 L (n.sh.) CO₂ hosil bo'ldi. "
  "Aldegidni aniqlang.",
  "propanal", [("etanal", "unda 4,48 L chiqardi"), ("metanal", "unda 2,24 L"),
                ("butanal", "unda 8,96 L")],
  "n(CO₂) = 0,3 mol → molekulada 3 ta C → C₂H₅CHO.",
  dict(arch="co2_teskari_b5"))

# 27 (2)
q(2, "o'rta",
  "Kucherov reaksiyasining katalizatori qaysi?",
  "simob(II) tuzlari", [("nikel", "u gidrogenlashda"), ("temir(III) xlorid", "u fenol sinovida"),
                         ("platina", "u boshqa jarayonlarda")],
  "Hg²⁺ ionlari suvning uchbog'ga birikishini tezlashtiradi.",
  dict(arch="kucherov_kat_b"))

# 28 (3)
check("q28", 9.2/46*44*0.8, 7.04)
q(3, "yuqori",
  "9,2 g etanol CuO bilan oksidlanganda etanal 80 % unum bilan olindi. Hosil bo'lgan etanal "
  "massasini toping.",
  "7,04 g", [("8,8 g", "unum hisobga olinmadi"), ("4,4 g", "mol xato"),
              ("11 g", "unum teskari qo'llandi")],
  "n = 0,2 mol → nazariy 8,8 g → amaliy 8,8·0,8 = 7,04 g.",
  dict(arch="unum_hisob_b5"))

# 29 (3)
check("q29", 5.8/58*4*22.4, 8.96)
q(3, "yuqori",
  "CH₃COCH₃ + 4O₂ → 3CO₂ + 3H₂O. 5,8 g aseton to'liq yonishi uchun zarur kislorod hajmini "
  "(n.sh.) toping.",
  "8,96 L", [("6,72 L", "CO₂ hajmi topildi"), ("22,4 L", "1 mol uchun"), ("4,48 L", "hisob xato")],
  "n = 0,1 mol → n(O₂) = 0,4 → V = 8,96 L.",
  dict(arch="aseton_yonish_b"))

# 30 (3)
q(3, "yuqori",
  "Aseton haqidagi TO'G'RI fikrlarni tanlang: 1) keton sinfiga mansub; 2) yaxshi organik "
  "erituvchi; 3) «kumush ko'zgu» reaksiyasini beradi; 4) molekulyar formulasi C₃H₆O.",
  "1, 2, 4", [("1, 2, 3, 4", "keton ko'zgu bermaydi"), ("faqat 1, 4", "erituvchiligi mashhur"),
               ("2, 3", "sinfi ham to'g'ri ko'rsatilgan")],
  "3-fikr xato: ko'zgu — aldegidlar imzosi.",
  dict(arch="aseton_tanlov_b"))

# 31 (3)
check("q31a", 21.6/108/2, 0.1); check("q31b", 10.2-4.4, 5.8)
q(3, "yuqori",
  "Etanal va aseton aralashmasi 10,2 g. Aralashma ortiqcha ammiakli Ag₂O bilan ishlanganda "
  "21,6 g kumush ajraldi. Aralashmadagi aseton massasini toping.",
  "5,8 g", [("4,4 g", "bu etanal massasi"), ("10,2 g", "faqat etanal reaksiyaga kirishadi"),
             ("2,9 g", "hisob xato")],
  "n(Ag) = 0,2 → n(etanal) = 0,1 → m(etanal) = 4,4 g → m(aseton) = 10,2 − 4,4 = 5,8 g.",
  dict(arch="aralashma_ag_b"))

# 32 (3)
check("q32", 0.2*44*0.75, 6.6)
q(3, "yuqori",
  "0,2 mol kalsiy karbiddan olingan atsetilen Kucherov reaksiyasiga yuborildi (unum 75 %). "
  "Hosil bo'lgan etanal massasini toping.",
  "6,6 g", [("8,8 g", "unum hisobga olinmadi"), ("4,4 g", "mol xato"),
             ("13,2 g", "karbid 2 mol deb olindi")],
  "CaC₂ → C₂H₂ (0,2 mol) → nazariy 8,8 g etanal → amaliy 8,8·0,75 = 6,6 g.",
  dict(arch="karbid_zanjir_b"))

# ---------- Y2: laboratoriya identifikatsiyasi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.5",
  ichki_pasport=[dict(n=33, element="III.5", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=34, element="III.5", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="III.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uchta raqamlanmagan probirkada etanal, aseton va etanol bor. Ularni kimyoviy "
               "sinovlar bilan farqlash kerak. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Etanalni bir qadamda taniydigan sinov qaysi?",
    "34. Etanolni taniydigan sinov qaysi?",
    "35. Aseton qanday aniqlanadi?"],
  javoblar_royxati=["A) ammiakli Ag₂O bilan qizdirish — devorda kumush ko'zgu",
                    "B) qizdirilgan CuO sim tushirish — sim yaltiraydi, aldegid hidi keladi",
                    "C) ikkala sinov ham o'zgarish bermaydi — istisno usuli",
                    "D) lakmus tomizish — qizil rang",
                    "E) bromli suv qo'shish — rangsizlanish",
                    "F) FeCl₃ tomizish — binafsha rang"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="uchchala modda ham neytral — lakmus ishlamaydi"),
                   dict(variant="E", xato="to'yinmagan bog' yo'q — bromli suv o'zgarmaydi"),
                   dict(variant="F", xato="FeCl₃ — fenol sinovi, bu yerda fenol yo'q")],
  yechim=("Etanal Ag₂O bilan ko'zgu beradi (A). Etanol CuO da aldegidgacha oksidlanadi (B). "
          "Aseton ikkala sinovda ham «jim» — istisno bilan topiladi (C)."),
  parametrlar=dict(arch="lab_identifikatsiya_b5"))

# ---------- O1 (Spectrum uslubi) ----------
check("o36", 0.15*44, 6.6)
check("o37", 21.6/108/2*44, 4.4)
check("o38", 4.48/22.4*44, 8.8)
check("o39", 14.5/58*3*22.4, 16.8)
check("o40", 12.8/32*30, 12)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,15 mol etanalning massasini (g) toping. (M=44)",
      javob="6,6", yechim="m = 0,15·44 = 6,6 g.",
      parametrlar=dict(arch="etanal_massa_o1_b")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="«Kumush ko'zgu» reaksiyasida 21,6 g kumush olish uchun necha gramm etanal kerak? "
            "(M(Ag)=108)",
      javob="4,4", yechim="n(Ag) = 0,2 → n(etanal) = 0,1 → m = 4,4 g.",
      parametrlar=dict(arch="ag_teskari_o1_b")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayon bo'yicha: 4,48 L (n.sh.) atsetilen Kucherov reaksiyasiga to'liq "
            "kirishganda hosil bo'lgan etanal massasini (g) toping.",
      javob="8,8", yechim="n = 0,2 mol → m = 0,2·44 = 8,8 g.",
      parametrlar=dict(arch="sxema_kucherov_b"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="14,5 g aseton to'liq yonganda hosil bo'lgan CO₂ hajmini (n.sh., L) toping. (M=58)",
      javob="16,8", yechim="n = 0,25 → n(CO₂) = 0,75 mol → V = 16,8 L.",
      parametrlar=dict(arch="aseton_yonish_o1_b")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="12,8 g metanol to'liq oksidlanganda hosil bo'ladigan metanal massasini (g) toping. "
            "(M(CH₃OH)=32, M(HCHO)=30)",
      javob="12", yechim="n = 0,4 mol → m(HCHO) = 0,4·30 = 12 g.",
      parametrlar=dict(arch="metanol_oksidlanish_o1_b")),
]

# ---------- O2 ----------
check("o41b", 12.8/64, 0.2); check("o41c", 0.2*44, 8.8); check("o41d", 0.4*108, 43.2)
check("o43b", 21.6/108/2, 0.1); check("o43c", 7.2/0.1, 72)
O2 = [
 dict(n=41, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "12,8 g kalsiy karbiddan (CaC₂, M=64) olingan atsetilen Kucherov reaksiyasiga, mahsulot "
            "esa «kumush ko'zgu» reaksiyasiga to'liq yuborildi."),
      bandlar=[
        dict(savol="a) Zanjirning uchala tenglamasini yozing.",
             yechim=["CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂; C₂H₂ + H₂O →(Hg²⁺) CH₃CHO;",
                     "CH₃CHO + Ag₂O →(NH₃) CH₃COOH + 2Ag↓."], M=5, A=2),
        dict(savol="b) Atsetilen mol miqdorini toping.",
             yechim=["n(CaC₂) = 12,8/64 = 0,2 mol → n(C₂H₂) = 0,2 mol."], M=3, A=3),
        dict(savol="c) Hosil bo'lgan etanal massasini hisoblang.",
             yechim=["n = 0,2 mol → m = 8,8 g."], M=4, A=2),
        dict(savol="d) Ajralgan kumush massasini toping.",
             yechim=["n(Ag) = 0,4 mol → m = 43,2 g."], M=3, A=3),
      ],
      rasmiylashtirish="Karbid-Kucherov-ko'zgu zanjiri; M15+A10.",
      parametrlar=dict(arch="karbid_kozgu_o2_b")),
 dict(n=42, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Aldegid — spirt bilan karbon kislota orasidagi «ko'prik» modda. Quyidagilarga "
            "MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Nega aldegid «oraliq oksidlanish bosqichi» deyiladi? Etanol misolida zanjirni "
                   "tuzib, har bosqichda uglerod atomining holatini tushuntiring.",
             yechim=["C₂H₅OH → CH₃CHO → CH₃COOH: har bosqichda uglerod vodorod yo'qotib,",
                     "kislorod «orttiradi» — oksidlanish darajasi izchil ortadi;",
                     "aldegid ham oksidlanishi, ham qaytarilishi mumkin bo'lgan o'rtadagi holat."], M=13, A=0),
        dict(savol="b) Har yo'nalish uchun mos reagentlarni ko'rsating.",
             yechim=["Oksidlash: Ag₂O (ammiakli), Cu(OH)₂, O₂/kat.; qaytarish: H₂ (Ni)."], M=9, A=0),
        dict(savol="c) Bu «ikki tomonlamalik»ning sanoatdagi ahamiyatini bitta misolda yozing.",
             yechim=["Bitta xomashyodan (etanal) ham sirka kislota, ham etanol olish mumkin."], M=3, A=0),
      ],
      rasmiylashtirish="Ko'prik-modda mulohazasi (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="koprik_mulohaza_b")),
 dict(n=43, tur="O2", element="III.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "7,2 g noma'lum to'yingan bir asosli aldegid «kumush ko'zgu» reaksiyasida 21,6 g kumush "
            "ajratdi. (M(Ag)=108)"),
      bandlar=[
        dict(savol="a) Reaksiyaning umumiy tenglamasini yozing.",
             yechim=["R–CHO + Ag₂O →(NH₃) R–COOH + 2Ag↓."], M=4, A=2),
        dict(savol="b) Aldegid mol miqdorini toping.",
             yechim=["n(Ag) = 0,2 → n(aldegid) = 0,1 mol."], M=4, A=3),
        dict(savol="c) Aldegidning molyar massasini va formulasini aniqlang.",
             yechim=["M = 7,2/0,1 = 72 g/mol → C₃H₇CHO (butanal)."], M=4, A=3),
        dict(savol="d) Shu tarkibga mos yana bitta izomer aldegid nomini yozing.",
             yechim=["2-metilpropanal (izobutanal)."], M=3, A=2),
      ],
      rasmiylashtirish="Teskari masala: tenglama → mol → M → izomer; M15+A10.",
      parametrlar=dict(arch="nomalum_aldegid_o2_b")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263504)
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
    variant="mavzu-III5-B", daraja="B", bob=5, bob_nomi="Aldegidlar va ketonlar",
    manba=("MS spetsifikatsiyasi III.5; Tongotarov-uslub arxetiplar — savollar yangi tuzilgan, "
           "barcha javoblar mustaqil hisoblangan"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
