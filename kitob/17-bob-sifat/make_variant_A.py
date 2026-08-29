# -*- coding: utf-8 -*-
"""17-bob A-varianti: Sifat reaksiyalari (IV.2) — O'RGATUVCHI ★★.
Hayotiy sahnalar: yodlangan tuz, mineral suv etiketkasi, rassom bo'yoqlari, akvarium test-to'plami."""
import json, random

OUT = "mavzu_IV2A.json"
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
  "SIFAT reaksiyasi deb qanday reaksiyaga aytiladi?",
  "muayyan ion yoki moddani ANIQLAB beradigan xarakterli reaksiyaga",
  [("juda tez boradigan reaksiyaga", "tezlik emas, tanish belgisi muhim"),
   ("issiqlik ajratadigan reaksiyaga", "issiqlik ko'p reaksiyalarda bor"),
   ("faqat rangli reaksiyaga", "belgi gaz yoki cho'kma ham bo'lishi mumkin")],
  "Sifat reaksiya «imzo» beradi: rang, cho'kma, gaz, hid — modda taniladi.",
  dict(arch="sifat_tarif"))

# 2 (2)
q(2, "quyi",
  "Xlorid ionini (Cl⁻) aniqlash uchun qaysi reagent ishlatiladi?",
  "AgNO₃ — oq suzmasimon cho'kma tushadi",
  [("BaCl₂", "u sulfatga reagent"), ("NaOH", "ishqor xloridga cho'kma bermaydi"),
   ("lakmus", "indikator ionni aniqlamaydi")],
  "Ag⁺ + Cl⁻ → AgCl↓ (oq, yorug'likda qorayadi).",
  dict(arch="cl_reagent"))

# 3 (2)
q(2, "o'rta",
  "Sulfat ionini (SO₄²⁻) qaysi reagent bilan aniqlash mumkin?",
  "BaCl₂ — kislotada erimaydigan oq cho'kma",
  [("AgNO₃", "Ag₂SO₄ yaxshi ko'rinmaydi — asosiy reagent bariy"),
   ("fenolftalein", "indikator cho'kma bermaydi"),
   ("mis", "metall sulfat ioni bilan cho'kma bermaydi")],
  "Ba²⁺ + SO₄²⁻ → BaSO₄↓ — og'ir oq cho'kma, HNO₃ da ham erimaydi.",
  dict(arch="so4_reagent"))

# 4 (2) — SAHNA: yodlangan tuz
q(2, "o'rta",
  "Rasmda «yodlangan tuz» qadog'i. Bunday tuzga yod birikmalari nima maqsadda qo'shiladi?",
  "qalqonsimon bez uchun zarur yod tanqisligini to'ldirish",
  [("ta'mni kuchaytirish", "yod miqdori ta'mga sezilmaydi"),
   ("tuzni oqartirish", "rang uchun emas"),
   ("saqlash muddatini uzaytirish", "konservant emas")],
  "KIO₃/KI qo'shimchasi — yod yetishmovchiligi (buqoq) profilaktikasi.",
  dict(arch="yodli_tuz_sahna"), fig="iodized")

# 5 (2)
q(2, "o'rta",
  "Karbonat ionini (CO₃²⁻) qanday aniqlash mumkin?",
  "kislota qo'shilganda «vishillab» CO₂ ajralishi orqali",
  [("ishqor qo'shib", "ko'zga ko'rinadigan belgi yo'q"),
   ("suv qo'shib", "erish belgisiz"),
   ("qizdirib faqat", "hamma karbonat ham parchalanavermaydi")],
  "CO₃²⁻ + 2H⁺ → H₂O + CO₂↑; gaz ohakli suvni loyqalatadi.",
  dict(arch="co3_aniqlash"))

# 6 (2)
q(2, "o'rta",
  "Mis(II) ionining (Cu²⁺) «vizit kartasi» qanday?",
  "eritmasi ko'k; ishqor bilan ko'k cho'kma beradi",
  [("eritmasi yashil; qora cho'kma", "yashil — Fe²⁺ ga yaqin"),
   ("rangsiz eritma", "Cu²⁺ har doim rangli"),
   ("qizil cho'kma", "qizil cho'kma boshqa ionlarga xos emas bu holda")],
  "Cu²⁺ + 2OH⁻ → Cu(OH)₂↓ (havorang); qizdirilsa qora CuO.",
  dict(arch="cu_belgi"))

