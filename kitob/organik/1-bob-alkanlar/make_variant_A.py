# -*- coding: utf-8 -*-
"""Organik 1-bob A-varianti: Organik kimyo nazariyasi. Alkanlar (III.1) — O'RGATUVCHI ★★.
Hayotiy sahnalar: gaz plita, propan-butan ballon, neft qudug'i, gazga hid beruvchi."""
import json, random

OUT = "mavzu_III1A.json"
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
  "Organik kimyo nimani o'rganadi?",
  "uglerod birikmalarini (uglevodorodlar va ularning hosilalarini)",
  [("faqat tirik organizmlarni", "biologiya bilan adashtirilgan"),
   ("metallarning birikmalarini", "bu anorganik kimyo"),
   ("faqat gazlarni", "organik moddalar har uch holatda bo'ladi")],
  "Millionlab organik moddalarning asosi — uglerod atomining zanjir hosil qilish qobiliyati.",
  dict(arch="organika_tarif"))

# 2 (2)
q(2, "quyi",
  "Organik birikmalarda uglerodning valentligi qanday?",
  "doimo IV", [("II", "CO da shunday, organikada emas"), ("VI", "uglerodda bo'lmaydi"),
                ("o'zgaruvchan", "organikada qat'iy to'rt")],
  "Butlerov nazariyasining tayanchi: C — to'rt valentli, 4 ta bog' hosil qiladi.",
  dict(arch="c_valentlik"))

# 3 (2)
q(2, "o'rta",
  "Organik moddalar tuzilish nazariyasining asoschisi kim?",
  "A. M. Butlerov",
  [("D. I. Mendeleyev", "u davriy qonun asoschisi"),
   ("M. V. Lomonosov", "massa saqlanish qonuni bilan bog'liq"),
   ("A. Lavuazye", "yonish nazariyasi bilan mashhur")],
  "1861-yil: «Moddaning xossalari uning kimyoviy tuzilishiga bog'liq».",
  dict(arch="butlerov"))

# 4 (2) — SAHNA: gaz plita
q(2, "o'rta",
  "Rasmda gaz plitaning KO'K alangasi. Bu qaysi gaz va nima uchun alanga ko'k?",
  "metan; kislorod yetarli bo'lganda to'liq yonadi",
  [("vodorod; u doim ko'k yonadi", "uy gazi — metan"),
   ("is gazi; xavfli gaz", "CO yoqilg'i sifatida uyga berilmaydi"),
   ("propan sof holda", "asosiy uy gazi — tabiiy gaz (metan)")],
  "CH₄ + 2O₂ → CO₂ + 2H₂O: to'liq yonish — ko'k alanga; sariq alanga kislorod yetishmasligini bildiradi.",
  dict(arch="plita_sahna"), fig="stove")

# 5 (2)
q(2, "o'rta",
  "Alkanlarning UMUMIY formulasi qaysi?",
  "CₙH₂ₙ₊₂", [("CₙH₂ₙ", "bu alkenlar/sikloalkanlar"), ("CₙH₂ₙ₋₂", "bu alkinlar"),
               ("CₙHₙ", "bunday qator asosiy emas")],
  "Metan CH₄, etan C₂H₆, propan C₃H₈... — har C ga «2n+2» vodorod.",
  dict(arch="alkan_formula"))

# 6 (2)
q(2, "o'rta",
  "GOMOLOGLAR deb qanday moddalarga aytiladi?",
  "tuzilishi o'xshash, tarkibi CH₂ ga farq qiladigan moddalarga",
  [("tarkibi bir xil, tuzilishi har xil moddalarga", "bu izomerlar"),
   ("bir xil massali moddalarga", "massa emas, qator muhim"),
   ("faqat gazsimon moddalarga", "gomologlar suyuq-qattiq ham bo'ladi")],
  "CH₄ va C₂H₆ — gomologlar: farqi bitta CH₂ zvenosi.",
  dict(arch="gomolog_tarif"))

# 7 (2)
q(2, "o'rta",
  "IZOMERLAR deb qanday moddalarga aytiladi?",
  "molekulyar formulasi bir xil, tuzilishi har xil moddalarga",
  [("tarkibi CH₂ ga farq qiladigan moddalarga", "bu gomologlar"),
   ("bir elementdan iborat moddalarga", "bu allotropiya"),
   ("har xil formulali moddalarga", "formula aynan BIR XIL bo'ladi")],
  "C₄H₁₀: butan va izobutan — bir formula, ikki xil zanjir, har xil xossa.",
  dict(arch="izomer_tarif"))

