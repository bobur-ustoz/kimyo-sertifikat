# -*- coding: utf-8 -*-
"""9-bob A-varianti: Oksidlanish-qaytarilish reaksiyalari (I.9) — O'RGATUVCHI ★★.
Hayotiy sahnalar: kesilgan olma, bengal olovi (otashin), zanglagan panjara, batareyka.
Soddaroq sonlar, o'rgatuvchi chalg'ituvchilar; barcha javoblar mustaqil hisoblangan."""
import json, random

OUT = "mavzu_I9A.json"
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

# 1 (2) — OQR ta'rifi
q(2, "quyi",
  "Oksidlanish-qaytarilish reaksiyalari deb qanday reaksiyalarga aytiladi?",
  "elementlarning oksidlanish darajalari o'zgaradigan reaksiyalarga",
  [("issiqlik ajralib chiqadigan reaksiyalarga", "issiqlik effekti OQR mezoni emas"),
   ("cho'kma hosil bo'ladigan reaksiyalarga", "cho'kma almashinishda ham hosil bo'ladi"),
   ("faqat kislorod ishtirok etadigan reaksiyalarga", "kislorodsiz OQR ham ko'p (masalan, Fe + Cl₂)")],
  "OQR belgisi — kamida ikkita elementning oksidlanish darajasi o'zgarishi (elektron almashinishi).",
  dict(arch="oqr_tarif"))

# 2 (2) — oksidlanish ta'rifi
q(2, "quyi",
  "Oksidlanish jarayoni deb nimaga aytiladi?",
  "zarrachaning elektron BERISHIGA",
  [("zarrachaning elektron OLISHIGA", "bu qaytarilish jarayoni"),
   ("moddaning kislorod bilan birikishiga", "torroq ta'rif — kislorodsiz oksidlanish ham bor"),
   ("moddaning parchalanishiga", "parchalanish alohida reaksiya turi")],
  "Oksidlanish — e berish (daraja ortadi); qaytarilish — e olish (daraja pasayadi).",
  dict(arch="oksidlanish_tarif"))

# 3 (2) — daraja aniqlash oddiy
q(2, "o'rta",
  "H₂SO₄ birikmasidagi oltingugurtning oksidlanish darajasini aniqlang.",
  "+6", [("+4", "SO₂ dagi qiymat"), ("−2", "H₂S dagi qiymat"), ("+2", "asossiz qiymat")],
  "2(+1) + x + 4(−2) = 0 → x = +6.",
  dict(arch="daraja_oddiy"))

# 4 (2) — SAHNA: kesilgan olma
q(2, "o'rta",
  "Rasmga qarang: kesilgan olma bir necha daqiqada qorayadi. Buning kimyoviy sababi nimada?",
  "olma tarkibidagi moddalar havo kislorodi ta'sirida oksidlanadi",
  [("olma suvi bug'lanib ketadi", "qurish rang o'zgarishiga bunchalik tez olib kelmaydi"),
   ("olma tarkibida temir zanglaydi", "qorayish polifenollarning oksidlanishi, temir zangi emas"),
   ("yorug'lik olmani kuydiradi", "jarayon qorong'ida ham boradi")],
  "Kislorod — oksidlovchi: olma to'qimasidagi moddalarni oksidlab, qoramtir mahsulotlar hosil qiladi. "
  "Limon sharbati (vitamin C — qaytaruvchi) bu jarayonni sekinlashtiradi.",
  dict(arch="olma_sahna"), fig="apple")

# 5 (2) — qaytaruvchi ta'rifi
q(2, "quyi",
  "Reaksiyada QAYTARUVCHI vazifasini bajargan zarracha ...",
  "elektron beradi va o'zi oksidlanadi",
  [("elektron oladi va o'zi qaytariladi", "bu oksidlovchining ta'rifi"),
   ("elektron beradi va o'zi qaytariladi", "e bergan zarracha oksidlanadi"),
   ("elektron olmaydi ham, bermaydi ham", "unda u OQR ishtirokchisi emas")],
  "Qaytaruvchi e beradi (o'zi oksidlanadi) va sherigini qaytaradi.",
  dict(arch="qaytaruvchi_tarif"))

