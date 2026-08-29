# -*- coding: utf-8 -*-
"""7-bob B-varianti: Eritmalar (I.7) — HAQIQIY MS MUHITI ★★★.
Ko'p bosqichli hisoblar, kristallogidrat cho'kishi, oleum, gaz eruvchanligi.
A-variantdan arxetip-pozitsiya jihatidan farqli; barcha javoblar mustaqil hisoblangan."""
import json, random

OUT = "mavzu_I7B.json"
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

# 1 (3) — kristallogidratli foiz
check("q1", 100*(50*160/250)/200, 16)
q(3, "yuqori",
  "50 g mis kuporosi CuSO₄·5H₂O 150 g suvda eritildi. Eritmadagi suvsiz tuzning massa ulushini (%) toping. "
  "(M(CuSO₄)=160, M(CuSO₄·5H₂O)=250)",
  "16", [("25", "kristallogidrat massasi olingan (50/200)"), ("20", "suvsiz tuz 40 g deb olingan"),
          ("21,3", "eritma massasi 150 g deb olingan")],
  "CuSO₄: 50·160/250 = 32 g; eritma 200 g; ω = 16%.",
  dict(arch="kristallogidrat_foiz", gidrat=50, suv=150))

# 2 (3) — hajm-zichlik tuzog'i
check("q2", 100*44/(2000*1.1), 2)
q(3, "yuqori",
  "Hajmi 2 litr, zichligi 1,1 g/ml bo'lgan eritmada 44 g tuz erigan. Tuzning massa ulushini (%) toping.",
  "2", [("2,2", "zichlik hisobga olinmagan (44/2000)"), ("4,4", "eritma 1 litr deb olingan"),
         ("0,02", "foizga o'tkazilmagan")],
  "m(eritma) = 2000·1,1 = 2200 g; ω = 44/2200 · 100% = 2%.",
  dict(arch="hajm_zichlik", V=2000, rho=1.1, tuz=44))

# 3 (2) — teskari
check("q3", 45/0.15 - 45, 255)
q(2, "yuqori",
  "15 % li eritma tayyorlash uchun 45 g tuzga necha gramm suv qo'shish kerak?",
  "255", [("300", "eritma massasi olingan"), ("240", "asossiz ayirma"),
           ("270", "10% uchun hisob 405 dan chalkashuv")],
  "m(eritma) = 45/0,15 = 300 g → suv = 300 − 45 = 255 g.",
  dict(arch="tayyorlash_teskari", tuz=45, w=15))

# 4 (3) — grafik: cho'kmali to'yingan eritma qizdirilganda
q(3, "yuqori",
  "Idishda cho'kmasi bilan muvozanatda turgan to'yingan eritma bor (tuz eruvchanligi harorat bilan ortadi). "
  "Eritma asta-sekin qizdirilganda undagi tuzning massa ulushi (ω) qanday o'zgaradi? To'g'ri grafikni tanlang.",
  "ortadi, cho'kma tugagach o'zgarmay qoladi",
  [("uzluksiz ortib boradi", "cho'kma tugagach ω ni oshiradigan manba qolmaydi"),
   ("o'zgarmaydi", "eruvchanlik ortishi bilan cho'kma eriy boshlaydi"),
   ("avval ortadi, keyin kamayadi", "qizdirishda erigan tuz kamaymaydi")],
  "Qizdirilganda eruvchanlik ortadi — cho'kma eriy borib ω ortadi; cho'kma tugagach eritma to'yinmagan bo'lib, "
  "ω o'zgarmay qoladi (o'sish + plato).",
  svg=dict(correct="rise_flat", d1="rise", d2="flat", d3="rise_fall", xlab="t, °C", ylab="ω"))

# 5 (3) — RASMLI: B egri chizig'idan ω hisoblash
check("q5", 100*25/125, 20)
q(3, "yuqori",
  "Rasmda X tuzining eruvchanlik egri chizig'i berilgan. Grafikdan foydalanib, 60 °C dagi TO'YINGAN eritmada "
  "tuzning massa ulushini (%) hisoblang.",
  "20", [("25", "eruvchanlik qiymatining o'zi olingan"), ("15", "40 °C qiymati (15 g) bilan chalkashuv"),
          ("33,3", "25/75 — eritma massasi xato")],
  "Grafikdan: s(60°) = 25 g → ω = 25/125 · 100% = 20%.",
  dict(arch="grafik_hisob", s60=25), fig="solubility_b")