# 8 (2) — SAHNA: gaz balloni
q(2, "o'rta",
  "Rasmda avtomobil va uy uchun «propan-butan» ballonlari. Nega bu gazlar BALLONDA suyuq holda "
  "saqlanadi?",
  "bosim ostida oson suyuladi — kam joyda ko'p yoqilg'i sig'adi",
  [("ular odatda suyuqlik", "oddiy sharoitda gaz"),
   ("ballonda sovutiladi", "sovutgich yo'q — bosim ishlaydi"),
   ("suyuq holda yonmaydi", "xavfsizlikka aloqasi boshqa")],
  "C₃H₈ va C₄H₁₀ ning qaynash haroratlari yuqoriroq — xona haroratida bosim bilan suyuladi.",
  dict(arch="ballon_sahna"), fig="balloon_gas")

# 9 (2)
q(2, "o'rta",
  "Metanning laboratoriyada olinish usuli qaysi?",
  "natriy atsetatni natron ohak bilan qizdirish",
  [("suvni elektroliz qilish", "u H₂ va O₂ beradi"),
   ("ohaktoshni kuydirish", "u CO₂ beradi"),
   ("ammiakni oksidlash", "u NO beradi")],
  "CH₃COONa + NaOH → CH₄↑ + Na₂CO₃ (natron ohak bilan qizdirilganda).",
  dict(arch="metan_olinish"))

# 10 (3)
check("q10", 4.48/22.4*22.4, 4.48)
q(3, "o'rta",
  "CH₄ + 2O₂ → CO₂ + 2H₂O. 4,48 L (n.sh.) metan yonganda hosil bo'lgan CO₂ hajmini toping.",
  "4,48 L", [("2,24 L", "nisbat 1:1"), ("8,96 L", "bu suv bug'iga tegishli nisbat"), ("22,4 L", "1 mol uchun")],
  "n(CH₄) = n(CO₂) = 0,2 mol → V = 4,48 L.",
  dict(arch="metan_co2_hisob"))

# 11 (2)
q(2, "o'rta",
  "Alkanlarning gomologik qatorida birinchi TO'RT vakil qanday nomlanadi?",
  "metan, etan, propan, butan",
  [("metan, eten, propen, buten", "-en qo'shimchasi alkenlarda"),
   ("metanol, etanol, propanol, butanol", "bular spirtlar"),
   ("metin, etin, propin, butin", "-in alkinlarda")],
  "«MEPB» — dastlabki to'rtlik; beshinchidan boshlab yunoncha sonlar: pentan, geksan...",
  dict(arch="alkan_nomlar"))

# 12 (3)
check("q12", 58, 58)
q(3, "o'rta",
  "Molyar massasi 58 g/mol bo'lgan alkanning molekulyar formulasini toping.",
  "C₄H₁₀", [("C₃H₈", "M = 44"), ("C₅H₁₂", "M = 72"), ("C₄H₈", "bu alken (M=56)")],
  "12n + 2n + 2 = 58 → 14n = 56 → n = 4 — butan.",
  dict(arch="m_dan_formula"))

# 13 (2) — SAHNA: neft qudug'i
q(2, "o'rta",
  "Rasmda neft qudug'i. Neft asosan qanday moddalar aralashmasi?",
  "turli uglevodorodlar (asosan alkanlar) aralashmasi",
  [("bitta toza modda", "neft — murakkab aralashma"),
   ("faqat metan", "metan — tabiiy gaz asosi"),
   ("mineral tuzlar eritmasi", "organik aralashma")],
  "Neftda yuzlab uglevodorodlar bor; haydash orqali benzin, kerosin va boshqalarga ajratiladi.",
  dict(arch="neft_sahna"), fig="oilrig")

# 14 (2)
q(2, "o'rta",
  "Alkanlar oddiy sharoitda kimyoviy jihatdan qanday?",
  "ancha inert — «parafinlar» deb ham ataladi",
  [("juda faol", "faollik alken/alkinlarga xos"),
   ("faqat ishqorlar bilan reaksiyaga kirishadi", "ishqor bilan kirishmaydi"),
   ("suvda yaxshi eriydi", "suvda deyarli erimaydi")],
  "Barcha bog'lar — mustahkam sigma-bog': shu bois «parum affinis» (kam moyil).",
  dict(arch="alkan_inertlik"))

