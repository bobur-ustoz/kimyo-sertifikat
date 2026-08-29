# -*- coding: utf-8 -*-
"""Organik 4-bob B-varianti: Spirtlar va fenollar (III.4) — HAQIQIY MS MUHITI ★★★★.
1-2-3 tanlovlar, mosliklar, teskari masalalar, sifat sinovlari (Cu(OH)2, FeCl3, Br2)."""
import json, random

OUT = "mavzu_III4B.json"
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
q(2, "o'rta",
  "Birlamchi spirtni ko'rsating.",
  "propan-1-ol", [("propan-2-ol", "OH ikkilamchi C da"),
                  ("2-metilpropan-2-ol", "OH uchlamchi C da"),
                  ("dimetil efir", "u umuman spirt emas")],
  "OH faqat bitta boshqa C bilan bog'langan uglerodda — CH₃CH₂CH₂OH.",
  dict(arch="birlamchi_spirt_b"))

# 2 (3)
q(3, "o'rta",
  "C₄H₉OH tarkibli bir atomli spirtning nechta izomer spirti bor?",
  "4 ta", [("2 ta", "faqat zanjir izomeriyasi sanaladi"), ("3 ta", "uchlamchi izomer unutildi"),
            ("5 ta", "efir izomerlari spirt emas")],
  "Butan-1-ol, butan-2-ol, 2-metilpropan-1-ol, 2-metilpropan-2-ol.",
  dict(arch="c4_izomer_b"))

# 3 (3)
q(3, "yuqori",
  "Molekulalari O'ZARO vodorod bog' hosil qila oladigan moddalarni tanlang: 1) etanol; "
  "2) dimetil efir; 3) suv; 4) metan.",
  "1, 3", [("1, 2, 3", "efirda O–H bog'i yo'q"), ("faqat 1", "suv ham H-bog' ustasi"),
            ("1, 2, 3, 4", "metanda qutbli bog' yo'q")],
  "H-bog' uchun O–H (yoki N–H) kerak: etanol va suvda bor, efir va metanda yo'q.",
  dict(arch="hbog_tanlov_b"))

# 4 (3) — RASM: laboratoriya degidratatsiya
q(3, "o'rta",
  "Rasmdagi tajriba: etanol konsentrlangan H₂SO₄ bilan 170 °C dan yuqorida qizdirilmoqda. "
  "Asosiy mahsulot qaysi?",
  "etilen C₂H₄", [("dietil efir", "u ~140 °C da hosil bo'ladi"),
                   ("sirka aldegidi", "u oksidlanish mahsuloti"),
                   ("vodorod", "bu Na bilan reaksiya belgisi")],
  "Molekula ICHIDAN suv ajraladi: C₂H₅OH → C₂H₄ + H₂O (H₂SO₄, t>170 °C).",
  dict(arch="degidratatsiya_b"), fig="dehydro")

# 5 (2)
q(2, "o'rta",
  "Fenol reaksiyaga kirishadi-yu, etanol kirishMAYdigan reagent qaysi?",
  "NaOH eritmasi", [("natriy metali", "ikkalasi ham kirishadi"),
                     ("kislorod (yonish)", "ikkalasi ham yonadi"),
                     ("xlorid kislota", "ikkalasi ham HCl bilan tuz hosil qilmaydi")],
  "Fenol kuchsiz kislota: C₆H₅OH + NaOH → C₆H₅ONa + H₂O; spirtlar ishqor bilan reaksiyaga kirishmaydi.",
  dict(arch="fenol_naoh_b"))

# 6 (3)
check("q6", 36/60, 0.6)
q(3, "yuqori",
  "Bir atomli to'yingan spirtda uglerodning massa ulushi 60 %. Spirtni aniqlang.",
  "propanol C₃H₇OH", [("etanol", "unda C ulushi 52,2 %"), ("butanol", "unda 64,9 %"),
                       ("metanol", "unda 37,5 %")],
  "CₙH₂ₙ₊₂O: 12n/(14n+18) = 0,60 → n = 3. M = 60 g/mol.",
  dict(arch="c_ulush_teskari_b"))

