# -*- coding: utf-8 -*-
"""6-bob B-varianti: Kimyoviy muvozanat (I.6) — HAQIQIY MS MUHITI ★★★.
ICE jadvallari, Kc hisoblari, dissotsiatsiya darajasi, kombinatsiyalangan Le Chatelier.
Barcha sonli javoblar mustaqil qayta hisoblangan."""
import json, random

OUT = "mavzu_I6B.json"
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

# 1 (3) — Kc to'g'ridan-to'g'ri hisob
check("q1", 1.2/(0.2*0.3), 20)
q(3, "yuqori",
  "CO(g) + Cl₂(g) ⇌ COCl₂(g) reaksiyasida muvozanat konsentratsiyalari: [CO]=0,2 M, [Cl₂]=0,3 M, "
  "[COCl₂]=1,2 M. Muvozanat konstantasini hisoblang.",
  "20", [("0,05", "teskari nisbat olingan"), ("2", "ko'paytma o'rniga yig'indi bo'lingan"),
          ("7,2", "maxrajda yig'indi olingan (1,2/0,5 xato ko'rinishlari)")],
  "Kc = [COCl₂]/([CO]·[Cl₂]) = 1,2/(0,2·0,3) = 20.",
  dict(arch="kc_hisob", c=[0.2, 0.3, 1.2]))

# 2 (3) — ICE dan Kc
check("q2", 0.6**2/(0.2**2*0.2), 45)
q(3, "yuqori",
  "2SO₂ + O₂ ⇌ 2SO₃ reaksiyasi bo'yicha ma'lumotlar jadvalda berilgan:\n"
  "[JADVAL] Holat | [SO₂], M | [O₂], M | [SO₃], M ;; boshlang'ich | 0,8 | 0,5 | 0 ;; muvozanat | ? | ? | 0,6\n"
  "Muvozanat konstantasini toping.",
  "45", [("11,25", "sarflanish hisobga olinmagan (boshlang'ich qiymatlar bilan)"), ("22,5", "O₂ sarfi 0,6 deb olingan"),
          ("5,6", "SO₃ kvadratga ko'tarilmagan")],
  "Sarflandi: SO₂ 0,6; O₂ 0,3 → muvozanatda [SO₂]=0,2, [O₂]=0,2. Kc = 0,36/(0,04·0,2) = 45.",
  dict(arch="ice_kc", b=[0.8, 0.5], so3=0.6))

# 3 (2) — muvozanatda nima tenglashadi
q(2, "yuqori",
  "Kimyoviy muvozanat qaror topganda quyidagilardan qaysi biri O'ZARO TENGLASHADI?",
  "to'g'ri va teskari reaksiya tezliklari",
  [("reagent va mahsulot konsentratsiyalari", "konsentratsiyalar o'zgarmas, lekin teng bo'lishi shart emas"),
   ("reagent va mahsulot mollari", "mol nisbatlari Kc ga bog'liq, teng emas"),
   ("to'g'ri va teskari reaksiya issiqliklari", "issiqliklar qarama-qarshi ishorali, teng emas")],
  "Muvozanat sharti: v(to'g'ri) = v(teskari). Konsentratsiyalar o'zgarmaydi, ammo o'zaro teng emas.",
  dict(arch="tezlik_teng"))

# 4 (3) — grafik tanlash: teskari reaksiya tezligi
q(3, "yuqori",
  "Yopiq idishga faqat reagentlar solindi. Vaqt o'tishi bilan TESKARI reaksiya tezligi qanday "
  "o'zgaradi? To'g'ri grafikni tanlang.",
  "noldan ortib, muvozanatda o'zgarmay qoladi",
  [("doimiy kamayadi", "bu to'g'ri reaksiya tezligining grafigi emas — teskari 0 dan boshlanadi"),
   ("boshdan o'zgarmas", "mahsulot dastlab yo'q — teskari tezlik 0 dan boshlanadi"),
   ("ortib, keyin kamayadi", "muvozanatda tezlik pasaymaydi, o'zgarmas bo'lib qoladi")],
  "Mahsulot to'plangani sari teskari tezlik 0 dan ortib boradi va muvozanatda platoga chiqadi.",
  svg=dict(correct="rise_flat", d1="fall", d2="flat", d3="rise_fall", xlab="t", ylab="v(tesk)"))

# 5 (3) — RASMLI: c–t grafigidan Kc
check("q5", 0.8**2/0.2, 3.2)
q(3, "yuqori",
  "Rasmda N₂O₄(g) ⇌ 2NO₂(g) reaksiyasi uchun konsentratsiyalarning vaqtga bog'liqligi berilgan. "
  "Grafikdan foydalanib muvozanat konstantasini hisoblang.",
  "3,2", [("4", "[NO₂] kvadratga ko'tarilmagan (0,8/0,2)"), ("1,07", "boshlang'ich 0,6 maxrajda olingan"),
          ("0,31", "teskari nisbat")],
  "Grafikdan: muvozanatda [N₂O₄]=0,2, [NO₂]=0,8. Kc = 0,8²/0,2 = 3,2.",
  dict(arch="grafik_kc", n2o4=[0.6, 0.2], no2=0.8), fig="ct_eq")

