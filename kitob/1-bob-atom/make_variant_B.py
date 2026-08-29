# -*- coding: utf-8 -*-
"""1-bob B-varianti: Atom tuzilishi (I.1) — HAQIQIY MS MUHITI ★★★.
Konfiguratsiyalar, izotop hisoblari, ionlanish energiyalari, izoelektron zarralar.
Tongotarov variantlari arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_I1B.json"
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

# 1 (3) — elektronlari soni FARQLI ionlar (Tongotarov arxetipi)
q(3, "yuqori",
  "Qaysi qatorda elektronlari soni FARQLI bo'lgan ionlar berilgan?",
  "Al³⁺ va Cl⁻",
  [("Na⁺ va Mg²⁺", "ikkalasida ham 10 e"), ("K⁺ va Ca²⁺", "ikkalasida ham 18 e"),
   ("Ca²⁺ va S²⁻", "ikkalasida ham 18 e")],
  "Al³⁺: 13−3 = 10 e; Cl⁻: 17+1 = 18 e — farqli. Qolgan juftlar izoelektron.",
  dict(arch="ion_e_farq"))

# 2 (3) — qavat-moslash (K L M)
q(3, "yuqori",
  "Elektron qavatlari K²L⁸M⁷ bo'lgan zarra qaysi?",
  "Cl atomi", [("S²⁻ ioni", "S²⁻ da K²L⁸M⁸ (18 e)"), ("Ar atomi", "Ar: K²L⁸M⁸"),
                ("K⁺ ioni", "K⁺: K²L⁸M⁸ (18 e)")],
  "2+8+7 = 17 e, zaryadsiz → Z = 17 — xlor atomi.",
  dict(arch="qavat_moslash"))

# 3 (2) — atom tarkibi
q(2, "yuqori",
  "³⁵Cl atomida proton, neytron va elektronlar soni mos ravishda qancha?",
  "17; 18; 17",
  [("17; 35; 17", "A — massa soni, neytron emas: n = A − Z"),
   ("18; 17; 18", "p = Z = 17"), ("17; 18; 18", "neytral atomda e = p")],
  "Z = 17 → p = e = 17; n = 35 − 17 = 18.",
  dict(arch="atom_tarkib"))

# 4 (3) — o'rtacha atom massasi
check("q4", 35*0.75 + 37*0.25, 35.5)
q(3, "yuqori",
  "Tabiiy xlor ³⁵Cl (75 %) va ³⁷Cl (25 %) izotoplaridan iborat. Xlorning o'rtacha atom massasini toping.",
  "35,5", [("36", "oddiy o'rta arifmetik olingan"), ("35", "faqat asosiy izotop"),
            ("35,75", "ulushlar teskari olingan... 35,75 xato")],
  "M = 35·0,75 + 37·0,25 = 26,25 + 9,25 = 35,5.",
  dict(arch="ortacha_massa"))

# 5 (3) — RASMLI: ionlanish energiyalari
q(3, "yuqori",
  "Rasmda X elementining ketma-ket ionlanish energiyalari berilgan: E₃ va E₄ orasida keskin sakrash bor. "
  "X atomining TASHQI qavatida nechta elektron bor?",
  "3", [("4", "sakrash 4-elektrondan keyin emas, oldin"), ("1", "unda E₁ va E₂ orasida sakrash bo'lardi"),
         ("8", "tashqi qavat to'la bo'lsa E₁ ning o'zi juda katta bo'lardi")],
  "Sakrash ichki (barqaror) qavatga o'tishni bildiradi: 3 ta e oson, 4-chisi ichki qavatdan → tashqi qavatda 3 e.",
  dict(arch="ionlanish_oqish"), fig="ion_energy")

# 6 (3) — konfiguratsiyadan element
q(3, "yuqori",
  "Elektron konfiguratsiyasi 1s²2s²2p⁶3s²3p⁴ bo'lgan element qaysi va u qaysi guruhda joylashgan?",
  "S; VI A", [("P; V A", "3p³ bo'lardi"), ("Cl; VII A", "3p⁵ bo'lardi"), ("Si; IV A", "3p² bo'lardi")],
  "Jami 16 e → oltingugurt; valent e: 3s²3p⁴ = 6 → VI A guruh.",
  dict(arch="konfig_element"))

# 7 (3) — orbitallar soni
q(3, "yuqori",
  "d-pog'onachada nechta orbital bor va unga eng ko'pi bilan nechta elektron sig'adi?",
  "5 ta orbital; 10 e",
  [("3 ta orbital; 6 e", "bu p-pog'onacha"), ("7 ta orbital; 14 e", "bu f-pog'onacha"),
   ("5 ta orbital; 5 e", "har orbitalga 2 tadan e sig'adi")],
  "d: 5 orbital × 2 e = 10 e.",
  dict(arch="d_orbital"))

# 8 (2) — yadro zaryadi
q(2, "yuqori",
  "Atom yadrosining zaryadi nimaga teng?",
  "protonlar soniga (tartib raqamiga)",
  [("neytronlar soniga", "neytron zaryadsiz"), ("elektronlar va protonlar yig'indisiga", "e yadroda emas"),
   ("massa soniga", "A = p + n, zaryad emas")],
  "Yadro zaryadi +Z — davriy sistemadagi tartib raqami.",
  dict(arch="yadro_zaryad"))

# 9 (2) — bosh kvant soni
q(2, "yuqori",
  "Bosh kvant soni (n) elektronning qaysi xususiyatini belgilaydi?",
  "energetik daraja (qavat) va orbital o'lchamini",
  [("orbital shaklini", "shaklni orbital (yonaki) kvant soni l belgilaydi"),
   ("orbitalning fazodagi yo'nalishini", "buni magnit kvant soni m belgilaydi"),
   ("elektronning o'z aylanishini", "buni spin kvant soni s belgilaydi")],
  "n = 1, 2, 3... — qavat raqami: n qancha katta bo'lsa, elektron yadrodan uzoq va energiyasi yuqori.",
  dict(arch="bosh_kvant"))

# 10 (3) — ion konfiguratsiyasi
q(3, "yuqori",
  "Fe²⁺ ionining elektron konfiguratsiyasi qaysi javobda to'g'ri berilgan?",
  "[Ar]3d⁶", [("[Ar]3d⁴4s²", "avval 4s elektronlari ketadi"), ("[Ar]3d⁵4s¹", "bu neytral Cr ga o'xshash xato"),
               ("[Ar]3d⁸", "faqat 2 e ketgan: 26−2=24 e, 3d⁶")],
  "Fe: [Ar]3d⁶4s². Ion hosil bo'lishida avval TASHQI 4s dan 2 e ketadi → [Ar]3d⁶.",
  dict(arch="ion_konfig"))

# 11 (3) — n-p farqidan element
check("q11", 39-19-19, 1)
q(3, "yuqori",
  "Massa soni 39 bo'lgan X atomida neytronlar soni protonlardan 1 taga ko'p. Elementni aniqlang.",
  "K (kaliy)", [("Ca", "Ca uchun Z=20: n=19 < p"), ("Ar", "Ar-39 uchun n−p=3"),
                 ("Sc", "Z=21: n=18 < p")],
  "p + n = 39, n = p + 1 → 2p = 38 → p = 19 — kaliy.",
  dict(arch="np_farq"))

# 12 (2) — izotoplar
q(2, "yuqori",
  "Izotoplar bir-biridan nimasi bilan farq qiladi?",
  "neytronlar soni (massa soni) bilan",
  [("protonlar soni bilan", "p farq qilsa boshqa element bo'lardi"),
   ("elektronlar soni bilan", "neytral izotoplarda e soni teng"),
   ("yadro zaryadi bilan", "zaryad bir xil — element bitta")],
  "Izotoplar: Z bir xil, A (n soni) har xil — masalan, ³⁵Cl va ³⁷Cl.",
  dict(arch="izotop_tarif"))

# 13 (3) — 1-2-3: izoelektron zarralar
q(3, "yuqori",
  "Quyidagi zarralarning qaysilari IZOELEKTRON (elektronlari soni teng)?\n"
  "1) Ne;  2) Na⁺;  3) Cl⁻;  4) Mg²⁺;  5) O²⁻.",
  "1, 2, 4 va 5",
  [("1, 2 va 3", "Cl⁻ da 18 e — qolganlarda 10 e"),
   ("hammasi", "Cl⁻ mos emas"),
   ("2, 3 va 4", "Cl⁻ chiqadi, Ne va O²⁻ kiradi")],
  "10 e: Ne(10), Na⁺(11−1), Mg²⁺(12−2), O²⁻(8+2). Cl⁻ esa 18 e.",
  dict(arch="izoelektron_tanlov"))

# 14 (3) — JADVALLI: zarralar «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni mos ravishda aniqlang:\n"
  "[JADVAL] Zarra | p | n | e ;; ²³Na⁺ | 11 | ? | ? ;; ³²S²⁻ | 16 | 16 | ?",
  "12; 10; 18",
  [("12; 11; 16", "Na⁺ da e = 11−1 = 10; S²⁻ da e = 16+2"),
   ("11; 10; 18", "n = 23 − 11 = 12"),
   ("12; 10; 16", "anion elektron biriktirgan: 18 e")],
  "Na⁺: n = 23−11 = 12, e = 10. S²⁻: e = 16+2 = 18.",
  dict(arch="zarra_jadval"))

# 15 (3) — teskari izotop ulushi
check("q15", (65-63.54)/2*100, 73)
q(3, "yuqori",
  "Mis ⁶³Cu va ⁶⁵Cu izotoplaridan iborat; o'rtacha atom massasi 63,54. ⁶³Cu ning ulushini (%) toping.",
  "73", [("27", "bu ⁶⁵Cu ulushi"), ("50", "teng deb olingan"), ("63", "massa bilan chalkashuv")],
  "63x + 65(1−x) = 63,54 → 2x = 1,46 → x = 0,73 → 73 %.",
  dict(arch="izotop_teskari"))

# 16 (2) — magnit kvant soni
q(2, "yuqori",
  "Orbital kvant soni l = 1 (p-pog'onacha) uchun magnit kvant soni (m) qanday qiymatlar oladi?",
  "−1, 0, +1",
  [("0, 1", "m manfiy qiymatlar ham oladi"), ("faqat 0", "bu l = 0 (s) uchun"),
   ("−2, −1, 0, +1, +2", "bu l = 2 (d) uchun")],
  "m = −l ... 0 ... +l: l=1 da 3 qiymat — shu bois p-pog'onachada 3 ta orbital bor.",
  dict(arch="magnit_kvant"))

# 17 (3) — JADVALLI: davr/guruhdan konfiguratsiya
q(3, "yuqori",
  "Jadvalda element o'rni berilgan:\n"
  "[JADVAL] Davr | Guruh ;; 3 | II A\n"
  "Uning tashqi qavat konfiguratsiyasini va elementni aniqlang.",
  "3s²; Mg", [("2s²; Be", "davr 3 — uchinchi qavat ochiladi"), ("3s¹; Na", "II A — 2 valent e"),
               ("3s²3p²; Si", "IV A bo'lardi")],
  "3-davr → n = 3; II A → s² → 3s², Z = 12 — magniy.",
  dict(arch="davr_guruh_jadval"))

# 18 (2) — valent elektronlar
q(2, "yuqori",
  "V A guruh (asosiy guruhcha) elementlarining tashqi qavatida nechta elektron bor?",
  "5", [("3", "III A uchun"), ("7", "VII A uchun"), ("15", "tartib raqami bilan chalkashuv")],
  "Asosiy guruhchada tashqi e soni guruh raqamiga teng: V A → 5 e (ns²np³).",
  dict(arch="valent_e"))

# 19 (3) — iondan element
check("q19", 18-2, 16)
q(3, "yuqori",
  "X²⁻ ionida 18 ta elektron bor. X elementini aniqlang.",
  "S", [("Ar", "Ar ion hosil qilmaydi (18 e — atomida)"), ("Ca", "Ca²⁺ da 18 e, lekin u kation"),
         ("O", "O²⁻ da 10 e")],
  "Atomda e = 18 − 2 = 16 → Z = 16 — oltingugurt.",
  dict(arch="ion_element"))

# 20 (2) — qavat sig'imi
q(2, "yuqori",
  "n-qavatning maksimal elektron sig'imi qaysi formula bilan topiladi?",
  "2n²", [("n²", "2 koeffitsiyenti tushib qolgan"), ("2n", "chiziqli emas, kvadratik"),
           ("8n", "faqat 2-qavat uchun tasodifan 8 emas")],
  "N = 2n²: K(2), L(8), M(18), N(32).",
  dict(arch="qavat_sigim"))

# 21 (3) — «sakragan» konfiguratsiya
q(3, "yuqori",
  "4-davr elementining konfiguratsiyasi ...3d⁵4s¹ bilan tugaydi. Bu element qaysi va nega shunday?",
  "Cr — yarim to'lgan 3d⁵ barqarorroq (elektron «sakrashi»)",
  [("Mn — oddiy tartib", "Mn: 3d⁵4s²"), ("V — 3d³4s²", "berilgan konfiguratsiya V niki emas"),
   ("Fe — 3d⁶4s²", "mos emas")],
  "Xrom (Z=24): 4s dan bitta e 3d ga «sakraydi» — 3d⁵ yarim to'la holat energetik qulay.",
  dict(arch="sakrash_konfig"))

# 22 (3) — 1-2-3: qo'zg'algan holatlar
q(3, "yuqori",
  "Qaysi konfiguratsiyalar atomning QO'ZG'ALGAN holatiga mos keladi?\n"
  "1) 1s²2s¹2p¹;  2) 1s²2s²2p²;  3) 1s²2s¹2p³;  4) 1s²2s²2p⁶.",
  "1 va 3",
  [("2 va 4", "bular asosiy (eng past energiyali) holatlar"),
   ("faqat 1", "3-da ham 2s dan e ko'chgan (C* holati)"),
   ("1, 2 va 3", "2 — uglerodning asosiy holati")],
  "Qo'zg'alishda juftlangan e yuqoriroq pog'onachaga ko'chadi: Be* (2s¹2p¹) va C* (2s¹2p³).",
  dict(arch="qozgalgan_tanlov"))

# 23 (3) — proton mollari
check("q23", 40/40*20, 20)
q(3, "yuqori",
  "40 g kalsiyda necha mol proton bor? (M(Ca)=40, Z=20)",
  "20", [("1", "atom mollari — proton emas"), ("40", "massa soni olingan"), ("0,5", "asossiz bo'lish")],
  "n(Ca) = 1 mol; har atomda 20 p → 20 mol proton.",
  dict(arch="proton_mol"))

# 24 (2) — davr raqami
q(2, "yuqori",
  "Elementning davr raqami nimani ko'rsatadi?",
  "elektron qavatlar sonini",
  [("valent elektronlar sonini", "buni (asosiy guruhda) guruh raqami ko'rsatadi"),
   ("neytronlar sonini", "davriy jadval n ni bermaydi"),
   ("izotoplar sonini", "izotoplar davrga bog'liq emas")],
  "3-davr elementi — 3 qavatli atom (K, L, M).",
  dict(arch="davr_raqam"))

# 25 (3) — radius qatori
q(3, "yuqori",
  "Qaysi qatorda atom radiusi ORTIB borishi to'g'ri ko'rsatilgan?",
  "F → Cl → Br → I",
  [("I → Br → Cl → F", "bu kamayish tartibi"), ("Na → Mg → Al → Si", "davrda radius kamayadi"),
   ("Cs → K → Na → Li", "guruhda yuqoriga kamayadi")],
  "Guruhda pastga qavatlar soni ortadi → radius kattalashadi.",
  dict(arch="radius_qator"))

# 26 (3) — RASMLI: izotop ustunlari
check("q26", 24*0.79 + 25*0.10 + 26*0.11, 24.32, tol=0.01)
q(3, "yuqori",
  "Diagrammada magniy izotoplarining tabiiy ulushlari berilgan. Magniyning o'rtacha atom massasini "
  "hisoblang (yuzdan birgacha).",
  "24,32", [("25", "oddiy o'rta arifmetik"), ("24", "faqat asosiy izotop"), ("24,5", "taxminiy xato")],
  "M = 24·0,79 + 25·0,10 + 26·0,11 = 18,96 + 2,5 + 2,86 = 24,32.",
  dict(arch="izotop_bars_hisob"), fig="isotope_bars")

# 27 (3) — ion elektronlari yig'indisi
check("q27", 7+4-1, 10)
q(3, "yuqori",
  "Ammoniy ioni (NH₄⁺) tarkibidagi elektronlar sonini aniqlang.",
  "10", [("11", "musbat zaryad e YO'QOLGANINI bildiradi"), ("9", "zaryad ikki marta ayirilgan"),
          ("7", "vodorodlar unutilgan")],
  "N(7) + 4H(4) = 11 e; «+» zaryad → 1 e kam: 10 e.",
  dict(arch="ion_e_yigindi"))

# 28 (2) — RASMLI: atom modeli
q(2, "yuqori",
  "Rasmdagi atom modelida qaysi zarralar YADRODA joylashgan?",
  "protonlar va neytronlar",
  [("elektronlar va protonlar", "elektronlar qavatlarda aylanadi"),
   ("faqat protonlar", "neytronlar ham yadroda"),
   ("barcha zarralar", "elektronlar yadrodan tashqarida")],
  "Yadro: p + n (nuklonlar); elektronlar — atrofdagi qavatlarda.",
  dict(arch="model_oqish"), fig="atom_model")

# 29 (3) — Klechkovskiy (n+l) tartibi
q(3, "yuqori",
  "3p, 3d, 4s, 4p pog'onachalarini elektron bilan TO'LISH tartibida joylashtiring.",
  "3p → 4s → 3d → 4p",
  [("3p → 3d → 4s → 4p", "n+l: 4s(4) 3d(5) dan oldin to'ladi"),
   ("4s → 3p → 3d → 4p", "3p(4... aniqrog'i n+l=4, n kichik) birinchi"),
   ("3p → 4s → 4p → 3d", "4p(5) va 3d(5): n kichigi (3d) oldin")],
  "Klechkovskiy qoidasi: n+l kichigi oldin; teng bo'lsa n kichigi. 3p(4) → 4s(4) → 3d(5) → 4p(5).",
  dict(arch="klechkovskiy"))

# 30 (2) — qo'zg'algan holat ta'rifi
q(2, "yuqori",
  "Atomning QO'ZG'ALGAN holati nima?",
  "elektron energiya yutib yuqoriroq pog'onachaga o'tgan holat",
  [("atom elektron yo'qotgan holat", "bu ion holati"),
   ("yadro parchalangan holat", "bu yadro reaksiyasi"),
   ("atom harakatlanayotgan holat", "mexanik harakat emas, elektron holati")],
  "Qo'zg'alish — vaqtinchalik: e qaytishida energiya (yorug'lik) chiqaradi.",
  dict(arch="qozgalgan_tarif"))

# 31 (3) — atomlar sonidan element
check("q31", 48/2, 24)
q(3, "yuqori",
  "12,04·10²³ ta atomdan iborat metallning massasi 48 g. Metallni aniqlang.",
  "Mg", [("Ca", "M=40 bo'lardi (80 g)"), ("Cu", "M=64 (128 g)"), ("C", "uglerod metall emas")],
  "n = 12,04·10²³/6,02·10²³ = 2 mol → M = 48/2 = 24 g/mol — magniy.",
  dict(arch="atom_soni_element"))

# 32 (3) — RASMLI: ionlanish energiyasidan guruh
q(3, "yuqori",
  "5-savoldagi rasmdan foydalaning: X elementi qaysi guruhda joylashgan?",
  "III A", [("IV A", "sakrash E₄ dan keyin bo'lardi"), ("I A", "sakrash E₁ dan keyin bo'lardi"),
             ("VIII A", "inert gazlarda E₁ ning o'zi maksimal")],
  "Tashqi qavatda 3 e (5-savol) → III A guruh (masalan, Al).",
  dict(arch="ionlanish_guruh"), fig="ion_energy")

# ---------- Y2: uch zarra ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.1",
  ichki_pasport=[dict(n=33, element="I.1", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.1", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch zarra tavsifi berilgan: X — 11 p, 12 n, 10 e; Y — 17 p, 18 n, 18 e; "
               "Z — 10 p, 10 n, 10 e. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X zarra nima?",
    "34. Y zarraning massa soni qancha?",
    "35. Qaysi zarralar o'zaro izoelektron?"],
  javoblar_royxati=["A) Na⁺ (kation)", "B) 35", "C) X va Z", "D) Cl atomi", "E) 33", "F) Y va Z"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="Y da e=18 ≠ p — bu Cl⁻ ioni, atom emas"),
                   dict(variant="E", xato="p+e yig'indisi — massa soni p+n bo'ladi"),
                   dict(variant="F", xato="Y da 18 e, Z da 10 e — teng emas")],
  yechim=("X: p=11, e=10 → Na⁺ (A). Y: A = 17+18 = 35 (B). "
          "Izoelektron: X (10 e) va Z (10 e) → C."),
  parametrlar=dict(arch="zarra_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36", 4.8/0.2, 24); check("o36b", 12+13, 25)
check("o37", 6/24*12, 3)
check("o38", 0.1*2*108, 21.6)
check("o39", (7-6.9)/1*100, 10, tol=0.5); check("o39b", 0.9*6.02, 5.42, tol=0.01)
check("o40", 0.2*12+0.2*14, 5.2)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="4,8 g X metalida 1,204\u00b710\u00b2\u00b3 ta atom bor. Shu metallning yadrosida 13 ta neytron "
            "tutgan izotopining MASSA SONINI aniqlang.",
      javob="25", yechim="n = 0,2 mol \u2192 M = 24 \u2192 Mg (Z=12); A = 12 + 13 = 25 (\u00b2\u2075Mg).",
      parametrlar=dict(arch="massa_son_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="X\u00b2\u207a ionida 10 ta elektron bor; yadrosida 12 ta neytron. Shu izotopning 6 g miqdoridagi "
            "NEYTRONLAR mol sonini toping.",
      javob="3", yechim="e+2 = 12 = Z \u2192 Mg; A = 24 \u2192 n(atom) = 0,25 mol \u2192 neytron = 0,25\u00b712 = 3 mol.",
      parametrlar=dict(arch="ion_neytron_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi jarayonda 0,1 mol magniy to'liq ionlashib, ajralgan BARCHA elektronlar Ag\u207a "
            "ionlarini qaytardi. Hosil bo'lgan kumushning massasini (g) toping. (M(Ag)=108)",
      javob="21,6", yechim="Mg \u2212 2e \u2192 Mg\u00b2\u207a: e = 0,2 mol \u2192 Ag = 0,2 mol \u2192 21,6 g.",
      parametrlar=dict(arch="sxema_elektron"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Tabiiy litiy \u2076Li va \u2077Li izotoplaridan iborat, o'rtacha atom massasi 6,9. "
            "6,9 g litiydagi \u2077Li atomlari sonini aniqlang (\u00b710\u00b2\u00b3).",
      javob="5,42", yechim="6x+7(1\u2212x)=6,9 \u2192 x=0,1 \u2192 \u2077Li 90%. n=1 mol \u2192 0,9\u00b76,02\u00b710\u00b2\u00b3 = 5,42\u00b710\u00b2\u00b3.",
      parametrlar=dict(arch="izotop_atom_soni")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Teng mol miqdorda olingan \u00b2\u2074Mg va \u00b2\u2076Mg izotoplaridan iborat 10 g aralashmadagi "
            "neytronlarning umumiy mol sonini toping.",
      javob="5,2", yechim="O'rtacha M = 25 \u2192 jami 0,4 mol (0,2+0,2). Neytron: 0,2\u00b712 + 0,2\u00b714 = 5,2 mol.",
      parametrlar=dict(arch="izotop_aralash_neytron")),
]

# ---------- O2 ----------
check("o41c", 10.8*0.199 + 11*0.801, 10.96, tol=0.01)
check("o43b", 39+19+20+19, 97)
O2 = [
 dict(n=41, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. Tabiiy bor (B) ikkita izotopdan iborat: ¹⁰B (ulushi 19,9 %) va ¹¹B (80,1 %). "
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir izotopning yadro tarkibini (p, n) yozing.",
             yechim=["¹⁰B: 5p, 5n; ¹¹B: 5p, 6n (Z=5 — bir xil)."], M=3, A=2),
        dict(savol="b) Nega ikkala izotop ham «bor» elementi hisoblanadi?",
             yechim=["Protonlar soni bir xil (Z=5) — element aynan Z bilan belgilanadi."], M=3, A=1),
        dict(savol="c) Borning o'rtacha atom massasini hisoblang.",
             yechim=["M = 10·0,199 + 11·0,801 = 1,99 + 8,81 ≈ 10,8"], M=4, A=3),
        dict(savol="d) Nega davriy jadvaldagi atom massalari butun son emas? Izohlang.",
             yechim=["Jadvalda izotoplarning tabiiy ulushlar bo'yicha O'RTACHA massasi beriladi."], M=3, A=2),
        dict(savol="e) ¹⁰B va ¹¹B ning kimyoviy xossalari farq qiladimi? Sababini yozing.",
             yechim=["Deyarli farq qilmaydi: kimyoviy xossa elektron qavatga (Z ga) bog'liq, n soniga emas."], M=2, A=2),
      ],
      rasmiylashtirish="Izotop zanjiri: tarkib → tushuncha → o'rtacha massa → izohlar; M15+A10.",
      parametrlar=dict(arch="izotop_zanjir")),
 dict(n=42, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Noma'lum X elementi haqida ma'lumot: u 3-davrda joylashgan, tashqi qavatida 2 ta elektron "
            "bor. Quyidagilarni MULOHAZA bilan bajaring (davriy jadvaldan nusxa ko'chirmasdan)."),
      bandlar=[
        dict(savol="a) X ning to'liq elektron konfiguratsiyasini keltirib chiqarish yo'lini bosqichma-bosqich "
                   "yozing va elementni aniqlang.",
             yechim=["3-davr → 3 qavat; tashqi 3s² → to'liq: 1s²2s²2p⁶3s² → 12 e → Z=12 — magniy."], M=13, A=0),
        dict(savol="b) X qanday ion hosil qiladi va nega aynan shunday?",
             yechim=["Mg²⁺: 2 ta tashqi e ni berib, barqaror 8 e li (neon kabi) qavatga erishadi."], M=9, A=0),
        dict(savol="c) X oksidining formulasini yozing.",
             yechim=["MgO (Mg²⁺ va O²⁻)."], M=3, A=0),
      ],
      rasmiylashtirish="Element-detektiv (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="element_detektiv")),
 dict(n=43, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch zarraning tarkibi jadvalda berilgan:\n"
            "[JADVAL] Zarra | p | n | e ;; X | 19 | 20 | 18 ;; Y | 19 | 21 | 19 ;; Z | 18 | 22 | 18\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir zarrani tavsiflang: atommi yoki ionmi, qaysi element?",
             yechim=["X: p≠e → K⁺ ioni; Y: p=e → K atomi (⁴⁰K izotopi); Z: p=e → Ar atomi (⁴⁰Ar)."], M=5, A=2),
        dict(savol="b) X va Y ning massa sonlari yig'indisini toping.",
             yechim=["A(X)=39, A(Y)=40 → 79... aniqrog'i: 39+40=79"], M=4, A=3),
        dict(savol="c) Qaysi juftlik izotoplar? Qaysi juftlik izoelektron? Asoslang.",
             yechim=["X va Y — izotop juft manbai (ikkalasi K, Z=19); X va Z — izoelektron (18 e)."], M=3, A=3),
        dict(savol="d) Y va Z ning massa sonlari teng (40). Nega ular baribir HAR XIL element?",
             yechim=["Element Z (proton) bilan belgilanadi: 19 ≠ 18. Bunday zarralar izobaralar deyiladi."], M=3, A=2),
      ],
      rasmiylashtirish="Zarra-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="zarra_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260111)
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
    d = dict(n=n, tur="Y1", element="I.1", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I1-B", daraja="B", bob=1, bob_nomi="Atom tuzilishi",
    manba=("Tongotarov 1-5-variantlari arxetiplari (ion elektronlari, K-L-M moslash, konfiguratsiyalar) — "
           "javoblar mustaqil tekshirilgan; MS spetsifikatsiyasi I.1"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: izotop hisoblari, ion konfiguratsiyalari, "
          "ionlanish energiyalari grafigi, izoelektron tanlovlar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
