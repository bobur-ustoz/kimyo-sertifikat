# -*- coding: utf-8 -*-
"""10-bob B-varianti: Elektroliz (I.10) — HAQIQIY MS MUHITI ★★★.
Faradey hisoblari, eritma/suyuqlanma mahsulotlari, teskari (X%) masalalar,
ikki bosqichli katod jarayonlari. Javoblar mustaqil qayta hisoblangan."""
import json, random

OUT = "mavzu_I10B.json"
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

# 1 (3) — suyuqlanma vs eritma
q(3, "yuqori",
  "NaCl SUYUQLANMASI va NaCl ERITMASI inert elektrodlarda elektroliz qilinganda katodda mos "
  "ravishda nima ajraladi?",
  "Na va H₂",
  [("Na va Na", "eritmada aktiv metall ajralmaydi — suv qaytariladi"),
   ("H₂ va H₂", "suyuqlanmada suv yo'q — Na⁺ qaytariladi"),
   ("Cl₂ va O₂", "bular anod mahsulotlari")],
  "Suyuqlanmada raqobat yo'q: Na⁺+e→Na. Eritmada Na aktiv — suv qaytariladi: 2H₂O+2e→H₂+2OH⁻.",
  dict(arch="suyuqlanma_eritma"))

# 2 (3) — CuSO4 mahsulotlari
q(3, "yuqori",
  "CuSO₄ eritmasi inert elektrodlarda elektroliz qilinganda katod va anodda mos ravishda nima ajraladi, "
  "eritmada qaysi modda to'planadi?",
  "Cu; O₂; H₂SO₄",
  [("Cu; SO₂; SO₃", "sulfat-ion anodda oksidlanmaydi — suv oksidlanadi"),
   ("H₂; O₂; CuSO₄", "Cu aktivlik qatorida H dan keyin — o'zi qaytariladi"),
   ("Cu; O₂; Cu(OH)₂", "eritmada H⁺ ortadi — kislota to'planadi")],
  "Katod: Cu²⁺+2e→Cu; anod: 2H₂O−4e→O₂+4H⁺ → eritmada H₂SO₄ to'planadi.",
  dict(arch="cuso4_mahsulot"))

# 3 (2) — katodda jarayon
q(2, "yuqori",
  "Elektroliz jarayonida KATODDA qanday jarayon boradi?",
  "qaytarilish — kationlar (yoki suv) elektron oladi",
  [("oksidlanish — anionlar elektron beradi", "bu anod jarayoni"),
   ("neytrallanish", "kislota-asos jarayoni elektrodda bormaydi"),
   ("dissotsiatsiya", "dissotsiatsiya eritmaning o'zida boradi")],
  "Katod manba «−» qutbiga ulanadi: unga kelgan zarrachalar e olib qaytariladi.",
  dict(arch="katod_jarayon"))

# 4 (3) — grafik tanlash: m(katod)-t CuSO4 cheklangan
q(3, "yuqori",
  "Oz miqdordagi CuSO₄ eritmasi doimiy tok bilan elektroliz qilinmoqda. KATOD massasining vaqtga "
  "bog'liq grafigi qanday bo'ladi? (Cu²⁺ tugagach elektroliz davom etadi.)",
  "chiziqli ortib, so'ng o'zgarmay qoladi",
  [("doimiy chiziqli ortadi", "Cu²⁺ tugagach katodda H₂ ajraladi — gaz massani oshirmaydi"),
   ("boshdan o'zgarmas", "Cu ajralar ekan massa ortadi"),
   ("ortib, keyin kamayadi", "ajralgan mis qaytib erimaydi")],
  "Cu²⁺ bor ekan m ~ Q chiziqli ortadi; tugagach katodda H₂ chiqadi — massa o'zgarmaydi.",
  svg=dict(correct="rise_flat", d1="rise", d2="flat", d3="rise_fall", xlab="t", ylab="m(katod)"),
  params=dict(arch="grafik_mt"))

# 5 (3) — RASMLI: m-Q grafigidan o'qish
check("q5", 0.2*108, 21.6)
q(3, "yuqori",
  "Rasmda AgNO₃ eritmasi elektrolizida katodda ajralgan kumush massasining o'tgan zaryadga (F) "
  "bog'liqligi berilgan. Grafikdan foydalanib, 0,2 F zaryadda ajralgan kumush massasini toping (g).",
  "21,6", [("10,8", "0,1 F qiymati"), ("43,2", "0,4 F qiymati"), ("5,4", "0,05 F qiymati")],
  "Ag⁺+e→Ag: 1 F → 108 g. Grafikdan: 0,2 F → 21,6 g.",
  dict(arch="grafik_oqish", f=0.2), fig="mt_graph")

