# -*- coding: utf-8 -*-
"""1-bob A-varianti: Atom tuzilishi (I.1) — O'RGATUVCHI ★★.
Hayotiy sahnalar: alanga testi, neon reklama, tibbiy rentgen, banan (K-40)."""
import json, random

OUT = "mavzu_I1A.json"
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
  "Atom qanday zarralardan tashkil topgan?",
  "yadro (proton + neytron) va elektronlardan",
  [("faqat elektronlardan", "yadro ham bor"), ("faqat proton va elektronlardan", "yadroda neytron ham bor"),
   ("molekulalardan", "molekula atomlardan tuziladi, aksincha emas")],
  "Markazda zich yadro (p, n), atrofida yengil elektronlar.",
  dict(arch="atom_tarkib_oddiy"))

# 2 (2)
q(2, "quyi",
  "Qaysi zarra MANFIY zaryadga ega?",
  "elektron", [("proton", "zaryadi +1"), ("neytron", "zaryadsiz"), ("yadro", "yadro musbat")],
  "e⁻: zaryadi −1, massasi eng kichik.",
  dict(arch="zaryad_oddiy"))

# 3 (2)
q(2, "o'rta",
  "Elementning tartib raqami (Z) nimani bildiradi?",
  "yadrodagi protonlar sonini",
  [("neytronlar sonini", "n = A − Z dan topiladi"), ("massa sonini", "massa soni — A"),
   ("qavatlar sonini", "qavatlar soni — davr raqami")],
  "Z = p = (neytral atomda) e soni.",
  dict(arch="z_oddiy"))

# 4 (2) — SAHNA: alanga testi
q(2, "o'rta",
  "Rasmga qarang: osh tuzi alangaga tutilsa, alanga SARIQ rangga bo'yaladi. Buning sababi nimada?",
  "natriy atomlarida elektronlar sakrab, energiyani sariq yorug'lik sifatida chiqaradi",
  [("tuz yonib ketadi", "NaCl yonmaydi — rang elektron o'tishlaridan"),
   ("alanga tuzni eritadi", "erish rang bermaydi"),
   ("xlor sariq rang beradi", "rang metallga (Na ga) xos")],
  "Qizdirilganda elektron yuqori pog'onaga ko'chadi, qaytishida Na ga xos sariq nur chiqaradi — "
  "alanga testi shu hodisaga asoslangan.",
  dict(arch="alanga_sahna"), fig="flame")

# 5 (2)
q(2, "o'rta",
  "Massa soni (A) qanday topiladi?",
  "A = protonlar + neytronlar",
  [("A = protonlar + elektronlar", "elektron massasi hisobga olinmaydi"),
   ("A = neytronlar − protonlar", "bu farq, massa soni emas"),
   ("A = 2·Z har doim", "faqat ba'zi yengil elementlarda")],
  "A — yadrodagi nuklonlar (p + n) soni.",
  dict(arch="massa_son_oddiy"))

# 6 (3)
check("q6", 23-11, 12)
q(3, "o'rta",
  "²³Na atomidagi neytronlar sonini toping.",
  "12", [("11", "protonlar soni"), ("23", "massa soni"), ("34", "yig'indi olingan")],
  "n = A − Z = 23 − 11 = 12.",
  dict(arch="n_hisob_oddiy"))

# 7 (2)
q(2, "o'rta",
  "Neytral atomda elektronlar soni nimaga teng?",
  "protonlar soniga",
  [("neytronlar soniga", "n soni farq qilishi mumkin"), ("massa soniga", "A ≫ e soni"),
   ("qavatlar soniga", "qavatlar ancha kam")],
  "Zaryadlar tengligi: e = p = Z.",
  dict(arch="e_teng_oddiy"))

