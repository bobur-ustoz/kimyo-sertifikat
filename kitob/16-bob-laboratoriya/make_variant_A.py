# -*- coding: utf-8 -*-
"""16-bob A-varianti: Laboratoriya amaliyoti (IV.1) — O'RGATUVCHI ★★.
Hayotiy sahnalar: choy xaltasi (filtrlash), himoya ko'zoynagi, magnit bilan ajratish, tuz bug'latish."""
import json, random

OUT = "mavzu_IV1A.json"
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

# 1 (2) — RASMLI: jihozlar
q(2, "quyi",
  "Rasmdagi (b) belgili jihozning nomi va vazifasi qanday?",
  "menzurka — suyuqlik hajmini o'lchash",
  [("kolba — moddalarni saqlash", "kolba (a) belgida"),
   ("probirka — kichik tajribalar", "probirka (c) belgida"),
   ("quyg'ich — suyuqlik quyish", "quyg'ich (d) belgida")],
  "Menzurka darajalangan idish: hajm aynan chizig'i bo'yicha o'qiladi.",
  dict(arch="jihoz_menzurka"), fig="equip")

# 2 (2)
q(2, "quyi",
  "Spirt lampani qanday O'CHIRISH kerak?",
  "qopqoqcha bilan yopib",
  [("puflab", "uchqun sachrashi va alanga tarqalishi mumkin"),
   ("suv sepib", "spirt suv yuzasida yonishda davom etishi mumkin"),
   ("qo'l bilan yopib", "kuyish xavfi!")],
  "Qopqoq kislorodni to'sadi — alanga xavfsiz o'chadi.",
  dict(arch="spirtlampa"))

# 3 (2)
q(2, "o'rta",
  "FILTRLASH usuli bilan qanday aralashmani ajratish mumkin?",
  "suyuqlik va unda ERIMAYDIGAN qattiq moddani",
  [("ikki erigan tuzni", "eritma filtrdan to'liq o'tadi"),
   ("ikki gazni", "gazlar filtr qog'ozdan o'tib ketadi"),
   ("suv va spirtni", "aralashuvchi suyuqliklar filtrda ajralmaydi")],
  "Filtr qog'oz zarrachalarni ushlab, eritmani o'tkazadi: qum + suv — klassik misol.",
  dict(arch="filtrlash_tarif"))

# 4 (2) — SAHNA: choy xaltasi
q(2, "o'rta",
  "Rasmda damlanayotgan choy xaltasi. Bu jarayon laboratoriyadagi qaysi usullarga o'xshaydi?",
  "eritish (ekstraktsiya) va filtrlash",
  [("haydash va quritish", "hech narsa bug'latilmayapti"),
   ("elektroliz", "tok yo'q-ku"),
   ("sublimatlanish", "qattiq → gaz o'tishi yo'q")],
  "Suv choy moddalarini eritib oladi; xaltacha (filtr) barglarni o'tkazmaydi.",
  dict(arch="choy_sahna"), fig="teabag")

# 5 (2)
q(2, "o'rta",
  "Erigan tuzni eritmadan qanday ajratib olinadi?",
  "bug'latish (suvni uchirish) orqali",
  [("filtrlash orqali", "erigan modda filtrdan o'tib ketadi"),
   ("tindirish orqali", "eritma tinib ajralmaydi"),
   ("magnit bilan", "tuz magnitlanmaydi")],
  "Suv bug'lanadi — idish tubida tuz kristallari qoladi.",
  dict(arch="buglatish_tarif"))

# 6 (2)
q(2, "quyi",
  "Laboratoriyada moddalarni TATIB KO'RISH mumkinmi?",
  "qat'iyan mumkin emas — zaharlanish xavfi",
  [("faqat oz-ozdan mumkin", "oz miqdor ham zaharli bo'lishi mumkin"),
   ("shirin moddalarni mumkin", "ko'rinishdan bilib bo'lmaydi"),
   ("o'qituvchi ruxsati bilan mumkin", "hech qanday holatda tatib ko'rilmaydi")],
  "Lab qoidasi: hidlash ham faqat «qo'l silkitib», tatish — hech qachon.",
  dict(arch="tatib_korish"))

# 7 (2)
q(2, "o'rta",
  "Distillangan suv oddiy suvdan nimasi bilan farq qiladi?",
  "erigan tuzlar deyarli yo'q — bug'latib kondensatlangan",
  [("tarkibida ko'proq mineral bor", "aksincha — minerallar yo'q"),
   ("rangi bilan", "ikkalasi ham rangsiz"),
   ("faqat harorati bilan", "gap tozalikda")],
  "Distillash: suv bug'ga aylanib, tuzlar qolib ketadi — «kimyoviy toza» suv.",
  dict(arch="distillangan_suv"))

