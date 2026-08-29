# -*- coding: utf-8 -*-
"""Organik 4-bob A-varianti: Spirtlar va fenollar (III.4) — O'RGATUVCHI ★★.
Hayotiy sahnalar: antiseptik gel, antifriz, glitserinli krem, metanol xavfi."""
import json, random

OUT = "mavzu_III4A.json"
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
  "Spirtlarning funksional guruhi qaysi?",
  "–OH (gidroksil)", [("–COOH", "u karbon kislotalarda"), ("–CHO", "u aldegidlarda"),
                       ("–NH₂", "u aminlarda")],
  "Uglevodorod radikali + OH: R–OH.",
  dict(arch="oh_guruh"))

# 2 (2)
q(2, "quyi",
  "Bir atomli to'yingan spirtlarning umumiy formulasi qaysi?",
  "CₙH₂ₙ₊₁OH", [("CₙH₂ₙOH", "vodorod balansi noto'g'ri"), ("CₙH₂ₙ₋₁OH", "bu to'yinmagan radikal"),
                 ("CₙH₂ₙ₊₂O₂", "kislorod bitta")],
  "Metanol CH₃OH, etanol C₂H₅OH...",
  dict(arch="spirt_formula"))

# 3 (2)
q(2, "o'rta",
  "Etil spirtining kimyoviy formulasi qaysi?",
  "C₂H₅OH", [("CH₃OH", "u metanol"), ("C₃H₇OH", "u propanol"), ("C₂H₄(OH)₂", "u etilenglikol")],
  "«Vino spirti» — ikki uglerodli.",
  dict(arch="etanol_formula"))

# 4 (2) — SAHNA: antiseptik
q(2, "o'rta",
  "Rasmda qo'l antiseptigi: tarkibida ~70 % etanol. Spirt mikroblarni qanday «yengadi»?",
  "hujayra oqsillarini ivitib (denaturatsiya qilib) nobud qiladi",
  [("mikroblarni muzlatadi", "harorat pasaymaydi"),
   ("faqat yuvib tashlaydi", "kimyoviy ta'sir bor"),
   ("kislota hosil qiladi", "etanol kislotaga aylanmaydi qo'lda")],
  "Oqsil «pishib» qoladi — mikrob nobud bo'ladi; 70 % li eritma eng samarali.",
  dict(arch="antiseptik_sahna"), fig="sanitizer")

# 5 (2)
q(2, "o'rta",
  "Quyi spirtlar (metanol, etanol) suvda qanday eriydi?",
  "cheksiz (har qanday nisbatda) eriydi",
  [("umuman erimaydi", "OH suv bilan «do'stlashadi»"),
   ("faqat qizdirilganda", "sovuqda ham cheksiz"),
   ("cho'kma beradi", "eritma bir jinsli")],
  "OH guruhi suv bilan vodorod bog'lari hosil qiladi.",
  dict(arch="spirt_eruvchanlik"))

# 6 (2)
q(2, "o'rta",
  "Etanol natriy bilan reaksiyaga kirishganda qaysi gaz ajraladi?",
  "vodorod", [("kislorod", "OH dagi H o'rin almashadi"), ("etilen", "degidratatsiya boshqa sharoitda"),
               ("uglerod oksidi", "yonish emas")],
  "2C₂H₅OH + 2Na → 2C₂H₅ONa + H₂↑ — spirtning «kislotaliligi» juda kuchsiz bo'lsa-da bor.",
  dict(arch="na_spirt"))

# 7 (2)
q(2, "o'rta",
  "Etanol sanoatda qanday olinadi?",
  "etilenni gidratlash yoki uglevodlarni bijg'itish orqali",
  [("metanni xlorlash orqali", "u galogenalkan beradi"),
   ("benzolni nitrolash orqali", "u nitrobenzol"),
   ("suvni elektroliz qilish orqali", "u H₂ va O₂")],
  "C₂H₄ + H₂O → C₂H₅OH; yoki C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂.",
  dict(arch="etanol_olinish"))

