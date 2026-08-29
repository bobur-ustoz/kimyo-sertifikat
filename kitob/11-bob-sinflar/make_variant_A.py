# -*- coding: utf-8 -*-
"""11-bob A-varianti: Anorganik moddalar sinflari va genetik bog'lanish (II.1) — O'RGATUVCHI ★★.
Hayotiy sahnalar: antatsid tabletka, choynak qasqoni, devor oqlash, gazli ichimlik."""
import json, random

OUT = "mavzu_II1A.json"
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
  "Oksidlar deb qanday moddalarga aytiladi?",
  "biri kislorod bo'lgan IKKI elementdan tashkil topgan birikmalarga",
  [("tarkibida kislorod bo'lgan har qanday moddaga", "KOH da ham O bor, lekin u asos"),
   ("metall va kislota qoldig'idan iborat moddalarga", "bu tuzlar"),
   ("faqat metallarning birikmalariga", "CO₂ — metallmas oksidi ham bor")],
  "Oksid: EₓOᵧ — masalan, CaO, CO₂, Fe₂O₃.",
  dict(arch="oksid_tarif"))

# 2 (2)
q(2, "quyi",
  "Qaysi qatorda FAQAT kislotali oksidlar berilgan?",
  "CO₂, SO₂, P₂O₅",
  [("CaO, Na₂O, MgO", "bular asosli oksidlar"),
   ("CO₂, CaO, ZnO", "CaO — asosli, ZnO — amfoter"),
   ("CO, NO, N₂O", "bular befarq (tuz hosil qilmaydigan) oksidlar")],
  "Kislotali oksidlar suv bilan kislota beradi: CO₂ → H₂CO₃, SO₂ → H₂SO₃, P₂O₅ → H₃PO₄.",
  dict(arch="kislotali_qator"))

# 3 (2)
q(2, "quyi",
  "Qaysi formula ASOSGA tegishli?",
  "NaOH", [("HNO₃", "kislota (H bilan boshlanadi)"), ("Na₂SO₄", "tuz"),
            ("SO₃", "kislotali oksid")],
  "Asos: metall + gidroksid guruh(lar)i — NaOH, Ca(OH)₂.",
  dict(arch="asos_formula"))

# 4 (2) — SAHNA: antatsid
q(2, "o'rta",
  "Rasmda antatsid tabletka: me'dada kislota (HCl) ko'payib ketganda Mg(OH)₂ li tabletka ichiladi. "
  "Bunda qanday reaksiya boradi?",
  "neytrallanish: asos kislotani tuz va suvga aylantiradi",
  [("parchalanish: kislota parchalanadi", "kislota asos bilan BIRGA reaksiyaga kirishadi"),
   ("o'rin olish: magniy vodorodni siqib chiqaradi", "Mg(OH)₂ — asos, metall emas"),
   ("hech qanday reaksiya bormaydi", "aynan reaksiya tufayli og'riq qoladi")],
  "Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O — ortiqcha kislota neytrallanadi.",
  dict(arch="antacid_sahna"), fig="antacid")

# 5 (2)
q(2, "quyi",
  "Kislotalar tarkibi qanday qismlardan iborat?",
  "vodorod atomlari va kislota qoldig'idan",
  [("metall va gidroksid guruhidan", "bu asoslar tarkibi"),
   ("metall va kislota qoldig'idan", "bu tuzlar tarkibi"),
   ("faqat metallmaslardan", "tarkibda albatta H bo'ladi")],
  "HCl, H₂SO₄, H₃PO₄: almashinuvchi H + qoldiq.",
  dict(arch="kislota_tarkib"))

# 6 (2)
q(2, "quyi",
  "Tuzlar deb qanday moddalarga aytiladi?",
  "metall atomlari va kislota qoldig'idan iborat moddalarga",
  [("vodorod va kislota qoldig'idan iborat moddalarga", "bu kislotalar"),
   ("ikki metalldan iborat moddalarga", "bu qotishma, birikma emas"),
   ("metall va kisloroddan iborat moddalarga", "bu asosli oksidlar")],
  "NaCl, K₂SO₄, CaCO₃ — kislotadagi H o'rnini metall olgan.",
  dict(arch="tuz_tarif"))

