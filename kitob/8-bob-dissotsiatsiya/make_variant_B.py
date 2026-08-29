# -*- coding: utf-8 -*-
"""8-bob B-varianti: Elektrolitik dissotsiatsiya va pH (I.8) — HAQIQIY MS MUHITI ★★★.
pH hisoblari, ion tenglamalar, dissotsiatsiya darajasi, o'tkazuvchanlik egri chizig'i."""
import json, random, math

OUT = "mavzu_I8B.json"
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

# 1 (3) — kuchli elektrolitlar qatori
q(3, "yuqori",
  "Qaysi qatorda FAQAT kuchli elektrolitlar berilgan?",
  "HCl, NaOH, K₂SO₄",
  [("CH₃COOH, HCl, NaCl", "sirka kislota — kuchsiz elektrolit"),
   ("NaOH, NH₄OH, KCl", "NH₄OH — kuchsiz asos"),
   ("H₂S, H₂SO₄, KOH", "H₂S — kuchsiz kislota")],
  "Kuchli: barcha ishqorlar, HCl/HBr/HI/HNO₃/H₂SO₄ va eruvchan tuzlar. CH₃COOH, NH₄OH, H₂S — kuchsiz.",
  dict(arch="kuchli_qator"))

# 2 (3) — ionlar soni hisob
check("q2", 0.2*5, 1.0)
q(3, "yuqori",
  "0,2 mol Al₂(SO₄)₃ to'liq dissotsiatsiyalanganda eritmada jami necha mol ion hosil bo'ladi?",
  "1", [("0,2", "har formula birligi 5 ta ion berishi unutilgan"), ("0,4", "faqat kationlar hisoblangan"),
         ("0,6", "faqat anionlar hisoblangan")],
  "Al₂(SO₄)₃ → 2Al³⁺ + 3SO₄²⁻ (5 ion) → 0,2·5 = 1 mol ion.",
  dict(arch="ion_soni", mol=0.2))

# 3 (2) — noelektrolit
q(2, "yuqori",
  "Quyidagilardan qaysi biri NOELEKTROLIT?",
  "glyukoza eritmasi",
  [("osh tuzi eritmasi", "kuchli elektrolit"), ("xlorid kislota", "kuchli elektrolit"),
   ("kaliy ishqori eritmasi", "kuchli elektrolit")],
  "Glyukoza (shakar kabi) molekulalar holida eriydi — ionlarga ajralmaydi, tok o'tkazmaydi.",
  dict(arch="noelektrolit"))

# 4 (3) — grafik tanlash: suyultirishda alfa
q(3, "yuqori",
  "Kuchsiz kislota eritmasi suv bilan suyultirib borilganda uning dissotsiatsiya darajasi (α) "
  "qanday o'zgaradi? To'g'ri grafikni tanlang.",
  "ortib boradi",
  [("kamayib boradi", "suyultirishda ionlarning qayta birikishi qiyinlashadi — α ortadi"),
   ("o'zgarmaydi", "α konsentratsiyaga bog'liq (Ostvald qonuni)"),
   ("avval ortib, keyin kamayadi", "monoton ortadi (1 ga intiladi)")],
  "Suyultirilganda ionlar uchrashib qayta birikishi kamayadi — α ortadi (cheksiz suyultirishda 1 ga intiladi).",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="rise_fall", xlab="suyultirish", ylab="α"),
  params=dict(arch="alfa_grafik"))