# 7 (2)
q(2, "o'rta",
  "Temir(III) ioniga (Fe³⁺) ishqor ta'sir ettirilganda qanday cho'kma tushadi?",
  "qo'ng'ir-qizg'ish Fe(OH)₃",
  [("oq cho'kma", "oq — Al(OH)₃, BaSO₄ kabi"), ("ko'k cho'kma", "ko'k — mis"),
   ("qora cho'kma", "qora — sulfidlar")],
  "Fe³⁺ + 3OH⁻ → Fe(OH)₃↓ — «zang rangli» cho'kma.",
  dict(arch="fe3_belgi"))

# 8 (2) — SAHNA: mineral suv
q(2, "o'rta",
  "Rasmda mineral suv etiketkasi: unda Ca²⁺, Mg²⁺, HCO₃⁻, SO₄²⁻ miqdorlari yozilgan. Bu "
  "ma'lumotlar qanday aniqlanadi?",
  "laboratoriyada ionlarga sifat va miqdor tahlillari o'tkazib",
  [("ta'mga qarab taxminan", "aniq raqamlar tahlildan keladi"),
   ("suv rangiga qarab", "bu ionlar rangsiz"),
   ("qadoqlash paytida o'ylab yoziladi", "etiketka tahlil natijasi")],
  "Har bir ion o'z reaksiyasi bilan topiladi va miqdori o'lchanadi — analitik kimyo ishi.",
  dict(arch="mineral_suv_sahna"), fig="mineral")

# 9 (2)
q(2, "o'rta",
  "Ammoniy ionini (NH₄⁺) aniqlash usuli qanday?",
  "ishqor qo'shib qizdirilganda o'tkir hidli NH₃ ajraladi",
  [("kislota qo'shilganda gaz chiqadi", "kislota bilan belgi yo'q"),
   ("AgNO₃ bilan cho'kma", "ammoniy kumush bilan xarakterli cho'kma bermaydi"),
   ("alanga qizil bo'ladi", "NH₄⁺ alanga rangi bermaydi")],
  "NH₄⁺ + OH⁻ → NH₃↑ + H₂O: hid va nam lakmusning ko'karishi.",
  dict(arch="nh4_aniqlash"))

# 10 (3)
check("q10", 5.85/58.5*143.5, 14.35)
q(3, "o'rta",
  "5,85 g osh tuzi eritmasiga ortiqcha AgNO₃ qo'shildi. Hosil bo'lgan cho'kma massasini toping. "
  "(M: NaCl=58,5, AgCl=143,5)",
  "14,35 g", [("5,85 g", "cho'kma — AgCl, tuz emas"), ("143,5 g", "1 mol uchun"),
               ("28,7 g", "ikki baravar")],
  "n = 0,1 mol → m(AgCl) = 14,35 g.",
  dict(arch="agcl_hisob"))

# 11 (2)
q(2, "o'rta",
  "Alanga testida bariy tuzlari qanday rang beradi?",
  "sarg'ish-yashil", [("qizil", "qizil — Li, Sr"), ("sariq", "sariq — Na"), ("binafsha", "binafsha — K")],
  "Ba — yashil alanga; Sr — qirmizi; Ca — g'isht-qizil.",
  dict(arch="ba_alanga"))

# 12 (3)
check("q12", 0.2*233, 46.6)
q(3, "o'rta",
  "Eritmada 0,2 mol sulfat ioni bor. Ortiqcha BaCl₂ qo'shilganda hosil bo'ladigan cho'kma massasini "
  "toping. (M(BaSO₄)=233)",
  "46,6 g", [("23,3 g", "0,1 mol emas, 0,2 mol"), ("233 g", "1 mol uchun"), ("11,65 g", "chorak")],
  "m = 0,2·233 = 46,6 g.",
  dict(arch="baso4_hisob_a"))

