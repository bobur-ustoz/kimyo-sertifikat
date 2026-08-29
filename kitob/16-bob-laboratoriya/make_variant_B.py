# -*- coding: utf-8 -*-
"""16-bob B-varianti: Laboratoriya amaliyoti (IV.1) — HAQIQIY MS MUHITI ★★★.
Usul tanlash tuzoqlari, aralashtirish/suyultirish hisoblari, ko'p bosqichli ajratish.
Laboratoriya banki arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_IV1B.json"
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

# 1 (3) — 1-2-3: filtrlash bilan ajralmaydiganlar
q(3, "yuqori",
  "Qaysi aralashmalarni FILTRLASH bilan ajratib BO'LMAYDI?\n"
  "1) osh tuzi eritmasi;  2) bo'r + suv;  3) spirt + suv;  4) qum + suv.",
  "1 va 3",
  [("2 va 4", "aynan ular filtrlanadi"), ("faqat 1", "spirt-suv ham filtrdan birga o'tadi"),
   ("hammasi", "erimaydigan zarrachali 2 va 4 filtrlanadi")],
  "Filtr faqat erimaydigan zarrachalarni ushlaydi; eritma va aralashuvchi suyuqliklar o'tib ketadi.",
  dict(arch="filtr_tuzoq_tanlov"))

# 2 (3) — aralashtirish
check("q2", (150*0.1+250*0.26)/400*100, 20)
q(3, "yuqori",
  "150 g 10 % li eritma 250 g 26 % li eritma bilan aralashtirildi. Hosil bo'lgan eritmaning "
  "konsentratsiyasini toping.",
  "20 %", [("18 %", "(15+65)/400 = 20 %"), ("36 %", "foizlar shunchaki qo'shilmaydi"),
            ("16 %", "hisob xato")],
  "m(tuz) = 15 + 65 = 80 g; m(eritma) = 400 g → ω = 20 %.",
  dict(arch="aralashtirish_hisob"))

# 3 (3)
q(3, "yuqori",
  "Yod va qum aralashmasidan yodni qanday ajratib olish MAQBUL?",
  "qizdirib sublimatlash — yod bug'i sovuq yuzada kristallanadi",
  [("suvda eritib filtrlash", "yod suvda deyarli erimaydi"),
   ("magnit bilan", "hech biri magnitlanmaydi"),
   ("ajratuvchi voronkada", "quruq aralashma uchun emas")],
  "I₂ sublimatlanadi (qum emas): eng nozik ajratish usullaridan biri.",
  dict(arch="yod_sublimat"))

# 4 (3) — kristallogidratdan eritma
check("q4a", 25/250*160, 16); check("q4b", 16/200*100, 8)
q(3, "yuqori",
  "25 g mis kuporosi (CuSO₄·5H₂O) 175 g suvda eritildi. Eritmadagi CuSO₄ ning massa ulushini "
  "toping. (M: CuSO₄·5H₂O=250, CuSO₄=160)",
  "8 %", [("12,5 %", "kuporos massasi emas, suvsiz tuz olinadi"), ("16 %", "eritma 200 g"),
           ("10 %", "hisob xato")],
  "m(CuSO₄) = 16 g; m(eritma) = 25 + 175 = 200 g → ω = 8 %.",
  dict(arch="kuporos_eritma"))

# 5 (3) — RASMLI: qizdirish egri (aralashma)
q(3, "yuqori",
  "Rasmda ikki suyuqlikning qizdirish egri chiziqlari berilgan: birida aniq plato bor, ikkinchisida "
  "harorat uzluksiz ko'tariladi. Qaysi xulosa TO'G'RI?",
  "platoli — toza modda; platosiz — aralashma",
  [("platoli — aralashma", "toza modda aynan bir haroratda qaynaydi"),
   ("ikkalasi ham toza", "aralashmada qaynash oralig'i «suziladi»"),
   ("grafikdan xulosa chiqarib bo'lmaydi", "qaynash platosi — toza modda belgisi")],
  "Toza modda o'zgarmas t da qaynaydi; aralashma tarkibi o'zgargani sari t ham o'zgaradi.",
  dict(arch="heat_curve_aralashma"), fig="heat_curve")

# 6 (3)
q(3, "yuqori",
  "Spirt (t_qayn = 78 °C) va suv aralashmasini haydashda QABUL kolbasiga avval nima yig'iladi?",
  "spirtga boy fraksiya — u pastroq haroratda qaynaydi",
  [("toza suv", "suv keyin keladi (100 °C)"),
   ("teng aralashma", "haydash aynan boyitib ajratadi"),
   ("hech narsa", "78 °C dan boshlab bug' keladi")],
  "Past t(qayn.)li komponent birinchi haydaladi — fraksiyalab yig'iladi.",
  dict(arch="haydash_fraksiya"))

# 7 (3) — 1-2-3: gaz yig'ish
q(3, "yuqori",
  "Qaysi gazlarni SUV USTIDA yig'ish mumkin?\n"
  "1) H₂;  2) NH₃;  3) O₂;  4) HCl.",
  "1 va 3",
  [("2 va 4", "ular suvda juda yaxshi eriydi — yig'ib bo'lmaydi"),
   ("hammasi", "NH₃ va HCl suvga «singib» ketadi"),
   ("faqat 1", "O₂ ham suvda deyarli erimaydi")],
  "Suv ustida faqat suvda erimaydigan gazlar yig'iladi.",
  dict(arch="gaz_yigish_tanlov"))

# 8 (2)
q(2, "yuqori",
  "Gazlarni QURITISH uchun ular qaysi modda orqali o'tkaziladi?",
  "konsentrlangan H₂SO₄ yoki suvsiz CaCl₂ orqali",
  [("suv orqali", "suv aksincha namlaydi"),
   ("spirt orqali", "spirt bug'i qo'shiladi"),
   ("kir soda eritmasi orqali", "eritma ham nam beradi")],
  "Gigroskopik moddalar suv bug'ini yutadi (NH₃ uchun H₂SO₄ ishlatilmaydi — reaksiyaga kirishadi!).",
  dict(arch="gaz_quritish"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi aralashmalarni ajratish usullari bilan TO'G'RI moslang:\n"
  "[JADVAL] Aralashma | Usul ;; a) benzin + suv | 1) haydash ;; b) spirt + suv | 2) ajratuvchi "
  "voronka ;; c) yod + qum | 3) sublimatlash",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "benzin-suv qatlamlanadi — voronka"), ("a—2, b—3, c—1", "spirt sublimatlanmaydi"),
   ("a—3, b—1, c—2", "moslashuvlar chalkash")],
  "Qatlamlanadiganlar — voronka; aralashuvchilar — haydash; uchuvchan qattiq — sublimatlash.",
  dict(arch="ajratish_moslash_jadval"))

# 10 (3) — bug'latish hisob
check("q10", 300*0.08/200*100, 12)
q(3, "yuqori",
  "300 g 8 % li eritmadan 100 g suv bug'latildi. Yangi konsentratsiyani toping.",
  "12 %", [("8 %", "eritma massasi kamaydi — foiz ortadi"), ("24 %", "uch barobar emas"),
            ("10 %", "hisob xato")],
  "Tuz 24 g o'zgarmadi; eritma 200 g → ω = 12 %.",
  dict(arch="buglatish_hisob"))

# 11 (3) — aralashma tarkibi
check("q11", (20-12)/20*100, 40)
q(3, "yuqori",
  "Qum va osh tuzidan iborat 20 g aralashma suvda eritildi; filtrlab, quritilgan qum massasi 12 g "
  "chiqdi. Aralashmadagi tuzning massa ulushini toping.",
  "40 %", [("60 %", "bu qum ulushi"), ("12 %", "gramm emas, foiz so'ralyapti"),
            ("8 %", "8 g — massa, ulush 40 %")],
  "m(tuz) = 20 − 12 = 8 g → ω = 8/20 = 40 %.",
  dict(arch="aralashma_tarkib_hisob"))

# 12 (2)
q(2, "yuqori",
  "O'lchov silindri (menzurka) va tomizg'ich (pipetka)dan qaysi biri hajmni ANIQROQ o'lchaydi?",
  "pipetka (va byuretka) — aniq hajm uchun mo'ljallangan",
  [("menzurka", "u taxminiy o'lchov uchun"), ("ikkalasi bir xil", "aniqlik sinflari farq qiladi"),
   ("stakan", "stakan belgilari eng taxminiy")],
  "Aniqlik: byuretka/pipetka > o'lchov kolbasi > menzurka > stakan.",
  dict(arch="aniqlik_tartibi"))

# 13 (2)
q(2, "yuqori",
  "Nima uchun laboratoriya shkafidagi reaktiv idishlarining yorlig'i (etiketkasi) doim toza va "
  "o'qiladigan bo'lishi kerak?",
  "moddani adashtirish o'ta xavfli oqibatlarga olib keladi",
  [("chiroyli ko'rinish uchun", "gap estetikada emas — xavfsizlikda"),
   ("tekshiruvchilar uchun", "asosiy sabab — adashmaslik"),
   ("shart emas", "yorliqsiz reaktiv ishlatilmaydi — utilizatsiya qilinadi")],
  "Qoida: yorliqsiz yoki o'qib bo'lmaydigan idishdagi modda ISHLATILMAYDI.",
  dict(arch="yorliq_qoida"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Gaz | Havoga nisbatan | Yig'ish usuli ;; H₂ | yengil | ? ;; CO₂ | og'ir | ?",
  "og'zi pastga; og'zi yuqoriga",
  [("og'zi yuqoriga; og'zi pastga", "teskari"), ("ikkalasi pastga", "og'ir gaz to'kilib ketadi"),
   ("ikkalasi yuqoriga", "yengil gaz uchib chiqadi")],
  "Yengil gaz teskari idishda, og'ir gaz tik idishda yig'iladi.",
  dict(arch="gaz_yigish_jadval"))

# 15 (3) — qo'shish hisob
check("q15", (400*0.15+100)/(400+100)*100, 32)
q(3, "yuqori",
  "400 g 15 % li eritmaga necha gramm tuz qo'shilsa, konsentratsiya 32 % ga yetadi?",
  "100 g", [("68 g", "(60+x)/(400+x) = 0,32 dan x = 100"), ("128 g", "tenglama noto'g'ri yechilgan"),
             ("60 g", "bu boshlang'ich tuz massasi")],
  "60 + x = 0,32(400 + x) → 0,68x = 68 → x = 100 g.",
  dict(arch="tuz_qoshish_hisob"))

# 16 (2)
q(2, "yuqori",
  "Qattiq ishqor (NaOH) donachalarini tortishda qaysi qoidaga amal qilinadi?",
  "to'g'ridan-to'g'ri tarozi pallasiga emas, soat oynasi/stakanchada tortiladi",
  [("qog'ozga solib tortiladi", "gigroskopik ishqor qog'ozni ho'llab teshadi"),
   ("qo'lda ushlab tortiladi", "kuydiradi!"),
   ("farqi yo'q", "pallani yemiradi va namlanadi")],
  "NaOH nam tortadi va yemiradi — faqat shisha idishchada, tez tortiladi.",
  dict(arch="ishqor_tortish"))

# 17 (3) — zichlikli hisob
check("q17", 200*1.1*0.2, 44)
q(3, "yuqori",
  "Zichligi 1,1 g/mL bo'lgan 20 % li eritmaning 200 mL hajmida necha gramm tuz bor?",
  "44 g", [("40 g", "avval massa: 200·1,1 = 220 g"), ("22 g", "hisob xato"), ("220 g", "bu eritma massasi")],
  "m(eritma) = 220 g → m(tuz) = 220·0,2 = 44 g.",
  dict(arch="zichlik_foiz_hisob"))

# 18 (2)
q(2, "yuqori",
  "Nima uchun qizdirilayotgan probirka OLDIN butunlay, keyin bir joyda qizdiriladi?",
  "notekis qizishda shisha yorilib ketishi mumkin",
  [("tezroq qaynashi uchun", "gap tezlikda emas, xavfsizlikda"),
   ("rang chiroyli chiqishi uchun", "estetikaga aloqasi yo'q"),
   ("shart emas", "sovuq shishaga to'satdan olov — yorilish")],
  "Bir tekis dastlabki qizdirish termik zarbani oldini oladi.",
  dict(arch="tekis_qizdirish"))

# 19 (3) — RASMLI: ajratuvchi voronka
q(3, "yuqori",
  "Rasmdagi ajratuvchi voronkada benzin-suv aralashmasi turibdi. Suvni ajratib olish uchun nima "
  "qilinadi?",
  "jo'mrak ochilib, PASTKI (suv) qatlam alohida idishga chiqariladi",
  [("ustki qatlam avval quyib olinadi", "ustidan quyishda aralashib ketadi"),
   ("voronka chayqatiladi va birga quyiladi", "qatlamlar yana aralashadi"),
   ("suv bug'latiladi", "voronkaning vazifasi — jo'mrakli ajratish")],
  "Zichligi katta suv pastda: jo'mrakdan chegaragacha oqiziladi, benzin voronkada qoladi.",
  dict(arch="voronka_oqish"), fig="separator")

# 20 (2)
q(2, "yuqori",
  "Kimyoviy idishlarni yuvishda ular TOZA deb qachon hisoblanadi?",
  "suv devorlardan tomchilanmasdan, tekis parda bo'lib oqsa",
  [("ko'zga toza ko'rinsa", "yog' pardasi ko'rinmasligi mumkin"),
   ("bir marta chayilsa", "qoldiq reaktiv qolishi mumkin"),
   ("quruq artilsa", "latta tola qoldiradi")],
  "Tomchilar qolsa — yuzada yog'li ifloslik bor: yana yuviladi.",
  dict(arch="idish_yuvish"))

# 21 (3) — ikki eritma
check("q21", 150*0.05+150*0.25, 45); check("q21b", 45/300*100, 15)
q(3, "yuqori",
  "5 % li va 25 % li eritmalardan qanday massalarda olib aralashtirilsa, 300 g 15 % li eritma "
  "hosil bo'ladi?",
  "150 g dan har biridan",
  [("100 g va 200 g", "u holda ω = 18,3 % bo'lardi"),
   ("200 g va 100 g", "u holda ω = 11,7 % bo'lardi"),
   ("250 g va 50 g", "ω ≈ 8,3 % bo'lardi")],
  "15 % — o'rtada (5 va 25 ning o'rtachasi) → teng massalar: 150 va 150 g.",
  dict(arch="ikki_eritma_hisob"))

# 22 (2)
q(2, "yuqori",
  "Nima uchun konsentrlangan kislotalar shkafda PASTKI tokchada saqlanadi?",
  "yiqilib sinsa, yuqoridan boshqa moddalar ustiga to'kilmasligi uchun",
  [("og'ir bo'lgani uchun ko'tarish qiyin", "asosiy sabab — xavfsizlik"),
   ("pastda sovuqroq", "harorat hal qiluvchi emas"),
   ("tasodifiy tartib", "saqlash qoidalari qat'iy")],
  "Xavfli suyuqliklar past va barqaror joyda — «yiqilish balandligi» minimal.",
  dict(arch="kislota_saqlash_qoida"))

# 23 (3) — uch komponentli
check("q23", 20-5-8, 7)
q(3, "yuqori",
  "Temir qirindilari, qum va osh tuzidan iborat 20 g aralashmadan magnit bilan 5 g temir ajratildi; "
  "qolgani suvda eritilib filtrlanganda eritmadan 8 g tuz olindi. Qum massasini toping.",
  "7 g", [("12 g", "temir ham ayiriladi"), ("15 g", "tuz ham ayiriladi"), ("13 g", "hisob xato")],
  "m(qum) = 20 − 5 − 8 = 7 g.",
  dict(arch="uch_komponent_hisob"))

# 24 (2)
q(2, "yuqori",
  "XROMATOGRAFIYA usuli nimaga asoslangan?",
  "moddalarning shimuvchi yuza bo'ylab har xil tezlikda harakatlanishiga",
  [("qaynash haroratlari farqiga", "bu haydash"), ("zichlik farqiga", "bu voronka/tindirish"),
   ("magnit xossalarga", "bu magnitli ajratish")],
  "Siyoh dog'i filtr qog'ozda ranglarga «tarqaladi» — flomaster tajribasi.",
  dict(arch="xromatografiya"))

# 25 (3)
q(3, "yuqori",
  "Eritmani filtrlashda suyuqlik sathi filtr qog'oz chetidan QUYI bo'lishi shart. Aks holda nima "
  "bo'ladi?",
  "aralashma qog'oz chetidan filtrlanmasdan oqib o'tadi",
  [("filtr tezroq ishlaydi", "aksincha — ajratish buziladi"),
   ("hech nima o'zgarmaydi", "cho'kma filtratga o'tib ketadi"),
   ("qog'oz mustahkamlanadi", "qog'oz namlanib yirtilishi ham mumkin")],
  "Suyuqlik faqat qog'oz ORQALI o'tishi kerak — chetlab o'tsa filtrat loyqa chiqadi.",
  dict(arch="filtr_qoida"))

# 26 (3) — RASMLI: heat curve hisob
q(3, "yuqori",
  "5-savol grafigidagi toza suyuqlikning qaynash platosi 78 °C da joylashgan. Bu qaysi modda "
  "bo'lishi mumkin?",
  "etil spirti", [("suv", "suv 100 °C da qaynaydi"), ("simob", "357 °C"),
                   ("kislota eritmasi", "eritma «suzuvchi» oraliqda qaynaydi")],
  "78 °C — etanolning qaynash harorati; plato aynan shu sathda.",
  dict(arch="heat_curve_hisob"), fig="heat_curve")

# 27 (3) — suyultirish teskari
check("q27", 100*0.2/0.04-100, 400)
q(3, "yuqori",
  "100 g 20 % li eritmani 4 % li qilish uchun necha gramm suv qo'shish kerak?",
  "400 g", [("100 g", "20/(100+x) = 0,04 → x = 400"), ("500 g", "bu yakuniy eritma massasi"),
             ("80 g", "hisob xato")],
  "20 = 0,04(100+x) → 100+x = 500 → x = 400 g.",
  dict(arch="suyultirish_teskari"))

# 28 (2) — RASMLI: voronka reuse
q(2, "yuqori",
  "19-savol rasmidagi voronkada qaysi qatlam USTIDA joylashgan?",
  "benzin — zichligi suvdan kichik",
  [("suv", "suv og'irroq — pastda"), ("qatlamlar bo'lmaydi", "aralashmaydigan suyuqliklar qatlamlanadi"),
   ("aralash qatlam", "chegara aniq ko'rinadi")],
  "ρ(benzin) ≈ 0,7 g/mL < 1 → ustki qatlam.",
  dict(arch="voronka_qatlam"), fig="separator")

# 29 (3)
check("q29", 500*0.04/200*100, 10)
q(3, "yuqori",
  "500 g 4 % li eritmadan 300 g suv bug'latildi. Yangi konsentratsiyani toping.",
  "10 %", [("4 %", "eritma massasi kamaydi"), ("6,7 %", "hisob xato"), ("20 %", "ikki baravar ortiq")],
  "Tuz 20 g; eritma 200 g → ω = 10 %.",
  dict(arch="buglatish_katta_hisob"))

# 30 (2)
q(2, "yuqori",
  "Termometrni haydash kolbasiga o'rnatishda uning rezervuari qayerda bo'lishi kerak?",
  "bug' chiqish nayi ro'parasida (suyuqlik ichida emas)",
  [("suyuqlik tubida", "suyuqlik harorati emas, BUG' harorati o'lchanadi"),
   ("kolba og'zida ochiq havoda", "bug'dan tashqarida noto'g'ri ko'rsatadi"),
   ("sovutgich ichida", "u yerda bug' allaqachon soviydi")],
  "Haydashda aynan bug'ning harorati fraksiya tozaligini ko'rsatadi.",
  dict(arch="termometr_orni"))

# 31 (3)
check("q31", (100*0.3+200*0.06)/300*100, 14)
q(3, "yuqori",
  "100 g 30 % li eritma 200 g 6 % li eritma bilan aralashtirildi. Yakuniy konsentratsiyani toping.",
  "14 %", [("18 %", "(30+12)/300 = 14 %"), ("36 %", "foizlar qo'shilmaydi"), ("12 %", "hisob xato")],
  "m(tuz) = 30 + 12 = 42 g; m = 300 g → ω = 14 %.",
  dict(arch="aralashtirish_hisob2"))

# 32 (3) — RASMLI: heat curve aralashma
q(3, "yuqori",
  "5-savol grafigidan: aralashma egri chizig'i uchun qaysi xulosa TO'G'RI?",
  "qaynash bir haroratda emas, harorat oralig'ida boradi",
  [("aralashma umuman qaynamaydi", "qaynaydi, lekin «suzuvchi» haroratda"),
   ("aralashma pastroq haroratda muzlaydi", "grafik qizdirish haqida"),
   ("aralashma toza moddadan tez qaynaydi", "tezlik emas, plato yo'qligi muhim")],
  "Tarkib o'zgargani sari qaynash harorati ham o'zgaradi — plato hosil bo'lmaydi.",
  dict(arch="heat_curve_xulosa"), fig="heat_curve")

# ---------- Y2: uch texnika ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="IV.1",
  ichki_pasport=[dict(n=33, element="IV.1", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="IV.1", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="IV.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uchta ajratish vazifasi berilgan: X — yod va osh tuzi aralashmasi; Y — spirt va suv "
               "aralashmasi; Z — o'simlik yog'i va suv aralashmasi. 33–35-savollarga A–F ro'yxatidan "
               "javob tanlang."),
  savollar_ichki=[
    "33. X uchun eng mos usul qaysi?",
    "34. Y uchun qaysi usul va nima sababdan?",
    "35. Z da suv qatlami voronkaning qayeridan olinadi?"],
  javoblar_royxati=["A) sublimatlash", "B) haydash — t(qayn.) farqi", "C) pastdan (jo'mrakdan)",
                    "D) filtrlash", "E) bug'latish — eruvchanlik farqi", "F) ustidan quyib"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="ikkala qattiq modda filtrda birga qoladi"),
                   dict(variant="E", xato="spirt ham suv bilan birga bug'lanadi — haydash kerak"),
                   dict(variant="F", xato="ustidan quyishda qatlamlar aralashadi")],
  yechim=("X: yod sublimatlanadi (A). Y: aralashuvchi suyuqliklar — haydash (B). "
          "Z: og'ir suv pastda — jo'mrakdan (C)."),
  parametrlar=dict(arch="texnika_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36", 15/30*100, 50)
check("o37", 12.8/0.32, 40)
check("o38", 30-6-9, 15)
check("o39", 50/250*160/320*100, 10)
check("o40", 500*0.04/200*100, 10)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Temir, qum va tuzdan iborat 30 g aralashmadan magnit bilan 6 g temir ajratildi; suvda "
            "eritib filtrlangach, 9 g quruq qum qoldi. Aralashmadagi tuzning massa ulushini (%) toping.",
      javob="50", yechim="m(tuz) = 30 − 6 − 9 = 15 g → ω = 15/30 = 50 %.",
      parametrlar=dict(arch="uch_komponent_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="Necha gramm 40 % li eritma 160 g suvga qo'shilsa, 8 % li eritma hosil bo'ladi?",
      javob="40", yechim="0,4x = 0,08(x + 160) → 0,32x = 12,8 → x = 40 g.",
      parametrlar=dict(arch="aralashtirish_teskari_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi ketma-ketlik bo'yicha 30 g aralashma (temir + qum + tuz) ajratildi: magnit "
            "6 g temirni oldi, filtrda 9 g qum qoldi. Bug'latishdan olinadigan tuz massasini (g) toping.",
      javob="15", yechim="m(tuz) = 30 − 6 − 9 = 15 g.",
      parametrlar=dict(arch="sxema_ajratish_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="50 g mis kuporosi (CuSO₄·5H₂O) 270 g suvda eritildi. Eritmadagi suvsiz tuzning massa "
            "ulushini (%) toping. (M: kuporos=250, CuSO₄=160)",
      javob="10", yechim="m(CuSO₄) = 32 g; m(eritma) = 320 g → ω = 10 %.",
      parametrlar=dict(arch="kuporos_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="500 g 4 % li eritmadan 300 g suv bug'latildi. Yakuniy eritma konsentratsiyasini (%) toping.",
      javob="10", yechim="Tuz 20 g; eritma 200 g → 10 %.",
      parametrlar=dict(arch="buglatish_zanjir")),
]

# ---------- O2 ----------
check("o41a", 250*0.1, 25)
check("o41c", 25/0.2, 125); check("o41d", 250-125, 125)
check("o43b", 60/300*100, 20)
O2 = [
 dict(n=41, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Laborantga 250 g 10 % li eritmadan 20 % li eritma tayyorlash topshirildi (suvni bug'latish "
            "orqali). Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Boshlang'ich eritmadagi tuz massasini toping.",
             yechim=["m(tuz) = 250·0,1 = 25 g."], M=4, A=2),
        dict(savol="b) Bug'latishda tuz massasi o'zgaradimi? Asoslang.",
             yechim=["Yo'q — faqat suv uchadi, tuz eritmada qoladi."], M=3, A=2),
        dict(savol="c) 20 % li bo'lishi uchun yakuniy eritma massasi qancha bo'lishi kerak?",
             yechim=["m = 25/0,2 = 125 g."], M=4, A=3),
        dict(savol="d) Necha gramm suv bug'latish kerakligini toping.",
             yechim=["Δm = 250 − 125 = 125 g."], M=4, A=3),
      ],
      rasmiylashtirish="Konsentrlash-zanjir: tuz → tamoyil → yakuniy massa → suv; M15+A10.",
      parametrlar=dict(arch="konsentrlash_zanjir")),
 dict(n=42, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Ajratish usullarining chegaralari tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega tuz eritmasini filtrlash bilan ajratib bo'lmaydi, lekin bo'r-suv "
                   "aralashmasini bo'ladi? Zarrachalar darajasida tushuntiring.",
             yechim=["Erigan tuz ion/molekulalargacha maydalangan — ular filtr g'ovaklaridan bemalol o'tadi.",
                     "Bo'r zarrachalari millionlab marta yirik — qog'oz ularni ushlab qoladi."], M=13, A=0),
        dict(savol="b) Nega haydash «eng universal» tozalash usullaridan hisoblanadi?",
             yechim=["Har bir moddaning o'z qaynash harorati bor — deyarli istalgan suyuq aralashmani "
                     "fraksiyalarga bo'lish mumkin."], M=9, A=0),
        dict(savol="c) Sublimatlanadigan bitta moddaga misol yozing.",
             yechim=["Yod (yoki naftalin, «quruq muz» — CO₂)."], M=3, A=0),
      ],
      rasmiylashtirish="Usul-chegaralari (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="usul_chegara_mulohaza")),
 dict(n=43, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Ikki eritma jadvalda berilgan:\n"
            "[JADVAL] Eritma | Massa, g | ω, % ;; 1-eritma | 100 | 30 ;; 2-eritma | 200 | 15\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir eritmadagi tuz massasini toping.",
             yechim=["1-eritma: 30 g; 2-eritma: 30 g."], M=4, A=2),
        dict(savol="b) Ikkala eritma aralashtirilsa, yangi konsentratsiya qancha bo'ladi?",
             yechim=["m(tuz) = 60 g; m = 300 g → ω = 20 %."], M=4, A=3),
        dict(savol="c) Bu eritmadan 5 % li eritma olish uchun unga necha gramm suv qo'shish kerak?",
             yechim=["60 = 0,05(300 + x) → x = 900 g."], M=4, A=3),
        dict(savol="d) Aralashtirish va suyultirishda qaysi kattalik O'ZGARMAY qoladi?",
             yechim=["Erigan tuzning umumiy massasi."], M=3, A=2),
      ],
      rasmiylashtirish="Eritmalar-jadvali: tuzlar → aralashtirish → suyultirish → tamoyil; M15+A10.",
      parametrlar=dict(arch="eritmalar_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261605)
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
    d = dict(n=n, tur="Y1", element="IV.1", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-IV1-B", daraja="B", bob=16, bob_nomi="Laboratoriya amaliyoti",
    manba=("Laboratoriya banki arxetiplari (usul tanlash tuzoqlari, ko'p bosqichli ajratish, gaz "
           "yig'ish) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS "
           "spetsifikatsiyasi IV.1"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: aralashtirish/suyultirish hisoblari, qizdirish "
          "egri chiziqlari, uch komponentli ajratish."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="IV.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