# 15 (2)
q(2, "o'rta",
  "2-metilpropan qaysi moddaning izomeri?",
  "butan (C₄H₁₀)", [("propan", "C₃H₈ da izomer yo'q"), ("pentan", "u C₅H₁₂"),
                     ("etan", "juda kichik")],
  "Ikkalasining formulasi C₄H₁₀; farqi — zanjir shakli (to'g'ri va tarmoqlangan).",
  dict(arch="izobutan"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Alkan | Formula ;; metan | ? ;; propan | ? ;; pentan | ?",
  "CH₄; C₃H₈; C₅H₁₂",
  [("CH₄; C₃H₆; C₅H₁₀", "CₙH₂ₙ₊₂ bo'lishi kerak"), ("C₂H₆; C₃H₈; C₄H₁₀", "metan — CH₄"),
   ("CH₄; C₄H₁₀; C₅H₁₂", "propan — uch uglerodli")],
  "n = 1, 3, 5 → CH₄, C₃H₈, C₅H₁₂.",
  dict(arch="formula_jadval"))

# 17 (2)
q(2, "o'rta",
  "Butanning nechta zanjir izomeri bor?",
  "2 ta", [("1 ta", "izobutan ham bor"), ("3 ta", "3 ta — pentanda"), ("4 ta", "ko'p emas")],
  "n-butan va 2-metilpropan (izobutan).",
  dict(arch="butan_izomer"))

# 18 (2) — SAHNA: gaz hidi
q(2, "o'rta",
  "Rasmda gaz sizishini sezgan odam. Tabiiy gaz aslida HIDSIZ — biz sezadigan «gaz hidi» qayerdan?",
  "gazga ataylab o'tkir hidli modda (merkaptan) qo'shiladi",
  [("metanning o'z hidi shunday", "sof CH₄ hidsiz"),
   ("quvurlarning hidi", "quvur hid bermaydi"),
   ("hid tuyulishi — xato", "aynan xavfsizlik uchun qo'shilgan hid")],
  "Odorant sizishni darhol sezdiradi — portlashning oldini oladigan «signal hid».",
  dict(arch="odorant_sahna"), fig="gasleak")

# 19 (3)
check("q19", 4.4/44*3*22.4, 6.72)
q(3, "o'rta",
  "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O. 4,4 g propan yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(M(C₃H₈)=44)",
  "6,72 L", [("2,24 L", "koeffitsiyent 3 unutilgan"), ("22,4 L", "1 mol uchun"), ("4,48 L", "hisob xato")],
  "n = 0,1 mol → n(CO₂) = 0,3 → V = 6,72 L.",
  dict(arch="propan_hisob"))

# 20 (2)
q(2, "o'rta",
  "Uglerod atomlari orasidagi bog' alkanlarda qanday?",
  "birlamchi (yakka) sigma-bog'lar",
  [("qo'shbog'lar", "qo'shbog' — alkenlarda"), ("uchbog'lar", "uchbog' — alkinlarda"),
   ("ion bog'lar", "organikada kovalent bog')")],
  "To'yingan uglevodorodlar: barcha bog'lar «to'yingan» — faqat C−C va C−H.",
  dict(arch="sigma_bog"))

# 21 (2)
q(2, "o'rta",
  "Metan havodan yengilmi yoki og'irmi?",
  "yengil (M=16 < 29)",
  [("og'ir", "16 < 29"), ("bir xil", "farq salmoqli"), ("holatga bog'liq", "M o'zgarmaydi")],
  "Shu bois sizgan gaz shift ostida to'planadi — xonani yuqoridan shamollatish kerak.",
  dict(arch="metan_zichlik"))

# 22 (2)
q(2, "o'rta",
  "Sikloalkanlarning umumiy formulasi qanday?",
  "CₙH₂ₙ", [("CₙH₂ₙ₊₂", "bu alkanlar"), ("CₙH₂ₙ₋₂", "bu alkinlar"), ("CₙH₂ₙ₊₁", "radikal formulasi")],
  "Halqa yopilishi ikki vodorodni «yeydi»: siklopropan C₃H₆, siklogeksan C₆H₁₂.",
  dict(arch="sikloalkan_formula"))

# 23 (3)
check("q23", 0.2*44, 8.8)
q(3, "o'rta",
  "0,2 mol propanning massasini toping. (M(C₃H₈)=44)",
  "8,8 g", [("44 g", "1 mol uchun"), ("4,4 g", "0,1 mol emas"), ("17,6 g", "ikki baravar")],
  "m = 0,2·44 = 8,8 g.",
  dict(arch="propan_massa"))

# 24 (2)
q(2, "o'rta",
  "Kislorod yetishmaganda metan CHALA yonsa nima hosil bo'lishi mumkin?",
  "zaharli is gazi (CO) yoki qurum (C)",
  [("faqat CO₂", "to'liq yonishda shunday"), ("vodorod", "H suvga o'tadi"),
   ("metanol", "yonishda spirt hosil bo'lmaydi")],
  "Shu bois gaz asboblari xonasida ventilyatsiya SHART.",
  dict(arch="chala_yonish_a"))

# 25 (3)
q(3, "o'rta",
  "IUPAC bo'yicha CH₃–CH(CH₃)–CH₂–CH₃ birikmasining nomi qanday?",
  "2-metilbutan",
  [("3-metilbutan", "raqamlash yaqin uchidan"), ("pentan", "pentan — to'g'ri zanjirli C₅H₁₂"),
   ("2-metilpropan", "asosiy zanjir to'rt uglerodli")],
  "Eng uzun zanjir — butan; metil 2-holatda (kichik raqam tomonidan).",
  dict(arch="nomlash_oddiy"))

# 26 (3) — RASMLI: tabiiy gaz tarkibi
q(3, "o'rta",
  "Diagrammada tabiiy gaz tarkibi berilgan. Undagi ASOSIY komponent qaysi?",
  "metan (≈ 93 %)", [("etan (≈ 4 %)", "ikkinchi o'rinda"), ("propan-butan", "oz miqdorda"),
                      ("azot", "aralashma sifatida ozgina")],
  "Tabiiy gaz deyarli sof metan — eng «toza» qazilma yoqilg'i.",
  dict(arch="bar_gaz_tarkib"), fig="bar_gas")

# 27 (3)
check("q27", 30, 30)
q(3, "o'rta",
  "Vodorodga nisbatan zichligi 15 bo'lgan alkanni aniqlang.",
  "etan (C₂H₆)", [("metan", "M = 16, zichligi 8"), ("propan", "M = 44, zichligi 22"),
                   ("butan", "M = 58, zichligi 29")],
  "M = 15·2 = 30 → 14n+2 = 30 → n = 2 — etan.",
  dict(arch="zichlik_formula"))

# 28 (2) — RASMLI: qaynash grafigi
q(2, "o'rta",
  "Grafikda alkanlar qaynash haroratlari berilgan. Qator bo'ylab (CH₄ → C₅H₁₂) qaynash harorati "
  "qanday o'zgaradi?",
  "ortib boradi", [("kamayadi", "molekula kattalashgani sari ortadi"), ("o'zgarmaydi", "grafik ko'tarilyapti"),
                    ("tartibsiz", "qonuniy o'sish")],
  "Molekulalararo tortishuv kuchayadi: C₁–C₄ gaz, C₅ dan suyuq.",
  dict(arch="bp_oqish_a"), fig="bp_alkan")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Yonayotgan metan miqdori ortib borsa, ajralayotgan CO₂ hajmi qanday o'zgaradi? Grafikni tanlang.",
  "to'g'ri proporsional ortadi",
  [("o'zgarmaydi", "har mol metan o'z CO₂ sini beradi"),
   ("kamayadi", "aksincha"),
   ("avval ortib, keyin to'xtaydi", "kislorod yetarli bo'lsa chegara yo'q")],
  "n(CO₂) = n(CH₄) — chiziqli bog'lanish.",
  svg=dict(correct="rise", d1="flat", d2="fall", d3="rise_flat", xlab="n(CH₄)", ylab="V(CO₂)"),
  params=dict(arch="yonish_grafik_a"))