# 6 (3) — Kc dan noma'lum konsentratsiya
check("q6", 1*(0.4*0.1)/0.2, 0.2)
q(3, "yuqori",
  "CO + H₂O(g) ⇌ CO₂ + H₂ reaksiyasi uchun Kc = 1. Muvozanatda [CO]=0,4 M, [H₂O]=0,1 M, [CO₂]=0,2 M "
  "bo'lsa, [H₂] ni toping (M).",
  "0,2", [("0,5", "ko'paytirish o'rniga bo'lish xatosi"), ("0,04", "Kc ga bo'linmagan holda ko'paytma"),
           ("0,1", "H₂O qiymati ko'chirilgan")],
  "Kc = [CO₂][H₂]/([CO][H₂O]) → [H₂] = 1·0,4·0,1/0,2 = 0,2 M.",
  dict(arch="kc_teskari", kc=1))

# 7 (3) — dissotsiatsiya darajasidan Kc
check("q7", 0.6**2/1.4, 0.257, tol=0.01)
q(3, "yuqori",
  "PCl₅(g) ⇌ PCl₃(g) + Cl₂(g). Boshlang'ich [PCl₅] = 2 mol/l, dissotsiatsiya darajasi 30 %. "
  "Muvozanat konstantasini hisoblang.",
  "≈0,26", [("0,18", "maxrajda boshlang'ich 2 M olingan"), ("0,6", "muvozanat konsentratsiya ko'chirilgan"),
             ("0,09", "α kvadrati olingan")],
  "Parchalandi 0,6 M → [PCl₃]=[Cl₂]=0,6; [PCl₅]=1,4. Kc = 0,36/1,4 ≈ 0,26.",
  dict(arch="alfa_kc", c0=2, alfa=0.3))

# 8 (3) — harorat + unum birga
q(3, "yuqori",
  "2SO₂ + O₂ ⇌ 2SO₃ + Q reaksiyasida harorat OSHIRILSA muvozanat va SO₃ unumi haqida to'g'ri xulosa qaysi?",
  "muvozanat chapga siljiydi, SO₃ unumi kamayadi",
  [("muvozanat o'ngga siljiydi, unum ortadi", "ekzotermik reaksiyada T ortishi teskari (endo) yo'nalishni kuchaytiradi"),
   ("muvozanat siljimaydi, unum o'zgarmaydi", "harorat muvozanatni doim siljitadi (Kc o'zgaradi)"),
   ("muvozanat chapga siljiydi, unum ortadi", "chapga siljish — mahsulot kamayishi demakdir")],
  "Reaksiya ekzotermik: T↑ endotermik (teskari) yo'nalishga yordam beradi — chapga, SO₃ kamayadi.",
  dict(arch="harorat_unum"))

# 9 (2) — katalizator tuzoq
q(2, "yuqori",
  "Katalizator kiritilganda muvozanatdagi sistemada nima o'zgaradi?",
  "muvozanat siljimaydi, faqat unga erishish vaqti qisqaradi",
  [("muvozanat mahsulotlar tomonga siljiydi", "katalizator ikkala tezlikni teng ravishda oshiradi"),
   ("Kc qiymati ortadi", "Kc faqat haroratga bog'liq"),
   ("mahsulot unumi ortadi", "muvozanat holati o'zgarmagach unum ham o'zgarmaydi")],
  "Katalizator to'g'ri va teskari reaksiyalarni bir xil marta tezlashtiradi — muvozanat holatiga ta'sir etmaydi.",
  dict(arch="katalizator_tuzoq"))

# 10 (3) — bosim va tezlik darajali
check("q10", 2*2**3, 16)
q(3, "yuqori",
  "N₂ + 3H₂ ⇌ 2NH₃ sistemasida bosim 2 marta oshirildi. TO'G'RI reaksiya tezligi necha marta ortadi?",
  "16", [("8", "faqat H₂ darajasi hisoblangan"), ("4", "koeffitsiyentlar yig'indisi 2 daraja deb olingan"),
          ("2", "darajaga ko'tarilmagan")],
  "v = k[N₂][H₂]³; konsentratsiyalar 2 marta ortadi → 2·2³ = 16 marta.",
  dict(arch="bosim_tezlik", n=2))