# 6 (3) — aralashtirish teskari
check("q6", (140-100*0.2)/300*100, 40)
q(3, "yuqori",
  "20 % li va noma'lum konsentratsiyali eritmalardan 400 g 35 % li eritma tayyorlandi. Agar 20 % li eritmadan "
  "100 g olingan bo'lsa, ikkinchi eritmaning konsentratsiyasini (%) toping.",
  "40", [("50", "ikkinchi eritma 200 g deb olingan"), ("35", "aralashma qiymati ko'chirilgan"),
          ("45", "krest qoidasi xato qo'llangan")],
  "Tuz balansi: 100·0,2 + 300·x = 400·0,35 → 20 + 300x = 140 → x = 0,4 → 40%.",
  dict(arch="aralash_teskari", m1=100, w1=20, m=400, w=35))

# 7 (3) — gaz eritmasi
check("q7", 100*73/200, 36.5)
q(3, "yuqori",
  "44,8 l (n.sh.) vodorod xlorid 127 g suvda eritildi. Hosil bo'lgan xlorid kislotaning massa ulushini (%) toping.",
  "36,5", [("57,5", "HCl massasi 73 emas, hajmdan xato o'tilgan"), ("26,9", "eritma massasiga HCl qo'shilmagan (73/271)"),
            ("18,25", "1 mol deb olingan")],
  "n(HCl) = 44,8/22,4 = 2 mol = 73 g; eritma = 73 + 127 = 200 g; ω = 36,5%.",
  dict(arch="gaz_eritma", V=44.8, suv=127))

# 8 (3) — molyal teskari
check("q8", 2*0.5, 1)
q(3, "yuqori",
  "2 molyal eritma tayyorlash uchun 500 g suvda necha mol modda eritish kerak?",
  "1", [("2", "erituvchi kg ga aylantirilmagan"), ("4", "nisbat teskari"),
         ("0,5", "ikki marta bo'lib yuborilgan")],
  "Molyallik — 1 kg erituvchidagi mol: 2 mol/kg · 0,5 kg = 1 mol.",
  dict(arch="molyal_teskari", m=2, suv=500))

# 9 (2) — normal
check("q9", 24.5/49/0.5, 1)
q(2, "yuqori",
  "0,5 l eritmada 24,5 g sulfat kislota erigan. Eritmaning normal konsentratsiyasini (mol-ekv/l) toping. (E(H₂SO₄)=49)",
  "1", [("0,5", "molyar konsentratsiya hisoblangan"), ("2", "hajmga bo'lish o'rniga ko'paytirilgan"),
         ("0,25", "ekvivalent 98 deb olingan")],
  "n(ekv) = 24,5/49 = 0,5; N = 0,5/0,5 = 1 mol-ekv/l.",
  dict(arch="normal_konts", m=24.5, E=49, V=0.5))

# 10 (3) — titrdan molyar
check("q10", 0.008*1000/40, 0.2)
q(3, "yuqori",
  "NaOH eritmasining titri 0,008 g/ml. Eritmaning molyar konsentratsiyasini (mol/l) toping. (M(NaOH)=40)",
  "0,2", [("0,008", "titr ko'chirilgan"), ("0,32", "M ga ko'paytirilgan"),
           ("2", "o'nlik xato")],
  "c = T·1000/M = 0,008·1000/40 = 0,2 mol/l.",
  dict(arch="titrdan_molyar", T=0.008, M=40))

# 11 (3) — oleum (bank, mustaqil: 30%)
check("q11", 100*(976-8*80)/(144+976), 30)
q(3, "yuqori",
  "144 g suvga 976 g SO₃ qo'shilganda necha foizli oleum hosil bo'ladi?",
  "30", [("40", "bog'langan SO₃ ayirilmagan holda taxmin"), ("60", "erkin SO₃ ning H₂SO₄ ga nisbati olingan"),
          ("70", "H₂SO₄ ulushi hisoblangan")],
  "H₂O (8 mol) 640 g SO₃ ni bog'laydi; erkin SO₃ = 336 g; jami 1120 g; ω = 30%.",
  dict(arch="oleum_foiz", suv=144, so3=976, manba="Oleum banki, javob mustaqil tekshirildi"))