# 6 (3) — faradey hisob (Cu)
check("q6", 0.2/2*64, 6.4)
q(3, "yuqori",
  "CuSO₄ ning mo'l eritmasidan 0,2 F zaryad o'tkazildi. Katodda ajralgan misning massasini (g) toping. "
  "(M(Cu)=64)",
  "6,4", [("12,8", "2 e ekani unutilgan"), ("3,2", "0,1 F uchun qiymat"), ("64", "1 mol deb olingan")],
  "Cu²⁺+2e→Cu: n(Cu) = 0,2/2 = 0,1 mol → 6,4 g.",
  dict(arch="faradey_cu"))

# 7 (3) — Cl2 hajmi
check("q7", 1/2*22.4, 11.2)
q(3, "yuqori",
  "NaCl ning mo'l eritmasidan 1 F zaryad o'tkazilganda anodda ajralgan xlorning hajmini (l, n.sh.) toping.",
  "11,2", [("22,4", "1 mol deb olingan"), ("5,6", "0,25 mol xato"), ("44,8", "2 mol xato")],
  "2Cl⁻−2e→Cl₂: n(Cl₂) = 1/2 = 0,5 mol → 11,2 l.",
  dict(arch="cl2_hajm"))

# 8 (2) — suv elektrolizi bo'ladigan tuz
q(2, "yuqori",
  "Qaysi tuz ERITMASINING elektrolizi amalda faqat SUVNING parchalanishiga teng bo'ladi?",
  "Na₂SO₄", [("CuSO₄", "katodda mis ajraladi"), ("NaCl", "anodda xlor ajraladi"),
              ("AgNO₃", "katodda kumush ajraladi")],
  "Na⁺ (aktiv) qaytarilmaydi, SO₄²⁻ oksidlanmaydi → ikkala elektrodda ham suv parchalanadi (H₂ va O₂).",
  dict(arch="suv_elektroliz_tuz"))

# 9 (2) — kationlar navbati
q(2, "yuqori",
  "Tarkibida Cu²⁺ va K⁺ ionlari bo'lgan eritma elektroliz qilinganda katodda BIRINCHI navbatda nima qaytariladi?",
  "Cu²⁺ ionlari",
  [("K⁺ ionlari", "aktiv metall ioni eritmada qaytarilmaydi"),
   ("ikkala ion baravar", "qaytarilish osonligi aktivlikka teskari"),
   ("suv molekulalari", "Cu²⁺ turganda suv navbatda emas")],
  "Aktivlik qatorida keyin turgan metallning ioni oson qaytariladi: avval Cu²⁺, K⁺ esa umuman qaytarilmaydi.",
  dict(arch="kation_navbat"))

# 10 (3) — suv sarfi (bank arxetipi)
check("q10", (0.2 + 0.8/2)*18, 10.8)
q(3, "yuqori",
  "0,1 kg 11,7 % li NaCl eritmasidan 1 F zaryad o'tkazildi. Elektroliz davomida sarflangan suvning "
  "massasini (g) toping. (M(NaCl)=58,5)",
  "10,8", [("9", "faqat katod suvi hisoblangan holdagi xato"), ("5,4", "0,3 mol xato"),
            ("12,6", "0,4 mol NaCl (boshqa masala) qiymati")],
  "NaCl = 0,2 mol → 0,2 F da: 2NaCl+2H₂O→2NaOH+H₂+Cl₂ (suv 0,2 mol). Qolgan 0,8 F — suv elektrolizi: "
  "2H₂O→2H₂+O₂ (4 F ga 2 mol) → 0,4 mol. Jami 0,6 mol = 10,8 g.",
  dict(arch="suv_sarfi", nacl=0.2))