# 11 (3) — ICE: muvozanat konsentratsiya
check("q11", 5-3, 2)
q(3, "yuqori",
  "N₂ + 3H₂ ⇌ 2NH₃. Boshlang'ich: [N₂]=2 M, [H₂]=5 M. Muvozanatda [NH₃]=2 M bo'ldi. "
  "Muvozanatdagi [H₂] ni toping (M).",
  "2", [("3", "sarflangan miqdorning o'zi"), ("4", "1:1 nisbat olingan"),
         ("1", "N₂ ning muvozanat qiymati bilan chalkashuv")],
  "NH₃ 2 mol/l hosil bo'ldi → H₂ sarfi 3 mol/l → [H₂] = 5 − 3 = 2 M.",
  dict(arch="ice_konts", b=[2, 5], nh3=2))

# 12 (3) — ICE teskari: boshlang'ichni topish
check("q12", 0.3+0.4, 0.7)
q(3, "yuqori",
  "A + B ⇌ 2C reaksiyasida muvozanat konsentratsiyalari: [A]=0,3 M, [B]=0,5 M, [C]=0,8 M. "
  "A ning BOSHLANG'ICH konsentratsiyasini toping (M).",
  "0,7", [("1,1", "C ning to'liq qiymati qo'shilgan"), ("0,3", "muvozanat qiymati ko'chirilgan"),
           ("0,9", "B uchun hisob olingan")],
  "C dan 0,8 M hosil bo'lgan → A sarfi 0,4 M → boshlang'ich [A] = 0,3 + 0,4 = 0,7 M.",
  dict(arch="ice_teskari", c=[0.3, 0.5, 0.8]))

# 13 (3) — kombinatsiya
q(3, "yuqori",
  "2CO + O₂ ⇌ 2CO₂ + Q reaksiyasida CO₂ unumini OSHIRISH uchun qaysi juft chora to'g'ri?",
  "bosimni oshirish va haroratni pasaytirish",
  [("bosimni pasaytirish va haroratni oshirish", "ikkalasi ham chapga siljitadi"),
   ("katalizator qo'shish va haroratni oshirish", "katalizator siljitmaydi, T↑ chapga siljitadi"),
   ("hajmni oshirish va CO₂ qo'shish", "ikkalasi ham teskari yo'nalishga xizmat qiladi")],
  "O'ng tomonda mol kam (2 < 3) → bosim↑ o'ngga; reaksiya ekzotermik → T↓ o'ngga.",
  dict(arch="kombinatsiya"))

# 14 (2) — fikrlar tanlovi (1-2-3 format)
q(2, "yuqori",
  "Muvozanat haqidagi fikrlardan qaysilari TO'G'RI?\n"
  "1) muvozanatda to'g'ri va teskari reaksiyalar davom etadi;\n"
  "2) muvozanatda barcha moddalar konsentratsiyalari o'zaro teng bo'ladi;\n"
  "3) katalizator kiritilganda Kc qiymati o'zgarmaydi.",
  "1 va 3",
  [("1 va 2", "2-fikr xato: konsentratsiyalar o'zgarmas, lekin teng emas"),
   ("faqat 1", "3-fikr ham to'g'ri — Kc faqat haroratga bog'liq"),
   ("2 va 3", "2-fikr xato, 1-fikr esa to'g'ri (dinamiklik)")],
  "1 — dinamiklik, 3 — Kc faqat T ga bog'liq: to'g'ri. 2 — keng tarqalgan xato tasavvur.",
  dict(arch="fikrlar_tanlovi"))

# 15 (3) — heterogen Kc
check("q15", 0.01/0.05, 0.2)
q(3, "yuqori",
  "FeO(q) + CO(g) ⇌ Fe(q) + CO₂(g) reaksiyasida muvozanatda [CO]=0,05 M, [CO₂]=0,01 M. "
  "Muvozanat konstantasini toping.",
  "0,2", [("5", "teskari nisbat"), ("0,0005", "qattiq moddalar ifodaga kiritilgan deb ko'paytirilgan"),
           ("0,06", "yig'indi olingan")],
  "Qattiq moddalar Kc ifodasiga kirmaydi: Kc = [CO₂]/[CO] = 0,01/0,05 = 0,2.",
  dict(arch="heterogen_kc"))

# 16 (3) — inert gaz tuzoq
q(3, "yuqori",
  "O'zgarmas HAJMDAGI idishda N₂ + 3H₂ ⇌ 2NH₃ muvozanatiga argon qo'shildi (T = const). Muvozanat qanday o'zgaradi?",
  "siljimaydi — reagentlar konsentratsiyasi o'zgarmadi",
  [("o'ngga siljiydi", "umumiy bosim ortsa-da, parsial konsentratsiyalar o'zgarmaydi"),
   ("chapga siljiydi", "argon reaksiyada qatnashmaydi va hajm o'zgarmagan"),
   ("avval o'ngga, so'ng chapga siljiydi", "hech qanday siljish yuz bermaydi")],
  "V = const da inert gaz reagent-mahsulot konsentratsiyalarini o'zgartirmaydi → muvozanat joyida qoladi.",
  dict(arch="inert_tuzoq"))