# 5 (3) — RASMLI: o'tkazuvchanlik egri chizig'i
q(3, "yuqori",
  "H₂SO₄ eritmasiga tomchilab Ba(OH)₂ eritmasi qo'shib borildi; elektr o'tkazuvchanlikning o'zgarishi "
  "rasmda berilgan. Egri chiziqning MINIMAL nuqtasida (M) eritmada qanday holat yuzaga keladi?",
  "ionlar deyarli qolmaydi: BaSO₄↓ va H₂O hosil bo'lgan",
  [("kislota ortiqcha bo'lib qoladi", "unda o'tkazuvchanlik hali yuqori bo'lardi"),
   ("ishqor ortiqcha bo'lib qoladi", "minimumdan KEYIN ishqor ortadi"),
   ("eritma qaynay boshlaydi", "harorat emas, ion konsentratsiyasi hal qiluvchi")],
  "Ba²⁺+SO₄²⁻→BaSO₄↓ va H⁺+OH⁻→H₂O: ekvivalent nuqtada erkin ionlar deyarli yo'q — tok minimal.",
  dict(arch="otkazuvchanlik_minimal"), fig="cond_curve")

# 6 (3) — pH hisob
check("q6", -math.log10(1e-3), 3)
q(3, "yuqori",
  "Eritmada [H⁺] = 10⁻³ mol/l bo'lsa, uning pH qiymatini toping.",
  "3", [("11", "pOH hisoblangan"), ("−3", "ishora xatosi"), ("0,001", "kontsentratsiyaning o'zi")],
  "pH = −lg[H⁺] = −lg10⁻³ = 3 (kislotali muhit).",
  dict(arch="ph_hisob"))

# 7 (3) — pH dan [OH-]
check("q7", 1e-14/1e-4, 1e-10)
q(3, "yuqori",
  "Eritmaning pH = 4 bo'lsa, undagi gidroksid-ionlar konsentratsiyasini toping (mol/l).",
  "10⁻¹⁰", [("10⁻⁴", "bu [H⁺] qiymati"), ("10⁻⁷", "neytral muhit qiymati"),
             ("10¹⁰", "manfiy daraja unutilgan")],
  "[H⁺] = 10⁻⁴ → [OH⁻] = 10⁻¹⁴/10⁻⁴ = 10⁻¹⁰ mol/l.",
  dict(arch="oh_topish"))

# 8 (2) — fenolftalein
q(2, "yuqori",
  "Fenolftalein qaysi muhitda TO'Q PUSHTI rangga kiradi?",
  "ishqoriy (pH > 8)",
  [("kislotali", "kislotada rangsiz qoladi"), ("neytral", "neytralda ham rangsiz"),
   ("har qanday muhitda", "faqat ishqoriyda rang beradi")],
  "Fenolftalein — ishqor indikatori: OH⁻ ko'p muhitda pushti, boshqasida rangsiz.",
  dict(arch="fenolftalein"))

# 9 (2) — ion almashinish sharti
q(2, "yuqori",
  "Ion almashinish reaksiyasi OXIRIGACHA borishi uchun qanday shart bajarilishi kerak?",
  "cho'kma, gaz yoki kam dissotsiatsiyalanuvchi modda hosil bo'lishi",
  [("harorat ko'tarilishi", "issiqlik shart emas"),
   ("katalizator qo'shilishi", "ion reaksiyalari katalizatorsiz tez boradi"),
   ("eritmaning rangli bo'lishi", "rang mezon emas")],
  "Ionlar muhitdan chiqib ketishi kerak: cho'kma (AgCl), gaz (CO₂), suv kabi kuchsiz elektrolit.",
  dict(arch="almashinish_shart"))

# 10 (3) — qisqa ion tenglama
q(3, "yuqori",
  "Har qanday kuchli kislota va ishqor orasidagi neytrallanishning QISQA ion tenglamasi qaysi?",
  "H⁺ + OH⁻ → H₂O",
  [("Na⁺ + Cl⁻ → NaCl", "bu ionlar eritmada erkin qoladi"),
   ("H⁺ + Cl⁻ → HCl", "HCl kuchli — ionlarga ajralgan holda qoladi"),
   ("2H⁺ + O²⁻ → H₂O", "eritmada O²⁻ ioni bo'lmaydi")],
  "Kuchli kislota/ishqor to'liq dissotsiatsiyalangan; mohiyat — H⁺ va OH⁻ dan suv hosil bo'lishi.",
  dict(arch="qisqa_ion"))