# 8 (2) — SAHNA: neon reklama
q(2, "o'rta",
  "Rasmda tungi shahar — rangli neon reklamalar. Naychalardagi gaz nega yorug'lik taratadi?",
  "tok ta'sirida qo'zg'algan elektronlar qaytishida yorug'lik chiqaradi",
  [("gaz yonadi", "naycha ichida yonish yo'q — kislorod kiritilmaydi"),
   ("naycha qizib ketadi", "neon «sovuq» yorug'lik beradi"),
   ("bo'yalgan shisha", "rang gazning o'ziga (Ne — qizil, Ar — ko'k...) bog'liq")],
  "Elektr toki elektronlarni qo'zg'atadi; ular asosiy holatga qaytishda gazga xos rangli nur taratadi.",
  dict(arch="neon_sahna"), fig="neon")

# 9 (2)
q(2, "o'rta",
  "Birinchi (K) elektron qavatga eng ko'pi bilan nechta elektron sig'adi?",
  "2", [("8", "L qavat sig'imi"), ("18", "M qavat sig'imi"), ("1", "vodorodda 1 e bor, sig'im 2")],
  "2n²: n=1 → 2 e.",
  dict(arch="k_qavat"))

# 10 (3)
q(3, "o'rta",
  "Natriy (Z=11) atomining elektron qavatlari bo'yicha taqsimoti qaysi javobda to'g'ri?",
  "2, 8, 1", [("2, 9", "L qavatga 8 tadan ortiq sig'maydi"), ("8, 2, 1", "ichkaridan boshlanadi: K=2"),
               ("2, 8, 8", "jami 18 bo'lardi (argon)")],
  "11 e: K—2, L—8, M—1. Tashqi 1 e — natriyning «faol» elektroni.",
  dict(arch="na_taqsimot"))

# 11 (2)
q(2, "o'rta",
  "Izotoplar deb nimaga aytiladi?",
  "protonlari bir xil, neytronlari har xil atomlarga",
  [("elektronlari har xil atomlarga", "neytral atomda e = p — u ham bir xil"),
   ("har qanday ikki elementga", "izotoplar BITTA elementning turlari"),
   ("zaryadlari har xil zarralarga", "zaryad (Z) bir xil bo'ladi")],
  "Masalan: ¹H, ²H, ³H — vodorod izotoplari.",
  dict(arch="izotop_oddiy"))

# 12 (3)
check("q12", 12*0.99 + 13*0.01, 12.01, tol=0.02)
q(3, "o'rta",
  "Uglerod asosan ¹²C (99 %) va ¹³C (1 %) dan iborat. O'rtacha atom massasi taxminan qancha?",
  "12,01", [("12,5", "oddiy o'rta olingan"), ("13", "kam uchraydigan izotop olingan"),
             ("25", "yig'indi olingan")],
  "12·0,99 + 13·0,01 = 11,88 + 0,13 ≈ 12,01.",
  dict(arch="ortacha_oddiy"))

# 13 (2) — SAHNA: rentgen
q(2, "o'rta",
  "Rasmda tibbiy rentgen surati. Rentgen nurlari qayerda «to'xtab» suratda oq soya beradi?",
  "og'ir atomli to'qimalarda (suyak — kalsiy) yutiladi",
  [("faqat teri ushlab qoladi", "teri yengil atomlardan — nur o'tib ketadi"),
   ("nur hech narsadan o'tmaydi", "yumshoq to'qimalardan bemalol o'tadi"),
   ("suyak nur chiqaradi", "suyak nurni YUTADI, chiqarmaydi")],
  "Atom qancha og'ir (Z katta) bo'lsa, rentgen nurini shuncha kuchli yutadi — suyaklar oq ko'rinadi.",
  dict(arch="rentgen_sahna"), fig="xray")

# 14 (3)
check("q14", 2*9, 18)
q(3, "o'rta",
  "Uchinchi (M) qavatning maksimal sig'imini toping.",
  "18", [("8", "faqat 3s+3p hisoblangan"), ("32", "N qavat sig'imi"), ("9", "2 ga ko'paytirilmagan")],
  "2n² = 2·3² = 18 e (3s² 3p⁶ 3d¹⁰).",
  dict(arch="m_sigim"))