# 7 (2)
q(2, "o'rta",
  "CO₂ + H₂O → H₂CO₃ reaksiyasida qanday sinflar qatnashadi va hosil bo'ladi?",
  "kislotali oksid + suv → kislota",
  [("asosli oksid + suv → asos", "CO₂ — kislotali oksid"),
   ("kislota + suv → oksid", "yo'nalish teskari"),
   ("tuz + suv → kislota", "CO₂ tuz emas")],
  "Kislotali oksidlar suv bilan tegishli kislotani beradi.",
  dict(arch="co2_suv"))

# 8 (2) — SAHNA: choynak qasqoni
q(2, "o'rta",
  "Rasmda qasqon bosgan choynak: uni sirka kislota eritmasi bilan tozalashadi. Qasqon (CaCO₃) "
  "bilan kislota reaksiyasida qanday belgi kuzatiladi?",
  "gaz pufakchalari (CO₂) ajraladi",
  [("eritma qizil rangga kiradi", "rang o'zgarishi bu reaksiyada kuzatilmaydi"),
   ("cho'kma tushadi", "aksincha — qattiq qasqon ERIB ketadi"),
   ("hech narsa kuzatilmaydi", "«vishillash» — CO₂ ajralishi")],
  "CaCO₃ + 2CH₃COOH → (CH₃COO)₂Ca + H₂O + CO₂↑ — karbonatlar kislotada «vishillaydi».",
  dict(arch="kettle_sahna"), fig="kettle")

# 9 (2)
q(2, "o'rta",
  "Qaysi asos ISHQOR hisoblanadi?",
  "KOH — suvda yaxshi eriydi",
  [("Cu(OH)₂ — ko'k cho'kma", "suvda erimaydi"),
   ("Fe(OH)₃ — qo'ng'ir cho'kma", "suvda erimaydi"),
   ("Al(OH)₃ — oq cho'kma", "erimaydi, ustiga amfoter")],
  "Ishqorlar — suvda eriydigan asoslar: NaOH, KOH, Ba(OH)₂...",
  dict(arch="ishqor_tanlov"))

# 10 (3)
check("q10", 5.6/56*74, 7.4)
q(3, "o'rta",
  "CaO + H₂O → Ca(OH)₂. 5,6 g kalsiy oksididan necha gramm asos olinadi? (M: CaO=56, Ca(OH)₂=74)",
  "7,4 g", [("5,6 g", "massa saqlanmaydi — suv qo'shildi"), ("74 g", "1 mol uchun qiymat"),
             ("14,8 g", "ikki baravar ko'p")],
  "n = 5,6/56 = 0,1 mol → m = 0,1·74 = 7,4 g.",
  dict(arch="cao_hisob"))

# 11 (2)
q(2, "o'rta",
  "Qaysi tuz NORDON tuz hisoblanadi?",
  "NaHCO₃", [("Na₂CO₃", "o'rta tuz — H qolmagan"), ("NaCl", "o'rta tuz"),
              ("(CuOH)₂CO₃", "asosli tuz — OH bor")],
  "Nordon tuzda kislota vodorodi qisman saqlangan: NaHCO₃ (gidrokarbonat).",
  dict(arch="nordon_misol"))

# 12 (3)
check("q12", 0.2*40, 8)
q(3, "o'rta",
  "0,2 mol xlorid kislotani to'liq neytrallash uchun necha gramm NaOH kerak? (M(NaOH)=40)",
  "8 g", [("40 g", "1 mol uchun qiymat"), ("4 g", "ikkiga bo'lib yuborilgan"),
           ("16 g", "ikki baravar ko'p")],
  "HCl + NaOH → NaCl + H₂O (1:1): n = 0,2 mol → m = 0,2·40 = 8 g.",
  dict(arch="neytrallanish_hisob"))