# 13 (2) — SAHNA: rassom bo'yoqlari
q(2, "o'rta",
  "Rasmda rassom bo'yoqlari: yashil rang — malaxit, ko'k — azurit (mis birikmalari). Bo'yoqlarning "
  "rangi nimadan?",
  "tarkibidagi metall ionlarining o'ziga xos ranglaridan",
  [("qo'shilgan sun'iy bo'yoqlardan", "tabiiy mineral pigmentlar"),
   ("yorug'likning sinishidan faqat", "asosi — moddaning o'z rangi"),
   ("moy tarkibidan", "moy — bog'lovchi, rang bermaydi")],
  "Ko'p pigmentlar — rangli metall birikmalari: mis — yashil-ko'k, temir — qo'ng'ir-qizil.",
  dict(arch="boyoq_sahna"), fig="paints")

# 14 (2)
q(2, "o'rta",
  "Kislorod gazini qanday TANISH mumkin?",
  "cho'g'lanib turgan cho'p alangalanib ketadi",
  [("«pop» tovush beradi", "bu vodorod"), ("ohakli suvni loyqalatadi", "bu CO₂"),
   ("o'tkir hidi bor", "O₂ hidsiz")],
  "O₂ yonishni kuchaytiradi — cho'g' testi.",
  dict(arch="o2_tanish"))

# 15 (2)
q(2, "o'rta",
  "Fosfat ioniga (PO₄³⁻) AgNO₃ ta'sir ettirilganda qanday cho'kma tushadi?",
  "SARIQ Ag₃PO₄", [("oq", "oq — AgCl"), ("qora", "qora — sulfidlar"), ("ko'k", "ko'k — mis birikmalari")],
  "Ag₃PO₄ — sariq cho'kma (nitrat kislotada eriydi).",
  dict(arch="po4_belgi"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Ion | Reagent | Belgi ;; Cl⁻ | AgNO₃ | ? ;; SO₄²⁻ | BaCl₂ | ?",
  "oq cho'kma; oq cho'kma",
  [("sariq cho'kma; gaz", "AgCl oq; BaSO₄ ham oq"), ("gaz; oq cho'kma", "xlorid gaz bermaydi"),
   ("oq cho'kma; qora cho'kma", "BaSO₄ oq")],
  "Ikkalasi ham oq; farqi: AgCl yorug'likda qorayadi, BaSO₄ kislotada erimaydi.",
  dict(arch="ion_belgi_jadval"))

# 17 (2)
q(2, "o'rta",
  "Vodorod gazi qanday taniladi?",
  "yoqilganda «pop» tovush beradi",
  [("cho'g'ni alangalatadi", "bu O₂"), ("nam lakmusni ko'kartiradi", "bu NH₃"),
   ("sariq-yashil rangi bor", "bu Cl₂")],
  "H₂-havo aralashmasi mayda «portlash» bilan yonadi.",
  dict(arch="h2_tanish_a"))

# 18 (2) — SAHNA: akvarium testi
q(2, "o'rta",
  "Rasmda akvarium suvi uchun test-to'plam: tomchi reagent suv namunasida rang o'zgartiradi. "
  "Bu qanday tahlil?",
  "sifat (va yarim miqdoriy) tahlil — ionlar rang orqali aniqlanadi",
  [("mikroskopik tahlil", "mikroskop ishlatilmaydi"),
   ("faqat harorat o'lchash", "rang ion konsentratsiyasini ko'rsatadi"),
   ("suvni tozalash vositasi", "test tozalamaydi, o'lchaydi")],
  "Maishiy test-to'plamlar — sifat reaksiyalarining «cho'ntak» varianti.",
  dict(arch="testkit_sahna"), fig="testkit")

# 19 (3)
check("q19", 0.15*22.4, 3.36)
q(3, "o'rta",
  "0,15 mol soda (Na₂CO₃) ortiqcha xlorid kislota bilan reaksiyaga kirishdi. Ajralgan gaz hajmini "
  "(n.sh.) toping.",
  "3,36 L", [("2,24 L", "0,1 mol emas"), ("22,4 L", "1 mol uchun"), ("6,72 L", "ikki baravar")],
  "n(CO₂) = 0,15 mol → V = 3,36 L.",
  dict(arch="co2_hisob_a"))

# 20 (2)
q(2, "o'rta",
  "Ohakli suvdan CO₂ o'tkazilganda nima kuzatiladi?",
  "eritma oq loyqalanadi (CaCO₃)",
  [("qizil rangga kiradi", "rang o'zgarishi emas, cho'kma"),
   ("gaz pufakchalari chiqadi", "gaz kirityapmiz-ku"),
   ("hech narsa", "loyqalanish — CO₂ ning asosiy sinovi")],
  "Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O — «karbonat ko'zgusi».",
  dict(arch="ohakli_suv_sinov"))

# 21 (2)
q(2, "o'rta",
  "Alanga testini o'tkazish uchun namuna qaysi asbobda alangaga kiritiladi?",
  "toza nixrom (platina) simchada",
  [("temir mixda", "temirning o'zi rang beradi"),
   ("yog'och cho'pda", "yog'och yonib xalaqit qiladi"),
   ("mis simda", "mis o'zi yashil rang beradi!")],
  "Sim avval kislotada tozalanib, rang bermasligi tekshiriladi.",
  dict(arch="alanga_asbob"))

# 22 (2)
q(2, "o'rta",
  "Qaysi ionlar eritmani RANGSIZ qoldiradi?",
  "Na⁺, K⁺, Ca²⁺, Cl⁻, SO₄²⁻",
  [("Cu²⁺, Fe³⁺", "ular rangli"), ("Fe²⁺, Cu²⁺", "yashil va ko'k"),
   ("hamma ionlar rangli", "ko'pchiligi rangsiz")],
  "Rangsiz ionlar alanga testi yoki cho'kma reaksiyalari bilan topiladi.",
  dict(arch="rangsiz_ionlar"))

# 23 (3)
check("q23", 0.1*22.4, 2.24)
q(3, "o'rta",
  "0,1 mol ammoniy xlorid ishqor bilan qizdirildi. Ajralgan gaz hajmini (n.sh.) toping.",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("1,12 L", "yarmi"), ("4,48 L", "ikki baravar")],
  "NH₄Cl + NaOH → NaCl + NH₃↑ + H₂O: n = 0,1 → V = 2,24 L.",
  dict(arch="nh3_hisob_a"))