# 15 (2)
q(2, "o'rta",
  "Qaysi yozuv KISLOROD atomining to'g'ri elektron konfiguratsiyasi? (Z=8)",
  "1s²2s²2p⁴",
  [("1s²2s²2p⁶", "bu neon (10 e)"), ("1s²2s⁴2p²", "s ga 2 tadan ortiq sig'maydi"),
   ("1s⁴2s⁴", "s-orbital sig'imi 2")],
  "8 e: 2 + 2 + 4.",
  dict(arch="o_konfig"))

# 16 (3)
q(3, "o'rta",
  "Element 2-davr, VII A guruhda joylashgan. Bu qaysi element?",
  "F", [("Cl", "3-davrda"), ("O", "VI A guruhda"), ("N", "V A guruhda")],
  "2-davr, 7 valent e → ftor (2s²2p⁵).",
  dict(arch="davr_guruh_oddiy"))

# 17 (2)
q(2, "o'rta",
  "Jadvaldagi «?» katakni to'ldiring:\n"
  "[JADVAL] Zarra | p | e ;; Mg atomi | 12 | 12 ;; Mg²⁺ ioni | 12 | ?",
  "10", [("12", "ion 2 e YO'QOTGAN"), ("14", "kation e yo'qotadi, olmaydi"), ("2", "qolgan e so'raldi")],
  "Mg²⁺: 12 − 2 = 10 e.",
  dict(arch="ion_jadval_oddiy"))

# 18 (2) — SAHNA: banan
q(2, "o'rta",
  "Rasmda banan tasvirlangan. Banan tarkibidagi kaliyning oz qismi tabiiy radioaktiv ⁴⁰K izotopidir. "
  "⁴⁰K va oddiy ³⁹K atomlari bir-biridan nimasi bilan farq qiladi?",
  "neytronlar soni bilan (21 va 20)",
  [("protonlar soni bilan", "ikkalasida ham 19 p — ikkalasi ham kaliy"),
   ("elektronlar soni bilan", "neytral atomlarda 19 tadan"),
   ("umuman farq qilmaydi", "massa (neytron) farqi bor")],
  "Izotoplar: Z=19 bir xil; n = 40−19 = 21 va 39−19 = 20. ⁴⁰K juda oz — banan mutlaqo xavfsiz!",
  dict(arch="banan_sahna"), fig="banana")

# 19 (3)
check("q19", 40-20, 20)
q(3, "o'rta",
  "⁴⁰Ca atomida nechta neytron bor? (Z=20)",
  "20", [("40", "massa soni"), ("60", "yig'indi"), ("10", "yarmi olingan")],
  "n = 40 − 20 = 20 (p = n).",
  dict(arch="ca_neytron"))

# 20 (2)
q(2, "o'rta",
  "Atomdagi elektronning holatini TO'LIQ tavsiflash uchun nechta kvant soni ishlatiladi?",
  "4 ta (n, l, m, s)",
  [("2 ta", "qavat va pog'onachadan tashqari yo'nalish va spin ham bor"),
   ("3 ta", "spin kvant soni (s) ham hisobga olinadi"),
   ("8 ta", "kvant sonlari to'rtta — 8 bu qavat sig'imi")],
  "n — qavat, l — pog'onacha (shakl), m — yo'nalish, s — spin: to'rttasi elektron «manzili».",
  dict(arch="kvant_soni_oddiy"))

# 21 (3)
check("q21", 19, 19)
q(3, "o'rta",
  "X⁺ ionida 18 ta elektron bor. X elementini aniqlang.",
  "K", [("Ar", "u ion hosil qilmaydi"), ("Cl", "Cl⁻ da 18 e — u anion"), ("Ca", "Ca²⁺ da 18 e")],
  "Atomda e = 18 + 1 = 19 → kaliy.",
  dict(arch="ion_element_oddiy"))

# 22 (2)
q(2, "o'rta",
  "s-orbital qanday shaklga ega?",
  "shar (sfera)", [("gantel", "bu p-orbital"), ("halqa", "orbital halqa emas"), ("kub", "bunday orbital yo'q")],
  "s — sferik simmetrik; p — gantelsimon.",
  dict(arch="s_shakl"))

