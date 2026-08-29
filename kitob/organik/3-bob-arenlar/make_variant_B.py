# -*- coding: utf-8 -*-
"""Organik 3-bob B-varianti: Aromatik uglevodorodlar. Neft, gaz, ko'mir (III.3) — HAQIQIY MS MUHITI ★★★.
Nitrolash/galogenlash, kreking tenglamalari, zanjir hisoblari, ksilol izomerlari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_III3B.json"
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
  "Benzol haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) barcha C–C bog'lari teng uzunlikda;  2) bromli suvni oson rangsizlantiradi;  "
  "3) katalizator ishtirokida Br₂ bilan o'rin olish beradi;  4) yuqori haroratda H₂ biriktira oladi.",
  "1, 3 va 4",
  [("hammasi", "aromatik halqa Br₂ suvi bilan oddiy sharoitda kirishmaydi"),
   ("1 va 2", "2 noto'g'ri; 3-4 to'g'ri"),
   ("faqat 1", "katalitik o'rin olish va gidrogenlash ham bor")],
  "Aromatiklik: teng bog'lar; birikishga «qarshilik», katalitik o'rin olish oson.",
  dict(arch="benzol_fikr_b"))

# 2 (3) — nitrolash
q(3, "yuqori",
  "Benzol nitrolanganda (HNO₃ + H₂SO₄) qanday mahsulot hosil bo'ladi?",
  "nitrobenzol (C₆H₅NO₂) va suv",
  [("anilin darhol", "anilin — nitrobenzolni QAYTARIB olinadi"),
   ("benzol nitrat", "bunday tuz yo'q — o'rin olish boradi"),
   ("fenol", "u boshqa jarayon mahsuloti")],
  "C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O — «badam hidli» sariq suyuqlik.",
  dict(arch="nitrolash"))

# 3 (3) — katalitik bromlash hisob
check("q3", 0.1*157, 15.7)
q(3, "yuqori",
  "C₆H₆ + Br₂ → (FeBr₃) C₆H₅Br + HBr. 0,1 mol benzol to'liq bromlanganda hosil bo'lgan brombenzol "
  "massasini toping. (M(C₆H₅Br)=157)",
  "15,7 g", [("157 g", "1 mol uchun"), ("7,85 g", "yarmi"), ("8,1 g", "bu HBr massasi")],
  "n = 0,1 mol → m = 15,7 g.",
  dict(arch="brombenzol_hisob"))

# 4 (3) — kreking tenglama
q(3, "yuqori",
  "C₁₆H₃₄ krekingida mahsulotlardan biri C₈H₁₈ bo'lsa, ikkinchisi qaysi?",
  "C₈H₁₆ (okten)",
  [("C₈H₁₈ yana", "vodorodlar yig'indisi 36 bo'lib qoladi"),
   ("C₈H₁₄", "H balansi buziladi (34 kerak)"),
   ("CH₄", "uglerod balansi buziladi")],
  "C va H saqlanadi: 16=8+8; 34=18+16 → alkan + alken jufti.",
  dict(arch="kreking_balans"))

# 5 (3) — RASMLI: kolonna (B talqini)
q(3, "yuqori",
  "Rasmdagi rektifikatsion kolonnada fraksiyalar qanday tartibda joylashadi (pastdan yuqoriga)?",
  "mazut → dizel → kerosin → benzin",
  [("benzin → kerosin → dizel → mazut", "teskari: og'irlar pastda"),
   ("aralash holda", "har «tarelka»da o'z fraksiyasi"),
   ("faqat harorat bir xil joyda", "kolonnada harorat gradiyenti bor")],
  "Pastda issiq (og'irlar suyuq), yuqorida salqin (yengillar kondensatlanadi).",
  dict(arch="kolonna_tartib"), fig="column")

# 6 (3)
q(3, "yuqori",
  "Toluol KMnO₄ bilan oksidlanganda nima hosil bo'ladi?",
  "benzoy kislota (C₆H₅COOH)",
  [("benzol", "halqa emas, YON ZANJIR oksidlanadi"),
   ("fenol", "OH halqaga bunda kirmaydi"),
   ("CO₂ va suv", "to'liq yonish emas — yumshoq oksidlanish")],
  "Yon zanjir «kuyadi», halqa qoladi: arenlarni farqlash siri shu.",
  dict(arch="toluol_oksidlanish"))

# 7 (3) — 1-2-3
q(3, "yuqori",
  "Qaysi moddalar BENZOLDAN bir bosqichda olinishi mumkin?\n"
  "1) nitrobenzol;  2) brombenzol;  3) siklogeksan;  4) anilin.",
  "1, 2 va 3",
  [("hammasi", "anilin ikki bosqich (nitrolash + qaytarish)"),
   ("faqat 1", "bromlash va gidrogenlash ham bir bosqich"),
   ("2 va 4", "4 — ikki bosqich")],
  "Nitrolash, katalitik bromlash, gidrogenlash — to'g'ridan-to'g'ri.",
  dict(arch="benzoldan_tanlov"))

# 8 (2)
q(2, "yuqori",
  "Benzolda uglerodning gibridlanishi qanday?",
  "barcha C — sp²",
  [("sp³", "u to'yinganlarda"), ("sp", "u alkinlarda"), ("aralash sp²/sp³", "halqada bir xil")],
  "Tekis halqa: har C da p-orbital umumiy pi-tizimga «ulangan».",
  dict(arch="benzol_sp2"))

# 9 (3) — JADVAL: ksilol izomerlari
q(3, "yuqori",
  "Dimetilbenzol (ksilol, C₈H₁₀) uchun jadvaldagi «?» ni to'ldiring:\n"
  "[JADVAL] Izomer | Metillar holati ;; orto- | ? ;; meta- | ? ;; para- | ?",
  "1,2; 1,3; 1,4",
  [("1,1; 1,2; 1,3", "bitta uglerodda ikki metil — boshqa modda"),
   ("1,2; 1,4; 1,3", "meta — 1,3; para — 1,4"),
   ("1,3; 1,2; 1,4", "orto — qo'shni (1,2)")],
  "Orto — yonma-yon; meta — bittadan keyin; para — qarama-qarshi.",
  dict(arch="ksilol_jadval"))

# 10 (3)
check("q10", 0.2*123, 24.6)
q(3, "yuqori",
  "C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O. 0,2 mol benzol nitrolanganda hosil bo'lgan nitrobenzol massasini "
  "toping. (M(C₆H₅NO₂)=123)",
  "24,6 g", [("123 g", "1 mol uchun"), ("12,3 g", "0,1 mol emas"), ("49,2 g", "ikki baravar")],
  "m = 0,2·123 = 24,6 g.",
  dict(arch="nitrobenzol_hisob"))

# 11 (3) — zanjir hisob
check("q11", 13.44/22.4/3*78, 15.6)
q(3, "yuqori",
  "3C₂H₂ → C₆H₆. 13,44 L (n.sh.) atsetilendan (yo'qotishsiz) olinadigan benzol massasini toping. "
  "(M(C₆H₆)=78)",
  "15,6 g", [("46,8 g", "3 ga bo'lish unutilgan"), ("7,8 g", "hisob xato"), ("78 g", "1 mol uchun")],
  "n(C₂H₂) = 0,6 → n(C₆H₆) = 0,2 mol → m = 15,6 g.",
  dict(arch="trimer_hisob"))

# 12 (2)
q(2, "yuqori",
  "Neftni QAYTA ishlashning birlamchi va ikkilamchi usullari mos ravishda qaysilar?",
  "haydash; kreking va riforming",
  [("kreking; haydash", "teskari"), ("filtrlash; haydash", "filtrlash usul emas"),
   ("yoqish; haydash", "yoqish qayta ishlash emas")],
  "Birlamchi — fizik ajratish; ikkilamchi — kimyoviy o'zgartirish.",
  dict(arch="birlamchi_ikkilamchi"))

# 13 (3)
check("q13", 106, 106)
q(3, "yuqori",
  "Molyar massasi 106 g/mol bo'lgan benzol gomologini aniqlang.",
  "ksilol (C₈H₁₀)", [("toluol", "M = 92"), ("benzol", "M = 78"), ("stirol", "M = 104, gomolog emas")],
  "CₙH₂ₙ₋₆: 12·8 + 10 = 106 → C₈H₁₀.",
  dict(arch="m106"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Xomashyo | Qayta ishlash usuli | Asosiy mahsulot ;; neft | haydash | ? ;; "
  "ko'mir | kokslash | ? ;; tabiiy gaz | konversiya | ?",
  "fraksiyalar; koks; vodorod (sintez-gaz)",
  [("koks; fraksiyalar; vodorod", "birinchi ikkisi almashgan"),
   ("benzin; kul; metan", "kul — mahsulot emas, qoldiq"),
   ("fraksiyalar; smola faqat; CO₂", "koks — asosiy qattiq mahsulot")],
  "Har xomashyoning o'z «texnologik yo'li» bor.",
  dict(arch="xomashyo_jadval"))

# 15 (3)
check("q15", 39/78*3*22.4, 33.6)
q(3, "yuqori",
  "C₆H₆ + 3H₂ → C₆H₁₂. 39 g benzolni to'liq gidrogenlash uchun zarur vodorod hajmini (n.sh.) toping. "
  "(M(C₆H₆)=78)",
  "33,6 L", [("11,2 L", "koeffitsiyent 3"), ("22,4 L", "1 mol H₂"), ("67,2 L", "ikki baravar")],
  "n = 0,5 → n(H₂) = 1,5 mol → V = 33,6 L.",
  dict(arch="benzol_h2_hisob"))

# 16 (2)
q(2, "yuqori",
  "Riforming jarayonining maqsadi nima?",
  "benzinning oktan sonini oshirish (aromatiklashtirish)",
  [("neftni fraksiyalarga bo'lish", "u haydash"), ("gazni suyultirish", "boshqa jarayon"),
   ("mazutni yoqish", "yoqish texnologiya emas")],
  "To'g'ri zanjirlar halqali/aromatik shakllarga o'tadi — yoqilg'i sifati o'sadi.",
  dict(arch="riforming"))

# 17 (3)
check("q17", 10.6/106, 0.1)
q(3, "yuqori",
  "10,6 g ksilol (C₈H₁₀) necha mol bo'ladi?",
  "0,1", [("1", "gramm-mol adashuvi"), ("0,2", "ikki baravar"), ("0,05", "yarmi")],
  "n = 10,6/106 = 0,1 mol.",
  dict(arch="ksilol_mol"))

# 18 (2)
q(2, "yuqori",
  "Stirolning (C₆H₅–CH=CH₂) benzoldan farqli xossasi qaysi?",
  "bromli suvni RANGSIZLANTIRADI — yon zanjirda qo'shbog' bor",
  [("umuman reaksiyaga kirishmaydi", "qo'shbog' faol"), ("gaz holatida", "suyuqlik"),
   ("aromatik emas", "halqasi aromatik, yon zanjiri to'yinmagan")],
  "«Ikki dunyo» molekulasi: halqa + vinil guruh.",
  dict(arch="stirol_farq"))

# 19 (3) — RASMLI: kolonna hisob
q(3, "yuqori",
  "5-savol kolonnasida kerosin fraksiyasi 180–270 °C oralig'ida yig'iladi. 150 °C da qaynaydigan "
  "uglevodorod qaysi fraksiyaga tushadi?",
  "benzin fraksiyasiga (u yuqoriroq «tarelkada»)",
  [("kerosinga", "150 < 180 — kerosin oralig'iga kirmaydi"),
   ("mazutga", "mazut — eng og'ir qoldiq"),
   ("dizelga", "dizel oralig'i yuqoriroq haroratda")],
  "Har fraksiya o'z t-oralig'ini «ushlaydi»; 150 °C — benzin-ligroin zonasi.",
  dict(arch="kolonna_hisob"), fig="column")

# 20 (2)
q(2, "yuqori",
  "Koks gazining asosiy komponentlari qaysilar?",
  "H₂ va CH₄", [("CO₂ va N₂ faqat", "yonuvchi gazlar asosiy"), ("O₂ va O₃", "kislorod pirolizda ajralmaydi"),
                 ("faqat NH₃", "ammiak oz miqdorda")],
  "Koks gazi — qimmatli yoqilg'i va vodorod manbai.",
  dict(arch="koks_gazi"))

# 21 (3)
check("q21", 44.8/22.4/3*78, 52)
q(3, "yuqori",
  "44,8 L (n.sh.) atsetilendan trimerlanish orqali olinadigan benzol massasini toping. (M(C₆H₆)=78)",
  "52 g", [("156 g", "3 ga bo'lish unutilgan"), ("26 g", "hisob xato"), ("78 g", "1 mol uchun")],
  "n = 2 mol → n(C₆H₆) = 2/3 mol → m = 52 g.",
  dict(arch="trimer_katta"))

# 22 (3) — 1-2-3
q(3, "yuqori",
  "Qaysi juftliklar IZOMERLAR?\n"
  "1) o-ksilol va p-ksilol;  2) toluol va benzol;  3) etilbenzol va ksilol;  4) benzol va siklogeksan.",
  "1 va 3",
  [("hammasi", "2 — gomologlar; 4 — formulalari farqli"),
   ("faqat 1", "etilbenzol ham C₈H₁₀"),
   ("2 va 4", "ular izomer emas")],
  "C₈H₁₀: o-/m-/p-ksilol va etilbenzol — to'rt izomer.",
  dict(arch="aren_izomer_tanlov"))

# 23 (3)
check("q23", 500*(0.20+0.25), 225)
q(3, "yuqori",
  "Krekingsiz haydashda neftdan 20 % benzin olinadi. 500 kg neftdan krekingda yana qo'shimcha 25 % "
  "benzin olinsa, JAMI benzin massasini toping.",
  "225 kg", [("100 kg", "faqat birlamchi"), ("125 kg", "faqat kreking ulushi"), ("45 kg", "hisob xato")],
  "m = 500·(0,20 + 0,25) = 225 kg.",
  dict(arch="kreking_unum_hisob"))

# 24 (2)
q(2, "yuqori",
  "Benzolni birinchi bo'lib qaysi olim toshko'mir smolasidan ajratib olgan?",
  "M. Faradey",
  [("A. Butlerov", "u tuzilish nazariyasi asoschisi"), ("D. Mendeleyev", "davriy qonun"),
   ("N. Zelinskiy", "u trimerlanishni amalga oshirgan")],
  "1825-yil: yoritish gazidan; keyin Kekule halqa formulasini taklif qildi.",
  dict(arch="faradey"))

# 25 (3)
q(3, "yuqori",
  "Zanjirdagi X va Y ni aniqlang: C₆H₆ → (X) C₆H₅NO₂ → (Y) C₆H₅NH₂.",
  "X — nitrolash; Y — qaytarish",
  [("X — qaytarish; Y — nitrolash", "teskari"), ("X — bromlash; Y — gidroliz", "mahsulotlar mos emas"),
   ("X — oksidlash; Y — yonish", "anilin yonishdan hosil bo'lmaydi")],
  "Nitrobenzol [H] bilan anilinga qaytariladi (Zinin reaksiyasi) — bo'yoqlar sanoati asosi.",
  dict(arch="anilin_zanjir"))

# 26 (3) — RASMLI: benzol halqa (B)
q(3, "yuqori",
  "Benzol halqasidagi C–C bog' uzunligi 140 pm. Bu qiymat nimadan dalolat beradi? "
  "(C–C 154 pm, C=C 134 pm)",
  "bog'lar yakka va qo'shbog' ORALIG'IDA — «o'rtachalashgan»",
  [("barcha bog'lar yakka", "154 bo'lardi"), ("barcha bog'lar qo'shbog'", "134 bo'lardi"),
   ("o'lchov xatosi", "aromatiklikning bevosita isboti")],
  "140 pm — aromatik delokalizatsiya belgisi: «bir yarim» bog'lar.",
  dict(arch="halqa_140"), fig="benzene")

# 27 (3)
check("q27", 0.5*92, 46)
q(3, "yuqori",
  "0,5 mol toluolning massasini toping. (M(C₇H₈)=92)",
  "46 g", [("92 g", "1 mol uchun"), ("23 g", "chorak"), ("184 g", "2 mol uchun")],
  "m = 0,5·92 = 46 g.",
  dict(arch="toluol_massa"))

# 28 (2) — RASMLI: benzol halqasi tarixi
q(2, "yuqori",
  "Rasmdagi ikki tasvir (Kekule formulasi va doirali halqa) haqida qaysi fikr TO'G'RI?",
  "doirali tasvir elektron taqsimotni aniqroq aks ettiradi",
  [("Kekule formulasi mutlaqo xato", "u tarixiy bosqich, «cheklangan» model"),
   ("ikkalasi har xil moddalar", "bitta benzolning ikki tasviri"),
   ("doira — kislorod belgisi", "elektron «bulut» belgisi")],
  "Kekule almashinuvchi bog'lar deb o'ylagan; zamonaviy model — delokalizatsiya.",
  dict(arch="kekule_vs_doira"), fig="benzene")

# 29 (3)
check("q29", 23.4/78*6*44/44, 1.8)
q(3, "yuqori",
  "23,4 g benzol yonganda hosil bo'lgan CO₂ mol miqdorini toping. (M(C₆H₆)=78)",
  "1,8", [("0,3", "har mol benzol 6 CO₂ beradi"), ("0,6", "hisob xato"), ("3,6", "ikki baravar")],
  "n = 0,3 → n(CO₂) = 1,8 mol.",
  dict(arch="benzol_co2_b"))

# 30 (2)
q(2, "yuqori",
  "Tabiiy gaz konversiyasidan olinadigan «sintez-gaz» nima?",
  "CO va H₂ aralashmasi",
  [("CO₂ va N₂", "ular sintezga yaroqsiz"), ("CH₄ va O₂", "bu xomashyo, mahsulot emas"),
   ("faqat vodorod", "CO ham bor")],
  "Sintez-gazdan metanol, ammiak va sun'iy yoqilg'ilar olinadi.",
  dict(arch="sintez_gaz"))

# 31 (3)
check("q31", 0.2*104, 20.8)
q(3, "yuqori",
  "0,2 mol stirolning massasini toping. (M(C₈H₈)=104)",
  "20,8 g", [("104 g", "1 mol uchun"), ("10,4 g", "0,1 mol emas"), ("41,6 g", "ikki baravar")],
  "m = 0,2·104 = 20,8 g.",
  dict(arch="stirol_massa"))

# 32 (3) — RASMLI: halqa xulosa
q(3, "yuqori",
  "Benzol halqasi tasviri asosida: nega benzol KMnO₄ ning suvdagi eritmasini (sovuqda) "
  "rangsizlantirmaydi?",
  "delokalizatsiyalangan pi-tizim alohida qo'shbog'day «ochiq» emas",
  [("molekulada pi-elektron yo'q", "bor — lekin umumiy bulutda"),
   ("KMnO₄ organikaga umuman ta'sir qilmaydi", "alkenlarni oksidlaydi-ku"),
   ("benzol suvda erimagani uchun faqat", "stirol ham erimaydi, lekin rangsizlantiradi")],
  "Aromatik barqarorlik — halqa oksidlanish va birikishga «qarshilik» ko'rsatadi.",
  dict(arch="halqa_kmno4"), fig="benzene")

# ---------- Y2: uch suyuqlik ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.3",
  ichki_pasport=[dict(n=33, element="III.3", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="III.3", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="III.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch rangsiz suyuqlik tekshirildi: X — bromli suvni ham, KMnO₄ ni ham "
               "rangsizlantirmadi, M = 78; Y — bromli suvni rangsizlantirdi, M = 104; Z — KMnO₄ bilan "
               "qizdirilganda benzoy kislota berdi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X suyuqlik qaysi?",
    "34. Y suyuqlik qaysi?",
    "35. Z suyuqlik qaysi?"],
  javoblar_royxati=["A) benzol", "B) stirol", "C) toluol", "D) geksan", "E) ksilol", "F) siklogeksan"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="geksan M = 86"),
                   dict(variant="E", xato="ksilol M = 106 va ikki kislota beradi"),
                   dict(variant="F", xato="siklogeksan oksidlanishda benzoy kislota bermaydi")],
  yechim=("X: M=78, ikkala sinovga «jim» — benzol (A). Y: M=104, qo'shbog'li — stirol (B). "
          "Z: yon zanjiri oksidlanadi — toluol (C)."),
  parametrlar=dict(arch="uch_suyuqlik_ssenariy"))

# ---------- O1 (Spectrum uslubi) ----------
check("o36a", 6.72/22.4/3, 0.1); check("o36b", 0.1*78, 7.8)
check("o37", 0.2*157, 31.4)
check("o38", 12.8/64*22.4/22.4/3*78, 5.2)
check("o39", 800*0.45, 360)
check("o40a", 9.2/92, 0.1); check("o40b", 0.1*122, 12.2)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="6,72 L (n.sh.) atsetilen trimerlanishidan olingan benzol massasini (g) toping. "
            "(M(C₆H₆)=78)",
      javob="7,8", yechim="n = 0,3 → benzol 0,1 mol → 7,8 g.",
      parametrlar=dict(arch="trimer_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="15,6 g benzol katalizator ishtirokida to'liq bromlandi (o'rin olish). Hosil bo'lgan "
            "brombenzol massasini (g) toping. (M: C₆H₆=78, C₆H₅Br=157)",
      javob="31,4", yechim="n = 0,2 mol → m = 0,2·157 = 31,4 g.",
      parametrlar=dict(arch="bromlash_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi zanjir bo'yicha 12,8 g kalsiy karbiddan (yo'qotishsiz) olinadigan benzol "
            "massasini (g) toping. (M: CaC₂=64, C₆H₆=78)",
      javob="5,2", yechim="n(CaC₂) = 0,2 → C₂H₂ 0,2 → C₆H₆ 0,2/3 mol → m = 5,2 g.",
      parametrlar=dict(arch="sxema_karbid_benzol"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Zavod 800 t neftni qayta ishlab, undan 45 % «yorug'» mahsulotlar (benzin+kerosin+dizel) "
            "oldi. Ularning jami massasini (t) toping.",
      javob="360", yechim="m = 800·0,45 = 360 t.",
      parametrlar=dict(arch="zavod_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="9,2 g toluol KMnO₄ bilan to'liq oksidlanib benzoy kislota berdi. Kislota massasini (g) "
            "toping. (M: C₇H₈=92, C₆H₅COOH=122)",
      javob="12,2", yechim="n = 0,1 mol → m = 0,1·122 = 12,2 g.",
      parametrlar=dict(arch="benzoy_zanjir")),
]

# ---------- O2 ----------
check("o41b", 31.2/78, 0.4); check("o41c", 0.4*123, 49.2)
check("o41d", 49.2*0.85, 41.82)
O2 = [
 dict(n=41, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Zavodda 31,2 kg benzol nitrolanib nitrobenzol olindi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing va turini ayting.",
             yechim=["C₆H₆ + HNO₃ → (H₂SO₄) C₆H₅NO₂ + H₂O — o'rin olish (nitrolash)."], M=4, A=2),
        dict(savol="b) Benzol mol miqdorini toping. (M=78)",
             yechim=["n = 31,2/78 = 0,4 kmol."], M=4, A=3),
        dict(savol="c) Nazariy nitrobenzol massasini hisoblang. (M=123)",
             yechim=["m = 0,4·123 = 49,2 kg."], M=4, A=3),
        dict(savol="d) Unum 85 % bo'lsa, amaldagi massani toping.",
             yechim=["m = 49,2·0,85 ≈ 41,8 kg."], M=3, A=2),
      ],
      rasmiylashtirish="Nitrolash-zanjir: tenglama → mol → nazariy → unum; M15+A10.",
      parametrlar=dict(arch="nitrolash_zanjir_o2")),
 dict(n=42, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Aromatiklik «siri» tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Benzol formal jihatdan «uch qo'shbog'li» bo'lsa-da, nega alkenlarga xos "
                   "birikish reaksiyalariga qiyin kirishadi?",
             yechim=["6 pi-elektron alohida bog'larda emas — halqa bo'ylab delokalizatsiyalangan.",
                     "Bu holat energetik juda qulay: uni buzish «qimmat», shu bois halqa o'zini saqlaydi."], M=13, A=0),
        dict(savol="b) Benzolning o'rin olishga moyilligini shu asosda tushuntiring.",
             yechim=["O'rin olishda aromatik tizim SAQLANIB qoladi — energetik jihatdan «arzon» yo'l."], M=9, A=0),
        dict(savol="c) Aromatik halqani buzadigan bitta jarayonni ayting.",
             yechim=["Katalitik gidrogenlash (C₆H₆ + 3H₂ → C₆H₁₂) yoki yonish."], M=3, A=0),
      ],
      rasmiylashtirish="Aromatiklik-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="aromatiklik_mulohaza")),
 dict(n=43, tur="O2", element="III.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Noma'lum aromatik uglevodorod X: vodorodga nisbatan zichligi 46; KMnO₄ bilan "
            "oksidlanganda BITTA monokarbon kislota beradi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X ning molyar massasini toping.",
             yechim=["M = 46·2 = 92 g/mol."], M=4, A=2),
        dict(savol="b) X ning formulasi va nomini aniqlang.",
             yechim=["CₙH₂ₙ₋₆ = 92 → n = 7 → C₇H₈ — toluol."], M=4, A=3),
        dict(savol="c) Nega oksidlanish mahsuloti aynan benzoy kislota?",
             yechim=["Bitta yon zanjir (CH₃) COOH gacha oksidlanadi, halqa saqlanadi."], M=4, A=3),
        dict(savol="d) X ning nitrolanish mahsulotini yozing (asosiy).",
             yechim=["o- va p-nitrotoluol (metil guruh o'rin olishni shu holatlarga yo'naltiradi)."], M=3, A=2),
      ],
      rasmiylashtirish="X-aren detektivi: M → formula → oksidlanish → nitrolash; M15+A10.",
      parametrlar=dict(arch="aren_detektiv_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263305)
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
    d = dict(n=n, tur="Y1", element="III.3", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III3-B", daraja="B", bob=3, bob_nomi="Aromatik uglevodorodlar. Neft, gaz, ko'mir",
    manba=("Tongotarov/DTM arxetiplari (nitrolash, kreking balansi, trimer hisoblari, ksilol "
           "izomerlari) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS "
           "spetsifikatsiyasi III.3"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★ (Organik kimyo kitobi)."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