# 8 (2) — SAHNA: himoya ko'zoynagi
q(2, "o'rta",
  "Rasmda himoya ko'zoynagi. Qaysi ishlarda uni taqish SHART?",
  "kislota-ishqorlar bilan ishlaganda va qizdirish tajribalarida",
  [("faqat o'qituvchi kelganda", "xavf doim mavjud"),
   ("faqat portlash tajribalarida", "sachrash har qanday tajribada bo'lishi mumkin"),
   ("umuman shart emas", "ko'z — eng himoyasiz a'zo")],
  "Sachragan bir tomchi ishqor ko'rishdan ayirishi mumkin — ko'zoynak doimo taqiladi.",
  dict(arch="kozoynak_sahna"), fig="safety")

# 9 (2)
q(2, "o'rta",
  "Probirkada suyuqlik qizdirilayotganda uning og'zi qayoqqa qaratiladi?",
  "odamlardan chetga (devor tomonga)",
  [("o'ziga", "otilib chiqsa kuydiradi"), ("qo'shniga", "xavfli!"),
   ("yuqoriga tik", "otilish baribir xavfli")],
  "Qizigan suyuqlik «otilib» chiqishi mumkin — og'iz doim xavfsiz tomonga.",
  dict(arch="probirka_ogzi"))

# 10 (3)
check("q10", 200*0.1, 20)
q(3, "o'rta",
  "10 % li 200 g eritma tayyorlash uchun necha gramm tuz kerak?",
  "20 g", [("10 g", "200 ning 10 %i — 20"), ("180 g", "bu suv massasi"), ("40 g", "ikki baravar")],
  "m(tuz) = 200 · 0,1 = 20 g (va 180 g suv).",
  dict(arch="eritma_hisob_oddiy"))

# 11 (2)
q(2, "o'rta",
  "TINDIRISH usuli qanday aralashma uchun qo'llanadi?",
  "og'ir cho'kuvchi zarrachali suyuqlik uchun (loyqa suv)",
  [("erigan tuz eritmasi uchun", "erigan modda cho'kmaydi"),
   ("ikki gaz uchun", "gazlar «cho'kmaydi»"),
   ("spirt-suv uchun", "aralashuvchi suyuqliklar tinmaydi")],
  "Og'ir zarrachalar asta cho'kadi — tiniq qism ustidan quyib olinadi (dekantatsiya).",
  dict(arch="tindirish"))

# 12 (3)
check("q12", 20/0.05, 400)
q(3, "o'rta",
  "Tarkibida 20 g tuz bo'lgan 5 % li eritmaning umumiy massasi qancha?",
  "400 g", [("100 g", "20/0,05 = 400"), ("200 g", "10 % uchun to'g'ri bo'lardi"), ("500 g", "hisob xato")],
  "m(eritma) = 20/0,05 = 400 g.",
  dict(arch="eritma_teskari_oddiy"))

# 13 (2) — SAHNA: magnit
q(2, "o'rta",
  "Rasmda temir qirindilari va oltingugurt kukuni aralashmasiga magnit yaqinlashtirilgan. "
  "Nima kuzatiladi?",
  "temir magnitga yopishadi, oltingugurt qoladi",
  [("ikkalasi ham yopishadi", "S magnitlanmaydi"),
   ("hech biri yopishmaydi", "temir ferromagnit-ku"),
   ("oltingugurt yopishadi", "aksincha")],
  "Magnit — temirli aralashmalarni ajratishning eng tez usuli.",
  dict(arch="magnit_sahna"), fig="magnet")

# 14 (2)
q(2, "o'rta",
  "HAYDASH (distillash) usuli qaysi aralashmani ajratadi?",
  "qaynash haroratlari farq qiladigan aralashuvchi suyuqliklarni",
  [("qattiq moddalar aralashmasini", "ular haydalmaydi"),
   ("erimaydigan qattiq va suyuqlikni", "buning uchun filtrlash yetarli"),
   ("ikkita gazni oddiy sharoitda", "gazlar boshqa usulda ajratiladi")],
  "Avval past haroratda qaynaydigani bug'lanib, sovutgichda yig'iladi.",
  dict(arch="haydash_tarif"))