# 11 (3) — teskari X% (bank arxetipi)
check("q11", (2-1)/2*160/200*100, 40)
q(3, "yuqori",
  "0,2 kg X % li CuSO₄ eritmasi orqali 2 F zaryad o'tkazilganda katodda 11,2 l (n.sh.) gaz ajraldi. "
  "X ni aniqlang (inert elektrodlar).",
  "40", [("20", "Cu uchun 1 F deb olingan"), ("60", "gaz 1 mol deb olingan"),
          ("50", "eritma 0,16 kg xato")],
  "Katodda gaz (H₂ 0,5 mol) — 1 F sarflagan; qolgan 1 F misga: Cu = 0,5 mol → CuSO₄ 80 g → X = 80/200 = 40 %.",
  dict(arch="teskari_foiz", m=200, f=2))

# 12 (2) — anodda suv oksidlanishi
q(2, "yuqori",
  "K₂SO₄ eritmasi elektroliz qilinganda ANODDA qanday jarayon boradi?",
  "2H₂O − 4e → O₂ + 4H⁺ (suv oksidlanadi)",
  [("SO₄²⁻ − 2e → SO₄ (ion oksidlanadi)", "kislorodli kislota qoldig'i eritmada oksidlanmaydi"),
   ("K⁺ + e → K", "bu katod jarayoni bo'lardi (lekin K aktiv)"),
   ("2H₂O + 2e → H₂ + 2OH⁻", "bu katodda boradigan qaytarilish")],
  "SO₄²⁻ barqaror — anodda suv oksidlanib O₂ ajraladi.",
  dict(arch="anod_suv"))

# 13 (3) — ketma-ket qaytarilish hisobi
check("q13", 0.1*108 + (0.25-0.1)/2*64, 15.6)
q(3, "yuqori",
  "Tarkibida 0,1 mol AgNO₃ va 0,1 mol Cu(NO₃)₂ bo'lgan eritmadan 0,25 F zaryad o'tkazildi. Katodda "
  "ajralgan moddalarning umumiy massasini (g) toping. (M(Ag)=108, M(Cu)=64)",
  "15,6", [("10,8", "faqat kumush hisoblangan"), ("17,2", "Cu 0,1 mol to'liq ajraldi deb olingan"),
            ("14,0", "Ag uchun 2 e xato olingan")],
  "Avval Ag⁺: 0,1 mol (0,1 F) → 10,8 g. Qolgan 0,15 F → Cu 0,075 mol → 4,8 g. Jami 15,6 g.",
  dict(arch="ketma_ket"))

# 14 (3) — 1-2-3: suyuqlanmadan olinadigan metallar
q(3, "yuqori",
  "Qaysi metallar sanoatda ularning birikmalari SUYUQLANMASINI elektroliz qilib olinadi?\n"
  "1) natriy;  2) alyuminiy;  3) mis;  4) kalsiy.",
  "1, 2 va 4",
  [("1 va 2", "Ca ham suyuqlanma (CaCl₂) elektrolizidan olinadi"),
   ("2 va 3", "mis eritma elektrolizi/pirometallurgiya bilan olinadi"),
   ("1, 3 va 4", "mis suyuqlanmani talab qilmaydi")],
  "Aktiv metallar (Na, Ca, Al) suvli eritmadan ajralmaydi — faqat suyuqlanmadan olinadi. Cu — eritmadan.",
  dict(arch="suyuqlanma_tanlov"))

# 15 (3) — vaqt hisobi
check("q15", 0.02*96500/2, 965)
q(3, "yuqori",
  "2 A tok kuchida 0,02 mol elektron o'tishi uchun qancha vaqt (s) kerak? (F = 96500 C/mol)",
  "965", [("1930", "Q ning o'zi (kulon)"), ("482,5", "4 A uchun qiymat"), ("96,5", "o'n barobar xato")],
  "Q = 0,02·96500 = 1930 C → t = Q/I = 1930/2 = 965 s.",
  dict(arch="vaqt_hisob"))

# 16 (2) — elektrod qutblari
q(2, "yuqori",
  "Elektroliz vannasida KATOD tok manbaining qaysi qutbiga ulanadi va unda qanday zaryadli zarrachalar razryadlanadi?",
  "manfiy qutbga; kationlar",
  [("musbat qutbga; anionlar", "bu anodning ta'rifi"),
   ("manfiy qutbga; anionlar", "manfiy elektrodga musbat ionlar tortiladi"),
   ("musbat qutbga; kationlar", "kationlar manfiy elektrodga boradi")],
  "Katod «−» qutbga ulanadi; unga musbat ionlar (kationlar) kelib qaytariladi.",
  dict(arch="qutb"))