# 13 (2) — SAHNA: devor oqlash
q(2, "o'rta",
  "Rasmda devorni ohak suti bilan oqlash: bir necha kundan keyin qoplama qattiq va oq bo'lib qotadi. "
  "Buning sababi qanday reaksiya?",
  "Ca(OH)₂ havodagi CO₂ bilan CaCO₃ ga aylanadi",
  [("ohak shunchaki qurib qoladi", "qurish ham bor, lekin qotish — kimyoviy"),
   ("ohak kislorod bilan oksidlanadi", "reaksiya CO₂ bilan boradi"),
   ("ohak suv bilan birikadi", "aksincha, suv bug'lanib chiqadi")],
  "Ca(OH)₂ + CO₂ → CaCO₃ + H₂O: yumshoq ohak «toshga» aylanadi.",
  dict(arch="whitewash_sahna"), fig="whitewash")

# 14 (3)
q(3, "o'rta",
  "Genetik qatordagi X moddani aniqlang: Ca → CaO → X → CaCO₃.",
  "Ca(OH)₂", [("CaCl₂", "xlorid karbonatga bevosita o'tmaydi"),
               ("CaH₂", "gidrid bu qatorga kirmaydi"),
               ("Ca(NO₃)₂", "nitrat emas — oksiddan suv bilan olinadigan asos")],
  "CaO + H₂O → Ca(OH)₂; Ca(OH)₂ + CO₂ → CaCO₃: X — kalsiy gidroksid.",
  dict(arch="genetik_x"))