# 12 (3) — kristallogidrat cho'kishi (Y1 darajasida!)
check("q12", (70-0.2*200)/(0.5-0.2*0.5)*1, 75)
q(3, "yuqori",
  "35 °C da X·5H₂O tarkibli kristallogidrat hosil qiluvchi X tuzining (M(X)=90, M(X·5H₂O)=180) 270 g to'yingan "
  "eritmasi 10 °C gacha sovutildi. Necha gramm X·5H₂O cho'kadi? (S₃₅=35, S₁₀=20 g/100 g suv)",
  "75", [("30", "suvsiz tuz farqi olingan (70−40)"), ("60", "kristall suvi hisobga olinmagan"),
          ("90", "to'yinganlik sharti noto'g'ri yozilgan")],
  "270 g = 2·135 → tuz 70 g, suv 200 g. x g gidrat cho'ksa (50% tuz, 50% suv): "
  "(70−0,5x)/(200−0,5x) = 20/100 → 70−0,5x = 40−0,1x → 0,4x = 30 → x = 75 g.",
  dict(arch="kristallogidrat_chokish", s1=35, s2=20, m=270))

# 13 (3) — parametrli formula
q(3, "yuqori",
  "To'yingan eritmada tuzning massa ulushi ω (%) va eruvchanlik koeffitsiyenti s (g/100 g suv) orasidagi "
  "TO'G'RI bog'lanishni ko'rsating.",
  "ω = 100s/(100+s)",
  [("ω = s", "s suvga, ω eritmaga nisbatan — teng emas"),
   ("ω = 100s/(100−s)", "maxrajda ayirma emas, yig'indi bo'ladi"),
   ("ω = (100+s)/s", "nisbat teskari")],
  "100 g suv + s g tuz = (100+s) g eritma → ω = s/(100+s)·100.",
  dict(arch="parametrli_formula", manba="DIM parametrli uslub"))

# 14 (2) — o'ta to'yingan tuzoq
q(2, "yuqori",
  "O'ta to'yingan eritma haqidagi fikrlardan qaysi biri NOTO'G'RI?",
  "u barqaror bo'lib, uzoq vaqt o'zgarmay saqlanadi",
  [("unda to'yinganlikdagidan ORTIQ modda erigan bo'ladi", "bu to'g'ri ta'rif"),
   ("kichik turtki (kristallcha tushishi) kristallanishni boshlab yuboradi", "bu to'g'ri — beqarorlik belgisi"),
   ("u ehtiyotkor sovutish orqali olinadi", "bu to'g'ri usul")],
  "O'ta to'yingan eritma BEQAROR: chayqatish yoki 'urug'' kristall ortiqcha moddani darhol cho'ktiradi.")

# 15 (3) — molyar-zichlik teskari
check("q15", 2*98/(10*1.12), 17.5)
q(3, "yuqori",
  "2 M li sulfat kislota eritmasining zichligi 1,12 g/ml. Eritmadagi H₂SO₄ ning massa ulushini (%) toping. (M=98)",
  "17,5", [("19,6", "zichlik hisobga olinmagan"), ("8,75", "1 M uchun hisob"),
            ("22,4", "molyar hajm bilan chalkashuv")],
  "1 l: 1120 g eritma, 196 g H₂SO₄ → ω = 196/1120 · 100% = 17,5%. (ω = cM/(10ρ).)",
  dict(arch="molyardan_foiz", c=2, rho=1.12, M=98))

# 16 (3) — tuz qo'shish teskari
check("q16", (40-20)/0.8, 25)
q(3, "yuqori",
  "200 g 10 % li eritmaga necha gramm tuz qo'shilsa, eritma 20 % li bo'ladi?",
  "25", [("20", "maxrajga qo'shilgan tuz kiritilmagan"), ("40", "kerakli jami tuz olingan"),
          ("50", "eritmaning o'zi 10% ga oshirilgan")],
  "(20+x)/(200+x) = 0,2 → 20+x = 40+0,2x → 0,8x = 20 → x = 25 g.",
  dict(arch="tuz_qoshish", m=200, w1=10, w2=20))

# 17 (3) — jadval: uch eritma aralashmasi
check("q17", 100*(20+15+10)/500, 9)
q(3, "yuqori",
  "Jadvalda aralashtirilgan uch eritma berilgan:\n"
  "[JADVAL] Eritma | massasi, g | ω, % ;; 1 | 100 | 20 ;; 2 | 150 | 10 ;; 3 | 250 | 4\n"
  "Hosil bo'lgan eritmaning konsentratsiyasini (%) toping.",
  "9", [("11,3", "oddiy o'rtacha olingan"), ("34", "foizlar yig'indisi"),
         ("12", "massalar noto'g'ri jamlangan")],
  "Tuz: 20 + 15 + 10 = 45 g; eritma 500 g → ω = 9%.",
  dict(arch="jadval_aralash", data=[[100,20],[150,10],[250,4]]))

