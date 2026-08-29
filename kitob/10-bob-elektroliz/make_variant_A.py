# -*- coding: utf-8 -*-
"""10-bob A-varianti: Elektroliz (I.10) — O'RGATUVCHI ★★.
Hayotiy sahnalar: zargarlik ustaxonasi, alyuminiy zavodi, avtomobil akkumulyatori, Hoffman apparati.
Soddaroq sonlar, o'rgatuvchi chalg'ituvchilar; barcha javoblar mustaqil hisoblangan."""
import json, random

OUT = "mavzu_I10A.json"
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

# 1 (2) — ta'rif
q(2, "quyi",
  "Elektroliz deb qanday jarayonga aytiladi?",
  "elektr toki ta'sirida elektrolitda boradigan oksidlanish-qaytarilish jarayoniga",
  [("eritmaning ionlarga ajralishiga", "bu dissotsiatsiya — toksiz ham boradi"),
   ("moddaning suvda erishiga", "erish fizik-kimyoviy jarayon"),
   ("issiqlik ta'sirida parchalanishga", "bu termik parchalanish")],
  "Elektroliz — tashqi tok energiyasi hisobiga elektrodlarda boradigan majburiy OQR.",
  dict(arch="elektroliz_tarif"))

# 2 (2) — katod/anod
q(2, "quyi",
  "Elektrolizda KATOD va ANODDA mos ravishda qanday jarayonlar boradi?",
  "qaytarilish va oksidlanish",
  [("oksidlanish va qaytarilish", "teskari: katod «−» — e beradi ionlarga"),
   ("ikkalasida ham qaytarilish", "anodda anionlar/suv e beradi — oksidlanadi"),
   ("ikkalasida ham oksidlanish", "katodda kationlar e oladi — qaytariladi")],
  "Katod (−): kationlar e olib qaytariladi; anod (+): anionlar/suv e berib oksidlanadi.",
  dict(arch="katod_anod"))

# 3 (2) — elektrolit
q(2, "quyi",
  "Quyidagilardan qaysi biri elektrolizga UCHRAYDIGAN muhit (elektrolit) bo'la oladi?",
  "NaCl eritmasi",
  [("distillangan suv", "sof suvda erkin ionlar deyarli yo'q"),
   ("shakar eritmasi", "shakar — noelektrolit, ionlarga ajralmaydi"),
   ("quruq osh tuzi kristali", "qattiq holatda ionlar harakatlanmaydi")],
  "Elektroliz uchun erkin ionlar kerak: tuz eritmasi yoki suyuqlanmasi mos keladi.",
  dict(arch="elektrolit_tanlash"))

# 4 (2) — SAHNA: zargarlik
q(2, "o'rta",
  "Rasmga qarang: zargar uzukni kumush qatlami bilan qoplamoqchi (AgNO₃ eritmasida). Uzuk qaysi "
  "elektrodga ulanishi kerak?",
  "katodga — unda Ag⁺ qaytarilib qatlam o'tiradi",
  [("anodga — u yerda kumush yig'iladi", "anodda oksidlanish boradi, qatlam o'tirmaydi"),
   ("navbat bilan ikkala elektrodga", "qatlam faqat katodda hosil bo'ladi"),
   ("elektrodga ulanmaydi — eritmaga tashlab qo'yiladi", "toksiz qoplama juda sekin/notekis bo'ladi")],
  "Qoplanadigan buyum — katod (−): Ag⁺ + e → Ag qatlam bo'lib o'tiradi.",
  dict(arch="zargarlik_sahna"), fig="jewelry")

# 5 (2) — suv elektrolizi gazlari
q(2, "o'rta",
  "Suv elektroliz qilinganda katodda va anodda mos ravishda qaysi gazlar ajraladi?",
  "H₂ va O₂",
  [("O₂ va H₂", "vodorod katodda (qaytarilish mahsuloti)"),
   ("H₂ va Cl₂", "sof suvda xlor yo'q"),
   ("O₂ va CO₂", "uglerod manbai yo'q")],
  "Katod: 2H₂O+2e→H₂+2OH⁻; anod: 2H₂O−4e→O₂+4H⁺.",
  dict(arch="suv_gazlar"))

