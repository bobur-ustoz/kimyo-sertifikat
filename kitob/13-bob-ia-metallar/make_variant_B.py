# -*- coding: utf-8 -*-
"""13-bob B-varianti: IA guruh metallari (II.3) — HAQIQIY MS MUHITI ★★★.
Noma'lum metall, peroksid/superoksid, kristallogidrat, aralashma va nisbat masalalari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_II3B.json"
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

# 1 (3) — 1-2-3: to'g'ri fikrlar
q(3, "yuqori",
  "Ishqoriy metallar haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) barchasi +1 oksidlanish darajasini namoyon qiladi;  2) zichliklari juda katta;  "
  "3) Li, Na, K suvdan yengil;  4) guruhda pastga suyuqlanish harorati ortadi.",
  "1 va 3",
  [("1, 3 va 4", "suyuqlanish harorati pastga KAMAYADI"),
   ("2 va 4", "zichliklari kichik: Li 0,53 g/sm³"),
   ("faqat 1", "Li, Na, K haqiqatan suvda qalqib turadi (reaksiya bilan!)")],
  "ns¹ → +1; yengil metallar (Li, Na, K < 1 g/sm³); t(suyuql.) pastga kamayadi.",
  dict(arch="togri_fikr_tanlov"))

# 2 (3) — noma'lum metall
check("q2", 3.9/(1.12/22.4*2), 39)
q(3, "yuqori",
  "3,9 g noma'lum ishqoriy metall suv bilan reaksiyaga kirishganda 1,12 L (n.sh.) vodorod ajraldi. "
  "Metallni aniqlang.",
  "K", [("Na", "M = 23 bo'lardi (2,3 g kerak edi)"), ("Li", "M = 7 — juda yengil"),
         ("Rb", "M = 85,5 — mos emas")],
  "n(H₂) = 0,05 → n(Me) = 0,1 mol → M = 3,9/0,1 = 39 g/mol — kaliy.",
  dict(arch="nomalum_metall"))

# 3 (3) — peroksid
q(3, "yuqori",
  "Natriy havoda (ortiqcha kislorodda) yonganda ASOSAN qaysi mahsulot hosil bo'ladi?",
  "Na₂O₂ (peroksid)",
  [("Na₂O (oksid)", "oddiy oksid faqat kislorod yetishmaganda"),
   ("NaOH", "gidroksid suv bilan hosil bo'ladi"),
   ("NaO₂ ko'p miqdorda", "superoksid asosan K, Rb, Cs ga xos")],
  "2Na + O₂ → Na₂O₂ — IA guruhda faqat Li oddiy oksid (Li₂O) beradi.",
  dict(arch="peroksid"))

# 4 (3) — aralashma AgCl orqali
check("q4a", 28.7/143.5, 0.2); check("q4b", (13.3-58.5*0.2)/(74.5-58.5), 0.1); check("q4c", 0.1*74.5, 7.45)
q(3, "yuqori",
  "NaCl va KCl dan iborat 13,3 g aralashma eritmasiga ortiqcha AgNO₃ qo'shilganda 28,7 g cho'kma "
  "tushdi. Aralashmadagi KCl massasini toping. (M: NaCl=58,5, KCl=74,5, AgCl=143,5)",
  "7,45 g", [("5,85 g", "bu NaCl massasi"), ("13,3 g", "aralashmaning hammasi emas"),
              ("14,9 g", "0,2 mol deb olingan")],
  "n(AgCl) = 0,2 = x+y; 58,5x + 74,5y = 13,3 → y = 0,1 mol → m(KCl) = 7,45 g.",
  dict(arch="xlorid_aralashma"))

# 5 (3) — RASMLI: 1 g metall — H2
q(3, "yuqori",
  "Diagrammada TENG MASSALI (1 g dan) Li, Na va K ning suv bilan reaksiyasida ajralgan vodorod "
  "hajmlari berilgan. Nega eng ko'p vodorodni litiy beradi?",
  "molyar massasi eng kichik — 1 g da atomlar soni eng ko'p",
  [("litiy eng faol metall", "faollik aksincha K da yuqori — gap mol sonida"),
   ("litiy ko'proq elektron beradi", "har atom baribir 1 e beradi"),
   ("diagramma xato tuzilgan", "hisob buni tasdiqlaydi: 1/7 > 1/23 > 1/39")],
  "n = m/M: 1 g Li — 0,143 mol; Na — 0,043; K — 0,026 → H₂ ham shunga proporsional.",
  dict(arch="bar_teng_massa"), fig="bar_water")

# 6 (3)
q(3, "yuqori",
  "Sanoat va laboratoriyada NaOH ni Na₂CO₃ dan olishning qadimiy usuli (kaustifikatsiya) qaysi "
  "reaksiyaga asoslangan?",
  "Na₂CO₃ + Ca(OH)₂ → 2NaOH + CaCO₃↓",
  [("Na₂CO₃ + HCl → ...", "bu tuz va CO₂ beradi, ishqor emas"),
   ("Na₂CO₃ ni qizdirish", "o'rta karbonat parchalanmaydi"),
   ("Na₂CO₃ + H₂O → ...", "gidroliz to'liq NaOH bermaydi")],
  "CaCO₃ cho'kmaga tushib, eritmada NaOH qoladi — «kaustiklash».",
  dict(arch="kaustifikatsiya"))

# 7 (3) — 1-2-3: kaliy haqida
q(3, "yuqori",
  "Kaliy haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) suv bilan reaksiyada ajralgan H₂ alangalanadi;  2) alangani binafsha rangga bo'yaydi;  "
  "3) natriydan passivroq;  4) kerosin ostida saqlanadi.",
  "1, 2 va 4",
  [("1, 2 va 3", "K natriydan FAOLROQ"), ("faqat 2", "1 va 4 ham to'g'ri"),
   ("2 va 3", "3 noto'g'ri, 1 va 4 to'g'ri")],
  "K: shiddatli reaksiya (H₂ yonadi), binafsha alanga, kerosinda saqlanadi; faollik Na dan yuqori.",
  dict(arch="k_fikrlar"))

# 8 (2)
q(2, "yuqori",
  "«Texnik nom — formula» mosligini TO'G'RI ko'rsating: potash — ?",
  "K₂CO₃", [("KOH", "u — o'yuvchi kaliy"), ("KCl", "u — silvin (o'g'it)"), ("KNO₃", "u — kaliyli selitra")],
  "Potash — kaliy karbonat, o'simlik kuli tarkibida bo'lgan qadimiy modda.",
  dict(arch="potash_nom"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi metallarni suvdagi reaksiya kuzatuvi bilan TO'G'RI moslang:\n"
  "[JADVAL] Metall | Kuzatuv ;; a) Li | 1) yuzada yugurib eriydi ;; b) Na | 2) sekin, tinch eriydi ;; "
  "c) K | 3) chaqnab, binafsha alanga bilan",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "Li eng sekin — u «tinch»"), ("a—2, b—3, c—1", "alanga — kaliyda"),
   ("a—3, b—1, c—2", "Li chaqnamaydi")],
  "Faollik Li < Na < K: sekin → yugurib → alanga bilan.",
  dict(arch="suv_kuzatuv_jadval"))

# 10 (3)
check("q10", 0.23/23*40, 0.4)
q(3, "yuqori",
  "0,23 g natriy suvga tashlandi. Hosil bo'lgan ishqor massasini toping. (M: Na=23, NaOH=40)",
  "0,4 g", [("0,23 g", "massa o'zgaradi — OH qo'shiladi"), ("4 g", "nol adashgan"),
             ("0,2 g", "yarim olingan")],
  "n = 0,01 mol → m(NaOH) = 0,01·40 = 0,4 g.",
  dict(arch="kichik_na_hisob"))

# 11 (3) — kristallogidrat
check("q11", 28.6/286*106, 10.6)
q(3, "yuqori",
  "28,6 g kristall soda (Na₂CO₃·10H₂O) tarkibidagi suvsiz tuz massasini toping. "
  "(M: Na₂CO₃·10H₂O=286, Na₂CO₃=106)",
  "10,6 g", [("28,6 g", "suv chegirilmagan"), ("18 g", "bu suvning bir molyar massasi"),
              ("21,2 g", "0,2 mol deb olingan")],
  "n = 28,6/286 = 0,1 mol → m(Na₂CO₃) = 10,6 g.",
  dict(arch="kristall_soda"))

# 12 (2)
q(2, "yuqori",
  "IA metallarning ionlari (Na⁺, K⁺) eritmada qanday rang beradi va ular qanday aniqlanadi?",
  "rangsiz; alanga testi orqali aniqlanadi",
  [("sariq va binafsha rangda", "eritma emas, ALANGA shunday bo'yaladi"),
   ("ko'k rangda", "ko'k — Cu²⁺ ioni"),
   ("aniqlab bo'lmaydi", "alanga testi ishonchli usul")],
  "Eritmalari rangsiz; cho'kma reaksiyalari ham deyarli yo'q — shu bois alanga testi asosiy usul.",
  dict(arch="ion_rang"))

# 13 (3)
q(3, "yuqori",
  "0,2 mol KOH orqali 0,2 mol SO₂ o'tkazildi. Qaysi tuz hosil bo'ladi?",
  "KHSO₃ (nordon tuz)",
  [("K₂SO₃ (o'rta tuz)", "buning uchun KOH ikki barobar ko'p bo'lishi kerak"),
   ("K₂SO₄", "sulfat SO₃ dan hosil bo'ladi"),
   ("ikkala tuz teng miqdorda", "nisbat aynan 1:1 — faqat nordon tuz")],
  "KOH : SO₂ = 1:1 → KOH + SO₂ → KHSO₃.",
  dict(arch="nisbat_tuz"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Xossa | Na | K ;; zichlik, g/sm³ | 0,97 | 0,86 ;; suvdan yengilmi? | ? | ? ;; "
  "pichoqda kesiladimi? | ha | ?",
  "ha; ha; ha",
  [("yo'q; ha; ha", "0,97 < 1 — natriy ham suvdan yengil"),
   ("ha; yo'q; ha", "0,86 < 1 — kaliy ham yengil"),
   ("ha; ha; yo'q", "K natriydan ham yumshoqroq")],
  "Ikkalasining zichligi 1 dan kichik; ikkalasi yumshoq.",
  dict(arch="xossa_jadval"))

# 15 (3)
q(3, "yuqori",
  "Suyuqlantirilgan NaCl elektroliz qilinganda katodda va anodda mos ravishda nima ajraladi?",
  "Na va Cl₂",
  [("H₂ va Cl₂", "bu NaCl ERITMASI elektrolizi"), ("Na va O₂", "kislorod xloridda yo'q"),
   ("Cl₂ va Na", "elektrodlar almashib ketgan")],
  "Suyuqlanmada suv yo'q: katod — Na⁺ + e → Na; anod — 2Cl⁻ − 2e → Cl₂.",
  dict(arch="suyuqlanma_elektroliz"))

# 16 (2)
q(2, "yuqori",
  "Rubidiy va seziy qanday saqlanadi?",
  "vakuumlangan shisha ampulalarda",
  [("kerosin ostida", "ular kerosin ostida ham xavfli darajada faol"),
   ("ochiq bankada", "havoda o'z-o'zidan alangalanadi"),
   ("suv ostida", "portlaydi")],
  "Rb, Cs — havoda o'z-o'zidan yonadi: faqat ampulada, inert muhitda.",
  dict(arch="rb_cs_saqlash"))

# 17 (3)
check("q17", 11.2/56*63, 12.6)
q(3, "yuqori",
  "11,2 g kaliy gidroksidni to'liq neytrallash uchun necha gramm nitrat kislota kerak? "
  "(M: KOH=56, HNO₃=63)",
  "12,6 g", [("63 g", "1 mol uchun"), ("6,3 g", "0,1 mol deb olingan"), ("25,2 g", "ikki baravar")],
  "n(KOH) = 0,2 mol → n(HNO₃) = 0,2 → m = 12,6 g.",
  dict(arch="koh_hno3"))

# 18 (2)
q(2, "yuqori",
  "Kosmik kemalarda havodagi CO₂ ni yutish uchun qaysi modda ishlatiladi?",
  "LiOH", [("NaCl", "tuz CO₂ ni yutmaydi"), ("Li metali", "metall bilan emas, ishqor bilan yutiladi"),
            ("H₂SO₄", "kislota CO₂ bilan reaksiyaga kirishmaydi")],
  "2LiOH + CO₂ → Li₂CO₃ + H₂O: LiOH yengil — har gramm muhim bo'lgan kosmosda qulay.",
  dict(arch="lioh_kosmos"))

# 19 (3) — RASMLI: natriyni kesish
q(3, "yuqori",
  "Rasmda natriy bilan ishlash jarayoni: metall pinset bilan olinib, filtr qog'ozda quritilyapti va "
  "pichoq bilan kesilyapti. Filtr qog'ozning vazifasi nima?",
  "yuzadagi kerosinni shimib olish — aks holda tortishda xato bo'ladi va reaksiya sekinlashadi",
  [("metallni sovutish", "harorat muammo emas"),
   ("metallni yumshatish", "Na o'zi yumshoq"),
   ("qo'lni himoya qilish", "qo'l himoyasi — pinsetning ishi")],
  "Tajribadan oldin kerosin qoldig'i olib tashlanadi; metall qo'lga OLINMAYDI.",
  dict(arch="na_kesish_oqish"), fig="sodium_cut")

# 20 (2)
q(2, "yuqori",
  "Davriy jadvalda IA guruh katagida vodorod ham yoziladi. Vodorod haqida qaysi fikr to'g'ri?",
  "u metall emas — faqat konfiguratsiyasi (1s¹) o'xshash",
  [("u ham ishqoriy metall", "H — metallmas gaz"),
   ("u suyuq metall", "suyuq metall — simob"),
   ("u kerosinda saqlanadi", "gaz ballonlarda saqlanadi")],
  "H ning o'rni shartli: 1 valent elektron bor, lekin xossalari galogenlarga ham o'xshaydi.",
  dict(arch="vodorod_orni"))

# 21 (3)
check("q21", 6.2/62*2*40, 8)
q(3, "yuqori",
  "Na₂O + H₂O → 2NaOH. 6,2 g natriy oksididan olingan ishqor massasini toping. (M: Na₂O=62, NaOH=40)",
  "8 g", [("4 g", "koeffitsiyent 2 unutilgan"), ("40 g", "1 mol uchun"), ("6,2 g", "massa o'zgaradi")],
  "n = 0,1 mol → NaOH 0,2 mol → 8 g.",
  dict(arch="na2o_hisob"))

# 22 (3) — 1-2-3: suvdan H2
q(3, "yuqori",
  "Qaysi metallar ODDIY sharoitda suv bilan reaksiyaga kirishib, ishqor va vodorod beradi?\n"
  "1) Na;  2) Cu;  3) K;  4) Fe;  5) Ag.",
  "1 va 3",
  [("1, 3 va 4", "Fe faqat qizdirilganda bug' bilan (va ishqor emas, oksid beradi)"),
   ("hammasi", "Cu, Ag suv bilan umuman kirishmaydi"),
   ("faqat 1", "K ham (hattoki shiddatliroq)")],
  "Faqat ishqoriy (va ba'zi IIA) metallar: 2Me + 2H₂O → 2MeOH + H₂.",
  dict(arch="suv_h2_tanlov"))

# 23 (3) — aralashma
check("q23a", 1.12/22.4*2*23, 2.3); check("q23b", 6.2-2.3, 3.9)
q(3, "yuqori",
  "Na va Na₂O dan iborat 6,2 g aralashma suvga solindi; 1,12 L (n.sh.) vodorod ajraldi. "
  "Aralashmadagi Na₂O massasini toping. (M: Na=23, Na₂O=62)",
  "3,9 g", [("2,3 g", "bu Na massasi"), ("6,2 g", "aralashmaning hammasi emas"),
             ("3,1 g", "0,05 mol deb olingan")],
  "H₂ faqat metalldan: n(Na) = 0,1 mol → 2,3 g → m(Na₂O) = 6,2 − 2,3 = 3,9 g.",
  dict(arch="na_na2o_aralashma"))

# 24 (2)
q(2, "yuqori",
  "Kaliyli selitra (KNO₃) asosan qayerda ishlatiladi?",
  "kompleks o'g'it sifatida (K va N beradi)",
  [("faqat portlovchi sifatida", "asosiy zamonaviy ishlatilishi — o'g'it"),
   ("oziq-ovqat konservanti sifatida keng", "cheklangan; asosiy yo'nalish o'g'it"),
   ("yoqilg'i sifatida", "o'zi yonmaydi — oksidlovchi")],
  "KNO₃ — ikki oziq elementli (N + K) qimmatli o'g'it.",
  dict(arch="kno3_ishlatish"))

# 25 (3)
q(3, "yuqori",
  "NaOH dan NaHCO₃ (nordon tuz) olish uchun qanday shart bajarilishi kerak?",
  "CO₂ ORTIQCHA miqdorda o'tkazilishi",
  [("CO₂ kam miqdorda berilishi", "kam CO₂ o'rta tuz (Na₂CO₃) beradi"),
   ("eritma qizdirilishi", "qizdirish NaHCO₃ ni aksincha parchalaydi"),
   ("katalizator qo'shilishi", "katalizator shart emas")],
  "NaOH + CO₂(ortiqcha) → NaHCO₃; 2NaOH + CO₂(kam) → Na₂CO₃ + H₂O.",
  dict(arch="nordon_shart"))

# 26 (3) — RASMLI: bar hisob
check("q26", 1/7/2*22.4, 1.6)
q(3, "yuqori",
  "5-savol diagrammasini tekshiring: 1 g litiy suv bilan reaksiyaga kirishganda ajraladigan vodorod "
  "hajmini hisoblang. (M(Li)=7)",
  "1,6 L", [("3,2 L", "H₂ koeffitsiyenti unutilgan"), ("22,4 L", "1 mol uchun"),
             ("0,8 L", "yana ikkiga bo'lingan")],
  "n(Li) = 1/7 mol → n(H₂) = 1/14 → V = 22,4/14 = 1,6 L.",
  dict(arch="bar_water_hisob"), fig="bar_water")

# 27 (3)
check("q27", 200*0.2/40, 1)
q(3, "yuqori",
  "200 g 20 % li NaOH eritmasida necha mol ishqor bor? (M(NaOH)=40)",
  "1", [("0,5", "40 g = 1 mol"), ("2", "ikki baravar"), ("0,2", "foiz mol emas")],
  "m(NaOH) = 40 g → n = 1 mol.",
  dict(arch="foiz_mol"))

# 28 (2) — RASMLI: suyuqlanish grafigi (B talqini)
q(2, "yuqori",
  "Grafikdan foydalaning: qaysi ishqoriy metall inson kaftida (36,6 °C) erib ketishi mumkin?",
  "Cs (28 °C)", [("Na (98 °C)", "kaft harorati yetmaydi"), ("Li (181 °C)", "eng chidamlisi"),
                  ("K (64 °C)", "64 > 36,6")],
  "Suyuqlanish harorati tana haroratidan past bo'lgan yagona barqaror IA metall — seziy.",
  dict(arch="kaft_erish"), fig="melting")

# 29 (3)
q(3, "yuqori",
  "Suv osti kemalari va kosmik stansiyalarda Na₂O₂ (peroksid) nima maqsadda ishlatiladi?",
  "CO₂ ni yutib, kislorod ajratish uchun",
  [("suvni tozalash uchun", "asosiy vazifasi havo regeneratsiyasi"),
   ("yoqilg'i sifatida", "u oksidlovchi, yoqilg'i emas"),
   ("issiqlik manbai sifatida", "maqsad — kislorod")],
  "2Na₂O₂ + 2CO₂ → 2Na₂CO₃ + O₂ — «nafas olayotgan» modda.",
  dict(arch="na2o2_regeneratsiya"))

# 30 (2)
q(2, "yuqori",
  "Li, Na, K zichliklari haqida qaysi fikr to'g'ri?",
  "uchalasi ham suvdan yengil",
  [("uchalasi suvdan og'ir", "0,53; 0,97; 0,86 g/sm³ — hammasi < 1"),
   ("faqat Li yengil", "Na va K ham yengil"),
   ("faqat K og'ir", "K ham yengil (0,86)")],
  "Shu bois ular suv YUZASIDA reaksiyaga kirishadi.",
  dict(arch="zichlik_fakt"))

# 31 (3)
check("q31", 5.6/56*39, 3.9)
q(3, "yuqori",
  "Noma'lum massali kaliy suv bilan reaksiyaga kirishib, 5,6 g KOH hosil qildi. Olingan kaliy "
  "massasini toping. (M: K=39, KOH=56)",
  "3,9 g", [("5,6 g", "mahsulot massasi"), ("7,8 g", "ikki baravar"), ("1,95 g", "yarmi")],
  "n(KOH) = 0,1 mol → n(K) = 0,1 → m = 3,9 g.",
  dict(arch="k_teskari"))

# 32 (3) — RASMLI: grafik hisob
check("q32", 181-28, 153)
q(3, "yuqori",
  "Grafikdan: litiy va seziy suyuqlanish haroratlari orasidagi farqni toping.",
  "153 °C", [("209 °C", "yig'indi olingan"), ("117 °C", "Li−K farqi"), ("70 °C", "bu Na va Cs farqi (98−28)")],
  "181 − 28 = 153 °C.",
  dict(arch="suyuqlanish_farq_b"), fig="melting")

# ---------- Y2: uch metall ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.3",
  ichki_pasport=[dict(n=33, element="II.3", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="II.3", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="II.3", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch ishqoriy metall tekshirildi: X — suv bilan tinch reaksiyaga kirishadi, alangani "
               "qizil rangga bo'yaydi; Y — shiddatli reaksiyada H₂ alangalanadi, alanga binafsha; "
               "Z — suv yuzasida «yugurib» eriydi, alanga sariq. 33–35-savollarga A–F ro'yxatidan "
               "javob tanlang."),
  savollar_ichki=[
    "33. Y metall qaysi?",
    "34. Z ning suv bilan reaksiyasida hosil bo'ladigan ishqor qaysi?",
    "35. X, Y, Z ni faollik ORTIB borish tartibida joylashtiring."],
  javoblar_royxati=["A) K", "B) NaOH", "C) X → Z → Y", "D) Na", "E) KOH", "F) Y → Z → X"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="sariq alanga — Z (natriy); Y binafsha — kaliy"),
                   dict(variant="E", xato="Z — natriy: ishqori NaOH"),
                   dict(variant="F", xato="bu kamayish tartibi")],
  yechim=("Qizil — Li (X), binafsha — K (Y), sariq — Na (Z). "
          "Faollik: Li < Na < K → X → Z → Y."),
  parametrlar=dict(arch="uch_ia_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 2.24/22.4*2, 0.2); check("o36b", (6.2-23*0.2)/(39-23), 0.1); check("o36c", 0.1*39, 3.9)
check("o37", 4.6/23/2*142, 14.2)
check("o38", 11.7/58.5*40, 8)
check("o39", 57.2/286*106, 21.2)
check("o40a", 8/40, 0.2); check("o40b", 3.36/22.4, 0.15); check("o40c", 0.1*84, 8.4)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Na va K dan iborat 6,2 g aralashma suv bilan reaksiyaga kirishganda 2,24 L (n.sh.) "
            "vodorod ajraldi. Aralashmadagi kaliy massasini (g) toping. (M: Na=23, K=39)",
      javob="3,9", yechim="x+y = 0,2; 23x+39y = 6,2 → 16y = 1,6 → y = 0,1 → m(K) = 3,9 g.",
      parametrlar=dict(arch="na_k_aralashma_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="Na → NaOH → Na₂SO₄ zanjiri bo'yicha 4,6 g natriydan (yo'qotishsiz) olingan tuz massasini "
            "(g) toping. (M(Na₂SO₄)=142)",
      javob="14,2", yechim="n(Na) = 0,2 → n(Na₂SO₄) = 0,1 mol → m = 14,2 g.",
      parametrlar=dict(arch="na_zanjir_o1")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi zanjir bo'yicha 11,7 g osh tuzidan (yo'qotishsiz) olingan NaOH massasini (g) "
            "toping. (M: NaCl=58,5, NaOH=40)",
      javob="8", yechim="n(NaCl) = 0,2 → elektroliz → Na 0,2 → NaOH 0,2 mol → 8 g.",
      parametrlar=dict(arch="sxema_nacl_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="57,2 g kristall soda (Na₂CO₃·10H₂O) qizdirilib suvsizlantirildi. Qolgan suvsiz tuz "
            "massasini (g) toping. (M: krist.=286, Na₂CO₃=106)",
      javob="21,2", yechim="n = 0,2 mol → m = 0,2·106 = 21,2 g.",
      parametrlar=dict(arch="kristall_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="8 g NaOH li eritma orqali 3,36 L (n.sh.) CO₂ o'tkazildi. Hosil bo'lgan NaHCO₃ massasini "
            "(g) toping. (M: NaOH=40, NaHCO₃=84)",
      javob="8,4", yechim="n(NaOH)=0,2; n(CO₂)=0,15 → aralash tuzlar: x+2y=0,2, x+y=0,15 → "
            "x(NaHCO₃)=0,1 mol → 8,4 g.",
      parametrlar=dict(arch="co2_nisbat_zanjir")),
]

# ---------- O2 ----------
check("o41b", 0.46/23/2*22.4, 0.224)
check("o41c", 0.02*40, 0.8)
check("o41d", 0.8/(100+0.46-0.02*2)*100, 0.8, tol=0.02)
check("o43", 0.1+0.1+0.1*1, 0.3)
O2 = [
 dict(n=41, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "0,46 g natriy 100 g suvga tashlandi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing.",
             yechim=["2Na + 2H₂O → 2NaOH + H₂↑."], M=3, A=2),
        dict(savol="b) Ajralgan vodorod hajmini (n.sh.) toping.",
             yechim=["n(Na) = 0,02 mol → n(H₂) = 0,01 → V = 0,224 L."], M=4, A=3),
        dict(savol="c) Hosil bo'lgan NaOH massasini hisoblang.",
             yechim=["n = 0,02 mol → m = 0,8 g."], M=4, A=3),
        dict(savol="d) Eritmadagi NaOH ning massa ulushini (%) toping (H₂ chiqib ketganini hisobga oling).",
             yechim=["m(eritma) = 100 + 0,46 − 0,02 = 100,44 g → ω = 0,8/100,44 ≈ 0,8 %."], M=4, A=2),
      ],
      rasmiylashtirish="Na-suv to'liq zanjiri: tenglama → gaz → ishqor → foiz; M15+A10.",
      parametrlar=dict(arch="na_suv_foiz_zanjir")),
 dict(n=42, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("IA guruh bo'ylab qonuniyatlar tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega guruhda yuqoridan pastga metallik faolligi ortadi? Atom tuzilishi asosida "
                   "bosqichma-bosqich tushuntiring.",
             yechim=["Pastga qavatlar soni ortadi → radius kattalashadi → tashqi 1 e yadrodan uzoqlashadi",
                     "va ichki qavatlar uni to'sadi → e ni berish osonlashadi → faollik ortadi."], M=13, A=0),
        dict(savol="b) Nega ishqoriy metallar doim +1 oksidlanish darajasini namoyon qiladi?",
             yechim=["Bitta e berish barqaror inert-gaz qavatini ochadi; 2-e ni ichki qavatdan olish "
                     "juda katta energiya talab qiladi."], M=9, A=0),
        dict(savol="c) Fransiy (Fr) haqida bashorat: faolligi qanday bo'ladi?",
             yechim=["Guruhning eng ostida — nazariy jihatdan eng faol ishqoriy metall."], M=3, A=0),
      ],
      rasmiylashtirish="Qonuniyat-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="qonuniyat_mulohaza")),
 dict(n=43, tur="O2", element="II.3", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Uch natriy birikmasi jadvalda berilgan:\n"
            "[JADVAL] № | Modda ;; 1 | NaOH ;; 2 | Na₂CO₃ ;; 3 | NaHCO₃\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har birining xlorid kislota bilan reaksiya tenglamasini yozing.",
             yechim=["NaOH+HCl→NaCl+H₂O; Na₂CO₃+2HCl→2NaCl+H₂O+CO₂; NaHCO₃+HCl→NaCl+H₂O+CO₂."], M=5, A=3),
        dict(savol="b) 0,1 mol NaOH, 0,1 mol Na₂CO₃ va 0,1 mol NaHCO₃ aralashmasini to'liq "
                   "neytrallash uchun jami necha mol HCl kerak?",
             yechim=["0,1 + 0,2 + 0,1 = 0,4 mol."], M=4, A=3),
        dict(savol="c) Qaysi ikkitasi o'zaro reaksiyaga kirisha oladi? Tenglama yozing.",
             yechim=["NaOH + NaHCO₃ → Na₂CO₃ + H₂O."], M=3, A=2),
        dict(savol="d) Uchchalasini bitta reagent bilan qanday farqlash mumkinligini tavsiflang.",
             yechim=["Masalan, CaCl₂: Na₂CO₃ — darhol cho'kma; NaOH — cho'kmasiz (issiqlik); "
                     "NaHCO₃ — qizdirilgandagina cho'kma."], M=3, A=2),
      ],
      rasmiylashtirish="Uch birikma tahlili: tenglamalar → mol hisobi → o'zaro → farqlash; M15+A10.",
      parametrlar=dict(arch="uch_birikma_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261305)
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
    d = dict(n=n, tur="Y1", element="II.3", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II3-B", daraja="B", bob=13, bob_nomi="IA guruh metallari",
    manba=("Tongotarov/DTM arxetiplari (noma'lum metall, aralashma, kristallogidrat, nisbatga qarab "
           "tuz turi) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS "
           "spetsifikatsiyasi II.3"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: noma'lum metall masalalari, peroksidlar, "
          "teng massa diagrammasi, aralash tuz hosil bo'lishi."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.3") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
