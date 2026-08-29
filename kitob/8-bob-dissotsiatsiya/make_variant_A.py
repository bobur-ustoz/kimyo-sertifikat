# -*- coding: utf-8 -*-
"""8-bob A-varianti: Elektrolitik dissotsiatsiya va pH (I.8) — O'RGATUVCHI ★★.
Hayotiy sahnalar: sovun, gidrangeya guli, oshqozon-antatsid, basseyn."""
import json, random

OUT = "mavzu_I8A.json"
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
  "Elektrolitlar deb qanday moddalarga aytiladi?",
  "eritmasi (yoki suyuqlanmasi) elektr tokini o'tkazadigan moddalarga",
  [("faqat metallarga", "metallar eritma emas, o'zi o'tkazadi"),
   ("barcha suyuq moddalarga", "spirt, benzin o'tkazmaydi"),
   ("faqat kislotalarga", "tuzlar va ishqorlar ham elektrolit")],
  "Elektrolitlar: kislotalar, ishqorlar, tuzlar — suvda ionlarga ajraladi.",
  dict(arch="elektrolit_tarif"))

# 2 (2)
q(2, "quyi",
  "Elektrolitik dissotsiatsiya nima?",
  "elektrolitning suvda ionlarga ajralishi",
  [("moddaning bug'lanishi", "bu fizik jarayon"),
   ("cho'kma hosil bo'lishi", "bu reaksiya natijasi"),
   ("moddaning yonishi", "yonish — oksidlanish")],
  "Erish jarayonida qutbli suv molekulalari ta'sirida elektrolit ionlarga ajraladi.",
  dict(arch="dissotsiatsiya_tarif"))

# 3 (2)
q(2, "o'rta",
  "NaCl ning suvdagi dissotsiatsiya tenglamasi qaysi javobda TO'G'RI yozilgan?",
  "NaCl → Na⁺ + Cl⁻",
  [("NaCl → Na⁻ + Cl⁺", "zaryadlar teskari: metall kation bo'ladi"),
   ("NaCl → Na + Cl", "zaryadsiz atomlar hosil bo'lmaydi"),
   ("NaCl → NaCl⁺ + e", "elektron ajralishi — bu dissotsiatsiya emas")],
  "Metall — musbat (kation), kislota qoldig'i — manfiy (anion).",
  dict(arch="dissots_tenglama"))

# 4 (2) — SAHNA: sovun
q(2, "o'rta",
  "Rasmga qarang: sovun ko'pigi qo'lda «sirg'anchiq» seziladi va uni universal indikator "
  "ko'kartiradi. Sovun eritmasining muhiti qanday?",
  "ishqoriy — pH > 7",
  [("kislotali — pH < 7", "kislotalar indikatorni qizartiradi"),
   ("neytral — pH = 7", "neytralda indikator rangi o'zgarmasdi"),
   ("muhiti bo'lmaydi", "har qanday suvli eritmaning pH i bor")],
  "Sovun — kuchsiz kislota va kuchli asos «tuzi»: eritmasi ishqoriy (pH ≈ 9–10), shu bois teri "
  "yog'ini eritib «sirg'anadi».",
  dict(arch="sovun_sahna"), fig="soap")

# 5 (2)
q(2, "o'rta",
  "Barcha kislotalar eritmalari uchun UMUMIY bo'lgan ion qaysi?",
  "H⁺", [("OH⁻", "bu ishqorlarning umumiy ioni"), ("Na⁺", "faqat natriyli birikmalarda"),
          ("Cl⁻", "faqat xloridlarda")],
  "Kislotalarning nordon ta'mi va indikatorga ta'siri — H⁺ ionlaridan.",
  dict(arch="h_umumiy"))

# 6 (2)
q(2, "o'rta",
  "Barcha ishqorlar eritmalari uchun UMUMIY ion qaysi?",
  "OH⁻", [("H⁺", "kislotalarning ioni"), ("K⁺", "faqat kaliyli ishqorda"), ("O²⁻", "eritmada bo'lmaydi")],
  "Ishqoriy muhit belgilari (sirg'anish, indikator ranglari) — OH⁻ dan.",
  dict(arch="oh_umumiy"))

# 7 (2)
q(2, "o'rta",
  "Lakmus ISHQORIY muhitda qanday rangga kiradi?",
  "ko'k", [("qizil", "kislota rangi"), ("rangsiz", "lakmus rangsizlanmaydi"), ("qora", "bunday rang yo'q")],
  "Lakmus: kislotada qizil, ishqorda ko'k, neytralda binafsha.",
  dict(arch="lakmus_ishqor"))