# 6 (3) — 1 Faradey
q(3, "o'rta",
  "1 faradey (1 F) zaryad nimani anglatadi?",
  "1 mol elektron zaryadini (≈96500 C)",
  [("1 mol modda massasini", "faradey — zaryad birligi, massa emas"),
   ("1 amper tok kuchini", "amper — tok birligi"),
   ("1 mol gaz hajmini", "22,4 l — molyar hajm, zaryad emas")],
  "1 F = Nₐ ta elektron zaryadi = 96500 C; hisoblarda «necha mol e o'tdi» degani.",
  dict(arch="faradey_tarif"))

# 7 (2) — suyuqlanma mahsulotlari
q(2, "o'rta",
  "NaCl SUYUQLANMASI elektroliz qilinganda katod va anodda mos ravishda nima ajraladi?",
  "Na va Cl₂",
  [("H₂ va Cl₂", "suyuqlanmada suv yo'q — natriy ajraladi"),
   ("Na va O₂", "kislorod manbai yo'q"),
   ("NaOH va HCl", "bular elektrodlarda hosil bo'lmaydi")],
  "Suyuqlanmada faqat Na⁺ va Cl⁻ bor: katodda Na, anodda Cl₂.",
  dict(arch="suyuqlanma_oddiy"))

# 8 (2) — SAHNA: alyuminiy zavodi
q(2, "o'rta",
  "Rasmda alyuminiy zavodi ko'rsatilgan: Al faqat Al₂O₃ SUYUQLANMASINI elektroliz qilib olinadi. "
  "Buning sababi nimada?",
  "Al aktiv metall — eritmada uning o'rniga suv qaytariladi",
  [("Al₂O₃ suvda juda yaxshi eriydi", "aksincha, u suvda erimaydi"),
   ("suyuqlanmada tok kam sarflanadi", "aksincha, suyuqlantirish katta energiya talab qiladi"),
   ("eritmada alyuminiy portlaydi", "xavf emas, qaytarilish tartibidagi gap")],
  "Aktiv metallar (Al, Na, Ca) ionlari suvli eritmada qaytarilmaydi — katodda H₂ chiqadi. "
  "Shuning uchun suyuqlanma (kriolit bilan) ishlatiladi.",
  dict(arch="alzavod_sahna"), fig="aluminum")

# 9 (2) — NaCl eritma katodi
q(2, "o'rta",
  "NaCl ERITMASI elektroliz qilinganda katodda nima ajraladi?",
  "H₂ — suv qaytariladi",
  [("Na — metall qatlami", "aktiv natriy eritmada ajralmaydi"),
   ("Cl₂", "xlor anodda ajraladi"), ("O₂", "kislorod ham anod mahsuloti (boshqa tuzlarda)")],
  "Na aktiv: katodda 2H₂O+2e→H₂+2OH⁻ boradi; eritmada NaOH to'planadi.",
  dict(arch="nacl_eritma_katod"))

# 10 (2) — CuSO4 rang
q(2, "o'rta",
  "CuSO₄ eritmasi elektroliz qilinganda katodda qizil-g'isht rangli qatlam paydo bo'ladi. Bu qaysi modda?",
  "mis — Cu²⁺ qaytarildi",
  [("mis oksidi", "oksid katodda hosil bo'lmaydi"),
   ("oltingugurt", "sulfat-ion qaytarilmaydi"),
   ("vodorod birikmasi", "H₂ — rangsiz gaz")],
  "Cu²⁺ + 2e → Cu⁰: katod yuzasiga mis qatlami o'tiradi.",
  dict(arch="cuso4_rang"))

# 11 (3) — 1 F da Ag
check("q11", 1*108, 108)
q(3, "o'rta",
  "AgNO₃ ning mo'l eritmasidan 1 F zaryad o'tkazilganda katodda necha gramm kumush ajraladi? (M(Ag)=108)",
  "108", [("54", "2 e xato olingan"), ("216", "2 mol xato"), ("10,8", "0,1 F qiymati")],
  "Ag⁺+e→Ag: 1 F → 1 mol → 108 g.",
  dict(arch="ag_1f"))

# 12 (2) — anod ta'rifi
q(2, "quyi",
  "Elektroliz vannasidagi ANOD ...",
  "manbaning «+» qutbiga ulanadi, unda oksidlanish boradi",
  [("«−» qutbga ulanadi, qaytarilish boradi", "bu katod"),
   ("«+» qutbga ulanadi, qaytarilish boradi", "anodda e beriladi — oksidlanish"),
   ("qutbi ahamiyatsiz", "jarayonlar qutbga bog'liq")],
  "Anod (+): anionlar/suv elektron berib oksidlanadi.",
  dict(arch="anod_tarif"))