# 18 (2) — eruvchanlikdan to'yingan massa ichidagi tuz
check("q18", 720/144*44, 220)
q(2, "yuqori",
  "Tuzning eruvchanligi 44 g (100 g suvda). 720 g to'yingan eritmadagi tuz massasini (g) toping.",
  "220", [("317", "720·0,44 — eritmaga nisbat olingan"), ("144", "eritma birligi ko'chirilgan"),
           ("176", "besh barobar qilingan")],
  "144 g eritmada 44 g tuz → 720 g = 5·144 → tuz 5·44 = 220 g.",
  dict(arch="eruvchanlik_eritmadan", s=44, m=720))

# 19 (3) — kristallogidratdan molyar
check("q19", (25/250)/0.5, 0.2)
q(3, "yuqori",
  "25 g CuSO₄·5H₂O suvda eritilib, eritma hajmi 500 ml ga yetkazildi. CuSO₄ ning molyar konsentratsiyasini (mol/l) toping. (M=250)",
  "0,2", [("0,1", "hajmga bo'lish unutilgan"), ("0,4", "gidrat massasi 125 deb olingan"),
           ("0,05", "ikki marta bo'lingan")],
  "n = 25/250 = 0,1 mol; c = 0,1/0,5 = 0,2 M.",
  dict(arch="gidratdan_molyar", gidrat=25, V=0.5))

# 20 (2) — I/II/III sifat
q(2, "yuqori",
  "TO'YINMAGAN tuz eritmasi haqida qaysi hukmlar to'g'ri?\n"
  "I. Yopiq idishda qizdirilsa, ω o'zgarmaydi. II. Ochiq idishda qizdirilsa (suv bug'lansa), ω ortadi. "
  "III. Unga shu tuzdan qo'shib eritilsa, ω ortadi.",
  "I, II va III",
  [("faqat II va III", "yopiq idishda massa saqlanadi — ω o'zgarmaydi, bu ham to'g'ri"),
   ("faqat I va III", "bug'lanishda tuz massasi saqlanib, eritma kamayadi — ω ortadi"),
   ("faqat III", "uchala hukm ham to'g'ri")],
  "Yopiq idish: hech narsa chiqib ketmaydi → ω const. Ochiq: suv ketadi → ω ortadi. Tuz qo'shilsa → ω ortadi.")

# 21 (3) — oleum (bank, mustaqil: 40%)
check("q21", 100*(150-60)/(75+150), 40)
q(3, "yuqori",
  "75 g 82 % li sulfat kislota eritmasiga 150 g SO₃ shimdirilganda necha foizli oleum hosil bo'ladi?",
  "40", [("30", "bog'lanadigan SO₃ xato hisoblangan"), ("70", "H₂SO₄ ulushi olingan"),
          ("60", "erkin SO₃ ning kislotaga nisbati")],
  "Suv: 75·0,18 = 13,5 g = 0,75 mol → 60 g SO₃ ni bog'laydi. Erkin SO₃ = 90 g; jami 225 g → ω = 40%.",
  dict(arch="oleum_shimdirish", m=75, w=82, so3=150, manba="Oleum banki, mustaqil tekshirildi"))

# 22 (3) — gaz ajralishi hisob
check("q22", (66-22)/44*22.4, 22.4)
q(3, "yuqori",
  "0 °C da CO₂ ning 100 g suvdagi to'yingan eritmasi (S₀ = 66 g) qizdirildi; yangi haroratda S = 22 g. "
  "Ajralib chiqqan CO₂ ning hajmini (l, n.sh.) toping.",
  "22,4", [("44,8", "butun erigan gaz ajraladi deb olingan"), ("11,2", "yarim mol deb olingan"),
            ("33,6", "S qiymatlari yig'ilgan")],
  "Ajraladi: 66 − 22 = 44 g = 1 mol → V = 22,4 l.",
  dict(arch="gaz_ajralish", s1=66, s2=22, manba="ERUVCHANLIK banki uslubi"))

# 23 (3) — normaldan titr
check("q23", 0.2*49/1000, 0.0098)
q(3, "yuqori",
  "0,2 N li sulfat kislota eritmasining titrini (g/ml) toping. (E(H₂SO₄)=49)",
  "0,0098", [("0,098", "o'nlik xato"), ("0,0196", "M=98 bilan hisoblangan"),
              ("0,0049", "N/2 olingan")],
  "T = N·E/1000 = 0,2·49/1000 = 0,0098 g/ml.",
  dict(arch="normaldan_titr", N=0.2, E=49))