# 6 (3) — daraja: KMnO4
q(3, "o'rta",
  "KMnO₄ birikmasidagi marganesning oksidlanish darajasini aniqlang.",
  "+7", [("+4", "MnO₂ dagi qiymat"), ("+2", "MnSO₄ dagi qiymat"), ("+6", "K₂MnO₄ dagi qiymat")],
  "+1 + x + 4(−2) = 0 → x = +7. Shu sababli KMnO₄ — kuchli oksidlovchi.",
  dict(arch="daraja_kmno4"))

# 7 (2) — jarayonni tanish
q(2, "o'rta",
  "Zn⁰ → Zn²⁺ o'zgarishi qanday jarayon?",
  "oksidlanish — 2 ta elektron berildi",
  [("qaytarilish — 2 ta elektron olindi", "daraja ortdi (0 → +2), demak e berildi"),
   ("almashinish", "bu elektron almashinuvli yarim reaksiya"),
   ("dissotsiatsiya", "dissotsiatsiyada daraja o'zgarmaydi")],
  "Daraja 0 dan +2 ga ortdi → Zn 2e berdi → oksidlanish.",
  dict(arch="jarayon_tanish"))

# 8 (2) — SAHNA: bengal olovi / otashin
q(2, "o'rta",
  "Rasmda bayram otashini (bengal olovi) ko'rsatilgan: magniy kukuni yorqin oq alanga bilan yonadi "
  "(2Mg + O₂ → 2MgO). Bu reaksiyada magniy qanday vazifani bajaradi?",
  "qaytaruvchi — elektron berib oksidlanadi",
  [("oksidlovchi — elektron oladi", "e oluvchi — kislorod"),
   ("katalizator — o'zi o'zgarmaydi", "Mg reaksiyada MgO ga aylanadi"),
   ("muhit hosil qiluvchi", "bu tushuncha eritmalardagi reaksiyalarga oid")],
  "Mg⁰ − 2e → Mg⁺² (oksidlandi, ya'ni qaytaruvchi); O₂ + 4e → 2O⁻² (oksidlovchi). Yorug'lik — reaksiya energiyasi.",
  dict(arch="otashin_sahna"), fig="firework")

# 9 (2) — oksidlovchini topish
q(2, "o'rta",
  "CuO + H₂ → Cu + H₂O reaksiyasida OKSIDLOVCHI qaysi modda?",
  "CuO", [("H₂", "vodorod e berdi (0 → +1) — qaytaruvchi"),
           ("Cu", "mahsulot — qaytarilgan mis"), ("H₂O", "mahsulot oksidlovchi bo'lmaydi")],
  "Cu⁺² + 2e → Cu⁰: mis oksidi e oldi — oksidlovchi. H₂ — qaytaruvchi.",
  dict(arch="oksidlovchi_topish"))

# 10 (2) — elektron soni
q(2, "o'rta",
  "Al⁰ → Al³⁺ o'zgarishida bitta alyuminiy atomi nechta elektron beradi?",
  "3", [("1", "guruh raqami emas, daraja farqi olinadi... aslida 3"), ("2", "Mg uchun qiymat"),
         ("13", "tartib raqami bilan chalkashuv")],
  "Daraja 0 dan +3 ga ortdi → 3 e berildi.",
  dict(arch="e_soni_oddiy"))

