# -*- coding: utf-8 -*-
"""4-bob B-varianti: Kimyoviy bog'lanish (I.4) — HAQIQIY MS MUHITI ★★★.
Bog' turlari, EM jadvali, sigma/pi, kristall panjaralar, bog' energiyasi-uzunligi qatorlari.
Tongotarov bog'lanish banki arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_I4B.json"
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

# 1 (3) — metall-kovalent-ion ketma-ketligi
q(3, "yuqori",
  "Metall, kovalent va ion bog'lanishli moddalar KETMA-KETLIGI to'g'ri berilgan javobni toping.",
  "Fe, CO₂, KCl",
  [("NaCl, Cu, H₂O", "tartib buzilgan: ion, metall, kovalent"),
   ("Zn, KBr, NH₃", "ikkinchi o'rinda ion birikma turibdi"),
   ("SO₃, Ag, CaF₂", "birinchi o'rinda kovalent birikma")],
  "Fe — metall panjara; CO₂ — kovalent (qutbli); KCl — tipik ion birikma.",
  dict(arch="ketma_ketlik"))

# 2 (3) — barcha qutbli kovalent
q(3, "yuqori",
  "Qaysi javobdagi BARCHA moddalar qutbli kovalent bog'lanishga ega?",
  "NH₃, PCl₃, H₂O",
  [("CO₂, Cl₂, H₂S", "Cl₂ — qutbsiz kovalent"),
   ("NO₂, O₂, HF", "O₂ — qutbsiz"),
   ("O₃, S₈, P₄", "barchasi qutbsiz (bir xil atomlar)")],
  "Har uch moddada turli elektromanfiylikdagi atomlar bog'langan — qutbli kovalent.",
  dict(arch="qutbli_tanlash"))

# 3 (2) — ion bog' sharti
q(2, "yuqori",
  "Ion bog'lanish qanday atomlar orasida hosil bo'ladi?",
  "elektromanfiyliklari keskin farq qiluvchi (tipik metall va metallmas) atomlar orasida",
  [("elektromanfiyliklari teng atomlar orasida", "bu qutbsiz kovalent sharti"),
   ("faqat bir xil element atomlari orasida", "bir xil atomlar ion juftlik hosil qilmaydi"),
   ("faqat gaz holatdagi atomlar orasida", "agregat holat shart emas")],
  "ΔEM katta (≳1,7–2) bo'lganda elektron amalda to'liq o'tadi — ionlar hosil bo'ladi.",
  dict(arch="ion_shart"))

# 4 (3) — 1-2-3: to'yinuvchan va yo'naluvchan bog'lar
q(3, "yuqori",
  "Qaysi birikmalardagi kimyoviy bog'lar TO'YINUVCHANLIK va YO'NALUVCHANLIK xossasiga ega?\n"
  "1) NH₃;  2) LiH;  3) CaH₂;  4) C₂H₄;  5) CrCl₃;  6) SiH₄.",
  "1, 4 va 6",
  [("2, 3 va 5", "bular ionli birikmalar — ion bog' yo'nalishsiz"),
   ("1, 3 va 5", "3 va 5 — ionli"),
   ("2, 4 va 6", "LiH — ionli gidrid")],
  "To'yinuvchanlik/yo'naluvchanlik — KOVALENT bog' xossalari: NH₃, C₂H₄, SiH₄. "
  "LiH, CaH₂, CrCl₃ — ion bog'li.",
  dict(arch="toyinuvchan_tanlov"))

# 5 (3) — JADVALLI: EM dan bog' turi
q(3, "yuqori",
  "Elementlarning elektromanfiyliklari jadvalda berilgan:\n"
  "[JADVAL] Element | Na | H | Cl | F ;; EM | 0,9 | 2,1 | 3,0 | 4,0\n"
  "Qaysi juftlik ION bog'lanish hosil qiladi?",
  "Na va F", [("H va Cl", "ΔEM = 0,9 — qutbli kovalent"),
               ("Cl va F", "ΔEM = 1,0 — kovalent"),
               ("H va F", "ΔEM = 1,9 — kuchli qutbli kovalent (HF molekula)")],
  "ΔEM(NaF) = 4,0 − 0,9 = 3,1 — eng katta farq: elektron to'liq o'tadi, ion bog'.",
  dict(arch="em_jadval"))

# 6 (3) — pi-bog' bor molekula
q(3, "yuqori",
  "Qaysi molekula tarkibida π-bog' uchraydi?",
  "CO₂", [("Cl₂", "bitta σ-bog'"), ("NH₃", "uchta σ-bog'"), ("SiO₂", "atom panjarada σ-bog'lar")],
  "CO₂: O=C=O — har bir qo'sh bog'da 1σ + 1π; jami 2σ + 2π.",
  dict(arch="pi_topish"))

# 7 (3) — Al2(SO4)3 bog'lar soni
q(3, "yuqori",
  "Al₂(SO₄)₃ tarkibidagi ION va KOVALENT bog'lar sonini aniqlang.",
  "6 va 18", [("6 va 12", "S=O qo'sh bog'lardagi π-bog'lar hisoblanmagan"),
               ("9 va 15", "ion bog'lar soni xato"), ("8 va 16", "ikkala son ham asossiz")],
  "2Al³⁺ va 3SO₄²⁻ orasida 6 ta ion bog'; har SO₄²⁻ da 6 ta bog' (4σ + 2π) → 3·6 = 18 kovalent.",
  dict(arch="bog_sanash"))

# 8 (2) — vodorod bog'lanish
q(2, "yuqori",
  "Qaysi moddaning suyuq holatida molekulalar orasida VODOROD bog'lanish mavjud?",
  "H₂O", [("CH₄", "C–H qutbliligi juda kichik"), ("H₂S", "S ning EM i yetarli emas — vodorod bog' juda kuchsiz"),
           ("CO₂", "molekulada H atomi yo'q")],
  "Vodorod bog' H bilan kuchli EM li element (F, O, N) orasida hosil bo'ladi: suvda O–H···O.",
  dict(arch="vodorod_bog"))

# 9 (2) — panjara turi
q(2, "yuqori",
  "Osh tuzi (NaCl) kristali qanday panjaraga ega?",
  "ion panjara",
  [("molekular panjara", "NaCl da molekula yo'q — ionlar tuguni"),
   ("atom panjara", "atom panjara olmos, SiO₂ kabilarda"),
   ("metall panjara", "metallmas ishtirokidagi tuz metall panjara hosil qilmaydi")],
  "Tugunlarda Na⁺ va Cl⁻ ionlari — ion panjara (yuqori suyuql. harorat, eritmasi tok o'tkazadi).",
  dict(arch="panjara_nacl"))

# 10 (3) — molekular panjara jufti
q(3, "yuqori",
  "Qaysi moddalar JUFTI qattiq holatda MOLEKULAR kristall panjaraga ega?",
  "CO₂, NH₃",
  [("Cl₂, NaCl", "NaCl — ion panjara"), ("H₂O, SiO₂", "SiO₂ — atom panjara"),
   ("KI, NaI", "ikkalasi ham ion panjara")],
  "«Quruq muz» (CO₂) va qattiq NH₃ tugunlarida molekulalar turadi.",
  dict(arch="molekular_juft"))

# 11 (3) — bog' energiyasi tartibi
q(3, "yuqori",
  "Moddalarni bog' energiyasi ORTISH tartibida joylashtiring: 1) HCl; 2) HF; 3) HI; 4) HBr.",
  "3, 4, 1, 2",
  [("2, 1, 4, 3", "bu kamayish tartibi"), ("4, 3, 1, 2", "HI eng kuchsiz — birinchi turishi kerak"),
   ("3, 4, 2, 1", "HF eng mustahkam — oxirida")],
  "Atom radiusi kichrayishi bilan bog' qisqaradi va mustahkamlanadi: HI < HBr < HCl < HF.",
  dict(arch="energiya_tartib"))

# 12 (2) — donor-akseptor
q(2, "yuqori",
  "NH₄⁺ ionidagi TO'RTINCHI N–H bog' qanday mexanizm bo'yicha hosil bo'lgan?",
  "donor-akseptor: juftni azot beradi, bo'sh orbitalni H⁺ beradi",
  [("oddiy almashinuv mexanizmi", "to'rtinchi bog'da H⁺ ning elektroni yo'q"),
   ("ion mexanizmi", "N–H bog' kovalent, ion emas"),
   ("vodorod bog'lanish", "bu molekulalararo kuch, ichki bog' emas")],
  "N dagi taqsimlanmagan juft H⁺ ning bo'sh orbitaliga o'tadi; hosil bo'lgach to'rttala bog' teng.",
  dict(arch="donor_akseptor"))

# 13 (3) — qator o'zgarishi (qutblilik+uzunlik)
q(3, "yuqori",
  "CBr₄ → CCl₄ → CF₄ qatorida bog' QUTBLILIGI va bog' UZUNLIGI qanday o'zgaradi?",
  "qutblilik ortadi; uzunlik kamayadi",
  [("qutblilik kamayadi; uzunlik ortadi", "F eng elektromanfiy va eng kichik atom"),
   ("ikkalasi ham ortadi", "radius kichraygani uchun bog' qisqaradi"),
   ("ikkalasi ham kamayadi", "ΔEM ortadi — qutblilik kuchayadi")],
  "Br→Cl→F: EM ortadi (qutblilik ↑), radius kichrayadi (uzunlik ↓).",
  dict(arch="qator_ozgarish"))

# 14 (3) — 1-2-3: faqat sigma
q(3, "yuqori",
  "Qaysi moddalarda FAQAT σ-bog'lar mavjud?\n1) CH₄;  2) C₂H₄;  3) H₂O;  4) N₂;  5) NH₃.",
  "1, 3 va 5",
  [("1, 2 va 3", "C₂H₄ da C=C tarkibida π-bog' bor"),
   ("3, 4 va 5", "N₂ da 2 ta π-bog' bor"),
   ("faqat 1", "H₂O va NH₃ da ham faqat σ")],
  "Yakka bog'lar — faqat σ: CH₄, H₂O, NH₃. C₂H₄ (1π) va N₂ (2π) chiqadi.",
  dict(arch="sigma_tanlov"))

# 15 (3) — parametrli taqqoslash (bank arxetipi)
q(3, "yuqori",
  "NH₃ va AsH₃ dagi bog' uzunliklari mos ravishda 0,101 va 0,151 nm. PH₃ va SbH₃ dagi bog' "
  "uzunliklari (nm) qanday bo'lishi mumkin?",
  "0,142 va 0,170",
  [("0,126 va 0,141", "SbH₃ AsH₃ dan KATTA bo'lishi kerak (0,151 dan ortiq)"),
   ("0,170 va 0,161", "PH₃ oraliqda (0,101–0,151) bo'lishi kerak"),
   ("0,074 va 0,161", "0,074 — H₂ ning uzunligi, PH₃ emas")],
  "Guruhda pastga radius ortadi: N–P–As–Sb → PH₃ 0,101 va 0,151 orasida; SbH₃ > 0,151.",
  dict(arch="parametrli_uzunlik"))

# 16 (2) — metall bog'lanish
q(2, "yuqori",
  "Metallarning elektr o'tkazuvchanligi qaysi xususiyat bilan tushuntiriladi?",
  "panjara bo'ylab erkin harakatlanuvchi umumlashgan elektronlar bilan",
  [("ionlarning erkin harakati bilan", "qattiq metallda ionlar tugunlarda tebranadi"),
   ("molekulalarning harakati bilan", "metallda molekula yo'q"),
   ("protonlarning ko'chishi bilan", "protonlar yadroda — ko'chmaydi")],
  "Metall bog'lanish: kationlar «elektron gazi» ichida — elektronlar tokni tashiydi.",
  dict(arch="metall_bog"))

# 17 (3) — JADVALLI: panjara «?»
q(3, "yuqori",
  "Moddalar va panjaralari jadvalda berilgan:\n"
  "[JADVAL] Modda | Panjara | Suyuql. harorati ;; olmos | atom | juda yuqori ;; muz | ? | past ;; KBr | ? | yuqori\n"
  "«?» o'rnidagi panjaralarni mos ravishda aniqlang.",
  "molekular va ion",
  [("ion va molekular", "muz — molekulalardan, KBr — ionlardan tuzilgan"),
   ("atom va metall", "ikkala katak ham xato"),
   ("molekular va atom", "KBr — tipik ion birikma")],
  "Muz tugunlarida H₂O molekulalari (past t suyuql.); KBr da K⁺ va Br⁻ ionlari.",
  dict(arch="panjara_jadval"))

# 18 (2) — valentlik va daraja farqi
q(2, "yuqori",
  "H₂O₂ (vodorod peroksid) dagi kislorodning VALENTLIGI va OKSIDLANISH DARAJASI qanday?",
  "2 va −1",
  [("2 va −2", "peroksidda O–O bog' bor — daraja −1"),
   ("1 va −1", "har O ikkita bog' hosil qiladi (H–O–O–H)"),
   ("2 va +1", "kislorod faqat OF₂ da musbat")],
  "H–O–O–H: har O 2 ta bog' (valentlik 2); O–O bog' darajaga hissa qo'shmaydi → −1.",
  dict(arch="valentlik_daraja"))

# 19 (3) — N2 tarkibi
q(3, "yuqori",
  "Azot molekulasidagi (N≡N) bog'larning tarkibini aniqlang.",
  "1 σ va 2 π",
  [("3 σ", "karrali bog'da faqat bittasi σ bo'ladi"),
   ("2 σ va 1 π", "ikkinchi va uchinchi bog'lar π"),
   ("1 σ va 1 π", "uch bog'da jami 3 ta bog' bor")],
  "Karrali bog'da birinchisi σ, qolganlari π: N≡N → 1σ + 2π.",
  dict(arch="n2_tarkib"))

# 20 (2) — qutbsiz kovalent
q(2, "yuqori",
  "Qaysi moddada QUTBSIZ kovalent bog'lanish mavjud?",
  "O₂", [("HCl", "ΔEM ≠ 0 — qutbli"), ("NaBr", "ion birikma"), ("H₂S", "qutbli kovalent")],
  "Bir xil atomlar orasida ΔEM = 0 — elektron juft o'rtada: qutbsiz kovalent.",
  dict(arch="qutbsiz"))

# 21 (3) — F2-O2-N2 qatori
q(3, "yuqori",
  "F₂ → O₂ → N₂ qatorida bog' ENERGIYASI va bog' KARRALILIGI qanday o'zgaradi?",
  "ikkalasi ham ortadi",
  [("ikkalasi ham kamayadi", "F–F (1), O=O (2), N≡N (3) — karralilik ortyapti"),
   ("energiya ortadi; karralilik kamayadi", "karralik 1→2→3 ortadi"),
   ("energiya kamayadi; karralilik ortadi", "karralilik ortishi bilan energiya ham ortadi")],
  "Karralilik 1→2→3; energiya 159 → 498 → 946 kJ/mol — ikkalasi ortadi.",
  dict(arch="f2o2n2"))

# 22 (3) — 1-2-3: vodorod bog' hosil qiluvchilar
q(3, "yuqori",
  "Qaysi moddalar suyuq holatda molekulalararo VODOROD bog'lanish hosil qiladi?\n"
  "1) H₂O;  2) HF;  3) C₂H₅OH;  4) CH₄.",
  "1, 2 va 3",
  [("1 va 2", "spirtdagi O–H guruhi ham vodorod bog' beradi"),
   ("hammasi", "CH₄ da H kuchli EM li atomga bog'lanmagan"),
   ("faqat 1", "HF — eng kuchli vodorod bog'lardan biri")],
  "Shart: H atom F, O yoki N ga bog'langan bo'lishi. CH₄ mos emas.",
  dict(arch="vodorod_tanlov"))

# 23 (3) — energiya taqqoslash (bank arxetipi)
q(3, "yuqori",
  "Br₂ molekulasining bog' energiyasi 193 kJ/mol. I₂ va H₂ molekulalarining bog' energiyalari "
  "(kJ/mol) qanday bo'lishi mumkin?",
  "151 va 436",
  [("297 va 436", "I₂ Br₂ dan kuchsiz — 193 dan kichik bo'lishi kerak"),
   ("151 va 136", "H₂ — juda mustahkam bog' (kichik radius)"),
   ("156 va 171", "H₂ uchun qiymat juda kichik")],
  "I₂ < Br₂ (katta radius) → 151; H₂ — eng qisqa bog'lardan → 436 kJ/mol.",
  dict(arch="energiya_taqqos"))

# 24 (2) — panjara-xossa
q(2, "yuqori",
  "Molekular panjarali moddalarga qanday xossalar xos?",
  "past suyuqlanish harorati, uchuvchanlik",
  [("juda yuqori suyuqlanish harorati", "bu atom/ion panjara belgisi"),
   ("eritmalarining elektr o'tkazishi", "molekular moddalar ko'pincha noelektrolit"),
   ("yuqori qattiqlik", "molekular kristallar yumshoq")],
  "Molekulalar orasida kuchsiz kuchlar — oson suyuqlanadi va bug'lanadi (muz, quruq muz, yod).",
  dict(arch="panjara_xossa"))

# 25 (3) — geometriya
q(3, "yuqori",
  "Metan (CH₄) molekulasining fazoviy shakli va bog'lar orasidagi burchak qanday?",
  "tetraedr; 109,5°",
  [("kvadrat; 90°", "sp³ gibridlanish tekis kvadrat bermaydi"),
   ("uchburchak; 120°", "bu sp² (masalan, BF₃) geometriyasi"),
   ("chiziqli; 180°", "bu sp (CO₂) geometriyasi")],
  "sp³ gibridlanish: to'rt bog' fazoda teng taqsimlanadi — tetraedr, 109,5°.",
  dict(arch="geometriya"))

# 26 (3) — uglerod zanjiri uzunliklari
q(3, "yuqori",
  "Rasmda molekulaning tuzilish formulasi berilgan. Undagi uglerod–uglerod bog' uzunligi "
  "O'NGDAN CHAPGA tomon qanday o'zgaradi?",
  "ortadi; kamayadi",
  [("kamayadi; kamayadi", "C=C dan C–C ga o'tishda uzunlik ortadi"),
   ("ortadi; ortadi", "oxirida C≡C — eng qisqa bog'"),
   ("kamayadi; ortadi", "tartib teskari")],
  "O'ngdan: C=C (0,134) → C–C (0,146) ortadi → C≡C (0,120) keskin kamayadi.",
  dict(arch="zanjir_uzunlik"), fig="molecule")

# 27 (3) — jadvaldan qutblilik tartibi
q(3, "yuqori",
  "5-savoldagi EM jadvalidan foydalanib, H–F, H–Cl va Na–Cl bog'larini QUTBLILIK ortish tartibida joylashtiring.",
  "H–Cl < H–F < Na–Cl",
  [("H–F < H–Cl < Na–Cl", "ΔEM: HF 1,9 > HCl 0,9"),
   ("Na–Cl < H–F < H–Cl", "NaCl ΔEM = 2,1 — eng qutbli (ion)"),
   ("H–Cl < Na–Cl < H–F", "HF (1,9) NaCl (2,1) dan kichik")],
  "ΔEM: H–Cl 0,9 < H–F 1,9 < Na–Cl 2,1.",
  dict(arch="qutblilik_tartib"))

# 28 (2) — RASMLI: ikki panjara
q(2, "yuqori",
  "Rasmda ikki xil kristall panjara sxemasi berilgan. Qaysi biri ION panjara va buni nimadan bilish mumkin?",
  "1-panjara — tugunlarda zaryadli ionlar navbatlashgan",
  [("2-panjara — tugunlarda molekulalar bor", "molekulali tugunlar molekular panjara belgisi"),
   ("ikkalasi ham ion", "2-rasmda alohida CO₂ molekulalari ko'rinib turibdi"),
   ("rasmdan aniqlab bo'lmaydi", "tugunlardagi zarracha turi panjarani belgilaydi")],
  "1-rasm: «+» va «−» ionlar navbatlashgan (NaCl tipi); 2-rasm: tugunlarda CO₂ molekulalari.",
  dict(arch="panjara_rasm"), fig="lattice")

# 29 (3) — 1-2-3: NH4Cl dagi bog'lar
q(3, "yuqori",
  "NH₄Cl kristalida qanday bog'lanish TURLARI mavjud?\n"
  "1) qutbli kovalent;  2) ion;  3) donor-akseptor mexanizmli kovalent.",
  "1, 2 va 3 — barchasi",
  [("faqat 2", "N–H bog'lari kovalent"), ("1 va 2", "to'rtinchi N–H — donor-akseptor"),
   ("faqat 1", "NH₄⁺ va Cl⁻ orasida ion bog' bor")],
  "N–H (qutbli kovalent, biri donor-akseptor) + NH₄⁺·Cl⁻ (ion) — uchala tur ham bor.",
  dict(arch="nh4cl_bog"))

# 30 (2) — suv anomaliyasi
q(2, "yuqori",
  "Nega suvning qaynash harorati (100 °C) o'ziga o'xshash H₂S (−60 °C) nikidan keskin yuqori?",
  "suv molekulalari orasida vodorod bog'lanish bor",
  [("suv molekulasi og'irroq", "aksincha, H₂S og'irroq (34 > 18)"),
   ("suvda kovalent bog' kuchliroq", "qaynashda molekulalararo kuchlar uziladi, ichki bog' emas"),
   ("H₂S gaz holatda bo'lgani uchun", "bu oqibat, sabab emas")],
  "O–H···O vodorod bog'larini uzish qo'shimcha energiya talab qiladi — qaynash t keskin yuqori.",
  dict(arch="suv_anomaliya"))

# 31 (3) — NH4+ valentlik/daraja
q(3, "yuqori",
  "NH₄⁺ ionidagi azotning VALENTLIGI va OKSIDLANISH DARAJASINI aniqlang.",
  "4 va −3",
  [("3 va −3", "to'rtinchi (donor-akseptor) bog' ham valentlikka kiradi"),
   ("4 va +4", "vodorodlar +1: x + 4 = +1 → x = −3"),
   ("5 va −3", "azotda 4 tagina bog' bor")],
  "N to'rtta bog' hosil qilgan (valentlik 4); x + 4(+1) = +1 → x = −3.",
  dict(arch="nh4_valentlik"))

# 32 (3) — RASMLI: EM shkalasi
q(3, "yuqori",
  "Rasmdagi shkala bo'yicha bog' turi ΔEM ga qarab aniqlanadi. X–Y bog'ida ΔEM = 2,1 bo'lsa, "
  "bog' turi qanday?",
  "ion", [("qutbli kovalent", "1,7 dan katta farq ion bog'ga o'tadi"),
           ("qutbsiz kovalent", "ΔEM = 0 atrofida bo'lardi"),
           ("metall bog'lanish", "shkala metall bog'ni ko'rsatmaydi")],
  "Shkala: ΔEM ≈ 0 — qutbsiz; 0 < ΔEM < 1,7 — qutbli kovalent; ΔEM > 1,7 — ion. 2,1 → ion.",
  dict(arch="em_shkala"), fig="em_axis")

# ---------- Y2: EM jadvali ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.4",
  ichki_pasport=[dict(n=33, element="I.4", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.4", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("X, Y, Z elementlarining elektromanfiyliklari mos ravishda 0,9; 3,0 va 2,1. "
               "(ΔEM > 1,7 — ion; 0 < ΔEM ≤ 1,7 — qutbli kovalent; ΔEM = 0 — qutbsiz kovalent.) "
               "33–35-savollarda hosil bo'ladigan bog' turini A–F ro'yxatidan tanlang."),
  savollar_ichki=[
    "33. X va Y atomlari orasida qanday bog' hosil bo'ladi?",
    "34. Z va Y atomlari orasida-chi?",
    "35. Y va Y atomlari orasida-chi?"],
  javoblar_royxati=["A) ion", "B) qutbli kovalent", "C) qutbsiz kovalent",
                    "D) metall", "E) vodorod bog'lanish", "F) donor-akseptor"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="metall bog' — sof metallarga xos"),
                   dict(variant="E", xato="vodorod bog' — molekulalararo kuch"),
                   dict(variant="F", xato="mexanizm nomi, bog' turi emas")],
  yechim=("33: ΔEM = 2,1 > 1,7 → ion (A). 34: ΔEM = 0,9 → qutbli kovalent (B). "
          "35: ΔEM = 0 → qutbsiz kovalent (C)."),
  parametrlar=dict(arch="em_ssenariy"))

# ---------- O1 ----------
check("o36", 3, 3); check("o36b", 2, 2)
check("o37", 2, 2)
check("o38", 2, 2)
check("o39", 5, 5)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="Asetilen (HC≡CH) molekulasidagi σ- va π-bog'lar sonini mos ravishda yozing.",
      javob="3 va 2", yechim="σ: 2 ta C–H + 1 ta C–C = 3; π: uch bog'ning ikkitasi = 2.",
      parametrlar=dict(arch="sigma_pi_o1")),
 dict(n=37, qiyinlik=2, kognitiv="yuqori",
      savol="Azot molekulasida nechta π-bog' bor?",
      javob="2", yechim="N≡N: 1σ + 2π.",
      parametrlar=dict(arch="n2_o1")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="CaCl₂ formula birligidagi ion bog'lar sonini aniqlang.",
      javob="2", yechim="Ca²⁺ ikkita Cl⁻ bilan — 2 ta ion bog'.",
      parametrlar=dict(arch="ion_son_o1")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Etilen (C₂H₄) molekulasidagi σ-bog'lar sonini aniqlang.",
      javob="5", yechim="4 ta C–H + 1 ta C–C(σ) = 5 (C=C ning ikkinchisi — π).",
      parametrlar=dict(arch="etilen_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="NH₄Cl kristalida nechta XIL bog'lanish turi bor (mexanizm bilan birga sanang)?",
      javob="3", yechim="Qutbli kovalent (N–H), donor-akseptor mexanizmli kovalent, ion (NH₄⁺–Cl⁻).",
      parametrlar=dict(arch="nh4cl_o1")),
]

# ---------- O2 ----------
O2 = [
 dict(n=41, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Elektromanfiyliklar: Na — 0,9; H — 2,1; O — 3,5; Cl — 3,0. Quyidagi moddalar berilgan: "
            "NaCl, HCl, Cl₂, H₂O. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir moddadagi bog' turini aniqlang.",
             yechim=["NaCl — ion; HCl — qutbli kovalent; Cl₂ — qutbsiz kovalent; H₂O — qutbli kovalent"], M=4, A=2),
        dict(savol="b) HCl, H₂O va NaCl uchun ΔEM ni hisoblab, qutblilik ortish tartibida joylashtiring.",
             yechim=["ΔEM: HCl 0,9 < H₂O 1,4 < NaCl 2,1"], M=4, A=3),
        dict(savol="c) Qaysi modda suyuq holatda vodorod bog'lanish hosil qiladi? Sababini yozing.",
             yechim=["H₂O — H atom kuchli EM li O ga bog'langan: O–H···O ko'priklari."], M=3, A=2),
        dict(savol="d) NaCl va Cl₂ ning qattiq holatdagi panjara turlarini va bittadan xossasini yozing.",
             yechim=["NaCl — ion (yuqori suyuql. t); Cl₂ — molekular (past t, uchuvchan)."], M=4, A=3),
      ],
      rasmiylashtirish="EM-tahlil zanjiri: tur → tartib → vodorod bog' → panjara; M15+A10.",
      parametrlar=dict(arch="em_zanjir")),
 dict(n=42, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Noma'lum X modda: oq kristall, suyuqlanish harorati yuqori, suvda yaxshi eriydi, "
            "eritmasi elektr tokini o'tkazadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) X moddaning panjara va bog'lanish turini aniqlash yo'lini bosqichma-bosqich yozing.",
             yechim=["Yuqori t(suyuql.) → atom yoki ion panjara; eritmasi tok o'tkazadi → erkin ionlar bor →",
                     "ion panjara, ion bog'lanish (masalan, NaCl, KBr)."], M=13, A=0),
        dict(savol="b) Xossalari X ga QARAMA-QARSHI bo'lgan (molekular panjarali) moddaga misol keltirib, farqni tushuntiring.",
             yechim=["Masalan, yod yoki muz: past t suyuqlanadi, eritmasi tok o'tkazmaydi —",
                     "tugunlarda neytral molekulalar."], M=9, A=0),
        dict(savol="c) Nega X ning suvdagi eritmasi tok o'tkazadi-yu, kristali o'tkazmaydi?",
             yechim=["Kristallda ionlar mahkam; eritmada gidratlanib erkin harakatlanadi."], M=3, A=0),
      ],
      rasmiylashtirish="Modda-detektiv formati (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="detektiv")),
 dict(n=43, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch moddaning xossalari jadvalda berilgan:\n"
            "[JADVAL] Modda | Suyuql. t, °C | Qattiq holatda tok | Suvda eruvchanligi ;; "
            "X | 801 | o'tkazmaydi | yaxshi ;; Y | 3550 | o'tkazmaydi | erimaydi ;; Z | −78* | o'tkazmaydi | yomon\n"
            "(*Z sublimatlanadi.) Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X, Y, Z ning kristall panjara turlarini aniqlang va asoslang.",
             yechim=["X — ion (yuqori t, eritmasi elektrolit — NaCl tipi); Y — atom (o'ta yuqori t — olmos tipi);",
                     "Z — molekular (past t, sublimatlanadi — quruq muz tipi)."], M=6, A=3),
        dict(savol="b) X ning suyuqlanmasi tok o'tkazadimi? Sababi bilan yozing.",
             yechim=["Ha — suyuqlanmada ionlar erkinlashadi (elektroliz ham qilish mumkin)."], M=3, A=2),
        dict(savol="c) Y va Z dagi bog'lanish turlarini ko'rsating.",
             yechim=["Y — kovalent (atomlar orasida); Z — molekulada kovalent, molekulalararo kuchsiz kuchlar."], M=3, A=2),
        dict(savol="d) Har bir moddaga mos bitta real misol keltiring.",
             yechim=["X — NaCl; Y — olmos (yoki SiO₂); Z — CO₂ (quruq muz)."], M=3, A=3),
      ],
      rasmiylashtirish="Jadval-tahlil (xossa → panjara): M15+A10.",
      parametrlar=dict(arch="xossa_jadval")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260518)
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
    d = dict(n=n, tur="Y1", element="I.4", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I4-B", daraja="B", bob=4, bob_nomi="Kimyoviy bog'lanish",
    manba=("Tongotarov bog'lanish banki (2019-2021) arxetiplari — javoblar mustaqil tekshirilgan; "
           "MS spetsifikatsiyasi I.4"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: EM jadvallari, bog' sanash, energiya-uzunlik qatorlari, "
          "1-2-3 tanlovlar, parametrli taqqoslashlar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