# 13 (2) — SAHNA: akkumulyator
q(2, "o'rta",
  "Rasmda avtomobil akkumulyatori zaryadga ulangan. Zaryadlanish paytida akkumulyator ichida qanday "
  "jarayon boradi?",
  "elektroliz — tok energiyasi kimyoviy energiyaga aylanadi",
  [("yonish — energiya issiqlikka aylanadi", "ichida alanga yo'q"),
   ("faqat isish — kimyoviy jarayon bormaydi", "elektrodlarda moddalar qayta tiklanadi"),
   ("bug'lanish", "asosiy jarayon elektrokimyoviy")],
  "Zaryadlanish — majburiy OQR (elektroliz): razryadda ketgan reaksiyalar teskari yo'nalishda boradi.",
  dict(arch="akkumulyator_sahna"), fig="carbattery")

# 14 (3) — 0,1 F da Cu
check("q14", 0.1/2*64, 3.2)
q(3, "o'rta",
  "CuSO₄ ning mo'l eritmasidan 0,1 F zaryad o'tkazilganda katodda necha gramm mis ajraladi? (M(Cu)=64)",
  "3,2", [("6,4", "1 e xato olingan"), ("0,64", "o'n barobar xato"), ("32", "1 F ga mos qiymat... 32 g")],
  "Cu²⁺+2e→Cu: n = 0,1/2 = 0,05 mol → 3,2 g.",
  dict(arch="cu_01f"))

# 15 (2) — gazlarni tanish
q(2, "o'rta",
  "Suv elektrolizida katodda yig'ilgan gazga yonayotgan cho'p tutilsa «pop» etib portlab yonadi. Bu qaysi gaz?",
  "vodorod", [("kislorod", "O₂ cho'g'ni yondirib yuboradi, portlamaydi"),
               ("azot", "yonmaydi"), ("karbonat angidrid", "o'chiradi")],
  "«Pop» tovushi — H₂ ning havoda portlab yonishi. Katod mahsuloti — vodorod.",
  dict(arch="gaz_tanish"))

# 16 (3) — H2 hajmi
check("q16", 0.2/2*22.4, 2.24)
q(3, "o'rta",
  "Suvning elektrolizida 0,2 F zaryad o'tganda katodda ajralgan vodorodning hajmini (l, n.sh.) toping.",
  "2,24", [("4,48", "1 e xato"), ("1,12", "0,05 mol xato"), ("22,4", "1 mol deb olingan")],
  "H₂ = 0,2/2 = 0,1 mol → 2,24 l.",
  dict(arch="h2_hajm"))

# 17 (2) — jadval o'qish
q(2, "o'rta",
  "Jadvalda ikki eritma elektrolizining katod mahsulotlari berilgan:\n"
  "[JADVAL] Eritma | Katodda ;; CuSO₄ | Cu ;; K₂SO₄ | H₂\n"
  "Nega ikkinchi holatda metall ajralmadi?",
  "K aktiv metall — uning o'rniga suv qaytariladi",
  [("K⁺ ionlari anodga boradi", "kationlar doim katodga boradi"),
   ("K₂SO₄ dissotsiatsiyalanmaydi", "tuz to'liq dissotsiatsiyalanadi"),
   ("suv kaliyni eritib yuboradi", "kaliy umuman ajralmaydi — sabab qaytarilish tartibida")],
  "Aktivlik qatorining boshidagi metallar (K, Na, Ca, Al) suvli eritmadan ajralmaydi.",
  dict(arch="jadval_oddiy"))

# 18 (2) — SAHNA: Hoffman apparati
q(2, "o'rta",
  "Rasmda suv elektrolizi apparati (Hoffman) ko'rsatilgan: bir naychada gaz ikkinchisidagidan ikki "
  "barobar ko'p yig'ilgan. Ko'p yig'ilgan gaz qaysi va u qaysi elektrod ustida?",
  "H₂ — katod ustida",
  [("O₂ — anod ustida", "kislorod ikki barobar KAM yig'iladi"),
   ("H₂ — anod ustida", "vodorod katod mahsuloti"),
   ("O₂ — katod ustida", "kislorod anodda ajraladi")],
  "2H₂O → 2H₂ + O₂: vodorod (katod) hajmi kislorodnikidan 2 barobar katta.",
  dict(arch="hoffman_sahna"), fig="hoffman")