# 23 (3)
check("q23", 2+8+5, 15)
q(3, "o'rta",
  "Elektron qavatlari 2, 8, 5 bo'lgan element qaysi?",
  "P", [("N", "2, 5 bo'lardi"), ("As", "4 qavatli"), ("Al", "2, 8, 3")],
  "Jami 15 e → fosfor (3-davr, V A).",
  dict(arch="qavat_element"))

# 24 (2)
q(2, "o'rta",
  "Kation qanday hosil bo'ladi?",
  "atom elektron BERIB, musbat zaryadlanadi",
  [("atom elektron olib", "bu anion hosil bo'lishi"), ("atom proton berib", "protonlar yadrodan chiqmaydi"),
   ("atom neytron olib", "neytron zaryadga ta'sir qilmaydi")],
  "Me − ne⁻ → Meⁿ⁺ (masalan, Na⁺, Mg²⁺).",
  dict(arch="kation_oddiy"))

# 25 (3)
q(3, "o'rta",
  "Qaysi zarralar juftligi IZOELEKTRON (elektronlari teng)?",
  "F⁻ va Ne", [("Na⁺ va K⁺", "10 va 18 e"), ("Cl⁻ va F⁻", "18 va 10 e"), ("O²⁻ va S²⁻", "10 va 18 e")],
  "F⁻: 9+1 = 10 e; Ne: 10 e — teng.",
  dict(arch="izoelektron_oddiy"))

# 26 (3) — RASMLI: izotop ustunlari (oddiy o'qish)
q(3, "o'rta",
  "Diagrammada magniy izotoplarining tabiiy ulushlari berilgan. Qaysi izotop tabiatda ENG KO'P uchraydi?",
  "²⁴Mg", [("²⁵Mg", "ulushi ~10 %"), ("²⁶Mg", "ulushi ~11 %"), ("hammasi teng", "ustunlar farqli")],
  "Diagrammadan: ²⁴Mg ≈ 79 % — eng baland ustun.",
  dict(arch="izotop_bars_oddiy"), fig="isotope_bars")

# 27 (3)
check("q27", 0.5*6, 3)
q(3, "o'rta",
  "0,5 mol uglerodda (¹²C) necha mol proton bor? (Z=6)",
  "3", [("6", "1 mol uchun qiymat"), ("0,5", "atom mollari"), ("12", "massa soni bilan chalkashuv")],
  "0,5 · 6 = 3 mol proton.",
  dict(arch="proton_mol_oddiy"))

# 28 (2) — RASMLI: atom modeli
q(2, "o'rta",
  "Rasmdagi Bor modelida elektronlar qayerda joylashgan?",
  "yadro atrofidagi qavatlarda (orbitalarda)",
  [("yadro ichida", "yadroda p va n"), ("atomdan tashqarida", "elektron atomga tegishli"),
   ("qavatlar orasida tartibsiz", "har e o'z qavatida")],
  "Bor modeli: e lar aniq energiyali qavatlarda aylanadi.",
  dict(arch="model_oddiy"), fig="atom_model")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "I A guruhda yuqoridan pastga (Li → Na → K → ...) atom radiusi qanday o'zgaradi? Grafikni tanlang.",
  "ortib boradi",
  [("kamayadi", "qavatlar soni ortadi — radius kattalashadi"),
   ("o'zgarmaydi", "har davrda yangi qavat qo'shiladi"),
   ("avval ortib, keyin kamayadi", "monoton ortadi")],
  "Har qadam yangi elektron qavat → radius ortadi.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="u", xlab="Li→Cs", ylab="r"),
  params=dict(arch="radius_grafik"))

# 30 (2)
q(2, "o'rta",
  "Atom tuzilishi haqidagi fikrlardan XATOSINI toping.",
  "elektronlar yadro ichida joylashgan",
  [("atom massasining asosiy qismi yadroda", "to'g'ri — e juda yengil"),
   ("yadro atomga nisbatan juda kichik", "to'g'ri fikr"),
   ("elektronlar qavatlarda joylashadi", "to'g'ri fikr")],
  "Elektronlar yadro ATROFIDA; yadroda faqat p va n.",
  dict(arch="xato_fikr"))

