# -*- coding: utf-8 -*-
"""12-bob A-varianti: Oksidlar, asoslar, kislotalar va tuzlarning xossalari, olinishi (II.2) — O'RGATUVCHI ★★.
Hayotiy sahnalar: o't o'chirgich, tish emali, qoraygan mis idish, tuproqqa ohak solish."""
import json, random

OUT = "mavzu_II2A.json"
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
  "Kislota eritmasiga lakmus tomizilsa, u qanday rangga kiradi?",
  "qizil", [("ko'k", "ko'k — ishqoriy muhitda"), ("sariq", "lakmus sariq bermaydi"),
             ("rangsiz", "fenolftalein kislotada rangsiz")],
  "Lakmus: kislotada qizil, ishqorda ko'k, neytralda binafsha.",
  dict(arch="lakmus_kislota"))

# 2 (2)
q(2, "quyi",
  "Fenolftalein qaysi muhitda PUSHTI rangga kiradi?",
  "ishqoriy muhitda", [("kislotali muhitda", "kislotada rangsiz qoladi"),
                        ("neytral muhitda", "neytralda ham rangsiz"),
                        ("har qanday eritmada", "faqat ishqorda pushti")],
  "Fenolftalein — ishqorlarning «bayroqchasi»: OH⁻ ko'p bo'lsa pushti.",
  dict(arch="fenolftalein"))

# 3 (2)
q(2, "o'rta",
  "Qaysi metall xlorid kislotadan vodorodni siqib chiqaradi?",
  "Zn", [("Cu", "faollik qatorida H dan keyin"), ("Ag", "H dan keyin"), ("Au", "eng passiv metall")],
  "Faollik qatorida H dan OLDINGI metallar kislotadan H₂ ajratadi: Zn + 2HCl → ZnCl₂ + H₂↑.",
  dict(arch="metall_kislota"))

# 4 (2) — SAHNA: o't o'chirgich
q(2, "o'rta",
  "Rasmda ko'pikli o't o'chirgich: ishga tushirilganda ichidagi soda eritmasi kislota bilan "
  "aralashadi. Olovni nima o'chiradi?",
  "ajralgan CO₂ gazi havodagi kislorodni olovdan to'sadi",
  [("soda olovni sovutadi", "asosiy ish — CO₂ pardasida"),
   ("kislota olovga sepiladi", "kislota idish ichida reaksiya uchun"),
   ("ko'pik yonib ketadi", "ko'pik yonmaydi — himoya qatlami")],
  "NaHCO₃ + kislota → tuz + H₂O + CO₂↑: og'ir CO₂ olov ustini «yopadi».",
  dict(arch="otochirgich_sahna"), fig="extinguisher")

# 5 (2)
q(2, "o'rta",
  "Ishqorlar qanday olinadi?",
  "faol metall yoki uning oksidini suv bilan reaksiyaga kiritib",
  [("har qanday metallni suvda eritib", "Cu, Fe suv bilan ishqor bermaydi"),
   ("kislotani qizdirib", "kislotadan ishqor hosil bo'lmaydi"),
   ("tuzni suvda eritib", "erish — fizik jarayon")],
  "2Na + 2H₂O → 2NaOH + H₂; Na₂O + H₂O → 2NaOH.",
  dict(arch="ishqor_olinish"))

# 6 (2)
q(2, "o'rta",
  "Erimaydigan asos (masalan, Cu(OH)₂) qanday olinadi?",
  "tuz eritmasiga ishqor ta'sir ettirib",
  [("metallga suv ta'sir ettirib", "Cu suv bilan reaksiyaga kirishmaydi"),
   ("oksidga suv qo'shib", "CuO suv bilan birikmaydi"),
   ("kislotaga metall solib", "bu tuz va vodorod beradi")],
  "CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄ — ko'k cho'kma.",
  dict(arch="asos_olinish"))