# 19 (3) — Al hisob
check("q19", 0.3/3*27, 2.7)
q(3, "o'rta",
  "Al₂O₃ suyuqlanmasidan 0,3 F zaryad o'tkazilganda necha gramm alyuminiy olinadi? (M(Al)=27)",
  "2,7", [("8,1", "1 e deb olingan"), ("5,4", "0,2 mol xato"), ("27", "1 mol deb olingan")],
  "Al³⁺+3e→Al: n = 0,1 mol → 2,7 g.",
  dict(arch="al_hisob"))

# 20 (2) — qo'llanilish
q(2, "o'rta",
  "Elektroliz sanoatda nimalar uchun QO'LLANILADI? Eng to'liq javobni tanlang.",
  "aktiv metallar olish, metallarni rafinlash, buyumlarni qoplash",
  [("faqat suvni tozalash", "asosiy qo'llanilishlar kengroq"),
   ("neft mahsulotlarini ajratish", "bu rektifikatsiya — fizik usul"),
   ("faqat issiqlik olish", "elektroliz issiqlik manbai emas")],
  "Elektroliz: Na/Al olish, Cu rafinlash, galvanostegiya, Cl₂/NaOH ishlab chiqarish.",
  dict(arch="qollanilish_oddiy"))

# 21 (3) — NaOH hisob
check("q21", 0.2*40, 8)
q(3, "o'rta",
  "NaCl ning mo'l eritmasidan 0,2 F zaryad o'tkazilganda eritmada necha gramm NaOH to'planadi? (M=40)",
  "8", [("4", "0,1 mol xato"), ("16", "0,4 mol qiymati"), ("40", "1 mol deb olingan")],
  "OH⁻ = 0,2 mol → NaOH = 8 g.",
  dict(arch="naoh_oddiy"))

# 22 (3) — vaqt hisobi
check("q22", 96500/1, 96500)
q(3, "o'rta",
  "1 A tok kuchida 1 F (96500 C) zaryad o'tishi uchun qancha vaqt kerak?",
  "96500 s (≈26,8 soat)", [("3600 s (1 soat)", "Q = I·t: 3600 C bo'lardi"),
                            ("965 s", "yuz barobar xato"), ("86400 s (1 sutka)", "sutka 86400 s — mos emas")],
  "t = Q/I = 96500/1 = 96500 s ≈ 26,8 soat.",
  dict(arch="vaqt_oddiy"))

# 23 (2) — rafinlash maqsadi
q(2, "o'rta",
  "Misni elektrolitik RAFINLASHDAN maqsad nima?",
  "xom misni qo'shimchalardan tozalab, yuqori toza mis olish",
  [("misni boshqa metallga aylantirish", "element o'zgarmaydi"),
   ("mis ishlab chiqarish hajmini oshirish", "miqdor emas, tozalik ortadi"),
   ("misning rangini o'zgartirish", "rang tabiiy xossa")],
  "Xom mis anodda eriydi, katodda 99,99 % li toza mis o'tiradi; qo'shimchalar shlamda qoladi.",
  dict(arch="rafinlash_maqsad"))

# 24 (3) — massa kamayishi
check("q24", 0.5/2*64 + 0.5/4*32, 20)
q(3, "o'rta",
  "CuSO₄ ning mo'l eritmasidan 0,5 F zaryad o'tkazilganda eritma massasi necha grammga kamayadi?",
  "20", [("16", "faqat mis hisoblangan"), ("4", "faqat kislorod hisoblangan"),
          ("40", "1 F uchun qiymat")],
  "Cu = 0,25 mol (16 g); O₂ = 0,125 mol (4 g) → jami 20 g.",
  dict(arch="massa_oddiy"))

# 25 (2) — tok o'tkazuvchi eritma
q(2, "o'rta",
  "Qaysi suyuqlik elektr tokini O'TKAZMAYDI?",
  "spirtning suvdagi eritmasi",
  [("KCl eritmasi", "kuchli elektrolit — o'tkazadi"),
   ("H₂SO₄ eritmasi", "kuchli kislota — o'tkazadi"),
   ("NaOH eritmasi", "ishqor — o'tkazadi")],
  "Spirt — noelektrolit: eritmada erkin ionlar hosil qilmaydi.",
  dict(arch="otkazmaydigan"))