# 8 (2) — SAHNA: gidrangeya
q(2, "o'rta",
  "Rasmda gidrangeya (vodosbor) guli: KISLOTALI tuproqda KO'K, ishqoriy tuproqda PUSHTI gullaydi. "
  "Bog'bon ko'k gul olmoqchi. Tuproq qanday bo'lishi kerak?",
  "kislotali (pH < 7)",
  [("ishqoriy (pH > 7)", "ishqoriyda pushti gullaydi"),
   ("faqat neytral", "neytralda oraliq rang bo'ladi"),
   ("muhit ahamiyatsiz", "rang aynan tuproq pH iga bog'liq")],
  "Gul rangi tuproq pH ining tabiiy «indikatori»: kislotali muhit → ko'k gul.",
  dict(arch="gul_sahna"), fig="flower")

# 9 (2)
q(2, "o'rta",
  "pH = 7 bo'lgan eritma qanday muhitga ega?",
  "neytral", [("kislotali", "pH < 7 bo'lardi"), ("ishqoriy", "pH > 7 bo'lardi"),
               ("aniqlab bo'lmaydi", "pH aynan muhit o'lchovi")],
  "pH = 7: [H⁺] = [OH⁻] = 10⁻⁷ — toza suv, neytral tuz eritmalari.",
  dict(arch="ph7"))

# 10 (3)
check("q10", 4, 4)
q(3, "o'rta",
  "Eritmada [H⁺] = 10⁻⁴ mol/l. Eritmaning pH ini toping.",
  "4", [("10", "pOH hisoblangan"), ("−4", "ishora xatosi"), ("7", "neytral deb olingan")],
  "pH = −lg10⁻⁴ = 4 — kislotali muhit.",
  dict(arch="ph_oddiy"))

# 11 (2)
q(2, "o'rta",
  "Qaysi modda KUCHLI elektrolit?",
  "HNO₃", [("CH₃COOH", "kuchsiz kislota"), ("H₂S", "kuchsiz kislota"), ("NH₄OH", "kuchsiz asos")],
  "Nitrat kislota suvda to'liq dissotsiatsiyalanadi.",
  dict(arch="kuchli_oddiy"))

# 12 (2)
q(2, "o'rta",
  "Qaysi moddaning eritmasi elektr tokini O'TKAZMAYDI?",
  "shakar", [("osh tuzi", "ionlarga ajraladi"), ("xlorid kislota", "kuchli elektrolit"),
              ("kaliy nitrat", "eruvchan tuz — elektrolit")],
  "Shakar molekulalar holida eriydi — ion yo'q, tok yo'q.",
  dict(arch="noelektrolit_oddiy"))

# 13 (2) — SAHNA: oshqozon
q(2, "o'rta",
  "Rasmga qarang: jig'ildon qaynaganda (oshqozonda kislota ortib ketganda) antatsid dori "
  "(masalan, Mg(OH)₂) ichiladi. Dori qanday ta'sir qiladi?",
  "ortiqcha xlorid kislotani neytrallaydi",
  [("kislotani yanada oshiradi", "asos kislotani kamaytiradi"),
   ("oshqozonni sovutadi", "ta'sir kimyoviy, harorat emas"),
   ("ovqatni tez hazm qiladi", "antatsid ferment emas")],
  "Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O — neytrallanish: pH me'yorga qaytadi.",
  dict(arch="oshqozon_sahna"), fig="stomach")

# 14 (3)
check("q14", 3, 3)
q(3, "o'rta",
  "MgCl₂ to'liq dissotsiatsiyalanganda bitta formula birligidan nechta ion hosil bo'ladi?",
  "3", [("2", "2 ta xlor unutilgan"), ("4", "ortiqcha ion"), ("1", "ajralmaydi deb olingan")],
  "MgCl₂ → Mg²⁺ + 2Cl⁻ — jami 3 ta ion.",
  dict(arch="ion_sanash_oddiy"))

# 15 (2)
q(2, "o'rta",
  "AgNO₃ va NaCl eritmalari aralashtirilganda nima kuzatiladi?",
  "oq cho'kma (AgCl) tushadi",
  [("gaz ajraladi", "gaz hosil qiluvchi ionlar yo'q"),
   ("hech narsa o'zgarmaydi", "Ag⁺ + Cl⁻ → AgCl↓ boradi"),
   ("eritma qizib ketadi", "asosiy belgi — cho'kma")],
  "Ag⁺ + Cl⁻ → AgCl↓ — ion almashinish cho'kma bilan tugaydi.",
  dict(arch="agcl"))

