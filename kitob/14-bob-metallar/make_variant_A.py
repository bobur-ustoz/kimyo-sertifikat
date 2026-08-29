# -*- coding: utf-8 -*-
"""14-bob A-varianti: IIA, IIIA va d-metallar. Suv qattiqligi (II.4) — O'RGATUVCHI ★★.
Hayotiy sahnalar: kislotali yomg'ir va haykal, samolyot (Al), tibbiy gips, kir mashina TENi."""
import json, random

OUT = "mavzu_II4A.json"
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
  "IIA guruh metallari atomlarining tashqi qavatida nechta elektron bor?",
  "2", [("1", "bu IA guruh"), ("3", "bu IIIA guruh"), ("8", "bu inert gazlar")],
  "ns² — ikkita valent elektron → +2 zaryadli ionlar (Ca²⁺, Mg²⁺).",
  dict(arch="iia_tashqi_e"))

# 2 (2)
q(2, "quyi",
  "Alanga testida kalsiy qanday rang beradi?",
  "g'isht-qizil", [("sariq", "sariq — natriy"), ("binafsha", "binafsha — kaliy"),
                    ("ko'k", "IA/IIA da ko'k alanga yo'q")],
  "Ca — g'isht-qizil; Sr — qirmizi; Ba — yashil.",
  dict(arch="ca_alanga"))

# 3 (2)
q(2, "o'rta",
  "Magniy lentasi yondirilganda nima kuzatiladi?",
  "ko'zni qamashtiruvchi yorqin oq alanga",
  [("ko'k tutun", "alanga oq-yorqin"), ("qizil uchqunlar", "qizil — Li, Sr ranglari"),
   ("rangsiz sekin yonish", "juda yorqin — fotosuratlarda ishlatilgan")],
  "2Mg + O₂ → 2MgO: yorqinligi tufayli eski fotoapparat «chaqnashlarida» ishlatilgan.",
  dict(arch="mg_yonish"))

# 4 (2) — SAHNA: haykal va kislotali yomg'ir
q(2, "o'rta",
  "Rasmda eski marmar haykal: qirralari yemirilib silliqlashgan. Bunga sabab — kislotali "
  "yomg'irlar. Qanday reaksiya boradi?",
  "marmar (CaCO₃) kislotalar bilan reaksiyaga kirishib asta eriydi",
  [("marmar suvda oddiy eriydi", "toza suvda CaCO₃ deyarli erimaydi"),
   ("shamol yedirib yuboradi", "shamol ta'siri bor, lekin asosiysi — kimyoviy yemirilish"),
   ("marmar quyoshda parchalanadi", "yorug'lik CaCO₃ ni buzmaydi")],
  "CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂: havoga chiqqan SO₂/NO₂ yomg'irni kislotali qiladi.",
  dict(arch="haykal_sahna"), fig="statue")

# 5 (2)
q(2, "o'rta",
  "Alyuminiy davriy jadvalning qaysi guruhida joylashgan va birikmalarida qanday oksidlanish "
  "darajasini namoyon qiladi?",
  "IIIA; +3", [("IIA; +2", "u IIIA da"), ("IA; +1", "bu ishqoriy metallar"),
                ("IIIA; −3", "metall manfiy daraja olmaydi")],
  "Al: 3s²3p¹ — uchala elektronini berib Al³⁺ bo'ladi.",
  dict(arch="al_guruh"))

# 6 (2)
q(2, "quyi",
  "Suvning QATTIQLIGI qaysi ionlar tufayli yuzaga keladi?",
  "Ca²⁺ va Mg²⁺", [("Na⁺ va K⁺", "ular qattiqlik bermaydi"), ("H⁺ va OH⁻", "bular muhit ionlari"),
                    ("Fe³⁺ va Cu²⁺", "og'ir metallar — ifloslanish, qattiqlik emas")],
  "Qattiq suv — tarkibida ko'p Ca²⁺/Mg²⁺ tuzlari bo'lgan suv.",
  dict(arch="qattiqlik_tarif"))