# 7 (2)
q(2, "o'rta",
  "Cu(OH)₂ qizdirilganda qanday o'zgarish kuzatiladi?",
  "ko'k modda qorayadi: CuO va suv hosil bo'ladi",
  [("oq tusga kiradi", "CuO — qora"), ("erib ketadi", "parchalanadi, erimaydi"),
   ("o'zgarish bo'lmaydi", "erimaydigan asoslar qizdirishda parchalanadi")],
  "Cu(OH)₂ → CuO + H₂O: erimaydigan asoslar termik beqaror.",
  dict(arch="cuoh2_parchalanish"))

# 8 (2) — SAHNA: tish emali
q(2, "o'rta",
  "Rasmda tish emali: uning asosi kalsiy fosfat va gidroksiapatit. Shirinliklardan keyin og'izda "
  "hosil bo'ladigan kislotalar tishga qanday ta'sir qiladi?",
  "emal tuzlarini asta-sekin eritib, karies boshlaydi",
  [("emalni mustahkamlaydi", "kislota tuzni yemiradi"),
   ("hech qanday ta'sir qilmaydi", "kislota + tuz reaksiyasi boradi"),
   ("tishni oqartiradi", "yemirilish oqartirish emas")],
  "Kislota kalsiy tuzlarini eriydigan holga o'tkazadi — shu bois ovqatdan keyin og'iz chayiladi.",
  dict(arch="tish_sahna"), fig="tooth")

# 9 (2)
q(2, "o'rta",
  "Qaysi ikki eritma aralashtirilganda OQ cho'kma tushadi?",
  "AgNO₃ va NaCl", [("NaOH va HCl", "mahsulotlar eriydi"), ("KNO₃ va NaCl", "reaksiya bormaydi"),
                     ("CuSO₄ va NaOH", "cho'kma ko'k, oq emas")],
  "Ag⁺ + Cl⁻ → AgCl↓ — xlorid ioniga sifat reaksiyasi.",
  dict(arch="agcl_chokma"))

# 10 (3)
check("q10", 9.8/98*80, 8)
q(3, "o'rta",
  "CuO + H₂SO₄ → CuSO₄ + H₂O. 9,8 g sulfat kislota uchun necha gramm mis(II) oksidi kerak? "
  "(M: H₂SO₄=98, CuO=80)",
  "8 g", [("80 g", "1 mol uchun"), ("9,8 g", "massalar teng bo'lmaydi"), ("4 g", "ikkiga bo'lingan")],
  "n = 0,1 mol → m(CuO) = 0,1·80 = 8 g.",
  dict(arch="cuo_hisob"))

# 11 (2)
q(2, "o'rta",
  "Tuz olishning qaysi usuli TO'G'RI ko'rsatilgan?",
  "kislota + asos → tuz + suv",
  [("kislota + kislota → tuz", "ikki kislota tuz bermaydi"),
   ("metall + asos → tuz", "odatdagi metallar asos bilan kirishmaydi"),
   ("oksid + oksid → suv", "ikki oksiddan tuz hosil bo'ladi, suv emas")],
  "Neytrallanish — tuz olishning asosiy usuli.",
  dict(arch="tuz_olinish_usul"))

# 12 (3)
check("q12", 5.6/56, 0.1)
q(3, "o'rta",
  "Fe + H₂SO₄(suyul.) → FeSO₄ + H₂. 5,6 g temir eriganda necha mol vodorod ajraladi? (M(Fe)=56)",
  "0,1", [("1", "mol bilan gramm adashgan"), ("0,2", "ikki baravar"), ("5,6", "massa qiymati")],
  "n(Fe) = 0,1 mol → n(H₂) = 0,1 mol.",
  dict(arch="fe_h2_hisob"))

# 13 (2) — SAHNA: qoraygan mis idish
q(2, "o'rta",
  "Rasmda qoraygan mis qozoncha: olovda uzoq turgach yuzasi qora qatlam bilan qoplangan. "
  "Bu qatlam nima va uni limon kislota nega tozalaydi?",
  "qatlam — CuO; kislota u bilan reaksiyaga kirishib eriydigan tuz beradi",
  [("qatlam — kuya; kislota uni yuvadi", "kuya emas — kimyoviy oksidlanish mahsuloti"),
   ("qatlam — zang (Fe₂O₃)", "mis idishda temir zangi bo'lmaydi"),
   ("qatlam — tuz; suv eritadi", "suvda erimaydi — kislota kerak")],
  "2Cu + O₂ → 2CuO (qora); CuO + kislota → mis tuzi + suv — yuza yana yaltiraydi.",
  dict(arch="mis_idish_sahna"), fig="copperpan")