# 30 (2)
q(2, "o'rta",
  "«To'yingan uglevodorodlar» atamasi nimani anglatadi?",
  "molekulada vodorod maksimal miqdorda — qo'shbog' yo'q",
  [("suvga to'yingan", "suvga aloqasi yo'q"),
   ("kislorodga boy", "tarkibda O umuman yo'q"),
   ("og'ir moddalar", "massa emas, bog' turi muhim")],
  "Har uglerod «to'rt qo'li» bilan band: qo'shimcha atom biriktira olmaydi.",
  dict(arch="toyingan_manosi"))

# 31 (3)
check("q31", 7.2/72, 0.1)
q(3, "o'rta",
  "7,2 g pentan necha mol bo'ladi? (M(C₅H₁₂)=72)",
  "0,1", [("1", "gramm-mol adashuvi"), ("0,2", "ikki baravar"), ("0,05", "yarmi")],
  "n = 7,2/72 = 0,1 mol.",
  dict(arch="pentan_mol"))

# 32 (3) — RASMLI: gaz tarkibi hisob
check("q32", 100*0.93, 93)
q(3, "o'rta",
  "26-savol diagrammasidan: 100 m³ tabiiy gazda taxminan qancha metan bor?",
  "93 m³", [("50 m³", "diagrammada 93 %"), ("21 m³", "bu havo kislorodiga o'xshash xato"),
             ("100 m³", "boshqa gazlar ham bor")],
  "V = 100·0,93 = 93 m³.",
  dict(arch="bar_gaz_hisob_a"), fig="bar_gas")