# 16 (3)
q(3, "o'rta",
  "pH = 9 bo'lgan eritma qanday muhitga ega?",
  "kuchsiz ishqoriy", [("kuchli kislotali", "pH < 3 bo'lardi"), ("neytral", "pH = 7 bo'lardi"),
                        ("kuchli ishqoriy", "kuchli ishqoriylik pH ≈ 12–14")],
  "7 < pH < 10 — kuchsiz ishqoriy oraliq.",
  dict(arch="ph9"))

# 17 (2)
q(2, "o'rta",
  "Indikatorlar jadvalidagi «?» katakni to'ldiring:\n"
  "[JADVAL] Muhit | lakmus | fenolftalein ;; kislotali | qizil | rangsiz ;; ishqoriy | ko'k | ?",
  "pushti", [("rangsiz", "ishqorda fenolftalein rang beradi"), ("qizil", "bu lakmusning kislota rangi"),
              ("yashil", "fenolftaleinda bunday rang yo'q")],
  "Fenolftalein faqat ishqoriy muhitda to'q pushti bo'ladi.",
  dict(arch="indikator_jadval"))

# 18 (2) — SAHNA: basseyn
q(2, "o'rta",
  "Rasmda basseyn ko'rsatilgan: suvining pH i doim 7,2–7,6 oralig'ida ushlab turiladi. Buning sababi nima?",
  "bu oraliq ko'z-teri uchun bezarar va dezinfeksiya samarali ishlaydi",
  [("suv shu pH da chiroyliroq ko'rinadi", "rang emas, xavfsizlik va samaradorlik muhim"),
   ("pH suzish tezligiga ta'sir qiladi", "tezlikka aloqasi yo'q"),
   ("shunchaki an'ana", "aniq gigiyenik-kimyoviy asos bor")],
  "Juda past pH ko'zni achitadi, yuqori pH da xlorli dezinfeksiya kuchsizlanadi — shuning uchun doimiy nazorat.",
  dict(arch="basseyn_sahna"), fig="pool")

# 19 (3)
check("q19", 0.1, 0.1)
q(3, "o'rta",
  "0,1 mol NaOH to'liq dissotsiatsiyalanganda necha mol gidroksid-ion hosil bo'ladi?",
  "0,1", [("0,2", "NaOH da bitta OH bor"), ("0,05", "bo'lish xatosi"), ("1", "o'n barobar xato")],
  "NaOH → Na⁺ + OH⁻: 0,1 mol → 0,1 mol OH⁻.",
  dict(arch="oh_oddiy"))

# 20 (2)
q(2, "o'rta",
  "Toza suv nima uchun elektr tokini juda YOMON o'tkazadi?",
  "suv juda oz miqdorda ionlarga ajraladi",
  [("suvda umuman ion yo'q", "10⁻⁷ mol/l H⁺ va OH⁻ bor"),
   ("suv molekulasi og'ir", "massa sabab emas"),
   ("suv rangsiz", "rang o'tkazuvchanlikka aloqasiz")],
  "Suv — juda kuchsiz elektrolit: ionlari o'ta kam, tok deyarli o'tmaydi.",
  dict(arch="suv_kuchsiz"))

# 21 (3)
check("q21", 10, 10)
q(3, "o'rta",
  "pH bir birlikka kamaysa, eritmadagi [H⁺] necha marta o'zgaradi?",
  "10 marta ortadi", [("2 marta ortadi", "shkala logarifmik — 10 lik"), ("10 marta kamayadi", "pH kamayishi H⁺ ortishi demak"),
                       ("o'zgarmaydi", "pH aynan [H⁺] o'lchovi")],
  "pH — o'nli logarifm: har birlik = 10 barobar.",
  dict(arch="log_shkala"))

# 22 (3)
q(3, "o'rta",
  "HCl + NaOH → NaCl + H₂O reaksiyasining QISQA ion tenglamasini ko'rsating.",
  "H⁺ + OH⁻ → H₂O",
  [("Na⁺ + Cl⁻ → NaCl", "bu ionlar reaksiyada qatnashmaydi (tomoshabin)"),
   ("HCl + OH⁻ → Cl⁻ + H₂O", "HCl kuchli — ion holida yoziladi"),
   ("H⁺ + NaOH → Na⁺ + H₂O", "NaOH ham ion holida yoziladi")],
  "Kuchli elektrolitlar ionlarga yoziladi; mohiyat — suv hosil bo'lishi.",
  dict(arch="qisqa_ion_oddiy"))