# 17 (3) — JADVALLI: mahsulotlar «?»
q(3, "yuqori",
  "Inert elektrodlardagi elektroliz mahsulotlari jadvalda berilgan:\n"
  "[JADVAL] Eritma | Katodda | Anodda ;; NaCl | ? | Cl₂ ;; CuSO₄ | Cu | ? ;; Na₂SO₄ | H₂ | O₂\n"
  "«?» o'rnidagi mahsulotlarni mos ravishda aniqlang.",
  "H₂ va O₂", [("Na va O₂", "eritmada natriy ajralmaydi"), ("H₂ va SO₂", "sulfat-ion oksidlanmaydi"),
                ("Na va SO₃", "ikkala katak ham xato")],
  "NaCl eritmasida katodda suv qaytariladi (H₂); CuSO₄ da anodda suv oksidlanadi (O₂).",
  dict(arch="mahsulot_jadval"))

# 18 (2) — galvanostegiya
q(2, "yuqori",
  "Metall buyumni nikel bilan qoplash (galvanostegiya) uchun buyum qaysi elektrod vazifasida ulanadi?",
  "katod — unda Ni²⁺ qaytarilib qatlam hosil qiladi",
  [("anod — u erib turadi", "anod sifatida nikel plastinka ulanadi"),
   ("istalgan elektrod", "metall faqat katodda ajraladi"),
   ("elektrolitning o'zi", "buyum elektrod bo'lishi shart")],
  "Qoplanadigan buyum — katod: Ni²⁺ + 2e → Ni. Anod — eriydigan Ni plastinka.",
  dict(arch="galvanostegiya"))

# 19 (3) — eritma massasi kamayishi
check("q19", 0.5*64 + 0.25*32, 40)
q(3, "yuqori",
  "CuSO₄ ning mo'l eritmasidan 1 F zaryad o'tkazilganda eritma massasi necha grammga kamayadi? "
  "(Katodda faqat mis ajraladi.)",
  "40", [("32", "anod kislorodi unutilgan"), ("8", "faqat O₂ hisoblangan"), ("72", "Cu 1 mol deb olingan")],
  "Cu = 0,5 mol (32 g) + O₂ = 0,25 mol (8 g) → eritmadan 40 g chiqib ketadi.",
  dict(arch="massa_kamayish"))

# 20 (2) — ion o'tkazuvchanlik
q(2, "yuqori",
  "Nima uchun qattiq NaCl tok o'tkazmaydi-yu, uning suyuqlanmasi o'tkazadi?",
  "suyuqlanmada ionlar erkin harakatlanadi",
  [("suyuqlanmada erkin elektronlar paydo bo'ladi", "o'tkazuvchanlik ionli, elektronli emas"),
   ("qattiq holatda ionlar yo'q", "ionlar bor, lekin panjarada mahkam"),
   ("suyuqlanmada molekulalar hosil bo'ladi", "NaCl ion birikma — molekula hosil qilmaydi")],
  "Kristallda ionlar tugunlarda qotgan; suyuqlanishda ular erkinlashib zaryad tashiy oladi.",
  dict(arch="ion_otkazish"))

# 21 (3) — massa + atom soni (bank arxetipi, toza sonlar)
check("q21", 0.5*64 + 0.5*32 + 0.5*1*2, 49)
q(3, "yuqori",
  "CuSO₄ eritmasi inert elektrodlarda elektroliz qilinganda eritma massasi 49 g ga, undagi atomlar soni "
  "2,5·Nₐ taga kamaydi. Eritmadan necha faradey zaryad o'tgan?",
  "2", [("1", "faqat mis bosqichi hisoblangan"), ("1,5", "vodorod bosqichi unutilgan"),
         ("2,5", "atomlar soni faradeyga tenglashtirilgan")],
  "Cu²⁺ 0,5 mol bo'lgan: 1-bosqich (1 F): Cu 0,5 mol (32 g; 0,5Nₐ atom). Anodda jami O₂ 0,5 mol "
  "(16 g; 1Nₐ atom). 2-bosqich (1 F): H₂ 0,5 mol (1 g; 1Nₐ atom). Jami: 49 g va 2,5Nₐ → 2 F.",
  dict(arch="massa_atom"))