# 11 (2) — 1-2-3 yengil
q(2, "o'rta",
  "Quyidagi o'zgarishlarning qaysilari OKSIDLANISH hisoblanadi?\n"
  "1) S⁰ → S⁺⁴;  2) Cu⁺² → Cu⁰;  3) N⁻³ → N⁺².",
  "1 va 3",
  [("faqat 1", "3-o'zgarishda ham daraja ortgan (−3 → +2)"),
   ("2 va 3", "2 — qaytarilish (daraja pasaygan)"),
   ("1 va 2", "2 — qaytarilish")],
  "Oksidlanish — daraja ortishi: 1 (0→+4) va 3 (−3→+2). 2 — qaytarilish.",
  dict(arch="tanlov_yengil"))

# 12 (2) — daraja: NH3
q(2, "o'rta",
  "Ammiak (NH₃) tarkibidagi azotning oksidlanish darajasi qanday?",
  "−3", [("+3", "ishora teskari olingan"), ("0", "erkin azotdagi qiymat"), ("+5", "nitratlardagi qiymat")],
  "x + 3(+1) = 0 → x = −3.",
  dict(arch="daraja_nh3"))

# 13 (2) — SAHNA: zanglagan panjara
q(2, "o'rta",
  "Rasmda zanglagan temir panjara ko'rsatilgan. Zanglash (korroziya) jarayonida temir qanday "
  "vazifani bajaradi?",
  "qaytaruvchi — elektron berib Fe⁺³ gacha oksidlanadi",
  [("oksidlovchi — elektron oladi", "e oluvchi — havo kislorodi (nam ishtirokida)"),
   ("katalizator", "temirning o'zi zangga aylanadi"),
   ("hech qanday — zanglash fizik jarayon", "zanglash — tipik OQR")],
  "4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃: temir e beradi (qaytaruvchi), kislorod oladi (oksidlovchi).",
  dict(arch="zang_sahna"), fig="fence")

# 14 (3) — balans oddiy
check("q14", 2+1+2, 5)
q(3, "o'rta",
  "Mg + O₂ → MgO reaksiyasi tenglashtirilganda barcha koeffitsiyentlar yig'indisini toping.",
  "5", [("3", "tenglashtirilmagan holda"), ("4", "MgO oldida 1 qoldirilgan"),
         ("7", "ortiqcha ikkilantirilgan")],
  "2Mg + O₂ → 2MgO (Mg−2e ×2; O₂+4e ×1). Jami: 2+1+2 = 5.",
  dict(arch="balans_oddiy"))

# 15 (3) — e mol hisob
check("q15", 0.3*2, 0.6)
q(3, "o'rta",
  "0,3 mol rux to'liq oksidlanib Zn²⁺ ga o'tganda necha mol elektron beradi?",
  "0,6", [("0,3", "valentlik unutilgan"), ("1,2", "4 e deb olingan"), ("0,15", "bo'lish xatosi")],
  "n(e) = 0,3·2 = 0,6 mol.",
  dict(arch="e_mol_oddiy"))

# 16 (2) — disproporsiya misoli
q(2, "o'rta",
  "Quyidagi reaksiyalardan qaysi biri DISPROPORSIYAGA (bir element ham oksidlanib, ham qaytarilishiga) misol?",
  "Cl₂ + H₂O → HCl + HClO",
  [("Zn + 2HCl → ZnCl₂ + H₂", "ikki xil element almashinadi — molekulyararo"),
   ("CaCO₃ → CaO + CO₂", "darajalar o'zgarmaydi — OQR emas"),
   ("Fe + S → FeS", "birikish, ikki xil element")],
  "Cl⁰ bir vaqtda −1 (HCl) va +1 (HClO) ga o'tadi — disproporsiya.",
  dict(arch="disprop_misol"))