# 15 (2) — RASMLI: filtrlash apparati
q(2, "o'rta",
  "Rasmdagi filtrlash qurilmasida filtr qog'ozda nima qoladi va kolbaga nima o'tadi?",
  "qog'ozda — erimaydigan zarrachalar; kolbada — tiniq eritma (filtrat)",
  [("qog'ozda — eritma; kolbada — cho'kma", "teskari"),
   ("ikkalasi ham o'tadi", "unda ajratishning ma'nosi yo'q"),
   ("hech narsa o'tmaydi", "suyuqlik o'tadi")],
  "Kolbadagi tiniq suyuqlik — filtrat deb ataladi.",
  dict(arch="filtr_apparat"), fig="filter")

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi aralashmalarga mos ajratish usullarini to'ldiring:\n"
  "[JADVAL] Aralashma | Usul ;; qum + suv | ? ;; tuz + suv | ?",
  "filtrlash; bug'latish",
  [("bug'latish; filtrlash", "teskari"), ("magnit; filtrlash", "qum magnitlanmaydi"),
   ("tindirish; tindirish", "erigan tuz tinmaydi")],
  "Erimaydigan — filtr; erigan — bug'latish.",
  dict(arch="usul_jadval"))

# 17 (2)
q(2, "o'rta",
  "Suyuqlik hajmini menzurkada o'lchashda ko'z qayerda bo'lishi kerak?",
  "suyuqlik sathi (menisk) bilan bir tekislikda",
  [("yuqoridan qarash kerak", "sath noto'g'ri o'qiladi"),
   ("pastdan qarash kerak", "xuddi shunday xato"),
   ("farqi yo'q", "parallaks xatosi paydo bo'ladi")],
  "Menisk pastki chizig'i ko'z bilan bir sathda o'qiladi.",
  dict(arch="menisk"))

# 18 (2) — SAHNA: tuz bug'latish
q(2, "o'rta",
  "Rasmda chinni kosachada tuzli eritma qizdirilmoqda: suv kamayib, devorlarida oq qatlam paydo "
  "bo'lyapti. Bu qaysi usul?",
  "bug'latish — erigan tuzni ajratib olish",
  [("filtrlash", "filtr ishlatilmayapti"), ("haydash", "bug' yig'ilmayapti"),
   ("tindirish", "cho'kma emas, erigan tuz")],
  "Suv uchadi, tuz kristallanadi — sho'r ko'llarda tuz shu tarzda olinadi.",
  dict(arch="evap_sahna"), fig="evap")

# 19 (3)
check("q19", 30/150*100, 20)
q(3, "o'rta",
  "30 g tuz 120 g suvda eritildi. Eritmaning foiz konsentratsiyasini toping.",
  "20 %", [("25 %", "eritma massasi 150 g (tuz ham qo'shiladi)"), ("30 %", "120 emas, 150 ga bo'linadi"),
            ("15 %", "hisob xato")],
  "ω = 30/(30+120) · 100 = 20 %.",
  dict(arch="foiz_hisob_oddiy"))

# 20 (2)
q(2, "o'rta",
  "Idishdagi reaktivni olishda qaysi qoida TO'G'RI?",
  "quruq moddani maxsus qoshiqcha (shpatel) bilan olish",
  [("qo'l bilan olish", "teri zararlanadi, reaktiv ifloslanadi"),
   ("idishni to'g'ridan-to'g'ri og'dirish", "to'kilish xavfi"),
   ("ortiqchasini idishga qaytarib solish", "butun idish ifloslanadi!")],
  "Shpatel — toza va xavfsiz; olingan ortiqcha reaktiv qaytarilmaydi.",
  dict(arch="reaktiv_olish"))

# 21 (2) — RASMLI: haydash apparati
q(2, "o'rta",
  "Rasmdagi haydash qurilmasida sovutgichning (xolodilnikning) vazifasi nima?",
  "bug'ni sovutib, yana suyuqlikka aylantirish",
  [("suyuqlikni qizdirish", "qizdirgich alohida"), ("bug'ni ushlab qolish", "u kondensatlaydi"),
   ("gazni tozalash", "tozalash emas — kondensatsiya")],
  "Suv «ko'ylagi»dagi sovutgichda bug' kondensatlanib, qabul kolbasiga tomadi.",
  dict(arch="haydash_apparat"), fig="distill")

