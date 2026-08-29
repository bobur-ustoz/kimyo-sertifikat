# -*- coding: utf-8 -*-
"""12-bob B-varianti: Oksidlar, asoslar, kislotalar va tuzlarning xossalari, olinishi (II.2) — HAQIQIY MS MUHITI ★★★.
Olinish usullarini sanash, ion almashinish shartlari, termik parchalanish, yetishmovchi/ortiqcha reagent.
Tongotarov/DIM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_II2B.json"
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

# 1 (3) — 1-2-3: ZnCl2 olish usullari
q(3, "yuqori",
  "ZnCl₂ tuzini quyidagi qaysi usullar bilan olish MUMKIN?\n"
  "1) Zn + HCl;  2) ZnO + HCl;  3) Zn(OH)₂ + HCl;  4) Zn + NaCl eritmasi.",
  "1, 2 va 3",
  [("faqat 1", "oksid va gidroksid ham kislotada eriydi"),
   ("hammasi", "Zn natriyni tuzidan siqib chiqara olmaydi — Na faolroq"),
   ("2 va 4", "metall + kislota ham beradi; 4 esa bormaydi")],
  "Metall, uning oksidi va gidroksidi — uchalasi ham HCl bilan ZnCl₂ beradi; 4 — faollik qatoriga zid.",
  dict(arch="olinish_sanash"))

# 2 (3) — ion almashinish sharti
q(3, "yuqori",
  "Qaysi juft eritmalar orasida almashinish reaksiyasi OXIRIGACHA BORMAYDI?",
  "NaCl va KNO₃",
  [("BaCl₂ va Na₂SO₄", "BaSO₄↓ cho'kadi"),
   ("Na₂CO₃ va HCl", "CO₂↑ ajraladi"),
   ("NaOH va HCl", "H₂O (kuchsiz elektrolit) hosil bo'ladi")],
  "Almashinish borishi uchun cho'kma, gaz yoki suv kerak; NaCl + KNO₃ da hech biri yo'q.",
  dict(arch="almashinish_shart"))

# 3 (3) — termik parchalanish
q(3, "yuqori",
  "Qizdirilganda PARCHALANMAYDIGAN tuzni ko'rsating.",
  "Na₂CO₃", [("CaCO₃", "CaO + CO₂ ga parchalanadi"), ("NaHCO₃", "Na₂CO₃ + H₂O + CO₂"),
              ("NH₄Cl", "NH₃ + HCl ga «sublimatlanadi»")],
  "Ishqoriy metallarning O'RTA karbonatlari termik juda barqaror.",
  dict(arch="termik_barqaror"))

# 4 (3) — yetishmovchilik
check("q4", 0.1 - 0.15/2, 0.025, tol=0.001)
q(3, "yuqori",
  "0,1 mol rux bilan 0,15 mol xlorid kislota reaksiyaga kiritildi (Zn + 2HCl → ZnCl₂ + H₂). "
  "Qaysi modda va qancha miqdorda ORTIB qoladi?",
  "Zn — 0,025 mol",
  [("HCl — 0,05 mol", "0,1 mol Zn ga 0,2 mol HCl kerak edi — HCl yetishmaydi, ortmaydi"),
   ("hech biri ortmaydi", "nisbat 1:2 ga mos kelmaydi"),
   ("Zn — 0,05 mol", "0,15/2 = 0,075 mol Zn sarflanadi: 0,1 − 0,075 = 0,025")],
  "HCl cheklovchi: 0,15 mol HCl 0,075 mol Zn ni eritadi → Zn dan 0,025 mol ortib qoladi.",
  dict(arch="cheklovchi_reagent"))

# 5 (3) — RASMLI: Kipp apparati
q(3, "yuqori",
  "Rasmdagi Kipp apparatida marmar va xlorid kislota yordamida gaz olinmoqda. Jo'mrak yopilganda "
  "reaksiya nima uchun TO'XTAYDI?",
  "gaz bosimi kislotani marmardan pastga siqib chiqarib, aloqani uzadi",
  [("kislota tugab qoladi", "kislota apparat ichida qoladi"),
   ("marmar erib bo'ladi", "marmar ham qoladi — aloqa uziladi xolos"),
   ("harorat pasayadi", "jarayon haroratga bog'liq emas")],
  "Kipp apparatining afzalligi: yig'ilgan CO₂ bosimi kislota sathini tushirib, jarayonni o'zi boshqaradi.",
  dict(arch="kipp_oqish"), fig="kipp")

# 6 (3)
q(3, "yuqori",
  "Qaysi reaksiyada UCHUVCHAN kislota o'z tuzidan kuchliroq (uchmaydigan) kislota yordamida siqib "
  "chiqariladi?",
  "NaCl(qattiq) + H₂SO₄(kons.) → NaHSO₄ + HCl↑",
  [("Na₂SO₄ + HCl → ...", "kuchsizroq/uchuvchan kislota sulfatni siqib chiqara olmaydi"),
   ("NaNO₃ + H₂O → ...", "suv kislota emas"),
   ("Na₂CO₃ + NaOH → ...", "ishqor kislota siqib chiqarmaydi")],
  "Konsentrlangan H₂SO₄ uchmaydi — qizdirishda uchuvchan HCl haydab chiqariladi.",
  dict(arch="uchuvchan_siqish"))

# 7 (3) — 1-2-3: NaOH bilan reaksiya
q(3, "yuqori",
  "Quyidagilarning qaysilari NaOH eritmasi bilan reaksiyaga kirishadi?\n"
  "1) CO₂;  2) CuSO₄;  3) K₂O;  4) Al(OH)₃;  5) BaCl₂.",
  "1, 2 va 4",
  [("1, 3 va 5", "K₂O ham ishqoriy — o'zaro kirishmaydi; BaCl₂ bilan belgi yo'q"),
   ("faqat 1 va 2", "amfoter Al(OH)₃ ham ishqorda eriydi"),
   ("hammasi", "K₂O va BaCl₂ — yo'q")],
  "Ishqor bilan: kislotali oksid (CO₂), tuz (CuSO₄ — cho'kma), amfoter gidroksid (Al(OH)₃).",
  dict(arch="naoh_tanlov123"))

# 8 (2)
q(2, "yuqori",
  "Konsentrlangan sulfat kislota suyultirilganda qaysi qoidaga amal qilinadi?",
  "kislota suvga OZ-OZDAN quyiladi",
  [("suv kislotaga quyiladi", "qaynab sachraydi — xavfli!"),
   ("farqi yo'q", "issiqlik ajralishi tartibni belgilaydi"),
   ("ikkalasini birdan aralashtiriladi", "keskin qizib ketadi")],
  "Erish juda ekzotermik: «kislotani suvga, sekin, aralashtirib».",
  dict(arch="suyultirish_qoida"))

# 9 (3) — JADVAL: reagent tanlash
q(3, "yuqori",
  "Jadvaldagi o'tishlar uchun reagentlarni TO'G'RI moslang:\n"
  "[JADVAL] O'tish | Reagent ;; a) Fe₂O₃ → FeCl₃ | 1) HCl ;; b) FeCl₃ → Fe(OH)₃ | 2) KOH ;; "
  "c) Fe(OH)₃ → Fe₂O₃ | 3) qizdirish",
  "a—1, b—2, c—3",
  [("a—2, b—1, c—3", "oksidga ishqor emas, kislota kerak"),
   ("a—1, b—3, c—2", "tuzdan gidroksid — ishqor bilan"),
   ("a—3, b—2, c—1", "qizdirish oksidni tuzga aylantirmaydi")],
  "Oksid+kislota → tuz; tuz+ishqor → gidroksid↓; gidroksid → (t°) oksid.",
  dict(arch="otish_moslash_jadval"))

# 10 (3)
check("q10", 16/80*2*36.5/0.2, 73)
q(3, "yuqori",
  "16 g CuO ni eritish uchun 20 % li xlorid kislota eritmasidan necha gramm kerak? (M: CuO=80, HCl=36,5)",
  "73 g", [("36,5 g", "eritma emas, sof HCl massasi ham 14,6 g"), ("14,6 g", "bu sof HCl massasi"),
            ("40 g", "foiz hisobga olinmagan")],
  "n(CuO)=0,2 → n(HCl)=0,4 → m(HCl)=14,6 g → m(eritma) = 14,6/0,2 = 73 g.",
  dict(arch="eritma_kislota_hisob"))

# 11 (3) — 1-2-3: o'zaro reaksiya
q(3, "yuqori",
  "Qaysi juftliklar O'ZARO reaksiyaga kirisha oladi?\n"
  "1) CaO va SO₃;  2) NaOH va Ba(OH)₂;  3) Zn(OH)₂ va NaOH;  4) HCl va HNO₃.",
  "1 va 3",
  [("2 va 4", "ikkita ishqor / ikkita kislota o'zaro kirishmaydi"),
   ("faqat 1", "amfoter Zn(OH)₂ ishqorda eriydi"),
   ("1, 2 va 3", "ikki asos reaksiyaga kirishmaydi")],
  "Qarama-qarshi tabiatlilar kirishadi: asosli+kislotali oksid (1), amfoter+ishqor (3).",
  dict(arch="ozaro_tanlov123"))

# 12 (2)
q(2, "yuqori",
  "Vodorodni sinash («pop» tovushi) qaysi xossaga asoslangan?",
  "vodorod-havo aralashmasi yonganda portlash tovushi beradi",
  [("vodorod hidiga", "H₂ hidsiz"), ("rangiga", "rangsiz gaz"),
   ("ohakli suvni loyqalatishiga", "bu CO₂ sinovi")],
  "Toza H₂ tinch yonadi, havo aralashgani «pop» etadi — shu bilan aniqlanadi.",
  dict(arch="h2_sinov"))

# 13 (3)
q(3, "yuqori",
  "Nitratlarning termik parchalanishida ishqoriy metall nitratlari (masalan, KNO₃) nima beradi?",
  "nitrit va kislorod (KNO₂ + O₂)",
  [("oksid, NO₂ va O₂", "bu o'rtacha faol metallar (Cu) uchun"),
   ("sof metall", "bu Ag, Au nitratlari uchun"),
   ("parchalanmaydi", "qizdirishda O₂ ajratadi")],
  "2KNO₃ → 2KNO₂ + O₂: faollik qatoridagi o'rniga qarab mahsulot farq qiladi.",
  dict(arch="nitrat_parchalanish"))

# 14 (3) — JADVAL «?»
check("q14", 20/80, 0.25)
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring (CuO + H₂SO₄ → CuSO₄ + H₂O):\n"
  "[JADVAL] m(CuO), g | n(CuO), mol | m(CuSO₄), g ;; 20 | ? | ?",
  "0,25; 40",
  [("0,25; 25", "M(CuSO₄)=160: 0,25·160=40"), ("0,2; 32", "n = 20/80 = 0,25"),
   ("2,5; 400", "nol adashgan")],
  "n = 20/80 = 0,25 mol → m(CuSO₄) = 0,25·160 = 40 g.",
  dict(arch="hisob_jadval"))

# 15 (3)
q(3, "yuqori",
  "Temir(II) sulfat FeSO₄ tuzini olish uchun temir qaysi moddalar bilan reaksiyaga kiritilishi mumkin?\n"
  "1) suyultirilgan H₂SO₄;  2) CuSO₄ eritmasi;  3) konsentrlangan HNO₃ (sovuqda);  4) MgSO₄ eritmasi.",
  "1 va 2",
  [("1, 2 va 3", "kons. HNO₃ sovuqda temirni passivlaydi"),
   ("faqat 1", "Fe misni tuzidan siqib chiqaradi (2)"),
   ("2 va 4", "Mg temirdan faol — Fe uni siqib chiqara olmaydi")],
  "Fe + H₂SO₄(suyul.) → FeSO₄ + H₂; Fe + CuSO₄ → FeSO₄ + Cu.",
  dict(arch="feso4_yollari"))

# 16 (2)
q(2, "yuqori",
  "Qaysi gidroksid ISHQORLARDA ham, KISLOTALARDA ham eriydi?",
  "Al(OH)₃", [("Fe(OH)₃", "faqat kislotada"), ("Cu(OH)₂", "faqat kislotada"),
               ("Mg(OH)₂", "faqat kislotada")],
  "Amfoter gidroksidlar: Al(OH)₃, Zn(OH)₂, Be(OH)₂, Cr(OH)₃.",
  dict(arch="amfoter_gidroksid"))

# 17 (3)
check("q17", 34.2/342, 0.1); check("q17b", 0.1*3*233, 69.9)
q(3, "yuqori",
  "34,2 g Al₂(SO₄)₃ eritmasiga ortiqcha BaCl₂ qo'shildi. Hosil bo'lgan cho'kma massasini toping. "
  "(M: Al₂(SO₄)₃=342, BaSO₄=233)",
  "69,9 g", [("23,3 g", "koeffitsiyent 3 unutilgan"), ("34,2 g", "cho'kma boshqa modda"),
              ("46,6 g", "2 deb olingan")],
  "n(tuz) = 0,1 mol → n(BaSO₄) = 0,3 mol → m = 69,9 g.",
  dict(arch="baso4_hisob"))

# 18 (2)
q(2, "yuqori",
  "CO₂ gazini quruq usulda qanday aniqlash mumkin?",
  "yonayotgan cho'pni so'ndirishi orqali",
  [("«pop» tovushi orqali", "bu H₂"), ("hidi orqali", "CO₂ hidsiz"),
   ("rangi orqali", "rangsiz gaz")],
  "CO₂ yonishni quvvatlamaydi — cho'p o'chadi (asosiy sinov — ohakli suv).",
  dict(arch="co2_sinov"))

# 19 (3) — RASMLI: massa grafigi
q(3, "yuqori",
  "Rasmda NaHCO₃ namunasini qizdirishdagi massa o'zgarishi berilgan. Qoldiq massa boshlang'ichdan "
  "kichikligining sababi nimada?",
  "H₂O va CO₂ uchib chiqadi: 2NaHCO₃ → Na₂CO₃ + H₂O + CO₂",
  [("natriy bug'lanadi", "metall bug'lanmaydi"),
   ("modda idishga yopishib qoladi", "kimyoviy sabab bor — gazlar chiqadi"),
   ("tarozi xatosi", "qonuniy massa kamayishi")],
  "Parchalanishda uchuvchi mahsulotlar chiqib ketadi — qoldiq Na₂CO₃.",
  dict(arch="massa_grafik_oqish"), fig="mass_curve")

# 20 (2)
q(2, "yuqori",
  "Qaysi kislota saqlanganda ham, tashilganda ham SHISHA idishda bo'lishi shart emas — u shishani "
  "yemiradi?",
  "HF (ftorid kislota)",
  [("HCl", "shishaga ta'sir qilmaydi"), ("H₂SO₄", "shishada saqlanadi"),
   ("HNO₃", "qoramtir shishada saqlanadi")],
  "HF + SiO₂ → SiF₄ + H₂O: shisha tarkibidagi SiO₂ ni yemiradi — plastik idishda saqlanadi.",
  dict(arch="hf_shisha"))

# 21 (3)
check("q21", 11.2/56*98, 19.6)
q(3, "yuqori",
  "11,2 g temir to'liq erishi uchun kerak bo'lgan sulfat kislota massasini toping. "
  "(Fe + H₂SO₄ → FeSO₄ + H₂; M: Fe=56, H₂SO₄=98)",
  "19,6 g", [("98 g", "1 mol uchun"), ("9,8 g", "0,05 mol deb olingan"), ("39,2 g", "ikki baravar")],
  "n = 0,2 mol → m(H₂SO₄) = 0,2·98 = 19,6 g.",
  dict(arch="fe_h2so4_hisob"))

# 22 (3) — 1-2-3: kislota bilan ham ishqor bilan ham
q(3, "yuqori",
  "Qaysi moddalar HAM xlorid kislota, HAM natriy gidroksid eritmasi bilan reaksiyaga kirishadi?\n"
  "1) ZnO;  2) Al(OH)₃;  3) CaCO₃;  4) NaHCO₃;  5) CuO.",
  "1, 2 va 4",
  [("1 va 2", "NaHCO₃ ham: kislota bilan CO₂, ishqor bilan o'rta tuz beradi"),
   ("3 va 5", "CaCO₃ va CuO ishqor bilan kirishmaydi"),
   ("hammasi", "CaCO₃, CuO — faqat kislota bilan")],
  "Amfoterlar (ZnO, Al(OH)₃) va nordon tuz (NaHCO₃) ikkala tabiatli reagent bilan ham ishlaydi.",
  dict(arch="ikki_tomonlama_tanlov"))

# 23 (3)
check("q23a", 0.1*100, 10); check("q23b", 25-10, 15)
q(3, "yuqori",
  "CaCO₃ va SiO₂ (qum) dan iborat 25 g aralashmaga ortiqcha HCl qo'shildi; 2,24 L (n.sh.) gaz ajraldi. "
  "Erimay qolgan qoldiq massasini toping. (M(CaCO₃)=100)",
  "15 g", [("10 g", "bu CaCO₃ massasi"), ("22,76 g", "gaz massasi ayirilgan"),
            ("4,4 g", "bu CO₂ massasi")],
  "SiO₂ HCl da erimaydi: m(CaCO₃) = 0,1·100 = 10 g → qoldiq (qum) = 25 − 10 = 15 g.",
  dict(arch="qoldiq_aralashma"))

# 24 (2)
q(2, "yuqori",
  "Qattiq ishqor (NaOH) ochiq havoda saqlansa nima bo'ladi?",
  "namlikni va CO₂ ni yutib, sifati buziladi",
  [("hech narsa bo'lmaydi", "NaOH gigroskopik va CO₂ bilan reaksiyaga kirishadi"),
   ("bug'lanib ketadi", "qattiq modda bug'lanmaydi"),
   ("rangi qizaradi", "rang o'zgarishi kuzatilmaydi")],
  "NaOH + CO₂ → Na₂CO₃: shu bois ishqor zich yopiq idishda saqlanadi.",
  dict(arch="naoh_saqlash"))

# 25 (3)
q(3, "yuqori",
  "P → P₂O₅ → H₃PO₄ → Na₃PO₄ zanjiridagi 3-o'tish uchun eng mos reagentni tanlang.",
  "NaOH (ortiqcha miqdorda)",
  [("Na₂SO₄", "kuchsizroq kislota tuzini siqib chiqara olmaydi"),
   ("NaCl", "reaksiya belgisi yo'q"),
   ("Cu(OH)₂", "mis gidroksidi natriyli tuz bera olmaydi")],
  "H₃PO₄ + 3NaOH → Na₃PO₄ + 3H₂O — to'liq neytrallanish uchun ishqor ortiqcha olinadi.",
  dict(arch="p_zanjir_reagent"))

# 26 (3) — RASMLI: gaz ustunlari (B talqini)
check("q26", 0.15*22.4, 3.36)
q(3, "yuqori",
  "Diagrammadagi 3-tajribada (2H₂O₂ → 2H₂O + O₂) 0,3 mol vodorod peroksid parchalangan. "
  "Yig'ilgan kislorod hajmi diagrammada qanday ko'rsatilgan bo'lishi kerak?",
  "3,36 L", [("6,72 L", "koeffitsiyent: O₂ ikki barobar KAM"), ("2,24 L", "0,1 mol deb olingan"),
              ("22,4 L", "1 mol uchun")],
  "n(O₂) = 0,3/2 = 0,15 mol → V = 0,15·22,4 = 3,36 L.",
  dict(arch="bar_gaz_hisob_b"), fig="bar_gaz")

# 27 (3)
check("q27", 0.2*63, 12.6)
q(3, "yuqori",
  "CuO + 2HNO₃ → Cu(NO₃)₂ + H₂O. 8 g mis(II) oksidini eritish uchun kerak bo'lgan nitrat kislota "
  "massasini toping. (M: CuO=80, HNO₃=63)",
  "12,6 g", [("6,3 g", "koeffitsiyent 2 unutilgan"), ("63 g", "1 mol uchun"), ("25,2 g", "ikki baravar")],
  "n(CuO) = 0,1 mol → n(HNO₃) = 0,2 mol → m = 12,6 g.",
  dict(arch="hno3_hisob"))

# 28 (2) — RASMLI: Kipp reuse
q(2, "yuqori",
  "5-savoldagi Kipp apparatida vodorod olish uchun qaysi juftlik yuklanadi?",
  "rux donachalari va xlorid kislota",
  [("marmar va xlorid kislota", "bu CO₂ beradi"),
   ("mis va xlorid kislota", "Cu kislotadan H₂ ajratmaydi"),
   ("osh tuzi va suv", "erish — gaz bermaydi")],
  "Zn + 2HCl → ZnCl₂ + H₂↑ — laboratoriyada H₂ ning klassik olinishi.",
  dict(arch="kipp_h2"), fig="kipp")

# 29 (3)
check("q29", 16.2/81*2*36.5, 14.6)
q(3, "yuqori",
  "16,2 g ZnO ni to'liq eritish uchun kerak bo'ladigan sof HCl massasini toping. (M: ZnO=81, HCl=36,5)",
  "14,6 g", [("7,3 g", "koeffitsiyent 2 unutilgan"), ("36,5 g", "1 mol uchun"), ("29,2 g", "hisob xato")],
  "n(ZnO) = 0,2 mol → n(HCl) = 0,4 mol → m = 0,4·36,5 = 14,6 g.",
  dict(arch="zno_hcl_hisob"))

# 30 (2)
q(2, "yuqori",
  "Kumush buyumlarning vaqt o'tishi bilan QORAYISHI sababi nimada?",
  "havodagi oltingugurtli birikmalar bilan Ag₂S qatlami hosil bo'ladi",
  [("kumush zanglaydi (oksid)", "Ag ochiq havoda oksidlanmaydi"),
   ("chang yig'iladi", "yuvish bilan ketmaydi — kimyoviy qatlam"),
   ("kumush parchalanadi", "metall parchalanmaydi")],
  "4Ag + 2H₂S + O₂ → 2Ag₂S + 2H₂O — qora sulfid pardasi.",
  dict(arch="kumush_qorayish"))

# 31 (3)
check("q31", 9.8/98*233, 23.3)
q(3, "yuqori",
  "9,8 g sulfat kislota eritmasiga ortiqcha bariy xlorid qo'shildi. Cho'kma massasini toping. "
  "(M: H₂SO₄=98, BaSO₄=233)",
  "23,3 g", [("9,8 g", "cho'kma boshqa modda"), ("46,6 g", "ikki baravar"), ("11,65 g", "yarmi")],
  "n = 0,1 mol → m(BaSO₄) = 0,1·233 = 23,3 g.",
  dict(arch="h2so4_bacl2"))

# 32 (3) — RASMLI: massa grafigi hisob
check("q32", 16.8/84, 0.2); check("q32b", 0.1*106, 10.6)
q(3, "yuqori",
  "19-savol grafigidagi tajribada 16,8 g NaHCO₃ olingan edi. Qizdirish tugagach qoldiq (Na₂CO₃) "
  "massasi qancha bo'ladi? (M: NaHCO₃=84, Na₂CO₃=106)",
  "10,6 g", [("16,8 g", "massa kamayadi"), ("21,2 g", "koeffitsiyent teskari"), ("8,4 g", "asossiz yarim")],
  "2NaHCO₃ → Na₂CO₃ + H₂O + CO₂: n = 0,2 mol → Na₂CO₃ 0,1 mol → 10,6 g.",
  dict(arch="massa_grafik_hisob"), fig="mass_curve")

# ---------- Y2: uch metall ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.2",
  ichki_pasport=[dict(n=33, element="II.2", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="II.2", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="II.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch probirkada xlorid kislota bor. Ularga uch metall tashlandi: X — shiddatli gaz "
               "ajratib eridi; Y — sekin gaz ajratib eridi; Z — hech qanday o'zgarish bermadi. "
               "Metallar Mg, Fe va Cu ekani ma'lum. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Z metall qaysi?",
    "34. X metall eriganda hosil bo'lgan tuz qaysi?",
    "35. Y metallning kislotadagi reaksiyasida ajralgan gaz qaysi?"],
  javoblar_royxati=["A) Cu", "B) MgCl₂", "C) H₂", "D) Fe", "E) FeCl₃", "F) Cl₂"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="Fe — sekin eriydi (Y), erimay qolgani Cu"),
                   dict(variant="E", xato="HCl bilan FeCl₂ hosil bo'ladi; X esa Mg"),
                   dict(variant="F", xato="kislotadan xlor emas, vodorod ajraladi")],
  yechim=("Faollik: Mg > Fe > (H) > Cu. Z — Cu (A). X — Mg → MgCl₂ (B). Y — Fe, gaz — H₂ (C)."),
  parametrlar=dict(arch="uch_metall_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 4.48/22.4, 0.2); check("o36b", 0.2*65, 13); check("o36c", 20-13, 7)
check("o37", 8/80*64, 6.4)
check("o38a", 10/100, 0.1); check("o38b", 0.1*111, 11.1)
check("o39a", 14.6*0.2/36.5, 0.08); check("o39b", 0.08/2*22.4, 0.896)
check("o40a", 24.8-0.2*18, 21.2); check("o40b", 24.8-0.2*98, 5.2)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Zn va Cu dan iborat 20 g aralashma ortiqcha xlorid kislotaga solindi: 4,48 L (n.sh.) gaz "
            "ajraldi. Aralashmadagi mis massasini (g) toping. (M(Zn)=65)",
      javob="7", yechim="Cu erimaydi. n(H₂) = 0,2 → n(Zn) = 0,2 → 13 g → m(Cu) = 20 − 13 = 7 g.",
      parametrlar=dict(arch="zn_cu_aralashma")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="CuSO₄ → Cu(OH)₂ → CuO → Cu zanjiri bo'yicha 0,1 mol mis(II) sulfatdan (yo'qotishsiz) "
            "olingan mis massasini (g) toping. (M(Cu)=64)",
      javob="6,4", yechim="Har bosqich 1:1 → n(Cu) = 0,1 mol → m = 6,4 g.",
      parametrlar=dict(arch="cu_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayonda 10 g marmar (CaCO₃) xlorid kislotada to'liq eritildi. Hosil bo'lgan "
            "CaCl₂ massasini (g) toping. (M: CaCO₃=100, CaCl₂=111)",
      javob="11,1", yechim="n = 0,1 mol → m(CaCl₂) = 0,1·111 = 11,1 g.",
      parametrlar=dict(arch="sxema_marmar"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="20 % li 14,6 g xlorid kislota eritmasi ortiqcha rux bilan reaksiyaga kirishdi. Ajralgan "
            "vodorod hajmini (n.sh., L) toping. (M(HCl)=36,5)",
      javob="0,896", yechim="m(HCl) = 2,92 g → n = 0,08 mol → n(H₂) = 0,04 → V = 0,896 L.",
      parametrlar=dict(arch="foizli_kislota_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Cu(OH)₂ va CuO dan iborat 24,8 g aralashma qizdirilganda massa 21,2 g gacha kamaydi. "
            "Boshlang'ich aralashmadagi CuO massasini (g) toping. (M: Cu(OH)₂=98, H₂O=18)",
      javob="5,2", yechim="Yo'qolgan 3,6 g — suv: n(H₂O) = 0,2 → n(Cu(OH)₂) = 0,2 → 19,6 g → "
            "m(CuO) = 24,8 − 19,6 = 5,2 g.",
      parametrlar=dict(arch="qizdirish_aralashma")),
]

# ---------- O2 ----------
check("o41b", 13/65, 0.2); check("o41c", 0.2*136, 27.2); check("o41d", 0.2*22.4, 4.48)
check("o43c", 0.05*233, 11.65)
O2 = [
 dict(n=41, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "13 g rux suyultirilgan sulfat kislota eritmasida to'liq eritildi. Bandlar ketma-ket "
            "yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing va turini aniqlang.",
             yechim=["Zn + H₂SO₄ → ZnSO₄ + H₂↑ — o'rin olish."], M=3, A=2),
        dict(savol="b) Hosil bo'lgan tuzning massasini hisoblang. (M: Zn=65, ZnSO₄=161)",
             yechim=["n = 0,2 mol → m(ZnSO₄) = 32,2 g."], M=4, A=3),
        dict(savol="c) Ajralgan gazning hajmini (n.sh.) toping.",
             yechim=["n(H₂) = 0,2 mol → V = 4,48 L."], M=4, A=3),
        dict(savol="d) Xuddi shu tuzni yana qanday ikki usul bilan olish mumkin? Tenglamalar yozing.",
             yechim=["ZnO + H₂SO₄ → ZnSO₄ + H₂O; Zn(OH)₂ + H₂SO₄ → ZnSO₄ + 2H₂O."], M=4, A=2),
      ],
      rasmiylashtirish="Metall-kislota zanjiri: tenglama → tuz → gaz → muqobil usullar; M15+A10.",
      parametrlar=dict(arch="zn_kislota_zanjir")),
 dict(n=42, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada konsentrlangan sulfat kislota bilan ishlash qoidalari o'rganilmoqda. "
            "Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega suyultirishda kislota suvga quyiladi, aksincha emas? Jarayonning issiqlik "
                   "tabiati asosida batafsil tushuntiring.",
             yechim=["Erish kuchli ekzotermik. Suv kislotaga quyilsa, yengil suv yuzada qizib qaynaydi",
                     "va kislota sachraydi; kislota suvga oz-ozdan quyilsa, issiqlik katta hajmga tarqaladi."], M=13, A=0),
        dict(savol="b) Kons. H₂SO₄ ning gigroskopikligi qanday amaliy maqsadda ishlatiladi?",
             yechim=["Gazlarni quritishda (eksikatorlarda) — suv bug'ini o'ziga tortadi."], M=9, A=0),
        dict(savol="c) Teriga kislota tegsa birinchi yordam qadamini yozing.",
             yechim=["Ko'p oqar suv bilan yuvish, so'ng kuchsiz soda eritmasi bilan neytrallash."], M=3, A=0),
      ],
      rasmiylashtirish="Xavfsizlik-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="xavfsizlik_mulohaza")),
 dict(n=43, tur="O2", element="II.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Rangsiz eritmada H₂SO₄ va MgSO₄ aralash holda bor deb taxmin qilinadi. Bandlar ketma-ket "
            "yechiladi."),
      bandlar=[
        dict(savol="a) Eritmada kislota borligini qanday isbotlash mumkin? Usulni va kutiladigan "
                   "natijani yozing.",
             yechim=["Lakmus — qizil bo'ladi (yoki Zn solinsa H₂ ajraladi)."], M=4, A=2),
        dict(savol="b) Sulfat ionini qanday aniqlash mumkin? Tenglama yozing.",
             yechim=["BaCl₂ qo'shiladi: Ba²⁺ + SO₄²⁻ → BaSO₄↓ (oq, kislotada erimaydigan cho'kma)."], M=4, A=3),
        dict(savol="c) Agar eritmada jami 0,05 mol sulfat ioni bo'lsa, cho'kma massasini hisoblang. "
                   "(M(BaSO₄)=233)",
             yechim=["m = 0,05·233 = 11,65 g."], M=4, A=3),
        dict(savol="d) Mg²⁺ ionini qanday ko'rsatish mumkin?",
             yechim=["Ishqor qo'shiladi: Mg²⁺ + 2OH⁻ → Mg(OH)₂↓ (oq cho'kma)."], M=3, A=2),
      ],
      rasmiylashtirish="Tahlil-zanjir: kislota → sulfat → hisob → kation; M15+A10.",
      parametrlar=dict(arch="tahlil_zanjir_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261205)
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
    variant="mavzu-II2-B", daraja="B", bob=12, bob_nomi="Oksidlar, asoslar, kislotalar va tuzlarning xossalari",
    manba=("Tongotarov/DIM arxetiplari (olinish usullarini sanash, ion almashinish shartlari, termik "
           "parchalanish, cheklovchi reagent) va Spectrum uslubidagi 36–43 — javoblar mustaqil "
           "tekshirilgan; MS spetsifikatsiyasi II.2"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: Kipp apparati, massa-grafik, aralashma va "
          "foizli eritma hisoblari."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