# 17 (2) — jadval o'qish yengil
q(2, "o'rta",
  "Jadvalda reaksiya ishtirokchilarining darajalari berilgan:\n"
  "[JADVAL] Element | boshlang'ich | oxirgi ;; Mn | +7 | +2 ;; Fe | +2 | +3\n"
  "OKSIDLOVCHI qaysi element?",
  "Mn — darajasi pasaygan", [("Fe — darajasi ortgan", "daraja ortishi qaytaruvchini bildiradi"),
                              ("ikkalasi ham", "faqat e olgan zarracha oksidlovchi"),
                              ("hech qaysi", "Mn e oldi — u oksidlovchi")],
  "Mn: +7 → +2 (5 e oldi) — oksidlovchi. Fe: +2 → +3 (e berdi) — qaytaruvchi.",
  dict(arch="jadval_yengil"))

# 18 (2) — SAHNA: batareyka
q(2, "o'rta",
  "Rasmda cho'ntak batareykasi ko'rsatilgan: unda rux g'ilof asta-sekin yemiriladi va tok hosil "
  "bo'ladi. Rux qanday vazifani bajaradi?",
  "qaytaruvchi — elektron berib, tashqi zanjirga tok beradi",
  [("oksidlovchi — elektron yig'adi", "e beruvchi elektrod aynan rux"),
   ("izolyator", "rux g'ilof elektrodning o'zi"),
   ("katalizator", "rux sarflanadi — katalizator sarflanmaydi")],
  "Batareyka — OQRdan tok oladi: Zn⁰ − 2e → Zn⁺² (qaytaruvchi); elektronlar tashqi zanjir orqali oqadi.",
  dict(arch="batareyka_sahna"), fig="battery")

# 19 (3) — balans: Fe + Cl2
check("q19", 2+3+2, 7)
q(3, "o'rta",
  "Fe + Cl₂ → FeCl₃ reaksiyasi tenglashtirilganda barcha koeffitsiyentlar yig'indisini toping.",
  "7", [("5", "FeCl₂ deb olingan (1+1+... xato)"), ("6", "Cl₂ oldida 2"), ("4", "tenglashtirilmagan")],
  "2Fe + 3Cl₂ → 2FeCl₃ (Fe−3e ×2; Cl₂+2e ×3). Jami: 2+3+2 = 7.",
  dict(arch="balans_fecl3"))

# 20 (2) — oddiy modda darajasi
q(2, "quyi",
  "Erkin holdagi oddiy moddalarda (Cl₂, O₂, Fe) elementlarning oksidlanish darajasi qanday?",
  "0", [("+1", "birikmalardagi vodorod qiymati"), ("−1", "galogenidlardagi qiymat"),
         ("guruh raqamiga teng", "bu eng yuqori daraja, erkin holat emas")],
  "Oddiy moddada element «o'z-o'zi» bilan bog'langan — daraja 0.",
  dict(arch="oddiy_modda"))

# 21 (3) — e balans koeffitsiyenti
check("q21", 4, 4)
q(3, "o'rta",
  "Al + O₂ → Al₂O₃ reaksiyasi elektron balans bilan tenglashtirilganda QAYTARUVCHI oldida qanday "
  "koeffitsiyent turadi?",
  "4", [("2", "Al₂O₃ dagi indeks"), ("3", "kislorod koeffitsiyenti"), ("1", "tenglashtirilmagan")],
  "Al−3e ×4; O₂+4e ×3 → 4Al + 3O₂ → 2Al₂O₃. Qaytaruvchi (Al) oldida 4.",
  dict(arch="balans_al"))

# 22 (3) — KMnO4 oladigan e
check("q22", 0.1*5, 0.5)
q(3, "o'rta",
  "Kislotali muhitda 0,1 mol KMnO₄ (Mn⁺⁷ → Mn⁺²) qaytarilganda necha mol elektron oladi?",
  "0,5", [("0,1", "5 e ekani unutilgan"), ("0,7", "daraja qiymati (+7) ko'paytirilgan"),
           ("0,2", "2 e deb olingan")],
  "Har bir Mn⁺⁷ 5 e oladi → 0,1·5 = 0,5 mol e.",
  dict(arch="kmno4_e"))