# 17 (3) — jadval: muvozanatni aniqlash + ICE
check("q17", 1-0.8, 0.2)
q(3, "yuqori",
  "H₂ + I₂ ⇌ 2HI reaksiyasida [H₂]₀ = [I₂]₀ = 1 M. HI konsentratsiyasi o'lchab borildi:\n"
  "[JADVAL] t, min | 0 | 10 | 20 | 30 | 40 ;; [HI], M | 0 | 1,2 | 1,5 | 1,6 | 1,6\n"
  "Muvozanatdagi [H₂] ni toping (M).",
  "0,2", [("0,4", "1,2 qiymatidan hisoblangan (10-min hali muvozanat emas)"), ("1,6", "HI qiymati ko'chirilgan"),
           ("0,8", "sarflangan miqdorning o'zi")],
  "Muvozanat 30-min dan ([HI]=1,6 o'zgarmadi). H₂ sarfi = 1,6/2 = 0,8 → [H₂] = 1 − 0,8 = 0,2 M.",
  dict(arch="jadval_ice", hi=1.6))

# 18 (2) — konsentratsiya siljitish
q(2, "yuqori",
  "N₂ + 3H₂ ⇌ 2NH₃ muvozanatida hosil bo'layotgan NH₃ doimiy ravishda sistemadan chiqarib turilsa, nima kuzatiladi?",
  "muvozanat o'ngga siljiydi, NH₃ hosil bo'lishi davom etadi",
  [("muvozanat chapga siljiydi", "mahsulot kamayishi to'g'ri yo'nalishni kuchaytiradi"),
   ("reaksiya butunlay to'xtaydi", "reagentlar yetarli ekan reaksiya davom etadi"),
   ("Kc kamayadi", "Kc harorat o'zgarmasa o'zgarmaydi")],
  "Mahsulot konsentratsiyasining pasayishi Le Chatelier bo'yicha to'g'ri reaksiyani kuchaytiradi.",
  dict(arch="konts_siljish"))

# 19 (3) — konversiya darajasi
check("q19", 100*2/4, 50)
q(3, "yuqori",
  "4 mol N₂ va 12 mol H₂ aralashmasida muvozanat qaror topganda 4 mol NH₃ hosil bo'ldi. "
  "N₂ ning necha foizi reaksiyaga kirishgan?",
  "50", [("25", "NH₃ ning yarmi emas, N₂ sarfi 2 mol"), ("100", "4 mol NH₃ = 4 mol N₂ deb olingan"),
          ("33", "H₂ bo'yicha hisob aralashgan")],
  "4 mol NH₃ uchun 2 mol N₂ sarflanadi → 2/4 · 100% = 50%.",
  dict(arch="konversiya", n2=4, nh3=4))

# 20 (2) — Kc nimaga bog'liq
q(2, "yuqori",
  "Muvozanat konstantasi Kc qiymatini quyidagilardan qaysi biri O'ZGARTIRADI?",
  "haroratni o'zgartirish",
  [("bosimni oshirish", "bosim muvozanatni siljitadi, lekin Kc ni o'zgartirmaydi"),
   ("katalizator kiritish", "katalizator Kc ga ta'sir etmaydi"),
   ("reagent konsentratsiyasini oshirish", "konsentratsiyalar o'zgarsa ham Kc saqlanadi")],
  "Kc — faqat haroratning funksiyasi; qolgan omillar muvozanat holatini siljitadi, konstantani emas.",
  dict(arch="kc_omil"))

# 21 (3) — kvadratli ICE (Kc = 64)
check("q21", 2*0.8, 1.6)
q(3, "yuqori",
  "H₂ + I₂ ⇌ 2HI, Kc = 64. Boshlang'ich [H₂] = [I₂] = 1 M. Muvozanatdagi [HI] ni toping (M).",
  "1,6", [("0,8", "sarflangan H₂ qiymati (x) — HI = 2x"), ("2", "to'liq aylanish deb olingan"),
           ("1", "Kc dan foydalanilmagan")],
  "(2x)²/(1−x)² = 64 → 2x/(1−x) = 8 → x = 0,8 → [HI] = 1,6 M.",
  dict(arch="ice_kvadrat", kc=64))