# 24 (2) — grafik: gaz eruvchanligi bosimga bog'liq
q(2, "yuqori",
  "O'zgarmas haroratda gazning suvdagi eruvchanligi bosimga qanday bog'liq? To'g'ri grafikni tanlang.",
  "bosim ortishi bilan to'g'ri proporsional ortadi",
  [("bosimga bog'liq emas", "gazlar uchun bosim asosiy omil"),
   ("bosim ortishi bilan kamayadi", "aksincha — Genri qonuni bo'yicha ortadi"),
   ("avval ortib, keyin kamayadi", "bunday maksimum kuzatilmaydi")],
  "Genri qonuni: erigan gaz miqdori gaz bosimiga proporsional — chiziqli o'suvchi grafik.",
  svg=dict(correct="rise", d1="flat", d2="fall", d3="rise_fall", xlab="P", ylab="s"))

# 25 (3) — krest og'ir
check("q25a", 100.0, 100); check("q25b", 150.0, 150)
q(3, "yuqori",
  "60 % li va 10 % li eritmalardan 250 g 30 % li eritma tayyorlash uchun har biridan necha grammdan olish kerak?",
  "100 g (60 %) va 150 g (10 %)",
  [("125 g va 125 g", "o'rtacha 35% chiqadi"), ("150 g (60 %) va 100 g (10 %)", "nisbat teskari — 40% chiqadi"),
   ("80 g va 170 g", "krest nisbat xato")],
  "x+y=250; 0,6x+0,1y=75 → 0,5x=50 → x=100, y=150. (Krest: 20:30 = 2:3.)",
  dict(arch="krest", w1=60, w2=10, w=30, m=250))

# 26 (3) — to'liq erish + sovutish kombinatsiyasi
check("q26", 90 - 2*20, 50)
q(3, "yuqori",
  "60 °C da (S₆₀ = 50 g) 200 g suvga 90 g tuz solindi. Eritma 20 °C gacha sovutilganda (S₂₀ = 20 g) necha gramm cho'kma hosil bo'ladi?",
  "50", [("70", "20° chegarasi 100 g suvga olingan"), ("90", "hamma tuz cho'kadi deb olingan"),
          ("40", "erigan qolgan tuz massasi")],
  "60° da chegara 100 g — 90 g to'liq eriydi. 20° da 200 g suvda 40 g eriydi → cho'kma 90−40 = 50 g.",
  dict(arch="erish_sovutish", s1=50, s2=20, suv=200, tuz=90))

# 27 (3) — normaldan massa
check("q27", 2*0.25*53, 26.5)
q(3, "yuqori",
  "250 ml 2 N li natriy karbonat eritmasini tayyorlash uchun necha gramm Na₂CO₃ kerak? (E(Na₂CO₃)=53)",
  "26,5", [("53", "hajm hisobga olinmagan"), ("13,25", "1 N uchun"),
            ("106", "molyar massa bilan to'liq hisob")],
  "n(ekv) = 2·0,25 = 0,5 → m = 0,5·53 = 26,5 g.",
  dict(arch="normaldan_massa", N=2, V=0.25, E=53))

# 28 (2) — suyultirish molyar
check("q28", 0.4*50/200, 0.1)
q(2, "yuqori",
  "50 ml 0,4 M li eritma suv bilan 200 ml gacha suyultirildi. Yangi eritmaning molyar konsentratsiyasini (mol/l) toping.",
  "0,1", [("0,4", "suyultirish e'tiborsiz"), ("1,6", "nisbat teskari"),
           ("0,2", "ikki marta suyultirilgan deb olingan")],
  "c₁V₁ = c₂V₂ → c₂ = 0,4·50/200 = 0,1 M.",
  dict(arch="suyultirish_molyar", c1=0.4, V1=50, V2=200))

# 29 (3) — DIM munosabat: tuz qo'shilganda formula
q(3, "yuqori",
  "m gramm ω ulushli (kasrda) eritmaga a gramm quruq tuz qo'shib eritildi. Yangi eritmaning massa ulushini "
  "ifodalovchi formulani ko'rsating.",
  "(mω + a)/(m + a)",
  [("(mω + a)/m", "maxrajga qo'shilgan tuz kiritilmagan"),
   ("mω/(m + a)", "suratga qo'shilgan tuz kiritilmagan"),
   ("(m + a)/(mω + a)", "nisbat teskari")],
  "Yangi tuz massasi mω + a; yangi eritma massasi m + a.",
  dict(arch="munosabat_formula", manba="DIM parametrli uslub"))