# 26 (3) — grafik tanlash: m ~ Q
q(3, "o'rta",
  "Katodda ajralgan metall massasining o'tgan zaryadga bog'liqligi (elektrolit mo'l) qanday grafik bilan "
  "ifodalanadi?",
  "noldan chiquvchi to'g'ri chiziq",
  [("gorizontal to'g'ri chiziq", "zaryad ortsa massa ham ortadi"),
   ("avval ortib, so'ng to'xtaydigan chiziq", "elektrolit mo'l — to'xtash yo'q"),
   ("egri chiziq (parabola)", "m = (M/nF)·Q — chiziqli bog'lanish")],
  "Faradey qonuni: m ~ Q — proporsional (to'g'ri chiziq).",
  svg=dict(correct="rise", d1="flat", d2="rise_flat", d3="u", xlab="Q", ylab="m"),
  params=dict(arch="grafik_mq"))

# 27 (3) — teskari F
check("q27", 5.4/108, 0.05)
q(3, "o'rta",
  "Katodda 5,4 g kumush ajralishi uchun AgNO₃ eritmasidan necha faradey zaryad o'tkazish kerak? (M(Ag)=108)",
  "0,05", [("0,1", "10,8 g uchun qiymat"), ("0,5", "54 g uchun qiymat"), ("0,025", "2 e xato")],
  "n(Ag) = 0,05 mol; Ag⁺ + e → 0,05 F.",
  dict(arch="teskari_f_oddiy"))

# 28 (2) — qoplama sifatiga ta'sir
q(2, "o'rta",
  "Galvanik qoplama qalinligi asosan nimalarga bog'liq?",
  "tok kuchi va elektroliz vaqtiga",
  [("faqat eritma rangiga", "rang qalinlikni belgilamaydi"),
   ("faqat idish shakliga", "shakl tekislikka ta'sir qilishi mumkin, qalinlikka emas"),
   ("buyumning nomiga", "ahamiyatsiz")],
  "m ~ I·t (Faradey): tok kuchi va vaqt qancha katta bo'lsa, qatlam shuncha qalin.",
  dict(arch="qoplama_omil"))

# 29 (3) — Cl2 hajmi
check("q29", 0.2/2*22.4, 2.24)
q(3, "o'rta",
  "NaCl ning mo'l eritmasidan 0,2 F zaryad o'tkazilganda anodda ajralgan xlorning hajmini (l, n.sh.) toping.",
  "2,24", [("4,48", "1 e xato"), ("1,12", "0,05 mol xato"), ("2,8", "asossiz qiymat")],
  "Cl₂ = 0,2/2 = 0,1 mol → 2,24 l.",
  dict(arch="cl2_oddiy"))

# 30 (2) — xato fikr
q(2, "o'rta",
  "Elektroliz haqidagi fikrlardan XATOSINI toping.",
  "elektroliz o'z-o'zidan (tashqi toksiz) boradi",
  [("elektroliz majburiy OQR jarayoni", "to'g'ri — tok energiyasi hisobiga"),
   ("katodda qaytarilish boradi", "to'g'ri fikr"),
   ("suyuqlanma va eritma elektrolizi farq qilishi mumkin", "to'g'ri — suv ishtiroki tufayli")],
  "Elektroliz — majburiy jarayon: tashqi tok manbaisiz bormaydi (galvanik elementdan farqi shu).",
  dict(arch="xato_fikr"))

# 31 (3) — Al 0,15 F
check("q31", 0.15/3*27, 1.35)
q(3, "o'rta",
  "Al₂O₃ suyuqlanmasidan 0,15 F zaryad o'tkazilganda necha gramm alyuminiy ajraladi? (M(Al)=27)",
  "1,35", [("4,05", "1 e xato"), ("2,7", "0,3 F qiymati"), ("0,45", "9 ga bo'lish xatosi")],
  "n(Al) = 0,15/3 = 0,05 mol → 1,35 g.",
  dict(arch="al_015"))