# 11 (3) — OH mol hisob
check("q11", 0.1*2, 0.2)
q(3, "yuqori",
  "0,1 mol bariy gidroksid to'liq dissotsiatsiyalanganda necha mol gidroksid-ion hosil bo'ladi?",
  "0,2", [("0,1", "2 ta OH⁻ berishi unutilgan"), ("0,3", "3 ion jami — OH⁻ emas"),
           ("0,05", "bo'lish xatosi")],
  "Ba(OH)₂ → Ba²⁺ + 2OH⁻ → 0,1·2 = 0,2 mol OH⁻.",
  dict(arch="oh_mol"))

# 12 (2) — suv ion ko'paytmasi
q(2, "yuqori",
  "25 °C da suvning ion ko'paytmasi [H⁺]·[OH⁻] nimaga teng?",
  "10⁻¹⁴", [("10⁻⁷", "bu neytral muhitdagi [H⁺]"), ("10⁻¹", "asossiz qiymat"), ("14", "daraja unutilgan")],
  "Kw = [H⁺][OH⁻] = 10⁻¹⁴ — har qanday suvli eritmada o'rinli.",
  dict(arch="kw"))

# 13 (3) — 1-2-3: cho'kmali juftlar
q(3, "yuqori",
  "Qaysi eritma juftlari aralashtirilganda ion almashinish reaksiyasi OXIRIGACHA boradi?\n"
  "1) BaCl₂ + Na₂SO₄;  2) NaCl + KNO₃;  3) Na₂CO₃ + HCl;  4) KOH + NaNO₃.",
  "1 va 3",
  [("1 va 2", "2-juftda barcha ionlar eritmada qoladi"),
   ("2 va 4", "ikkala juftda ham yangi mahsulot yo'q"),
   ("faqat 1", "3-juftda gaz (CO₂) ajraladi — reaksiya boradi")],
  "1: BaSO₄↓; 3: CO₂↑ + H₂O. 2 va 4 da cho'kma/gaz/suv yo'q — reaksiya bormaydi.",
  dict(arch="juft_tanlov"))

# 14 (3) — JADVALLI: lampochka tajribasi
q(3, "yuqori",
  "Bir xil konsentratsiyali eritmalarda lampochka yorqinligi tekshirildi:\n"
  "[JADVAL] Eritma | HCl | CH₃COOH | shakar ;; Lampochka | yorqin | ? | ?\n"
  "«?» kataklarni mos ravishda to'ldiring.",
  "xira va yonmaydi",
  [("yorqin va xira", "shakar umuman ion bermaydi"),
   ("yonmaydi va xira", "sirka kislota qisman dissotsiatsiyalanadi — xira yonadi"),
   ("xira va yorqin", "noelektrolitda lampochka yonmaydi")],
  "CH₃COOH — kuchsiz (oz ion, xira); shakar — noelektrolit (yonmaydi).",
  dict(arch="lampochka_jadval"))

# 15 (3) — n(H+) hisob
check("q15", 0.01*1, 0.01)
q(3, "yuqori",
  "pH = 2 bo'lgan 1 l eritmada necha mol vodorod ioni bor?",
  "0,01", [("2", "pH ning o'zi olingan"), ("0,001", "pH=3 qiymati"), ("0,1", "pH=1 qiymati")],
  "[H⁺] = 10⁻² = 0,01 mol/l; V = 1 l → n = 0,01 mol.",
  dict(arch="nh_hisob"))

# 16 (2) — kuchsiz elektrolit
q(2, "yuqori",
  "Quyidagilardan qaysi biri KUCHSIZ elektrolit?",
  "CH₃COOH", [("HNO₃", "kuchli kislota"), ("Ba(OH)₂", "ishqor — kuchli"), ("K₂SO₄", "eruvchan tuz — kuchli")],
  "Sirka kislota qisman dissotsiatsiyalanadi (α ≈ 1% atrofida).",
  dict(arch="kuchsiz_tanlash"))