# 22 (3) — Al suyuqlanma
check("q22", 0.3/3*27, 2.7)
q(3, "yuqori",
  "Al₂O₃ suyuqlanmasidan (kriolitda) 0,3 F zaryad o'tkazilganda katodda necha gramm alyuminiy ajraladi? "
  "(M(Al)=27)",
  "2,7", [("8,1", "1 e deb olingan"), ("0,9", "9 ga bo'lish xatosi"), ("5,4", "0,2 mol xato")],
  "Al³⁺+3e→Al: n = 0,3/3 = 0,1 mol → 2,7 g.",
  dict(arch="al_suyuqlanma"))

# 23 (3) — 1-2-3: katodda metall ajraladigan eritmalar
q(3, "yuqori",
  "Qaysi eritmalar elektroliz qilinganda katodda METALL ajraladi?\n"
  "1) CuSO₄;  2) AgNO₃;  3) KNO₃;  4) NaCl.",
  "1 va 2",
  [("1, 2 va 4", "NaCl eritmasida katodda H₂ ajraladi"),
   ("faqat 1", "kumush ham H dan keyin — katodda ajraladi"),
   ("2 va 3", "K⁺ eritmada qaytarilmaydi")],
  "H dan keyingi metallar (Cu, Ag) eritmadan ajraladi; K, Na — aktiv, o'rniga suv qaytariladi.",
  dict(arch="metall_tanlov"))

# 24 (2) — qo'llanilish emas
q(2, "yuqori",
  "Quyidagilardan qaysi biri elektrolizning sanoatdagi qo'llanilishiga MANSUB EMAS?",
  "neftni haydash (rektifikatsiya)",
  [("alyuminiy olish", "Al₂O₃ suyuqlanmasi elektrolizi"),
   ("misni rafinlash", "eruvchan anodli elektroliz"),
   ("buyumlarni xromlash", "galvanostegiya — elektroliz turi")],
  "Rektifikatsiya — fizik ajratish (qaynash haroratlari bo'yicha), elektrokimyoga aloqasi yo'q.",
  dict(arch="qollanilish"))

# 25 (3) — rafinlash
check("q25", 1/2*64, 32)
q(3, "yuqori",
  "Misni rafinlashda xom mis ANOD qilib ulanadi. 1 F zaryad o'tganda anodning massasi necha grammga "
  "kamayadi? (M(Cu)=64)",
  "32", [("64", "1 mol deb olingan"), ("16", "4 e xato"), ("0", "anod erimaydi deb olingan")],
  "Eruvchan anod: Cu⁰−2e→Cu²⁺ → 0,5 mol = 32 g eriydi (katodda shuncha toza mis o'tiradi).",
  dict(arch="rafinlash"))

# 26 (3) — NaOH hosil bo'lishi
check("q26", 0.4*40, 16)
q(3, "yuqori",
  "NaCl ning mo'l eritmasidan 0,4 F zaryad o'tkazilganda eritmada necha gramm NaOH to'planadi? "
  "(M(NaOH)=40)",
  "16", [("8", "0,2 mol deb olingan"), ("40", "1 mol deb olingan"), ("32", "0,8 mol xato")],
  "Katodda 2H₂O+2e→H₂+2OH⁻: OH⁻ = 0,4 mol → NaOH 0,4 mol = 16 g.",
  dict(arch="naoh_hisob"))

# 27 (3) — RASMLI: grafikdan teskari o'qish
check("q27", 32.4/108, 0.3)
q(3, "yuqori",
  "5-savoldagi grafikdan foydalaning: katodda 32,4 g kumush ajralishi uchun eritmadan necha faradey "
  "zaryad o'tishi kerak?",
  "0,3", [("0,2", "21,6 g uchun qiymat"), ("0,4", "43,2 g uchun qiymat"), ("3", "o'n barobar xato")],
  "Grafik: 1 F → 108 g nisbat → 32,4/108 = 0,3 F.",
  dict(arch="grafik_teskari"), fig="mt_graph")

# 28 (2) — RASMLI: elektrolizyor sxemasi
q(2, "yuqori",
  "Rasmdagi elektrolizyor sxemasida qaysi elektrod KATOD hisoblanadi?",
  "tok manbaining «−» qutbiga ulangan 1-elektrod",
  [("«+» qutbga ulangan 2-elektrod", "u anod — oksidlanish boradi"),
   ("ikkalasi ham katod", "zanjirda bitta katod, bitta anod bo'ladi"),
   ("elektrolitga chuqurroq tushgani", "chuqurlik ahamiyatsiz — qutb muhim")],
  "Katod — manbaning manfiy qutbiga ulangan elektrod; rasmda 1-elektrod.",
  dict(arch="sxema_oqish"), fig="cell")

