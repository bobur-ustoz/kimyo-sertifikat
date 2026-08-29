# -*- coding: utf-8 -*-
"""11-bob B-varianti: Anorganik moddalar sinflari va genetik bog'lanish (II.1) — HAQIQIY MS MUHITI ★★★.
Sinflarga ajratish, nordon/asosli tuzlar, amfoterlik, genetik zanjirlar, aralashma hisoblari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_II1B.json"
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

# 1 (3) — sinflarga mos formulalar
q(3, "yuqori",
  "Quyidagi sinflarga mos moddalar TO'G'RI ko'rsatilgan javobni toping: "
  "1) o'rta tuz; 2) nordon tuz; 3) asosli tuz.",
  "1—K₂S; 2—NaHSO₃; 3—(CuOH)₂CO₃",
  [("1—NaHS; 2—K₂SO₃; 3—CuCO₃", "NaHS — nordon, K₂SO₃ — o'rta, CuCO₃ — o'rta"),
   ("1—K₂S; 2—(CuOH)₂CO₃; 3—NaHSO₃", "2 va 3 o'rni almashgan"),
   ("1—KOH; 2—NaHSO₃; 3—CuS", "KOH tuz emas — asos")],
  "O'rta: H ham, OH ham yo'q (K₂S); nordon: H saqlangan (NaHSO₃); asosli: OH saqlangan ((CuOH)₂CO₃).",
  dict(arch="sinf_mos_tanlov"))

# 2 (3) — necha xil tuz
q(3, "yuqori",
  "KOH va H₃PO₄ o'zaro reaksiyasidan jami necha XIL tuz hosil bo'lishi mumkin?",
  "3", [("1", "kislota uch negizli — H bosqichma-bosqich almashadi"),
         ("2", "KH₂PO₄, K₂HPO₄ VA K₃PO₄ — uchtasi ham bor"),
         ("4", "KOH bir kislotali asos — asosli tuz bermaydi")],
  "KH₂PO₄, K₂HPO₄ (nordon) va K₃PO₄ (o'rta) — negizlilik nechta bo'lsa, tuz shuncha xil.",
  dict(arch="necha_tuz"))

# 3 (3) — amfoter qator
q(3, "yuqori",
  "Qaysi qatorda FAQAT amfoter oksidlar berilgan?",
  "Al₂O₃, ZnO, Cr₂O₃",
  [("Al₂O₃, Na₂O, ZnO", "Na₂O — asosli"),
   ("ZnO, CO₂, BeO", "CO₂ — kislotali"),
   ("CrO₃, ZnO, Al₂O₃", "CrO₃ — kislotali (yuqori daraja)")],
  "Amfoterlar: BeO, ZnO, Al₂O₃, Cr₂O₃, PbO... — ham kislota, ham ishqor bilan reaksiyaga kirishadi.",
  dict(arch="amfoter_qator"))

# 4 (3) — oksidni eritish
check("q4", 10.2/102*6, 0.6)
q(3, "yuqori",
  "10,2 g alyuminiy oksidini to'liq eritish uchun necha mol xlorid kislota kerak? (M(Al₂O₃)=102)",
  "0,6", [("0,3", "Al₂O₃ + 6HCl — koeffitsiyent 6"), ("0,2", "mol soni bilan adashuv"),
           ("0,1", "bu oksidning o'zi")],
  "Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O: n(oksid) = 0,1 mol → n(HCl) = 0,6 mol.",
  dict(arch="al2o3_hcl"))

# 5 (3) — RASMLI: amfoter grafik
q(3, "yuqori",
  "Rasmda AlCl₃ eritmasiga NaOH tomchilab qo'shilganda cho'kma massasining o'zgarishi berilgan. "
  "Cho'kmaning ortib borib, so'ng ERIB ketishining sababi nimada?",
  "Al(OH)₃ amfoter — ortiqcha ishqorda erib ketadi",
  [("cho'kma qizdirilib parchalanadi", "harorat emas, ishqor miqdori o'zgaryapti"),
   ("NaOH cho'kmani yuvib yuboradi", "mexanik emas — kimyoviy erish: aluminat hosil bo'ladi"),
   ("AlCl₃ tugab qoladi", "tugasa cho'kma o'zgarmay qolardi, kamaymasdi")],
  "Avval AlCl₃ + 3NaOH → Al(OH)₃↓; so'ng Al(OH)₃ + NaOH → Na[Al(OH)₄] — cho'kma eriydi.",
  dict(arch="aloh_grafik"), fig="aloh")

# 6 (3)
q(3, "yuqori",
  "Qaysi juftlik o'zaro reaksiyaga KIRISHMAYDI?",
  "CO₂ va SO₃",
  [("CaO va CO₂", "asosli + kislotali → CaCO₃"),
   ("ZnO va NaOH", "amfoter + ishqor → sinkat"),
   ("K₂O va H₂O", "faol metall oksidi ishqor beradi")],
  "Ikkala oksid ham kislotali — bir-biri bilan tuz hosil qila olmaydi.",
  dict(arch="kirishmaydigan_juft"))

# 7 (3) — 1-2-3: HCl bilan reaksiya
q(3, "yuqori",
  "Quyidagi moddalarning qaysilari xlorid kislota bilan reaksiyaga kirishadi?\n"
  "1) Ag;  2) MgO;  3) Na₂CO₃;  4) SiO₂;  5) Fe(OH)₃.",
  "2, 3 va 5",
  [("1, 2 va 3", "Ag faollik qatorida H dan keyin — kirishmaydi"),
   ("2, 4 va 5", "SiO₂ kislotali oksid — HCl bilan reaksiya yo'q"),
   ("hammasi", "Ag va SiO₂ kirishmaydi")],
  "HCl bilan: asosli oksid (MgO), tuz (Na₂CO₃ — gaz chiqadi), erimaydigan asos (Fe(OH)₃).",
  dict(arch="hcl_tanlov123"))

# 8 (2)
q(2, "yuqori",
  "NaHS tuzining to'g'ri nomini ko'rsating.",
  "natriy gidrosulfid",
  [("natriy sulfid", "bu Na₂S"), ("natriy sulfat", "bu Na₂SO₄"),
   ("natriy gidrosulfat", "bu NaHSO₄")],
  "Nordon tuzlarda «gidro-» old qo'shimchasi H ni bildiradi: NaHS — gidrosulfid.",
  dict(arch="nordon_nom"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi oksidlarni turlari bilan TO'G'RI moslang:\n"
  "[JADVAL] Oksid | Tur ;; a) CO | 1) asosli ;; b) CaO | 2) kislotali ;; c) Mn₂O₇ | 3) befarq",
  "a—3, b—1, c—2",
  [("a—2, b—1, c—3", "CO tuz hosil qilmaydi — befarq"),
   ("a—3, b—2, c—1", "CaO — tipik asosli oksid"),
   ("a—1, b—3, c—2", "moslashuvlar chalkash")],
  "CO — befarq; CaO — asosli; Mn₂O₇ — kislotali (HMnO₄ ga mos).",
  dict(arch="oksid_moslash_jadval"))

# 10 (3)
q(3, "yuqori",
  "Qaysi birikmada metall atomlari soni bilan kislota qoldiqlari soni 2:1 nisbatda?",
  "natriy sulfat",
  [("alyuminiy sulfat", "Al₂(SO₄)₃ — 2:3"), ("kalsiy fosfat", "Ca₃(PO₄)₂ — 3:2"),
   ("kaliy nitrat", "KNO₃ — 1:1")],
  "Na₂SO₄: 2 ta Na va 1 ta SO₄ — 2:1.",
  dict(arch="nisbat_tanlov"))

# 11 (3) — aralashma
check("q11a", 2.24/22.4*100, 10); check("q11b", 15.6-10, 5.6)
q(3, "yuqori",
  "CaCO₃ va CaO dan iborat 15,6 g aralashma qizdirilganda 2,24 L (n.sh.) CO₂ ajraldi. "
  "Boshlang'ich aralashmadagi CaO massasini toping. (M(CaCO₃)=100)",
  "5,6 g", [("10 g", "bu CaCO₃ massasi"), ("4,4 g", "bu ajralgan CO₂ massasi"),
             ("7,8 g", "hisob xato")],
  "n(CO₂) = 0,1 mol → m(CaCO₃) = 10 g → m(CaO) = 15,6 − 10 = 5,6 g.",
  dict(arch="aralashma_caco3"))

# 12 (2)
q(2, "yuqori",
  "Qaysi qatorda BEFARQ (tuz hosil qilmaydigan) oksidlar berilgan?",
  "CO, NO, N₂O",
  [("CO₂, NO₂, SO₂", "bular kislotali"), ("CaO, CO, NO", "CaO — asosli"),
   ("ZnO, NO, CO", "ZnO — amfoter")],
  "CO, NO, N₂O, SiO — kislota ham, ishqor bilan ham tuz bermaydi.",
  dict(arch="befarq_qator"))

# 13 (3)
q(3, "yuqori",
  "Qaysi tuzning termik parchalanishidan KISLOTALI oksid hosil bo'ladi?",
  "CaCO₃", [("NaNO₃", "NaNO₂ + O₂ — kislotali oksid yo'q"), ("NH₄NO₂", "N₂ + H₂O beradi"),
             ("NaCl", "termik barqaror — parchalanmaydi")],
  "CaCO₃ → CaO + CO₂: kislotali oksid — CO₂.",
  dict(arch="termik_parchalanish"))

# 14 (3) — JADVAL «?»: amfoterlik
q(3, "yuqori",
  "ZnO ning ikki xil reaksiyasi jadvalda berilgan. «?» o'rnidagi mahsulotlarni aniqlang:\n"
  "[JADVAL] Reaksiya | Tuz ;; ZnO + 2HCl | ? ;; ZnO + 2NaOH (suyuqlanma) | ?",
  "ZnCl₂; Na₂ZnO₂",
  [("ZnCl₂; NaZnOH", "sinkat formulasi Na₂ZnO₂"), ("ZnH₂; Na₂ZnO₂", "kislota bilan tuz ZnCl₂"),
   ("Zn(OH)₂; NaOH", "mahsulotlar tuz bo'lishi kerak")],
  "Kislota bilan: ZnCl₂ + H₂O; ishqor suyuqlanmasi bilan: Na₂ZnO₂ (natriy sinkat) + H₂O.",
  dict(arch="zno_jadval"))

# 15 (3)
check("q15a", 4.9/98, 0.05); check("q15b", 4/40, 0.1)
q(3, "yuqori",
  "4,9 g H₂SO₄ ga 4 g NaOH qo'shildi. Reaksiya natijasida qanday tuz hosil bo'ladi?",
  "Na₂SO₄ (o'rta tuz)",
  [("NaHSO₄ (nordon tuz)", "NaOH:H₂SO₄ = 0,1:0,05 = 2:1 — to'liq neytrallanish"),
   ("ikkala tuz aralashmasi", "ishqor aynan yetarli — faqat o'rta tuz"),
   ("tuz hosil bo'lmaydi", "kislota + ishqor doim tuz beradi")],
  "n(H₂SO₄)=0,05; n(NaOH)=0,1 → nisbat 1:2 → H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O.",
  dict(arch="nisbat_tuz_turi"))

# 16 (2)
q(2, "yuqori",
  "Qaysi qatorda FAQAT ishqorlar berilgan?",
  "NaOH, KOH, Ba(OH)₂",
  [("NaOH, Cu(OH)₂, KOH", "Cu(OH)₂ erimaydi"), ("Ca(OH)₂, Fe(OH)₂, LiOH", "Fe(OH)₂ erimaydi"),
   ("KOH, Al(OH)₃, NaOH", "Al(OH)₃ — erimaydigan amfoter gidroksid")],
  "Ishqorlar: I A metallari va Ca, Sr, Ba gidroksidlari.",
  dict(arch="ishqor_qator"))

# 17 (3)
q(3, "yuqori",
  "Fe → FeCl₂ → Fe(OH)₂ → FeO zanjirida 2-o'tish (FeCl₂ → Fe(OH)₂) uchun qaysi reagent kerak?",
  "NaOH eritmasi",
  [("H₂O", "FeCl₂ suv bilan gidroksid bermaydi"), ("HCl", "kislota gidroksidni ERITADI"),
   ("O₂", "oksidlanish boshqa mahsulot beradi")],
  "FeCl₂ + 2NaOH → Fe(OH)₂↓ + 2NaCl: tuz + ishqor → erimaydigan asos.",
  dict(arch="zanjir_reagent"))

# 18 (2)
q(2, "yuqori",
  "SO₄ kislota qoldig'ining valentligi qanday?",
  "II", [("I", "H₂SO₄ da 2 ta H bor"), ("IV", "oltingugurt darajasi bilan adashuv"),
          ("VI", "S ning darajasi VI, qoldiq valentligi emas")],
  "Qoldiq valentligi = almashingan H soni: H₂SO₄ → SO₄ (II).",
  dict(arch="qoldiq_valentlik"))

# 19 (3) — RASMLI: ohakli suv apparati
q(3, "yuqori",
  "Rasmdagi asbobda CO₂ ohakli suvdan o'tkazilmoqda: eritma avval loyqalanadi, gaz UZOQ o'tkazilsa "
  "yana tiniqlashadi. Tiniqlashish sababini ko'rsating.",
  "CaCO₃ ortiqcha CO₂ da eriydigan Ca(HCO₃)₂ ga aylanadi",
  [("CaCO₃ cho'kmaga tushib bo'ldi", "cho'kma yo'qolyapti — bu erish"),
   ("suv bug'lanib ketadi", "haroratsiz jarayon"),
   ("CO₂ eritmani suyultiradi", "gaz kimyoviy reaksiyaga kirishadi")],
  "CaCO₃ + CO₂ + H₂O → Ca(HCO₃)₂: o'rta tuz nordon (eriydigan) tuzga o'tadi.",
  dict(arch="limewater_oqish"), fig="limewater")

# 20 (2)
q(2, "yuqori",
  "Quyidagilardan qaysi biri OKSID hisoblanmaydi?",
  "H₂O₂", [("H₂O", "vodorod oksidi"), ("Fe₃O₄", "aralash oksid (FeO·Fe₂O₃)"),
            ("N₂O₅", "azot(V) oksidi")],
  "H₂O₂ — peroksid: unda −O−O− bog' bor, kislorod darajasi −1.",
  dict(arch="oksid_emas"))

# 21 (3)
check("q21a", 11.2/22.4, 0.5); check("q21b", 0.5*106, 53)
q(3, "yuqori",
  "11,2 L (n.sh.) CO₂ 1 mol NaOH li eritmadan o'tkazildi. Hosil bo'lgan tuzning massasini toping. "
  "(M(Na₂CO₃)=106)",
  "53 g", [("42 g", "NaHCO₃ deb olingan — ishqor ikki barobar ortiq"), ("106 g", "1 mol tuz uchun"),
            ("84 g", "NaHCO₃ 1 mol massasi")],
  "n(CO₂)=0,5; NaOH:CO₂ = 2:1 → o'rta tuz: Na₂CO₃ 0,5 mol → 53 g.",
  dict(arch="co2_naoh_hisob"))

# 22 (3) — 1-2-3: suv bilan reaksiya
q(3, "yuqori",
  "Qaysi oksidlar suv bilan reaksiyaga kirishadi?\n"
  "1) K₂O;  2) SiO₂;  3) SO₃;  4) CuO;  5) BaO.",
  "1, 3 va 5",
  [("1, 2 va 3", "SiO₂ suvda erimaydi (kislotali bo'lsa ham)"),
   ("3, 4 va 5", "CuO suv bilan birikmaydi"),
   ("hammasi", "SiO₂ va CuO kirishmaydi")],
  "Suv bilan: faol metall oksidlari (K₂O, BaO) va ko'pchilik kislotali oksidlar (SO₃); SiO₂ — istisno.",
  dict(arch="suv_tanlov123"))

# 23 (3) — aralashma
check("q23a", 2.24/22.4*106, 10.6); check("q23b", 20-10.6, 9.4)
q(3, "yuqori",
  "Na₂CO₃ va NaCl dan iborat 20 g aralashmaga ortiqcha HCl qo'shilganda 2,24 L (n.sh.) gaz ajraldi. "
  "Aralashmadagi NaCl massasini toping. (M(Na₂CO₃)=106)",
  "9,4 g", [("10,6 g", "bu Na₂CO₃ massasi"), ("4,4 g", "bu CO₂ massasi"),
             ("15,6 g", "hisob xato")],
  "n(CO₂) = 0,1 mol → m(Na₂CO₃) = 10,6 g → m(NaCl) = 20 − 10,6 = 9,4 g.",
  dict(arch="aralashma_na2co3"))

# 24 (2)
q(2, "yuqori",
  "Tabiiy mineral malaxit (CuOH)₂CO₃ qaysi tuzlar sinfiga kiradi?",
  "asosli tuz", [("o'rta tuz", "tarkibida OH guruhi bor"), ("nordon tuz", "H emas, OH saqlangan"),
                  ("qo'sh tuz", "bitta metall — qo'sh emas")],
  "Asosli tuz: OH guruhi saqlangan — (CuOH)₂CO₃.",
  dict(arch="asosli_misol"))

# 25 (3) — 1-2-3: negizlilik
q(3, "yuqori",
  "Ikki negizli kislotalarni toping:\n1) H₂S;  2) H₃PO₄;  3) H₂CO₃;  4) HNO₃;  5) H₃BO₃.",
  "1 va 3",
  [("2 va 5", "bular uch negizli"), ("1, 3 va 4", "HNO₃ — bir negizli"),
   ("3 va 4", "H₂S ham ikki negizli, HNO₃ emas")],
  "Ikki negizli: H₂S, H₂CO₃ (2 ta almashinuvchi H).",
  dict(arch="negiz_tanlov123"))

# 26 (3) — RASMLI: o'g'it hisobi
check("q26", 500*0.21, 105)
q(3, "yuqori",
  "Diagrammadagi ma'lumotdan foydalaning: 500 kg ammoniy sulfat ((NH₄)₂SO₄) tarkibidagi azot "
  "massasini toping.",
  "105 kg", [("21 kg", "100 kg uchun qiymat"), ("175 kg", "NH₄NO₃ ulushi olingan"),
              ("70 kg", "KNO₃ ulushi olingan")],
  "Diagrammadan ω(N) = 21 % → m = 500 · 0,21 = 105 kg.",
  dict(arch="bar_ogit_hisob_b"), fig="bar_ogit")

# 27 (3)
check("q27", 9.8/98*3*56, 16.8)
q(3, "yuqori",
  "9,8 g ortofosfat kislotani TO'LIQ neytrallash uchun necha gramm KOH kerak? (M: H₃PO₄=98, KOH=56)",
  "16,8 g", [("5,6 g", "koeffitsiyent 3 unutilgan"), ("11,2 g", "ikki negizli deb olingan"),
              ("33,6 g", "ikki baravar ko'p")],
  "H₃PO₄ + 3KOH → K₃PO₄ + 3H₂O: n = 0,1 → KOH 0,3 mol → 16,8 g.",
  dict(arch="h3po4_koh"))

# 28 (2) — RASMLI: grafik o'qish
q(2, "yuqori",
  "5-savol grafigidagi KO'TARILISH qismida qanday reaksiya boradi?",
  "AlCl₃ + 3NaOH → Al(OH)₃↓ + 3NaCl",
  [("Al(OH)₃ + NaOH → Na[Al(OH)₄]", "bu — pasayish (erish) qismi"),
   ("AlCl₃ + H₂O → gidroliz", "grafik ishqor qo'shilishiga oid"),
   ("NaOH + HCl → NaCl + H₂O", "eritmada erkin HCl yo'q")],
  "Cho'kma ortishi — Al(OH)₃ hosil bo'lish bosqichi.",
  dict(arch="aloh_kotarilish"), fig="aloh")

# 29 (3) — oksid formulasidan metall
check("q29", 16/0.2 - 16, 64)
q(3, "yuqori",
  "Ikki valentli metall oksidi (MeO) tarkibida 20 % kislorod bor. Metallni aniqlang.",
  "Cu", [("Mg", "MgO da ω(O) = 40 %"), ("Ca", "CaO da 28,6 %"), ("Zn", "ZnO da 19,75 % — yaqin, lekin M=65")],
  "16/(M+16) = 0,2 → M + 16 = 80 → M = 64 — mis.",
  dict(arch="oksid_metall_topish"))

# 30 (2)
q(2, "yuqori",
  "K₂HPO₄ tuzining to'g'ri nomini ko'rsating.",
  "kaliy gidrofosfat",
  [("kaliy fosfat", "bu K₃PO₄"), ("kaliy digidrofosfat", "bu KH₂PO₄"),
   ("kaliy fosfit", "fosfit — H₃PO₃ tuzi")],
  "Bitta H qolgan → «gidro-»: K₂HPO₄ — kaliy gidrofosfat.",
  dict(arch="tuz_nomlash"))

# 31 (3)
check("q31", 8/40*74, 14.8)
q(3, "yuqori",
  "Ca → CaO → Ca(OH)₂ zanjiri bo'yicha 8 g kalsiydan (yo'qotishsiz) necha gramm gidroksid olinadi? "
  "(M: Ca=40, Ca(OH)₂=74)",
  "14,8 g", [("8 g", "massa ortadi — O va H₂O qo'shiladi"), ("7,4 g", "0,1 mol deb olingan"),
              ("29,6 g", "ikki baravar ko'p")],
  "n(Ca) = 0,2 mol → n(Ca(OH)₂) = 0,2 mol → m = 14,8 g.",
  dict(arch="ca_zanjir_hisob"))

# 32 (3) — RASMLI: grafik hisob
check("q32", 7.8/78, 0.1)
q(3, "yuqori",
  "5-savol grafigida cho'kma maksimal nuqtada 7,8 g bo'lgan. Bu necha mol Al(OH)₃? (M(Al(OH)₃)=78)",
  "0,1", [("0,78", "molyar massaga bo'linmagan"), ("1", "7,8 g — 1 mol emas"),
           ("0,2", "ikki baravar ko'p")],
  "n = 7,8/78 = 0,1 mol.",
  dict(arch="aloh_hisob"), fig="aloh")

# ---------- Y2: uch oksid ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.1",
  ichki_pasport=[dict(n=33, element="II.1", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="II.1", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="II.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch oksid berilgan: X — suvda erib ishqor beradi; Y — ham kislota, ham ishqor bilan "
               "reaksiyaga kirishadi; Z — suv bilan uch negizli kislota beradi. Oksidlar Na₂O, ZnO va "
               "P₂O₅ ekani ma'lum. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Y oksid qaysi modda?",
    "34. X ning suv bilan reaksiya mahsuloti qaysi?",
    "35. Z dan olinadigan kislota qaysi?"],
  javoblar_royxati=["A) ZnO", "B) NaOH", "C) H₃PO₄", "D) P₂O₅", "E) Na₂CO₃", "F) H₃PO₃"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="P₂O₅ — Z, u amfoter emas, kislotali"),
                   dict(variant="E", xato="Na₂O + H₂O ishqor beradi, karbonat emas"),
                   dict(variant="F", xato="P₂O₅ dan H₃PO₄ (fosfat), H₃PO₃ emas")],
  yechim=("Y — amfoter ZnO (A). X — Na₂O: Na₂O + H₂O → 2NaOH (B). "
          "Z — P₂O₅: P₂O₅ + 3H₂O → 2H₃PO₄ (C)."),
  parametrlar=dict(arch="uch_oksid_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 4.48/22.4, 0.2); check("o36b", 12.4-0.2*24, 7.6)
check("o37", 13/65*81, 16.2)
check("o38", 20/40*100, 50)
check("o39", 8/40*84, 16.8)
check("o40a", 15.2-0.3*40, 3.2); check("o40b", 3.2/16*56, 11.2)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Mg va MgO dan iborat 12,4 g aralashma ortiqcha xlorid kislotada eritilganda 4,48 L (n.sh.) "
            "vodorod ajraldi. Aralashmadagi MgO massasini (g) toping. (M: Mg=24, MgO=40)",
      javob="7,6", yechim="H₂ faqat Mg dan: n(Mg) = 0,2 mol → 4,8 g → m(MgO) = 12,4 − 4,8 = 7,6 g.",
      parametrlar=dict(arch="aralashma_mg_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="Zn → ZnCl₂ → Zn(OH)₂ → ZnO zanjiri bo'yicha 13 g ruxdan (yo'qotishsiz) olingan ZnO "
            "massasini (g) toping. (M: Zn=65, ZnO=81)",
      javob="16,2", yechim="n(Zn) = 0,2 mol → n(ZnO) = 0,2 mol → m = 0,2·81 = 16,2 g.",
      parametrlar=dict(arch="zn_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi zanjir bo'yicha 20 g kalsiydan (yo'qotishsiz) oxirida olinadigan CaCO₃ "
            "massasini (g) toping. (M: Ca=40, CaCO₃=100)",
      javob="50", yechim="n(Ca) = 0,5 mol → har bosqichda 1:1 → m(CaCO₃) = 0,5·100 = 50 g.",
      parametrlar=dict(arch="sxema_ca_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Ortiqcha CO₂ natriy gidroksid eritmasidan o'tkazilganda NORDON tuz hosil bo'ladi. "
            "8 g NaOH dan olingan tuz massasini (g) toping. (M: NaOH=40, NaHCO₃=84)",
      javob="16,8", yechim="CO₂ + NaOH → NaHCO₃: n = 0,2 mol → m = 0,2·84 = 16,8 g.",
      parametrlar=dict(arch="nordon_tuz_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="NaOH va KOH dan iborat 15,2 g aralashmani neytrallash uchun 0,3 mol HCl sarflandi. "
            "Aralashmadagi KOH massasini (g) toping. (M: NaOH=40, KOH=56)",
      javob="11,2", yechim="x+y = 0,3; 40x+56y = 15,2 → 16y = 3,2 → y = 0,2 mol → m(KOH) = 11,2 g.",
      parametrlar=dict(arch="ishqor_aralashma_zanjir")),
]

# ---------- O2 ----------
check("o41b", 200/100*56, 112)
check("o41c", 200/100*74, 148)
check("o41d", 112*0.8, 89.6)
check("o43d", 0.1*98, 9.8)
O2 = [
 dict(n=41, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Ohak zavodida ohaktosh kuydiriladi va so'ndiriladi: CaCO₃ → CaO → Ca(OH)₂. "
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Ikkala bosqichning tenglamalarini yozing va reaksiya turlarini aniqlang.",
             yechim=["CaCO₃ → CaO + CO₂ (parchalanish, endotermik); CaO + H₂O → Ca(OH)₂ (birikish, ekzotermik)."], M=4, A=2),
        dict(savol="b) 200 kg toza ohaktoshdan nazariy jihatdan qancha CaO olinadi? (M: CaCO₃=100, CaO=56)",
             yechim=["n = 2 kmol → m(CaO) = 2·56 = 112 kg."], M=4, A=3),
        dict(savol="c) Shu CaO to'liq so'ndirilsa, qancha Ca(OH)₂ hosil bo'ladi? (M(Ca(OH)₂)=74)",
             yechim=["n = 2 kmol → m = 148 kg."], M=4, A=3),
        dict(savol="d) Kuydirish bosqichining unumi 80 % bo'lsa, amalda olinadigan CaO massasini toping.",
             yechim=["m = 112 · 0,8 = 89,6 kg."], M=3, A=2),
      ],
      rasmiylashtirish="Sanoat zanjiri: tenglamalar → nazariy hisob → unum; M15+A10.",
      parametrlar=dict(arch="ohak_zavod_zanjir")),
 dict(n=42, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Rux oksidi ZnO amfoter modda hisoblanadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) ZnO ning amfoterligini ikkita reaksiya tenglamasi orqali isbotlab, har birida "
                   "qaysi sinf vazifasini bajarayotganini tushuntiring.",
             yechim=["ZnO + 2HCl → ZnCl₂ + H₂O — asosli oksid kabi;",
                     "ZnO + 2NaOH → Na₂ZnO₂ + H₂O (suyuqlanma) — kislotali oksid kabi."], M=13, A=0),
        dict(savol="b) Nega alyuminiy idishlarda kuchli ishqoriy eritmalarni saqlash mumkin emas?",
             yechim=["Al va uning himoya qatlami Al₂O₃ amfoter — ishqor bilan reaksiyaga kirishib yemiriladi."], M=9, A=0),
        dict(savol="c) Yana bitta amfoter gidroksidga misol yozing.",
             yechim=["Al(OH)₃ (yoki Be(OH)₂, Cr(OH)₃)."], M=3, A=0),
      ],
      rasmiylashtirish="Amfoterlik-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="amfoter_mulohaza")),
 dict(n=43, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "To'rt modda jadvalda berilgan:\n"
            "[JADVAL] № | Modda ;; 1 | Na₂O ;; 2 | SO₃ ;; 3 | ZnO ;; 4 | NaHSO₄\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir moddaning sinfini (turini) aniqlang.",
             yechim=["Na₂O — asosli oksid; SO₃ — kislotali oksid; ZnO — amfoter oksid; NaHSO₄ — nordon tuz."], M=4, A=3),
        dict(savol="b) 1- va 2-moddalarning suv bilan reaksiya tenglamalarini yozing.",
             yechim=["Na₂O + H₂O → 2NaOH; SO₃ + H₂O → H₂SO₄."], M=4, A=2),
        dict(savol="c) 1- va 2-moddalar O'ZARO reaksiyasining tenglamasini yozing.",
             yechim=["Na₂O + SO₃ → Na₂SO₄ — asosli + kislotali oksid → tuz."], M=4, A=2),
        dict(savol="d) 0,1 mol SO₃ dan olinadigan sulfat kislota massasini hisoblang. (M(H₂SO₄)=98)",
             yechim=["n = 0,1 mol → m = 9,8 g."], M=3, A=3),
      ],
      rasmiylashtirish="Sinflar-jadval: tasnif → reaksiyalar → hisob; M15+A10.",
      parametrlar=dict(arch="tort_modda_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261105)
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
    d = dict(n=n, tur="Y1", element="II.1", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II1-B", daraja="B", bob=11, bob_nomi="Anorganik moddalar sinflari va genetik bog'lanish",
    manba=("Tongotarov/DTM arxetiplari (sinflarga mos formulalar, necha xil tuz, amfoterlik, "
           "aralashma hisoblari) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; "
           "MS spetsifikatsiyasi II.1"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: nordon/asosli tuzlar, amfoterlik grafigi, "
          "genetik zanjirlar, aralashma va teskari masalalar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