# 24 (2)
q(2, "o'rta",
  "AgCl cho'kmasining o'ziga xos qo'shimcha belgisi qanday?",
  "yorug'likda asta qorayadi",
  [("qizdirilganda ko'karadi", "bunday emas"), ("suvda erib ketadi", "erimaydi"),
   ("hid chiqaradi", "hidsiz")],
  "2AgCl → (yorug'lik) 2Ag + Cl₂ — fotokimyoviy parchalanish (fotografiya asosi).",
  dict(arch="agcl_yoruglik"))

# 25 (2)
q(2, "o'rta",
  "Sulfid ioni (S²⁻) og'ir metall tuzlari bilan qanday cho'kmalar beradi?",
  "qora (CuS, PbS)",
  [("oq", "sulfidlar odatda to'q rangli"), ("sariq faqat", "CdS sariq, lekin ko'pi qora"),
   ("cho'kma bermaydi", "og'ir metall sulfidlari erimaydi")],
  "Qora dog' — sulfidning klassik belgisi (kumush qorayishi ham shu).",
  dict(arch="s2_belgi"))

# 26 (3) — RASMLI: alanga panel
q(3, "o'rta",
  "Rasmda to'rt alanga rangi berilgan. Qaysi biri NATRIYGA tegishli?",
  "2-alanga (sariq)", [("1-alanga (qirmizi)", "bu litiy/stronsiy"), ("3-alanga (binafsha)", "bu kaliy"),
                        ("4-alanga (yashil)", "bu bariy/mis")],
  "Panel: qizil — Li/Sr; sariq — Na; binafsha — K; yashil — Ba/Cu.",
  dict(arch="alanga_panel_oqish"), fig="flame_panel")