# 29 (3) — parametrli: elektrokimyoviy ekvivalent
q(3, "yuqori",
  "Molyar massasi M bo'lgan n valentli metall tuzining eritmasidan 1 F zaryad o'tганda katodda "
  "ajraladigan metall massasi qaysi ifoda bilan topiladi?",
  "M/n", [("M·n", "valentlikka bo'linadi, ko'paytirilmaydi"), ("n/M", "teskari kasr"),
           ("M/(2n)", "2 koeffitsiyenti asossiz")],
  "1 F = 1 mol e → metall (Meⁿ⁺+ne) dan 1/n mol ajraladi → massasi M/n g.",
  dict(arch="parametrli_ekvivalent"))

# 30 (2) — suv elektrolizi nisbati
q(2, "yuqori",
  "Suv elektroliz qilinganda katod va anodda ajralgan gazlarning hajm nisbati (n.sh.) qanday bo'ladi?",
  "2 : 1 (H₂ : O₂)",
  [("1 : 2 (H₂ : O₂)", "vodorod ikki barobar KO'P ajraladi"),
   ("1 : 1", "2H₂O → 2H₂ + O₂ — nisbat teng emas"),
   ("3 : 1", "suvda H:O atom nisbati emas, mol nisbat olinadi")],
  "2H₂O → 2H₂ + O₂: har 2 mol vodorodga 1 mol kislorod.",
  dict(arch="suv_nisbat"))

# 31 (3) — jami gaz hajmi
check("q31", (0.6/2 + 0.6/4)*22.4, 10.08)
q(3, "yuqori",
  "Na₂SO₄ eritmasidan (amalda suv elektrolizi) 0,6 F zaryad o'tkazildi. Ikkala elektrodda ajralgan "
  "gazlarning UMUMIY hajmini (l, n.sh.) toping.",
  "10,08", [("6,72", "faqat H₂ hisoblangan"), ("3,36", "faqat O₂ hisoblangan"),
             ("13,44", "H₂ ga 1 e xato olingan")],
  "H₂ = 0,6/2 = 0,3 mol; O₂ = 0,6/4 = 0,15 mol → jami 0,45 mol = 10,08 l.",
  dict(arch="jami_gaz"))

# 32 (3) — 1-2-3: Faradey omillari
q(3, "yuqori",
  "Katodda ajralgan modda massasi quyidagilarning qaysilariga BOG'LIQ?\n"
  "1) tok kuchiga;  2) elektroliz vaqtiga;  3) elektrod yuzasiga;  4) metallning molyar massasiga.",
  "1, 2 va 4",
  [("1 va 2", "m = M·I·t/(nF) — molyar massa ham formulada"),
   ("1, 2, 3 va 4", "yuza tezlikni emas, faqat tok zichligini o'zgartiradi — massa Q va M ga bog'liq"),
   ("faqat 4", "zaryad (I·t) asosiy omil")],
  "Faradey qonuni: m = M·I·t/(n·F) — tok, vaqt va M/n ga bog'liq; yuza formulaga kirmaydi.",
  dict(arch="faradey_omillar"))

# ---------- Y2: kumushlash vannasi ----------
check("y2_33", 0.05*108, 5.4)
check("y2_34", 0.05/4*22.4, 0.28)
check("y2_35", 10.8/108, 0.1)
Y2 = dict(
  n=33, tur="Y2", element="I.10",
  ichki_pasport=[dict(n=33, element="I.10", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.10", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.10", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Galvanika sexida buyumlar AgNO₃ eritmasida (inert anod bilan) kumushlanadi. Bitta buyum "
               "uchun vannadan 0,05 F zaryad o'tkaziladi. (M(Ag)=108.) 33–35-savollarga A–F ro'yxatidan "
               "javob tanlang."),
  savollar_ichki=[
    "33. Bitta buyumga o'tirgan kumush massasi (g) qancha?",
    "34. Shu vaqtda anodda ajralgan kislorodning hajmi (l, n.sh.) qancha?",
    "35. 10,8 g kumush o'tirishi uchun necha faradey zaryad kerak bo'ladi?"],
  javoblar_royxati=["A) 5,4", "B) 0,28", "C) 0,1", "D) 10,8", "E) 0,56", "F) 0,05"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="0,1 F uchun massa — 33-savolga xato javob"),
                   dict(variant="E", xato="O₂ ga 2 e deb olish xatosi"),
                   dict(variant="F", xato="zaryadning o'zi — 35 uchun chalg'itadi")],
  yechim=("33: Ag = 0,05 mol → 5,4 g (A). 34: O₂ = 0,05/4 = 0,0125 mol → 0,28 l (B). "
          "35: 10,8/108 = 0,1 F (C)."),
  parametrlar=dict(arch="kumushlash_ssenariy", f=0.05))