# 8 (2) — SAHNA: antifriz
q(2, "o'rta",
  "Rasmda avtomobil antifrizi: asosi — etilenglikol. Nega u qishda muzlamaydi?",
  "glikol-suv aralashmasining muzlash harorati juda past",
  [("u umuman suyuqlik emas", "suyuqlik"),
   ("motorni isitib turadi", "issiqlikni faqat TASHIYDI"),
   ("muzlasa ham zarar yo'q", "muzlash blokni yorib yuboradi")],
  "C₂H₄(OH)₂ + suv: −40 °C gachayam suyuq — sovutish tizimi himoyada. Ehtiyot: shirin ta'mli, zaharli!",
  dict(arch="antifriz_sahna"), fig="antifreeze")

# 9 (2)
q(2, "o'rta",
  "Uch atomli spirt vakili qaysi?",
  "glitserin C₃H₅(OH)₃", [("etanol", "bir atomli"), ("etilenglikol", "ikki atomli"),
                            ("fenol", "u spirt emas — alohida sinf")],
  "Uchta OH: qovushqoq, shirin, teri uchun «namlovchi».",
  dict(arch="glitserin"))

# 10 (3)
check("q10", 9.2/46*2*22.4, 8.96)
q(3, "o'rta",
  "C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O. 9,2 g etanol yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(M(C₂H₅OH)=46)",
  "8,96 L", [("4,48 L", "koeffitsiyent 2"), ("22,4 L", "1 mol uchun"), ("2,24 L", "hisob xato")],
  "n = 0,2 → n(CO₂) = 0,4 mol → V = 8,96 L.",
  dict(arch="etanol_yonish"))

# 11 (2)
q(2, "o'rta",
  "Fenol molekulasida OH guruhi qayerga birikkan?",
  "bevosita benzol halqasiga",
  [("alkil zanjirga", "u holda aromatik spirt bo'lardi"),
   ("kislota qoldig'iga", "fenol tuz emas"),
   ("azot atomiga", "fenolda azot yo'q")],
  "C₆H₅–OH: halqa OH xossalarini keskin o'zgartiradi.",
  dict(arch="fenol_tuzilish"))

# 12 (3)
check("q12", 46, 46)
q(3, "o'rta",
  "Molyar massasi 46 g/mol bo'lgan bir atomli spirtni aniqlang.",
  "etanol", [("metanol", "M = 32"), ("propanol", "M = 60"), ("glitserin", "M = 92")],
  "14n + 18 = 46 → n = 2.",
  dict(arch="m46"))

# 13 (2) — SAHNA: glitserin krem
q(2, "o'rta",
  "Rasmda qo'l kremi: tarkibida glitserin. U teriga qanday foyda beradi?",
  "namlikni tortib, terini yumshoq saqlaydi",
  [("terini oqartiradi", "asosiy ishi — namlash"),
   ("mikroblarni o'ldiradi kuchli", "u antiseptik emas — namlovchi"),
   ("terini qizdiradi", "isitish xossasi yo'q")],
  "Uch OH guruhi suvni «magnitday» tortadi — gigroskopik namlovchi.",
  dict(arch="krem_sahna"), fig="cream")

# 14 (2)
q(2, "o'rta",
  "Spirtlar nomlarida qaysi qo'shimcha ishlatiladi?",
  "-ol", [("-al", "aldegidlarda"), ("-en", "alkenlarda"), ("-in", "alkinlarda")],
  "Metan → metanol; etan → etanol.",
  dict(arch="ol_qoshimcha"))