# 22 (3) — hajm kamaytirilganda tezlik
check("q22", 3**2*3, 27)
q(3, "yuqori",
  "2NO + O₂ ⇌ 2NO₂ sistemasida idish hajmi 3 marta KAMAYTIRILDI. To'g'ri reaksiya tezligi necha marta ortadi?",
  "27", [("9", "O₂ darajasi tushirib qoldirilgan"), ("6", "darajalar o'rniga koeffitsiyentlar qo'shilgan"),
          ("3", "darajaga ko'tarilmagan")],
  "Konsentratsiyalar 3 marta ortadi: v = k[NO]²[O₂] → 3²·3 = 27 marta.",
  dict(arch="hajm_tezlik", n=3))

# 23 (3) — mol ortishi / bosim
check("q23", (1-0.25) + 2*0.25, 1.25)
q(3, "yuqori",
  "Yopiq idishda 1 mol N₂O₄ ning 25 % i NO₂ ga parchalanib muvozanat qaror topdi (T = const). "
  "Idishdagi bosim boshlang'ichiga nisbatan necha marta ortadi?",
  "1,25", [("1,5", "α=50% uchun qiymat"), ("2", "to'liq parchalanish deb olingan"),
            ("1,125", "NO₂ koeffitsiyenti unutilgan")],
  "Mollar: N₂O₄ 0,75 + NO₂ 0,5 = 1,25 mol → bosim 1,25 marta ortadi.",
  dict(arch="mol_ortish", alfa=0.25))

# 24 (2) — choralar tanlovi (1-2-3-4 format)
q(2, "yuqori",
  "N₂ + 3H₂ ⇌ 2NH₃ + Q muvozanatida NH₃ unumini qaysi choralar OSHIRADI?\n"
  "1) bosimni oshirish;  2) haroratni oshirish;\n"
  "3) NH₃ ni doimiy chiqarib turish;  4) o'zgarmas hajmda inert gaz qo'shish.",
  "1 va 3",
  [("1 va 2", "T↑ ekzotermik reaksiyada unumni kamaytiradi"),
   ("faqat 1", "3-chora ham ishlaydi — mahsulot kamayishi o'ngga siljitadi"),
   ("1, 3 va 4", "inert gaz (V=const) konsentratsiyalarni o'zgartirmaydi")],
  "Bosim↑ mol kam tomonga (1 ✓); T↑ chapga (2 ✗); mahsulotni chiqarish o'ngga (3 ✓); inert gaz ta'sirsiz (4 ✗).",
  dict(arch="choralar_tanlovi"))

# 25 (3) — Kc va harorat: termik xarakter
q(3, "yuqori",
  "Harorat ko'tarilganda reaksiyaning muvozanat konstantasi KAMAYDI. Bundan qanday xulosa chiqadi?",
  "to'g'ri reaksiya ekzotermik",
  [("to'g'ri reaksiya endotermik", "endotermik bo'lsa T↑ da Kc ortardi"),
   ("reaksiya issiqliksiz boradi", "unda Kc haroratga deyarli bog'liq bo'lmasdi"),
   ("muvozanat o'ngga siljigan", "Kc kamayishi chapga siljishni bildiradi")],
  "T↑ endotermik yo'nalishni kuchaytiradi; Kc kamaygani — muvozanat chapga siljigani, ya'ni to'g'ri reaksiya ekzotermik.",
  dict(arch="kc_harorat"))

# 26 (3) — Kc = 1 ICE
check("q26", 1.0, (1.0**2)/((2-1.0)**2))
q(3, "yuqori",
  "CO + H₂O(g) ⇌ CO₂ + H₂, Kc = 1. Boshlang'ich [CO] = [H₂O] = 2 M. Muvozanatdagi [CO₂] ni toping (M).",
  "1", [("2", "to'liq aylanish deb olingan"), ("0,5", "x/2 bilan chalkashuv"),
         ("1,5", "asossiz qiymat")],
  "x²/(2−x)² = 1 → x/(2−x) = 1 → x = 1 M.",
  dict(arch="kc1_ice"))

# 27 (3) — unumdan muvozanat mollari
check("q27", 1.6+0.4+0.2, 2.2)
q(3, "yuqori",
  "2 mol SO₂ va 1 mol O₂ aralashmasida SO₂ ning 80 % i SO₃ ga aylanib muvozanat qaror topdi. "
  "Muvozanatdagi gazlarning UMUMIY mol sonini toping.",
  "2,2", [("3", "boshlang'ich yig'indi (o'zgarish yo'q deb olingan)"), ("2", "faqat SO₃ va SO₂ qo'shilgan"),
           ("2,6", "O₂ sarfi 0,4 o'rniga 0,8 dan xato")],
  "SO₃ = 1,6; SO₂ qoldiq = 0,4; O₂ = 1 − 0,8 = 0,2 → jami 2,2 mol.",
  dict(arch="unum_mol", unum=0.8))