# 14 (3)
q(3, "o'rta",
  "Qaysi reaksiya AMALGA OSHMAYDI?",
  "Cu + HCl → ...",
  [("Zn + HCl → ...", "Zn faol — vodorod ajraladi"),
   ("Fe + CuSO₄ → ...", "Fe misdan faol — siqib chiqaradi"),
   ("CuO + HCl → ...", "oksid kislota bilan kirishadi")],
  "Cu faollik qatorida H dan KEYIN — kislotadan vodorod ajrata olmaydi.",
  dict(arch="bormaydigan_reaksiya"))

# 15 (2)
q(2, "o'rta",
  "Kislotali oksidlar qanday olinadi?",
  "metallmaslarni yondirib yoki tuzlarni parchalab",
  [("metallarga suv qo'shib", "bu ishqor beradi"),
   ("faqat tuzlarni eritib", "erish oksid bermaydi"),
   ("ishqorlarni qizdirib", "ishqorlar termik barqaror")],
  "S + O₂ → SO₂; CaCO₃ → CaO + CO₂ (bunda CO₂ — kislotali oksid).",
  dict(arch="oksid_olinish"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi cho'kmalarning ranglarini mos ravishda aniqlang:\n"
  "[JADVAL] Cho'kma | Rang ;; Cu(OH)₂ | ? ;; Fe(OH)₃ | ?",
  "ko'k; qo'ng'ir-qizg'ish",
  [("oq; qora", "ranglar noto'g'ri"), ("ko'k; oq", "Fe(OH)₃ — qo'ng'ir"),
   ("qora; ko'k", "teskari joylashgan")],
  "Cu(OH)₂ — havorang-ko'k; Fe(OH)₃ — zang rangli (qo'ng'ir).",
  dict(arch="chokma_rang_jadval"))

# 17 (2)
q(2, "o'rta",
  "Metall + kislota reaksiyasida qanday mahsulotlar hosil bo'ladi (suyultirilgan HCl, H₂SO₄ uchun)?",
  "tuz va vodorod", [("tuz va suv", "bu asos yoki oksid bilan"), ("faqat tuz", "H₂ ham ajraladi"),
                      ("oksid va vodorod", "metall tuzga o'tadi")],
  "Zn + H₂SO₄ → ZnSO₄ + H₂↑ (faol metallar uchun).",
  dict(arch="metall_kislota_mahsulot"))

# 18 (2) — SAHNA: tuproqqa ohak
q(2, "o'rta",
  "Rasmda dehqon nordon (kislotali) tuproqqa maydalangan ohak (CaCO₃/Ca(OH)₂) sepmoqda. "
  "Buning maqsadi nima?",
  "tuproq kislotaliligini neytrallash",
  [("tuproqni oqartirish", "rang emas, muhit muhim"),
   ("zararkunandalarni yo'qotish", "ohak insektitsid emas"),
   ("tuproqni zichlash", "aksincha — unumdorlik uchun muhit tuzatiladi")],
  "Ohak tuproqdagi ortiqcha kislotalar bilan reaksiyaga kirishadi — ko'p ekinlar neytral muhitni yaxshi ko'radi.",
  dict(arch="tuproq_sahna"), fig="soil")

# 19 (3)
check("q19", 0.2*161, 32.2)
q(3, "o'rta",
  "Zn + H₂SO₄ → ZnSO₄ + H₂. 0,2 mol rux to'liq eriganda necha gramm tuz hosil bo'ladi? "
  "(M(ZnSO₄)=161)",
  "32,2 g", [("161 g", "1 mol uchun"), ("16,1 g", "0,1 mol deb olingan"), ("64,4 g", "ikki baravar")],
  "n(ZnSO₄) = 0,2 mol → m = 0,2·161 = 32,2 g.",
  dict(arch="znso4_hisob"))

# 20 (2)
q(2, "quyi",
  "Qaysi qatorda kislotalar KUCHAYIB borish tartibida joylashgan bo'lishi mumkin?",
  "H₂CO₃ → H₂SO₃ → H₂SO₄",
  [("H₂SO₄ → H₂SO₃ → H₂CO₃", "bu kuchsizlanish tartibi"),
   ("hammasi teng kuchli", "karbonat kislota juda kuchsiz"),
   ("H₂SO₃ → H₂CO₃ → H₂SO₄", "H₂CO₃ eng kuchsiz — o'rtada turolmaydi")],
  "Karbonat — juda kuchsiz, sulfit — o'rtacha, sulfat — kuchli kislota.",
  dict(arch="kislota_kuch"))

# 21 (3)
q(3, "o'rta",
  "Karbonat tuzini qanday BILIB olish mumkin?",
  "kislota qo'shilganda «vishillab» CO₂ ajratadi",
  [("suvda eritib", "ko'p tuzlar eriydi — farqlab bo'lmaydi"),
   ("rangiga qarab", "ko'p karbonatlar ham oq"),
   ("hidiga qarab", "karbonatlar hidsiz")],
  "CO₃²⁻ + 2H⁺ → H₂O + CO₂↑ — karbonatlarga sifat reaksiyasi.",
  dict(arch="karbonat_sifat"))

# 22 (2)
q(2, "o'rta",
  "Temir buyumlar nam havoda qanday modda bilan qoplanadi?",
  "zang — asosan temir(III) oksid-gidroksidlari",
  [("kuygan qatlam — sof uglerod", "uglerod havodan kelmaydi"),
   ("temir tuzi", "tuz uchun kislota kerak"),
   ("qo'rg'oshin qatlami", "boshqa metall paydo bo'lmaydi")],
  "4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃ — sekin oksidlanish (korroziya).",
  dict(arch="zang_hosil"))

# 23 (3)
check("q23", 10/100*22.4, 2.24)
q(3, "o'rta",
  "CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂. 10 g marmar to'liq eriganda ajralgan gaz hajmini (n.sh.) toping. "
  "(M(CaCO₃)=100)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("4,48 L", "ikki baravar"), ("1,12 L", "yarmi olingan")],
  "n = 0,1 mol → V(CO₂) = 2,24 L.",
  dict(arch="marmar_hisob"))

# 24 (2)
q(2, "o'rta",
  "Ishqor eritmasi teriga tegsa, nima qilish kerak?",
  "ko'p suv bilan yuvib, so'ng kuchsiz kislota (borat) eritmasi bilan ishlov berish",
  [("kuchli kislota quyish", "kuchli kislota o'zi kuydiradi"),
   ("hech narsa qilmaslik", "ishqor teri oqsillarini yemiradi"),
   ("quruq latta bilan artish", "avval albatta suv bilan yuviladi")],
  "Xavfsizlik qoidasi: suv + neytrallovchi kuchsiz eritma.",
  dict(arch="xavfsizlik"))

# 25 (3)
q(3, "o'rta",
  "Quyidagi o'zgarishni amalga oshirish uchun qaysi reagent kerak: CuSO₄ → Cu(OH)₂?",
  "NaOH eritmasi", [("H₂O", "tuz suv bilan gidroksid bermaydi"), ("HCl", "kislota gidroksid eritadi"),
                     ("Fe", "temir Cu METALLNI siqib chiqaradi")],
  "CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄.",
  dict(arch="otish_reagent"))

# 26 (3) — RASMLI: gaz ustunlari
q(3, "o'rta",
  "Diagrammada uch tajribada yig'ilgan gazlar hajmi berilgan. Qaysi tajribada VODOROD olingan "
  "bo'lishi mumkin?",
  "1-tajriba (Zn + HCl)", [("2-tajriba (CaCO₃ + HCl)", "bu CO₂ beradi"),
                            ("3-tajriba (H₂O₂ → ...)", "bu kislorod beradi"),
                            ("hech qaysi", "1-tajriba — klassik H₂ olinishi")],
  "Diagramma yorlig'idan: Zn + 2HCl → ZnCl₂ + H₂↑.",
  dict(arch="bar_gaz_oqish"), fig="bar_gaz")

# 27 (3)
check("q27", 8/80*98, 9.8)
q(3, "o'rta",
  "8 g CuO ni to'liq eritish uchun necha gramm sulfat kislota kerak? (M: CuO=80, H₂SO₄=98)",
  "9,8 g", [("98 g", "1 mol uchun"), ("4,9 g", "yarmi olingan"), ("19,6 g", "ikki baravar")],
  "n = 0,1 mol → m(H₂SO₄) = 9,8 g.",
  dict(arch="cuo_teskari"))

# 28 (2)
q(2, "o'rta",
  "Nitrat tuzlarining eruvchanligi haqida qaysi fikr to'g'ri?",
  "barcha nitratlar suvda eriydi",
  [("barchasi erimaydi", "aksincha — eruvchanlik jadvalida NO₃⁻ ustuni to'liq «E»"),
   ("faqat KNO₃ eriydi", "hammasi eriydi"),
   ("og'ir metallarniki erimaydi", "AgNO₃ ham yaxshi eriydi")],
  "NO₃⁻ tuzlari — eruvchanlik jadvalining «eng oq» ustuni.",
  dict(arch="nitrat_eruvchanlik"))

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Cu(OH)₂ namunasi asta qizdirilmoqda. Qattiq modda massasi vaqt davomida qanday o'zgaradi? "
  "Grafikni tanlang.",
  "kamayib, so'ng o'zgarmay qoladi",
  [("ortadi", "suv chiqib ketadi — massa kamayadi"),
   ("o'zgarmaydi", "parchalanish massa yo'qotadi"),
   ("nolgacha kamayadi", "CuO qattiq qoladi")],
  "Cu(OH)₂ → CuO + H₂O↑: suv uchgach massa CuO da to'xtaydi.",
  svg=dict(correct="fall_flat", d1="rise", d2="flat", d3="fall", xlab="t", ylab="m"),
  params=dict(arch="massa_grafik"))