# 27 (3)
check("q27", 0.1*197, 19.7)
q(3, "o'rta",
  "Eritmada 0,1 mol Ba²⁺ ioni bor. Ortiqcha soda qo'shilganda hosil bo'lgan cho'kma massasini "
  "toping. (M(BaCO₃)=197)",
  "19,7 g", [("197 g", "1 mol uchun"), ("9,85 g", "yarmi"), ("23,3 g", "bu BaSO₄ massasi")],
  "Ba²⁺ + CO₃²⁻ → BaCO₃↓: m = 19,7 g.",
  dict(arch="baco3_hisob"))

# 28 (2) — RASMLI: cho'kmalar paneli
q(2, "o'rta",
  "Rasmdagi probirkalar qatorida qaysi cho'kma temir(III) gidroksidga tegishli?",
  "3-probirka (qo'ng'ir)", [("1-probirka (oq)", "oq — AgCl/BaSO₄"), ("2-probirka (ko'k)", "ko'k — Cu(OH)₂"),
                             ("4-probirka (qora)", "qora — CuS")],
  "Cho'kma ranglari: oq, ko'k, qo'ng'ir, qora — «rang lug'ati» yodda bo'lsin.",
  dict(arch="chokma_panel_oqish"), fig="precip_panel")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Xlorid eritmasiga AgNO₃ tomchilab qo'shilmoqda. Cho'kma massasi qanday o'zgaradi? Grafikni "
  "tanlang.",
  "ortib borib, xlorid tugagach o'zgarmay qoladi",
  [("chegarasiz ortadi", "Cl⁻ tugagach cho'kma ko'paymaydi"),
   ("o'zgarmaydi", "cho'kma hosil bo'lyapti-ku"),
   ("ortib, keyin kamayadi", "AgCl ortiqcha reagentda erimaydi")],
  "Ekvivalent nuqtadan keyin qo'shilgan AgNO₃ «bo'sh» ketadi — plato.",
  svg=dict(correct="rise_flat", d1="rise", d2="flat", d3="rise_fall", xlab="V(AgNO₃)", ylab="m(AgCl)"),
  params=dict(arch="chokma_grafik"))

# 30 (2)
q(2, "o'rta",
  "Nitrat ioni (NO₃⁻) haqida qaysi fikr to'g'ri?",
  "oson aniqlanadigan cho'kma reaksiyasi yo'q — maxsus usullar kerak",
  [("AgNO₃ bilan cho'kadi", "barcha nitratlar eriydi"),
   ("BaCl₂ bilan cho'kadi", "Ba(NO₃)₂ ham eriydi"),
   ("ishqor bilan gaz beradi", "bu NH₄⁺ belgisi")],
  "Barcha nitratlar suvda eriydi — NO₃⁻ «qiyin» ion (mis + kons. H₂SO₄ sinovi qo'llanadi).",
  dict(arch="no3_muammo"))

# 31 (3)
check("q31", 0.05*98, 4.9)
q(3, "o'rta",
  "Eritmada 0,05 mol Cu²⁺ bor. Ortiqcha ishqor qo'shilganda hosil bo'lgan cho'kma massasini toping. "
  "(M(Cu(OH)₂)=98)",
  "4,9 g", [("9,8 g", "0,1 mol emas"), ("98 g", "1 mol uchun"), ("2,45 g", "yarmi")],
  "m = 0,05·98 = 4,9 g — havorang cho'kma.",
  dict(arch="cuoh2_hisob_a"))

# 32 (3) — RASMLI: alanga panel davomi
q(3, "o'rta",
  "26-savol panelidan foydalaning: noma'lum tuz alangani BINAFSHA rangga bo'yadi va AgNO₃ bilan "
  "oq cho'kma berdi. Bu qaysi tuz?",
  "KCl", [("NaCl", "sariq alanga bo'lardi"), ("KNO₃", "nitrat AgNO₃ bilan cho'kmaydi"),
           ("BaCl₂", "yashil alanga bo'lardi")],
  "Binafsha → K⁺; oq cho'kma → Cl⁻ ⇒ KCl.",
  dict(arch="alanga_panel_hisob"), fig="flame_panel")