# 28 (2) — RASMLI: porshenli idish (rang dinamikasi)
q(2, "yuqori",
  "Rasmdagi porshenli idishda 2NO₂(qo'ng'ir) ⇌ N₂O₄(rangsiz) muvozanati bor. Porshen TEZ pastga "
  "bosilib, hajm 2 marta kamaytirildi (T = const). Gaz rangi qanday o'zgaradi?",
  "avval keskin to'qlashadi, so'ng asta-sekin biroz ochiladi",
  [("darhol ochiladi", "siqilish avval [NO₂] ni oshiradi — rang avval to'qlashadi"),
   ("faqat to'qlashib boradi", "keyin muvozanat N₂O₄ (mol kam) tomonga siljib rangni ochadi"),
   ("o'zgarmaydi", "ham siqilish, ham siljish rangga ta'sir qiladi")],
  "Siqilish oniy: [NO₂] 2 marta ortadi — to'q. So'ng muvozanat mol kam (N₂O₄) tomonga siljiydi — rang qisman ochiladi.",
  dict(arch="porshen_dinamika"), fig="piston")

# 29 (3) — parametrli Kc formulasi
q(3, "yuqori",
  "A(g) + 2B(g) ⇌ C(g) reaksiyasida muvozanat konsentratsiyalari mos ravishda a, b va c bilan belgilangan. "
  "Muvozanat konstantasining to'g'ri ifodasini ko'rsating.",
  "c/(a·b²)",
  [("c/(a·2b)", "koeffitsiyent daraja bo'ladi, ko'paytuvchi emas"),
   ("(a·b²)/c", "teskari reaksiya konstantasi"),
   ("c²/(a·b)", "darajalar chalkashtirilgan")],
  "Kc = [C]/([A][B]²) = c/(a·b²).",
  dict(arch="parametrli_kc"))

# 30 (2) — rang: NO₂/N₂O₄
q(2, "yuqori",
  "2NO₂(qo'ng'ir) ⇌ N₂O₄(rangsiz) + Q. Gaz aralashmasi solingan yopiq idish muzli suvga tushirilsa, rang qanday o'zgaradi?",
  "rang ochiladi — muvozanat N₂O₄ tomonga siljiydi",
  [("rang to'qlashadi", "sovutish ekzotermik yo'nalishni, ya'ni rangsiz N₂O₄ ni kuchaytiradi"),
   ("rang o'zgarmaydi", "harorat muvozanatni doim siljitadi"),
   ("avval to'qlashib, keyin ochiladi", "siljish bir yo'nalishda boradi")],
  "T↓ ekzotermik yo'nalishga yordam beradi: qo'ng'ir NO₂ rangsiz N₂O₄ ga o'tadi — rang ochiladi.",
  dict(arch="rang"))

# 31 (3) — teskari reaksiya konstantasi
check("q31", 1/25, 0.04)
q(3, "yuqori",
  "To'g'ri reaksiya uchun Kc = 25 bo'lsa, xuddi shu sharoitda TESKARI reaksiyaning muvozanat konstantasi qancha?",
  "0,04", [("25", "teskari uchun ham bir xil deb olingan"), ("−25", "konstanta manfiy bo'lmaydi"),
            ("5", "kvadrat ildiz olingan")],
  "K(tesk) = 1/K(to'g'ri) = 1/25 = 0,04.",
  dict(arch="teskari_kc", kc=25))

# 32 (3) — RASMLI: shu grafikdan alfa
check("q32", 100*0.4/0.6, 66.7, tol=0.2)
q(3, "yuqori",
  "5-savoldagi grafikdan foydalaning: muvozanatga kelguncha N₂O₄ ning necha foizi parchalangan?",
  "≈66,7", [("33,3", "qolgan ulush olingan"), ("40", "mutlaq kamayish (0,4) foiz deb olingan"),
             ("80", "NO₂ qiymati bilan chalkashuv")],
  "Parchalandi: 0,6 − 0,2 = 0,4 → α = 0,4/0,6 ≈ 66,7%.",
  dict(arch="grafik_alfa"), fig="ct_eq")