# 7 (2)
q(2, "o'rta",
  "VAQTINCHALIK qattiqlik qanday yo'qotiladi?",
  "qaynatish bilan", [("muzlatish bilan", "muzlatish tuzlarni cho'ktirmaydi"),
                       ("filtrlash bilan", "erigan tuzlar filtrdan o'tadi"),
                       ("tindirish bilan", "erigan holda cho'kmaydi")],
  "Ca(HCO₃)₂ → (qaynatishda) CaCO₃↓ + H₂O + CO₂ — «qasqon» shu.",
  dict(arch="vaqtinchalik"))

# 8 (2) — SAHNA: samolyot
q(2, "o'rta",
  "Rasmda samolyot: korpusining asosiy qismi alyuminiy qotishmalaridan. Nega aynan alyuminiy?",
  "yengil, yetarlicha pishiq va korroziyaga chidamli",
  [("eng qattiq metall bo'lgani uchun", "qattiqlikda Cr, W ustun"),
   ("eng arzon metall bo'lgani uchun", "temir arzonroq — gap yengillikda"),
   ("magnitlanmagani uchun", "asosiy sabab — zichligi (2,7 g/sm³)")],
  "Zichlik temirdan ~3 barobar kichik; yuzadagi Al₂O₃ parda zangdan saqlaydi.",
  dict(arch="samolyot_sahna"), fig="plane")

# 9 (2)
q(2, "o'rta",
  "Temir buyumlardagi ZANG asosan qaysi birikmadan iborat?",
  "temir(III) oksid-gidroksidlaridan",
  [("sof temirdan", "zang — birikma"), ("temir sulfiddan", "S havoda yetarli emas"),
   ("temir karbiddan", "karbid cho'yanda bo'ladi")],
  "Nam havoda: Fe → Fe(OH)₃/Fe₂O₃·nH₂O — g'ovak qo'ng'ir qatlam.",
  dict(arch="zang_tarkib"))

# 10 (3)
check("q10", 4/40*56, 5.6)
q(3, "o'rta",
  "2Ca + O₂ → 2CaO. 4 g kalsiy yonganda necha gramm oksid hosil bo'ladi? (M: Ca=40, CaO=56)",
  "5,6 g", [("4 g", "kislorod massasi qo'shiladi"), ("56 g", "1 mol uchun"), ("11,2 g", "ikki baravar")],
  "n = 0,1 mol → m(CaO) = 5,6 g.",
  dict(arch="cao_yonish_hisob"))

# 11 (2)
q(2, "o'rta",
  "Alyuminiy faol metall bo'lsa-da, undan idishlar yasaladi. Buning sababi nimada?",
  "yuzasi zich Al₂O₃ pardasi bilan qoplanib himoyalanadi",
  [("alyuminiy aslida passiv", "u faol — parda himoya qiladi"),
   ("idishlar maxsus bo'yaladi", "parda tabiiy hosil bo'ladi"),
   ("suv bilan reaksiyaga kirisha olmaydi", "parda olib tashlansa kirisha oladi")],
  "Zich oksid parda metallni havo va suvdan to'sadi — «o'z-o'zini himoya».",
  dict(arch="al_parda"))

# 12 (3)
check("q12", 2.4/24*22.4, 2.24)
q(3, "o'rta",
  "Mg + 2HCl → MgCl₂ + H₂. 2,4 g magniy kislotada eriganda ajralgan vodorod hajmini (n.sh.) toping. "
  "(M(Mg)=24)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("4,48 L", "ikki baravar"), ("1,12 L", "yarmi")],
  "n(Mg) = 0,1 mol → n(H₂) = 0,1 → V = 2,24 L.",
  dict(arch="mg_hcl_hisob"))