# 15 (2)
q(2, "o'rta",
  "Ko'p atomli spirtlarga SIFAT reaksiyasi qaysi?",
  "yangi cho'ktirilgan Cu(OH)₂ bilan yorqin ko'k eritma berishi",
  [("bromli suvni rangsizlantirish", "u to'yinmaganlar sinovi"),
   ("lakmusni qizartirish", "spirtlar neytral"),
   ("«pop» tovushi", "u vodorod sinovi")],
  "Glitserin + Cu(OH)₂ → zangori-ko'k glitserat — «ko'p OH» belgisi.",
  dict(arch="cuoh2_sinov"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Spirt | OH soni ;; etanol | ? ;; etilenglikol | ? ;; glitserin | ?",
  "1; 2; 3",
  [("1; 3; 2", "glikol — «ikki», glitserin — «uch»"), ("2; 2; 3", "etanol bir atomli"),
   ("1; 2; 4", "glitserinda uchta")],
  "Atomlilik = OH guruhlar soni.",
  dict(arch="oh_soni_jadval"))

# 17 (2)
q(2, "o'rta",
  "Metanol iste'mol qilinsa nima bo'ladi?",
  "og'ir zaharlanish: ko'rlik va o'limga olib keladi",
  [("oddiy spirtdek ta'sir qiladi", "8-10 mL ham ko'r qilishi mumkin"),
   ("hech narsa bo'lmaydi", "o'ta xavfli!"),
   ("faqat bosh og'riydi", "oqibati fojiali")],
  "CH₃OH organizmda chumoli aldegidi/kislotasiga aylanadi — «yolg'on ichimliklar» fojialarining sababi.",
  dict(arch="metanol_xavf"))

# 18 (2) — SAHNA: metanol ogohlantirish
q(2, "o'rta",
  "Rasmda «Texnik spirt — ichish MUMKIN EMAS» yorlig'i. Metanolni etanoldan uy sharoitida ajratib "
  "bo'lmasligining sababi nimada?",
  "rangi, hidi va ta'mi deyarli bir xil",
  [("metanol qora rangda", "ikkalasi rangsiz"),
   ("metanol hidsiz", "hidi o'xshash"),
   ("farqi shishasida", "idish emas, modda muhim")],
  "Faqat laboratoriya aniqlaydi — shu bois nomalum spirtli suyuqlik ichilmaydi.",
  dict(arch="metanol_yorliq_sahna"), fig="warning")

# 19 (3)
check("q19", 9.2/46/2*22.4, 2.24)
q(3, "o'rta",
  "2C₂H₅OH + 2Na → 2C₂H₅ONa + H₂. 9,2 g etanol natriy bilan to'liq reaksiyaga kirishganda ajralgan "
  "vodorod hajmini (n.sh.) toping.",
  "2,24 L", [("4,48 L", "H₂ koeffitsiyenti ikki barobar kam"), ("22,4 L", "1 mol uchun"),
              ("1,12 L", "hisob xato")],
  "n = 0,2 → n(H₂) = 0,1 mol → V = 2,24 L.",
  dict(arch="na_spirt_hisob"))

# 20 (2)
q(2, "o'rta",
  "Fenolning eski texnik nomi qanday?",
  "karbol kislota", [("sirka kislota", "u CH₃COOH"), ("nashatir", "u NH₃ eritmasi"),
                      ("tuz kislotasi", "u HCl")],
  "Birinchi antiseptiklardan: jarrohlikda asboblarni zararsizlantirgan.",
  dict(arch="karbol"))

# 21 (2)
q(2, "o'rta",
  "Spirtlarning alkanlardan yuqori haroratda qaynashining sababi nimada?",
  "molekulalar orasidagi vodorod bog'lari",
  [("massasi kattaligi", "etan (30) va metanol (32) yaqin, lekin farq katta"),
   ("rangi", "rang xossaga ta'sir qilmaydi"),
   ("tasodif", "qonuniy sabab bor")],
  "OH...O «ko'priklari» molekulalarni ushlab turadi — bug'lanish qiyin.",
  dict(arch="vodorod_bog"))

# 22 (2)
q(2, "o'rta",
  "Tibbiyotda yod eritmasi qanday erituvchida tayyorlanadi?",
  "etil spirtida", [("suvda", "yod suvda yomon eriydi"), ("benzinda", "teri uchun yaroqsiz"),
                     ("kislotada", "teriga kislota surtilmaydi")],
  "«Yod nastoykasi» — 5 % li spirtli eritma.",
  dict(arch="yod_nastoyka"))

# 23 (3)
check("q23", 0.2*92, 18.4)
q(3, "o'rta",
  "0,2 mol glitserinning massasini toping. (M(C₃H₈O₃)=92)",
  "18,4 g", [("92 g", "1 mol uchun"), ("9,2 g", "0,1 mol emas"), ("36,8 g", "ikki baravar")],
  "m = 0,2·92 = 18,4 g.",
  dict(arch="glitserin_massa"))

# 24 (2)
q(2, "o'rta",
  "Spirt lampalarda yoqilg'i sifatida etanol ishlatilishining sababi qaysi?",
  "toza, qurumsiz alanga bilan yonadi",
  [("juda arzonligi", "asosiy sabab — toza yonish"),
   ("yonmasligi", "aksincha, yaxshi yonadi"),
   ("rangli alangasi", "alanga xira-ko'kish")],
  "C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O: idish tagini qoraytirmaydi.",
  dict(arch="spirt_lampa_a"))

# 25 (3)
q(3, "o'rta",
  "Zanjirdagi X moddani aniqlang: C₂H₄ → X → C₂H₅ONa.",
  "C₂H₅OH", [("C₂H₆", "etan natriy bilan kirishmaydi"), ("CH₃CHO", "aldegid alkogolyat bermaydi"),
              ("C₂H₅Cl", "xlorid boshqa yo'l")],
  "Gidratlanish → spirt; spirt + Na → alkogolyat.",
  dict(arch="zanjir_x_4"))

# 26 (3) — RASMLI: antiseptik diagramma
q(3, "o'rta",
  "Diagrammada turli konsentratsiyali spirtning mikroblarga ta'siri berilgan. Nega 96 % li spirt "
  "70 % lidan SAMARASIZROQ?",
  "juda kuchli spirt mikrob «qobig'ini» tez ivitib, ichiga kirolmaydi",
  [("96 % li spirt mikrobni oziqlantiradi", "bunday emas"),
   ("diagramma xato", "bu tasdiqlangan fakt"),
   ("70 % li arzonroq bo'lgani uchun", "gap narxda emas — mexanizmda")],
  "Sirt oqsili zich ivib «zirh» bo'ladi; 70 % li esa asta kirib to'liq ta'sir qiladi.",
  dict(arch="bar_antiseptik_oqish"), fig="bar_antiseptic")

# 27 (3)
check("q27", 32, 32)
q(3, "o'rta",
  "Molyar massasi 32 g/mol bo'lgan spirtni aniqlang.",
  "metanol (CH₃OH)", [("etanol", "M = 46"), ("propanol", "M = 60"), ("suv (H₂O)", "spirt emas, lekin M = 18 chalg'itadi")],
  "12 + 4 + 16 = 32.",
  dict(arch="m32"))

# 28 (2) — RASMLI: qaynash grafigi
q(2, "o'rta",
  "Grafikda spirtlar qaynash haroratlari: metanol 65°, etanol 78°, propanol 97 °C. Qator bo'ylab "
  "qaynash qanday o'zgaradi?",
  "ortib boradi", [("kamayadi", "molekula kattalashadi"), ("o'zgarmaydi", "grafik ko'tarilyapti"),
                    ("tartibsiz", "monoton o'sish")],
  "Zanjir uzaygani sari molekulalararo tortishuv kuchayadi.",
  dict(arch="spirt_bp_oqish"), fig="bp_spirt")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Etanol suvda eritilmoqda. Eritmadagi spirt ulushi qo'shilgan suv miqdoriga qarab qanday "
  "o'zgaradi? Grafikni tanlang.",
  "kamayib boradi",
  [("ortadi", "suyultirish kamaytiradi"), ("o'zgarmaydi", "nisbat o'zgaradi-ku"),
   ("avval ortib keyin kamayadi", "boshidanoq kamayadi")],
  "Spirt massasi o'zgarmay, eritma massasi o'sadi.",
  svg=dict(correct="fall", d1="rise", d2="flat", d3="rise_fall", xlab="suv", ylab="ω(spirt)"),
  params=dict(arch="suyultirish_grafik_4"))