# 15 (2)
q(2, "o'rta",
  "Qaysi oksid AMFOTER (ham kislota, ham ishqor bilan reaksiyaga kirishadi)?",
  "ZnO", [("Na₂O", "faqat kislota bilan — asosli"), ("SO₃", "faqat ishqor bilan — kislotali"),
           ("CO", "hech biri bilan — befarq")],
  "ZnO + 2HCl → ZnCl₂ + H₂O va ZnO + 2NaOH → Na₂ZnO₂ + H₂O.",
  dict(arch="amfoter_misol"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni mos ravishda to'ldiring:\n"
  "[JADVAL] Modda | Sinf ;; CO₂ | ? ;; KOH | ? ;; ZnSO₄ | ?",
  "kislotali oksid; ishqor; o'rta tuz",
  [("asosli oksid; kislota; nordon tuz", "hammasi noto'g'ri joylashgan"),
   ("kislotali oksid; ishqor; nordon tuz", "ZnSO₄ da vodorod yo'q — o'rta tuz"),
   ("befarq oksid; asos; o'rta tuz", "CO₂ kislota (H₂CO₃) beradi — befarq emas")],
  "CO₂ — kislotali oksid; KOH — eriydigan asos (ishqor); ZnSO₄ — o'rta tuz.",
  dict(arch="sinf_jadval"))

# 17 (2)
q(2, "o'rta",
  "Asosli oksid kislota bilan reaksiyaga kirishganda nima hosil bo'ladi?",
  "tuz va suv", [("faqat tuz", "suv ham hosil bo'ladi"), ("asos va vodorod", "H₂ ajralmaydi"),
                  ("yangi kislota", "kislota sarflanadi")],
  "CaO + 2HCl → CaCl₂ + H₂O — sinflararo asosiy reaksiya.",
  dict(arch="oksid_kislota"))

# 18 (2) — SAHNA: gazli ichimlik
q(2, "o'rta",
  "Rasmda gazli ichimlik: unga bosim ostida CO₂ eritilgan. Tildagi yengil «achchiq-o'tkir» ta'm "
  "qaysi moddadan?",
  "hosil bo'lgan kuchsiz karbonat kislotadan (H₂CO₃)",
  [("erigan shakardan", "shakar shirin ta'm beradi"),
   ("sof CO₂ gazining o'zidan", "gaz suv bilan birikib KISLOTA beradi"),
   ("idish materialidan", "ta'm eritmadagi kislotadan")],
  "CO₂ + H₂O ⇄ H₂CO₃: shu kislota ichimlikka o'tkir ta'm beradi.",
  dict(arch="sodadrink_sahna"), fig="sodadrink")

# 19 (3)
check("q19", 4.8/24*40, 8)
q(3, "o'rta",
  "2Mg + O₂ → 2MgO. 4,8 g magniy yonganda necha gramm oksid hosil bo'ladi? (M: Mg=24, MgO=40)",
  "8 g", [("4,8 g", "kislorod massasi qo'shilmagan"), ("40 g", "1 mol uchun"),
           ("16 g", "ikki baravar ko'p")],
  "n = 0,2 mol → m(MgO) = 0,2·40 = 8 g.",
  dict(arch="mgo_hisob"))

# 20 (2)
q(2, "quyi",
  "H₂SO₄ kislotasi necha negizli?",
  "ikki negizli", [("bir negizli", "2 ta almashinuvchi H bor"), ("uch negizli", "H₃PO₄ uch negizli"),
                    ("to'rt negizli", "H₄P₂O₇ to'rt negizli")],
  "Negizlilik — almashinuvchi H soni: H₂SO₄ da 2 ta.",
  dict(arch="negizlilik"))

# 21 (3)
q(3, "o'rta",
  "H₂SO₄ natriy bilan ikki xil tuz beradi: Na₂SO₄ va NaHSO₄. Qaysi biri nordon tuz va nima uchun?",
  "NaHSO₄ — tarkibida almashinmagan vodorod qolgan",
  [("Na₂SO₄ — natriy ko'p", "metall ko'pligi nordonlik belgisi emas"),
   ("ikkalasi ham nordon", "Na₂SO₄ da H yo'q — o'rta"),
   ("ikkalasi ham o'rta", "NaHSO₄ da H saqlangan — nordon")],
  "Nordon tuz = H qisman almashgan: NaHSO₄ (natriy gidrosulfat).",
  dict(arch="nordon_orta_farq"))

# 22 (2)
q(2, "o'rta",
  "Qaysi oksid suvda erib ISHQOR hosil qiladi?",
  "Na₂O", [("CuO", "suv bilan reaksiyaga kirishmaydi"), ("SO₂", "kislota beradi"),
            ("ZnO", "suvda erimaydi (amfoter)")],
  "Na₂O + H₂O → 2NaOH: faol metall oksidlari ishqor beradi.",
  dict(arch="oksid_suv_ishqor"))

# 23 (3)
check("q23", 6.5/65*22.4, 2.24)
q(3, "o'rta",
  "Zn + 2HCl → ZnCl₂ + H₂. 6,5 g rux kislotada to'liq eriganda ajralgan vodorod hajmini (n.sh.) toping. "
  "(M(Zn)=65)",
  "2,24 L", [("22,4 L", "1 mol uchun qiymat"), ("1,12 L", "ikkiga bo'lingan"),
              ("4,48 L", "ikki baravar ko'p")],
  "n(Zn) = 0,1 mol → n(H₂) = 0,1 mol → V = 2,24 L.",
  dict(arch="zn_hcl_hisob"))

# 24 (2)
q(2, "o'rta",
  "Qaysi oksid suv bilan reaksiyaga KIRISHMAYDI?",
  "CuO", [("K₂O", "ishqor beradi"), ("SO₃", "sulfat kislota beradi"), ("BaO", "ishqor beradi")],
  "Faol bo'lmagan metallarning oksidlari (CuO, FeO...) suv bilan birikmaydi.",
  dict(arch="suv_bilan_emas"))

# 25 (3)
q(3, "o'rta",
  "Genetik qatordagi X moddani aniqlang: S → SO₂ → X → H₂SO₄.",
  "SO₃", [("H₂SO₃", "sulfit kislotadan sulfat kislota bevosita olinmaydi"),
           ("Na₂SO₃", "tuz bu zanjirga kirmaydi"), ("H₂S", "qaytarilish — teskari yo'nalish")],
  "SO₂ oksidlanib SO₃ ga, SO₃ + H₂O → H₂SO₄.",
  dict(arch="genetik_s"))

# 26 (3) — RASMLI: o'g'itlar diagrammasi
q(3, "o'rta",
  "Diagrammada azotli o'g'itlardagi azot ulushi (%) berilgan. Qaysi o'g'it azotga eng boy?",
  "NH₄NO₃ (35 %)", [("(NH₄)₂SO₄ (21 %)", "o'rtacha ustun"), ("KNO₃ (14 %)", "eng past ustun"),
                     ("hammasi teng", "ustunlar farqli")],
  "Diagrammadan: ammiakli selitra NH₄NO₃ — 35 % azot bilan yetakchi.",
  dict(arch="bar_ogit_oqish"), fig="bar_ogit")

# 27 (3)
check("q27", 0.1*98, 9.8)
q(3, "o'rta",
  "CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄. 0,1 mol mis(II) sulfatdan necha gramm ko'k cho'kma olinadi? "
  "(M(Cu(OH)₂)=98)",
  "9,8 g", [("98 g", "1 mol uchun"), ("4,9 g", "ikkiga bo'lingan"), ("19,6 g", "ikki baravar")],
  "n(Cu(OH)₂) = 0,1 mol → m = 9,8 g.",
  dict(arch="cuoh2_hisob"))

# 28 (2)
q(2, "o'rta",
  "Asoslarning suvda erishi haqida qaysi fikr to'g'ri?",
  "ko'pchiligi erimaydi; eriydiganlari ishqor deyiladi",
  [("barcha asoslar suvda eriydi", "Cu(OH)₂, Fe(OH)₃ erimaydi"),
   ("hech biri erimaydi", "NaOH, KOH yaxshi eriydi"),
   ("faqat og'ir metallarniki eriydi", "aksincha — ishqoriy metallarniki eriydi")],
  "Eruvchanlik jadvalining «asos» ustuni asosan «E» (erimaydi) belgili.",
  dict(arch="asos_eruvchanlik"))

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Ohaktosh bo'lagiga xlorid kislota tomchilab qo'shilmoqda. Ajralgan CO₂ hajmi qo'shilgan kislota "
  "miqdoriga qanday bog'liq? Grafikni tanlang.",
  "ortib boradi, ohaktosh tugagach o'zgarmaydi",
  [("chegarasiz ortib boradi", "CaCO₃ tugagach gaz ajralishi to'xtaydi"),
   ("o'zgarmaydi", "kislota qo'shilgani sari gaz ortadi"),
   ("avval ortadi, keyin kamayadi", "ajralgan gaz kamaymaydi")],
  "CaCO₃ cheklangan: u tugaguncha V(CO₂) chiziqli ortadi, so'ng plato.",
  svg=dict(correct="rise_flat", d1="rise", d2="flat", d3="rise_fall", xlab="n(HCl)", ylab="V(CO₂)"),
  params=dict(arch="co2_grafik"))