# 17 (3) — JADVALLI: pH jadvali tahlili
q(3, "yuqori",
  "Uch eritmaning pH qiymatlari jadvalda:\n"
  "[JADVAL] Eritma | X | Y | Z ;; pH | 2 | 8 | 12\n"
  "Qaysi xulosa TO'G'RI?",
  "X — kislotali, Y — kuchsiz ishqoriy, Z — kuchli ishqoriy",
  [("X — ishqoriy, Z — kislotali", "pH < 7 kislotali, pH > 7 ishqoriy"),
   ("Y — neytral", "pH = 8 > 7 — kuchsiz bo'lsa-da ishqoriy"),
   ("hammasi kislotali", "faqat X kislotali")],
  "pH 2 — kuchli kislotali; 8 — kuchsiz ishqoriy; 12 — kuchli ishqoriy.",
  dict(arch="ph_jadval"))

# 18 (2) — lakmus
q(2, "yuqori",
  "Lakmus kislotali muhitda qanday rangga kiradi?",
  "qizil", [("ko'k", "ishqoriy muhit rangi"), ("sariq", "metilorange emas, lakmus haqida gap"),
             ("rangsiz", "lakmus rangsizlanmaydi")],
  "Lakmus: kislotada qizil, neytralda binafsha, ishqorda ko'k.",
  dict(arch="lakmus"))

# 19 (3) — aralashtirish pH
check("q19", (0.2-0.1)/1, 0.1)
q(3, "yuqori",
  "Rasmdagi titrlash qurilmasida kolbadagi 1 l eritmada 0,2 mol HCl bor; byuretkadan unga jami "
  "0,1 mol NaOH quyildi. Hosil bo'lgan eritmaning pH ini toping.",
  "1", [("7", "kislota ortiqcha qolganini e'tiborsiz"), ("13", "ishqor ortiqcha deb olingan"),
         ("2", "qoldiq 0,01 M deb olingan")],
  "H⁺ qoldiq = 0,2 − 0,1 = 0,1 mol → [H⁺] = 0,1 → pH = 1.",
  dict(arch="aralash_ph"), fig="burette")

# 20 (2) — alfa ta'rifi
q(2, "yuqori",
  "Dissotsiatsiya darajasi (α) nimani ko'rsatadi?",
  "ionlarga ajralgan molekulalar ulushini",
  [("eritmadagi ionlar zaryadini", "zaryad emas, ulush"),
   ("eritmaning zichligini", "zichlik alohida kattalik"),
   ("erigan modda massasini", "massa emas, nisbat")],
  "α = (dissotsiatsiyalangan mol) / (erigan jami mol); kuchlilarda α → 1.",
  dict(arch="alfa_tarif"))

# 21 (3) — alfa hisob
check("q21", 100*0.005/0.5, 1)
q(3, "yuqori",
  "0,5 mol sirka kislotadan eritmada 0,005 moli ionlarga ajralgan. Dissotsiatsiya darajasini (%) toping.",
  "1", [("0,5", "jami mol bilan chalkashuv"), ("10", "o'n barobar xato"), ("0,01", "foizga o'tkazilmagan")],
  "α = 0,005/0,5 = 0,01 → 1%.",
  dict(arch="alfa_hisob"))

# 22 (3) — 1-2-3: pH ni kamaytiruvchi
q(3, "yuqori",
  "Qaysi amallar eritmaning pH qiymatini KAMAYTIRADI?\n"
  "1) HCl qo'shish;  2) NaOH qo'shish;  3) CO₂ gazini eritish;  4) suv qo'shish (kislotali eritmaga).",
  "1 va 3",
  [("2 va 4", "NaOH pH ni oshiradi; suv kislotali eritmani neytralga yaqinlashtiradi (pH ortadi)"),
   ("faqat 1", "CO₂ ham suvda H₂CO₃ hosil qilib pH ni tushiradi"),
   ("1, 3 va 4", "kislotani suyultirish pH ni oshiradi")],
  "H⁺ manbalari pH ni tushiradi: HCl va CO₂ (H₂CO₃). NaOH va suyultirish — oshiradi.",
  dict(arch="ph_kamaytirish"))