# 23 (2) — qaytarilish jarayoni
q(2, "o'rta",
  "Quyidagi o'zgarishlardan qaysi biri QAYTARILISH jarayoni?",
  "Cu²⁺ → Cu⁰",
  [("S⁰ → S⁺⁴", "daraja ortgan — oksidlanish"), ("Fe⁺² → Fe⁺³", "e berilgan — oksidlanish"),
   ("Cl⁻ → Cl₂", "daraja ortgan — oksidlanish")],
  "Qaytarilish — e olish, daraja pasayishi: +2 → 0.",
  dict(arch="qaytarilish_tanish"))

# 24 (3) — Cu + AgNO3 hisob
check("q24", 0.1*2*108, 21.6)
q(3, "o'rta",
  "Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag. 0,1 mol mis reaksiyaga to'liq kirishganda necha gramm kumush "
  "ajralib chiqadi? (M(Ag)=108)",
  "21,6", [("10,8", "1:1 nisbat olingan"), ("108", "1 mol deb olingan"), ("5,4", "0,05 mol xato")],
  "Ag = 0,1·2 = 0,2 mol → 0,2·108 = 21,6 g.",
  dict(arch="cu_ag_hisob"))

# 25 (2) — kuchli oksidlovchi tanlash
q(2, "o'rta",
  "Quyidagi moddalardan qaysi birida element ENG YUQORI darajada bo'lib, u faqat OKSIDLOVCHI bo'la oladi?",
  "KMnO₄ (Mn⁺⁷)", [("MnO₂ (Mn⁺⁴)", "oraliq daraja — ikkala vazifada"),
                    ("MnSO₄ (Mn⁺²)", "past daraja — asosan qaytaruvchi"),
                    ("Mn (Mn⁰)", "metall — qaytaruvchi")],
  "Eng yuqori darajadagi element boshqa e ololmaydi berishga esa «yuqoriroq joy» yo'q — faqat oksidlovchi.",
  dict(arch="eng_yuqori"))

# 26 (3) — grafik tanlash: e ~ mol proporsional
q(3, "o'rta",
  "Alyuminiy mol soni ortib borganda u beradigan elektron mollari qanday o'zgaradi? "
  "To'g'ri grafikni tanlang.",
  "to'g'ri proporsional ortib boradi",
  [("o'zgarmaydi", "har mol Al 3 mol e beradi — bog'liqlik bor"),
   ("ortib, keyin to'xtaydi", "chegara yo'q — nisbat doimiy 3"),
   ("avval ortib, keyin kamayadi", "kamayishga sabab yo'q")],
  "n(e) = 3·n(Al) — noldan chiquvchi to'g'ri chiziq.",
  svg=dict(correct="rise", d1="flat", d2="rise_flat", d3="rise_fall", xlab="n(Al)", ylab="n(e)"),
  params=dict(arch="grafik_proporsional"))

# 27 (3) — e mol hisob (massadan)
check("q27", 5.4/27*3, 0.6)
q(3, "o'rta",
  "5,4 g alyuminiy to'liq oksidlanganda necha mol elektron beradi? (M(Al)=27)",
  "0,6", [("0,2", "mol sonining o'zi"), ("1,8", "27 ga bo'lmasdan xato"), ("0,4", "2 e deb olingan")],
  "n(Al) = 0,2 mol → e = 0,2·3 = 0,6 mol.",
  dict(arch="massa_e"))

# 28 (2) — ichki molekulyar misol
q(2, "o'rta",
  "2KClO₃ →(t) 2KCl + 3O₂ reaksiyasi qaysi turdagi OQR?",
  "ichki molekulyar",
  [("disproporsiya", "Cl darajasi faqat pasaydi (+5→−1), ikkiga ajralmadi"),
   ("molekulyararo", "oksidlovchi (Cl⁺⁵) va qaytaruvchi (O⁻²) bitta molekulada"),
   ("OQR emas", "Cl: +5→−1, O: −2→0 — darajalar o'zgardi")],
  "Oksidlovchi ham, qaytaruvchi ham KClO₃ ning ichida (Cl⁺⁵ va O⁻²) — ichki molekulyar OQR.",
  dict(arch="ichki_misol"))