# ---------- Y2: uch eritma ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="IV.2",
  ichki_pasport=[dict(n=33, element="IV.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="IV.2", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="IV.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch probirkada rangsiz eritmalar bor: X — NaCl, Y — Na₂SO₄, Z — Na₂CO₃ (qaysi "
               "birida qaysi eritma borligi noma'lum). Tajribalar o'tkazildi. 33–35-savollarga A–F "
               "ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X ga AgNO₃ tomizilganda oq cho'kma tushdi. X qaysi eritma bo'lishi mumkin?",
    "34. Z ga kislota qo'shilganda gaz ajraldi. Z qaysi eritma?",
    "35. Y ni tasdiqlash uchun qaysi reagent qo'shiladi?"],
  javoblar_royxati=["A) NaCl", "B) Na₂CO₃", "C) BaCl₂", "D) Na₂SO₄", "E) fenolftalein", "F) suv"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="sulfat AgNO₃ bilan xarakterli oq cho'kma bermaydi (asosiy sinov Ba²⁺)"),
                   dict(variant="E", xato="indikator ionni aniq ko'rsatmaydi"),
                   dict(variant="F", xato="suv reagent emas")],
  yechim=("X: Ag⁺ + Cl⁻ → AgCl↓ (A). Z: karbonat kislotada CO₂ beradi (B). "
          "Y (sulfat): BaCl₂ bilan oq cho'kma — tasdiq (C)."),
  parametrlar=dict(arch="uch_eritma_ssenariy"))

# ---------- O1 ----------
check("o36", 0.1*143.5, 14.35)
check("o37", 0.2*233, 46.6)
check("o38", 5.3/106*22.4, 1.12)
check("o39", 0.2*17, 3.4)
check("o40", 0.1*98, 9.8)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="Eritmada 0,1 mol xlorid ioni bor. Ortiqcha AgNO₃ dan hosil bo'ladigan cho'kma massasini "
            "(g) toping. (M(AgCl)=143,5)",
      javob="14,35", yechim="m = 0,1·143,5 = 14,35 g.",
      parametrlar=dict(arch="agcl_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Eritmada 0,2 mol sulfat ioni bor. Ortiqcha BaCl₂ dan hosil bo'ladigan cho'kma massasini "
            "(g) toping. (M(BaSO₄)=233)",
      javob="46,6", yechim="m = 0,2·233 = 46,6 g.",
      parametrlar=dict(arch="baso4_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="5,3 g soda (Na₂CO₃) ortiqcha kislota bilan reaksiyaga kirishganda ajralgan gaz hajmini "
            "(n.sh., L) toping. (M(Na₂CO₃)=106)",
      javob="1,12", yechim="n = 0,05 mol → V(CO₂) = 1,12 L.",
      parametrlar=dict(arch="co2_o1_a")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="0,2 mol ammoniy ionidan ishqor bilan qizdirishda ajraladigan ammiak massasini (g) "
            "toping. (M(NH₃)=17)",
      javob="3,4", yechim="n(NH₃) = 0,2 mol → m = 3,4 g.",
      parametrlar=dict(arch="nh3_o1_a")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Eritmadagi 0,1 mol Cu²⁺ ortiqcha ishqor bilan cho'ktirildi. Cho'kma massasini (g) "
            "toping. (M(Cu(OH)₂)=98)",
      javob="9,8", yechim="m = 0,1·98 = 9,8 g.",
      parametrlar=dict(arch="cuoh2_o1")),
]