# 32 (3) — RASMLI: Hoffman o'qish (hisob)
check("q32", 0.2/2*22.4, 2.24); check("q32b", 0.2/4*22.4, 1.12)
q(3, "o'rta",
  "18-savoldagi apparatda 0,2 F zaryad o'tdi. Katod va anod naychalarida yig'ilgan gazlarning "
  "hajmlari (l, n.sh.) mos ravishda qancha bo'ladi?",
  "2,24 va 1,12", [("1,12 va 2,24", "vodorod ko'p yig'iladi"), ("4,48 va 2,24", "1 e xato"),
                    ("2,24 va 2,24", "kislorod 4 e talab qiladi — ikki barobar kam")],
  "H₂ = 0,1 mol (2,24 l); O₂ = 0,05 mol (1,12 l).",
  dict(arch="hoffman_hisob"), fig="hoffman")

# ---------- Y2: zargarlik ustaxonasi ----------
check("y2_33", 0.02*108, 2.16)
check("y2_34", 0.02, 0.02)
check("y2_35", 0.04, 0.04)
Y2 = dict(
  n=33, tur="Y2", element="I.10",
  ichki_pasport=[dict(n=33, element="I.10", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.10", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.10", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Zargarlik ustaxonasida kumushlash vannasi (AgNO₃) orqali bitta uzuk uchun 0,02 F zaryad "
               "o'tkaziladi. (M(Ag)=108.) 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Uzukka o'tirgan kumushning massasi (g) qancha?",
    "34. Bunda necha mol elektron sarflandi?",
    "35. Qatlamni IKKI BAROBAR qalin qilish uchun necha faradey zaryad kerak?"],
  javoblar_royxati=["A) 2,16", "B) 0,02", "C) 0,04", "D) 4,32", "E) 0,2", "F) 1,08"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="0,04 F dagi massa — 33 ga xato javob"),
                   dict(variant="E", xato="o'n barobar xato"),
                   dict(variant="F", xato="2 e deb olish xatosi")],
  yechim=("33: Ag = 0,02 mol → 2,16 g (A). 34: 1 e → 0,02 mol e (B). "
          "35: massa ~ Q → 0,04 F (C)."),
  parametrlar=dict(arch="ustaxona_ssenariy", f=0.02))