# 23 (2)
q(2, "o'rta",
  "Na₂CO₃ eritmasiga HCl qo'shilganda «vishillab» chiqayotgan gaz qaysi?",
  "CO₂", [("H₂", "vodorod bunday reaksiyada ajralmaydi"), ("Cl₂", "xlor hosil bo'lmaydi"),
           ("O₂", "kislorod manbai yo'q")],
  "CO₃²⁻ + 2H⁺ → H₂O + CO₂↑ — karbonatlarning tanish reaksiyasi.",
  dict(arch="co2_gaz"))

# 24 (3)
check("q24", 0.05*2, 0.1)
q(3, "o'rta",
  "0,05 mol CaCl₂ to'liq dissotsiatsiyalanganda necha mol xlorid-ion hosil bo'ladi?",
  "0,1", [("0,05", "2 ta Cl unutilgan"), ("0,15", "3 ion jami — Cl⁻ emas"), ("0,2", "4 ta xato")],
  "CaCl₂ → Ca²⁺ + 2Cl⁻ → 0,05·2 = 0,1 mol Cl⁻.",
  dict(arch="cl_mol"))

# 25 (2)
q(2, "o'rta",
  "Fenolftalein KISLOTALI muhitda qanday bo'ladi?",
  "rangsiz", [("pushti", "bu ishqordagi rangi"), ("ko'k", "lakmus rangi"), ("qizil", "lakmus kislota rangi")],
  "Fenolftalein kislota va neytral muhitda rangsiz.",
  dict(arch="fenolftalein_oddiy"))

# 26 (3) — RASMLI: pH ustunlari
q(3, "o'rta",
  "Diagrammada kundalik moddalarning pH qiymatlari berilgan. Qaysi modda ENG KISLOTALI?",
  "limon sharbati",
  [("sirka", "pH 3 — limonnikidan (2) yuqori"), ("sut", "pH ≈ 6,5 — deyarli neytral"),
   ("sovun eritmasi", "pH ≈ 10 — ishqoriy")],
  "pH qancha KICHIK bo'lsa, muhit shuncha kislotali: limon (pH ≈ 2) ro'yxatda eng nordoni.",
  dict(arch="ph_bars_oqish"), fig="ph_bars")

# 27 (3)
check("q27", 3, 3)
q(3, "o'rta",
  "pH = 3 bo'lgan eritmadagi vodorod ionlari konsentratsiyasi qancha (mol/l)?",
  "10⁻³", [("3", "pH ning o'zi"), ("10⁻¹¹", "bu [OH⁻]"), ("10³", "manfiy daraja unutilgan")],
  "[H⁺] = 10⁻pH = 10⁻³ mol/l.",
  dict(arch="h_teskari"))

# 28 (2)
q(2, "o'rta",
  "Nega quruq osh tuzi tok o'tkazmaydi-yu, eritmasi o'tkazadi?",
  "eritmada ionlar erkin harakatlanadi, kristallda esa mahkam turadi",
  [("eritmada elektronlar paydo bo'ladi", "o'tkazuvchanlik ionli"),
   ("suvning o'zi tok o'tkazadi", "toza suv deyarli o'tkazmaydi"),
   ("kristall juda qattiq", "qattiqlik emas, ionlar harakati muhim")],
  "Tok tashuvchilar — erkin ionlar: ular faqat eritma/suyuqlanmada harakatchan.",
  dict(arch="kristall_eritma"))

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Kislotali eritma suv bilan suyultirib borilganda uning pH i qanday o'zgaradi? To'g'ri grafikni tanlang.",
  "ortib, 7 ga yaqinlashadi",
  [("kamayib boradi", "suyultirish [H⁺] ni kamaytiradi — pH ortadi"),
   ("o'zgarmaydi", "[H⁺] kamaygach pH ham o'zgaradi"),
   ("ortib, keyin kamayadi", "monoton 7 ga intiladi")],
  "[H⁺] kamayadi → pH ortadi, lekin 7 dan oshmaydi (kislota baribir kislota).",
  svg=dict(correct="rise_flat", d1="fall", d2="flat", d3="rise_fall", xlab="suyultirish", ylab="pH"),
  params=dict(arch="suyultirish_ph"))