# 13 (2) — SAHNA: tibbiy gips
q(2, "o'rta",
  "Rasmda singan qo'lga gips bog'lanmoqda. Tibbiy gipsning asosi qaysi modda?",
  "kalsiy sulfat (CaSO₄ asosidagi gips)",
  [("kalsiy karbonat (bo'r)", "bo'r suv bilan qotmaydi"),
   ("ohak (CaO)", "CaO suv bilan qizib ketadi — kuydiradi!"),
   ("osh tuzi", "NaCl qotib qolmaydi")],
  "Kuydirilgan gips suv bilan qorilganda CaSO₄·2H₂O holida tez qotadi — shakl beradi.",
  dict(arch="gips_sahna"), fig="gips")

# 14 (3)
q(3, "o'rta",
  "FeCl₂ va FeCl₃ birikmalarida temirning oksidlanish darajalari mos ravishda qanday?",
  "+2 va +3", [("+3 va +2", "teskari"), ("+1 va +2", "temirda +1 bo'lmaydi"),
                ("+2 va +2", "xlorlar soni farq qiladi-ku")],
  "Temir o'zgaruvchan valentli: FeCl₂ — temir(II), FeCl₃ — temir(III).",
  dict(arch="fe_valentlik"))

# 15 (2)
q(2, "o'rta",
  "Ohaktosh, marmar va bo'r — bularning barchasi qaysi bitta moddaning turlari?",
  "CaCO₃", [("CaSO₄", "bu gips asosi"), ("CaO", "bu so'ndirilmagan ohak"), ("Ca(OH)₂", "bu so'ndirilgan ohak")],
  "Uchalasi ham kalsiy karbonatning tabiiy shakllari.",
  dict(arch="caco3_shakllar"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Metall | Alanga rangi ;; Ca | ? ;; Ba | ?",
  "g'isht-qizil; yashil",
  [("yashil; g'isht-qizil", "teskari"), ("sariq; binafsha", "bular Na va K"),
   ("oq; qizil", "oq «rang» alanga testi emas")],
  "Ca — g'isht-qizil, Ba — sarg'ish-yashil.",
  dict(arch="alanga_iia_jadval"))

# 17 (2)
q(2, "o'rta",
  "Magniy oksidi (MgO) qanday xossasi uchun o'tga chidamli g'ishtlarda ishlatiladi?",
  "juda yuqori haroratda ham suyuqlanmaydi (t ≈ 2800 °C)",
  [("juda yengil bo'lgani uchun", "asosiysi — olovbardoshlik"),
   ("yonuvchan bo'lgani uchun", "oksid yonmaydi"),
   ("elektr o'tkazgani uchun", "MgO izolyator")],
  "MgO — olovbardosh material: pech va metallurgiya qurilmalari uchun.",
  dict(arch="mgo_olovbardosh"))

# 18 (2) — SAHNA: kir mashina TENi
q(2, "o'rta",
  "Rasmda kir mashinaning qizdirish elementi (TEN): oq-kulrang qattiq qatlam bilan qoplangan. "
  "Bu qatlam qayerdan paydo bo'ladi?",
  "qattiq suvdagi kalsiy-magniy tuzlari qizdirishda cho'kadi",
  [("kir yuvish kukunidan", "kukun eriydi va yuviladi"),
   ("metallning o'zi oqaradi", "metall rangini o'zgartirmaydi"),
   ("kiyimlardagi changdan", "chang bunday qattiq qatlam bermaydi")],
  "Qaynatishda Ca(HCO₃)₂ → CaCO₃↓: TENda «toshqatlam» o'sib, uni kuydiradi.",
  dict(arch="ten_sahna"), fig="washer")

# 19 (3)
check("q19", 50/100*56, 28)
q(3, "o'rta",
  "CaCO₃ → CaO + CO₂. 50 g ohaktosh to'liq kuydirilganda necha gramm so'ndirilmagan ohak olinadi? "
  "(M: CaCO₃=100, CaO=56)",
  "28 g", [("50 g", "CO₂ chiqib ketadi — massa kamayadi"), ("56 g", "1 mol uchun"), ("14 g", "yarmi")],
  "n = 0,5 mol → m(CaO) = 0,5·56 = 28 g.",
  dict(arch="ohak_kuydirish"))

# 20 (2)
q(2, "o'rta",
  "Fe, Cu, Zn, Cr metallari davriy jadvalning qaysi qismida joylashgan?",
  "yon guruhchalarda (B guruhlar, d-elementlar)",
  [("asosiy guruhchalarda", "ular d-blokda"), ("VIII A guruhda", "u inert gazlar guruhi"),
   ("lantanoidlar qatorida", "ular 4-davr d-metallari")],
  "d-metallar — o'zgaruvchan valentlik va rangli birikmalar bilan ajralib turadi.",
  dict(arch="d_metallar_orni"))

# 21 (3)
check("q21", 2.7/27*1.5*22.4, 3.36)
q(3, "o'rta",
  "2Al + 6HCl → 2AlCl₃ + 3H₂. 2,7 g alyuminiy kislotada eriganda ajralgan vodorod hajmini (n.sh.) "
  "toping. (M(Al)=27)",
  "3,36 L", [("2,24 L", "koeffitsiyent 3/2 unutilgan"), ("6,72 L", "ikki baravar"),
              ("1,12 L", "hisob xato")],
  "n(Al) = 0,1 → n(H₂) = 0,15 mol → V = 3,36 L.",
  dict(arch="al_hcl_hisob"))

# 22 (2)
q(2, "o'rta",
  "Bronza qaysi metallarning qotishmasi?",
  "mis va qalay", [("temir va uglerod", "bu po'lat/cho'yan"), ("mis va rux", "bu latun"),
                    ("alyuminiy va magniy", "bu dural tarkibiga yaqin")],
  "Cu + Sn — insoniyatning eng qadimiy qotishmalaridan biri.",
  dict(arch="bronza"))

# 23 (3)
q(3, "o'rta",
  "DOIMIY qattiqlikni (CaSO₄, CaCl₂) yo'qotish uchun suvga qaysi modda qo'shiladi?",
  "soda (Na₂CO₃)", [("osh tuzi", "NaCl cho'kma bermaydi"), ("kislota", "kislota qattiqlikni oshiradi"),
                     ("shakar", "kimyoviy ta'sir yo'q")],
  "Ca²⁺ + CO₃²⁻ → CaCO₃↓ — kation cho'kmaga o'tadi, suv yumshaydi.",
  dict(arch="doimiy_yumshatish"))

# 24 (2)
q(2, "quyi",
  "Quyidagi metallardan qaysi biri MAGNITGA tortiladi?",
  "temir", [("alyuminiy", "magnitlanmaydi"), ("mis", "magnitlanmaydi"), ("rux", "magnitlanmaydi")],
  "Fe (va Ni, Co) — ferromagnit metallar.",
  dict(arch="magnit"))

# 25 (3)
q(3, "o'rta",
  "Genetik qatordagi oxirgi o'tish uchun reagentni tanlang: CaCO₃ → Ca(HCO₃)₂.",
  "CO₂ va suv (birgalikda)",
  [("faqat suv", "CaCO₃ suvda erimaydi"), ("HCl", "u CaCl₂ beradi"),
   ("NaOH", "ishqor karbonatni nordon tuzga o'tkazmaydi")],
  "CaCO₃ + CO₂ + H₂O → Ca(HCO₃)₂ — g'orlardagi stalaktitlar «kimyosi».",
  dict(arch="gidrokarbonat_otish"))

# 26 (3) — RASMLI: suv qattiqligi ustunlari
q(3, "o'rta",
  "Diagrammada uch xil suvning qattiqligi berilgan. Qaysi suv ENG QATTIQ?",
  "quduq suvi", [("daryo suvi", "3 mg-ekv/L — o'rtacha"), ("distillangan suv", "deyarli 0"),
                  ("hammasi teng", "ustunlar keskin farq qiladi")],
  "Diagrammadan: quduq suvi ≈ 9 mg-ekv/L — yer osti suvlari ohaktosh qatlamlardan o'tadi.",
  dict(arch="bar_qattiqlik_oqish"), fig="bar_hardness")

# 27 (3)
check("q27", 10.2/102*2*27, 5.4)
q(3, "o'rta",
  "10,2 g alyuminiy oksidi tarkibidagi alyuminiy massasini toping. (M: Al₂O₃=102, Al=27)",
  "5,4 g", [("2,7 g", "molekulada 2 ta Al bor"), ("10,2 g", "kislorod ham bor-ku"),
             ("4,8 g", "bu kislorod massasi")],
  "n = 0,1 mol → n(Al) = 0,2 → m = 5,4 g.",
  dict(arch="al2o3_tarkib"))

# 28 (2) — RASMLI: diagramma o'qish
q(2, "o'rta",
  "26-savol diagrammasidan: distillangan suvning qattiqligi qanday va nima uchun?",
  "deyarli nol — bug'latib olinganda tuzlar qolib ketadi",
  [("eng yuqori — toza suv qattiq bo'ladi", "qattiqlik tuzlardan, tozalikdan emas"),
   ("daryo suviga teng", "diagrammada deyarli 0 ko'rsatilgan"),
   ("aniqlab bo'lmaydi", "diagramma aniq ko'rsatadi")],
  "Distillangan suv — bug'dan kondensatlangan: Ca²⁺/Mg²⁺ yo'q.",
  dict(arch="bar_qattiqlik_dist"), fig="bar_hardness")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Vaqtinchalik qattiq suv uzoq qaynatilmoqda. Suvdagi Ca(HCO₃)₂ miqdori vaqt bo'yicha qanday "
  "o'zgaradi? Grafikni tanlang.",
  "kamayib, nolga yaqin sathda to'xtaydi",
  [("o'zgarmaydi", "gidrokarbonat parchalanib cho'kadi"),
   ("ortadi", "suv bug'lansa ham tuz CHO'KADI, ko'paymaydi"),
   ("avval ortib keyin kamayadi", "boshidanoq kamayadi")],
  "Ca(HCO₃)₂ → CaCO₃↓ + H₂O + CO₂: erigan tuz cho'kmaga o'tib tugaydi.",
  svg=dict(correct="fall_flat", d1="flat", d2="rise", d3="rise_fall", xlab="t", ylab="C"),
  params=dict(arch="qattiqlik_grafik"))