# 30 (2)
q(2, "o'rta",
  "Fenol eritmasi teriga tegsa nima qilinadi?",
  "ko'p suv bilan, so'ng spirt bilan yuviladi — fenol kuydiradi",
  [("hech narsa qilinmaydi", "kimyoviy kuyish beradi"),
   ("kislota bilan yuviladi", "yana zarar"),
   ("bint bilan yopiladi faqat", "avval yuvish shart")],
  "Fenol — zaharli va kuydiruvchi: rezina qo'lqop bilan ishlanadi.",
  dict(arch="fenol_xavf"))

# 31 (3)
check("q31", 13.8/46, 0.3)
q(3, "o'rta",
  "13,8 g etanol necha mol bo'ladi? (M=46)",
  "0,3", [("3", "gramm-mol adashuvi"), ("0,15", "yarmi"), ("0,6", "ikki baravar")],
  "n = 13,8/46 = 0,3 mol.",
  dict(arch="etanol_mol"))

# 32 (3) — RASMLI: antiseptik hisob
check("q32", 250*0.7, 175)
q(3, "o'rta",
  "26-savol ma'lumotidan: 250 mL 70 % li antiseptikda necha mL sof spirt bor (hajmiy ulush deb "
  "hisoblang)?",
  "175 mL", [("70 mL", "250 ning 70 %i"), ("75 mL", "bu suv emas"), ("245 mL", "hisob xato")],
  "V = 250·0,7 = 175 mL.",
  dict(arch="bar_antiseptik_hisob"), fig="bar_antiseptic")