# 29 (3) — balans: H2S + O2
check("q29", 2+3+2+2, 9)
q(3, "o'rta",
  "H₂S + O₂ → SO₂ + H₂O reaksiyasi tenglashtirilganda barcha koeffitsiyentlar yig'indisini toping.",
  "9", [("7", "suv unutilgan"), ("5", "tenglashtirilmagan yig'indi"), ("11", "ortiqcha koeffitsiyent")],
  "2H₂S + 3O₂ → 2SO₂ + 2H₂O (S⁻²−6e ×2; O₂+4e ×3). Jami: 2+3+2+2 = 9.",
  dict(arch="balans_h2s"))

# 30 (2) — korroziyadan himoya
q(2, "o'rta",
  "Temir buyumni korroziyadan (zanglashdan) himoya qilishning qaysi usuli OKSIDLOVCHI bilan "
  "aloqani uzishga asoslangan?",
  "sirtini bo'yoq bilan qoplash",
  [("buyumni tez-tez yuvib turish", "nam — korroziyani tezlashtiradi"),
   ("buyumni qizdirish", "harorat oksidlanishni tezlashtiradi"),
   ("kislota bilan artish", "kislota temirni yemiradi")],
  "Bo'yoq qatlami havo kislorodi va namlikni (oksidlovchilarni) metalldan ajratib turadi.",
  dict(arch="himoya"))

# 31 (3) — CuO + H2 hisob
check("q31", 8/80*64, 6.4)
q(3, "o'rta",
  "8 g mis (II) oksidi vodorod bilan to'liq qaytarildi: CuO + H₂ → Cu + H₂O. Necha gramm mis "
  "hosil bo'ladi? (M(CuO)=80, M(Cu)=64)",
  "6,4", [("8", "massa o'zgarmaydi deb olingan"), ("3,2", "0,05 mol xato"), ("12,8", "0,2 mol xato")],
  "n(CuO) = 0,1 mol → Cu = 0,1·64 = 6,4 g.",
  dict(arch="cuo_hisob"))

# 32 (3) — RASMLI: aktivlik qatori
q(3, "o'rta",
  "Rasmda metallarning aktivlik qatori berilgan. Undan foydalanib aniqlang: qaysi metall CuSO₄ "
  "eritmasidan misni siqib chiqara OLADI?",
  "Fe", [("Ag", "qatorda misdan keyin — mis ionini qaytara olmaydi"),
          ("Au", "eng passiv metall"), ("Hg", "misdan keyin joylashgan")],
  "Qatorda misdan CHAP tomondagi (aktivroq) metallgina Cu²⁺ ni qaytaradi: Fe + CuSO₄ → FeSO₄ + Cu.",
  dict(arch="aktivlik_oqish"), fig="activity")