# 31 (3)
check("q31", 27/27, 1)
q(3, "o'rta",
  "27 g alyuminiyda nechta atom bor? (M(Al)=27)",
  "6,02·10²³", [("27·10²³", "mol tushunchasi qo'llanmagan"), ("3,01·10²³", "0,5 mol xato"),
                 ("13·10²³", "Z bilan chalkashuv")],
  "n = 1 mol → Nₐ = 6,02·10²³ ta atom.",
  dict(arch="atom_soni_oddiy"))

# 32 (3) — RASMLI: qavatlar modeli o'qish
q(3, "o'rta",
  "28-savoldagi modelda qavatlar 2, 8, 1 elektronli. Bu qaysi element va u qanday ion hosil qiladi?",
  "Na; Na⁺", [("Li; Li⁺", "Li: 2, 1 — ikki qavat"), ("K; K⁺", "K: 2, 8, 8, 1 — to'rt qavat"),
               ("Mg; Mg²⁺", "Mg: 2, 8, 2")],
  "2+8+1 = 11 e → natriy; tashqi 1 e ni berib Na⁺ bo'ladi.",
  dict(arch="model_element"), fig="atom_model")

# ---------- Y2: alanga testi ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.1",
  ichki_pasport=[dict(n=33, element="I.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Laboratoriyada uch idishdagi oq tuzlar alanga testi bilan tekshirildi: X tuz alangani "
               "SARIQ, Y tuz BINAFSHA rangga bo'yadi, Z tuz esa rang bermadi. Tuzlar NaCl, KCl va MgCl₂ "
               "ekani ma'lum. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X tuz tarkibidagi metall qaysi?",
    "34. Y tuz qaysi modda?",
    "35. Z tuz metallining ionida nechta elektron bor?"],
  javoblar_royxati=["A) Na", "B) KCl", "C) 10", "D) K", "E) NaCl", "F) 12"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="binafsha — kaliy; sariq esa natriy"),
                   dict(variant="E", xato="X ning o'zi NaCl, lekin savol metall haqida"),
                   dict(variant="F", xato="Mg²⁺ ATOMdagi emas, iondagi e: 12−2=10")],
  yechim=("Sariq — Na (A); binafsha — K → KCl (B). Z — MgCl₂: Mg²⁺ da 12−2 = 10 e (C)."),
  parametrlar=dict(arch="alanga_ssenariy"))

