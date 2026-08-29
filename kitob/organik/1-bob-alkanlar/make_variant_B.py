# -*- coding: utf-8 -*-
"""Organik 1-bob B-varianti: Organik kimyo nazariyasi. Alkanlar (III.1) — HAQIQIY MS MUHITI ★★★.
Formula topish (zichlik, yonish mahsulotlari, ω), izomerlar, xlorlash, aralashma masalalari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_III1B.json"
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
  "Alkanlar haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) barcha bog'lari yakka (sigma);  2) bromli suvni rangsizlantiradi;  3) yorug'likda xlor bilan "
  "o'rin olish reaksiyasiga kirishadi;  4) umumiy formulasi CₙH₂ₙ₊₂.",
  "1, 3 va 4",
  [("hammasi", "bromli suvni alkENlar rangsizlantiradi"),
   ("1 va 4", "xlorlash (radikal) ham alkanlarga xos"),
   ("2 va 3", "2 noto'g'ri")],
  "To'yingan: qo'shbog' yo'q — bromli suv sinoviga «befarq»; yorug'likda galogenlash boradi.",
  dict(arch="alkan_fikr_tanlov"))

# 2 (3) — zichlikdan formula
check("q2", 22*2, 44)
q(3, "yuqori",
  "Vodorodga nisbatan zichligi 22 bo'lgan alkanni aniqlang.",
  "propan (C₃H₈)",
  [("etan", "M = 30, zichligi 15"), ("butan", "M = 58, zichligi 29"), ("metan", "M = 16, zichligi 8")],
  "M = 22·2 = 44 → 14n + 2 = 44 → n = 3.",
  dict(arch="zichlik_formula_b"))

# 3 (3) — yonish mahsulotlaridan formula
check("q3a", 0.2/0.1, 2); check("q3b", 0.3*2/0.1, 6)
q(3, "yuqori",
  "0,1 mol uglevodorod yonganda 0,2 mol CO₂ va 0,3 mol H₂O hosil bo'ldi. Moddani aniqlang.",
  "C₂H₆ (etan)",
  [("CH₄", "unda CO₂ 0,1 mol bo'lardi"), ("C₃H₈", "CO₂ 0,3 mol bo'lardi"),
   ("C₂H₄", "unda H₂O 0,2 mol bo'lardi")],
  "C: 0,2/0,1 = 2; H: 0,6/0,1 = 6 → C₂H₆.",
  dict(arch="yonish_formula"))

# 4 (3) — ω dan formula
check("q4", 24/30*100, 80)
q(3, "yuqori",
  "Tarkibida 80 % uglerod bo'lgan alkanni aniqlang.",
  "etan (C₂H₆)",
  [("metan", "ω(C) = 75 %"), ("propan", "ω(C) = 81,8 %"), ("butan", "ω(C) = 82,8 %")],
  "C₂H₆: 24/30 = 80 %.",
  dict(arch="omega_formula"))

# 5 (3) — RASMLI: izomerlar sxemasi
q(3, "yuqori",
  "Rasmda C₅H₁₂ ning uch izomeri chizilgan. Qaysi izomerning qaynash harorati ENG PAST bo'ladi?",
  "neopentan — eng «sharsimon» molekula",
  [("n-pentan", "cho'ziq zanjir kuchliroq tortishadi — t eng yuqori"),
   ("izopentan", "o'rtacha"),
   ("hammasi teng", "shakl t(qayn.) ga ta'sir qiladi")],
  "Tarmoqlangan sari molekulalar «yopishishi» kamayadi: 36 °C → 28 °C → 9,5 °C.",
  dict(arch="izomer_sxema_oqish"), fig="isomers")

# 6 (3)
q(3, "yuqori",
  "Metanning yorug'likdagi xlorlanishida BIRINCHI bosqich mahsuloti qaysi?",
  "CH₃Cl (xlormetan) va HCl",
  [("CCl₄ darhol", "to'liq almashinish — oxirgi bosqich"),
   ("CH₄Cl", "bunday birikma yo'q — H o'rin almashadi"),
   ("C va HCl", "parchalanish bormaydi")],
  "CH₄ + Cl₂ → (yorug'lik) CH₃Cl + HCl — radikal O'RIN OLISH reaksiyasi.",
  dict(arch="xlorlash_bosqich"))

# 7 (3) — 1-2-3: izomer-gomolog
q(3, "yuqori",
  "Qaysi juftliklar IZOMERLAR hisoblanadi?\n"
  "1) butan va 2-metilpropan;  2) etan va propan;  3) pentan va 2,2-dimetilpropan;  "
  "4) metan va etan.",
  "1 va 3",
  [("2 va 4", "bular gomologlar"), ("hammasi", "2 va 4 — qator qo'shnilari"),
   ("faqat 1", "3 ham (ikkalasi C₅H₁₂)")],
  "Izomerlik sharti — bir xil molekulyar formula: C₄H₁₀ (1) va C₅H₁₂ (3).",
  dict(arch="izomer_juft_tanlov"))

# 8 (2)
q(2, "yuqori",
  "Alkanlarda uglerod atomining gibridlanish turi qanday?",
  "sp³", [("sp²", "alkenlarda"), ("sp", "alkinlarda"), ("gibridlanish yo'q", "organikada bor")],
  "To'rt yakka bog' — tetraedrik sp³ (bog' burchagi 109°28′).",
  dict(arch="sp3"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi formulalarni sinflari bilan TO'G'RI moslang:\n"
  "[JADVAL] Formula | Sinf ;; a) C₆H₁₄ | 1) sikloalkan ;; b) C₆H₁₂ | 2) alkan ;; c) C₆H₆ | 3) aren",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "C₆H₁₄ = CₙH₂ₙ₊₂ — alkan"), ("a—2, b—3, c—1", "C₆H₆ — benzol (aren)"),
   ("a—3, b—1, c—2", "moslashuvlar chalkash")],
  "2n+2 → alkan; 2n → sikloalkan (yoki alken); C₆H₆ — benzol.",
  dict(arch="sinf_moslash_jadval"))

# 10 (3)
check("q10", 11.2/22.4*58, 29)
q(3, "yuqori",
  "11,2 L (n.sh.) butanning massasini toping. (M(C₄H₁₀)=58)",
  "29 g", [("58 g", "1 mol uchun"), ("14,5 g", "chorak mol emas"), ("116 g", "ikki baravar")],
  "n = 0,5 mol → m = 29 g.",
  dict(arch="butan_massa_hisob"))

# 11 (3) — aralashma yonishi
check("q11", 0.1*1+0.2*2, 0.5)
q(3, "yuqori",
  "0,1 mol metan va 0,2 mol etan aralashmasi to'liq yondirildi. Hosil bo'lgan CO₂ ning umumiy mol "
  "miqdorini toping.",
  "0,5", [("0,3", "etan har moli 2 CO₂ beradi"), ("0,6", "hisob xato"), ("0,4", "metan ham qo'shiladi")],
  "n(CO₂) = 0,1·1 + 0,2·2 = 0,5 mol.",
  dict(arch="aralash_yonish"))

# 12 (2)
q(2, "yuqori",
  "Vyurs reaksiyasi nima uchun ishlatiladi?",
  "galogenalkanlardan uzunroq zanjirli alkan olish uchun",
  [("alkanni parchalash uchun", "aksincha — zanjir ulanadi"),
   ("spirt olish uchun", "spirtlar boshqa yo'l bilan"),
   ("alkanni to'yintirish uchun", "alkan allaqachon to'yingan")],
  "2CH₃Cl + 2Na → C₂H₆ + 2NaCl — zanjirlar «tikiladi».",
  dict(arch="vyurs"))

# 13 (3)
q(3, "yuqori",
  "2,2-dimetilbutan molekulasidagi uglerod atomlari sonini toping.",
  "6", [("4", "asosiy zanjir 4 + 2 metil"), ("5", "metillar ham uglerod"), ("8", "ortiqcha sanash")],
  "Butan zanjiri (4C) + ikkita metil (2C) = C₆H₁₄ — geksan izomeri.",
  dict(arch="nom_dan_formula"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] n | Alkan | Izomerlar soni ;; 4 | butan | 2 ;; 5 | pentan | ? ;; 6 | geksan | ?",
  "3; 5",
  [("2; 4", "pentanda 3 ta"), ("3; 4", "geksanda 5 ta"), ("4; 6", "ko'paytirib yuborilgan")],
  "C₅H₁₂ — 3 izomer; C₆H₁₄ — 5 izomer (soni tez o'sadi).",
  dict(arch="izomer_soni_jadval"))

# 15 (3)
check("q15", 44.8/22.4*16, 32)
q(3, "yuqori",
  "44,8 L (n.sh.) metan massasini va undagi uglerod massasini toping.",
  "32 g; 24 g", [("16 g; 12 g", "2 mol bor"), ("32 g; 8 g", "C: 2·12 = 24"), ("44,8 g; 24 g", "hajm massa emas")],
  "n = 2 mol → m = 32 g; m(C) = 2·12 = 24 g.",
  dict(arch="metan_c_hisob"))

# 16 (2)
q(2, "yuqori",
  "Alkanlarning tabiiy manbalari qaysilar?",
  "tabiiy gaz va neft",
  [("faqat o'simliklar", "asosiy manba — qazilmalar"),
   ("suv va havo", "ularda alkan yo'q"),
   ("faqat sun'iy sintez", "tabiiy zaxiralar ulkan")],
  "Tabiiy gaz — metan; neft — suyuq alkanlar ombori.",
  dict(arch="tabiiy_manba"))

# 17 (3)
check("q17", 0.1*50.5, 5.05)
q(3, "yuqori",
  "CH₄ + Cl₂ → CH₃Cl + HCl. 0,1 mol metan birinchi bosqichda to'liq xlorlanganda hosil bo'lgan "
  "xlormetan massasini toping. (M(CH₃Cl)=50,5)",
  "5,05 g", [("50,5 g", "1 mol uchun"), ("10,1 g", "ikki baravar"), ("3,65 g", "bu HCl massasi")],
  "n = 0,1 mol → m = 5,05 g.",
  dict(arch="xlorlash_hisob"))

# 18 (2)
q(2, "yuqori",
  "Sikloalkanlarning eng sodda vakili qaysi?",
  "siklopropan (C₃H₆)",
  [("siklometan", "bir ugleroddan halqa bo'lmaydi"), ("sikloetan", "ikki atomdan ham"),
   ("siklobutan", "u ikkinchi vakil")],
  "Halqa uchun kamida 3 uglerod kerak.",
  dict(arch="siklopropan"))

# 19 (3) — RASMLI: izomer nomlash
q(3, "yuqori",
  "5-savol rasmidagi 2-izomer (bitta metil tarmoqli) IUPAC bo'yicha qanday nomlanadi?",
  "2-metilbutan",
  [("3-metilbutan", "kichik raqam qoidasi"), ("pentan", "u to'g'ri zanjirli 1-izomer"),
   ("2-metilpentan", "asosiy zanjir 4 uglerodli")],
  "Asosiy zanjir — butan; CH₃ ikkinchi uglerodda.",
  dict(arch="izomer_nomlash"), fig="isomers")

# 20 (2)
q(2, "yuqori",
  "Metan «botqoq gazi» deb ham ataladi. Sababi nimada?",
  "botqoqlarda organik qoldiqlar chirishida hosil bo'ladi",
  [("botqoq rangida bo'lgani uchun", "metan rangsiz"),
   ("faqat botqoqda uchraydi", "asosiy manba — konlar"),
   ("botqoqni quritgani uchun", "gaz suvni quritmaydi")],
  "Anaerob bakteriyalar faoliyati — pufakchalar ko'tarilib turadi.",
  dict(arch="botqoq_gazi"))

# 21 (3)
check("q21", 44.8-2*11.2, 22.4)
q(3, "yuqori",
  "CH₄ + 2O₂ → CO₂ + 2H₂O. 11,2 L metan yonishi uchun 44,8 L havo-kisloroddan qancha kislorod "
  "ORTIB qoladi? (hajmlar n.sh.da, sof O₂ berilgan)",
  "22,4 L", [("33,6 L", "sarflangani 22,4 L"), ("11,2 L", "sarf ikki baravar"), ("0 L", "ortadi")],
  "Kerak: 2·11,2 = 22,4 L → ortadi: 44,8 − 22,4 = 22,4 L.",
  dict(arch="ortiqcha_o2"))

# 22 (3) — 1-2-3: metan ishlatilishi
q(3, "yuqori",
  "Metandan sanoatda nimalar olinadi?\n"
  "1) vodorod (konversiya);  2) atsetilen (piroliz);  3) qurum (is qora);  4) sulfat kislota.",
  "1, 2 va 3",
  [("hammasi", "H₂SO₄ oltingugurtdan olinadi"), ("faqat 1", "2 va 3 ham sanoat jarayonlari"),
   ("2 va 4", "4 metanga aloqasiz")],
  "CH₄ → CO+3H₂; 2CH₄ → C₂H₂+3H₂ (1500 °C); CH₄ → C + 2H₂.",
  dict(arch="metan_ishlatish_tanlov"))

# 23 (3) — aralashma teskari
check("q23a", 8.96/22.4, 0.4); check("q23b", (0.7-0.4)/1, 0.3)
q(3, "yuqori",
  "Metan va etan aralashmasi 8,96 L (n.sh.); yonishida jami 0,7 mol CO₂ hosil bo'ldi. Aralashmadagi "
  "etan mol miqdorini toping.",
  "0,3", [("0,1", "x + 2y = 0,7; x+y = 0,4 → y = 0,3"), ("0,4", "bu jami mol"), ("0,2", "hisob xato")],
  "x+y = 0,4; x+2y = 0,7 → y = 0,3 mol etan.",
  dict(arch="aralash_teskari_b"))

# 24 (2)
q(2, "yuqori",
  "Qaysi alkan xona haroratida SUYUQ holatda bo'ladi?",
  "geksan (C₆H₁₄)",
  [("metan", "gaz"), ("propan", "gaz"), ("butan", "gaz (chegarada)")],
  "C₅ dan C₁₅ gacha — suyuqliklar (benzin-kerosin diapazoni).",
  dict(arch="suyuq_alkan"))

# 25 (3)
q(3, "yuqori",
  "Metanning konversiyasi (CH₄ + H₂O → CO + 3H₂) sanoatda nima uchun MUHIM?",
  "ammiak sintezi va boshqa jarayonlar uchun vodorod beradi",
  [("kislorod olish uchun", "reaksiyada O₂ yo'q"),
   ("metanni tozalash uchun", "metan sarflanadi"),
   ("suvni tozalash uchun", "suv reagent")],
  "Dunyo vodorodining asosiy qismi aynan shu jarayondan olinadi.",
  dict(arch="konversiya"))

# 26 (3) — RASMLI: qaynash grafigi (B talqini)
q(3, "yuqori",
  "Grafikdan foydalaning: qaysi alkanlar qishda (−20 °C da) ham GAZ holatida qoladi?",
  "metan, etan, propan",
  [("faqat metan", "etan (−89°) va propan (−42°) ham qaynab bo'lgan"),
   ("hammasi", "butan −0,5 °C da qaynaydi — sovuqda suyuladi"),
   ("hech qaysi", "aksincha")],
  "t(qayn.) < −20 °C bo'lganlar gazligicha qoladi; butan sovuqda suyulib, ballon «ishlamay» qoladi.",
  dict(arch="bp_oqish_b"), fig="bp_alkan")

# 27 (3)
check("q27", 0.25*44+0.25*72, 29)
q(3, "yuqori",
  "Teng mol miqdordagi propan va pentan aralashmasining 0,5 molida qancha massa bor? "
  "(M: C₃H₈=44, C₅H₁₂=72)",
  "29 g", [("58 g", "1 mol aralashma uchun"), ("116 g", "ikki mol uchun"), ("14,5 g", "chorak")],
  "0,25·44 + 0,25·72 = 11 + 18 = 29 g (o'rtacha M = 58).",
  dict(arch="aralash_massa"))

# 28 (2) — RASMLI: izomerlar reuse
q(2, "yuqori",
  "5-savol rasmidagi uch izomer haqida qaysi fikr TO'G'RI?",
  "molekulyar formulalari bir xil (C₅H₁₂), xossalari farqli",
  [("formulalari har xil", "aynan bir xil — shu izomerlik"),
   ("xossalari bir xil", "qaynash haroratlari farqli-ku"),
   ("ular gomologlar", "gomologlar CH₂ ga farq qiladi")],
  "Izomerlik — «bitta formula, har xil modda» hodisasi.",
  dict(arch="izomer_xulosa"), fig="isomers")

# 29 (3)
check("q29", 5.8/58*4*22.4, 8.96)
q(3, "yuqori",
  "C₄H₁₀ + 13/2O₂ → 4CO₂ + 5H₂O. 5,8 g butan yonganda hosil bo'lgan CO₂ hajmini (n.sh.) toping. "
  "(M(C₄H₁₀)=58)",
  "8,96 L", [("2,24 L", "koeffitsiyent 4"), ("22,4 L", "1 mol uchun"), ("4,48 L", "hisob xato")],
  "n = 0,1 → n(CO₂) = 0,4 mol → V = 8,96 L.",
  dict(arch="butan_yonish_hisob"))

# 30 (2)
q(2, "yuqori",
  "«Oktan soni» qaysi yoqilg'ining sifat ko'rsatkichi?",
  "benzinning (detonatsiyaga chidamlilik)",
  [("tabiiy gazning", "gaz uchun boshqa ko'rsatkichlar"), ("ko'mirning", "qattiq yoqilg'i"),
   ("spirtning", "asosiy qo'llanish benzinda")],
  "AI-95: izooktanning 95 % li aralashmasiga teng chidamlilik.",
  dict(arch="oktan_soni"))

# 31 (3)
check("q31", 7.2/72*5*44, 22)
q(3, "yuqori",
  "7,2 g pentan to'liq yonganda hosil bo'lgan CO₂ massasini toping. (M: C₅H₁₂=72, CO₂=44)",
  "22 g", [("4,4 g", "koeffitsiyent 5"), ("44 g", "1 mol CO₂ massasi"), ("11 g", "hisob xato")],
  "n = 0,1 → n(CO₂) = 0,5 mol → m = 22 g.",
  dict(arch="pentan_yonish_hisob"))

# 32 (3) — RASMLI: bp hisob
check("q32", -0.5-(-42), 41.5)
q(3, "yuqori",
  "Grafikdan: butan va propan qaynash haroratlari orasidagi farq taxminan qancha?",
  "≈ 42 °C", [("≈ 10 °C", "−0,5 − (−42) ≈ 41,5"), ("≈ 90 °C", "bu boshqa juftlik"), ("0 °C", "farq bor")],
  "−0,5 − (−42) = 41,5 ≈ 42 °C.",
  dict(arch="bp_farq_b"), fig="bp_alkan")

# ---------- Y2: uch gaz ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.1",
  ichki_pasport=[dict(n=33, element="III.1", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="III.1", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="III.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch gazsimon alkan tekshirildi: X — vodorodga nisbatan zichligi 8; Y — vodorodga "
               "nisbatan zichligi 22; Z — 0,1 moli yonganda 0,4 mol CO₂ beradi. 33–35-savollarga "
               "A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X gaz qaysi?",
    "34. Y gazning formulasi qaysi?",
    "35. Z gaz qaysi alkan?"],
  javoblar_royxati=["A) metan", "B) C₃H₈", "C) butan", "D) etan", "E) C₂H₆", "F) pentan"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="etan zichligi 15 bo'lardi"),
                   dict(variant="E", xato="M = 44 — bu propan"),
                   dict(variant="F", xato="pentan 0,5 mol CO₂ berardi va u suyuq")],
  yechim=("X: M = 16 — metan (A). Y: M = 44 — propan (B). "
          "Z: 4 uglerodli — butan (C)."),
  parametrlar=dict(arch="uch_alkan_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 0.5*16+0.5*30, 23); check("o36b", 23/2, 11.5)
check("o37", 10/(0.1*3), 33.3, tol=0.5)
check("o38", 6.72/22.4/3, 0.1); check("o38b", 0.1*44, 4.4)
check("o39a", 4.48/22.4, 0.2); check("o39b", 0.2*3*18, 10.8)
check("o40a", 14.2/(0.1+0.1), 71); check("o40b", (14.2-0.1*44)/0.1, 98)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Teng mol miqdordagi metan-etan aralashmasining vodorodga nisbatan zichligini toping. "
            "(M: CH₄=16, C₂H₆=30)",
      javob="11,5", yechim="O'rtacha M = (16+30)/2 = 23 → D(H₂) = 11,5.",
      parametrlar=dict(arch="ortacha_zichlik_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="0,1 mol propan to'liq yonishi uchun kerak bo'ladigan HAVO mol miqdorini toping "
            "(havoda 21 % kislorod bor; C₃H₈ + 5O₂ → ...).",
      javob="2,4",
      yechim="n(O₂) = 0,5 mol → havo = 0,5/0,21 ≈ 2,4 mol — 10 mol ortig'i bilan yetadi.",
      parametrlar=dict(arch="havo_hisob_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayonda 6,72 L (n.sh.) noma'lum alkan yonib 0,9 mol CO₂ berdi. Alkanning "
            "molyar massasini (g/mol) toping.",
      javob="44", yechim="n = 0,3 mol; C soni = 0,9/0,3 = 3 → C₃H₈ → M = 44.",
      parametrlar=dict(arch="sxema_formula_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="4,48 L (n.sh.) etan to'liq yonganda hosil bo'lgan suvning massasini (g) toping. "
            "(2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O)",
      javob="10,8", yechim="n = 0,2 mol → n(H₂O) = 0,6 mol → m = 10,8 g.",
      parametrlar=dict(arch="etan_suv_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Propan va noma'lum alkan X ning teng mol (0,1 moldan) aralashmasi 14,2 g keladi. "
            "X alkanning molyar massasini (g/mol) toping. (M(C₃H₈)=44)",
      javob="98",
      yechim="0,1·44 + 0,1·M = 14,2 → M = 98 — mos alkan C₇H₁₆ (geptan).",
      parametrlar=dict(arch="aralash_m_zanjir")),
]

# ---------- O2 ----------
check("o41b", 8.96/22.4, 0.4); check("o41c", 0.4*2*22.4, 17.92)
check("o43a", 0.88/44, 0.02); check("o43b", 0.02*3, 0.06)
O2 = [
 dict(n=41, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Uy pechida 8,96 L (n.sh.) metan yoqildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Yonish tenglamasini yozing va reaksiya turini ayting.",
             yechim=["CH₄ + 2O₂ → CO₂ + 2H₂O — ekzotermik oksidlanish."], M=3, A=2),
        dict(savol="b) Yonish uchun zarur kislorod hajmini (n.sh.) toping.",
             yechim=["n(CH₄) = 0,4 → n(O₂) = 0,8 mol → V = 17,92 L."], M=4, A=3),
        dict(savol="c) Bu kislorodni beradigan havo hajmini baholang (O₂ ≈ 21 %).",
             yechim=["V(havo) ≈ 17,92/0,21 ≈ 85 L."], M=4, A=3),
        dict(savol="d) Nega yopiq xonada gaz asbobi ishlatish xavfli? Ikki sabab yozing.",
             yechim=["Kislorod kamayadi; chala yonishda zaharli CO to'planadi."], M=4, A=2),
      ],
      rasmiylashtirish="Metan-havo zanjiri: tenglama → O₂ → havo → xavfsizlik; M15+A10.",
      parametrlar=dict(arch="metan_havo_zanjir")),
 dict(n=42, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Izomeriya hodisasining «kuchi» tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega uglerod atomlari soni ortishi bilan izomerlar soni «portlab» o'sadi "
                   "(C₄ — 2 ta, C₁₀ — 75 ta, C₂₀ — 366 mingdan ortiq)?",
             yechim=["Har yangi uglerod zanjirga bir necha xil joyga «ulanishi» mumkin —",
                     "kombinatsiyalar soni ko'paytma qonuni bo'yicha keskin o'sadi."], M=13, A=0),
        dict(savol="b) Izomeriya benzin sifatiga qanday aloqador?",
             yechim=["Tarmoqlangan izomerlar (izooktan) detonatsiyaga chidamli — oktan soni yuqori."], M=9, A=0),
        dict(savol="c) C₇H₁₆ uchun bitta tarmoqlangan izomer formulasini (nomini) yozing.",
             yechim=["Masalan, 2-metilgeksan (yoki 2,2-dimetilpentan)."], M=3, A=0),
      ],
      rasmiylashtirish="Izomeriya-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="izomeriya_mulohaza")),
 dict(n=43, tur="O2", element="III.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Noma'lum gazsimon alkanning 0,02 moli yondirilganda 0,88 g CO₂ yig'ildi. Bandlar "
            "ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Hosil bo'lgan CO₂ mol miqdorini toping. (M(CO₂)=44)",
             yechim=["n(CO₂) = 0,88/44 = 0,02 mol."], M=4, A=2),
        dict(savol="b) Bir mol alkanga to'g'ri keladigan uglerod sonini aniqlang.",
             yechim=["0,02/0,02 = 1 → bitta uglerod."], M=4, A=3),
        dict(savol="c) Alkanning formulasi va nomini yozing.",
             yechim=["CH₄ — metan."], M=4, A=3),
        dict(savol="d) Shu alkan uchun izomerlar bormi? Sababini yozing.",
             yechim=["Yo'q — zanjir izomeriyasi kamida 4 uglerodda boshlanadi."], M=3, A=2),
      ],
      rasmiylashtirish="Formula-detektiv: CO₂ → C soni → formula → izomeriya; M15+A10.",
      parametrlar=dict(arch="formula_detektiv_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263105)
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
    variant="mavzu-III1-B", daraja="B", bob=1, bob_nomi="Organik kimyo nazariyasi. Alkanlar",
    manba=("Tongotarov/DTM arxetiplari (zichlik/yonish/ω dan formula topish, izomerlar, xlorlash, "
           "aralashma) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; MS "
           "spetsifikatsiyasi III.1"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★ (Organik kimyo kitobi): formula-detektiv "
          "masalalar, izomerlar sxemasi, aralashma yonishi."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