# 30 (2)
q(2, "o'rta",
  "Mis(II) tuzlari eritmalari odatda qanday rangda bo'ladi?",
  "ko'k (havorang)", [("yashil to'q", "yashil — Fe²⁺ ga yaqin, Cu²⁺ ko'k"),
                       ("qizil", "qizil eritma Cu²⁺ ga xos emas"), ("rangsiz", "d-metall ionlari ko'pincha rangli")],
  "CuSO₄ eritmasi — tiniq ko'k; suvsiz CuSO₄ esa oq.",
  dict(arch="cu_rang"))

# 31 (3)
check("q31", 0.2*100, 20)
q(3, "o'rta",
  "Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O. 0,2 mol so'ndirilgan ohak to'liq reaksiyaga kirishganda hosil "
  "bo'lgan cho'kma massasini toping. (M(CaCO₃)=100)",
  "20 g", [("100 g", "1 mol uchun"), ("10 g", "yarmi"), ("40 g", "ikki baravar")],
  "n = 0,2 mol → m = 20 g.",
  dict(arch="ohakli_suv_hisob"))

# 32 (3) — RASMLI: diagramma hisob
check("q32", 9-3, 6)
q(3, "o'rta",
  "26-savol diagrammasidan: quduq va daryo suvlari qattiqligi orasidagi farqni toping.",
  "6 mg-ekv/L", [("12 mg-ekv/L", "yig'indi olingan"), ("3 mg-ekv/L", "bu daryo suviniki"),
                  ("9 mg-ekv/L", "bu quduq suviniki")],
  "9 − 3 = 6 mg-ekv/L.",
  dict(arch="bar_qattiqlik_farq"), fig="bar_hardness")