# 30 (2)
q(2, "o'rta",
  "Quyidagi juftliklardan qaysi biri o'zaro reaksiyaga KIRISHADI?",
  "CO₂ va NaOH",
  [("CO₂ va SO₃", "ikkalasi kislotali — o'zaro birikmaydi"),
   ("NaCl va KNO₃", "eritmada almashinish belgisi yo'q"),
   ("CaO va Na₂O", "ikkalasi asosli oksid")],
  "Kislotali oksid + ishqor → tuz + suv: CO₂ + 2NaOH → Na₂CO₃ + H₂O.",
  dict(arch="juft_reaksiya"))

# 31 (3)
check("q31", 16/160*2*56, 11.2)
q(3, "o'rta",
  "Fe₂O₃ + 3H₂ → 2Fe + 3H₂O. 16 g temir(III) oksididan necha gramm temir olinadi? "
  "(M: Fe₂O₃=160, Fe=56)",
  "11,2 g", [("16 g", "kislorod chiqib ketadi — massa kamayadi"), ("5,6 g", "koeffitsiyent 2 unutilgan"),
              ("56 g", "1 mol Fe massasi")],
  "n(Fe₂O₃) = 0,1 mol → n(Fe) = 0,2 mol → m = 11,2 g.",
  dict(arch="fe2o3_hisob"))

