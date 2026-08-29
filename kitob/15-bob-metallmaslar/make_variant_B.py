# -*- coding: utf-8 -*-
"""15-bob B-varianti: Metallmaslar. Vodorod. Mineral o'g'itlar (II.5) — HAQIQIY MS MUHITI ★★★.
Noma'lum galogen, cheklovchi reagent, sanoat zanjirlari (NH3, HNO3, H2SO4), o'g'it hisoblari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_II5B.json"
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

# 1 (3) — 1-2-3
q(3, "yuqori",
  "Galogenlar haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) tashqi qavatida 7 tadan elektron bor;  2) guruhda pastga oksidlovchilik kuchayadi;  "
  "3) faolroq galogen passivrog'ini tuzidan siqib chiqaradi;  4) vodorod bilan HX tipidagi "
  "birikmalar beradi.",
  "1, 3 va 4",
  [("1, 2 va 3", "oksidlovchilik pastga KAMAYADI"), ("faqat 1 va 4", "3 ham to'g'ri (Cl₂ + KBr)"),
   ("hammasi", "2 noto'g'ri")],
  "ns²np⁵; F > Cl > Br > I; Cl₂ + 2KBr → 2KCl + Br₂; HF...HI.",
  dict(arch="galogen_fikr_tanlov"))

# 2 (3) — noma'lum galogen
check("q2", 1/36.5*100, 2.74, tol=0.01)
q(3, "yuqori",
  "HX tipidagi birikmada vodorodning massa ulushi 2,74 %. X elementni aniqlang.",
  "Cl", [("F", "HF da ω(H) = 5 %"), ("Br", "HBr da ω(H) = 1,23 %"), ("I", "HI da ω(H) = 0,78 %")],
  "M(HX) = 1/0,0274 ≈ 36,5 → M(X) = 35,5 — xlor.",
  dict(arch="nomalum_galogen"))

# 3 (3)
q(3, "yuqori",
  "Laboratoriyada ammiak qanday olinadi?",
  "NH₄Cl va Ca(OH)₂ aralashmasini qizdirib",
  [("azot va vodorodni aralashtirib", "sintez yuqori bosim/katalizator talab qiladi"),
   ("NH₄NO₃ ni suvda eritib", "erish NH₃ ajratmaydi"),
   ("azotni suvda eritib", "N₂ suv bilan reaksiyaga kirishmaydi")],
  "2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃↑ + 2H₂O — «ishqor + ammoniy tuzi» usuli.",
  dict(arch="nh3_lab_olinish"))

# 4 (3)
check("q4", 0.4*22.4, 8.96)
q(3, "yuqori",
  "4NH₃ + 5O₂ → 4NO + 6H₂O (katalizator). 0,4 mol ammiak oksidlanganda hosil bo'lgan NO hajmini "
  "(n.sh.) toping.",
  "8,96 L", [("11,2 L", "nisbat 4:4 = 1:1"), ("4,48 L", "0,2 mol deb olingan"), ("22,4 L", "1 mol uchun")],
  "n(NO) = 0,4 mol → V = 8,96 L — nitrat kislota zanjirining 2-bosqichi.",
  dict(arch="nh3_oksidlanish"))

# 5 (3) — RASMLI: ammiak favvorasi
q(3, "yuqori",
  "Rasmda «ammiak favvorasi» tajribasi: NH₃ to'la kolbaga bir tomchi suv kiritilganda suv kuchli "
  "otilib chiqa boshlaydi. Buning sababi nimada?",
  "NH₃ suvda juda yaxshi erib, kolbada bosim keskin pasayadi",
  [("NH₃ suv bilan portlaydi", "portlash yo'q — erish bor"),
   ("suv NH₃ ni siqib chiqaradi", "aksincha, tashqi bosim suvni ichkariga itaradi"),
   ("kolba qizib ketadi", "harorat emas, bosim farqi sabab")],
  "1 hajm suv ~700 hajm NH₃ ni yutadi → vakuumga yaqin holat → atmosfera suvni «otib» kiritadi.",
  dict(arch="favvora_oqish"), fig="fountain")

# 6 (3)
q(3, "yuqori",
  "Xlor suvda eriganida qanday jarayon boradi va eritma nima uchun oqartirish xossasiga ega?",
  "Cl₂ + H₂O ⇄ HCl + HClO; gipoxlorit kislota kuchli oksidlovchi",
  [("xlor shunchaki eriydi", "qisman kimyoviy reaksiya boradi"),
   ("Cl₂ + H₂O → 2HCl + O₂ to'liq", "bunday to'liq parchalanish yorug'likda sekin boradi"),
   ("xlor suvni muzlatadi", "harorat bilan bog'liq emas")],
  "HClO bo'yoq molekulalarini oksidlab buzadi — «xlorka»ning ishlash asosi.",
  dict(arch="xlorli_suv"))

# 7 (3) — 1-2-3: H2 olinishi
q(3, "yuqori",
  "Qaysi jarayonlarda VODOROD olinadi?\n"
  "1) Zn + HCl;  2) Cu + HCl;  3) suvning elektrolizi;  4) CaCO₃ ni qizdirish;  5) Na + H₂O.",
  "1, 3 va 5",
  [("1, 2 va 3", "Cu kislotadan H₂ ajratmaydi"), ("faqat 1 va 3", "Na + H₂O ham H₂ beradi"),
   ("hammasi", "2 va 4 — yo'q")],
  "Faol metall + kislota/suv va elektroliz — H₂ manbalari; CaCO₃ esa CO₂ beradi.",
  dict(arch="h2_olinish_tanlov"))

# 8 (2)
q(2, "yuqori",
  "Sulfat kislota ishlab chiqarishning KONTAKT usuli bosqichlarini to'g'ri tartibda ko'rsating.",
  "S → SO₂ → SO₃ → H₂SO₄",
  [("S → SO₃ → SO₂ → H₂SO₄", "avval SO₂, keyin katalitik SO₃"),
   ("S → H₂S → SO₂ → H₂SO₄", "vodorod sulfid bosqichi yo'q"),
   ("S → SO₂ → H₂SO₃ → H₂SO₄", "sulfit kislota orqali emas")],
  "Yonish → katalitik oksidlanish (V₂O₅) → absorbsiya (oleum orqali).",
  dict(arch="kontakt_tartib"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi o'g'itlarni beradigan elementi bilan TO'G'RI moslang:\n"
  "[JADVAL] O'g'it | Element ;; a) karbamid CO(NH₂)₂ | 1) K ;; b) superfosfat | 2) N ;; "
  "c) silvinit | 3) P",
  "a—2, b—3, c—1",
  [("a—1, b—2, c—3", "karbamid — azotli"), ("a—2, b—1, c—3", "superfosfat — fosforli"),
   ("a—3, b—2, c—1", "moslashuvlar chalkash")],
  "Karbamid — N (46 %); superfosfat — P; silvinit (KCl·NaCl) — K.",
  dict(arch="ogit_moslash_jadval"))

# 10 (3)
check("q10", 28/80*100, 35)
q(3, "yuqori",
  "Ammiakli selitradagi (NH₄NO₃) azotning massa ulushini toping. (M(NH₄NO₃)=80)",
  "35 %", [("17,5 %", "molekulada IKKITA azot bor"), ("28 %", "bu azot massasi, ulush emas"),
            ("46 %", "bu karbamid ko'rsatkichi")],
  "ω(N) = 2·14/80 = 35 %.",
  dict(arch="selitra_azot"))

# 11 (3) — cheklovchi reagent
check("q11", 0.9/3*2, 0.6)
q(3, "yuqori",
  "0,4 mol azot va 0,9 mol vodorod aralashmasi reaksiyaga kiritildi (N₂ + 3H₂ → 2NH₃, to'liq "
  "unum deb hisoblang). Necha mol ammiak hosil bo'ladi?",
  "0,6", [("0,8", "vodorod yetmaydi — u cheklovchi"), ("1,3", "mollar shunchaki qo'shilgan"),
           ("0,3", "nisbat 3:2, teskari emas")],
  "0,4 mol N₂ ga 1,2 mol H₂ kerak edi; H₂ cheklovchi: n(NH₃) = 0,9·2/3 = 0,6 mol.",
  dict(arch="cheklovchi_nh3"))

# 12 (2)
q(2, "yuqori",
  "Ozon qatlamining Yer hayoti uchun ahamiyati nimada?",
  "Quyoshning zararli ultrabinafsha nurlarini yutadi",
  [("kislorod zaxirasini saqlaydi", "nafas uchun ozon emas, O₂ xizmat qiladi"),
   ("issiqlikni ushlab turadi", "bu — issiqxona gazlari vazifasi"),
   ("yomg'ir hosil qiladi", "ozon yog'ingarchilikka aloqasiz")],
  "Stratosferadagi O₃ UV-B nurlarni yutib, tiriklikni himoya qiladi.",
  dict(arch="ozon_qatlam"))

# 13 (2)
q(2, "yuqori",
  "Konsentrlangan xlorid kislota ochiq idishda nega «tutaydi»?",
  "uchuvchan HCl gazi havo namligi bilan tuman hosil qiladi",
  [("kislota qaynayapti", "xona haroratida qaynamaydi"),
   ("idish qiziyapti", "issiqliksiz ham tutaydi"),
   ("xlor gazi ajralyapti", "ajralayotgani — HCl, Cl₂ emas")],
  "HCl juda uchuvchan: bug'lari nam havoda mayda tomchilar («tuman») beradi.",
  dict(arch="hcl_tutash"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring (oddiy sharoitda):\n"
  "[JADVAL] Galogen | Agregat holati ;; Cl₂ | ? ;; Br₂ | ? ;; I₂ | ?",
  "gaz; suyuqlik; qattiq",
  [("gaz; gaz; suyuqlik", "Br₂ — yagona suyuq metallmas"), ("suyuqlik; qattiq; gaz", "tartib chalkash"),
   ("gaz; qattiq; suyuqlik", "I₂ — qattiq, uchuvchan")],
  "Molekula kattalashgani sari: gaz → suyuq → qattiq.",
  dict(arch="galogen_holat_jadval"))

# 15 (3)
check("q15", 44.8/22.4*17, 34)
q(3, "yuqori",
  "44,8 L (n.sh.) ammiakning massasini toping. (M(NH₃)=17)",
  "34 g", [("17 g", "2 mol bor"), ("22,4 g", "hajm bilan chalkashuv"), ("68 g", "ikki baravar")],
  "n = 2 mol → m = 34 g.",
  dict(arch="nh3_massa_hisob"))

# 16 (2)
q(2, "yuqori",
  "Vodorod sanoatda asosan qanday olinadi?",
  "tabiiy gazni (metanni) suv bug'i bilan konversiya qilib",
  [("faqat rux va kislotadan", "bu laboratoriya usuli — qimmat"),
   ("havoni suyultirib", "havoda H₂ deyarli yo'q"),
   ("neftni haydab", "haydash H₂ ajratmaydi")],
  "CH₄ + H₂O → CO + 3H₂ (konversiya); yana suv elektrolizi ham qo'llanadi.",
  dict(arch="h2_sanoat"))

# 17 (3)
check("q17", 14.2/142*2*98, 19.6)
q(3, "yuqori",
  "P₂O₅ + 3H₂O → 2H₃PO₄. 14,2 g fosfor(V) oksididan olingan kislota massasini toping. "
  "(M: P₂O₅=142, H₃PO₄=98)",
  "19,6 g", [("9,8 g", "koeffitsiyent 2 unutilgan"), ("98 g", "1 mol uchun"), ("39,2 g", "ikki baravar")],
  "n = 0,1 mol → H₃PO₄ 0,2 mol → 19,6 g.",
  dict(arch="h3po4_hisob"))

# 18 (2)
q(2, "yuqori",
  "Qaysi gaz havodan YENGIL va nam lakmus qog'ozni KO'KARTIRADI?",
  "NH₃", [("HCl", "u qizartiradi va og'irroq"), ("CO₂", "kislotali, og'ir"),
           ("Cl₂", "og'ir, oqartiradi")],
  "Ammiak — yagona keng tarqalgan ishqoriy gaz.",
  dict(arch="ishqoriy_gaz"))

# 19 (3) — RASMLI: favvora davomi
q(3, "yuqori",
  "5-savol tajribasida kolbaga otilib kirayotgan suvga fenolftalein qo'shilgan edi. Favvora qanday "
  "rangda bo'ladi va nima uchun?",
  "pushti — NH₃ eritmasi ishqoriy muhit beradi",
  [("rangsiz — muhit neytral", "NH₃·H₂O — asos"),
   ("qizil — muhit kislotali", "kislota yo'q; fenolftalein kislotada rangsiz"),
   ("ko'k — mis ionlari bor", "eritmada mis yo'q")],
  "NH₃ + H₂O ⇄ NH₄⁺ + OH⁻: fenolftalein pushti «favvora» — samarali namoyish.",
  dict(arch="favvora_rang"), fig="fountain")

# 20 (2)
q(2, "yuqori",
  "Oltingugurtning qaysi qo'llanilishi TO'G'RI ko'rsatilgan?",
  "kauchukni vulkanizatsiya qilish",
  [("mikrosxemalar yasash", "u — kremniy"), ("lampochka to'ldirish", "u — inert gazlar"),
   ("ichimlik suvini xlorlash", "u — xlor")],
  "S kauchukka «ko'prik» bog'lar hosil qilib, uni pishiq rezinaga aylantiradi.",
  dict(arch="s_vulkanizatsiya"))

# 21 (3)
check("q21", 0.1*254, 25.4)
q(3, "yuqori",
  "Cl₂ + 2KI → 2KCl + I₂. 0,1 mol xlor to'liq reaksiyaga kirishganda ajralgan yod massasini toping. "
  "(M(I₂)=254)",
  "25,4 g", [("12,7 g", "nisbat 1:1 (mol bo'yicha)"), ("254 g", "1 mol uchun"), ("50,8 g", "ikki baravar")],
  "Faol galogen passivini siqib chiqaradi: n(I₂) = 0,1 → 25,4 g (eritma qo'ng'irlashadi).",
  dict(arch="galogen_siqish_hisob"))

# 22 (3) — 1-2-3: azotli o'g'itlar
q(3, "yuqori",
  "Qaysi moddalar AZOTLI o'g'it hisoblanadi?\n"
  "1) NH₄NO₃;  2) (NH₄)₂SO₄;  3) CO(NH₂)₂;  4) KCl;  5) Ca(H₂PO₄)₂.",
  "1, 2 va 3",
  [("1, 2 va 4", "KCl — kaliyli"), ("faqat 1", "sulfat va karbamid ham azot beradi"),
   ("1, 3 va 5", "superfosfat — fosforli")],
  "Selitra, ammoniy sulfat, karbamid — azot manbalari.",
  dict(arch="azotli_tanlov"))

# 23 (3)
check("q23", 28/60*100, 46.7, tol=0.1)
q(3, "yuqori",
  "Karbamid CO(NH₂)₂ dagi azotning massa ulushini toping. (M=60)",
  "46,7 %", [("23,3 %", "molekulada 2 ta azot"), ("35 %", "bu selitra ko'rsatkichi"),
              ("14 %", "bitta azot massasi bilan chalkashuv")],
  "ω = 28/60 ≈ 46,7 % — eng konsentrlangan azotli o'g'it.",
  dict(arch="karbamid_azot"))

# 24 (2)
q(2, "yuqori",
  "«Qaldiroq gaz» nima?",
  "vodorod va kislorodning 2:1 hajmiy aralashmasi",
  [("toza vodorod", "toza H₂ tinch yonadi"), ("vodorod va azot aralashmasi", "azot yonmaydi"),
   ("metan va havo", "u ham portlaydi, lekin nomi boshqa")],
  "2H₂ + O₂ — uchqundan kuchli portlaydi; nomi shundan.",
  dict(arch="qaldiroq_gaz"))

# 25 (3)
q(3, "yuqori",
  "NO ni NO₂ ga aylantirish uchun qanday shart YETARLI?",
  "havo kislorodi bilan aralashtirish (oddiy sharoitda)",
  [("yuqori bosim va katalizator", "bu NH₃ sintezi sharoiti"),
   ("kuchli qizdirish", "aksincha, qizdirish muvozanatni buzadi"),
   ("suvdan o'tkazish", "NO suvda deyarli erimaydi")],
  "2NO + O₂ → 2NO₂ — rangsiz gaz havoda o'z-o'zidan qo'ng'irlashadi.",
  dict(arch="no_no2"))

# 26 (3) — RASMLI: qaynash grafigi
q(3, "yuqori",
  "Grafikda galogenlarning qaynash haroratlari berilgan. Xona haroratida (25 °C) SUYUQ holatda "
  "bo'lgan galogen qaysi?",
  "Br₂", [("Cl₂", "−34 °C da qaynaydi — xonada gaz"), ("I₂", "xonada qattiq"),
           ("F₂", "−188 °C — gaz")],
  "Br₂: suyuqlanishi −7 °C, qaynashi 59 °C → 25 °C da suyuq (yagona suyuq metallmas).",
  dict(arch="bp_line_oqish"), fig="bp_line")

# 27 (3)
check("q27", 3.2/32*98, 9.8)
q(3, "yuqori",
  "Kontakt usuli bo'yicha (yo'qotishsiz) 3,2 g oltingugurtdan necha gramm sulfat kislota olinadi? "
  "(M: S=32, H₂SO₄=98)",
  "9,8 g", [("98 g", "1 mol uchun"), ("4,9 g", "0,05 mol deb yarim olingan xato"), ("19,6 g", "ikki baravar")],
  "S → SO₂ → SO₃ → H₂SO₄ (1:1:1:1): n = 0,1 mol → m = 9,8 g.",
  dict(arch="kontakt_hisob"))

# 28 (2) — RASMLI: grafik o'qish
q(2, "yuqori",
  "26-savol grafigidan: yod (I₂) xona haroratida qanday holatda bo'ladi?",
  "qattiq (qaynash harorati 184 °C)",
  [("gaz", "gaz bo'lish uchun t(qayn.) xona haroratidan past bo'lishi kerak"),
   ("suyuq", "suyuq galogen — brom"),
   ("plazma", "oddiy sharoitda emas")],
  "I₂ — to'q binafsha qattiq modda; qizdirilsa sublimatlanadi.",
  dict(arch="bp_line_i2"), fig="bp_line")

# 29 (3)
check("q29", 5.6/22.4*2*17, 8.5)
q(3, "yuqori",
  "5,6 L (n.sh.) azot yetarli vodorod bilan to'liq reaksiyaga kirishdi. Hosil bo'lgan ammiak "
  "massasini toping. (M(NH₃)=17)",
  "8,5 g", [("4,25 g", "koeffitsiyent 2 unutilgan"), ("17 g", "1 mol uchun"), ("34 g", "2 mol uchun")],
  "n(N₂) = 0,25 → NH₃ 0,5 mol → m = 8,5 g.",
  dict(arch="nh3_massa_zanjir"))

# 30 (2)
q(2, "yuqori",
  "Oq fosfor qanday saqlanadi va nima uchun?",
  "suv ostida — havoda o'z-o'zidan alangalanadi",
  [("kerosin ostida", "kerosin — ishqoriy metallar uchun"),
   ("ochiq havoda", "40 °C dayoq o'z-o'zidan yonadi"),
   ("ampulada faqat", "suv yetarli himoya")],
  "P₄ suv bilan reaksiyaga kirishmaydi — suv uni havodan to'sadi.",
  dict(arch="fosfor_saqlash"))

# 31 (3)
check("q31", 10.7/53.5*22.4, 4.48)
q(3, "yuqori",
  "2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃ + 2H₂O. 10,7 g ammoniy xlorid to'liq reaksiyaga kirishganda "
  "ajralgan ammiak hajmini (n.sh.) toping. (M(NH₄Cl)=53,5)",
  "4,48 L", [("2,24 L", "nisbat 2:2 = 1:1"), ("22,4 L", "1 mol uchun"), ("8,96 L", "ikki baravar")],
  "n = 0,2 mol → n(NH₃) = 0,2 → V = 4,48 L.",
  dict(arch="nh4cl_nh3_hisob"))

# 32 (3) — RASMLI: grafik hisob
check("q32", 59-(-34), 93)
q(3, "yuqori",
  "26-savol grafigidan: brom va xlor qaynash haroratlari orasidagi farqni toping.",
  "93 °C", [("25 °C", "farq emas"), ("59 °C", "bu bromning o'zi"), ("125 °C", "boshqa juftlik farqi")],
  "59 − (−34) = 93 °C.",
  dict(arch="bp_line_farq"), fig="bp_line")

# ---------- Y2: uch metallmas ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.5",
  ichki_pasport=[dict(n=33, element="II.5", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="II.5", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="II.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch metallmas berilgan: X — sariq qattiq modda, yonganda bo'g'uvchi hidli gaz beradi; "
               "Y — sariq-yashil zaharli gaz, nam rangli matoni oqartiradi; Z — rangsiz gaz, havoning "
               "asosiy qismi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X element qaysi?",
    "34. Y ning suvdagi eritmasi nima deb ataladi?",
    "35. Z dan sanoatda qaysi muhim mahsulot olinadi?"],
  javoblar_royxati=["A) oltingugurt", "B) xlorli suv", "C) ammiak", "D) fosfor",
                    "E) nashatir spirti", "F) kislorod"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="fosfor yonganda oq tutun (P₂O₅) beradi, bo'g'uvchi SO₂ emas"),
                   dict(variant="E", xato="nashatir spirti — NH₃ eritmasi, xlorniki emas"),
                   dict(variant="F", xato="azotdan kislorod olinmaydi — NH₃ sintez qilinadi")],
  yechim=("X — S (yonganda SO₂). Y — Cl₂, eritmasi xlorli suv (B). "
          "Z — N₂: undan Gaber usulida ammiak sintez qilinadi (C)."),
  parametrlar=dict(arch="uch_metallmas_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 0.6/3*2, 0.4); check("o36b", 0.4*0.5*17, 3.4)
check("o37", 6.4/32*98, 19.6)
check("o38", 4.48/22.4*63, 12.6)
check("o39", 160*0.35, 56)
check("o40a", 3.36/22.4/1.5, 0.1); check("o40b", 20-0.1*122.5, 7.75)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="0,3 mol azot va 0,6 mol vodorod aralashmasi reaksiyaga kiritildi; unum 50 %. Hosil "
            "bo'lgan ammiak massasini (g) toping. (M(NH₃)=17)",
      javob="3,4", yechim="H₂ cheklovchi: nazariy NH₃ = 0,4 mol; unum 50 % → 0,2 mol → m = 3,4 g.",
      parametrlar=dict(arch="unum_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="S → SO₂ → SO₃ → H₂SO₄ zanjiri bo'yicha 6,4 g oltingugurtdan (yo'qotishsiz) olingan "
            "kislota massasini (g) toping. (M: S=32, H₂SO₄=98)",
      javob="19,6", yechim="n = 0,2 mol → H₂SO₄ 0,2 mol → m = 19,6 g.",
      parametrlar=dict(arch="kontakt_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi zanjir bo'yicha 4,48 L (n.sh.) ammiakdan (yo'qotishsiz) olingan nitrat "
            "kislota massasini (g) toping. (M(HNO₃)=63)",
      javob="12,6", yechim="NH₃ → NO → NO₂ → HNO₃ (1:1:1:1): n = 0,2 mol → m = 12,6 g.",
      parametrlar=dict(arch="sxema_hno3_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Fermerga 160 kg ammiakli selitra keltirildi (ω(N) = 35 %). Bu o'g'it tuproqqa necha kg "
            "azot beradi?",
      javob="56", yechim="m(N) = 160 · 0,35 = 56 kg.",
      parametrlar=dict(arch="ogit_azot_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="KClO₃ va KCl dan iborat 20 g aralashma qizdirilganda 3,36 L (n.sh.) kislorod ajraldi "
            "(2KClO₃ → 2KCl + 3O₂). Boshlang'ich aralashmadagi KCl massasini (g) toping. "
            "(M(KClO₃)=122,5)",
      javob="7,75", yechim="n(O₂) = 0,15 → n(KClO₃) = 0,1 mol → 12,25 g → m(KCl) = 20 − 12,25 = 7,75 g.",
      parametrlar=dict(arch="kclo3_aralashma_zanjir")),
]

# ---------- O2 ----------
check("o41b", 0.2*2*17, 6.8)
check("o41c", 0.4*63, 25.2)
check("o41d", 25.2*0.8, 20.16)
check("o43a", 2*14/132*100, 21.2, tol=0.1)
check("o43c", 500*0.467, 233.5, tol=1)
O2 = [
 dict(n=41, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Zavodda azotdan nitrat kislota olinadi: N₂ → NH₃ → NO → NO₂ → HNO₃. Bandlar ketma-ket "
            "yechiladi."),
      bandlar=[
        dict(savol="a) Birinchi bosqich (ammiak sintezi) tenglamasini va sharoitlarini yozing.",
             yechim=["N₂ + 3H₂ ⇄ 2NH₃ — yuqori bosim, ~450 °C, temir katalizator."], M=4, A=2),
        dict(savol="b) 0,2 mol azotdan (yo'qotishsiz) olinadigan ammiak massasini toping. (M(NH₃)=17)",
             yechim=["n(NH₃) = 0,4 mol → m = 6,8 g."], M=4, A=3),
        dict(savol="c) Shu ammiakdan zanjir bo'yicha olinadigan HNO₃ massasini hisoblang. (M(HNO₃)=63)",
             yechim=["NH₃ → HNO₃ (1:1): n = 0,4 mol → m = 25,2 g."], M=4, A=3),
        dict(savol="d) Agar umumiy unum 80 % bo'lsa, amalda olinadigan kislota massasini toping.",
             yechim=["m = 25,2 · 0,8 = 20,16 g."], M=3, A=2),
      ],
      rasmiylashtirish="HNO₃ zanjiri: sintez → NH₃ → kislota → unum; M15+A10.",
      parametrlar=dict(arch="hno3_o2_zanjir")),
 dict(n=42, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Azot elementining «paradoksi» tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega azot oddiy sharoitda deyarli hech narsa bilan reaksiyaga kirishmaydi, "
                   "lekin azot birikmalari (nitratlar, NH₃) juda faol? Molekula tuzilishi asosida "
                   "tushuntiring.",
             yechim=["N≡N uch bog'ining energiyasi juda katta (945 kJ/mol) — uni uzish qiyin.",
                     "Birikmalarda esa bunday to'siq yo'q: azot atomi turli darajalarda faol qatnashadi."], M=13, A=0),
        dict(savol="b) Tabiatda azot qanday yo'llar bilan «bog'lanadi»?",
             yechim=["Chaqmoq (N₂ + O₂ → NO) va tuganak bakteriyalar (dukkakli o'simliklar ildizida)."], M=9, A=0),
        dict(savol="c) Sanoatda azotni bog'lash usulining nomini yozing.",
             yechim=["Gaber(-Bosh) usuli — ammiak sintezi."], M=3, A=0),
      ],
      rasmiylashtirish="Azot-paradoks (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="azot_paradoks_mulohaza")),
 dict(n=43, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Uch azotli o'g'it solishtiriladi:\n"
            "[JADVAL] O'g'it | Formula | M ;; selitra | NH₄NO₃ | 80 ;; ammoniy sulfat | (NH₄)₂SO₄ | 132 ;; "
            "karbamid | CO(NH₂)₂ | 60\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir o'g'itdagi azotning massa ulushini hisoblang.",
             yechim=["Selitra: 28/80 = 35 %; ammoniy sulfat: 28/132 ≈ 21,2 %; karbamid: 28/60 ≈ 46,7 %."], M=6, A=3),
        dict(savol="b) Azotga eng boy o'g'itni aniqlang.",
             yechim=["Karbamid — 46,7 %."], M=2, A=2),
        dict(savol="c) 500 kg karbamid tuproqqa qancha azot berishini toping.",
             yechim=["m(N) = 500 · 0,467 ≈ 233,5 kg."], M=4, A=3),
        dict(savol="d) Nega bir xil massa uchun karbamid tashish iqtisodiy foydali?",
             yechim=["Har kg da azot ko'p — tashish va saqlash xarajati birlik azotga kam tushadi."], M=3, A=2),
      ],
      rasmiylashtirish="O'g'it-taqqoslash: ω(N) → tanlash → hisob → iqtisod; M15+A10.",
      parametrlar=dict(arch="ogit_taqqos_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261505)
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
    d = dict(n=n, tur="Y1", element="II.5", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II5-B", daraja="B", bob=15, bob_nomi="Metallmaslar. Vodorod. Mineral o'g'itlar",
    manba=("Tongotarov/DTM metalmaslar banki arxetiplari (noma'lum galogen, cheklovchi reagent, "
           "sanoat zanjirlari, o'g'it hisoblari) va Spectrum uslubidagi 36–43 — javoblar mustaqil "
           "tekshirilgan; MS spetsifikatsiyasi II.5"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: ammiak favvorasi, kontakt va HNO₃ zanjirlari, "
          "unum va aralashma masalalari."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