# 30 (2)
q(2, "o'rta",
  "pH haqidagi fikrlardan XATOSINI toping.",
  "pH faqat kislotalarda bo'ladi",
  [("pH 0 dan 14 gacha o'zgaradi", "to'g'ri (odatdagi eritmalarda)"),
   ("pH = 7 — neytral muhit", "to'g'ri fikr"),
   ("pH kichik bo'lsa, kislotalilik kuchli", "to'g'ri fikr")],
  "pH har qanday suvli eritmada bor: ishqorda ham (7 dan katta), suvda ham (7).",
  dict(arch="xato_fikr"))

# 31 (3)
check("q31", 3, 3)
q(3, "o'rta",
  "0,001 M li xlorid kislota eritmasining pH ini toping (to'liq dissotsiatsiya).",
  "3", [("1", "0,1 M uchun qiymat"), ("11", "pOH hisoblangan"), ("0,001", "kontsentratsiyaning o'zi")],
  "[H⁺] = 10⁻³ → pH = 3.",
  dict(arch="hcl_ph"))

# 32 (3) — RASMLI: shkala o'qish
q(3, "o'rta",
  "Rasmdagi pH shkalasidan foydalaning: qora qahva pH ≈ 5 ga ega. U qanday muhitli ichimlik?",
  "kuchsiz kislotali",
  [("kuchli kislotali", "pH 5 — 7 ga ancha yaqin"), ("ishqoriy", "pH < 7 — kislotali tomon"),
   ("neytral", "neytral aynan 7")],
  "5 < 7, ammo 7 ga yaqin — kuchsiz kislotali (shkala chap-o'rta qismi).",
  dict(arch="shkala_qahva"), fig="ph_scale")

# ---------- Y2: choy-limon ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.8",
  ichki_pasport=[dict(n=33, element="I.8", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.8", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.8", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Achchiq choy — tabiiy indikator: muhitga qarab rangini o'zgartiradi. Bir piyola choyga "
               "limon bo'lagi solinganda rang keskin OCHILDI. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Limon qo'shilgach choy muhiti qanday bo'ldi?",
    "34. Bunda choyning pH qiymati qanday o'zgardi?",
    "35. Endi shu choyga oz-oz ichimlik sodasi qo'shib borilsa, muhit qaysi tomonga o'zgaradi?"],
  javoblar_royxati=["A) kislotali", "B) ishqoriy tomonga", "C) kamaydi", "D) ortdi", "E) o'zgarmadi", "F) neytral bo'ldi"],
  javoblar={"33": "A", "34": "C", "35": "B"},
  chalgituvchilar=[dict(variant="D", xato="kislota qo'shilishi pH ni KAMAYTIRADI"),
                   dict(variant="E", xato="rang o'zgardi — muhit ham o'zgargan"),
                   dict(variant="F", xato="soda ortiqcha qo'shilsa neytraldan ham o'tib ketadi")],
  yechim=("Limon kislotasi → muhit kislotali (A), pH kamaydi (C). Soda (NaHCO₃) kislotani "
          "neytrallab, muhitni ishqoriy tomonga suradi (B)."),
  parametrlar=dict(arch="choy_ssenariy"))