# 7 (3)
q(3, "yuqori",
  "Moslikni toping: 1) glitserin; 2) fenol; 3) etanol — a) Cu(OH)₂ bilan yorqin ko'k eritma; "
  "b) FeCl₃ bilan binafsha rang; c) qizdirilgan CuO bilan aldegid hosil qiladi.",
  "1–a, 2–b, 3–c", [("1–b, 2–a, 3–c", "FeCl₃ — fenolning «imzosi»"),
                     ("1–a, 2–c, 3–b", "CuO oksidlashi — spirtga xos"),
                     ("1–c, 2–b, 3–a", "ko'p atomlilik sinovi — Cu(OH)₂")],
  "Har sinfning o'z sifat sinovi bor: glitserat ko'ki, fenolyat-Fe binafshasi, aldegid hidi.",
  dict(arch="sifat_moslik_b"))

# 8 (3)
q(3, "o'rta",
  "Etanol bug'i qizdirilgan CuO ustidan o'tkazilganda qora sim qizil-yaltiroq bo'lib qoldi. "
  "Organik mahsulot qaysi?",
  "sirka aldegidi CH₃CHO", [("sirka kislota", "u kuchli oksidlovchida hosil bo'ladi"),
                             ("etilen", "bu degidratatsiya mahsuloti"),
                             ("dietil efir", "u H₂SO₄ ishtirokida")],
  "C₂H₅OH + CuO → CH₃CHO + Cu + H₂O; mis qaytariladi — sim «yangilanadi».",
  dict(arch="cuo_oksidlanish_b"))

# 9 (3)
q(3, "yuqori",
  "Butan-1-ol (M=74) va dietil efir (M=74) izomer. Qaysinisining qaynash harorati yuqori va nima uchun?",
  "butanolniki — molekulalari vodorod bog' bilan bog'langan",
  [("efirniki — kislorodi ikki radikal orasida", "bu H-bog' bermaydi"),
   ("ikkalasiniki teng — M bir xil", "M emas, bog'lanish hal qiladi"),
   ("butanolniki — u og'irroq", "massalari teng")],
  "O–H bo'lgani uchun butanol assotsiatsiyalangan: 117 °C; efir esa 35 °C da qaynaydi.",
  dict(arch="izomer_bp_b"))

# 10 (3)
check("q10", 9.4/94*3*160, 48)
q(3, "yuqori",
  "9,4 g fenol bromli suv bilan to'liq reaksiyaga kirishishi uchun zarur brom massasini toping. "
  "(M(C₆H₅OH)=94, M(Br₂)=160)",
  "48 g", [("16 g", "koeffitsiyent 3 unutildi"), ("32 g", "2 mol deb olindi"),
            ("24 g", "yarim hisob xatosi")],
  "C₆H₅OH + 3Br₂ → C₆H₂Br₃OH↓ + 3HBr: n(fenol)=0,1 → n(Br₂)=0,3 → m = 48 g.",
  dict(arch="fenol_brom_hisob_b"))

# 11 (2)
q(2, "o'rta",
  "Fenol suvda qanday eriydi?",
  "sovuqda cheklangan, qizdirilganda yaxshi eriydi",
  [("har qanday nisbatda", "bu quyi spirtlarga xos"),
   ("umuman erimaydi", "«karbol suvi» mavjud-ku"),
   ("faqat kislotalarda", "u o'zi kuchsiz kislota")],
  "70 °C dan yuqorida fenol suv bilan istalgan nisbatda aralashadi.",
  dict(arch="fenol_eruvchanlik_b"))

# 12 (3)
q(3, "yuqori",
  "Natriy metali bilan reaksiyaga kirishadigan moddalarni tanlang: 1) etanol; 2) fenol; "
  "3) dietil efir; 4) suv.",
  "1, 2, 4", [("1, 2, 3, 4", "efirda harakatchan H yo'q"), ("faqat 1, 4", "fenol OH i ham H beradi"),
               ("faqat 2", "spirt va suv ham H₂ ajratadi")],
  "O–H bog'i borlarning hammasi Na bilan H₂ ajratadi; efirda O–H yo'q.",
  dict(arch="na_tanlov_b"))