# ---------- Y2: uch suyuqlik ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.4",
  ichki_pasport=[dict(n=33, element="III.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="III.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="III.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch maishiy suyuqlik bor: X — qo'l antiseptigi asosi; Y — avtomobil antifrizi asosi; "
               "Z — qo'l kremidagi qovushqoq, shirin modda. 33–35-savollarga A–F ro'yxatidan javob "
               "tanlang."),
  savollar_ichki=[
    "33. X modda qaysi?",
    "34. Y modda qaysi?",
    "35. Z moddaga Cu(OH)₂ qo'shilsa nima kuzatiladi?"],
  javoblar_royxati=["A) etanol", "B) etilenglikol", "C) yorqin ko'k eritma", "D) metanol",
                    "E) glitserin", "F) oq cho'kma"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="metanol antiseptikka qo'shilmaydi — zaharli"),
                   dict(variant="E", xato="savol Z ning REAKSIYASI haqida"),
                   dict(variant="F", xato="ko'p atomli spirt cho'kma emas, ko'k eritma beradi")],
  yechim=("X — etanol (A). Y — etilenglikol (B). Z — glitserin: Cu(OH)₂ bilan yorqin ko'k "
          "glitserat (C)."),
  parametrlar=dict(arch="maishiy_ssenariy"))