# 32 (3) — RASMLI: o'g'it hisobi
check("q32", 200*0.35, 70)
q(3, "o'rta",
  "26-savol diagrammasidan foydalaning: 200 kg ammiakli selitra (NH₄NO₃) tarkibida necha kg azot bor?",
  "70 kg", [("35 kg", "100 kg uchun qiymat"), ("140 kg", "ikki baravar ko'p"),
             ("200 kg", "o'g'itning hammasi azot emas")],
  "m(N) = 200 · 0,35 = 70 kg.",
  dict(arch="bar_ogit_hisob"), fig="bar_ogit")

# ---------- Y2: uy kimyosi ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.1",
  ichki_pasport=[dict(n=33, element="II.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="II.1", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="II.1", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uyda uch modda bor: X — osh sodasi (NaHCO₃), Y — o'chirilgan ohak (Ca(OH)₂), "
               "Z — sirka kislota eritmasi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X modda qaysi sinfga kiradi?",
    "34. Y havodagi CO₂ bilan reaksiyada nima beradi?",
    "35. Z bilan X aralashtirilganda qaysi gaz ajraladi?"],
  javoblar_royxati=["A) nordon tuz", "B) CaCO₃", "C) CO₂", "D) o'rta tuz", "E) CaO", "F) H₂"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="NaHCO₃ da vodorod saqlangan — nordon tuz"),
                   dict(variant="E", xato="Ca(OH)₂ + CO₂ → karbonat, oksid emas"),
                   dict(variant="F", xato="kislota + karbonat CO₂ beradi, vodorod emas")],
  yechim=("X: NaHCO₃ — nordon tuz (A). Y: Ca(OH)₂ + CO₂ → CaCO₃ + H₂O (B). "
          "Z + X: CH₃COOH + NaHCO₃ → tuz + H₂O + CO₂↑ (C)."),
  parametrlar=dict(arch="uy_kimyo_ssenariy"))