# ---------- Y2: uy gazi ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.1",
  ichki_pasport=[dict(n=33, element="III.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="III.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="III.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch yoqilg'i solishtirildi: X — uy quvuridagi tabiiy gaz; Y — ballondagi suyultirilgan "
               "gaz; Z — avtomobil benzini. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X ning asosiy komponenti qaysi?",
    "34. Y tarkibiga kiruvchi juftlik qaysi?",
    "35. Z qanday aralashma?"],
  javoblar_royxati=["A) metan", "B) propan-butan", "C) suyuq uglevodorodlar aralashmasi",
                    "D) etan", "E) vodorod", "F) toza oktan"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="etan bor, lekin asosiy emas (≈4 %)"),
                   dict(variant="E", xato="vodorod uy gazi emas"),
                   dict(variant="F", xato="benzin — aralashma, bitta modda emas")],
  yechim=("X: tabiiy gaz ≈ 93 % metan (A). Y: ballonlarda C₃H₈+C₄H₁₀ (B). "
          "Z: benzin — C₅–C₁₀ atrofidagi suyuq alkanlar aralashmasi (C)."),
  parametrlar=dict(arch="yoqilgi_ssenariy"))

# ---------- O1 ----------
check("o36", 0.2*16, 3.2)
check("o37", 14*5+2, 72)
check("o38", 2.24/22.4*2, 0.2)
check("o39", 8.8/44*4*18, 14.4)
check("o40", 11.2/22.4*30, 15)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,2 mol metanning massasini (g) toping. (M(CH₄)=16)",
      javob="3,2", yechim="m = 0,2·16 = 3,2 g.",
      parametrlar=dict(arch="metan_massa_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Pentanning (C₅H₁₂) molyar massasini (g/mol) toping.",
      javob="72", yechim="M = 12·5 + 12 = 72 g/mol.",
      parametrlar=dict(arch="pentan_m_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="C₂H₆ + 7/2O₂ → 2CO₂ + 3H₂O. 2,24 L (n.sh.) etan yonganda hosil bo'lgan CO₂ mol "
            "miqdorini toping.",
      javob="0,2", yechim="n(C₂H₆) = 0,1 → n(CO₂) = 0,2 mol.",
      parametrlar=dict(arch="etan_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="8,8 g propan to'liq yonganda hosil bo'lgan suvning massasini (g) toping. "
            "(M: C₃H₈=44, H₂O=18)",
      javob="14,4", yechim="n = 0,2 → n(H₂O) = 0,8 mol → m = 14,4 g.",
      parametrlar=dict(arch="propan_suv_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="11,2 L (n.sh.) etanning massasini (g) toping. (M(C₂H₆)=30)",
      javob="15", yechim="n = 0,5 mol → m = 15 g.",
      parametrlar=dict(arch="etan_massa_o1")),
]

# ---------- O2 ----------
check("o41b", 3.2/16, 0.2); check("o41c", 0.2*22.4, 4.48)
O2 = [
 dict(n=41, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("3,2 g metan to'liq yondirildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Yonish reaksiyasining tenglamasini yozing.",
             yechim=["CH₄ + 2O₂ → CO₂ + 2H₂O."], M=4, A=2),
        dict(savol="b) Sarflangan kislorod hajmini (n.sh.) hisoblang.",
             yechim=["n(CH₄) = 0,2 → n(O₂) = 0,4 mol → V = 8,96 L."], M=4, A=3),
        dict(savol="c) Hosil bo'lgan CO₂ hajmini toping.",
             yechim=["n(CO₂) = 0,2 mol → V = 4,48 L."], M=4, A=3),
        dict(savol="d) Nega gaz o'choqlari xonasida havo almashinuvi shart? Izohlang.",
             yechim=["Kislorod kamaysa chala yonish boshlanadi — zaharli CO hosil bo'ladi."], M=3, A=2),
      ],
      rasmiylashtirish="Metan-yonish zanjiri: tenglama → O₂ → CO₂ → xavfsizlik; M15+A10.",
      parametrlar=dict(arch="metan_yonish_zanjir")),
 dict(n=42, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Butlerov nazariyasining ahamiyati tahlil qilinadi. Quyidagilarga MULOHAZA yuritib "
            "javob yozing."),
      bandlar=[
        dict(savol="a) «Xossalar tuzilishga bog'liq» tamoyilini butan va izobutan misolida "
                   "tushuntiring.",
             yechim=["Ikkalasi C₄H₁₀, lekin zanjirlari farqli: n-butan −0,5 °C da, izobutan −11,7 °C da",
                     "qaynaydi — bitta formula, har xil moddalar. Tuzilish — moddaning «pasporti»."], M=13, A=0),
        dict(savol="b) Nega uglerod millionlab birikma hosil qila oladi?",
             yechim=["C atomlari bir-biri bilan mustahkam zanjir, tarmoq va halqalar hosil qiladi — "
                     "4 valentlik va C−C bog'ining puxtaligi tufayli."], M=9, A=0),
        dict(savol="c) Izomeriya hodisasi kim tomonidan nazariy asoslangan?",
             yechim=["A. M. Butlerov tomonidan."], M=3, A=0),
      ],
      rasmiylashtirish="Nazariya-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="butlerov_mulohaza")),
 dict(n=43, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch uglevodorod jadvalda berilgan:\n"
            "[JADVAL] № | Modda | Formula ;; 1 | metan | CH₄ ;; 2 | etan | C₂H₆ ;; 3 | siklopropan | C₃H₆\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Qaysilari bir gomologik qatorga kiradi? Sababini yozing.",
             yechim=["1 va 2 — alkanlar (CₙH₂ₙ₊₂); siklopropan boshqa qator (CₙH₂ₙ)."], M=4, A=3),
        dict(savol="b) 2-modda uchun keyingi gomologning formulasi va nomini yozing.",
             yechim=["C₃H₈ — propan."], M=4, A=2),
        dict(savol="c) 3-modda bilan bir xil MOLEKULYAR formulaga ega ochiq zanjirli sinf vakili "
                   "qaysi sinfdan bo'ladi?",
             yechim=["Alkenlardan (propen C₃H₆) — sinflararo izomeriya."], M=4, A=3),
        dict(savol="d) Uchchala moddaning yonish mahsulotlari qanday?",
             yechim=["Barchasi CO₂ va H₂O beradi (to'liq yonishda)."], M=3, A=2),
      ],
      rasmiylashtirish="Qator-jadval: gomologiya → davomi → izomeriya → yonish; M15+A10.",
      parametrlar=dict(arch="qator_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263103)
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
    d = dict(n=n, tur="Y1", element="III.1", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III1-A", daraja="A", bob=1, bob_nomi="Organik kimyo nazariyasi. Alkanlar",
    manba=("MS spetsifikatsiyasi III.1; 10-sinf darslik alkanlar bo'limlari — savollar yangi "
           "tuzilgan, hayotiy sahnalar (gaz plita, ballon, neft qudug'i, gaz hidi) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★ (Organik kimyo kitobi): soddaroq savollar, rasmli hayotiy "
          "misollar. B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