# ---------- O1 ----------
check("o36", 0.2*46, 9.2)
check("o37", 6.4/32, 0.2)
check("o38", 0.5*3*22.4, 33.6)
check("o39", 4.6/46/2*22.4, 1.12)
check("o40", 0.1*92, 9.2)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,2 mol etanolning massasini (g) toping. (M=46)",
      javob="9,2", yechim="m = 0,2·46 = 9,2 g.",
      parametrlar=dict(arch="etanol_massa_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="6,4 g metanol necha mol bo'ladi? (M=32)",
      javob="0,2", yechim="n = 6,4/32 = 0,2 mol.",
      parametrlar=dict(arch="metanol_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O. 0,5 mol etanol yonishi uchun zarur kislorod hajmini "
            "(n.sh., L) toping.",
      javob="33,6", yechim="n(O₂) = 1,5 mol → V = 33,6 L.",
      parametrlar=dict(arch="etanol_o2_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="4,6 g etanol natriy bilan to'liq reaksiyaga kirishganda ajralgan vodorod hajmini "
            "(n.sh., L) toping.",
      javob="1,12", yechim="n = 0,1 → n(H₂) = 0,05 mol → V = 1,12 L.",
      parametrlar=dict(arch="na_h2_o1_4")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="0,1 mol glitserinning massasini (g) toping. (M=92)",
      javob="9,2", yechim="m = 0,1·92 = 9,2 g.",
      parametrlar=dict(arch="glitserin_o1")),
]

# ---------- O2 ----------
check("o41b", 23/46, 0.5); check("o41c", 0.5*2*22.4, 22.4)
O2 = [
 dict(n=41, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Spirt lampada 23 g etanol yoqildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Yonish tenglamasini yozing.",
             yechim=["C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O."], M=4, A=2),
        dict(savol="b) Etanol mol miqdorini toping.",
             yechim=["n = 23/46 = 0,5 mol."], M=4, A=3),
        dict(savol="c) Hosil bo'lgan CO₂ hajmini (n.sh.) hisoblang.",
             yechim=["n(CO₂) = 1 mol → V = 22,4 L."], M=4, A=3),
        dict(savol="d) Nega spirt alangasi qurumsiz? Izohlang.",
             yechim=["Molekulada kislorod «ichida» bor — yonish to'liq boradi."], M=3, A=2),
      ],
      rasmiylashtirish="Etanol-yonish: tenglama → mol → hajm → izoh; M15+A10.",
      parametrlar=dict(arch="etanol_yonish_zanjir")),
 dict(n=42, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Spirtlardagi vodorod bog'i hodisasi tahlil qilinadi. Quyidagilarga MULOHAZA yuritib "
            "javob yozing."),
      bandlar=[
        dict(savol="a) Nega etanol (M=46) gaz emas, suyuqlik, vaholanki og'irroq butan (M=58) gaz? "
                   "Batafsil tushuntiring.",
             yechim=["Spirt molekulalari OH orqali vodorod bog'lari bilan «tikilgan» —",
                     "ularni uzishga qo'shimcha energiya ketadi, qaynash harorati keskin yuqori."], M=13, A=0),
        dict(savol="b) Xuddi shu sabab spirtlarning suvda erishini qanday tushuntiradi?",
             yechim=["OH guruhi suv molekulalari bilan ham vodorod bog' hosil qiladi — cheksiz aralashish."], M=9, A=0),
        dict(savol="c) Zanjir uzayganda (C₅ va undan yuqori) eruvchanlik nega kamayadi?",
             yechim=["Katta uglevodorod «dumi» suvni «yoqtirmaydi» — gidrofob qism ustun keladi."], M=3, A=0),
      ],
      rasmiylashtirish="Vodorod-bog' mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="vodorod_bog_mulohaza")),
 dict(n=43, tur="O2", element="III.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch suyuqlik jadvalda berilgan:\n"
            "[JADVAL] № | Modda ;; 1 | etanol ;; 2 | glitserin ;; 3 | fenol eritmasi\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har birining sinfini aniqlang.",
             yechim=["Etanol — bir atomli spirt; glitserin — uch atomli spirt; fenol — aromatik "
                     "gidroksid (fenollar sinfi)."], M=4, A=2),
        dict(savol="b) Qaysi biri Cu(OH)₂ bilan yorqin ko'k eritma beradi?",
             yechim=["Glitserin (ko'p atomlilik sinovi)."], M=3, A=3),
        dict(savol="c) Qaysi biri bromli suv bilan OQ CHO'KMA beradi? Tenglama yozing.",
             yechim=["Fenol: C₆H₅OH + 3Br₂ → C₆H₂Br₃OH↓ + 3HBr."], M=5, A=3),
        dict(savol="d) Uchchalasi uchun umumiy bo'lgan reaksiyani ayting.",
             yechim=["Natriy bilan H₂ ajratish (OH guruhi bor)."], M=3, A=2),
      ],
      rasmiylashtirish="OH-uchlik: sinf → Cu(OH)₂ → Br₂ → umumiylik; M15+A10.",
      parametrlar=dict(arch="oh_uchlik_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263403)
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
    variant="mavzu-III4-A", daraja="A", bob=4, bob_nomi="Spirtlar va fenollar",
    manba=("MS spetsifikatsiyasi III.4; 10-sinf darslik — savollar yangi tuzilgan, hayotiy sahnalar "
           "(antiseptik, antifriz, krem, metanol xavfi) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