# 23 (3) — tuz muhiti (ishqoriy)
q(3, "yuqori",
  "Qaysi tuzning suvdagi eritmasi ISHQORIY muhit ko'rsatadi?",
  "Na₂CO₃", [("NaCl", "kuchli+kuchli — neytral"), ("NH₄Cl", "kuchsiz asos qoldig'i — kislotali"),
              ("KNO₃", "kuchli+kuchli — neytral")],
  "Na₂CO₃ — kuchli asos + kuchsiz kislota tuzi: karbonat-ion suvdan H⁺ tortib OH⁻ qoldiradi (pH > 7). "
  "Shu bois soda eritmasi «ishqorday» seziladi.",
  dict(arch="tuz_muhit"))

# 24 (2) — neytral tuz
q(2, "yuqori",
  "Qaysi tuzning eritmasi NEYTRAL muhitga ega?",
  "NaCl", [("Na₂CO₃", "ishqoriy (soda)"), ("NH₄Cl", "kislotali"), ("K₂S", "ishqoriy")],
  "Kuchli asos + kuchli kislota tuzi ionlari suv bilan ta'sirlashmaydi — pH = 7.",
  dict(arch="neytral_tuz"))

# 25 (3) — ion mol hisob
check("q25", 0.1*4, 0.4)
q(3, "yuqori",
  "0,1 mol natriy fosfat (Na₃PO₄) to'liq dissotsiatsiyalanganda hosil bo'ladigan JAMI ionlar mol sonini toping.",
  "0,4", [("0,3", "faqat Na⁺ hisoblangan"), ("0,1", "1 ta ion deb olingan"), ("0,5", "5 ion xato")],
  "Na₃PO₄ → 3Na⁺ + PO₄³⁻ (4 ion) → 0,1·4 = 0,4 mol.",
  dict(arch="ion_mol"))

# 26 (3) — kuchli vs kuchsiz pH
q(3, "yuqori",
  "Bir xil molyar konsentratsiyali (0,1 M) HCl va CH₃COOH eritmalarining pH lari haqida to'g'ri xulosa qaysi?",
  "HCl niki kichikroq — u to'liq dissotsiatsiyalangan",
  [("ikkalasi teng", "sirka qisman ajraladi — [H⁺] kam"),
   ("CH₃COOH niki kichikroq", "kuchsiz kislotada H⁺ kamroq"),
   ("taqqoslab bo'lmaydi", "α ni bilgan holda taqqoslash mumkin")],
  "HCl: [H⁺] = 0,1 → pH = 1; sirka: [H⁺] ≪ 0,1 → pH ≈ 3. Kuchli kislota pH i kichik.",
  dict(arch="kuchli_kuchsiz"))

# 27 (3) — [H+] nisbati
check("q27", 10**(5-2), 1000)
q(3, "yuqori",
  "pH = 2 va pH = 5 bo'lgan eritmalarda vodorod ionlari konsentratsiyalari necha marta farq qiladi?",
  "1000", [("3", "pH lar ayirmasi olingan"), ("100", "10² xato"), ("2,5", "nisbat asossiz")],
  "Har pH birligi — 10 marta: 10⁽⁵⁻²⁾ = 1000 marta (pH=2 da H⁺ ko'p).",
  dict(arch="h_nisbat"))

