# -*- coding: utf-8 -*-
"""2-bob B-varianti: Davriy qonun va davriy sistema (I.2) — HAQIQIY MS MUHITI ★★★.
Xossalar qatorlari, oliy oksid/gidroksid formulalari, teskari (%-dan element) masalalar,
davriy jadval fragmenti. Javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_I2B.json"
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

# 1 (3) — radius ortish qatori
q(3, "yuqori",
  "Qaysi qatorda atom radiusi ORTIB borishi to'g'ri ko'rsatilgan?",
  "O → S → Se → Te",
  [("Te → Se → S → O", "bu kamayish tartibi"), ("Na → Mg → Al → Si", "davrda radius kamayadi"),
   ("I → Br → Cl → F", "guruhda yuqoriga kamayadi")],
  "Guruhda pastga qavatlar soni ortadi → radius kattalashadi.",
  dict(arch="radius_qator"))

# 2 (3) — metallik eng kuchli
q(3, "yuqori",
  "Quyidagi elementlardan qaysi birida METALLIK xossalari eng kuchli namoyon bo'ladi?",
  "Cs", [("Li", "guruhning tepasida — kuchsizroq"), ("Al", "III A — metallik ancha past"),
          ("Mg", "II A, 3-davr — Cs dan kuchsiz")],
  "Metallik chapga va pastga kuchayadi: I A guruhning eng pastki barqaror vakili — Cs.",
  dict(arch="metallik_eng"))

# 3 (2) — davriy qonun ta'rifi
q(2, "yuqori",
  "Davriy qonunning ZAMONAVIY ta'rifida elementlar xossalari nimaga davriy bog'liq deb qaraladi?",
  "yadro zaryadiga (tartib raqamiga)",
  [("atom massasiga", "Mendeleev davridagi ta'rif; Ar–K juftida buziladi"),
   ("neytronlar soniga", "izotoplar xossani o'zgartirmaydi"),
   ("elektronlar umumiy soniga emas, faqat massaga", "aynan Z (va u orqali e tuzilishi) asos")],
  "Zamonaviy ta'rif: xossalar Z ortib borishiga davriy ravishda bog'liq.",
  dict(arch="qonun_tarif"))

# 4 (3) — 1-2-3: davrda ortadigan xossalar
q(3, "yuqori",
  "3-davrda chapdan o'ngga (Na → Cl) qaysi kattaliklar ORTIB boradi?\n"
  "1) elektromanfiylik;  2) atom radiusi;  3) oksidlovchilik;  4) metallik xossasi.",
  "1 va 3",
  [("2 va 4", "bular davrda KAMAYADI"),
   ("1, 2 va 3", "radius davrda kichrayadi"),
   ("faqat 1", "oksidlovchilik ham kuchayadi (Cl — kuchli oksidlovchi)")],
  "Davrda: EM ↑, oksidlovchilik ↑; radius ↓, metallik ↓.",
  dict(arch="davr_tanlov"))

# 5 (3) — RASMLI: radius grafigi
q(3, "yuqori",
  "Rasmda 3-davr elementlari atom radiuslarining o'zgarishi berilgan. Grafikdan foydalanib, radiusi "
  "118 pm bo'lgan elementni aniqlang.",
  "Si", [("Al", "grafikda 143 pm"), ("P", "grafikda 110 pm"), ("S", "grafikda 104 pm")],
  "Grafikdan: 118 pm nuqtasi kremniyga to'g'ri keladi.",
  dict(arch="radius_grafik_oqish"), fig="radius_line")

# 6 (3) — oliy oksid formulasi
q(3, "yuqori",
  "VI A guruh elementining OLIY oksidi qaysi umumiy formulaga ega?",
  "RO₃", [("RO₂", "IV A uchun"), ("R₂O₅", "V A uchun"), ("R₂O₇", "VII A uchun")],
  "Oliy oksidda valentlik = guruh raqami: VI → RO₃ (masalan, SO₃).",
  dict(arch="oliy_oksid"))

# 7 (3) — RH3 dan oliy oksid
q(3, "yuqori",
  "Elementning uchuvchan vodorodli birikmasi RH₃ ko'rinishga ega. Uning OLIY oksidi formulasini toping.",
  "R₂O₅", [("RO₃", "RH₂ bo'lganda"), ("R₂O₃", "oliy valentlik 8−3=5 emas, 3 deb olingan"),
            ("RO₂", "RH₄ bo'lganda")],
  "RH₃ → guruh = 8 − 3 = 5 → V A → oliy oksid R₂O₅ (N₂O₅, P₂O₅).",
  dict(arch="rh_oksid"))

# 8 (2) — guruh raqami
q(2, "yuqori",
  "Asosiy guruhcha elementlarida guruh raqami nimani ko'rsatadi?",
  "tashqi qavatdagi (valent) elektronlar sonini",
  [("qavatlar sonini", "buni davr raqami ko'rsatadi"),
   ("neytronlar sonini", "jadval n bermaydi"),
   ("izotoplar sonini", "bog'liq emas")],
  "Masalan, VI A → tashqi qavatda 6 e (ns²np⁴).",
  dict(arch="guruh_raqam"))

# 9 (2) — inert gazlar
q(2, "yuqori",
  "VIII A guruh (inert gazlar) elementlarining kimyoviy passivligi sababi nimada?",
  "tashqi qavati tugallangan (8 e, He da 2 e)",
  [("atomlari juda kichik", "o'lcham emas, qavat to'laligi sabab"),
   ("ular gaz holatda", "agregat holat sabab emas"),
   ("elektronlari yo'q", "elektronlari bor, lekin barqaror joylashgan")],
  "To'la qavat — energetik barqaror: e olish ham, berish ham foydasiz.",
  dict(arch="inert_sabab"))

# 10 (3) — amfoter oksid
q(3, "yuqori",
  "Qaysi oksid AMFOTER xossaga ega (ham kislota, ham ishqor bilan reaksiyaga kirishadi)?",
  "Al₂O₃", [("Na₂O", "tipik asosli oksid"), ("SO₃", "tipik kislotali oksid"),
             ("CaO", "asosli oksid")],
  "Al₂O₃ (shuningdek ZnO, BeO): HCl bilan ham, NaOH bilan ham reaksiyaga kirishadi.",
  dict(arch="amfoter"))

# 11 (3) — kislotalilik qatori
q(3, "yuqori",
  "Qaysi qatorda kislotalarning KUCHI ortib borishi to'g'ri ko'rsatilgan?",
  "H₂SiO₃ → H₃PO₄ → H₂SO₄ → HClO₄",
  [("HClO₄ → H₂SO₄ → H₃PO₄ → H₂SiO₃", "bu kamayish tartibi"),
   ("H₂SO₄ → H₃PO₄ → H₂SiO₃ → HClO₄", "tartib buzilgan"),
   ("H₃PO₄ → H₂SiO₃ → HClO₄ → H₂SO₄", "tartib aralash")],
  "Davrda o'ngga markaziy atom EM i ortadi → kislorodli kislotalar kuchayadi; HClO₄ — eng kuchlilaridan.",
  dict(arch="kislota_qator"))

# 12 (2) — davr raqami
q(2, "yuqori",
  "4-davr elementining atomida nechta elektron qavat bor?",
  "4", [("3", "davr raqami qavatlar soniga teng"), ("8", "guruh bilan chalkashuv"),
         ("18", "davrdagi elementlar soni")],
  "Davr raqami = qavatlar soni.",
  dict(arch="davr_qavat"))

# 13 (3) — 1-2-3: metallik kuchayishi
q(3, "yuqori",
  "Qaysi qatorlarda elementlarning METALLIK xossasi KUCHAYIB boradi?\n"
  "1) Li → Na → K;  2) Al → Mg → Na;  3) Be → Mg → Ca;  4) Cl → S → P.",
  "1, 2 va 3",
  [("faqat 1", "2 va 3 da ham metallik kuchayadi (chapga va pastga)"),
   ("1 va 4", "4-qator — metallmaslar faolligi, metallik emas"),
   ("2 va 4", "1 va 3 ham to'g'ri")],
  "Guruhda pastga (1, 3) va davrda chapga (2) metallik kuchayadi.",
  dict(arch="metallik_tanlov"))

# 14 (3) — RASMLI: jadval fragmenti
q(3, "yuqori",
  "Rasmda davriy jadval fragmenti berilgan: X elementining ustida N, chap yonida Si, o'ng yonida S "
  "turibdi. X ning OLIY oksidi formulasini aniqlang.",
  "X₂O₅ (P₂O₅)", [("XO₂", "bu Si ning oksidi"), ("XO₃", "bu S ning oliy oksidi"),
                   ("X₂O₃", "V A da oliy valentlik 5")],
  "N ostida, Si va S orasida — fosfor (V A, 3-davr) → oliy oksid P₂O₅.",
  dict(arch="fragment_oqish"), fig="pt_fragment")

# 15 (3) — teskari: % dan element (R2O5)
check("q15", 80/(2*31+80)*100, 56.3, tol=0.2)
q(3, "yuqori",
  "Elementning oliy oksidi R₂O₅ tarkibida 56,3 % kislorod bor. Elementni aniqlang.",
  "P", [("N", "N₂O₅ da O — 74 %"), ("As", "As₂O₅ da O — 34,8 %"), ("V", "V₂O₅ da O — 44 %")],
  "80/(2M+80) = 0,563 → 2M + 80 = 142 → M = 31 — fosfor.",
  dict(arch="foizdan_element"))

# 16 (2) — eng elektromanfiy
q(2, "yuqori",
  "Barcha elementlar ichida ELEKTROMANFIYLIGI eng katta element qaysi?",
  "F", [("O", "ikkinchi o'rinda"), ("Cl", "ftordan past"), ("Cs", "aksincha — eng kichiklaridan")],
  "Ftor (EM = 4,0) — jadvalning yuqori-o'ng burchagi.",
  dict(arch="eng_em"))

# 17 (3) — JADVALLI: element pasporti «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni mos ravishda aniqlang:\n"
  "[JADVAL] Element | davr | guruh | oliy oksid ;; Se | 4 | VI A | ? ;; Br | 4 | ? | Br₂O₇",
  "SeO₃ va VII A",
  [("SeO₂ va VII A", "oliy oksidda valentlik guruhga teng: VI → SeO₃"),
   ("SeO₃ va VI A", "Br₂O₇ dan guruh VII ekani ko'rinadi"),
   ("Se₂O₅ va V A", "ikkala katak ham xato")],
  "Se: VI A → SeO₃. Br: oksidi R₂O₇ → VII A.",
  dict(arch="pasport_jadval"))

# 18 (2) — metallmaslik qatori
q(2, "yuqori",
  "Qaysi qatorda METALLMASLIK xossasi kuchayib boradi?",
  "Si → P → S → Cl",
  [("Cl → S → P → Si", "bu kamayish"), ("F → Cl → Br → I", "guruhda pastga kuchsizlanadi"),
   ("Na → K → Rb → Cs", "bular metallar — metallik kuchaymoqda")],
  "Davrda o'ngga metallmaslik (EM, oksidlovchilik) kuchayadi.",
  dict(arch="metallmas_qator"))

# 19 (3) — gidroksid xarakteri
q(3, "yuqori",
  "NaOH → Mg(OH)₂ → Al(OH)₃ qatorida gidroksidlarning xarakteri qanday o'zgaradi?",
  "kuchli asosdan amfoterlikka tomon (asoslik kuchsizlanadi)",
  [("kislotalik kuchsizlanadi", "bular kislota emas — asoslik haqida gap"),
   ("asoslik kuchayadi", "aksincha: Al(OH)₃ amfoter"),
   ("o'zgarish yo'q", "davrda xarakter muntazam o'zgaradi")],
  "Davrda o'ngga: kuchli ishqor → kuchsiz asos → amfoter gidroksid.",
  dict(arch="gidroksid_qator"))

# 20 (2) — guruhda metallik
q(2, "yuqori",
  "Asosiy guruhchada YUQORIDAN PASTGA metallik xossasi qanday o'zgaradi?",
  "kuchayadi — tashqi elektron oson beriladi",
  [("kuchsizlanadi", "radius ortgani sari e berish osonlashadi"),
   ("o'zgarmaydi", "radius va tortishish o'zgaradi"),
   ("avval kuchayib, keyin kuchsizlanadi", "monoton kuchayadi")],
  "Radius ↑ → yadro tortishi tashqi e ga kuchsizroq → metallik ↑.",
  dict(arch="guruh_metallik"))

# 21 (3) — teskari: H% dan element (H2R)
check("q21", 2/(2+32)*100, 5.88, tol=0.05)
q(3, "yuqori",
  "VI A guruh elementining vodorodli birikmasida (H₂R) 5,88 % vodorod bor. Elementni aniqlang.",
  "S", [("O", "H₂O da H — 11,1 %"), ("Se", "H₂Se da H — 2,47 %"), ("Te", "H₂Te da H — 1,55 %")],
  "2/(2+M) = 0,0588 → M = 32 — oltingugurt (H₂S).",
  dict(arch="h_foizdan"))

# 22 (3) — 1-2-3: amfoter elementlar
q(3, "yuqori",
  "Qaysi elementlarning oksidi va gidroksidi AMFOTER xossaga ega?\n"
  "1) Be;  2) Na;  3) Al;  4) Zn;  5) Ca.",
  "1, 3 va 4",
  [("2 va 5", "Na va Ca — tipik asosli birikmalar beradi"),
   ("1, 2 va 3", "Na amfoter emas"),
   ("faqat 3", "Be(OH)₂ va Zn(OH)₂ ham amfoter")],
  "Amfoter «uchlik»: Be, Al, Zn (yana Cr³⁺, Sn, Pb).",
  dict(arch="amfoter_tanlov"))

# 23 (3) — ion va atom radiusi
q(3, "yuqori",
  "Zarralarni radiusi ORTIB borishi tartibida joylashtiring: Na⁺, Na, Cl, Cl⁻.",
  "Na⁺ < Cl < Na < Cl⁻",
  [("Na⁺ < Na < Cl < Cl⁻", "Cl atomi Na atomidan kichik (bir davr, o'ngda)"),
   ("Cl⁻ < Cl < Na < Na⁺", "teskari tartib"),
   ("Na < Na⁺ < Cl⁻ < Cl", "kation atomdan kichik, anion katta")],
  "Na⁺ (10 e, 2 qavat) eng kichik; Cl (99 pm) < Na (190 pm); Cl⁻ e biriktirgan — eng katta.",
  dict(arch="ion_radius"))

# 24 (2) — A va B guruhchalar
q(2, "yuqori",
  "Qaysi javobda faqat B (yonaki) guruhcha elementlari berilgan?",
  "Fe, Cu, Zn", [("Na, K, Li", "I A — asosiy guruhcha"), ("Cl, Br, I", "VII A"),
                  ("C, Si, Ge", "IV A")],
  "d-elementlar (Fe, Cu, Zn, Cr...) yonaki guruhchalarda joylashadi.",
  dict(arch="b_guruh"))

# 25 (3) — oksidlar xarakteri davrda
q(3, "yuqori",
  "3-davr oliy oksidlari Na₂O → Al₂O₃ → SO₃ qatorida xarakter qanday o'zgaradi?",
  "asosli → amfoter → kislotali",
  [("kislotali → amfoter → asosli", "teskari tartib"),
   ("hammasi asosli", "SO₃ — tipik kislotali oksid"),
   ("hammasi amfoter", "faqat Al₂O₃ amfoter")],
  "Davrda o'ngga oksidlar asoslidan kislotaliga o'tadi; o'rtada amfoterlar.",
  dict(arch="oksid_qator"))

# 26 (3) — RASMLI: EM ustunlari
q(3, "yuqori",
  "Diagrammada 2-davr elementlarining elektromanfiyliklari berilgan. Qaysi ikki element orasidagi "
  "bog' ENG qutbli (ΔEM eng katta) bo'ladi?",
  "Li va F", [("C va N", "ΔEM ≈ 0,5 — kichik"), ("B va C", "ΔEM ≈ 0,5"),
               ("N va O", "ΔEM ≈ 0,5")],
  "Diagrammadan: Li (1,0) va F (4,0) — ΔEM = 3,0, eng katta (LiF — ion birikma).",
  dict(arch="em_bars_oqish"), fig="em_bars")

# 27 (3) — teskari: R2O7 dan element
check("q27", 71/(71+112)*100, 38.8, tol=0.2)
q(3, "yuqori",
  "Elementning oliy oksidi R₂O₇ tarkibida element 38,8 % ni tashkil etadi. Elementni aniqlang.",
  "Cl", [("Mn", "Mn₂O₇ da Mn — 49,5 %"), ("Br", "Br₂O₇ da Br — 58,8 %"), ("I", "I₂O₇ da I — 69 %")],
  "2M/(2M+112) = 0,388 → 2M = 71 → M = 35,5 — xlor.",
  dict(arch="r2o7_teskari"))

# 28 (2) — RASMLI: fragmentdan radius
q(2, "yuqori",
  "14-savoldagi jadval fragmentidan foydalaning: ko'rsatilgan elementlar ichida atom radiusi ENG KATTA "
  "bo'lgani qaysi?",
  "As (pastki qator)", [("N (yuqori qator)", "guruhda yuqorida — eng kichik"),
                         ("S", "o'ng tomonda — kichikroq"), ("X (P)", "As dan yuqorida")],
  "Radius pastga va chapga ortadi: fragmentda eng pastdagi As eng katta.",
  dict(arch="fragment_radius"), fig="pt_fragment")

# 29 (3) — 3-davr RO2
q(3, "yuqori",
  "3-davr elementining oliy oksidi RO₂ ko'rinishga ega. Uning gidroksidi haqida to'g'ri xulosa qaysi?",
  "H₂SiO₃ — kuchsiz, suvda erimaydigan kislota",
  [("NaOH — kuchli ishqor", "RO₂ → IV A → Si, natriy emas"),
   ("H₂SO₄ — kuchli kislota", "S ning oliy oksidi SO₃ bo'lardi"),
   ("Al(OH)₃ — amfoter", "Al ning oksidi Al₂O₃")],
  "RO₂, 3-davr → Si → gidroksidi H₂SiO₃ (kremniy kislota) — kuchsiz.",
  dict(arch="ro2_element"))

# 30 (2) — davrlar soni
q(2, "yuqori",
  "Hozirgi davriy sistemada nechta davr bor?",
  "7", [("8", "8-davr hali to'ldirilmagan"), ("10", "guruhlar ham 8 A + 8 B"), ("18", "bu ustunlar soni (IUPAC)")],
  "7 davr: 1–3 kichik, 4–7 katta davrlar.",
  dict(arch="davr_soni"))

# 31 (3) — teskari: H3RO4 + RH3
check("q31", 3/(3+31)*100, 8.82, tol=0.05)
q(3, "yuqori",
  "Elementning gidroksidi H₃RO₄, vodorodli birikmasida esa 8,82 % vodorod bor. Elementni aniqlang.",
  "P", [("N", "NH₃ da H — 17,6 %"), ("As", "AsH₃ da H — 3,85 %"), ("Sb", "SbH₃ da H — 2,4 %")],
  "H₃RO₄ → V A → RH₃: 3/(3+M) = 0,0882 → M = 31 — fosfor.",
  dict(arch="h3ro4_teskari"))

# 32 (3) — RASMLI: radius grafigi ikkinchi o'qish
check("q32", 190/99, 1.9, tol=0.05)
q(3, "yuqori",
  "5-savoldagi grafikdan foydalaning: Na va Cl atom radiuslarining nisbatini taxminan toping.",
  "≈1,9", [("≈1,2", "qiymatlar 190 va 99 pm"), ("≈3", "juda katta olingan"), ("≈0,5", "teskari nisbat")],
  "r(Na)/r(Cl) = 190/99 ≈ 1,9.",
  dict(arch="radius_nisbat"), fig="radius_line")

# ---------- Y2: element-detektiv ssenariysi ----------
check("y2_34", 2*31+80, 142)
Y2 = dict(
  n=33, tur="Y2", element="I.2",
  ichki_pasport=[dict(n=33, element="I.2", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.2", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("X elementi 3-davrda joylashgan; uning uchuvchan vodorodli birikmasi XH₃, oliy oksidida "
               "esa massa jihatdan 43,7 % element bor. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X elementini aniqlang.",
    "34. X ning oliy oksidi molyar massasini (g/mol) toping.",
    "35. X ning gidroksidi (oliy) qaysi modda?"],
  javoblar_royxati=["A) P", "B) 142", "C) H₃PO₄", "D) N", "E) 110", "F) HPO₃ emas — H₃PO₃"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="azot 2-davrda; shart 3-davr deydi"),
                   dict(variant="E", xato="P₂O₃ massasi — oliy oksid P₂O₅ (142)"),
                   dict(variant="F", xato="oliy gidroksid — H₃PO₄ (ortofosfat kislota)"),],
  yechim=("XH₃ → V A; 3-davr → P (tekshiruv: P₂O₅ da 62/142 = 43,7 % ✓) (A). "
          "M(P₂O₅) = 142 (B). Oliy gidroksidi — H₃PO₄ (C)."),
  parametrlar=dict(arch="detektiv_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36", 32/80*100, 40); check("o36b", 2+32, 34)
check("o37", 14.2/142, 0.1); check("o37b", 0.1*7, 0.7)
check("o38", 3.36/22.4, 0.15); check("o38b", 0.3*23, 6.9)
check("o39", 0.05*7*16, 5.6)
check("o40", 15.6/156, 0.1); check("o40b", 0.1*2+0.1*2, 0.4)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="X elementining oliy oksidi RO₃ tarkibida 40 % element bor. X ning VODORODLI birikmasi "
            "molyar massasini (g/mol) toping.",
      javob="34", yechim="M/(M+48) = 0,4 → M = 32 → S. Vodorodli birikma H₂S: M = 34 g/mol.",
      parametrlar=dict(arch="oksiddan_vodorodli")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="Elementning konfiguratsiyasi ...3s²3p³ bilan tugaydi. Uning oliy oksididan 14,2 g olinganda "
            "undagi JAMI atomlar mol sonini toping.",
      javob="0,7", yechim="P (V A) → P₂O₅ (M=142): n = 0,1 mol → atomlar 0,1·(2+5) = 0,7 mol.",
      parametrlar=dict(arch="konfig_oksid_atom")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi X — 3-davr, I A guruh elementi. U suv bilan reaksiyaga kirishganda 3,36 l (n.sh.) "
            "gaz ajraldi. Reaksiyaga kirishgan X ning massasini (g) toping.",
      javob="6,9", yechim="X = Na. 2Na + 2H₂O → 2NaOH + H₂: H₂ = 0,15 mol → Na = 0,3 mol → 6,9 g.",
      parametrlar=dict(arch="sxema_metall"), fig="scheme2"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="VII A guruh elementining oliy oksididan 0,05 mol olindi. Undagi kislorodning massasini (g) toping.",
      javob="5,6", yechim="R₂O₇: har mol oksidda 7 mol O → 0,05·7·16 = 5,6 g.",
      parametrlar=dict(arch="r2o7_kislorod")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Teng mol miqdorda olingan Na₂O va K₂O dan iborat 15,6 g aralashmadagi metall atomlarining "
            "umumiy mol sonini toping.",
      javob="0,4", yechim="62x + 94x = 15,6 → x = 0,1 mol har biridan → metall: 0,2 + 0,2 = 0,4 mol.",
      parametrlar=dict(arch="aralash_oksid")),
]

# ---------- O2 ----------
check("o41a", 48/80*100, 60)
check("o41c", 0.2*2*40, 16)
check("o43c", 0.1*2*40, 8)
O2 = [
 dict(n=41, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "X elementining oliy oksidi RO₃ bo'lib, unda 60 % kislorod bor. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X elementini hisob orqali aniqlang.",
             yechim=["48/(M+48) = 0,6 → M = 32 → oltingugurt (S)."], M=4, A=2),
        dict(savol="b) X ning davriy sistemadagi o'rnini (davr, guruh) va konfiguratsiyasini yozing.",
             yechim=["3-davr, VI A; 1s²2s²2p⁶3s²3p⁴."], M=3, A=2),
        dict(savol="c) Oliy oksidiga mos gidroksidning 0,2 molini to'liq neytrallash uchun necha gramm "
                   "NaOH kerak? (M(NaOH)=40)",
             yechim=["H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O: 0,4 mol → 16 g."], M=4, A=3),
        dict(savol="d) X ning vodorodli birikmasini yozing va uning suvdagi eritmasi muhitini ayting.",
             yechim=["H₂S; eritmasi kuchsiz kislotali."], M=2, A=2),
        dict(savol="e) Davr bo'yicha qo'shnisi P bilan solishtirganda X ning metallmasligi qanday? Sababini yozing.",
             yechim=["Kuchliroq: davrda o'ngga EM va oksidlovchilik ortadi."], M=2, A=1),
      ],
      rasmiylashtirish="Element-aniqlash zanjiri: hisob → o'rin → neytrallash → xossalar; M15+A10.",
      parametrlar=dict(arch="element_zanjir")),
 dict(n=42, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Davriy qonun tarixi va mohiyati haqida MULOHAZA yuritib javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) Mendeleev jadvalida Ar (Ar=40) K (Ar=39) dan OLDIN turadi — massa tartibi buzilgan. "
                   "Zamonaviy davriy qonun buni qanday hal qiladi? Asoslab yozing.",
             yechim=["Asos — atom massasi emas, yadro zaryadi: Z(Ar)=18 < Z(K)=19.",
                     "Xossalar Z ga (elektron tuzilishga) bog'liq — tartib to'g'ri."], M=13, A=0),
        dict(savol="b) Mendeleev hali ochilmagan elementlar (masalan, galliy) xossalarini oldindan aytib "
                   "bergan. Bu qanday qilib mumkin bo'lgan?",
             yechim=["Davriylik tufayli bo'sh katak xossalari qo'shnilari (yuqori-quyi, chap-o'ng)",
                     "xossalaridan oraliq qiymat sifatida bashorat qilinadi."], M=9, A=0),
        dict(savol="c) Davriylikning sababi nimada? Bir jumla bilan yozing.",
             yechim=["Tashqi elektron qavat tuzilishining davriy takrorlanishi."], M=3, A=0),
      ],
      rasmiylashtirish="Tarix-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="mendeleev_mulohaza")),
 dict(n=43, tur="O2", element="I.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha hisoblarni uzviy ketma-ketlikda yozing. "
            "3-davr uch elementining oliy oksidlari jadvalda berilgan:\n"
            "[JADVAL] Element | Na | Al | S ;; Oliy oksid | Na₂O | Al₂O₃ | SO₃ ;; Xarakteri | ? | ? | ?\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Jadvaldagi «?» kataklarni to'ldiring va har birini bir jumla bilan asoslang.",
             yechim=["Na₂O — asosli (ishqoriy metall); Al₂O₃ — amfoter; SO₃ — kislotali (metallmas oliy oksidi)."], M=5, A=2),
        dict(savol="b) Al₂O₃ ning amfoterligini ikkita reaksiya tenglamasi bilan isbotlang.",
             yechim=["Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O; Al₂O₃ + 2NaOH → 2NaAlO₂ + H₂O."], M=4, A=3),
        dict(savol="c) 0,1 mol SO₃ ga mos kislotani to'liq neytrallash uchun necha gramm NaOH kerak?",
             yechim=["H₂SO₄ 0,1 mol → NaOH 0,2 mol → 8 g."], M=3, A=3),
        dict(savol="d) Ushbu qatordan davr bo'yicha qanday umumiy qonuniyat kelib chiqadi?",
             yechim=["Davrda chapdan o'ngga oksid/gidroksidlar asoslidan amfoter orqali kislotaliga o'tadi."], M=3, A=2),
      ],
      rasmiylashtirish="Oksid-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="oksid_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260222)
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
    d = dict(n=n, tur="Y1", element="I.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I2-B", daraja="B", bob=2, bob_nomi="Davriy qonun va davriy sistema",
    manba=("Tongotarov/Spectrum variantlari arxetiplari (xossa qatorlari, %-dan element, fragment) — "
           "javoblar mustaqil tekshirilgan; MS spetsifikatsiyasi I.2"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: teskari (%-dan element) masalalar, xossa qatorlari, "
          "jadval fragmenti, ko'p bosqichli 36–40."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