# ---------- O1 ----------
check("o37", 16+16, 32)
check("o38", 2+8+7, 17)
check("o39", 0.5*10, 5)
check("o40", 12.04/6.02, 2)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="Kaliy (Z=19) atomining elektron qavatlari bo'yicha taqsimotini yozing.",
      javob="2, 8, 8, 1", yechim="19 e: K—2, L—8, M—8, N—1.",
      parametrlar=dict(arch="taqsimot_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Yadrosida 16 proton va 16 neytron bo'lgan atomning massa sonini toping.",
      javob="32", yechim="A = 16 + 16 = 32 (³²S).",
      parametrlar=dict(arch="a_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="Elektron qavatlari 2, 8, 7 bo'lgan elementning tartib raqamini toping.",
      javob="17", yechim="2+8+7 = 17 — xlor.",
      parametrlar=dict(arch="z_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="0,5 mol neonda (Z=10) necha mol elektron bor?",
      javob="5", yechim="0,5·10 = 5 mol e.",
      parametrlar=dict(arch="e_mol_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="12,04·10²³ ta atomi 32 g keladigan elementning molyar massasini toping.",
      javob="16", yechim="n = 2 mol → M = 32/2 = 16 g/mol (kislorod).",
      parametrlar=dict(arch="m_topish_o1")),
]

# ---------- O2 ----------
check("o41b", 23-11, 12)
O2 = [
 dict(n=41, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("²³Na atomi haqida bandlar ketma-ket yechiladi — har biri keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) Atomdagi p, n, e sonlarini aniqlang.",
             yechim=["Z=11 → p=e=11; n = 23−11 = 12"], M=3, A=2),
        dict(savol="b) Elektron qavatlar bo'yicha taqsimotini va to'liq konfiguratsiyasini yozing.",
             yechim=["2, 8, 1; 1s²2s²2p⁶3s¹"], M=4, A=2),
        dict(savol="c) Natriy qanday ion hosil qiladi? Ion konfiguratsiyasini yozing.",
             yechim=["Na⁺ (3s¹ e ketadi): 1s²2s²2p⁶ — neonga izoelektron"], M=3, A=2),
        dict(savol="d) Nega natriy aynan +1 zaryadli ion hosil qiladi? Izohlang.",
             yechim=["Bitta e berish 8 e li barqaror qavatga olib keladi; 2-e ni ichki qavatdan olish juda qiyin."], M=3, A=2),
        dict(savol="e) Na va Na⁺ ning o'lchamlarini solishtiring va sababini yozing.",
             yechim=["Na⁺ kichikroq: tashqi qavat butunlay yo'qoldi (3 qavat → 2 qavat)."], M=2, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi atom-zanjiri: tarkib → konfiguratsiya → ion → izohlar; M15+A10.",
      parametrlar=dict(arch="na_zanjir")),
 dict(n=42, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Bayram otashinlari turli ranglarda porlaydi: stronsiy tuzlari — qizil, mis tuzlari — "
            "yashil-ko'k, natriy — sariq. Quyidagi savollarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Otashin ranglarining paydo bo'lish mexanizmini atom tuzilishi asosida tushuntiring.",
             yechim=["Qizdirilganda elektronlar yuqori pog'onachalarga qo'zg'aladi; qaytishida har element",
                     "o'ziga xos energiyali (rangli) yorug'lik kvantini chiqaradi."], M=13, A=0),
        dict(savol="b) Nega har bir element o'ziga xos rang beradi (masalan, Na doim sariq)?",
             yechim=["Pog'onachalar energiyalari har elementda har xil (Z ga bog'liq) — chiqayotgan kvant",
                     "energiyasi (rangi) elementga «imzo» bo'ladi."], M=9, A=0),
        dict(savol="c) Bu hodisaga asoslangan analitik usulni ayting.",
             yechim=["Alanga testi (spektral analiz) — metallarni rang orqali aniqlash."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="otashin_mulohaza")),
 dict(n=43, tur="O2", element="I.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch elementning elektron qavatlari jadvalda berilgan:\n"
            "[JADVAL] Element | Qavatlar ;; X | 2, 8, 1 ;; Y | 2, 8, 7 ;; Z | 2, 8\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X, Y, Z elementlarni aniqlang va tabiatini ayting (metall/metallmas/inert).",
             yechim=["X — Na (metall); Y — Cl (metallmas); Z — Ne (inert gaz)."], M=4, A=2),
        dict(savol="b) X va Y qanday ionlar hosil qiladi? Ikkala ionning elektron sonlarini yozing.",
             yechim=["Na⁺ (10 e) va Cl⁻ (18 e)."], M=4, A=3),
        dict(savol="c) X va Y hosil qiladigan birikma formulasini va bog' turini yozing.",
             yechim=["NaCl — ion bog'lanish."], M=4, A=3),
        dict(savol="d) Nega Z ion hosil qilmaydi?",
             yechim=["Tashqi qavati to'la (8 e) — energetik jihatdan barqaror, e olish-berishga moyil emas."], M=3, A=2),
      ],
      rasmiylashtirish="Qavat-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="qavat_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260203)
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
    variant="mavzu-I1-A", daraja="A", bob=1, bob_nomi="Atom tuzilishi",
    manba=("MS spetsifikatsiyasi I.1; darslik atom tuzilishi bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (alanga testi, neon, rentgen, banan-K40) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