# 28 (2) — RASMLI: pH shkalasi
q(2, "yuqori",
  "Rasmdagi pH shkalasidan foydalaning: pH = 11 bo'lgan eritma qanday muhitga mos keladi?",
  "ishqoriy",
  [("kislotali", "pH > 7 — ishqoriy tomon"), ("neytral", "neytral faqat pH = 7"),
   ("aniqlab bo'lmaydi", "shkala aynan muhitni ko'rsatadi")],
  "pH > 7 — ishqoriy: 11 — ancha kuchli ishqoriy muhit (masalan, ammiak eritmasi).",
  dict(arch="shkala_oqish"), fig="ph_scale")

# 29 (3) — formula
q(3, "yuqori",
  "Vodorod ko'rsatkichi (pH) qaysi ifoda bilan aniqlanadi?",
  "pH = −lg[H⁺]",
  [("pH = lg[H⁺]", "manfiy ishora tushib qolgan"), ("pH = −lg[OH⁻]", "bu pOH ifodasi"),
   ("pH = [H⁺]·[OH⁻]", "bu ion ko'paytmasi (Kw)")],
  "pH — vodorod ioni konsentratsiyasining manfiy o'nli logarifmi.",
  dict(arch="ph_formula"))

# 30 (2) — o'tkazuvchanlik sababi
q(2, "yuqori",
  "Elektrolit eritmalari nima hisobiga elektr tokini o'tkazadi?",
  "erkin harakatlanuvchi ionlar hisobiga",
  [("erkin elektronlar hisobiga", "elektron o'tkazuvchanlik metallarga xos"),
   ("suv molekulalari hisobiga", "sof suv deyarli o'tkazmaydi"),
   ("erigan gazlar hisobiga", "gazlar odatda ion bermaydi")],
  "Dissotsiatsiyada hosil bo'lgan kation va anionlar zaryad tashuvchilardir.",
  dict(arch="otkazish_sabab"))

# 31 (3) — NaOH dan pH
check("q31", 4/40/1, 0.1)
q(3, "yuqori",
  "4 g NaOH suvda eritilib, 1 l eritma tayyorlandi. Eritmaning pH ini toping. (M(NaOH)=40)",
  "13", [("1", "pOH ning o'zi"), ("12", "0,01 M xato"), ("7", "neytral deb olingan")],
  "c = 0,1 M → [OH⁻] = 0,1 → pOH = 1 → pH = 14 − 1 = 13.",
  dict(arch="naoh_ph"))

# 32 (3) — RASMLI: egri chiziqning davomi
q(3, "yuqori",
  "5-savoldagi grafikda minimal (M) nuqtadan KEYIN o'tkazuvchanlik yana orta boshlaydi. Buning sababi nimada?",
  "ortiqcha qo'shilgan Ba(OH)₂ ionlari eritmada to'plana boradi",
  [("BaSO₄ cho'kmasi eriy boshlaydi", "BaSO₄ amalda erimaydi"),
   ("suv ionlarga ajralib ketadi", "suvning dissotsiatsiyasi juda kichik"),
   ("harorat ko'tarilib ketadi", "sabab ion konsentratsiyasida")],
  "Ekvivalentlikdan keyin H⁺ qolmaydi: endi har tomchi Ba²⁺ va OH⁻ erkin ion qo'shadi — tok ortadi.",
  dict(arch="otkazuvchanlik_davom"), fig="cond_curve")