# 13 (3)
check("q13a", 12.4/62, 0.2); check("q13b", 0.2*22.4, 4.48)
q(3, "yuqori",
  "12,4 g etilenglikol ortiqcha natriy bilan reaksiyaga kirishganda ajralgan vodorod hajmini "
  "(n.sh.) toping. (M=62)",
  "4,48 L", [("2,24 L", "bitta OH deb olindi"), ("8,96 L", "H₂ koeffitsiyenti xato"),
              ("1,12 L", "hisob xato")],
  "Ikki OH: 1 mol glikol 1 mol H₂ beradi. n = 0,2 → V = 4,48 L.",
  dict(arch="glikol_na_hisob_b"))

# 14 (2)
q(2, "o'rta",
  "Etanolning suvdagi eritmasiga lakmus tomizilsa nima kuzatiladi?",
  "rang o'zgarmaydi — eritma neytral",
  [("qizaradi", "spirt eritmada dissotsiatsiyalanmaydi"),
   ("ko'karadi", "u ishqor emas"),
   ("rangsizlanadi", "lakmus oqartirilmaydi")],
  "Spirtlarning «kislotaliligi» suvdagidan ham kuchsiz — indikatorga ta'sir yo'q.",
  dict(arch="lakmus_b"))

# 15 (3)
check("q15a", 23*0.8, 18.4); check("q15b", 18.4/46*2*22.4, 17.92)
q(3, "yuqori",
  "Hajmi 23 mL, zichligi 0,8 g/mL bo'lgan etanol to'liq yondirildi. Hosil bo'lgan CO₂ hajmini "
  "(n.sh.) toping.",
  "17,92 L", [("8,96 L", "koeffitsiyent 2 unutildi"), ("22,4 L", "mol miqdori xato"),
               ("4,48 L", "massa hisoblanmadi")],
  "m = 23·0,8 = 18,4 g → n = 0,4 mol → n(CO₂) = 0,8 → V = 17,92 L.",
  dict(arch="zichlik_yonish_b"))

# 16 (2)
q(2, "quyi",
  "Moslikni toping: 1) metanol; 2) etilenglikol; 3) glitserin — a) bir atomli; b) ikki atomli; "
  "c) uch atomli.",
  "1–a, 2–b, 3–c", [("1–b, 2–a, 3–c", "metanolda bitta OH"),
                     ("1–a, 2–c, 3–b", "glikolda ikkita OH"),
                     ("1–c, 2–b, 3–a", "glitserinda uchta OH")],
  "OH soni: CH₃OH — 1, C₂H₄(OH)₂ — 2, C₃H₅(OH)₃ — 3.",
  dict(arch="atomlilik_moslik_b"))

# 17 (2)
q(2, "o'rta",
  "Ochiq havoda saqlangan fenol kristallari vaqt o'tishi bilan nega pushti rangga kiradi?",
  "havo kislorodida qisman oksidlanadi",
  [("suv tortib eriydi", "namlik rang bermaydi"),
   ("CO₂ bilan reaksiyaga kirishadi", "fenol karbonatdan kuchsiz"),
   ("yorug'likda izomerlanadi", "izomerlanish rang bermaydi")],
  "Oksidlanish mahsulotlari (xinonlar) pushti-qo'ng'ir tus beradi — shuning uchun qorong'ida, "
  "og'zi berk idishda saqlanadi.",
  dict(arch="fenol_oksidlanish_b"))

# 18 (3)
q(3, "yuqori",
  "Glitserin haqidagi TO'G'RI fikrlarni tanlang: 1) uch atomli spirt; 2) qovushqoq, shirin "
  "suyuqlik; 3) suvda erimaydi; 4) nitroglitserin olishda xomashyo.",
  "1, 2, 4", [("1, 2, 3, 4", "glitserin suvda cheksiz eriydi"), ("faqat 1, 4", "fizik xossasi ham to'g'ri"),
               ("1, 3", "eruvchanligi noto'g'ri aytilgan")],
  "Uchta OH suv bilan «do'st» — cheksiz eriydi; 3-fikr xato.",
  dict(arch="glitserin_tanlov_b"))

# 19 (3)
check("q19", 13.8/46*22.4, 6.72)
q(3, "o'rta",
  "13,8 g etanol to'liq degidratatsiyalanganda hosil bo'lgan etilen hajmini (n.sh.) toping.",
  "6,72 L", [("13,44 L", "2 mol deb olindi"), ("3,36 L", "yarim mol xatosi"),
              ("22,4 L", "mol hisoblanmadi")],
  "n = 13,8/46 = 0,3 mol → n(C₂H₄) = 0,3 → V = 6,72 L.",
  dict(arch="degidratatsiya_hisob_b"))