# ---------- O1 ----------
check("o37", 0.5/2*22.4, 5.6)
check("o38", 4/2*64, 128)
check("o39", 5*3860/96500*108, 21.6)
check("o40", 2.7/27*3, 0.3)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="KCl suyuqlanmasi elektroliz qilinganda katodda qaysi modda ajraladi?",
      javob="K (kaliy)", yechim="Suyuqlanmada suv yo'q: K⁺ + e → K.",
      parametrlar=dict(arch="suyuqlanma_o1")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="NaCl ning mo'l eritmasidan 0,5 F zaryad o'tkazilganda anodda ajralgan gazning hajmini "
            "(l, n.sh.) toping.",
      javob="5,6", yechim="Cl₂ = 0,5/2 = 0,25 mol → 5,6 l.",
      parametrlar=dict(arch="cl2_o1")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="CuSO₄ ning mo'l eritmasidan 4 F zaryad o'tkazilganda katodda ajralgan misning massasini (g) toping.",
      javob="128", yechim="Cu = 4/2 = 2 mol → 128 g.",
      parametrlar=dict(arch="cu_o1")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="AgNO₃ ning mo'l eritmasi 5 A tok bilan 3860 s elektroliz qilindi. Katodda ajralgan kumushning "
            "massasini (g) toping. (F=96500 C/mol, M(Ag)=108)",
      javob="21,6", yechim="Q = 5·3860 = 19300 C = 0,2 F → Ag = 0,2 mol → 21,6 g.",
      parametrlar=dict(arch="it_hisob")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="Suyuqlanmadan 2,7 g alyuminiy olish uchun necha faradey zaryad o'tkazish kerak? (M(Al)=27)",
      javob="0,3", yechim="n(Al) = 0,1 mol → Q = 0,1·3 = 0,3 F.",
      parametrlar=dict(arch="teskari_f")),
]

