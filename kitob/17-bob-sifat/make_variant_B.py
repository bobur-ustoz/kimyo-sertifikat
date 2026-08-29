# -*- coding: utf-8 -*-
"""17-bob B-varianti: Sifat reaksiyalari (IV.2) — HAQIQIY MS MUHITI ★★★.
Ion-detektiv masalalar, aralash eritmalar, cho'kma hisoblari, tahlil tartibi tuzoqlari.
Laboratoriya banki arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_IV2B.json"
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
  "AgNO₃ eritmasi bilan CHO'KMA beradigan ionlarni tanlang:\n"
  "1) Cl⁻;  2) NO₃⁻;  3) PO₄³⁻;  4) Br⁻;  5) K⁺.",
  "1, 3 va 4",
  [("1, 2 va 4", "barcha nitratlar eriydi — cho'kma yo'q"),
   ("faqat 1", "fosfat (sariq) va bromid (sarg'ish) ham cho'kadi"),
   ("hammasi", "NO₃⁻ va K⁺ cho'kma bermaydi")],
  "AgCl oq, AgBr sarg'ish, Ag₃PO₄ sariq; nitrat va kaliy — cho'kmasiz.",
  dict(arch="ag_chokma_tanlov"))

# 2 (3)
check("q2", 11.9/119*188, 18.8)
q(3, "yuqori",
  "11,9 g kaliy bromid eritmasiga ortiqcha AgNO₃ qo'shildi. Cho'kma massasini toping. "
  "(M: KBr=119, AgBr=188)",
  "18,8 g", [("11,9 g", "cho'kma — AgBr"), ("188 g", "1 mol uchun"), ("9,4 g", "yarmi")],
  "n = 0,1 mol → m(AgBr) = 18,8 g (sarg'ish cho'kma).",
  dict(arch="agbr_hisob"))

# 3 (3)
q(3, "yuqori",
  "Fe²⁺ va Fe³⁺ ionlarini ishqor yordamida qanday FARQLASH mumkin?",
  "Fe²⁺ — oqish-yashil cho'kma (havoda qo'ng'irlashadi); Fe³⁺ — darhol qo'ng'ir",
  [("ikkalasi ham oq cho'kma beradi", "ranglar keskin farqli"),
   ("Fe²⁺ cho'kma bermaydi", "Fe(OH)₂ cho'kadi"),
   ("Fe³⁺ ko'k cho'kma beradi", "ko'k — mis")],
  "Fe(OH)₂ oqish-yashil → havoda Fe(OH)₃ ga o'tib qo'ng'irlashadi; Fe(OH)₃ darhol qo'ng'ir.",
  dict(arch="fe2_fe3_farq"))

# 4 (3)
check("q4", 0.15*233, 34.95)
q(3, "yuqori",
  "Eritmada 0,15 mol sulfat ioni bor. Ortiqcha bariy nitrat qo'shilganda hosil bo'ladigan cho'kma "
  "massasini toping. (M(BaSO₄)=233)",
  "34,95 g", [("23,3 g", "0,1 mol emas"), ("46,6 g", "0,2 mol emas"), ("17,5 g", "yarmi")],
  "m = 0,15·233 = 34,95 g.",
  dict(arch="baso4_hisob_b"))

# 5 (3) — RASMLI: titr egri
q(3, "yuqori",
  "Rasmda xlorid eritmasiga AgNO₃ qo'shilishida cho'kma massasi grafigi berilgan. Grafikning "
  "SINISH nuqtasi nimani bildiradi?",
  "barcha xlorid cho'ktirilib bo'lganini (ekvivalent nuqta)",
  [("reaksiya endi boshlanganini", "boshlanish — koordinata boshi"),
   ("cho'kma eriy boshlaganini", "AgCl ortiqcha reagentda erimaydi"),
   ("haroratning ko'tarilganini", "grafik massa haqida")],
  "Sinishgacha har tomchi cho'kma beradi; keyin Cl⁻ qolmagan — chiziq gorizontal.",
  dict(arch="titr_egri_oqish"), fig="titr_curve")

# 6 (3)
q(3, "yuqori",
  "Nima uchun sulfatni tekshirishda BaCl₂ dan OLDIN eritmaga HCl qo'shiladi?",
  "karbonat/sulfit ham Ba²⁺ bilan oq cho'kma beradi — ularni yo'qotish uchun",
  [("reaksiyani tezlashtirish uchun", "tezlik emas, tanlovchanlik muhim"),
   ("cho'kmani rangli qilish uchun", "BaSO₄ baribir oq"),
   ("shart emas", "aks holda «soxta» oq cho'kma chalg'itadi")],
  "HCl da BaCO₃/BaSO₃ erib ketadi; BaSO₄ esa erimaydi — «haqiqiy» sulfat belgisi qoladi.",
  dict(arch="hcl_oldin_sabab"))

# 7 (3) — 1-2-3: gaz tanish
q(3, "yuqori",
  "Gaz va uning sinovi TO'G'RI juftlangan qatorlarni tanlang:\n"
  "1) CO₂ — ohakli suvni loyqalatadi;  2) NH₃ — nam lakmusni qizartiradi;  "
  "3) H₂ — «pop» tovush;  4) O₂ — cho'g'ni alangalatadi.",
  "1, 3 va 4",
  [("hammasi", "NH₃ lakmusni KO'KARTIRADI"), ("1 va 2", "2 xato, 3-4 to'g'ri"),
   ("faqat 1", "3 va 4 ham to'g'ri")],
  "NH₃ — ishqoriy gaz: lakmus ko'karadi; qolgan juftliklar to'g'ri.",
  dict(arch="gaz_juft_tanlov"))

# 8 (2)
q(2, "yuqori",
  "Alanga testida mis birikmalari qanday rang beradi?",
  "yashil-ko'kimtir", [("sariq", "sariq — Na"), ("qirmizi", "qirmizi — Sr/Li"),
                        ("binafsha", "binafsha — K")],
  "Cu — yashil alanga: mis simning o'zi ham shu rangni beradi.",
  dict(arch="cu_alanga"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi cho'kmalarni ranglari bilan TO'G'RI moslang:\n"
  "[JADVAL] Cho'kma | Rang ;; a) AgCl | 1) sariq ;; b) Ag₃PO₄ | 2) oq ;; c) CuS | 3) qora",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "AgCl — oq"), ("a—2, b—3, c—1", "fosfat — sariq"),
   ("a—3, b—1, c—2", "sulfid — qora")],
  "AgCl oq; Ag₃PO₄ sariq; CuS qora.",
  dict(arch="chokma_rang_moslash"))

# 10 (3) — teskari
check("q10", 2.24/22.4*106, 10.6)
q(3, "yuqori",
  "Noma'lum miqdordagi soda kislota bilan reaksiyaga kirishganda 2,24 L (n.sh.) gaz ajraldi. "
  "Boshlang'ich Na₂CO₃ massasini toping. (M=106)",
  "10,6 g", [("5,3 g", "0,05 mol emas — 0,1 mol"), ("106 g", "1 mol uchun"), ("21,2 g", "ikki baravar")],
  "n(CO₂) = 0,1 = n(Na₂CO₃) → m = 10,6 g.",
  dict(arch="soda_teskari"))

# 11 (3) — aralash eritma
check("q11a", 14.35/143.5, 0.1); check("q11b", 23.3/233*142, 14.2)
q(3, "yuqori",
  "Eritmada NaCl va Na₂SO₄ aralash holda bor. AgNO₃ ortiqchasi 14,35 g, alohida namunada BaCl₂ "
  "ortiqchasi 23,3 g cho'kma berdi. Eritmadagi Na₂SO₄ massasini toping. (M: AgCl=143,5, BaSO₄=233, "
  "Na₂SO₄=142)",
  "14,2 g", [("5,85 g", "bu NaCl massasi"), ("23,3 g", "bu cho'kma massasi"), ("28,4 g", "0,2 mol emas")],
  "n(BaSO₄) = 0,1 → n(Na₂SO₄) = 0,1 mol → m = 14,2 g.",
  dict(arch="aralash_eritma_hisob"))

# 12 (2)
q(2, "yuqori",
  "Xlor gazini boshqa gazlardan qaysi belgisi ajratib turadi?",
  "sariq-yashil rangi va nam rangli qog'ozni oqartirishi",
  [("rangsizligi", "Cl₂ rangli"), ("«pop» tovushi", "bu H₂"), ("hidsizligi", "o'tkir hidli")],
  "Cl₂ — rangi ko'rinadigan kam sonli gazlardan; oqartirish — HClO ishi.",
  dict(arch="cl2_tanish"))

# 13 (3)
q(3, "yuqori",
  "Nitrat ionini aniqlashning klassik sinovi qanday?",
  "mis va konsentrlangan H₂SO₄ qo'shib qizdirilganda qo'ng'ir gaz (NO₂) chiqadi",
  [("AgNO₃ qo'shish", "nitratlar cho'kmaydi"),
   ("BaCl₂ qo'shish", "Ba(NO₃)₂ eriydi"),
   ("faqat alanga testi", "NO₃⁻ alanga rangi bermaydi")],
  "NO₃⁻ + Cu + H₂SO₄(kons.) → qo'ng'ir NO₂ bug'lari — nitrat «imzosi».",
  dict(arch="no3_sinov"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Kation | Reagent | Kuzatish ;; NH₄⁺ | ishqor, t° | ? ;; Ba²⁺ | H₂SO₄ | ? ;; Ag⁺ | HCl | ?",
  "o'tkir hidli gaz; oq cho'kma; oq cho'kma",
  [("oq cho'kma; gaz; gaz", "ammoniy gaz beradi, qolganlari cho'kma"),
   ("gaz; qora cho'kma; oq cho'kma", "BaSO₄ oq"),
   ("hid yo'q; oq; sariq", "NH₃ hidi o'tkir; AgCl oq")],
  "NH₃↑; BaSO₄↓ oq; AgCl↓ oq.",
  dict(arch="kation_jadval_b"))

# 15 (3)
check("q15", 0.1*419, 41.9)
q(3, "yuqori",
  "Eritmada 0,1 mol fosfat ioni bor. Ortiqcha AgNO₃ dan hosil bo'ladigan sariq cho'kma massasini "
  "toping. (M(Ag₃PO₄)=419)",
  "41,9 g", [("14,35 g", "bu AgCl massasi"), ("419 g", "1 mol uchun"), ("20,95 g", "yarmi")],
  "m = 0,1·419 = 41,9 g.",
  dict(arch="ag3po4_hisob"))

# 16 (2)
q(2, "yuqori",
  "Ishqoriy muhitni ko'rsatadigan eng «ishonchli» indikator o'zgarishi qaysi?",
  "fenolftaleinning pushti bo'lishi",
  [("lakmusning qizarishi", "qizarish — kislota belgisi"),
   ("fenolftaleinning rangsizlanishi", "rangsiz — kislotali/neytralda"),
   ("eritmaning loyqalanishi", "indikator emas")],
  "Pushti fenolftalein — OH⁻ ortiqchaligining yorqin belgisi.",
  dict(arch="indikator_ishqor"))

# 17 (3) — 1-2-3: bitta reagent
q(3, "yuqori",
  "BITTA NaOH eritmasi yordamida qaysi eritma juftlarini farqlash mumkin?\n"
  "1) CuSO₄ va FeCl₃;  2) NaCl va KCl;  3) NH₄Cl va NaCl;  4) MgCl₂ va BaCl₂.",
  "1, 3 va 4",
  [("hammasi", "NaCl/KCl ga ishqor ta'sir bermaydi — alanga kerak"),
   ("faqat 1", "3 (hid) va 4 (cho'kma bor/yo'q) ham farqlanadi"),
   ("2 va 3", "2 farqlanmaydi")],
  "1: ko'k vs qo'ng'ir cho'kma; 3: hid bor/yo'q; 4: Mg(OH)₂↓ bor, Ba(OH)₂ eriydi.",
  dict(arch="bitta_reagent_tanlov"))

# 18 (2)
q(2, "yuqori",
  "Cho'kmaning kislotada ERISH-ERIMASLIGI nima uchun tekshiriladi?",
  "o'xshash cho'kmalarni bir-biridan farqlash uchun",
  [("cho'kmani yo'qotish uchun", "maqsad — qo'shimcha ma'lumot"),
   ("reaksiya unumini oshirish uchun", "unumga aloqasi yo'q"),
   ("shunchaki an'ana", "bu hal qiluvchi sinov")],
  "Masalan: BaSO₄ kislotada erimaydi, BaCO₃ eriydi — ikkala oq cho'kma farqlanadi.",
  dict(arch="kislota_erish_sinov"))

# 19 (3) — RASMLI: titr egri hisob
check("q19", 0.05*143.5, 7.175, tol=0.01)
q(3, "yuqori",
  "5-savol grafigida plato 7,175 g da boshlangan. Eritmada dastlab necha mol xlorid ioni bo'lgan? "
  "(M(AgCl)=143,5)",
  "0,05", [("0,1", "7,175/143,5 = 0,05"), ("0,5", "nol adashgan"), ("0,025", "yarmi emas")],
  "n(Cl⁻) = n(AgCl) = 7,175/143,5 = 0,05 mol.",
  dict(arch="titr_egri_hisob"), fig="titr_curve")

# 20 (2)
q(2, "yuqori",
  "Nima uchun sifat tahlilida DISTILLANGAN suv ishlatiladi?",
  "vodoprovod suvidagi ionlar (Cl⁻, Ca²⁺...) natijani buzadi",
  [("distillangan suv arzonroq", "aksincha, qimmatroq"),
   ("u tezroq eritadi", "erish tezligi deyarli bir xil"),
   ("farqi yo'q", "krandagi suv «soxta» cho'kmalar beradi")],
  "Krandagi suvning o'zida xlorid bor — AgNO₃ darhol «yolg'on» cho'kma beradi.",
  dict(arch="dist_suv_sabab"))

# 21 (3)
check("q21", 5.35/53.5*22.4, 2.24)
q(3, "yuqori",
  "5,35 g ammoniy xlorid ishqor bilan qizdirildi. Ajralgan gaz hajmini (n.sh.) toping. (M(NH₄Cl)=53,5)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("1,12 L", "yarmi"), ("4,48 L", "ikki baravar")],
  "n = 0,1 mol → V(NH₃) = 2,24 L.",
  dict(arch="nh4cl_hisob_b"))

# 22 (3) — 1-2-3: rangli eritmalar
q(3, "yuqori",
  "Qaysi eritmalar RANGLI bo'ladi?\n"
  "1) CuSO₄;  2) NaCl;  3) FeCl₃;  4) K₂SO₄;  5) FeSO₄.",
  "1, 3 va 5",
  [("1 va 3", "FeSO₄ ham och yashil"), ("hammasi", "Na⁺, K⁺ tuzlari rangsiz"),
   ("2 va 4", "aksincha — ular rangsiz")],
  "Ko'k (Cu²⁺), sarg'ish (Fe³⁺), och yashil (Fe²⁺); ishqoriy metall tuzlari rangsiz.",
  dict(arch="rangli_tanlov"))

# 23 (3) — aralashma
check("q23a", 1.12/22.4*106, 5.3); check("q23b", 15-5.3, 9.7)
q(3, "yuqori",
  "Na₂CO₃ va NaCl dan iborat 15 g aralashmaga ortiqcha kislota qo'shilganda 1,12 L (n.sh.) gaz "
  "ajraldi. Aralashmadagi NaCl massasini toping. (M(Na₂CO₃)=106)",
  "9,7 g", [("5,3 g", "bu soda massasi"), ("15 g", "soda ham bor edi"), ("2,2 g", "hisob xato")],
  "n(CO₂) = 0,05 → m(Na₂CO₃) = 5,3 g → m(NaCl) = 15 − 5,3 = 9,7 g.",
  dict(arch="aralashma_hisob_b"))

# 24 (2)
q(2, "yuqori",
  "Yorug'lik ta'sirida qorayadigan kumush tuzlarining bu xossasi qayerda qo'llanilgan?",
  "klassik (plyonkali) fotografiyada",
  [("elektronikada", "u yerda kremniy asosiy"), ("o'g'itlarda", "kumush o'g'it emas"),
   ("yoqilg'ida", "kumush yonilg'i emas")],
  "AgBr li emulsiya yorug'likda parchalanadi — tasvir shu tarzda «yozilgan».",
  dict(arch="foto_qollash"))

# 25 (3)
q(3, "yuqori",
  "Eritmada BIR VAQTDA Ba²⁺ va Ag⁺ borligini qanday ketma-ketlik bilan isbotlash to'g'ri?",
  "avval HCl (AgCl↓ oq) → filtrlab, so'ng H₂SO₄ (BaSO₄↓ oq)",
  [("avval H₂SO₄, keyin HCl", "Ag₂SO₄ ham qisman cho'kib chalg'itadi"),
   ("ikkala reagentni birga quyish", "cho'kmalar aralashib ketadi"),
   ("faqat alanga testi", "alanga Ag⁺ ni ko'rsatmaydi")],
  "Ketma-ketlik va oraliq filtrlash — ionlarni «birma-bir» ajratish tamoyili.",
  dict(arch="ketma_ketlik"))

# 26 (3) — RASMLI: AgX ustunlar
q(3, "yuqori",
  "Diagrammada 0,1 mol AgCl, AgBr va AgI cho'kmalarining massalari berilgan. Eng og'ir cho'kma "
  "qaysi va nima uchun?",
  "AgI — yod atomining massasi eng katta",
  [("AgCl — xlor faol", "faollik massaga aloqasiz"),
   ("AgBr — o'rtacha barqaror", "og'irlik galogen massasidan"),
   ("hammasi teng", "ustunlar farqli: 14,35; 18,8; 23,5 g")],
  "M(I) > M(Br) > M(Cl) → bir xil mol miqdorda AgI eng og'ir.",
  dict(arch="bar_agx_oqish"), fig="bar_agx")

# 27 (3)
check("q27", 0.1*96, 9.6)
q(3, "yuqori",
  "Eritmadagi 0,1 mol Cu²⁺ vodorod sulfid bilan to'liq cho'ktirildi. Qora cho'kma massasini toping. "
  "(M(CuS)=96)",
  "9,6 g", [("96 g", "1 mol uchun"), ("4,8 g", "yarmi"), ("19,2 g", "ikki baravar")],
  "Cu²⁺ + S²⁻ → CuS↓: m = 9,6 g.",
  dict(arch="cus_hisob"))

# 28 (2) — RASMLI: cho'kma panel (B talqini)
q(2, "yuqori",
  "Cho'kmalar panelidagi 2-probirka (ko'k cho'kma) qaysi ionlar uchrashganda hosil bo'lgan?",
  "Cu²⁺ va OH⁻", [("Fe³⁺ va OH⁻", "u qo'ng'ir beradi"), ("Ag⁺ va Cl⁻", "u oq"),
                   ("Cu²⁺ va S²⁻", "u qora (CuS)")],
  "Ko'k Cu(OH)₂ — mis ionining ishqor bilan uchrashuvi.",
  dict(arch="chokma_panel_b"), fig="precip_panel")

# 29 (3)
check("q29", 0.05*235, 11.75)
q(3, "yuqori",
  "Eritmada 0,05 mol yodid ioni bor. Ortiqcha AgNO₃ dan hosil bo'ladigan cho'kma massasini toping. "
  "(M(AgI)=235)",
  "11,75 g", [("235 g", "1 mol uchun"), ("23,5 g", "0,1 mol emas"), ("5,9 g", "yarmi")],
  "m(AgI) = 0,05·235 = 11,75 g (sariq cho'kma).",
  dict(arch="agi_hisob"))

# 30 (2)
q(2, "yuqori",
  "Sifat tahlilida reagentni TOMCHILAB qo'shish nima uchun muhim?",
  "ortiqcha reagent keyingi sinovlarga xalaqit berishi mumkin",
  [("reagentni tejash uchun faqat", "asosiy sabab — tahlil tozaligi"),
   ("chiroyli ko'rinish uchun", "estetika emas"),
   ("farqi yo'q", "«quyib yuborish» tahlilni buzadi")],
  "Oz-ozdan qo'shib, o'zgarish kuzatiladi — nazorat qo'ldan boy berilmaydi.",
  dict(arch="tomchilab_sabab"))

# 31 (3)
check("q31", 0.2*107, 21.4)
q(3, "yuqori",
  "Eritmadagi 0,2 mol Fe³⁺ ortiqcha ishqor bilan cho'ktirildi. Cho'kma massasini toping. "
  "(M(Fe(OH)₃)=107)",
  "21,4 g", [("10,7 g", "0,1 mol emas"), ("107 g", "1 mol uchun"), ("42,8 g", "ikki baravar")],
  "m = 0,2·107 = 21,4 g — qo'ng'ir cho'kma.",
  dict(arch="feoh3_hisob"))

# 32 (3) — RASMLI: AgX hisob
check("q32", 23.5-14.35, 9.15)
q(3, "yuqori",
  "26-savol diagrammasidan: AgI va AgCl ustunlari orasidagi massa farqini toping.",
  "9,15 g", [("4,7 g", "bu AgI−AgBr farqi"), ("14,35 g", "bu AgCl ning o'zi"), ("23,5 g", "bu AgI ning o'zi")],
  "23,5 − 14,35 = 9,15 g.",
  dict(arch="bar_agx_hisob"), fig="bar_agx")

# ---------- Y2: uch kation ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="IV.2",
  ichki_pasport=[dict(n=33, element="IV.2", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="IV.2", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="IV.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch eritmada bittadan kation bor: X — ishqor bilan qizdirilganda o'tkir hidli gaz "
               "beradi; Y — ishqor bilan qo'ng'ir cho'kma beradi; Z — sulfat kislota bilan oq cho'kma "
               "beradi. Kationlar NH₄⁺, Fe³⁺ va Ba²⁺ ekani ma'lum. 33–35-savollarga A–F ro'yxatidan "
               "javob tanlang."),
  savollar_ichki=[
    "33. X eritmadagi kation qaysi?",
    "34. Y dagi cho'kmaning formulasi qaysi?",
    "35. Z dagi cho'kma haqida qaysi fikr to'g'ri?"],
  javoblar_royxati=["A) NH₄⁺", "B) Fe(OH)₃", "C) kislotalarda erimaydi", "D) Ba²⁺",
                    "E) Fe(OH)₂", "F) kislotada oson eriydi"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="Ba²⁺ — Z eritmada (sulfat bilan cho'kma)"),
                   dict(variant="E", xato="qo'ng'ir cho'kma — Fe(III) gidroksidi"),
                   dict(variant="F", xato="BaSO₄ kislotalarda ERIMAYDI — shu belgisi qimmatli")],
  yechim=("X: NH₄⁺ (NH₃ hidi) — A. Y: Fe³⁺ → Fe(OH)₃ qo'ng'ir — B. "
          "Z: Ba²⁺ → BaSO₄, kislotaga chidamli oq cho'kma — C."),
  parametrlar=dict(arch="kation_detektiv_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36", 28.7/143.5/2*111, 11.1)
check("o37", 0.4/2*160, 32)
check("o38", 5.3/106*22.4, 1.12)
check("o39", 8/80*22.4, 2.24)
check("o40a", 14.35/143.5, 0.1)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="CaCl₂ eritmasiga ortiqcha AgNO₃ qo'shilganda 28,7 g cho'kma tushdi. Boshlang'ich "
            "eritmadagi CaCl₂ massasini (g) toping. (M: AgCl=143,5, CaCl₂=111)",
      javob="11,1", yechim="n(AgCl) = 0,2 → n(CaCl₂) = 0,1 mol → m = 11,1 g.",
      parametrlar=dict(arch="cacl2_teskari_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="FeSO₄ → Fe(OH)₂ → Fe(OH)₃ → Fe₂O₃ zanjiri bo'yicha 0,4 mol temir(II) sulfatdan "
            "(yo'qotishsiz) olingan qizil-qo'ng'ir oksid massasini (g) toping. (M(Fe₂O₃)=160)",
      javob="32", yechim="n(Fe₂O₃) = 0,2 mol → m = 32 g.",
      parametrlar=dict(arch="fe_oksid_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi tekshiruvda noma'lum oq kukun sariq alanga berdi, kislota bilan gaz ajratdi. "
            "5,3 g shu moddadan (Na₂CO₃, M=106) ajraladigan CO₂ hajmini (n.sh., L) toping.",
      javob="1,12", yechim="Kukun — Na₂CO₃: n = 0,05 mol → V = 1,12 L.",
      parametrlar=dict(arch="sxema_detektiv_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="8 g ammoniy nitrat ishqor bilan qizdirildi. Ajralgan ammiak hajmini (n.sh., L) toping. "
            "(M(NH₄NO₃)=80)",
      javob="2,24", yechim="n = 0,1 mol → NH₃ 0,1 mol → V = 2,24 L.",
      parametrlar=dict(arch="nh4no3_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Eritmada Ag⁺ va Ba²⁺ aralash. Ortiqcha NaCl 14,35 g cho'kma berdi. Eritmadagi kumush "
            "ionlari mol miqdorini toping. (M(AgCl)=143,5)",
      javob="0,1", yechim="Cho'kma faqat AgCl (BaCl₂ eriydi): n(Ag⁺) = 14,35/143,5 = 0,1 mol.",
      parametrlar=dict(arch="ag_ba_aralash_zanjir")),
]

# ---------- O2 ----------
check("o41c", 0.1*166, 16.6)
check("o43d", 0.05*233, 11.65)
O2 = [
 dict(n=41, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Oq kristall modda tekshirildi: alanga testi BINAFSHA rang berdi; eritmasiga AgNO₃ "
            "tomizilganda SARIQ cho'kma tushdi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir sinov natijasi qaysi ionni ko'rsatadi?",
             yechim=["Binafsha alanga → K⁺; sariq cho'kma (AgI) → I⁻."], M=4, A=2),
        dict(savol="b) Moddaning formulasini aniqlang.",
             yechim=["KI — kaliy yodid."], M=3, A=2),
        dict(savol="c) 0,1 mol shu moddaning massasini toping. (M(KI)=166)",
             yechim=["m = 16,6 g."], M=4, A=3),
        dict(savol="d) Xulosani tasdiqlovchi yana bitta mustaqil sinov taklif qiling.",
             yechim=["Xlorli suv qo'shish: eritma yod hisobiga qo'ng'irlashadi (Cl₂ + 2KI → I₂ + 2KCl)."], M=4, A=3),
      ],
      rasmiylashtirish="Ion-detektiv: sinovlar → formula → hisob → tasdiq; M15+A10.",
      parametrlar=dict(arch="ion_detektiv_o2")),
 dict(n=42, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Sifat tahlilining mantig'i tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega aralash eritmada ionlar ma'lum KETMA-KETLIKDA aniqlanadi va har "
                   "bosqichda cho'kma filtrlab olinadi? Misol bilan tushuntiring.",
             yechim=["Bir reagent bir nechta ionga «javob berishi» mumkin. Masalan, Ag⁺ ni HCl bilan",
                     "cho'ktirib olinmasa, sulfat sinovida Ag₂SO₄ ham aralashib xulosani buzadi."], M=13, A=0),
        dict(savol="b) «Ortiqcha reagent» qo'shishning maqsadi nima?",
             yechim=["Aniqlanayotgan ionning TO'LIQ cho'kishiga ishonch hosil qilish — miqdoriy hisob "
                     "ham to'g'ri chiqadi."], M=9, A=0),
        dict(savol="c) Sifat tahlili bilan miqdoriy tahlil farqini bir gapda yozing.",
             yechim=["Sifat — «nima bor?», miqdoriy — «qancha bor?» degan savolga javob beradi."], M=3, A=0),
      ],
      rasmiylashtirish="Tahlil-mantiq (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="tahlil_mantiq_o2")),
 dict(n=43, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Eritmada Ba²⁺, Fe³⁺ va NH₄⁺ ionlari ARALASH holda bor deb taxmin qilinadi. Bandlar "
            "ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) NH₄⁺ ni qanday sinov bilan ko'rsatish mumkin? Tenglama yozing.",
             yechim=["Ishqor + qizdirish: NH₄⁺ + OH⁻ → NH₃↑ + H₂O (hid, nam lakmus ko'karadi)."], M=4, A=2),
        dict(savol="b) Fe³⁺ ni qanday ko'rsatish mumkin? Tenglama yozing.",
             yechim=["Ishqor: Fe³⁺ + 3OH⁻ → Fe(OH)₃↓ — qo'ng'ir cho'kma."], M=4, A=2),
        dict(savol="c) Ba²⁺ ni qanday ko'rsatish mumkin? Tenglama yozing.",
             yechim=["Sulfat: Ba²⁺ + SO₄²⁻ → BaSO₄↓ — kislotada erimaydigan oq cho'kma."], M=4, A=3),
        dict(savol="d) Eritmada 0,05 mol Ba²⁺ bo'lsa, cho'kma massasini hisoblang. (M(BaSO₄)=233)",
             yechim=["m = 11,65 g."], M=3, A=3),
      ],
      rasmiylashtirish="Uch ion tahlili: NH₄⁺ → Fe³⁺ → Ba²⁺ → hisob; M15+A10.",
      parametrlar=dict(arch="uch_ion_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261705)
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
    d = dict(n=n, tur="Y1", element="IV.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-IV2-B", daraja="B", bob=17, bob_nomi="Sifat reaksiyalari",
    manba=("Laboratoriya banki arxetiplari (ion-detektiv, aralash eritmalar, tahlil tartibi) va "
           "Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS spetsifikatsiyasi IV.2"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: titrlash egri chizig'i, AgX qatorlari, aralash "
          "eritma hisoblari, tahlil ketma-ketligi."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="IV.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