# 20 (2)
q(2, "o'rta",
  "Etanol bilan sinflararo izomer bo'lgan modda qaysi?",
  "dimetil efir CH₃–O–CH₃", [("metanol", "tarkibi boshqa: CH₄O"),
                              ("sirka aldegidi", "C₂H₄O — vodorodi kam"),
                              ("etilenglikol", "C₂H₆O₂ — kislorodi ko'p")],
  "Ikkalasi ham C₂H₆O, lekin funksional guruhlari har xil.",
  dict(arch="sinflararo_izomer_b"))

# 21 (3)
check("q21", 200*0.96, 192)
q(3, "o'rta",
  "Tibbiy spirt — 96 % li eritma. 200 g shunday eritmada necha gramm sof etanol bor?",
  "192 g", [("96 g", "100 g uchun hisob"), ("8 g", "bu suv massasi"), ("184 g", "hisob xato")],
  "m = 200·0,96 = 192 g.",
  dict(arch="ulush_hisob_b"))

# 22 (3)
q(3, "yuqori",
  "Natriy fenolyat eritmasidan CO₂ o'tkazilganda fenol ajralib chiqadi. Bundan qanday xulosa kelib chiqadi?",
  "fenol karbonat kislotadan kuchsiz kislota",
  [("fenol karbonat kislotadan kuchli", "kuchli kislota kuchsizni siqib chiqaradi, aksincha emas"),
   ("fenol umuman kislota emas", "NaOH bilan tuz hosil qiladi-ku"),
   ("CO₂ fenol bilan birikadi", "reaksiya fenolyat bilan boradi")],
  "C₆H₅ONa + CO₂ + H₂O → C₆H₅OH + NaHCO₃: kuchliroq H₂CO₃ kuchsiz fenolni siqib chiqaradi.",
  dict(arch="fenolyat_co2_b"))

# 23 (3)
check("q23", 6.4/32*22.4, 4.48)
q(3, "o'rta",
  "6,4 g metanol to'liq yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(CH₃OH + 1,5O₂ → CO₂ + 2H₂O)",
  "4,48 L", [("8,96 L", "2 mol CO₂ deb olindi"), ("2,24 L", "mol xato"),
              ("6,72 L", "hisob xato")],
  "n = 6,4/32 = 0,2 mol → n(CO₂) = 0,2 → V = 4,48 L.",
  dict(arch="metanol_yonish_hisob_b"))

# 24 (2)
q(2, "o'rta",
  "IUPAC nomenklaturasida uglerod zanjiri qaysi tomondan raqamlanadi?",
  "OH guruhiga eng kichik raqam tegadigan tomondan",
  [("har doim chapdan", "yo'nalishni guruh belgilaydi"),
   ("eng uzun radikal tomondan", "lokant qoidasi ustun"),
   ("istalgan tomondan", "nom bir xil chiqmaydi")],
  "Masalan CH₃–CH(OH)–CH₃ — propan-2-ol (propan-2-ol, 2 kichik lokant).",
  dict(arch="nomenklatura_b"))

# 25 (3)
q(3, "o'rta",
  "Etanolning ishlatilishi haqidagi TO'G'RI fikrlarni tanlang: 1) tibbiyotda antiseptik; "
  "2) sirka kislota olishda xomashyo; 3) motor yoqilg'isiga qo'shimcha; 4) miqdoridan qat'i nazar "
  "organizm uchun zararsiz.",
  "1, 2, 3", [("1, 2, 3, 4", "etanol — narkotik ta'sirli zahar"), ("faqat 1", "sanoat ishlatilishi ham bor"),
               ("2, 4", "antiseptiklik ham to'g'ri")],
  "Etanol keng ishlatiladi, ammo ichilganda organizmga kuchli zarar yetkazadi — 4-fikr xato.",
  dict(arch="etanol_qollash_tanlov_b"))