# 22 (2)
q(2, "o'rta",
  "Qaysi hodisa SUBLIMATLANISH (qattiqdan to'g'ri gazga o'tish)ga misol?",
  "yodning qizdirilganda binafsha bug'ga aylanishi",
  [("suvning qaynashi", "suyuq → gaz"), ("muzning erishi", "qattiq → suyuq"),
   ("tuzning erishi", "eritmaga o'tish")],
  "I₂ suyuqlanmasdan bug'lanadi — yod shu usulda tozalanadi.",
  dict(arch="sublimatlanish"))

# 23 (3)
check("q23", 100*0.2/200*100, 10)
q(3, "o'rta",
  "100 g 20 % li eritmaga 100 g suv qo'shildi. Yangi eritmaning konsentratsiyasini toping.",
  "10 %", [("20 %", "suyultirishda kamayadi"), ("5 %", "ikki emas, to'rt barobar emas"),
            ("40 %", "aksincha kamayadi")],
  "Tuz 20 g o'zgarmaydi; eritma 200 g → ω = 10 %.",
  dict(arch="suyultirish_oddiy"))

# 24 (2)
q(2, "o'rta",
  "Laboratoriyada shisha idish singanda nima qilinadi?",
  "o'qituvchiga aytiladi; siniqlar maxsus cho'tka bilan yig'iladi",
  [("qo'l bilan tez terib olinadi", "kesilish xavfi"),
   ("hech narsa qilinmaydi", "boshqalar jarohatlanishi mumkin"),
   ("oyoq bilan chetga suriladi", "xavf saqlanadi")],
  "Shisha siniqlari — jarohat manbai: faqat asbob bilan, alohida qutiga.",
  dict(arch="shisha_sinig"))

# 25 (2)
q(2, "o'rta",
  "AJRATUVCHI VORONKA qanday aralashma uchun ishlatiladi?",
  "aralashmaydigan ikki suyuqlik uchun (yog' + suv)",
  [("qattiq + suyuq uchun", "u filtrlash bilan ajratiladi"),
   ("erigan tuz uchun", "eritma qatlamlanmaydi"),
   ("gazlar uchun", "voronkada gaz ushlanmaydi")],
  "Og'ir qatlam pastdan jo'mrak orqali chiqariladi — qatlamlar alohida yig'iladi.",
  dict(arch="voronka_tarif"))

# 26 (3) — RASMLI: qizdirish egri
q(3, "o'rta",
  "Grafikda toza suvni qizdirish egri chizig'i berilgan. Gorizontal qism (plato) nimani bildiradi?",
  "qaynash — berilgan issiqlik bug'lanishga sarflanadi",
  [("isitish to'xtatilgan", "olov o'chirilmagan — harorat baribir turibdi"),
   ("suv muzlayapti", "100 °C da muzlamaydi"),
   ("termometr buzilgan", "bu qonuniy hodisa")],
  "Qaynash davomida harorat o'zgarmaydi: energiya fazaviy o'tishga ketadi.",
  dict(arch="heat_curve_oqish"), fig="heat_curve")

# 27 (3)
check("q27", 50*1.2, 60)
q(3, "o'rta",
  "Menzurkada 50 mL suyuqlik bor; uning zichligi 1,2 g/mL. Suyuqlik massasini toping.",
  "60 g", [("50 g", "zichlik hisobga olinmagan"), ("41,7 g", "bo'lish emas, ko'paytirish"),
            ("120 g", "ikki baravar")],
  "m = V·ρ = 50 · 1,2 = 60 g.",
  dict(arch="zichlik_hisob"))

# 28 (2) — RASMLI: zichlik ustunlari
q(2, "o'rta",
  "Diagrammada uch suyuqlikning zichligi berilgan. Suvga aralashmaydigan o'simlik yog'i quyilsa, "
  "u qayerda joylashadi?",
  "suv USTIDA — zichligi kichik",
  [("idish tubida", "0,9 < 1,0 — suzib chiqadi"),
   ("suv bilan aralashib ketadi", "yog' suvda erimaydi"),
   ("bug'lanib ketadi", "xona haroratida uchmaydi")],
  "Zichligi kichik suyuqlik yengil — ustki qatlam bo'ladi.",
  dict(arch="bar_zichlik_oqish"), fig="bar_zichlik")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Eritma ustiga asta-sekin suv qo'shilmoqda. Eritma KONSENTRATSIYASI qanday o'zgaradi? Grafikni "
  "tanlang.",
  "kamayib boradi",
  [("ortadi", "tuz miqdori o'zgarmay, massa ortadi"),
   ("o'zgarmaydi", "suyultirish aynan kamaytiradi"),
   ("avval ortib keyin kamayadi", "boshidanoq kamayadi")],
  "ω = m(tuz)/m(eritma): maxraj o'sadi → ulush kamayadi.",
  svg=dict(correct="fall", d1="rise", d2="flat", d3="u", xlab="qo'shilgan suv", ylab="ω"),
  params=dict(arch="suyultirish_grafik"))