# ---------- O1 ----------
check("o38", 0.1/2*22.4, 1.12)
check("o39", 1/2*64, 32)
check("o40", 10.8/108, 0.1)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="Elektrolizda katodda boradigan jarayonning nomini yozing (oksidlanish yoki qaytarilish).",
      javob="qaytarilish", yechim="Katod (−) — kationlar elektron oladi.",
      parametrlar=dict(arch="jarayon_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="Suv elektrolizida H₂ hajmi O₂ hajmidan necha marta katta bo'ladi?",
      javob="2", yechim="2H₂O → 2H₂ + O₂ → nisbat 2:1.",
      parametrlar=dict(arch="nisbat_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="0,1 F zaryad o'tganda katodda ajralgan vodorodning hajmini (l, n.sh.) toping.",
      javob="1,12", yechim="H₂ = 0,05 mol → 1,12 l.",
      parametrlar=dict(arch="h2_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="CuSO₄ ning mo'l eritmasidan 1 F zaryad o'tkazilganda ajralgan misning massasini (g) toping. (M(Cu)=64)",
      javob="32", yechim="Cu = 0,5 mol → 32 g.",
      parametrlar=dict(arch="cu_o1a")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Katodda 10,8 g kumush ajralishi uchun necha faradey zaryad kerak? (M(Ag)=108)",
      javob="0,1", yechim="n(Ag) = 0,1 mol → 0,1 F.",
      parametrlar=dict(arch="f_o1")),
]

# ---------- O2 ----------
check("o41b", 0.4/2, 0.2); check("o41b2", 0.2*22.4, 4.48)
check("o41c", 0.4/4, 0.1); check("o41c2", 0.1*22.4, 2.24)
check("o41d", 4.48+2.24, 6.72)
check("o43b", 1*108, 108)
check("o43c", 96500/4, 24125)
O2 = [
 dict(n=41, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Na₂SO₄ eritmasi (amalda suv elektrolizi) inert elektrodlarda elektroliz qilinib, 0,4 F "
            "zaryad o'tkazildi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Katod va anod jarayonlarining tenglamalarini yozing.",
             yechim=["Katod: 2H₂O+2e→H₂+2OH⁻; anod: 2H₂O−4e→O₂+4H⁺"], M=3, A=1),
        dict(savol="b) Katodda ajralgan vodorodning miqdorini (mol) va hajmini (l, n.sh.) toping.",
             yechim=["H₂ = 0,4/2 = 0,2 mol → 4,48 l"], M=4, A=3),
        dict(savol="c) Anodda ajralgan kislorodning miqdorini (mol) va hajmini toping.",
             yechim=["O₂ = 0,4/4 = 0,1 mol → 2,24 l"], M=3, A=2),
        dict(savol="d) Ikkala gazning umumiy hajmini hisoblang.",
             yechim=["4,48 + 2,24 = 6,72 l"], M=2, A=2),
        dict(savol="e) Nega sof (distillangan) suv o'rniga tuz eritmasi olinadi? Izohlang.",
             yechim=["Sof suvda ionlar juda kam — tok o'tmaydi; Na₂SO₄ o'tkazuvchanlikni ta'minlaydi,",
                     "o'zi esa elektrodlarda o'zgarmaydi."], M=3, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi zanjir: tenglamalar → H₂ → O₂ → jami → izoh; M15+A10.",
      parametrlar=dict(arch="suv_zanjir", f=0.4)),
 dict(n=42, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Zargarlik ustaxonasida qoshiqni kumushlashmoqchi. Quyidagi savollarga MULOHAZA yuritib "
            "javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) Kumushlash vannasining sxemasini so'z bilan tavsiflang: qoshiq va kumush plastinka "
                   "qaysi elektrod bo'ladi, elektrolit nima, elektrodlarda qanday jarayonlar boradi?",
             yechim=["Qoshiq — katod (Ag⁺+e→Ag qatlam o'tiradi); toza kumush plastinka — anod (Ag−e→Ag⁺ eriydi);",
                     "elektrolit — AgNO₃ eritmasi."], M=13, A=0),
        dict(savol="b) Nega anod sifatida aynan KUMUSH plastinka olinadi (inert emas)?",
             yechim=["Anod erib, eritmadagi Ag⁺ konsentratsiyasini doimiy saqlaydi — qoplama bir tekis boradi."], M=9, A=0),
        dict(savol="c) Qatlam tekis bo'lishi uchun qanday amaliy shart muhim?",
             yechim=["Kichik tok zichligi (sekin qoplash) va buyumning toza yuzasi."], M=3, A=0),
      ],
      rasmiylashtirish="Amaliy mulohaza formati (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="qoshiq_mulohaza")),
 dict(n=43, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("AgNO₃ eritmasi bilan uchta tajriba o'tkazildi; hammasida bir xil massa kumush olindi. "
            "Ma'lumotlar jadvalda:\n"
            "[JADVAL] Tajriba | Tok kuchi, A | Vaqt, s ;; 1 | 1 | 96500 ;; 2 | 2 | 48250 ;; 3 | 4 | ?\n"
            "Bandlar ketma-ket yechiladi. (M(Ag)=108, F=96500 C/mol)"),
      bandlar=[
        dict(savol="a) 1- va 2-tajribalarda o'tgan zaryadlarni (F) hisoblab, ular tengligini ko'rsating.",
             yechim=["Q₁ = 1·96500 = 96500 C = 1 F; Q₂ = 2·48250 = 96500 C = 1 F."], M=4, A=2),
        dict(savol="b) Har bir tajribada ajralgan kumush massasini toping.",
             yechim=["1 F → 1 mol Ag = 108 g"], M=4, A=3),
        dict(savol="c) 3-tajribadagi «?» vaqtni hisoblang.",
             yechim=["t = 96500/4 = 24125 s"], M=4, A=3),
        dict(savol="d) Xulosa chiqaring: ajralgan massa nimaga bog'liq?",
             yechim=["m ~ Q = I·t: tok kuchi va vaqt ko'paytmasi bir xil bo'lsa, massa ham bir xil."], M=3, A=2),
      ],
      rasmiylashtirish="Jadval-tahlil (I·t tengligi): M15+A10.",
      parametrlar=dict(arch="it_jadval")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260214)
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
    d = dict(n=n, tur="Y1", element="I.10", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I10-A", daraja="A", bob=10, bob_nomi="Elektroliz",
    manba=("MS spetsifikatsiyasi I.10; darslik elektroliz bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (zargarlik, Al zavodi, akkumulyator, Hoffman) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq sonlar, rasmli hayotiy savollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.10") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