# 26 (3)
check("q26a", 1.12/22.4, 0.05); check("q26b", 8.8/0.1, 88)
q(3, "yuqori",
  "8,8 g noma'lum bir atomli to'yingan spirt natriy bilan reaksiyaga kirishganda 1,12 L (n.sh.) "
  "vodorod ajraldi. Spirtni aniqlang.",
  "pentanol C₅H₁₁OH", [("butanol", "M = 74 chiqishi kerak edi"), ("propanol", "M = 60"),
                        ("geksanol", "M = 102")],
  "n(H₂) = 0,05 → n(spirt) = 0,1 mol → M = 8,8/0,1 = 88 g/mol → C₅H₁₂O.",
  dict(arch="m_teskari_b"))

# 27 (2)
q(2, "o'rta",
  "Bijg'igan eritmadan etanolni ajratib olishning asosiy laboratoriya-sanoat usuli qaysi?",
  "haydash (rektifikatsiya)", [("filtrlash", "spirt eritmada, cho'kmada emas"),
                                ("bug'latib qoldirish", "spirtning o'zi uchib ketadi"),
                                ("magnit bilan ajratish", "magnit xossasi yo'q")],
  "Qaynash haroratlari farqi (78 °C va 100 °C) asosida kolonnalarda haydaladi.",
  dict(arch="rektifikatsiya_b"))

# 28 (3)
check("q28", 9.2/46*80, 16)
q(3, "yuqori",
  "9,2 g etanolni sirka aldegidigacha oksidlash uchun zarur mis(II) oksid massasini toping. "
  "(M(CuO)=80)",
  "16 g", [("8 g", "0,1 mol deb olindi"), ("32 g", "2 mol CuO xatosi"), ("80 g", "1 mol uchun")],
  "C₂H₅OH + CuO → CH₃CHO + Cu + H₂O: n = 0,2 → m(CuO) = 0,2·80 = 16 g.",
  dict(arch="cuo_hisob_b"))

# 29 (3)
check("q29", 0.05*331, 16.55)
q(3, "yuqori",
  "0,05 mol fenol bromli suv bilan to'liq reaksiyaga kirishganda hosil bo'lgan oq cho'kma "
  "massasini toping. (M(C₆H₂Br₃OH)=331)",
  "16,55 g", [("33,1 g", "0,1 mol deb olindi"), ("4,7 g", "bu fenol massasi"),
               ("9,4 g", "cho'kma emas, fenol M i ishlatildi")],
  "n(cho'kma) = n(fenol) = 0,05 → m = 0,05·331 = 16,55 g.",
  dict(arch="chokma_massa_b"))

# 30 (3)
q(3, "yuqori",
  "Fenol haqidagi TO'G'RI fikrlarni tanlang: 1) OH bevosita benzol halqasida; 2) suvli eritmasi "
  "kuchsiz kislota; 3) FeCl₃ bilan binafsha rang beradi; 4) natriy bilan reaksiyaga kirishmaydi.",
  "1, 2, 3", [("1, 2, 3, 4", "Na bilan fenolyat hosil qiladi"), ("faqat 1, 3", "kislotaliligi ham bor"),
               ("2, 4", "tuzilishi ham to'g'ri aytilgan")],
  "Fenol Na bilan ham, NaOH bilan ham reaksiyaga kirishadi — 4-fikr xato.",
  dict(arch="fenol_tanlov_b"))

# 31 (3)
check("q31a", 4.6/46 + 3.2/32, 0.2); check("q31b", 0.1*22.4, 2.24)
q(3, "yuqori",
  "4,6 g etanol va 3,2 g metanol aralashmasi ortiqcha natriy bilan reaksiyaga kirishdi. Ajralgan "
  "vodorod hajmini (n.sh.) toping.",
  "2,24 L", [("4,48 L", "H₂ koeffitsiyenti xato"), ("1,12 L", "faqat bittasi hisoblandi"),
              ("2,99 L", "mollar xato qo'shildi")],
  "n = 0,1 + 0,1 = 0,2 mol spirt → n(H₂) = 0,1 → V = 2,24 L.",
  dict(arch="aralashma_na_b"))