# 30 (2)
q(2, "o'rta",
  "Qaysi tuz suvda ERIMAYDI?",
  "BaSO₄", [("NaCl", "yaxshi eriydi"), ("K₂CO₃", "ishqoriy metall tuzi — eriydi"),
             ("Cu(NO₃)₂", "nitratlar eriydi")],
  "BaSO₄ — og'ir oq cho'kma; sulfat ioniga sifat reaksiyasida ishlatiladi.",
  dict(arch="erimaydigan_tuz"))

# 31 (3)
check("q31", 4/40*40, 4); check("q31b", 0.1*58.5, 5.85)
q(3, "o'rta",
  "NaOH + HCl → NaCl + H₂O. 4 g natriy gidroksid to'liq neytrallanganda necha gramm tuz hosil "
  "bo'ladi? (M: NaOH=40, NaCl=58,5)",
  "5,85 g", [("4 g", "tuz massasi asosnikidan farq qiladi"), ("58,5 g", "1 mol uchun"),
              ("11,7 g", "ikki baravar")],
  "n = 0,1 mol → m(NaCl) = 0,1·58,5 = 5,85 g.",
  dict(arch="nacl_hisob"))

# 32 (3) — RASMLI: gaz hisobi
check("q32", 6.5/65*22.4, 2.24)
q(3, "o'rta",
  "26-diagrammadagi 1-tajribada 6,5 g rux ishlatilgan. Yig'ilgan vodorod hajmi qancha bo'lgan? "
  "(M(Zn)=65)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("6,5 L", "massa qiymati"), ("1,12 L", "yarmi")],
  "n(Zn) = 0,1 mol → V(H₂) = 0,1·22,4 = 2,24 L — diagrammadagi ustunga mos.",
  dict(arch="bar_gaz_hisob"), fig="bar_gaz")