# ---------- Y2: bengal olovi ssenariysi ----------
check("y2_33", 2.4/24*2, 0.2)
check("y2_34", 2.4/24*40, 4)
check("y2_35", 2.4/24/2*22.4, 1.12)
Y2 = dict(
  n=33, tur="Y2", element="I.9",
  ichki_pasport=[dict(n=33, element="I.9", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.9", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.9", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Bayram otashinida 2,4 g magniy kukuni to'liq yondi: 2Mg + O₂ → 2MgO. "
               "(M(Mg)=24, M(MgO)=40.) 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Magniy bergan elektronlar necha mol?",
    "34. Hosil bo'lgan magniy oksidining massasi (g) qancha?",
    "35. Sarflangan kislorodning hajmi (l, n.sh.) qancha?"],
  javoblar_royxati=["A) 4", "B) 0,2", "C) 2,24", "D) 1,12", "E) 0,1", "F) 2"],
  javoblar={"33": "B", "34": "A", "35": "D"},
  chalgituvchilar=[dict(variant="C", xato="0,1 mol O₂ deb olish xatosi (aslida 0,05)"),
                   dict(variant="E", xato="Mg mol sonining o'zi"),
                   dict(variant="F", xato="MgO ni 0,05 mol deb olish xatosi")],
  yechim=("n(Mg) = 0,1 mol. 33: e = 0,1·2 = 0,2 mol (B). 34: MgO = 0,1·40 = 4 g (A). "
          "35: O₂ = 0,05 mol → 1,12 l (D)."),
  parametrlar=dict(arch="otashin_ssenariy", mg=2.4))

# ---------- O1 ----------
check("o37", 3-2, 1)
check("o38", 2+3+1, 6)
check("o39", 0.2*2, 0.4)
check("o40", 3.2/64*2*108, 10.8)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="Erkin azot (N₂) molekulasidagi azotning oksidlanish darajasini yozing.",
      javob="0", yechim="Oddiy modda — daraja 0.",
      parametrlar=dict(arch="daraja_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Fe²⁺ → Fe³⁺ o'zgarishida temir ioni nechta elektron beradi?",
      javob="1", yechim="Daraja +2 dan +3 ga ortdi → 1 e.",
      parametrlar=dict(arch="e_farq_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="Al + S → Al₂S₃ reaksiyasi tenglashtirilganda barcha koeffitsiyentlar yig'indisini toping.",
      javob="6", yechim="2Al + 3S → Al₂S₃ (Al−3e ×2; S+2e ×3). Jami: 2+3+1 = 6.",
      parametrlar=dict(arch="balans_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="0,2 mol magniy to'liq oksidlanganda beradigan elektron mollarini toping.",
      javob="0,4", yechim="0,2·2 = 0,4 mol e.",
      parametrlar=dict(arch="e_mol_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="3,2 g mis AgNO₃ ning mo'l eritmasiga tushirildi. Ajralib chiqqan kumushning massasini "
            "(g) toping. (M(Cu)=64, M(Ag)=108)",
      javob="10,8", yechim="n(Cu) = 0,05 mol → Ag = 0,1 mol → 10,8 g.",
      parametrlar=dict(arch="cu_ag_o1")),
]

# ---------- O2 ----------
check("o41b", 6.5/65, 0.1)
check("o41c", 0.1*64, 6.4)
check("o41d", 0.1*2, 0.2)
check("o43b", 11.2/56*64, 12.8)
check("o43c", 11.2/56*2, 0.4)
O2 = [
 dict(n=41, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("6,5 g rux mis (II) sulfatning mo'l eritmasiga tushirildi: Zn + CuSO₄ → ZnSO₄ + Cu. "
            "Bandlar ketma-ket yechiladi — har biri keyingisiga asos bo'ladi. (M(Zn)=65, M(Cu)=64)"),
      bandlar=[
        dict(savol="a) Reaksiyaning elektron balansini yozing: kim e beradi, kim oladi?",
             yechim=["Zn⁰ − 2e → Zn⁺² (qaytaruvchi); Cu⁺² + 2e → Cu⁰ (oksidlovchi)"], M=3, A=1),
        dict(savol="b) Ruxning miqdorini (mol) toping.",
             yechim=["n(Zn) = 6,5/65 = 0,1 mol"], M=3, A=2),
        dict(savol="c) Ajralib chiqqan misning massasini (g) hisoblang.",
             yechim=["Cu = 0,1 mol → 6,4 g"], M=4, A=3),
        dict(savol="d) Jarayonda necha mol elektron almashindi?",
             yechim=["e = 0,1·2 = 0,2 mol"], M=2, A=2),
        dict(savol="e) Nega bu reaksiya OQR hisoblanadi? Bir jumla bilan izohlang.",
             yechim=["Zn va Cu ning oksidlanish darajalari o'zgardi (0↔+2) — elektron almashindi."], M=3, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi zanjir: balans → mol → massa → elektron → izoh; M15+A10.",
      parametrlar=dict(arch="zn_cu_zanjir", zn=6.5)),
 dict(n=42, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Qishloq hovlisidagi temir panjara yomg'irli mavsumda tez zanglaydi. Quyidagi savollarga "
            "MULOHAZA yuritib javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) Zanglash jarayonining OQR mohiyatini yozing: qaytaruvchi va oksidlovchini ko'rsatib, "
                   "umumiy tenglamani keltiring.",
             yechim=["Fe — qaytaruvchi (Fe−3e→Fe⁺³), O₂ — oksidlovchi (nam ishtirokida):",
                     "4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃ (keyin quriydi — zang)."], M=13, A=0),
        dict(savol="b) Nega namlik (yomg'ir) zanglashni keskin tezlashtiradi?",
             yechim=["Suv elektrolit muhit yaratadi — elektron o'tishi (mikrogalvanik juftlar) osonlashadi;",
                     "quruq havoda jarayon juda sekin."], M=9, A=0),
        dict(savol="c) Panjarani himoya qilishning bitta usulini tavsiya qiling va sababini ayting.",
             yechim=["Bo'yash (yoki ruxlash): oksidlovchi (O₂, H₂O) bilan aloqa uziladi."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza formati (faqat M): M13+M9+M3 = 25 (rasmiy 42-format).",
      parametrlar=dict(arch="korroziya_mulohaza")),
 dict(n=43, tur="O2", element="I.9", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("O'quvchi uchta stakanda tajriba o'tkazdi; kuzatuvlar jadvalda:\n"
            "[JADVAL] Stakan | Metall | Eritma | Kuzatuv ;; 1 | Cu | FeSO₄ | o'zgarish yo'q ;; "
            "2 | Fe | CuSO₄ | qizil qatlam ;; 3 | Zn | CuSO₄ | qizil qatlam\n"
            "Bandlar ketma-ket yechiladi. (M(Fe)=56, M(Cu)=64)"),
      bandlar=[
        dict(savol="a) Nega 1-stakanda reaksiya bormadi? Aktivlik qatori orqali izohlang.",
             yechim=["Cu aktivlik qatorida Fe dan keyin — Fe⁺² ni qaytara olmaydi."], M=3, A=1),
        dict(savol="b) 2-stakan uchun tenglama yozing va 11,2 g temirdan ajraladigan mis massasini toping.",
             yechim=["Fe + CuSO₄ → FeSO₄ + Cu; n(Fe) = 0,2 mol → Cu = 12,8 g"], M=5, A=4),
        dict(savol="c) 2-stakan jarayonida almashingan elektron mollarini toping.",
             yechim=["e = 0,2·2 = 0,4 mol"], M=3, A=3),
        dict(savol="d) Uchala kuzatuvga tayanib Zn, Fe, Cu ni aktivlik tartibida joylashtiring.",
             yechim=["Zn > Fe > Cu (Zn va Fe misni siqib chiqardi; Cu temirni chiqara olmadi)."], M=4, A=2),
      ],
      rasmiylashtirish="Tajriba-jadval formati: M15+A10. B-variantdagi X/Y/Z jadvalidan farqli (aniq metallar).",
      parametrlar=dict(arch="stakan_tajriba")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260412)
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
    d = dict(n=n, tur="Y1", element="I.9", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I9-A", daraja="A", bob=9, bob_nomi="Oksidlanish-qaytarilish reaksiyalari",
    manba=("MS spetsifikatsiyasi I.9; darslik (8-9-sinf) OQR bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (olma, otashin, zang, batareyka) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq sonlar, rasmli hayotiy savollar, o'rgatuvchi "
          "chalg'ituvchilar. B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.9") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