# ---------- Y2: kontakt apparati ssenariysi ----------
check("y2_o2", 6/2, 3)
check("y2_jami", (8-6)+(5-3)+6, 10)
check("y2_kon", 100*6/8, 75)
Y2 = dict(
  n=33, tur="Y2", element="I.6",
  ichki_pasport=[dict(n=33, element="I.6", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="I.6", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="I.6", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Sulfat kislota ishlab chiqarishdagi kontakt apparatida 2SO₂ + O₂ ⇌ 2SO₃ + Q reaksiyasi boradi. "
               "Diagrammada reaktorga yuborilgan boshlang'ich mollar va muvozanatda hosil bo'lgan SO₃ miqdori "
               "ko'rsatilgan. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  fig="bar_kontakt",
  savollar_ichki=[
    "33. Muvozanatga kelguncha necha mol O₂ sarflangan?",
    "34. Muvozanatdagi gazlarning umumiy mol soni qancha?",
    "35. SO₂ ning necha foizi reaksiyaga kirishgan?"],
  javoblar_royxati=["A) 3", "B) 10", "C) 75", "D) 6", "E) 2", "F) 60"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="SO₃ mollari — O₂ sarfi bilan adashtiriladi"),
                   dict(variant="E", xato="qolgan SO₂ (yoki O₂) miqdori"),
                   dict(variant="F", xato="O₂ ga nisbatan foiz hisoblash xatosi")],
  yechim=("SO₃ 6 mol → O₂ sarfi 3 mol (33 → A). Qoldi: SO₂ 2, O₂ 2, SO₃ 6 → jami 10 mol (34 → B). "
          "Konversiya: 6/8 = 75% (35 → C)."),
  parametrlar=dict(arch="kontakt_ssenariy", so2=8, o2=5, so3=6))

# ---------- O1 ----------
check("o36", (4-3.2)/2*2, 0.8)
check("o37", 0.4**2/(0.1*0.2**3), 200)
check("o38", 100*0.1/0.5, 20)
check("o39", 2**2, 4)
check("o40", 1/8, 0.125)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="yuqori",
      savol="Yopiq idishda 1 mol N₂ va 3 mol H₂ aralashmasi muvozanatga keldi; bunda umumiy bosim "
            "boshlang'ichning 0,8 qismini tashkil etdi (T, V = const). Necha mol NH₃ hosil bo'lgan?",
      javob="0,8", yechim="Jami 4 mol → 4·0,8 = 3,2 mol. Kamayish 0,8 mol = 2x (Δn) → x = 0,4 → NH₃ = 2x = 0,8 mol.",
      parametrlar=dict(arch="bosim_teskari")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="N₂ + 3H₂ ⇌ 2NH₃ muvozanatida [NH₃]=0,4 M, [N₂]=0,1 M, [H₂]=0,2 M. Muvozanat konstantasini toping.",
      javob="200", yechim="Kc = 0,4²/(0,1·0,2³) = 0,16/0,0008 = 200.",
      parametrlar=dict(arch="kc_nh3")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Boshlang'ich [N₂O₄] = 0,5 M; muvozanatda [NO₂] = 0,2 M bo'ldi (N₂O₄ ⇌ 2NO₂). "
            "N₂O₄ ning dissotsiatsiya darajasini (%) toping.",
      javob="20", yechim="Parchalandi 0,1 M → α = 0,1/0,5 = 20%.",
      parametrlar=dict(arch="alfa_topish")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="N₂ + 3H₂ ⇌ 2NH₃ sistemasida idish hajmi 2 marta oshirildi. TESKARI reaksiya tezligi necha marta kamayadi?",
      javob="4", yechim="v(tesk) = k[NH₃]²; konsentratsiya 2 marta kamaydi → 2² = 4 marta.",
      parametrlar=dict(arch="hajm_teskari")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="H₂ + I₂ ⇌ 2HI uchun Kc = 64. HI ⇌ ½H₂ + ½I₂ reaksiyasining muvozanat konstantasini toping.",
      javob="0,125", yechim="K' = 1/√Kc = 1/8 = 0,125 (teskari + ½ koeffitsiyent → kvadrat ildiz).",
      parametrlar=dict(arch="kc_transform")),
]