# ---------- Y2: laboratoriya ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.2",
  ichki_pasport=[dict(n=33, element="II.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="II.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="II.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Laboratoriyada uchta probirkada rangsiz eritmalar bor: X — HCl, Y — NaOH, Z — NaCl. "
               "Ularni farqlash uchun tajribalar o'tkazildi. 33–35-savollarga A–F ro'yxatidan javob "
               "tanlang."),
  savollar_ichki=[
    "33. Lakmus X eritmada qanday rang beradi?",
    "34. Fenolftalein qaysi eritmada pushti bo'ladi?",
    "35. Z eritmaga AgNO₃ tomizilsa nima kuzatiladi?"],
  javoblar_royxati=["A) qizil", "B) Y da", "C) oq cho'kma", "D) ko'k", "E) X da", "F) gaz ajralishi"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="ko'k — ishqorda; X esa kislota"),
                   dict(variant="E", xato="fenolftalein kislotada rangsiz"),
                   dict(variant="F", xato="AgNO₃ + NaCl cho'kma beradi, gaz emas")],
  yechim=("X (HCl): lakmus qizil (A). Y (NaOH): fenolftalein pushti (B). "
          "Z (NaCl): Ag⁺ + Cl⁻ → AgCl↓ oq cho'kma (C)."),
  parametrlar=dict(arch="indikator_ssenariy"))