# 32 (3)
check("q32", 92/46/2*180, 180)
q(3, "yuqori",
  "Glyukozani bijg'itib 92 g etanol olish uchun necha gramm glyukoza kerak? "
  "(C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂, M(C₆H₁₂O₆)=180)",
  "180 g", [("360 g", "koeffitsiyent teskari olindi"), ("90 g", "2 unutildi"),
             ("46 g", "etanol M i yozildi")],
  "n(etanol) = 2 mol → n(glyukoza) = 1 mol → m = 180 g.",
  dict(arch="bijgish_teskari_b"))

# ---------- Y2: laboratoriya identifikatsiyasi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.4",
  ichki_pasport=[dict(n=33, element="III.4", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=34, element="III.4", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="III.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uchta raqamlanmagan probirkada etanol, glitserin va fenolning suvdagi eritmasi bor. "
               "Ularni faqat kimyoviy sinovlar bilan farqlash kerak. 33–35-savollarga A–F "
               "ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Glitserinni bir qadamda taniydigan sinov qaysi?",
    "34. Fenolni taniydigan eng qulay sinov qaysi?",
    "35. Qolgan probirkadagi etanolni tasdiqlovchi sinov qaysi?"],
  javoblar_royxati=["A) Cu(OH)₂ qo'shish — yorqin ko'k eritma",
                    "B) FeCl₃ tomizish — binafsha rang",
                    "C) qizdirilgan CuO sim tushirish — o'tkir hidli aldegid, sim yaltiraydi",
                    "D) lakmus tomizish — qizil rang",
                    "E) natriy tashlash — gaz ajralishi",
                    "F) AgNO₃ qo'shish — oq cho'kma"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="fenol shunchalik kuchsizki, lakmusni qizartira olmaydi"),
                   dict(variant="E", xato="Na uchchala eritma (suv!) bilan gaz beradi — farqlamaydi"),
                   dict(variant="F", xato="bu galogenidlar sinovi, spirtlarga aloqasi yo'q")],
  yechim=("Glitserin — ko'p atomli: Cu(OH)₂ ko'k glitserat (A). Fenol — FeCl₃ binafsha kompleks (B). "
          "Etanol — CuO da aldegidgacha oksidlanadi (C). Na va lakmus farqlamaydi."),
  parametrlar=dict(arch="lab_identifikatsiya_b"))

# ---------- O1 (Spectrum uslubi) ----------
check("o36", 0.25*94, 23.5)
check("o37", 92/46*2*22.4, 89.6)
check("o38", 9.2/46*22.4, 4.48)
check("o39", 18.8/94*331, 66.2)
check("o40", 0.3*3/2*22.4, 10.08)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,25 mol fenolning massasini (g) toping. (M=94)",
      javob="23,5", yechim="m = 0,25·94 = 23,5 g.",
      parametrlar=dict(arch="fenol_massa_o1_b")),
 dict(n=37, qiyinlik=3, kognitiv="o'rta",
      savol="92 g etanol to'liq yonganda hosil bo'lgan CO₂ hajmini (n.sh., L) toping.",
      javob="89,6", yechim="n = 2 mol → n(CO₂) = 4 mol → V = 89,6 L.",
      parametrlar=dict(arch="etanol_yonish_o1_b")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayon bo'yicha: 9,2 g etanol konsentrlangan H₂SO₄ bilan qizdirilganda "
            "(t>170 °C) hosil bo'ladigan etilen hajmini (n.sh., L) toping.",
      javob="4,48", yechim="n = 0,2 mol → n(C₂H₄) = 0,2 → V = 4,48 L.",
      parametrlar=dict(arch="sxema_degidratatsiya_b"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="18,8 g fenol ortiqcha bromli suv bilan reaksiyaga kirishganda hosil bo'lgan "
            "2,4,6-tribromfenol massasini (g) toping. (M=331)",
      javob="66,2", yechim="n = 0,2 mol → m = 0,2·331 = 66,2 g.",
      parametrlar=dict(arch="tribromfenol_o1_b")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="0,3 mol glitserin ortiqcha natriy bilan to'liq reaksiyaga kirishganda ajralgan "
            "vodorod hajmini (n.sh., L) toping.",
      javob="10,08", yechim="Uch OH: n(H₂) = 0,3·3/2 = 0,45 mol → V = 10,08 L.",
      parametrlar=dict(arch="glitserin_na_o1_b")),
]