# ---------- O2 ----------
check("o41c", 0.1*143.5, 14.35)
O2 = [
 dict(n=41, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Oq kristall modda tekshirildi: alanga testi SARIQ rang berdi; eritmasiga AgNO₃ "
            "tomizilganda OQ cho'kma tushdi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir sinov qaysi ionni ko'rsatadi?",
             yechim=["Sariq alanga → Na⁺; oq cho'kma (AgCl) → Cl⁻."], M=4, A=2),
        dict(savol="b) Moddaning formulasini va nomini yozing.",
             yechim=["NaCl — osh tuzi."], M=3, A=2),
        dict(savol="c) 0,1 mol shu tuzdan olinadigan AgCl massasini hisoblang. (M(AgCl)=143,5)",
             yechim=["m = 14,35 g."], M=4, A=3),
        dict(savol="d) Cho'kmani tasdiqlashning qo'shimcha belgisi qanday?",
             yechim=["AgCl yorug'likda asta qorayadi; HNO₃ da erimaydi."], M=4, A=3),
      ],
      rasmiylashtirish="Modda-detektiv: sinovlar → formula → hisob → tasdiq; M15+A10.",
      parametrlar=dict(arch="modda_detektiv")),
 dict(n=42, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Sifat tahlilining nozik jihatlari o'rganiladi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega xloridni AgNO₃ bilan tekshirishdan OLDIN eritmaga nitrat kislota "
                   "qo'shiladi? Batafsil tushuntiring.",
             yechim=["Karbonat/fosfat kabi ionlar ham Ag⁺ bilan cho'kma beradi — «soxta signal».",
                     "HNO₃ ularni parchalaydi (CO₂ chiqadi), AgCl esa kislotada erimay qoladi."], M=13, A=0),
        dict(savol="b) Nega alanga testida sim har namunadan keyin kislotada tozalanadi?",
             yechim=["Oldingi namuna qoldig'i (ayniqsa natriy) keyingi rangni «bosib» yuboradi."], M=9, A=0),
        dict(savol="c) Sifat tahlilida «bitta belgi — hukm emas» qoidasi nimani anglatadi?",
             yechim=["Xulosa kamida ikki mustaqil sinov bilan tasdiqlanadi."], M=3, A=0),
      ],
      rasmiylashtirish="Tahlil-madaniyati (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="tahlil_madaniyati")),
 dict(n=43, tur="O2", element="IV.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("To'rt rangsiz eritma jadvalda berilgan:\n"
            "[JADVAL] № | Eritma ;; 1 | NaCl ;; 2 | Na₂SO₄ ;; 3 | Na₂CO₃ ;; 4 | NaNO₃\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Uch reagent (HCl, BaCl₂, AgNO₃) yordamida to'rttala eritmani farqlash rejasini tuzing.",
             yechim=["Avval HCl: gaz bergani — Na₂CO₃. Keyin BaCl₂: cho'kma — Na₂SO₄. "
                     "So'ng AgNO₃: cho'kma — NaCl; hech narsa — NaNO₃."], M=6, A=3),
        dict(savol="b) Har bir musbat sinovning tenglamasini yozing.",
             yechim=["Na₂CO₃+2HCl→2NaCl+H₂O+CO₂; Na₂SO₄+BaCl₂→BaSO₄↓+2NaCl; NaCl+AgNO₃→AgCl↓+NaNO₃."], M=5, A=3),
        dict(savol="c) Nega NaNO₃ «istisno usuli» bilan topiladi?",
             yechim=["NO₃⁻ uchun oddiy cho'kma reaksiyasi yo'q — qolganlari chiqarilgach aniqlanadi."], M=2, A=2),
        dict(savol="d) Sinovlar TARTIBI muhimligini bitta misolda ko'rsating.",
             yechim=["AgNO₃ ni birinchi qo'shsak, karbonat/sulfat ham cho'kadi — natija chalkashadi."], M=2, A=2),
      ],
      rasmiylashtirish="Farqlash-reja: ketma-ketlik → tenglamalar → istisno → tartib; M15+A10.",
      parametrlar=dict(arch="farqlash_reja_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261703)
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
    variant="mavzu-IV2-A", daraja="A", bob=17, bob_nomi="Sifat reaksiyalari",
    manba=("MS spetsifikatsiyasi IV.2; laboratoriya banki arxetiplari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (yodlangan tuz, mineral suv, bo'yoqlar, test-to'plam) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="IV.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