# ---------- O1 ----------
check("o36", 0.2*161, 32.2)
check("o37", 4.9/98*2*56, 5.6)
check("o38", 16/80, 0.2)
check("o39", 0.05*22.4, 1.12)
check("o40", 20/80*64, 16)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="Zn + H₂SO₄ → ZnSO₄ + H₂. 0,2 mol rux eriganda hosil bo'lgan tuz massasini (g) toping. "
            "(M(ZnSO₄)=161)",
      javob="32,2", yechim="n = 0,2 mol → m = 0,2·161 = 32,2 g.",
      parametrlar=dict(arch="znso4_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="4,9 g sulfat kislotani neytrallash uchun necha gramm KOH kerak? (M: H₂SO₄=98, KOH=56)",
      javob="5,6", yechim="n = 0,05 mol → KOH 0,1 mol → 5,6 g.",
      parametrlar=dict(arch="koh_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="16 g mis(II) oksidini eritish uchun necha mol HCl kerak? (M(CuO)=80)",
      javob="0,4", yechim="CuO + 2HCl: n(CuO) = 0,2 mol → n(HCl) = 0,4 mol.",
      parametrlar=dict(arch="cuo_hcl_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Mg + 2HCl → MgCl₂ + H₂. 1,2 g magniy eriganda ajralgan vodorod hajmini (n.sh., L) toping. "
            "(M(Mg)=24)",
      javob="1,12", yechim="n = 0,05 mol → V = 0,05·22,4 = 1,12 L.",
      parametrlar=dict(arch="mg_h2_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="CuO + H₂ → Cu + H₂O. 20 g mis(II) oksididan necha gramm mis olinadi? (M: CuO=80, Cu=64)",
      javob="16", yechim="n = 0,25 mol → m(Cu) = 0,25·64 = 16 g.",
      parametrlar=dict(arch="cu_qaytarish_o1")),
]

# ---------- O2 ----------
check("o41c", 12/40*120, 36)
O2 = [
 dict(n=41, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("MgO dan magniy sulfat olish topshirig'i berildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing va bu tuz olishning qaysi usuli ekanini ayting.",
             yechim=["MgO + H₂SO₄ → MgSO₄ + H₂O — asosli oksid + kislota usuli."], M=4, A=2),
        dict(savol="b) Yana qanday ikki usul bilan MgSO₄ olish mumkin? Tenglamalarini yozing.",
             yechim=["Mg + H₂SO₄ → MgSO₄ + H₂; Mg(OH)₂ + H₂SO₄ → MgSO₄ + 2H₂O."], M=4, A=3),
        dict(savol="c) 12 g MgO dan olinadigan MgSO₄ massasini hisoblang. (M: MgO=40, MgSO₄=120)",
             yechim=["n = 0,3 mol → m = 0,3·120 = 36 g."], M=4, A=3),
        dict(savol="d) Olingan eritmadan qattiq tuzni qanday ajratib olish mumkin?",
             yechim=["Eritmani bug'latish (suvni uchirish) orqali."], M=3, A=2),
      ],
      rasmiylashtirish="Tuz olish usullari: tenglama → muqobil yo'llar → hisob; M15+A10.",
      parametrlar=dict(arch="mgso4_zanjir")),
 dict(n=42, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada ikkita bir xil ko'rinishdagi oq kukun bor: biri — osh tuzi (NaCl), "
            "ikkinchisi — bo'r (CaCO₃). Quyidagilarni MULOHAZA yuritib bajaring."),
      bandlar=[
        dict(savol="a) Ikkala kukunni kimyoviy usul bilan qanday farqlash mumkinligini ikki xil yo'l "
                   "bilan tushuntiring (tenglamalar bilan).",
             yechim=["1-yo'l: kislota qo'shish — CaCO₃ «vishillaydi» (CO₂), NaCl da o'zgarish yo'q.",
                     "2-yo'l: suvda eritish — NaCl eriydi, CaCO₃ erimaydi."], M=13, A=0),
        dict(savol="b) Nega farqlashda ta'm ko'rish usulidan foydalanish mumkin emas?",
             yechim=["Laboratoriyada moddalarni tatib ko'rish qat'iyan taqiqlangan — xavfsizlik qoidasi."], M=9, A=0),
        dict(savol="c) CaCO₃ + HCl reaksiyasining tenglamasini yozing.",
             yechim=["CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂↑."], M=3, A=0),
      ],
      rasmiylashtirish="Farqlash-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="farqlash_mulohaza")),
 dict(n=43, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Kimyoviy xossalar jadvalda tekshiriladi:\n"
            "[JADVAL] Reaksiya | Kuzatish ;; Zn + HCl | ? ;; CuSO₄ + NaOH | ? ;; "
            "CaCO₃ + HCl | ? ;; AgNO₃ + NaCl | ?\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir reaksiyada nima kuzatilishini yozing.",
             yechim=["Zn+HCl: gaz (H₂); CuSO₄+NaOH: ko'k cho'kma; CaCO₃+HCl: gaz (CO₂); "
                     "AgNO₃+NaCl: oq cho'kma."], M=5, A=3),
        dict(savol="b) Barcha reaksiya tenglamalarini yozing.",
             yechim=["Zn+2HCl→ZnCl₂+H₂; CuSO₄+2NaOH→Cu(OH)₂+Na₂SO₄; CaCO₃+2HCl→CaCl₂+H₂O+CO₂; "
                     "AgNO₃+NaCl→AgCl+NaNO₃."], M=4, A=3),
        dict(savol="c) Qaysi reaksiyalar almashinish turiga kiradi?",
             yechim=["CuSO₄+NaOH, CaCO₃+HCl, AgNO₃+NaCl — almashinish; Zn+HCl — o'rin olish."], M=3, A=2),
        dict(savol="d) Gaz ajralgan reaksiyalarda gazlarni qanday farqlash mumkin?",
             yechim=["H₂ — yonuvchan («pop» tovushi); CO₂ — ohakli suvni loyqalatadi, yonishni so'ndiradi."], M=3, A=2),
      ],
      rasmiylashtirish="Kuzatishlar-jadval: belgi → tenglama → tur → farqlash; M15+A10.",
      parametrlar=dict(arch="kuzatish_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261203)
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
    d = dict(n=n, tur="Y1", element="II.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II2-A", daraja="A", bob=12, bob_nomi="Oksidlar, asoslar, kislotalar va tuzlarning xossalari",
    manba=("MS spetsifikatsiyasi II.2; darslik sinflar xossalari bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (o't o'chirgich, tish emali, mis idish, tuproqqa ohak) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