# ---------- Y2: uch eritma ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.8",
  ichki_pasport=[dict(n=33, element="I.8", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.8", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.8", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uchta bir xil ko'rinishdagi eritma berilgan: X (pH = 1), Y (pH = 7), Z (pH = 13); "
               "ular 0,1 M li HCl, NaCl va NaOH eritmalari ekani ma'lum (qaysi biri qaysi — noma'lum). "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X eritma qaysi modda?",
    "34. Z eritmaga fenolftalein tomizilsa nima kuzatiladi?",
    "35. X va Z teng hajmda aralashtirilsa, hosil bo'lgan eritmaning pH i qancha bo'ladi?"],
  javoblar_royxati=["A) HCl", "B) to'q pushti rang", "C) 7", "D) NaOH", "E) rangsiz qoladi", "F) 13"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="NaOH — bu Z eritma (pH=13)"),
                   dict(variant="E", xato="ishqorda fenolftalein rang BERADI"),
                   dict(variant="F", xato="aralashmada ishqor ortiqcha emas — teng mol neytrallanadi")],
  yechim=("pH=1 → kislota: X = HCl (A). Z = NaOH: fenolftalein pushti (B). "
          "Teng hajm, teng c → to'liq neytrallanish: NaCl eritmasi, pH = 7 (C)."),
  parametrlar=dict(arch="uch_eritma_ssenariy"))

# ---------- O1 ----------
check("o36", 1+2, 3)
check("o37", 1e-5, 1e-5)
check("o38", 0.2*3, 0.6)
check("o39", 0.01, 0.01)
check("o40", 0.365/36.5, 0.01)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="Ca(OH)₂ → Ca²⁺ + 2OH⁻ dissotsiatsiya tenglamasida hosil bo'lgan ionlar oldidagi "
            "koeffitsiyentlar yig'indisini toping.",
      javob="3", yechim="1 (Ca²⁺) + 2 (OH⁻) = 3.",
      parametrlar=dict(arch="koef_o1")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="pH = 5 bo'lgan eritmadagi vodorod ionlari konsentratsiyasini yozing (mol/l).",
      javob="10⁻⁵", yechim="[H⁺] = 10⁻pH = 10⁻⁵ mol/l.",
      parametrlar=dict(arch="h_o1")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="0,2 mol K₂SO₄ to'liq dissotsiatsiyalanganda hosil bo'ladigan jami ionlar mol sonini toping.",
      javob="0,6", yechim="K₂SO₄ → 2K⁺ + SO₄²⁻ (3 ion) → 0,2·3 = 0,6 mol.",
      parametrlar=dict(arch="ion_o1")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="pH = 12 bo'lgan 1 l eritmada necha mol gidroksid-ion bor?",
      javob="0,01", yechim="pOH = 2 → [OH⁻] = 10⁻² = 0,01 mol/l → 0,01 mol.",
      parametrlar=dict(arch="oh_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="0,365 g HCl suvda eritilib 1 l eritma tayyorlandi. Eritmaning pH ini toping. (M(HCl)=36,5)",
      javob="2", yechim="c = 0,01 M → [H⁺] = 10⁻² → pH = 2.",
      parametrlar=dict(arch="hcl_ph_o1")),
]