# 30 (2)
q(2, "o'rta",
  "Quyidagi belgi (alanga tasviri) tushirilgan reaktiv idishi nimadan ogohlantiradi?",
  "modda yonuvchan — olovdan uzoq tutish kerak",
  [("modda sovuq saqlanishi kerak", "belgi harorat emas, yong'in haqida"),
   ("modda qimmatbaho", "belgilar xavf uchun"),
   ("ichish mumkin emas, xolos", "yonuvchanlik alohida belgi")],
  "Xavf belgilari: alanga — yonuvchan, bosh chanog'i — zaharli, tomchi-qo'l — yemiruvchi.",
  dict(arch="xavf_belgi"))

# 31 (3)
check("q31", 45/250*100, 18)
q(3, "o'rta",
  "250 g eritma bug'latilganda 45 g quruq tuz qoldi. Dastlabki eritma konsentratsiyasini toping.",
  "18 %", [("45 %", "eritma 250 g edi"), ("22,5 %", "hisob xato"), ("4,5 %", "nol adashgan")],
  "ω = 45/250 · 100 = 18 %.",
  dict(arch="qoldiq_foiz"))

# 32 (3) — RASMLI: zichlik hisob
check("q32", 13.6/0.9, 15.1, tol=0.1)
q(3, "o'rta",
  "28-savol diagrammasidan: simob zichligi yog'nikidan taxminan necha marta katta?",
  "≈ 15 marta", [("≈ 5 marta", "13,6/0,9 ≈ 15"), ("≈ 2 marta", "farq juda katta"),
                  ("teng", "ustunlar keskin farqli")],
  "13,6 : 0,9 ≈ 15.",
  dict(arch="bar_zichlik_hisob"), fig="bar_zichlik")

# ---------- Y2: uch aralashma ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="IV.1",
  ichki_pasport=[dict(n=33, element="IV.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="IV.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="IV.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch aralashma berilgan: X — qum va suv; Y — osh tuzi va suv; Z — temir qirindilari "
               "va oltingugurt kukuni. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X aralashmani ajratishning eng qulay usuli qaysi?",
    "34. Y aralashmadan tuzni qanday ajratib olinadi?",
    "35. Z aralashma uchun eng tez usul qaysi?"],
  javoblar_royxati=["A) filtrlash", "B) bug'latish", "C) magnit bilan", "D) haydash",
                    "E) tindirish yetarli", "F) ajratuvchi voronka"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="haydash suyuqliklar uchun — qum uchun ortiqcha"),
                   dict(variant="E", xato="mayda qum to'liq tinmaydi — filtr ishonchli"),
                   dict(variant="F", xato="voronka aralashmaydigan SUYUQLIKLAR uchun")],
  yechim=("X: erimaydigan qum — filtrlash (A). Y: erigan tuz — bug'latish (B). "
          "Z: temir ferromagnit — magnit (C)."),
  parametrlar=dict(arch="aralashma_ssenariy"))