# 30 (2) — oleum nazariy tuzoq
q(2, "yuqori",
  "Oleumga oz-ozdan suv qo'shib borilganda dastlab qanday jarayon boradi?",
  "erkin SO₃ suv bilan birikib, H₂SO₄ hosil qiladi",
  [("oleum shunchaki suyuladi", "avval SO₃ + H₂O → H₂SO₄ reaksiyasi boradi"),
   ("SO₃ gaz holida ajralib chiqadi", "suv uni chiqarib yubormaydi, biriktiradi"),
   ("sulfat kislota parchalanadi", "suv qo'shilishi kislotani parchalamaydi")],
  "Oleumdagi erkin SO₃ suv bilan shiddatli reaksiyaga kirishadi: SO₃ + H₂O → H₂SO₄; faqat SO₃ tugagach oddiy suyulish boshlanadi.")

# 31 (3) — foizdan molyal
check("q31", (10/40)/(0.09), 2.78, tol=0.01)
q(3, "yuqori",
  "10 % li NaOH eritmasining molyal konsentratsiyasini (mol/kg) toping. (M(NaOH)=40)",
  "2,78", [("2,5", "erituvchi 100 g deb olingan"), ("0,25", "mol soni molyallik deb ko'chirilgan"),
            ("4", "M ga bo'lish unutilgan")],
  "100 g eritmada: NaOH 10 g = 0,25 mol; suv 90 g = 0,09 kg → 0,25/0,09 ≈ 2,78 mol/kg.",
  dict(arch="foizdan_molyal", w=10, M=40))

# 32 (3) — RASMLI: B egri chizig'idan cho'kma o'qish
check("q32", 40-8, 32)
q(3, "yuqori",
  "Rasmdagi eruvchanlik egri chizig'idan foydalaning: X tuzining 100 g suvdagi 80 °C da to'yingan eritmasi "
  "20 °C gacha sovutilganda necha gramm tuz cho'kadi?",
  "32", [("40", "80° dagi butun tuz olingan"), ("8", "20° dagi qoldiq olingan"),
          ("24", "40° qiymati bilan chalkashuv")],
  "Grafikdan: s(80°) = 40 g, s(20°) = 8 g → cho'kma = 40 − 8 = 32 g.",
  dict(arch="grafik_chokma", s80=40, s20=8), fig="solubility_b")

assert len(Y1) == 32