# ---------- Y2: qurilish materiallari ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.4",
  ichki_pasport=[dict(n=33, element="II.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="II.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="II.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Qurilish omborida uch material bor: X — ohaktosh kukuni, Y — so'ndirilmagan ohak, "
               "Z — tibbiy gips. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Y ga suv quyilganda nima kuzatiladi?",
    "34. X ga xlorid kislota tomizilsa qaysi gaz ajraladi?",
    "35. Z materialning asosi qaysi modda?"],
  javoblar_royxati=["A) qizib, «qaynab» so'nadi", "B) CO₂", "C) CaSO₄", "D) sovib qoladi",
                    "E) H₂", "F) CaCO₃"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="CaO + H₂O — kuchli EKZOtermik: qiziydi"),
                   dict(variant="E", xato="karbonat + kislota CO₂ beradi, vodorod emas"),
                   dict(variant="F", xato="CaCO₃ — X (ohaktosh); gips esa sulfat")],
  yechim=("Y: CaO + H₂O → Ca(OH)₂ + Q — «so'nish» (A). X: CaCO₃ + HCl → ... + CO₂↑ (B). "
          "Z: gips — CaSO₄ asosida (C)."),
  parametrlar=dict(arch="qurilish_ssenariy"))

# ---------- O1 ----------
check("o36", 0.2*56, 11.2)
check("o37", 2.4/24, 0.1)
check("o38", 20.4/102, 0.2)
check("o39", 2/40*22.4, 1.12)
check("o40", 15/100*22.4, 3.36)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,2 mol kalsiy oksidning massasini (g) toping. (M(CaO)=56)",
      javob="11,2", yechim="m = 0,2·56 = 11,2 g.",
      parametrlar=dict(arch="cao_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="2,4 g magniy necha mol bo'ladi? (M(Mg)=24)",
      javob="0,1", yechim="n = 2,4/24 = 0,1 mol.",
      parametrlar=dict(arch="mg_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="20,4 g alyuminiy oksidi necha mol bo'ladi? (M(Al₂O₃)=102)",
      javob="0,2", yechim="n = 20,4/102 = 0,2 mol.",
      parametrlar=dict(arch="al2o3_mol_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Ca + 2H₂O → Ca(OH)₂ + H₂. 2 g kalsiy suv bilan reaksiyaga kirishganda ajralgan vodorod "
            "hajmini (n.sh., L) toping. (M(Ca)=40)",
      javob="1,12", yechim="n = 0,05 mol → V(H₂) = 1,12 L.",
      parametrlar=dict(arch="ca_suv_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="15 g ohaktosh to'liq kuydirilganda ajralgan CO₂ hajmini (n.sh., L) toping. (M(CaCO₃)=100)",
      javob="3,36", yechim="n = 0,15 mol → V = 3,36 L.",
      parametrlar=dict(arch="caco3_co2_o1")),
]

# ---------- O2 ----------
check("o41c", 4.8/24*58, 11.6)
O2 = [
 dict(n=41, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Magniyning genetik qatori beriladi: Mg → MgO → MgCl₂ → Mg(OH)₂. Bandlar ketma-ket "
            "yechiladi."),
      bandlar=[
        dict(savol="a) Har bir o'tish uchun reaksiya tenglamasini yozing.",
             yechim=["2Mg + O₂ → 2MgO; MgO + 2HCl → MgCl₂ + H₂O; MgCl₂ + 2NaOH → Mg(OH)₂↓ + 2NaCl."], M=5, A=2),
        dict(savol="b) Har bir moddaning sinfini ayting.",
             yechim=["Mg — metall; MgO — asosli oksid; MgCl₂ — o'rta tuz; Mg(OH)₂ — asos."], M=3, A=2),
        dict(savol="c) 4,8 g magniydan (yo'qotishsiz) olinadigan Mg(OH)₂ massasini hisoblang. "
                   "(M(Mg(OH)₂)=58)",
             yechim=["n = 0,2 mol → m = 0,2·58 = 11,6 g."], M=4, A=3),
        dict(savol="d) Oxirgi mahsulotni yana MgO ga qaytarish yo'lini yozing.",
             yechim=["Mg(OH)₂ → (qizdirish) MgO + H₂O."], M=3, A=3),
      ],
      rasmiylashtirish="Mg zanjiri: tenglamalar → sinflar → hisob → teskari yo'l; M15+A10.",
      parametrlar=dict(arch="mg_zanjir_o2")),
 dict(n=42, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Alyuminiy idishlar haqida maishiy savollar. Quyidagilarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Nega alyuminiy idishda nordon (sirkali, pomidorli) taomlarni uzoq saqlash "
                   "tavsiya etilmaydi? Kimyoviy asosini tushuntiring.",
             yechim=["Kislotalar himoya Al₂O₃ pardasini va metallni eritadi:",
                     "Al₂O₃ + 6H⁺ → 2Al³⁺ + 3H₂O — taomga alyuminiy ionlari o'tadi."], M=13, A=0),
        dict(savol="b) Nega yangi tozalangan (qirilgan) alyuminiy buyum ham bir zumda yaltirashini "
                   "«yo'qotadi»?",
             yechim=["Havo kislorodi bilan darhol yangi yupqa Al₂O₃ pardasi hosil bo'ladi."], M=9, A=0),
        dict(savol="c) Alyuminiyning yana bitta ishlatilish sohasini xossasi bilan bog'lab yozing.",
             yechim=["Elektr simlari — yengil va yaxshi o'tkazuvchan (yoki folga, aviatsiya)."], M=3, A=0),
      ],
      rasmiylashtirish="Al-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="al_mulohaza")),
 dict(n=43, tur="O2", element="II.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch oq kukun jadvalda berilgan:\n"
            "[JADVAL] № | Modda ;; 1 | CaCO₃ (ohaktosh) ;; 2 | CaO (ohak) ;; 3 | CaSO₄·2H₂O (gips)\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Qaysi kukun suv bilan kuchli qizib reaksiyaga kirishadi? Tenglama yozing.",
             yechim=["CaO + H₂O → Ca(OH)₂ + Q — so'nish."], M=4, A=2),
        dict(savol="b) Qaysi kukun kislotada «vishillab» eriydi? Tenglama yozing.",
             yechim=["CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂↑."], M=4, A=3),
        dict(savol="c) Gipsni qolgan ikkitasidan qanday farqlash mumkin?",
             yechim=["Kislota bilan gaz bermaydi, suv bilan qizib ketmaydi — suv bilan qorilsa asta QOTADI."], M=4, A=3),
        dict(savol="d) 1-kukun kuydirilganda massasi nega kamayadi?",
             yechim=["CaCO₃ → CaO + CO₂↑ — gaz uchib chiqadi (100 g dan 56 g qoladi)."], M=3, A=2),
      ],
      rasmiylashtirish="Uch kukun tahlili: kuzatish → tenglama → farqlash; M15+A10.",
      parametrlar=dict(arch="uch_kukun_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261403)
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
    variant="mavzu-II4-A", daraja="A", bob=14, bob_nomi="IIA, IIIA va d-metallar. Suv qattiqligi",
    manba=("MS spetsifikatsiyasi II.4; 9-sinf darslik metallar bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (haykal, samolyot, gips, kir mashina TENi) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