# ---------- O1 ----------
check("o38", 8, 8)
check("o39", 0.2*2, 0.4)
check("o40", 12, 12)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="HNO₃ dissotsiatsiyalanganda bitta molekuladan nechta vodorod ioni hosil bo'ladi?",
      javob="1", yechim="HNO₃ → H⁺ + NO₃⁻ — bitta H⁺.",
      parametrlar=dict(arch="h_soni_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="pH = 6 bo'lgan eritma muhitini yozing (kislotali/neytral/ishqoriy).",
      javob="kislotali", yechim="6 < 7 — kuchsiz bo'lsa-da kislotali.",
      parametrlar=dict(arch="muhit_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="Eritmada [H⁺] = 10⁻⁸ mol/l. pH ni toping.",
      javob="8", yechim="pH = −lg10⁻⁸ = 8 (kuchsiz ishqoriy).",
      parametrlar=dict(arch="ph_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="0,2 mol Na₂SO₄ dissotsiatsiyalanganda hosil bo'ladigan natriy ionlari mol sonini toping.",
      javob="0,4", yechim="Na₂SO₄ → 2Na⁺ + SO₄²⁻ → 0,2·2 = 0,4 mol Na⁺.",
      parametrlar=dict(arch="na_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="0,01 M li NaOH eritmasining pH ini toping.",
      javob="12", yechim="[OH⁻] = 10⁻² → pOH = 2 → pH = 12.",
      parametrlar=dict(arch="naoh_o1")),
]

# ---------- O2 ----------
check("o41a", 3.65/36.5, 0.1)
check("o41d", 0.1/10, 0.01)
O2 = [
 dict(n=41, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("3,65 g HCl suvda eritilib, 1 l eritma tayyorlandi. Bandlar ketma-ket yechiladi — har biri "
            "keyingisiga asos bo'ladi. (M(HCl)=36,5)"),
      bandlar=[
        dict(savol="a) Eritmaning molyar konsentratsiyasini toping.",
             yechim=["n = 0,1 mol → c = 0,1 M"], M=3, A=1),
        dict(savol="b) Vodorod ionlari konsentratsiyasini yozing.",
             yechim=["HCl kuchli → [H⁺] = 0,1 mol/l"], M=3, A=2),
        dict(savol="c) Eritmaning pH ini toping.",
             yechim=["pH = −lg0,1 = 1"], M=3, A=2),
        dict(savol="d) Eritmadan 100 ml olib, suv bilan 1 l gacha suyultirildi. Yangi pH ni toping.",
             yechim=["c = 0,01 M → pH = 2"], M=3, A=3),
        dict(savol="e) Bu eritmaga lakmus va fenolftalein tomizilsa qanday ranglar kuzatiladi?",
             yechim=["Lakmus — qizil; fenolftalein — rangsiz (kislotali muhit)."], M=3, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi pH zanjiri: c → [H⁺] → pH → suyultirish → indikatorlar; M15+A10.",
      parametrlar=dict(arch="hcl_zanjir")),
 dict(n=42, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Kechki ovqatdan so'ng odamning jig'ildoni qaynadi (oshqozonda HCl me'yordan oshib ketdi). "
            "Quyidagi savollarga MULOHAZA yuritib javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) «Jig'ildon qaynashi»ning kimyoviy sababini va antatsid dorining (Mg(OH)₂ asosli) "
                   "ta'sir mexanizmini tenglama bilan tushuntiring.",
             yechim=["Ortiqcha H⁺ qizilo'ngach devorini ta'sirlaydi. Antatsid — kuchsiz asos:",
                     "Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O — neytrallanish, pH me'yorlashadi."], M=13, A=0),
        dict(savol="b) Nega bu maqsadda NaOH kabi kuchli ishqor ishlatilmaydi?",
             yechim=["Kuchli ishqor to'qimani kuydiradi va pH ni keskin ishqoriy tomonga o'tkazib yuboradi;",
                     "kam eruvchan Mg(OH)₂ faqat ortiqcha kislota bilan reaksiyaga kirishadi."], M=9, A=0),
        dict(savol="c) Nega ichimlik sodasini tez-tez ichish tavsiya etilmaydi?",
             yechim=["NaHCO₃ + HCl → CO₂↑: gaz oshqozonni kengaytiradi, muhit buzilib kislota qayta ko'payadi."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="antatsid_mulohaza")),
 dict(n=43, tur="O2", element="I.8", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uy sharoitidagi uch suyuqlikning pH lari o'lchandi; natijalar jadvalda:\n"
            "[JADVAL] Suyuqlik | sirka | choynak suvi | sovun eritmasi ;; pH | 3 | 7 | 10\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir suyuqlikning muhitini aniqlang.",
             yechim=["Sirka — kislotali; suv — neytral; sovun — ishqoriy."], M=3, A=1),
        dict(savol="b) Har birida [H⁺] ni yozing.",
             yechim=["10⁻³; 10⁻⁷; 10⁻¹⁰ mol/l"], M=4, A=3),
        dict(savol="c) Sirka va sovun eritmalarida [H⁺] necha marta farq qilishini toping.",
             yechim=["10⁽¹⁰⁻³⁾ = 10⁷ marta (sirkada ko'p)."], M=4, A=3),
        dict(savol="d) Uchala suyuqlikka universal indikator tomizilsa qanday ranglar kuzatiladi?",
             yechim=["Sirka — qizg'ish-sariq; suv — yashil; sovun — ko'k-binafsha."], M=4, A=3),
      ],
      rasmiylashtirish="Uy-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="uy_jadval")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260626)
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
    variant="mavzu-I8-A", daraja="A", bob=8, bob_nomi="Elektrolitik dissotsiatsiya va pH",
    manba=("MS spetsifikatsiyasi I.8; darslik bo'limlari — savollar yangi tuzilgan, hayotiy sahnalar "
           "(sovun, gidrangeya, oshqozon, basseyn, choy-limon) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.8") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