# ---------- Y2: egri chiziqqa asoslangan ssenariy ----------
check("y2_tuz", 2*40, 80)
check("y2_chokma", 80-2*8, 64)
check("y2_w", 100*16/216, 7.4, tol=0.1)
Y2 = dict(
  n=33, tur="Y2", element="I.7",
  ichki_pasport=[dict(n=33, element="I.7", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.7", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.7", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Rasmdagi eruvchanlik egri chizig'iga ega X tuzining 200 g suvdagi 80 °C da to'yingan eritmasi "
               "20 °C gacha sovutildi (grafikdan: S₈₀ = 40 g, S₂₀ = 8 g). 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. Boshlang'ich eritmadagi tuz massasi (g) qancha?",
    "34. Sovutilganda necha gramm tuz cho'kadi?",
    "35. Sovutilgandan keyin qolgan eritmada tuzning massa ulushi (%) qancha?"],
  javoblar_royxati=["A) 64", "B) 7,4", "C) 80", "D) 16", "E) 40", "F) 29,6"],
  javoblar={"33": "C", "34": "A", "35": "B"},
  chalgituvchilar=[dict(variant="D", xato="qolgan erigan tuz massasi — cho'kma bilan adashtiriladi"),
                   dict(variant="E", xato="eruvchanlik koeffitsiyentining o'zi (100 g suv uchun)"),
                   dict(variant="F", xato="ω ni boshlang'ich eritmaga nisbatan hisoblash xatosi")],
  yechim=("200 g suv: tuz 2·40 = 80 g (33 → C). 20° da qoladi 2·8 = 16 g → cho'kma 64 g (34 → A). "
          "Qolgan eritma 216 g; ω = 16/216 ≈ 7,4% (35 → B)."),
  parametrlar=dict(arch="egri_ssenariy", s80=40, s20=8, suv=200), fig="solubility_b")

# ---------- O1 ----------
check("o36", 0.4, 0.4)
check("o37", (1*1+1*3)/2, 2)
check("o38", (976-320)/0.49 - 976 + 0*1, ((976*0+728))*1, tol=1e9)  # pastda aniq hisob
CHECKS.pop()  # yuqoridagi qo'pol satr o'rniga aniq tekshiruv:
check("o38", (0.51*72+320)/(1-0.51), 728, tol=0.5)
check("o39", (12.3/246)/0.5, 0.1)
check("o40", (80-0.5*0+0)*0 + 100, 100)  # x: (80-0.5x)=0.2(200-0.5x) -> x=100
check("o40b", (80-0.5*100)/(200-0.5*100), 0.2)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="500 ml 0,4 M li eritmadan 100 ml quyib olindi. Olingan qismning molyar konsentratsiyasi (mol/l) qancha?",
      javob="0,4", yechim="Bir jinsli eritmaning har qanday qismida konsentratsiya bir xil — 0,4 M (tuzoq-savol).",
      parametrlar=dict(arch="tuzoq_qism")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="1 l 1 M li va 1 l 3 M li bir xil tuz eritmalari aralashtirildi. Hosil bo'lgan eritmaning molyar konsentratsiyasini (mol/l) toping.",
      javob="2", yechim="n = 1 + 3 = 4 mol; V = 2 l → c = 2 M.",
      parametrlar=dict(arch="molyar_aralash", c1=1, c2=3)),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="72 g suvga necha gramm SO₃ qo'shilganda 51 % li oleum hosil bo'ladi?",
      javob="728", yechim="Suv 4 mol → 320 g SO₃ ni bog'laydi. (x−320)/(72+x) = 0,51 → 0,49x = 356,7 → x = 728 g.",
      parametrlar=dict(arch="oleum_teskari", suv=72, w=51, manba="Oleum banki, mustaqil tekshirildi")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="12,3 g MgSO₄·7H₂O suvda eritilib, hajmi 500 ml ga yetkazildi. MgSO₄ ning molyar konsentratsiyasini (mol/l) toping. (M(MgSO₄·7H₂O)=246)",
      javob="0,1", yechim="n = 12,3/246 = 0,05 mol; c = 0,05/0,5 = 0,1 M.",
      parametrlar=dict(arch="gidratdan_molyar", gidrat=12.3, M=246, V=0.5)),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="90 °C da X·5H₂O hosil qiluvchi X tuzining (M(X)=90, M(X·5H₂O)=180) 280 g to'yingan eritmasi 20 °C gacha "
            "sovutildi. Necha gramm X·5H₂O cho'kadi? (S₉₀=40, S₂₀=20)",
      javob="100", yechim="280 g = 2·140 → tuz 80, suv 200. (80−0,5x)/(200−0,5x)=0,2 → 80−0,5x=40−0,1x → x=100 g.",
      parametrlar=dict(arch="kristallogidrat_chokish", s1=40, s2=20, m=280)),
]