# ---------- O2 ----------
check("o41b", 0.2*64 + (0.5-0.4)/2*2, 12.9)
check("o41c", 0.5/4*22.4, 2.8)
check("o41d", 12.9 + 0.5/4*32, 16.9)
check("o43b", 0.1/2*64, 3.2)
check("o43c", 0.1/3*27, 0.9)
O2 = [
 dict(n=41, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("0,2 kg 16 % li CuSO₄ eritmasidan (inert elektrodlar) 0,5 F zaryad o'tkazildi. "
            "Bandlar ketma-ket yechiladi. (M(CuSO₄)=160, M(Cu)=64)"),
      bandlar=[
        dict(savol="a) Katod va anoddagi jarayonlarning tenglamalarini yozing (ikkala bosqich uchun).",
             yechim=["Katod: Cu²⁺+2e→Cu, so'ng 2H₂O+2e→H₂+2OH⁻; anod: 2H₂O−4e→O₂+4H⁺"], M=3, A=1),
        dict(savol="b) Katodda ajralgan moddalarning umumiy massasini toping.",
             yechim=["Cu²⁺ = 32/160 = 0,2 mol → 0,4 F sarflaydi (12,8 g). Qolgan 0,1 F → H₂ 0,05 mol (0,1 g).",
                     "Jami 12,9 g"], M=4, A=3),
        dict(savol="c) Anodda ajralgan gazning hajmini (l, n.sh.) toping.",
             yechim=["O₂ = 0,5/4 = 0,125 mol → 2,8 l"], M=3, A=2),
        dict(savol="d) Eritma massasi necha grammga kamayganini hisoblang.",
             yechim=["12,9 + 0,125·32 = 12,9 + 4 = 16,9 g"], M=2, A=2),
        dict(savol="e) Nega 0,4 F dan keyin katodda vodorod ajrala boshladi? Izohlang.",
             yechim=["Cu²⁺ ionlari tugadi — endi katodda navbatdagi zarracha, ya'ni suv qaytariladi."], M=3, A=2),
      ],
      rasmiylashtirish="Ikki bosqichli katod zanjiri: tenglamalar → massa → hajm → balans → izoh; M15+A10.",
      parametrlar=dict(arch="cuso4_zanjir", m=200, w=16, f=0.5)),
 dict(n=42, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Sxemadagi X₁, X₂, X₃ moddalarni aniqlab, quyidagilarni bajaring:\n"
            "NaCl(suyuqlanma) —elektroliz→ X₁(metall) + X₂(gaz);  X₁ + H₂O → X₃ + H₂↑"),
      bandlar=[
        dict(savol="a) X₁, X₂, X₃ ni aniqlab, ikkala reaksiya tenglamasini yozing (elektrod jarayonlari bilan).",
             yechim=["X₁=Na, X₂=Cl₂, X₃=NaOH. 2NaCl →(el-z) 2Na + Cl₂ (katod: Na⁺+e→Na; anod: 2Cl⁻−2e→Cl₂);",
                     "2Na + 2H₂O → 2NaOH + H₂"], M=13, A=0),
        dict(savol="b) NaCl ERITMASI elektrolizi suyuqlanmadan nimasi bilan farq qiladi? Tenglama bilan ko'rsating.",
             yechim=["Eritmada katodda suv qaytariladi: 2NaCl+2H₂O → 2NaOH+H₂+Cl₂ — natriy metall holida ajralmaydi."], M=9, A=0),
        dict(savol="c) Nega natriy metallini eritma elektrolizidan olib bo'lmaydi?",
             yechim=["Na juda aktiv: uning ioni o'rniga suv oson qaytariladi (ajralgan Na suv bilan darhol reaksiyaga kirishardi)."], M=3, A=0),
      ],
      rasmiylashtirish="Sxema-zanjir formati (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="nacl_sxema")),
 dict(n=43, tur="O2", element="I.10", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uchta elektroliz vannasi KETMA-KET ulangan; ularda mos ravishda AgNO₃, CuSO₄ eritmalari va "
            "Al₂O₃ suyuqlanmasi bor. Zanjirdan 0,1 F zaryad o'tdi; katodlarda ajralgan massalar "
            "diagrammada ko'rsatilgan (2- va 3-vannalar «?»). Bandlar ketma-ket yechiladi. "
            "(M(Ag)=108, M(Cu)=64, M(Al)=27)"),
      fig="bar_vanna",
      bandlar=[
        dict(savol="a) Nega ketma-ket ulangan vannalardan bir xil zaryad o'tadi?",
             yechim=["Ketma-ket zanjirda tok kuchi (va vaqt) barcha uchastkalarda bir xil → Q = I·t ham bir xil."], M=3, A=1),
        dict(savol="b) 2-vannadagi mis massasini hisoblang.",
             yechim=["Cu = 0,1/2 = 0,05 mol → 3,2 g"], M=4, A=3),
        dict(savol="c) 3-vannadagi alyuminiy massasini hisoblang.",
             yechim=["Al = 0,1/3 mol → 0,9 g"], M=4, A=3),
        dict(savol="d) Natijalarni solishtirib xulosa chiqaring: bir xil zaryadda massa nimaga proporsional?",
             yechim=["m ~ M/n (elektrokimyoviy ekvivalent): Ag(108/1) > Cu(64/2) > Al(27/3)."], M=4, A=3),
      ],
      rasmiylashtirish="Jadval-tahlil (ketma-ket vannalar): M15+A10.",
      parametrlar=dict(arch="vanna_jadval", f=0.1)),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261025)
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
    variant="mavzu-I10-B", daraja="B", bob=10, bob_nomi="Elektroliz",
    manba=("Tongotarov elektroliz banki (2019-2021) arxetiplari — javoblar mustaqil qayta hisoblangan; "
           "MS spetsifikatsiyasi I.10"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: Faradey hisoblari, ikki bosqichli katod, teskari X% "
          "masalalar, 1-2-3 tanlovlar, grafik-jadval savollar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.10") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