# ---------- O2 ----------
check("o41a", 8/40/2, 0.1)
check("o41d", 0.1/10, 0.01)
check("o43c", 0.01, 0.01)
O2 = [
 dict(n=41, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("8 g NaOH suvda eritilib, 2 l eritma tayyorlandi. Bandlar ketma-ket yechiladi. (M(NaOH)=40)"),
      bandlar=[
        dict(savol="a) Eritmaning molyar konsentratsiyasini toping.",
             yechim=["n = 0,2 mol; c = 0,2/2 = 0,1 M"], M=3, A=1),
        dict(savol="b) Gidroksid-ion konsentratsiyasini va pOH ni aniqlang.",
             yechim=["NaOH kuchli → [OH⁻] = 0,1 → pOH = 1"], M=3, A=2),
        dict(savol="c) Eritmaning pH ini hisoblang.",
             yechim=["pH = 14 − 1 = 13"], M=3, A=2),
        dict(savol="d) Eritma suv bilan 10 marta suyultirilsa, pH qanday o'zgaradi? Hisoblang.",
             yechim=["c = 0,01 M → pOH = 2 → pH = 12 (bir birlikka kamayadi)"], M=3, A=3),
        dict(savol="e) Nega NaOH kuchli elektrolit hisoblanadi? Izohlang.",
             yechim=["Ishqor suvda amalda to'liq ionlarga ajraladi (α ≈ 1): Na⁺ va OH⁻."], M=3, A=2),
      ],
      rasmiylashtirish="pH zanjiri: c → [OH⁻]/pOH → pH → suyultirish → izoh; M15+A10.",
      parametrlar=dict(arch="naoh_zanjir", m=8, V=2)),
 dict(n=42, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Quyidagi reaksiyalar uchun MOLEKULYAR, TO'LIQ ION va QISQA ion tenglamalarni yozish "
            "talab qilinadi: 1) BaCl₂ + Na₂SO₄;  2) Na₂CO₃ + HCl."),
      bandlar=[
        dict(savol="a) Ikkala reaksiya uchun uchala ko'rinishdagi tenglamalarni yozing.",
             yechim=["1) BaCl₂+Na₂SO₄→BaSO₄↓+2NaCl; Ba²⁺+SO₄²⁻→BaSO₄↓",
                     "2) Na₂CO₃+2HCl→2NaCl+H₂O+CO₂↑; CO₃²⁻+2H⁺→H₂O+CO₂↑"], M=13, A=0),
        dict(savol="b) Har bir reaksiya nega oxirigacha borishini qisqa ion tenglamaga tayanib tushuntiring.",
             yechim=["1-da cho'kma (BaSO₄), 2-da gaz (CO₂) va kuchsiz elektrolit (H₂O) —",
                     "ionlar muhitni tark etadi."], M=9, A=0),
        dict(savol="c) Qisqa ion tenglama qanday afzallik beradi?",
             yechim=["Reaksiya mohiyatini ko'rsatadi: bir xil mohiyatli o'nlab molekulyar reaksiyalarni bitta tenglama ifodalaydi."], M=3, A=0),
      ],
      rasmiylashtirish="Ion tenglamalar usuli (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="ion_tenglama_usul")),
 dict(n=43, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch eritma bilan lampochkali asbobda tajriba o'tkazildi; natijalar jadvalda:\n"
            "[JADVAL] Eritma (0,01 M) | Lampochka | pH ;; A | yorqin | 2 ;; B | xira | 3,4 ;; C | yonmaydi | 7\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) A, B, C eritmalarni tavsiflang: qaysi biri kuchli/kuchsiz elektrolit, qaysi biri noelektrolit?",
             yechim=["A — kuchli elektrolit (yorqin, pH past); B — kuchsiz elektrolit (xira);",
                     "C — noelektrolit (yonmaydi, neytral)."], M=5, A=2),
        dict(savol="b) A eritma 0,01 M kuchli kislota ekanini pH orqali isbotlang.",
             yechim=["To'liq dissotsiatsiya: [H⁺] = 0,01 → pH = 2 — jadvaldagi bilan mos."], M=4, A=3),
        dict(savol="c) Nega B ning pH i A nikidan katta, holbuki konsentratsiyalari teng?",
             yechim=["B qisman dissotsiatsiyalanadi (α < 1): [H⁺] < 0,01 → pH > 2."], M=3, A=3),
        dict(savol="d) A, B, C ga mos ravishda bittadan real modda taklif qiling.",
             yechim=["A — HCl; B — CH₃COOH; C — glyukoza (yoki shakar)."], M=3, A=2),
      ],
      rasmiylashtirish="Tajriba-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="lampochka_tahlil")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260808)
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
    d = dict(n=n, tur="Y1", element="I.8", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I8-B", daraja="B", bob=8, bob_nomi="Elektrolitik dissotsiatsiya va pH",
    manba=("MS spetsifikatsiyasi I.8; darslik dissotsiatsiya/pH bo'limlari — savollar yangi tuzilgan, "
           "javoblar mustaqil hisoblangan"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: pH zanjirlari, ion tenglamalar, o'tkazuvchanlik egri "
          "chizig'i, 1-2-3 tanlovlar, jadval-tahlillar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.8") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