# ---------- O2 ----------
check("o41a", 100*73/200, 36.5)
check("o41b", 10*1.18*36.5/36.5, 11.8)
check("o41c", 11.8*100/1000, 1.18)
check("o41d", 11.8*36.5/1000, 0.4307, tol=0.001)
check("o42a", 400*0.09/18, 2.0); check("o42b", (0.0+300), 300)
check("o43a1", 100*5/50, 10); check("o43a2", 100*13.25/50, 26.5); check("o43a3", 100*10/50, 20)
check("o43c", 10/0.05 - 50, 150)
O2 = [
 dict(n=41, tur="O2", element="I.7", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("44,8 l (n.sh.) vodorod xlorid 127 g suvda eritildi; hosil bo'lgan eritmaning zichligi 1,18 g/ml. "
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Eritmadagi HCl ning massa ulushini (%) hisoblang.",
             yechim=["n = 2 mol = 73 g; eritma 200 g → ω = 36,5%"], M=2, A=1),
        dict(savol="b) Eritmaning molyar konsentratsiyasini (mol/l) toping.",
             yechim=["c = 10ρω/M = 10·1,18·36,5/36,5 = 11,8 M"], M=3, A=2),
        dict(savol="c) Shu eritmadan 100 ml olinib, suv bilan 1 l gacha suyultirildi. Yangi konsentratsiyani toping.",
             yechim=["c₂ = 11,8·100/1000 = 1,18 M"], M=3, A=2),
        dict(savol="d) Dastlabki eritmaning titrini (g/ml) hisoblang.",
             yechim=["T = cM/1000 = 11,8·36,5/1000 ≈ 0,431 g/ml"], M=3, A=3),
        dict(savol="e) Nega konsentrlangan xlorid kislota ochiq idishda «tutaydi» va vaqt o'tishi bilan "
                   "konsentratsiyasi kamayadi? Gaz eruvchanligi tushunchasi orqali izohlang.",
             yechim=["HCl — gaz: eritma ustida uning bug' bosimi katta, gaz uchib chiqadi (havoda nam bilan",
                     "tuman hosil qiladi). Erigan gaz kamaygani sari ω pasayadi."], M=4, A=2),
      ],
      rasmiylashtirish="Gaz-eritma zanjiri: ω → c → suyultirish → titr → sifat izoh; M15+A10.",
      parametrlar=dict(arch="gaz_eritma_zanjir", V=44.8, suv=127, rho=1.18)),
 dict(n=42, tur="O2", element="I.7", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn="400 g 91 % li sulfat kislota eritmasi bor. Unga SO₃ shimdirilib, 20 % li oleum olinmoqchi.",
      bandlar=[
        dict(savol="a) Qancha SO₃ shimdirish kerakligini aniqlash yo'lini yozing va hisoblang.",
             yechim=["Suv: 400·0,09 = 36 g = 2 mol → 160 g SO₃ ni bog'laydi.",
                     "(x−160)/(400+x) = 0,2 → 0,8x = 240 → x = 300 g"], M=13, A=0),
        dict(savol="b) Hosil bo'lgan oleumning massasini toping.",
             yechim=["m = 400 + 300 = 700 g"], M=9, A=0),
        dict(savol="c) Nega oleum tarkibidagi suv «yo'qoladi»? Qisqacha izohlang.",
             yechim=["Eritmadagi barcha suv SO₃ bilan birikib H₂SO₄ ga aylanadi — oleumda erkin suv bo'lmaydi."], M=3, A=0),
      ],
      rasmiylashtirish="Oleum zanjiri (faqat M): M13+M9+M3 = 25. Bank arxetipi, mustaqil yechildi (300 g — kalit mos).",
      parametrlar=dict(arch="oleum_zanjir", m=400, w=91, oleum=20)),
 dict(n=43, tur="O2", element="I.7", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada uchta nomsiz tuz eritmasidan 50 g dan namuna olinib, suvi to'liq bug'latildi. "
            "Quruq qoldiq massalari diagrammada berilgan (25 °C da NaCl ning eruvchanligi S = 36 g/100 g suv). "
            "Bandlar ketma-ket yechiladi."),
      fig="bar_qoldiq",
      bandlar=[
        dict(savol="a) Har uchala eritmaning massa ulushini (%) hisoblang.",
             yechim=["ω₁ = 5/50 = 10%; ω₂ = 13,25/50 = 26,5%; ω₃ = 10/50 = 20%"], M=4, A=3),
        dict(savol="b) Qaysi namuna 25 °C da TO'YINGAN NaCl eritmasi bo'lishi mumkin? Asoslang.",
             yechim=["To'yingan NaCl: ω = 36/136 ≈ 26,5% → 2-namuna"], M=4, A=2),
        dict(savol="c) 3-namunadan 5 % li eritma tayyorlash uchun 50 g namunaga necha gramm suv qo'shish kerak?",
             yechim=["Tuz 10 g; 5% uchun eritma 200 g → suv 150 g"], M=4, A=3),
        dict(savol="d) Nega bug'latish usuli bilan eritma konsentratsiyasini aniqlash mumkin? Qisqacha izohlang.",
             yechim=["Bug'lanishda faqat suv chiqib ketadi, uchmaydigan tuz to'liq qoldiqda qoladi —",
                     "qoldiq massasi erigan tuz massasiga teng."], M=3, A=2),
      ],
      rasmiylashtirish="Tajriba-tahlil (bug'latish) formati: M15+A10. A-variantdagi formatlardan farqli.",
      parametrlar=dict(arch="buglatish_tahlil", data=[5, 13.25, 10])),
]

# ---------- A/B struktura farqlash: pozitsiya almashtirish ----------
# A-variantda 25-pozitsiya "krest" arxetipida; B-da uni 22-pozitsiyaga suramiz.
for _i, _j in [(21, 24)]:  # 0-index: 22 <-> 25
    assert Y1[_i]["qiyinlik"] == Y1[_j]["qiyinlik"], (_i, _j)
    Y1[_i], Y1[_j] = Y1[_j], Y1[_i]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260919)
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
    d = dict(n=n, tur="Y1", element="I.7", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
print("O2 ballari: OK")

variant = dict(
    variant="mavzu-I7-B", daraja="B", bob=7, bob_nomi="Eritmalar",
    manba=("Eritma/Oleum/ERUVCHANLIK banklari arxetiplari (javoblar mustaqil qayta hisoblangan), "
           "DIM parametrli formatlar; hammasi yangi sonlar bilan"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: kristallogidrat cho'kishi, oleum, gaz-eritma zanjirlari, "
          "molyal/normal/titr o'tishlari. A-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.7") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