# ---------- O2 ----------
check("o41b", 90/180, 0.5); check("o41c", 1*46, 46); check("o41d", 1*22.4, 22.4)
check("o43b", 2.24/22.4, 0.1); check("o43c", 14.8/0.2, 74)
O2 = [
 dict(n=41, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "90 g glyukoza spirtli bijg'ishga uchradi (chiqish 100 % deb olinadi)."),
      bandlar=[
        dict(savol="a) Bijg'ish tenglamasini yozing.",
             yechim=["C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂."], M=4, A=2),
        dict(savol="b) Glyukoza mol miqdorini toping.",
             yechim=["n = 90/180 = 0,5 mol."], M=4, A=2),
        dict(savol="c) Hosil bo'lgan etanol massasini hisoblang.",
             yechim=["n(C₂H₅OH) = 1 mol → m = 46 g."], M=4, A=3),
        dict(savol="d) Ajralgan CO₂ hajmini (n.sh.) toping.",
             yechim=["n(CO₂) = 1 mol → V = 22,4 L."], M=3, A=3),
      ],
      rasmiylashtirish="Bijg'ish zanjiri: tenglama → mol → massa → hajm; M15+A10.",
      parametrlar=dict(arch="bijgish_zanjir_o2_b")),
 dict(n=42, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Fenol va etanol — ikkalasida ham OH guruhi bor, lekin xossalari keskin farq qiladi. "
            "Quyidagilarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Nega fenol NaOH bilan reaksiyaga kirishadi, etanol esa kirishmaydi? Halqaning "
                   "OH guruhiga ta'sirini tushuntiring.",
             yechim=["Benzol halqasi O–H bog'idagi elektron zichlikni o'ziga tortadi —",
                     "H oson ajraladi, fenol kuchsiz kislota bo'lib qoladi; alkil radikal esa,",
                     "aksincha, zichlikni itaradi va spirtda kislotalilik deyarli yo'qoladi."], M=13, A=0),
        dict(savol="b) OH guruhining halqaga qanday «javob ta'siri» bor? Buni brom bilan reaksiyada ko'rsating.",
             yechim=["OH halqani faollashtiradi: fenol katalizatorsiz, xona haroratida 3 ta H ni",
                     "bromga almashtiradi (benzol esa faqat katalizator bilan, bitta H)."], M=9, A=0),
        dict(savol="c) Nima uchun bu ikki modda bitta sinfga kiritilmaydi?",
             yechim=["Funksional guruh bir xil, lekin bog'langan radikal tabiati (aromatik/alkil) "
                     "xossani tubdan o'zgartiradi — alohida sinflar."], M=3, A=0),
      ],
      rasmiylashtirish="Fenol-etanol qiyosiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="fenol_etanol_mulohaza_b")),
 dict(n=43, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "14,8 g noma'lum bir atomli to'yingan spirt ortiqcha natriy bilan reaksiyaga kirishganda "
            "2,24 L (n.sh.) vodorod ajraldi."),
      bandlar=[
        dict(savol="a) Reaksiyaning umumiy tenglamasini yozing.",
             yechim=["2R–OH + 2Na → 2R–ONa + H₂↑."], M=4, A=2),
        dict(savol="b) Spirt mol miqdorini toping.",
             yechim=["n(H₂) = 0,1 → n(spirt) = 0,2 mol."], M=4, A=3),
        dict(savol="c) Spirtning molyar massasini va formulasini aniqlang.",
             yechim=["M = 14,8/0,2 = 74 g/mol → C₄H₉OH (butanol)."], M=4, A=3),
        dict(savol="d) Shu tarkibga mos nechta izomer spirt borligini ko'rsating.",
             yechim=["4 ta: butan-1-ol, butan-2-ol, 2-metilpropan-1-ol, 2-metilpropan-2-ol."], M=3, A=2),
      ],
      rasmiylashtirish="Teskari masala: tenglama → mol → M → izomerlar; M15+A10.",
      parametrlar=dict(arch="nomalum_spirt_o2_b")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263404)
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
    d = dict(n=n, tur="Y1", element="III.4", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III4-B", daraja="B", bob=4, bob_nomi="Spirtlar va fenollar",
    manba=("MS spetsifikatsiyasi III.4; Tongotarov-uslub arxetiplar — savollar yangi tuzilgan, "
           "barcha javoblar mustaqil hisoblangan"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