# ---------- O1 ----------
check("o36", 8/40, 0.2)
check("o37", 11.2/56*74, 14.8)
check("o38", 0.1*2*98, 19.6)
check("o39", 5.6/56*88, 8.8)
check("o40", 4.9/98*2*40, 4)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="8 g natriy gidroksid necha mol bo'ladi? (M(NaOH)=40)",
      javob="0,2", yechim="n = 8/40 = 0,2 mol.",
      parametrlar=dict(arch="naoh_mol_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="11,2 g CaO suv bilan to'liq reaksiyaga kirishdi. Hosil bo'lgan Ca(OH)₂ massasini (g) toping.",
      javob="14,8", yechim="n = 11,2/56 = 0,2 mol → m = 0,2·74 = 14,8 g.",
      parametrlar=dict(arch="cao_suv_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="P₂O₅ + 3H₂O → 2H₃PO₄. 0,1 mol fosfor(V) oksididan olingan kislota massasini (g) toping. "
            "(M(H₃PO₄)=98)",
      javob="19,6", yechim="n(H₃PO₄) = 0,2 mol → m = 19,6 g.",
      parametrlar=dict(arch="p2o5_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Fe + S → FeS. 5,6 g temirdan olingan temir(II) sulfid massasini (g) toping. (M: Fe=56, FeS=88)",
      javob="8,8", yechim="n = 0,1 mol → m = 0,1·88 = 8,8 g.",
      parametrlar=dict(arch="fes_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="4,9 g sulfat kislotani to'liq neytrallash uchun necha gramm NaOH kerak? (M(H₂SO₄)=98)",
      javob="4", yechim="n = 0,05 mol → NaOH: 0,1 mol → m = 4 g.",
      parametrlar=dict(arch="h2so4_neytral_o1")),
]

# ---------- O2 ----------
check("o41", 20/40*56, 28)
O2 = [
 dict(n=41, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Kalsiyning genetik qatori beriladi: Ca → CaO → Ca(OH)₂ → CaCO₃. Bandlar ketma-ket "
            "yechiladi — har biri keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) Har bir o'tish uchun reaksiya tenglamasini yozing.",
             yechim=["2Ca + O₂ → 2CaO; CaO + H₂O → Ca(OH)₂; Ca(OH)₂ + CO₂ → CaCO₃ + H₂O."], M=5, A=2),
        dict(savol="b) Har bir moddaning sinfini ayting.",
             yechim=["Ca — oddiy modda (metall); CaO — asosli oksid; Ca(OH)₂ — asos; CaCO₃ — o'rta tuz."], M=3, A=2),
        dict(savol="c) 20 g kalsiydan (yo'qotishsiz) olinadigan CaO massasini hisoblang.",
             yechim=["n = 0,5 mol → m(CaO) = 0,5·56 = 28 g."], M=4, A=3),
        dict(savol="d) Zanjirni teskari yo'nalishda (CaCO₃ dan Ca(OH)₂ ga) qanday qaytish mumkin? Izohlang.",
             yechim=["CaCO₃ qizdirilib CaO olinadi (parchalanish), so'ng suv bilan Ca(OH)₂."], M=3, A=3),
      ],
      rasmiylashtirish="Genetik zanjir: tenglamalar → sinflar → hisob → teskari yo'l; M15+A10.",
      parametrlar=dict(arch="ca_genetik_zanjir")),
 dict(n=42, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Qurilishda ohak bilan ishlashda ikki hodisa kuzatiladi: (1) oqlangan devor asta-sekin "
            "qotib, oq va mustahkam bo'ladi; (2) xona havosini tekshirish uchun ohakli suv qo'yilsa, "
            "u loyqalanadi. Quyidagilarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Ikkala hodisaning kimyoviy mohiyatini tenglamalar bilan tushuntiring.",
             yechim=["Ikkalasi ham bitta reaksiya: Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O.",
                     "Devorda CaCO₃ qattiq qatlam beradi, eritmada — loyqa (cho'kma)."], M=13, A=0),
        dict(savol="b) Nega ohakli suv idishi ochiq qoldirilsa, yuzasida qattiq parda paydo bo'ladi?",
             yechim=["Havo CO₂ si yuzadagi Ca(OH)₂ bilan reaksiyaga kirishib CaCO₃ pardasini hosil qiladi."], M=9, A=0),
        dict(savol="c) Bu reaksiyada qatnashuvchi moddalarning sinflarini ayting.",
             yechim=["Asos + kislotali oksid → tuz + suv."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="ohak_mulohaza")),
 dict(n=43, tur="O2", element="II.1", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Beshta modda jadvalda berilgan:\n"
            "[JADVAL] № | Modda ;; 1 | K₂O ;; 2 | HNO₃ ;; 3 | Ba(OH)₂ ;; 4 | KHSO₄ ;; 5 | SO₂\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir moddaning sinfini (turini) aniqlang.",
             yechim=["K₂O — asosli oksid; HNO₃ — kislota; Ba(OH)₂ — asos (ishqor); "
                     "KHSO₄ — nordon tuz; SO₂ — kislotali oksid."], M=5, A=3),
        dict(savol="b) Qaysi juftliklar o'zaro reaksiyaga kirisha oladi? Ikkita misol tenglamasini yozing.",
             yechim=["K₂O + 2HNO₃ → 2KNO₃ + H₂O; Ba(OH)₂ + SO₂ → BaSO₃ + H₂O."], M=4, A=3),
        dict(savol="c) 1-modda suv bilan reaksiyasining tenglamasini yozing va mahsulot sinfini ayting.",
             yechim=["K₂O + H₂O → 2KOH — ishqor."], M=3, A=2),
        dict(savol="d) 4-moddadan o'rta tuz olish yo'lini ko'rsating.",
             yechim=["KHSO₄ + KOH → K₂SO₄ + H₂O — ishqor bilan to'liq neytrallash."], M=3, A=2),
      ],
      rasmiylashtirish="Sinflash-jadval tahlili: M15+A10.",
      parametrlar=dict(arch="sinf_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261103)
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
    variant="mavzu-II1-A", daraja="A", bob=11, bob_nomi="Anorganik moddalar sinflari va genetik bog'lanish",
    manba=("MS spetsifikatsiyasi II.1; darslik anorganik sinflar bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (antatsid, choynak qasqoni, devor oqlash, gazli ichimlik) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.1") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
