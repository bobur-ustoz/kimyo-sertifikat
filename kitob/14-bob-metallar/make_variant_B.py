# -*- coding: utf-8 -*-
"""14-bob B-varianti: IIA, IIIA va d-metallar. Suv qattiqligi (II.4) — HAQIQIY MS MUHITI ★★★.
Noma'lum metall, alyumotermiya, amfoter Al, aralashma va qattiqlik hisoblari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_II4B.json"
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
  "IIA guruh metallari haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) birikmalarida +2 oksidlanish darajasini namoyon qiladi;  2) Ca va Ba suv bilan oddiy sharoitda "
  "reaksiyaga kirishadi;  3) faolligi IA metallardan yuqori;  4) Mg sovuq suv bilan amalda kirishmaydi.",
  "1, 2 va 4",
  [("1, 2 va 3", "IIA faolligi IA dan PASTROQ"), ("faqat 1", "2 va 4 ham to'g'ri"),
   ("2 va 3", "3 noto'g'ri; 1 va 4 to'g'ri")],
  "ns² → +2; Ca, Sr, Ba suv bilan kirishadi; Mg faqat qaynoq suv/bug' bilan; faollik IA dan past.",
  dict(arch="iia_fikr_tanlov"))

# 2 (3) — noma'lum metall
check("q2", 4.8/(4.48/22.4), 24)
q(3, "yuqori",
  "4,8 g noma'lum ikki valentli metall xlorid kislotada eriganda 4,48 L (n.sh.) vodorod ajraldi. "
  "Metallni aniqlang.",
  "Mg", [("Ca", "M = 40 bo'lardi (8 g kerak edi)"), ("Zn", "M = 65 — mos emas"),
          ("Fe", "M = 56 — mos emas")],
  "Me + 2HCl → MeCl₂ + H₂: n(H₂) = 0,2 = n(Me) → M = 4,8/0,2 = 24 — magniy.",
  dict(arch="nomalum_ikki_valentli"))

# 3 (3) — qattiqlik turlari
q(3, "yuqori",
  "Suvda erigan qaysi tuz DOIMIY qattiqlikni yuzaga keltiradi?",
  "CaSO₄", [("Ca(HCO₃)₂", "gidrokarbonat — vaqtinchalik qattiqlik"),
             ("Mg(HCO₃)₂", "u ham vaqtinchalik"), ("NaCl", "Na⁺ qattiqlik bermaydi")],
  "Sulfat/xloridlar qaynatishda cho'kmaydi — doimiy qattiqlik: faqat kimyoviy usul yordam beradi.",
  dict(arch="doimiy_tuz"))

# 4 (3) — Al + ishqor
check("q4", 2.7/27*1.5*22.4, 3.36)
q(3, "yuqori",
  "2,7 g alyuminiy ORTIQCHA natriy gidroksid eritmasida eriganda qancha vodorod (n.sh.) ajraladi?",
  "3,36 L", [("0 L — Al ishqorda erimaydi", "Al amfoter: ishqorda ham eriydi!"),
              ("2,24 L", "H₂ koeffitsiyenti 3/2"), ("6,72 L", "ikki baravar ko'p")],
  "2Al + 2NaOH + 6H₂O → 2Na[Al(OH)₄] + 3H₂: n(H₂) = 0,15 → 3,36 L.",
  dict(arch="al_ishqor_hisob"))

# 5 (3) — RASMLI: qattiqlik egri
q(3, "yuqori",
  "Rasmda vaqtinchalik qattiq suvni qaynatishda erigan Ca(HCO₃)₂ miqdorining o'zgarishi berilgan. "
  "Kamayishning sababi qaysi reaksiya?",
  "Ca(HCO₃)₂ → CaCO₃↓ + H₂O + CO₂",
  [("Ca(HCO₃)₂ → CaO + ...", "oksid eritmada hosil bo'lmaydi"),
   ("Ca(HCO₃)₂ bug'lanib ketadi", "tuz bug'lanmaydi — parchalanadi"),
   ("Ca(HCO₃)₂ + O₂ → ...", "kislorod bilan reaksiya yo'q")],
  "Qizdirishda nordon tuz parchalanib, erimaydigan karbonat cho'kadi — «qasqon».",
  dict(arch="qattiqlik_egri_oqish"), fig="hardness_curve")

# 6 (3)
q(3, "yuqori",
  "Temirning xlor va xlorid kislota bilan reaksiyalarida qanday tuzlar hosil bo'ladi?",
  "Cl₂ bilan — FeCl₃; HCl bilan — FeCl₂",
  [("ikkalasida ham FeCl₃", "HCl kuchli oksidlovchi emas — +2 gacha"),
   ("ikkalasida ham FeCl₂", "erkin xlor kuchli oksidlovchi — +3 gacha"),
   ("Cl₂ bilan — FeCl₂; HCl bilan — FeCl₃", "teskari")],
  "2Fe + 3Cl₂ → 2FeCl₃; Fe + 2HCl → FeCl₂ + H₂ — oksidlovchi kuchiga bog'liq.",
  dict(arch="fe_cl2_hcl"))

# 7 (3) — 1-2-3: ishqorda eriydiganlar
q(3, "yuqori",
  "Qaysi moddalar ortiqcha NaOH eritmasida ERIYDI?\n"
  "1) Al;  2) Fe;  3) Zn(OH)₂;  4) Al₂O₃;  5) Cu.",
  "1, 3 va 4",
  [("1, 2 va 4", "Fe ishqorda erimaydi"), ("faqat 1", "amfoter Zn(OH)₂ va Al₂O₃ ham eriydi"),
   ("hammasi", "Fe va Cu — yo'q")],
  "Amfoterlar (Al, Zn birikmalari) ishqorda eriydi; Fe, Cu — erimaydi.",
  dict(arch="ishqorda_eriydigan"))

# 8 (2)
q(2, "yuqori",
  "Qattiq suvdan uzoq foydalanish maishiy texnikaga qanday zarar keltiradi?",
  "qizdirgichlarda qasqon o'sib, energiya isrofi va kuyish yuz beradi",
  [("hech qanday zarar yo'q", "TENlarning asosiy «dushmani» — qasqon"),
   ("suv rangini o'zgartiradi", "qattiqlik rangga ta'sir qilmaydi"),
   ("metallni eritib yuboradi", "aksincha — qatlam O'SADI")],
  "CaCO₃ qatlami issiqlikni yomon o'tkazadi: TEN qizib kuyadi, quvurlar torayadi.",
  dict(arch="qattiqlik_zarar"))

# 9 (3) — JADVAL moslash: ion ranglari
q(3, "yuqori",
  "Jadvaldagi kationlarni eritma rangi bilan TO'G'RI moslang:\n"
  "[JADVAL] Kation | Rang ;; a) Cu²⁺ | 1) och yashil ;; b) Fe²⁺ | 2) ko'k ;; c) Fe³⁺ | 3) sarg'ish-qo'ng'ir",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "Cu²⁺ — ko'k"), ("a—2, b—3, c—1", "Fe³⁺ — sarg'ish"),
   ("a—3, b—2, c—1", "moslashuvlar chalkash")],
  "Cu²⁺ ko'k; Fe²⁺ och yashil; Fe³⁺ sarg'ish-qo'ng'ir — d-metallarning «vizit kartasi».",
  dict(arch="ion_rang_jadval"))

# 10 (3) — alyumotermiya hisob
check("q10", 32/160*2*56, 22.4)
q(3, "yuqori",
  "Fe₂O₃ + 2Al → Al₂O₃ + 2Fe (alyumotermiya). 32 g temir(III) oksididan necha gramm temir olinadi? "
  "(M: Fe₂O₃=160, Fe=56)",
  "22,4 g", [("11,2 g", "koeffitsiyent 2 unutilgan"), ("32 g", "massa saqlanmaydi bu holda"),
              ("44,8 g", "ikki baravar ko'p")],
  "n = 0,2 mol → n(Fe) = 0,4 → m = 22,4 g.",
  dict(arch="termit_hisob"))

# 11 (3) — aralashma (ishqor bilan)
check("q11a", 3.36/22.4/1.5, 0.1); check("q11b", 10-2.7, 7.3)
q(3, "yuqori",
  "Al va Cu dan iborat 10 g aralashmaga ortiqcha NaOH eritmasi ta'sir ettirilganda 3,36 L (n.sh.) "
  "gaz ajraldi. Aralashmadagi mis massasini toping. (M(Al)=27)",
  "7,3 g", [("2,7 g", "bu Al massasi"), ("10 g", "Cu ishqorda erimaydi, lekin Al eridi-ku"),
             ("5 g", "asossiz yarim")],
  "Faqat Al eriydi: n(H₂) = 0,15 → n(Al) = 0,1 → 2,7 g → m(Cu) = 10 − 2,7 = 7,3 g.",
  dict(arch="al_cu_aralashma"))

# 12 (2)
q(2, "yuqori",
  "Yonayotgan magniyni SUV bilan o'chirish mumkin emas. Sababi nimada?",
  "qizigan Mg suv bilan reaksiyaga kirishib, yonuvchan H₂ ajratadi",
  [("suv magniyni sovutolmaydi", "gap sovutishda emas — kimyoviy xavfda"),
   ("magniy suvda eriydi", "erish emas, reaksiya boradi"),
   ("suv alangani kuchaytirmaydi ham, o'chirmaydi ham", "aksincha — portlash xavfini oshiradi")],
  "Mg + H₂O(bug') → MgO + H₂↑ — olov yanada avjlanadi. Quruq qum bilan o'chiriladi.",
  dict(arch="mg_suv_xavf"))

# 13 (3) — ohak usuli
q(3, "yuqori",
  "Vaqtinchalik qattiqlikni yo'qotishning «ohak usuli» qaysi reaksiyaga asoslangan?",
  "Ca(HCO₃)₂ + Ca(OH)₂ → 2CaCO₃↓ + 2H₂O",
  [("Ca(HCO₃)₂ + HCl → ...", "kislota qattiqlikni YO'QOTMAYDI, tuzni eritadi"),
   ("Ca(HCO₃)₂ + NaCl → ...", "reaksiya belgisi yo'q"),
   ("Ca(OH)₂ + CO₂ → ...", "bu ohakli suv sinovi, yumshatish emas")],
  "Hisoblangan miqdorda ohak qo'shilsa, barcha kalsiy karbonat holida cho'kadi.",
  dict(arch="ohak_usuli"))

# 14 (3) — JADVAL «?»: Fe darajalari
q(3, "yuqori",
  "Fe → FeCl₂ → Fe(OH)₂ → Fe(OH)₃ zanjiridagi temirning oksidlanish darajalarini jadvalga mos "
  "to'ldiring:\n[JADVAL] Modda | Fe darajasi ;; Fe | 0 ;; FeCl₂ | ? ;; Fe(OH)₂ | ? ;; Fe(OH)₃ | ?",
  "+2; +2; +3",
  [("+2; +3; +3", "Fe(OH)₂ da hali +2"), ("+3; +2; +3", "HCl bilan +2 hosil bo'ladi"),
   ("+2; +2; +2", "havoda oksidlanib +3 ga o'tadi")],
  "Fe(OH)₂ havo kislorodida qo'ng'ir Fe(OH)₃ ga o'tadi: 4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃.",
  dict(arch="fe_daraja_jadval"))

# 15 (3) — kristallogidrat
check("q15", 25/250*160, 16)
q(3, "yuqori",
  "25 g mis kuporosi (CuSO₄·5H₂O) tarkibidagi suvsiz tuz massasini toping. "
  "(M: CuSO₄·5H₂O=250, CuSO₄=160)",
  "16 g", [("25 g", "suv chegirilmagan"), ("9 g", "bu suv massasi"), ("8 g", "0,05 mol deb olingan")],
  "n = 0,1 mol → m(CuSO₄) = 16 g.",
  dict(arch="kuporos_hisob"))

# 16 (2)
q(2, "yuqori",
  "Po'lat bilan cho'yanning asosiy farqi nimada?",
  "uglerod miqdorida: po'latda 2 % dan kam, cho'yanda ko'p",
  [("po'latda temir yo'q", "ikkalasining asosi — temir"),
   ("cho'yan sof temir", "aksincha, C ko'proq"),
   ("po'lat — mis qotishmasi", "mis qotishmalari — bronza, latun")],
  "C kam — plastik po'lat; C ko'p (2–4 %) — qattiq, mo'rt cho'yan.",
  dict(arch="polat_choyan"))

# 17 (3)
check("q17", 8.1/27*1.5*22.4, 10.08)
q(3, "yuqori",
  "8,1 g alyuminiy ortiqcha ishqor eritmasida to'liq eridi. Ajralgan vodorod hajmini (n.sh.) toping. "
  "(M(Al)=27)",
  "10,08 L", [("6,72 L", "koeffitsiyent 3/2 unutilgan"), ("22,4 L", "1 mol uchun"),
               ("3,36 L", "0,1 mol Al uchun qiymat")],
  "n(Al) = 0,3 → n(H₂) = 0,45 mol → V = 10,08 L.",
  dict(arch="al_ishqor_katta"))

# 18 (2)
q(2, "yuqori",
  "Buyumlarni xromlash (Cr qoplash) qanday maqsadda qilinadi?",
  "korroziyadan himoya va qattiq yaltiroq yuza olish",
  [("massani oshirish uchun", "qoplama juda yupqa"),
   ("elektr o'tkazishni to'xtatish uchun", "Cr o'tkazgich"),
   ("faqat rang berish uchun", "asosiysi himoya va yeyilishga chidam")],
  "Xrom — qattiq, zanglamaydigan qoplama: santexnika, asboblar, detallar.",
  dict(arch="xromlash"))

# 19 (3) — RASMLI: alyumotermiya
q(3, "yuqori",
  "Rasmda alyumotermiya jarayoni: relslarni payvandlash uchun tigeldagi Fe₂O₃ + Al aralashmasi "
  "yondirilgan. Jarayonning qaysi xususiyati relslarni ulashga imkon beradi?",
  "reaksiya juda katta issiqlik berib, temir SUYUQ holda hosil bo'ladi",
  [("temir kukun holida hosil bo'ladi", "3000 °C atrofida — temir eriydi"),
   ("alyuminiy relslarni yelimlaydi", "Al oksidga o'tadi, «yelim» emas"),
   ("reaksiya sovuqda boradi", "aksincha — o'ta ekzotermik")],
  "Fe₂O₃ + 2Al → Al₂O₃ + 2Fe + Q: suyuq temir chokka quyilib, relslarni biriktiradi.",
  dict(arch="termit_oqish"), fig="termit")

# 20 (2)
q(2, "yuqori",
  "Rux qoplangan temir tunuka nima deb ataladi va qoplamaning vazifasi nima?",
  "galvanizatsiyalangan tunuka; temirni korroziyadan saqlaydi",
  [("bronza; bezak beradi", "bronza — qotishma, qoplama emas"),
   ("emal; issiqdan saqlaydi", "emal — oksid qoplama, rux emas"),
   ("nikel; magnitlaydi", "rux magnit xossa bermaydi")],
  "Zn faolroq — «qurbon qoplama»: tirnalganda ham avval rux yemiriladi.",
  dict(arch="galvanik_qoplama"))

# 21 (3) — qattiqlik hisob
check("q21", 0.005*1000*2, 10)
q(3, "yuqori",
  "1 L suvda 0,005 mol Ca²⁺ ioni bor. Suvning qattiqligini (mg-ekv/L) toping.",
  "10", [("5", "Ca²⁺ ikki zaryadli: mmol × 2"), ("2,5", "hisob teskari"),
          ("0,005", "birlik o'tkazilmagan")],
  "Qattiqlik = n(mmol/L) · zaryad = 5 · 2 = 10 mg-ekv/L — juda qattiq suv.",
  dict(arch="qattiqlik_hisob"))

# 22 (3) — 1-2-3: qaynatish bilan ketadiganlar
q(3, "yuqori",
  "Qaysi tuzlar keltirib chiqargan qattiqlik QAYNATISH bilan yo'qoladi?\n"
  "1) Ca(HCO₃)₂;  2) CaSO₄;  3) Mg(HCO₃)₂;  4) MgCl₂.",
  "1 va 3",
  [("2 va 4", "sulfat/xlorid — doimiy qattiqlik"), ("hammasi", "CaSO₄, MgCl₂ qaynatishda cho'kmaydi"),
   ("faqat 1", "Mg(HCO₃)₂ ham parchalanadi")],
  "Faqat gidrokarbonatlar termik parchalanadi — vaqtinchalik qattiqlik.",
  dict(arch="qaynatish_tanlov"))

# 23 (3) — aralashma
check("q23a", 2.24/22.4*56, 5.6); check("q23b", 12-5.6, 6.4)
q(3, "yuqori",
  "Fe va Cu dan iborat 12 g aralashma ortiqcha xlorid kislotaga solindi; 2,24 L (n.sh.) gaz ajraldi. "
  "Aralashmadagi mis massasini toping. (M(Fe)=56)",
  "6,4 g", [("5,6 g", "bu temir massasi"), ("12 g", "temir eridi-ku"), ("3,2 g", "asossiz yarim")],
  "Cu HCl da erimaydi: n(Fe) = n(H₂) = 0,1 → 5,6 g → m(Cu) = 6,4 g.",
  dict(arch="fe_cu_aralashma_b"))

# 24 (2)
q(2, "yuqori",
  "«So'ndirilgan» va «so'ndirilmagan» ohak mos ravishda qaysi moddalar?",
  "Ca(OH)₂ va CaO",
  [("CaO va Ca(OH)₂", "teskari"), ("CaCO₃ va CaO", "ohaktosh «ohak» emas"),
   ("Ca(OH)₂ va CaCO₃", "so'ndirilmagani — oksid")],
  "CaO + H₂O → Ca(OH)₂: suv bilan «so'ndiriladi».",
  dict(arch="ohak_nomlari"))

# 25 (3)
q(3, "yuqori",
  "Al(OH)₃ dan natriy alyuminat olish uchun qaysi reagent va shart kerak?",
  "NaOH bilan suyuqlantirish (yoki ortiqcha konsentrlangan ishqor)",
  [("suv bilan qaynatish", "suvda erimaydi"),
   ("HCl qo'shish", "kislota tuz (AlCl₃) beradi"),
   ("NaCl eritmasi", "neytral tuz bilan reaksiya yo'q")],
  "Al(OH)₃ + NaOH → NaAlO₂ + 2H₂O (suyuqlanma) — amfoterlikning «kislotali» tomoni.",
  dict(arch="alyuminat_olish"))

# 26 (3) — RASMLI: bar hisob
check("q26", 9/2, 4.5)
q(3, "yuqori",
  "Diagrammadagi quduq suvi (9 mg-ekv/L) ning 1 litrida necha mmol Ca²⁺ "
  "bo'lishi mumkin (barcha qattiqlik kalsiydan deb hisoblang)?",
  "4,5", [("9", "zaryadga bo'lish unutilgan"), ("18", "ko'paytirish emas, bo'lish kerak"),
           ("2,25", "yana ikkiga bo'lingan")],
  "mg-ekv = mmol · 2 → mmol = 9/2 = 4,5.",
  dict(arch="bar_qattiqlik_hisob_b"), fig="bar_hardness")

# 27 (3)
check("q27", 5.8/58*40, 4)
q(3, "yuqori",
  "Mg(OH)₂ → MgO + H₂O. 5,8 g magniy gidroksid to'liq parchalanganda qolgan qattiq modda massasini "
  "toping. (M: Mg(OH)₂=58, MgO=40)",
  "4 g", [("5,8 g", "suv uchib chiqadi"), ("1,8 g", "bu suv massasi"), ("2 g", "0,05 mol deb olingan")],
  "n = 0,1 mol → m(MgO) = 4 g.",
  dict(arch="mgoh2_parchalanish"))

# 28 (2) — RASMLI: egri o'qish
q(2, "yuqori",
  "5-savol grafigida egri nolga tushmay, past sathda TO'XTAB qoladi. Buning sababi nimada?",
  "doimiy qattiqlik tuzlari (CaSO₄, MgCl₂) qaynatishda cho'kmaydi",
  [("qaynatish yetarli emas edi", "qancha qaynatilmasin, sulfatlar cho'kmaydi"),
   ("suv tugab qoladi", "grafik konsentratsiya haqida"),
   ("asbob xatosi", "qonuniy hodisa — qattiqlik turi")],
  "Qaynatish faqat gidrokarbonatlarni yo'qotadi; qolgani — doimiy qattiqlik ulushi.",
  dict(arch="qoldiq_qattiqlik"), fig="hardness_curve")

# 29 (3)
check("q29", 0.1*2*80, 16)
q(3, "yuqori",
  "(CuOH)₂CO₃ → 2CuO + H₂O + CO₂. 0,1 mol malaxit to'liq parchalanganda hosil bo'lgan qora modda "
  "massasini toping. (M(CuO)=80)",
  "16 g", [("8 g", "koeffitsiyent 2 unutilgan"), ("80 g", "1 mol uchun"), ("32 g", "ikki baravar")],
  "n(CuO) = 0,2 mol → m = 16 g.",
  dict(arch="malaxit_hisob"))

# 30 (2)
q(2, "yuqori",
  "Xona haroratida SUYUQ holatda bo'lgan metall qaysi?",
  "simob (Hg)", [("qalay", "232 °C da suyuqlanadi"), ("qo'rg'oshin", "327 °C"),
                  ("galliy", "29,8 °C — kaftda eriydi, lekin xonada qattiq")],
  "Hg (t(suyuql.) = −39 °C) — termometrlarda ishlatilgan; bug'lari zaharli.",
  dict(arch="suyuq_metall"))

# 31 (3)
check("q31", 32.4/162*100, 20)
q(3, "yuqori",
  "Ca(HCO₃)₂ → CaCO₃ + H₂O + CO₂. 32,4 g kalsiy gidrokarbonat parchalanganda hosil bo'lgan cho'kma "
  "massasini toping. (M: Ca(HCO₃)₂=162, CaCO₃=100)",
  "20 g", [("32,4 g", "gazlar chiqib ketadi"), ("10 g", "0,1 mol deb olingan"), ("40 g", "ikki baravar")],
  "n = 0,2 mol → m(CaCO₃) = 20 g.",
  dict(arch="gidrokarbonat_hisob"))

# 32 (3) — RASMLI: termit hisob
check("q32", 5.4/27*56, 11.2)
q(3, "yuqori",
  "19-savol jarayonida 5,4 g alyuminiy kukuni to'liq sarflandi. Hosil bo'lgan temir massasini toping. "
  "(Fe₂O₃ + 2Al → Al₂O₃ + 2Fe; M: Al=27, Fe=56)",
  "11,2 g", [("5,6 g", "nisbat 2:2 = 1:1"), ("22,4 g", "ikki baravar"), ("5,4 g", "M lar farqli")],
  "n(Al) = 0,2 → n(Fe) = 0,2 mol → m = 11,2 g.",
  dict(arch="termit_hisob_rasm"), fig="termit")

# ---------- Y2: uch kation ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.4",
  ichki_pasport=[dict(n=33, element="II.4", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="II.4", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="II.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch rangli eritma bor: X — ko'k; Y — sarg'ish-qo'ng'ir; Z — rangsiz, alangani "
               "g'isht-qizil rangga bo'yaydi. Eritmalar CuSO₄, FeCl₃ va CaCl₂ ekani ma'lum. "
               "33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X eritmadagi tuz qaysi?",
    "34. Y ga ishqor qo'shilganda qanday cho'kma tushadi?",
    "35. Z eritmaga Na₂CO₃ qo'shilsa nima kuzatiladi?"],
  javoblar_royxati=["A) CuSO₄", "B) qo'ng'ir Fe(OH)₃", "C) oq cho'kma (CaCO₃)",
                    "D) FeCl₃", "E) ko'k Cu(OH)₂", "F) gaz ajralishi"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="sarg'ish rang — FeCl₃ (Y); ko'k esa mis tuzi"),
                   dict(variant="E", xato="ko'k cho'kma X dan tushadi, Y dan emas"),
                   dict(variant="F", xato="tuz + tuz almashinishida gaz emas, cho'kma kuzatiladi")],
  yechim=("Ko'k — CuSO₄ (A). Y (FeCl₃) + ishqor → Fe(OH)₃↓ qo'ng'ir (B). "
          "Z (CaCl₂) + Na₂CO₃ → CaCO₃↓ oq (C)."),
  parametrlar=dict(arch="uch_kation_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", (24*0.25-5.1)/(36-27), 0.1, tol=0.001)
check("o36b", 0.1*27, 2.7)
check("o37", 11.2/56/2*160, 16)
check("o38", 16/160*2*127, 25.4)
check("o39", 0.081/162*1000*2, 1)
check("o40a", 3.36/22.4/1.5, 0.1); check("o40b", 8.3-2.7, 5.6)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Mg va Al dan iborat 5,1 g aralashma ortiqcha xlorid kislotada eritilganda 5,6 L (n.sh.) "
            "vodorod ajraldi. Aralashmadagi alyuminiy massasini (g) toping. (M: Mg=24, Al=27)",
      javob="2,7", yechim="24x+27y = 5,1; x+1,5y = 0,25 → 9y = 0,9 → y = 0,1 mol → m(Al) = 2,7 g.",
      parametrlar=dict(arch="mg_al_aralashma_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="Fe → FeCl₃ → Fe(OH)₃ → Fe₂O₃ zanjiri bo'yicha 11,2 g temirdan (yo'qotishsiz) olingan "
            "temir(III) oksid massasini (g) toping. (M: Fe=56, Fe₂O₃=160)",
      javob="16", yechim="n(Fe) = 0,2 → n(Fe₂O₃) = 0,1 mol → m = 16 g.",
      parametrlar=dict(arch="fe_zanjir_o1")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayon bo'yicha 16 g Fe₂O₃ dan alyumotermiya orqali olingan temir to'liq "
            "xlorid kislotada eritildi. Hosil bo'lgan tuz massasini (g) toping. (M: Fe₂O₃=160, FeCl₂=127)",
      javob="25,4", yechim="n(Fe) = 0,2 → FeCl₂ 0,2 mol → m = 25,4 g.",
      parametrlar=dict(arch="sxema_termit_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="1 L quduq suvida 0,081 g Ca(HCO₃)₂ erigan. Suvning qattiqligini (mg-ekv/L) toping. "
            "(M(Ca(HCO₃)₂)=162)",
      javob="1", yechim="n = 0,5 mmol → qattiqlik = 0,5 · 2 = 1 mg-ekv/L.",
      parametrlar=dict(arch="qattiqlik_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Al va Fe dan iborat 8,3 g aralashmaga ortiqcha NaOH eritmasi ta'sir ettirilganda 3,36 L "
            "(n.sh.) gaz ajraldi. Aralashmadagi temir massasini (g) toping. (M(Al)=27)",
      javob="5,6", yechim="Ishqorda faqat Al eriydi: n(H₂)=0,15 → n(Al)=0,1 → 2,7 g → m(Fe) = 5,6 g.",
      parametrlar=dict(arch="al_fe_ishqor_zanjir")),
]

# ---------- O2 ----------
check("o41b", 0.324/162*1000*2/1000*1000, 4, tol=0.5)
check("o41c", 0.002*100, 0.2)
check("o43d", 0.1*98, 9.8)
O2 = [
 dict(n=41, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Quduq suvining 1 litrida 0,324 g Ca(HCO₃)₂ erigan. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Bu qanday turdagi qattiqlik? Sababi bilan yozing.",
             yechim=["Vaqtinchalik (karbonatli) — gidrokarbonat qaynatishda parchalanadi."], M=3, A=2),
        dict(savol="b) Suvning qattiqligini (mg-ekv/L) hisoblang. (M(Ca(HCO₃)₂)=162)",
             yechim=["n = 0,324/162 = 2 mmol → qattiqlik = 2·2 = 4 mg-ekv/L."], M=4, A=3),
        dict(savol="c) 1 L suv qaynatilganda hosil bo'ladigan cho'kma massasini toping. (M(CaCO₃)=100)",
             yechim=["Ca(HCO₃)₂ → CaCO₃↓: n = 2 mmol → m = 0,2 g."], M=5, A=3),
        dict(savol="d) Agar suvda CaSO₄ ham bo'lsa, uni qanday yo'qotish mumkin?",
             yechim=["Soda qo'shish: Ca²⁺ + CO₃²⁻ → CaCO₃↓ (yoki ion almashinuvchi filtrlar)."], M=3, A=2),
      ],
      rasmiylashtirish="Qattiqlik zanjiri: tur → mg-ekv → cho'kma → doimiy usul; M15+A10.",
      parametrlar=dict(arch="qattiqlik_o2_zanjir")),
 dict(n=42, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Alyumotermiya jarayoni tahlil qilinadi: Fe₂O₃ + 2Al → Al₂O₃ + 2Fe. Quyidagilarni "
            "MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega alyuminiy temirni uning oksididan siqib chiqara oladi? Jarayonning "
                   "ekzotermikligi nimadan dalolat beradi? Batafsil tushuntiring.",
             yechim=["Al faollik qatorida Fe dan oldin — kislorodga «ochroq»: Al₂O₃ ning hosil bo'lish",
                     "issiqligi juda katta. Farq issiqlik sifatida ajraladi — harorat ~3000 °C ga yetadi."], M=13, A=0),
        dict(savol="b) Nega aralashma o'z-o'zidan yonib ketmaydi — maxsus yondirgich kerak?",
             yechim=["Aktivlanish energiyasi yuqori: jarayonni boshlash uchun mahalliy qizdirish kerak."], M=9, A=0),
        dict(savol="c) Alyumotermiyaning bitta amaliy qo'llanilishini yozing.",
             yechim=["Relslarni payvandlash (yoki qiyin qaytariladigan metallar — Cr, Mn olish)."], M=3, A=0),
      ],
      rasmiylashtirish="Termit-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="termit_mulohaza")),
 dict(n=43, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Uch eritma jadvalda berilgan:\n"
            "[JADVAL] № | Eritma ;; 1 | CuSO₄ ;; 2 | FeCl₃ ;; 3 | CaCl₂\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir eritmaning rangini yozing.",
             yechim=["CuSO₄ — ko'k; FeCl₃ — sarg'ish-qo'ng'ir; CaCl₂ — rangsiz."], M=4, A=2),
        dict(savol="b) Har biriga NaOH qo'shilganda nima kuzatilishini tenglamalar bilan yozing.",
             yechim=["Cu(OH)₂↓ ko'k; Fe(OH)₃↓ qo'ng'ir; CaCl₂ bilan suyultirilgan eritmada deyarli "
                     "o'zgarish yo'q (Ca(OH)₂ o'rtacha eriydi)."], M=4, A=3),
        dict(savol="c) 3-eritmadagi kationni qanday aniqlash mumkin?",
             yechim=["Alanga testi (g'isht-qizil) yoki Na₂CO₃ bilan oq cho'kma."], M=4, A=2),
        dict(savol="d) 0,1 mol CuSO₄ dan olinadigan Cu(OH)₂ massasini hisoblang. (M(Cu(OH)₂)=98)",
             yechim=["n = 0,1 mol → m = 9,8 g."], M=3, A=3),
      ],
      rasmiylashtirish="Kation-tahlil: rang → cho'kma → sinov → hisob; M15+A10.",
      parametrlar=dict(arch="kation_tahlil_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261405)
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
    d = dict(n=n, tur="Y1", element="II.4", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II4-B", daraja="B", bob=14, bob_nomi="IIA, IIIA va d-metallar. Suv qattiqligi",
    manba=("Tongotarov/DTM metallar banki arxetiplari (noma'lum metall, ishqorda eriydigan aralashma, "
           "alyumotermiya, qattiqlik hisoblari) va Spectrum uslubidagi 36–43 — javoblar mustaqil "
           "tekshirilgan; MS spetsifikatsiyasi II.4"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: amfoter alyuminiy, temir zanjirlari, mg-ekv "
          "hisoblari, alyumotermiya."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