# ---------- O1 ----------
check("o36", 15/150*100, 10)
check("o37", 200*0.05, 10)
check("o38", 60*0.2/100*100, 12)
check("o39", 100*1.84, 184)
check("o40", 250*0.12, 30)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="15 g tuz 135 g suvda eritildi. Eritma konsentratsiyasini (%) toping.",
      javob="10", yechim="ω = 15/150 · 100 = 10 %.",
      parametrlar=dict(arch="foiz_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="200 g 5 % li eritmada necha gramm tuz bor?",
      javob="10", yechim="m = 200·0,05 = 10 g.",
      parametrlar=dict(arch="tuz_massa_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="60 g 20 % li eritmaga 40 g suv qo'shildi. Yangi konsentratsiyani (%) toping.",
      javob="12", yechim="Tuz 12 g; eritma 100 g → 12 %.",
      parametrlar=dict(arch="suyultirish_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Zichligi 1,84 g/mL bo'lgan konsentrlangan kislotaning 100 mL hajmi necha gramm keladi?",
      javob="184", yechim="m = 100·1,84 = 184 g.",
      parametrlar=dict(arch="zichlik_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="250 g 12 % li eritma to'liq bug'latildi. Qolgan quruq tuz massasini (g) toping.",
      javob="30", yechim="m = 250·0,12 = 30 g.",
      parametrlar=dict(arch="buglatish_o1")),
]

# ---------- O2 ----------
check("o41a", 150*0.08, 12)
O2 = [
 dict(n=41, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriq: 8 % li 150 g osh tuzi eritmasini tayyorlash. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Kerakli tuz va suv massalarini hisoblang.",
             yechim=["m(tuz) = 150·0,08 = 12 g; m(suv) = 138 g."], M=5, A=3),
        dict(savol="b) Qaysi jihozlar kerak bo'ladi? Ro'yxat tuzing.",
             yechim=["Tarozi va toshlar, shpatel, menzurka (138 mL suv), stakan, shisha tayoqcha."], M=4, A=2),
        dict(savol="c) Tayyorlash tartibini bosqichma-bosqich yozing.",
             yechim=["Tuzni tortish → suvni o'lchash → stakanda qo'shib, tayoqcha bilan to'liq eritish."], M=3, A=3),
        dict(savol="d) Qanday xatolar konsentratsiyani noto'g'ri qilishi mumkin?",
             yechim=["Noto'g'ri tortish/o'lchash, ho'l idish, tuzning to'liq erimasligi."], M=3, A=2),
      ],
      rasmiylashtirish="Eritma-protokol: hisob → jihoz → tartib → xatolar; M15+A10.",
      parametrlar=dict(arch="eritma_protokol")),
 dict(n=42, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriya xavfsizligi qoidalari tahlil qilinadi. Quyidagilarga MULOHAZA yuritib "
            "javob yozing."),
      bandlar=[
        dict(savol="a) Nega noma'lum moddani hidlashda idishni burunga to'g'ridan-to'g'ri "
                   "yaqinlashtirmasdan, qo'l bilan «yelpib» hidlanadi? Batafsil tushuntiring.",
             yechim=["Konsentrlangan bug' nafas yo'llarini kuydirishi yoki zaharlashi mumkin.",
                     "Yelpishda havo bilan suyulgan oz miqdor keladi — hid bilinadi, zarar yetmaydi."], M=13, A=0),
        dict(savol="b) Nega laboratoriyada ovqatlanish taqiqlanadi?",
             yechim=["Reaktiv zarralari qo'l/stol orqali ovqatga o'tib, organizmga tushishi mumkin."], M=9, A=0),
        dict(savol="c) Kislota teriga tekkanda birinchi yordamni yozing.",
             yechim=["Ko'p oqar suv bilan yuvish, so'ng kuchsiz soda eritmasi."], M=3, A=0),
      ],
      rasmiylashtirish="Xavfsizlik-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="lab_xavfsizlik_mulohaza")),
 dict(n=43, tur="O2", element="IV.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Ajratish usullari jadvalda tekshiriladi:\n"
            "[JADVAL] Aralashma | Usul ;; benzin + suv | ? ;; spirt + suv | ? ;; "
            "bo'r + suv | ? ;; tuz + suv | ?\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir aralashma uchun to'g'ri usulni tanlang.",
             yechim=["Benzin+suv — ajratuvchi voronka; spirt+suv — haydash; bo'r+suv — filtrlash; "
                     "tuz+suv — bug'latish."], M=6, A=3),
        dict(savol="b) Nega spirt-suvni voronkada ajratib bo'lmaydi?",
             yechim=["Ular cheksiz aralashadi — qatlam hosil qilmaydi; faqat t(qayn.) farqi ishlaydi."], M=4, A=3),
        dict(savol="c) Bo'r+suv aralashmasida filtrlashdan keyin bo'rni QURUQ holda olish uchun yana "
                   "qaysi amal kerak?",
             yechim=["Quritish (filtr qog'oz bilan yoki quritish shkafida)."], M=3, A=2),
        dict(savol="d) Barcha usullarning umumiy tamoyilini ayting.",
             yechim=["Komponentlarning FIZIK xossalari (eruvchanlik, t(qayn.), zichlik) farqidan foydalanish."], M=2, A=2),
      ],
      rasmiylashtirish="Usullar-jadvali: tanlash → asoslash → qo'shimcha amal → tamoyil; M15+A10.",
      parametrlar=dict(arch="usullar_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261603)
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
    variant="mavzu-IV1-A", daraja="A", bob=16, bob_nomi="Laboratoriya amaliyoti",
    manba=("MS spetsifikatsiyasi IV.1; laboratoriya banki arxetiplari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (choy xaltasi, ko'zoynak, magnit, tuz bug'latish) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="IV.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