# ---------- O2 ----------
check("o41a", 8/2, 4); check("o41a2", 3*4, 12)
check("o41b1", (10-4)/5, 1.2); check("o41b2", (30-12)/5, 3.6); check("o41b3", 8/5, 1.6)
check("o41c", 1.6**2/(1.2*3.6**3), 0.0457, tol=0.001)
check("o41d", 100*4/10, 40)
check("o42a", 0.6**2/(3-0.6), 0.15)
check("o42b", 100*0.6/3, 20)
check("o43b", 4*0.25, 1.0)
check("o43c", 1*0.25, 0.25)
O2 = [
 dict(n=41, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Hajmi 5 l bo'lgan yopiq reaktorga 10 mol N₂ va 30 mol H₂ yuborildi. Muvozanat qaror topganda "
            "reaktorda 8 mol NH₃ bor edi (N₂ + 3H₂ ⇌ 2NH₃ + Q). Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Muvozanatga kelguncha sarflangan N₂ va H₂ mollarini toping.",
             yechim=["N₂: 8/2 = 4 mol; H₂: 3·4 = 12 mol"], M=2, A=1),
        dict(savol="b) Muvozanatdagi barcha gazlarning molyar konsentratsiyalarini hisoblang.",
             yechim=["[N₂]=(10−4)/5=1,2 M; [H₂]=(30−12)/5=3,6 M; [NH₃]=8/5=1,6 M"], M=3, A=2),
        dict(savol="c) Muvozanat konstantasini hisoblang.",
             yechim=["Kc = 1,6²/(1,2·3,6³) = 2,56/55,99 ≈ 0,046"], M=4, A=3),
        dict(savol="d) N₂ ning konversiya darajasini (%) toping.",
             yechim=["4/10 = 40%"], M=2, A=2),
        dict(savol="e) Nega sanoatda bu jarayon yuqori bosimda va katalizator ishtirokida olib boriladi? Izohlang.",
             yechim=["Bosim↑ mol kamayadigan (NH₃) tomonga siljitadi — unum ortadi;",
                     "katalizator muvozanatni siljitmaydi, ammo unga erishishni tezlashtiradi."], M=4, A=2),
      ],
      rasmiylashtirish="ICE zanjiri: sarf → konsentratsiya → Kc → konversiya → sanoat izohi; M15+A10.",
      parametrlar=dict(arch="nh3_zanjir", V=5, n2=10, h2=30, nh3=8)),
 dict(n=42, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Hajmi 1 l bo'lgan yopiq idishga 3 mol PCl₅ solindi va qizdirildi. Muvozanat qaror topganda "
            "idishda 0,6 mol Cl₂ bor edi (PCl₅ ⇌ PCl₃ + Cl₂ − Q)."),
      bandlar=[
        dict(savol="a) ICE jadvalini tuzib, muvozanat konstantasini hisoblash yo'lini yozing va toping.",
             yechim=["Muvozanatda: PCl₅ 2,4; PCl₃ 0,6; Cl₂ 0,6 (mol/l).",
                     "Kc = 0,6·0,6/2,4 = 0,15"], M=13, A=0),
        dict(savol="b) PCl₅ ning dissotsiatsiya darajasini aniqlash usulini ko'rsating va hisoblang.",
             yechim=["α = 0,6/3 = 0,2 → 20%"], M=9, A=0),
        dict(savol="c) Harorat oshirilsa α qanday o'zgaradi? Sababini yozing.",
             yechim=["Parchalanish endotermik (−Q): T↑ muvozanatni o'ngga siljitadi — α ortadi."], M=3, A=0),
      ],
      rasmiylashtirish="Faqat usul baholanadi: M13+M9+M3 = 25 (rasmiy 42-format).",
      parametrlar=dict(arch="pcl5_usul", n0=3, cl2=0.6)),
 dict(n=43, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("CO(g) + Cl₂(g) ⇌ COCl₂(g) + Q reaksiyasi uchun muvozanat konstantasi turli haroratlarda o'lchandi:\n"
            "[JADVAL] T, K | 400 | 500 | 600 ;; Kc | 9 | 4 | 1\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Jadvalga asoslanib to'g'ri reaksiya ekzotermik yoki endotermik ekanini aniqlang va asoslang.",
             yechim=["T ortishi bilan Kc kamayyapti → muvozanat chapga siljiydi → to'g'ri reaksiya ekzotermik."], M=4, A=0),
        dict(savol="b) 500 K da muvozanatda [CO] = 0,5 M va [Cl₂] = 0,5 M bo'lsa, [COCl₂] ni hisoblang.",
             yechim=["[COCl₂] = Kc·[CO][Cl₂] = 4·0,25 = 1 M"], M=4, A=3),
        dict(savol="c) Xuddi shu [CO] va [Cl₂] qiymatlarida 600 K uchun [COCl₂] ni toping.",
             yechim=["[COCl₂] = 1·0,25 = 0,25 M"], M=3, A=3),
        dict(savol="d) Mahsulot unumi uchun qaysi harorat ma'qul? Sanoat nuqtai nazaridan qisqacha muhokama qiling.",
             yechim=["Unum uchun past T (400 K) ma'qul — Kc katta; ammo past T da tezlik sekin,",
                     "shuning uchun sanoatda oraliq harorat va katalizator tanlanadi."], M=4, A=4),
      ],
      rasmiylashtirish="Jadval-tahlil (Kc–T): M15+A10. 41/42 formatlaridan farqli.",
      parametrlar=dict(arch="kc_jadval", kc=[9, 4, 1])),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261106)
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
    d = dict(n=n, tur="Y1", element="I.6", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I6-B", daraja="B", bob=6, bob_nomi="Kimyoviy muvozanat",
    manba=("MS spetsifikatsiyasi I.6; darslik (8-9-sinf) muvozanat bo'limlari arxetiplari — "
           "barcha savollar yangi sonlar bilan tuzilgan, javoblar mustaqil qayta hisoblangan"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★: ICE jadvallari, Kc hisob-teskari masalalari, "
          "dissotsiatsiya darajasi, kombinatsiyalangan Le Chatelier. A-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.6") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
