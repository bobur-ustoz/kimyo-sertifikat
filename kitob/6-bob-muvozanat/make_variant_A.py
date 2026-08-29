# -*- coding: utf-8 -*-
"""6-bob A-varianti: Kimyoviy muvozanat (I.6) — O'RGATUVCHI ★★.
Hayotiy sahnalar: gazli ichimlik, ammiak zavodi, g'or stalaktitlari, NO₂ probirkalari.
Soddaroq sonlar, o'rgatuvchi chalg'ituvchilar; barcha javoblar mustaqil hisoblangan."""
import json, random

OUT = "mavzu_I6A.json"
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
  "Kimyoviy muvozanat deb qanday holatga aytiladi?",
  "to'g'ri va teskari reaksiya tezliklari tenglashgan holat",
  [("barcha reaksiyalar to'xtagan holat", "reaksiyalar davom etadi — muvozanat dinamik"),
   ("reagentlar to'liq sarflangan holat", "muvozanatda reagentlar ham, mahsulotlar ham bo'ladi"),
   ("faqat mahsulot hosil bo'layotgan holat", "teskari reaksiya ham xuddi shu tezlikda boradi")],
  "Muvozanat: v(to'g'ri) = v(teskari), konsentratsiyalar o'zgarmas bo'lib qoladi.",
  dict(arch="tarif_oddiy"))

# 2 (2) — belgi
q(2, "quyi",
  "Reaksiya tenglamasidagi «⇌» belgisi nimani bildiradi?",
  "reaksiya ikkala yo'nalishda ham borishini",
  [("reaksiya juda tez borishini", "belgi tezlik haqida ma'lumot bermaydi"),
   ("reaksiya issiqlik chiqarishini", "issiqlik +Q/−Q bilan ko'rsatiladi"),
   ("reaksiya faqat qizdirilganda borishini", "sharoit belgining ustida alohida yoziladi")],
  "«⇌» — qaytar reaksiya belgisi: jarayon to'g'ri va teskari yo'nalishda boradi.",
  dict(arch="qaytar_belgi"))

# 3 (2) — Kc ifodasini tanlash
q(2, "o'rta",
  "N₂ + 3H₂ ⇌ 2NH₃ reaksiyasi uchun muvozanat konstantasining TO'G'RI ifodasi qaysi?",
  "Kc = [NH₃]²/([N₂]·[H₂]³)",
  [("Kc = [N₂]·[H₂]³/[NH₃]²", "bu teskari reaksiyaning konstantasi"),
   ("Kc = [NH₃]/([N₂]·[H₂])", "koeffitsiyentlar daraja bo'lib kirishi kerak"),
   ("Kc = 2[NH₃]/([N₂]·3[H₂])", "koeffitsiyent ko'paytuvchi emas, daraja bo'ladi")],
  "Mahsulot kasrning suratida, koeffitsiyentlar daraja ko'rsatkichi bo'ladi.",
  dict(arch="kc_ifoda"))

# 4 (2) — SAHNA: gazli ichimlik
q(2, "o'rta",
  "Rasmga qarang: gazli ichimlik shishasi ochilganda «vish-sh» etib pufakchalar chiqadi. "
  "Buning muvozanat nuqtai nazaridan sababi nimada? (CO₂(g) ⇌ CO₂(eritma))",
  "bosim keskin pasayadi — muvozanat gaz tomonga siljiydi",
  [("harorat keskin ko'tariladi", "shisha ochilganda harorat deyarli o'zgarmaydi"),
   ("suv bug'lanib ketadi", "pufakchalar suv bug'i emas, erigan CO₂ dir"),
   ("katalizator hosil bo'ladi", "hech qanday katalizator ishtirok etmaydi")],
  "Qopqoq ostida CO₂ bosimi katta; ochilganda bosim tushadi — muvozanat erigan gaz chiqishi tomonga siljiydi.",
  dict(arch="soda_sahna"), fig="soda")

# 5 (2) — harorat oddiy
q(2, "o'rta",
  "A + B ⇌ C + Q reaksiyasida haroratni PASAYTIRSAK muvozanat qaysi tomonga siljiydi?",
  "o'ngga — mahsulot tomonga",
  [("chapga — reagentlar tomonga", "T↓ ekzotermik (issiqlik chiqaruvchi) yo'nalishga yordam beradi"),
   ("siljimaydi", "harorat muvozanatni doim siljitadi"),
   ("avval o'ngga, keyin chapga", "siljish bitta yangi holatgacha boradi")],
  "Sovutish issiqlik chiqaradigan (to'g'ri) reaksiyani kuchaytiradi — muvozanat o'ngga siljiydi.",
  dict(arch="harorat_oddiy"))

# 6 (3) — Kc oddiy hisob
check("q6", 1/(0.5*0.4), 5)
q(3, "o'rta",
  "A + B ⇌ C reaksiyasida muvozanat konsentratsiyalari: [A]=0,5 M, [B]=0,4 M, [C]=1 M. "
  "Muvozanat konstantasini hisoblang.",
  "5", [("0,2", "teskari nisbat olingan"), ("1,1", "ko'paytirish o'rniga qo'shilgan"),
         ("2", "faqat [A] ga bo'lingan")],
  "Kc = [C]/([A]·[B]) = 1/(0,5·0,4) = 5.",
  dict(arch="kc_oddiy_hisob"))

# 7 (2) — bosim oddiy
q(2, "o'rta",
  "N₂ + 3H₂ ⇌ 2NH₃ muvozanatida bosim OSHIRILSA muvozanat qaysi tomonga siljiydi?",
  "o'ngga — gaz mollari kam tomonga",
  [("chapga — gaz mollari ko'p tomonga", "bosim↑ mol KAM tomonga siljitadi"),
   ("siljimaydi", "mol sonlari teng emas: 4 ≠ 2"),
   ("bosim muvozanatga hech qachon ta'sir qilmaydi", "faqat Δn = 0 bo'lganda ta'sir qilmaydi")],
  "Chapda 4 mol, o'ngda 2 mol gaz: bosim ortishi mol kam tomonni «afzal» qiladi.",
  dict(arch="bosim_oddiy"))

# 8 (2) — SAHNA: ammiak zavodi
q(2, "o'rta",
  "Rasmda ammiak zavodi reaktori ko'rsatilgan. Nega sanoatda NH₃ sintezi 200–300 atm "
  "bosimda olib boriladi?",
  "yuqori bosim muvozanatni NH₃ tomonga siljitadi — unum ortadi",
  [("yuqori bosim reaksiyani qaytmas qiladi", "reaksiya baribir qaytarligicha qoladi"),
   ("yuqori bosimda katalizator kerak bo'lmaydi", "katalizator baribir ishlatiladi"),
   ("yuqori bosim haroratni pasaytiradi", "bosim haroratni avtomatik pasaytirmaydi")],
  "4 mol gazdan 2 mol hosil bo'ladi: bosim↑ mol kam (NH₃) tomonga siljitadi, unum ortadi.",
  dict(arch="plant_sahna"), fig="plant")

# 9 (2) — konsentratsiya oddiy
q(2, "o'rta",
  "CO + H₂O(g) ⇌ CO₂ + H₂ muvozanatida suv bug'i konsentratsiyasi OSHIRILSA nima kuzatiladi?",
  "muvozanat o'ngga siljiydi, CO₂ va H₂ ko'payadi",
  [("muvozanat chapga siljiydi", "reagent qo'shilishi to'g'ri reaksiyani kuchaytiradi"),
   ("hech narsa o'zgarmaydi", "konsentratsiya o'zgarishi muvozanatni siljitadi"),
   ("Kc ortadi", "Kc harorat o'zgarmagach o'zgarmaydi")],
  "Reagent qo'shilsa Le Chatelier bo'yicha muvozanat uni «sarflash» tomonga — o'ngga siljiydi.",
  dict(arch="konts_oddiy"))

# 10 (2) — katalizator oddiy
q(2, "o'rta",
  "Katalizator muvozanatdagi sistemaga qanday ta'sir ko'rsatadi?",
  "muvozanatni siljitmaydi, unga tezroq erishtiradi",
  [("muvozanatni mahsulot tomonga siljitadi", "ikkala tezlikni teng oshirgani uchun siljitmaydi"),
   ("mahsulot unumini oshiradi", "muvozanat holati o'zgarmas ekan, unum ham o'zgarmaydi"),
   ("teskari reaksiyani sekinlashtiradi", "katalizator ikkala yo'nalishni ham tezlashtiradi")],
  "Katalizator to'g'ri va teskari reaksiyalarni teng marta tezlashtiradi.",
  dict(arch="katalizator_oddiy"))

# 11 (2) — muvozanat belgisi (kuzatish)
q(2, "o'rta",
  "Yopiq idishdagi rangli gaz sistemasida muvozanat qaror topganini qanday KUZATISH orqali bilish mumkin?",
  "aralashma rangi o'zgarmay qoladi",
  [("rang butunlay yo'qoladi", "muvozanatda rangli modda ham qoladi"),
   ("pufakchalar chiqishi to'xtaydi", "yopiq idishda gaz chiqib ketmaydi"),
   ("harorat nolga tushadi", "harorat muvozanat belgisi emas")],
  "Konsentratsiyalar o'zgarmas bo'lgach, rang intensivligi ham o'zgarmay qoladi — muvozanat belgisi.",
  dict(arch="belgi_kuzatish"))

# 12 (2) — inert gaz oddiy
q(2, "o'rta",
  "O'zgarmas hajmli idishdagi muvozanatga inert gaz (masalan, argon) qo'shilsa, muvozanat holatiga nima bo'ladi?",
  "o'zgarmaydi",
  [("mahsulot tomonga siljiydi", "reagent-mahsulot konsentratsiyalari o'zgarmagan"),
   ("reagentlar tomonga siljiydi", "argon reaksiyada ishtirok etmaydi"),
   ("reaksiya to'xtaydi", "inert gaz reaksiyani to'xtatmaydi")],
  "V = const da inert gaz hech bir moddaning konsentratsiyasini o'zgartirmaydi.",
  dict(arch="inert_oddiy"))

# 13 (2) — SAHNA: g'or stalaktitlari
q(2, "o'rta",
  "Rasmga qarang: g'or shiftidan tomgan suvdan stalaktitlar o'sadi. Suvda "
  "Ca(HCO₃)₂ ⇌ CaCO₃↓ + CO₂↑ + H₂O muvozanati bor. G'or havosida tomchidan CO₂ uchib chiqishi "
  "muvozanatga qanday ta'sir qiladi?",
  "muvozanat o'ngga siljiydi — CaCO₃ cho'kib, stalaktit o'sadi",
  [("muvozanat chapga siljiydi — stalaktit eriydi", "mahsulot (CO₂) kamayishi to'g'ri yo'nalishni kuchaytiradi"),
   ("muvozanat siljimaydi", "CO₂ chiqib ketishi konsentratsiyani o'zgartiradi"),
   ("suv qaynab ketadi", "g'orda harorat past, qaynash yuz bermaydi")],
  "CO₂ chiqib ketgani sari muvozanat uni «to'ldirish» uchun o'ngga siljiydi — CaCO₃ cho'kadi.",
  dict(arch="cave_sahna"), fig="cave")

# 14 (3) — Kc dan konsentratsiya
check("q14", 2**2/2, 2)
q(3, "o'rta",
  "A ⇌ 2B reaksiyasi uchun Kc = 2. Muvozanatda [A] = 2 M bo'lsa, [B] ni toping (M).",
  "2", [("4", "kvadrat ildiz olinmagan"), ("1", "Kc/[A] deb olingan"),
         ("0,5", "teskari nisbat")],
  "Kc = [B]²/[A] → [B]² = 2·2 = 4 → [B] = 2 M.",
  dict(arch="kc_dan_topish"))

# 15 (3) — ICE oddiy
check("q15", 1-0.6, 0.4)
q(3, "o'rta",
  "H₂ + I₂ ⇌ 2HI. Boshlang'ich [H₂] = [I₂] = 1 M. Muvozanatda [HI] = 1,2 M bo'ldi. "
  "Muvozanatdagi [H₂] ni toping (M).",
  "0,4", [("0,6", "sarflangan miqdorning o'zi"), ("1,2", "HI qiymati ko'chirilgan"),
           ("0,8", "HI/2 ni ayirish unutilib, boshqa xato")],
  "HI 1,2 M hosil bo'ldi → H₂ sarfi 0,6 M → qoldi 1 − 0,6 = 0,4 M.",
  dict(arch="ice_oddiy_a", hi=1.2))

# 16 (3) — mollar hisobi (alfa)
check("q16", 0.5 + 2*0.5, 1.5)
q(3, "o'rta",
  "Yopiq idishdagi 1 mol N₂O₄ ning YARMI parchalanib muvozanat qaror topdi (N₂O₄ ⇌ 2NO₂). "
  "Idishdagi gazlarning umumiy mol soni qancha bo'ldi?",
  "1,5", [("1", "mol o'zgarmaydi deb olingan"), ("2", "to'liq parchalanish deb olingan"),
           ("0,5", "faqat qolgan N₂O₄ hisoblangan")],
  "Qoldi 0,5 mol N₂O₄, hosil bo'ldi 2·0,5 = 1 mol NO₂ → jami 1,5 mol.",
  dict(arch="mol_oddiy", alfa=0.5))

# 17 (2) — mahsulotni chiqarish
q(2, "o'rta",
  "Muvozanatdagi sistemada mahsulot unumini OSHIRISHNING to'g'ri usuli qaysi?",
  "hosil bo'layotgan mahsulotni doimiy chiqarib turish",
  [("katalizator miqdorini oshirish", "katalizator unumni o'zgartirmaydi"),
   ("reagentlarni kamaytirish", "bu muvozanatni chapga siljitadi"),
   ("idishni ochiq qoldirish", "reagent gazlar ham chiqib ketishi mumkin")],
  "Mahsulot chiqarilsa uning konsentratsiyasi kamayadi — muvozanat doim o'ngga siljib turadi.",
  dict(arch="mahsulot_chiqarish"))

# 18 (2) — SAHNA: NO₂ probirkalari
q(2, "o'rta",
  "Rasmda bir xil gaz (NO₂/N₂O₄ aralashmasi) solingan ikkita probirka: biri issiq suvda (to'q qo'ng'ir), "
  "biri muzda (och rangli). 2NO₂ ⇌ N₂O₄ + Q. Qaysi xulosa TO'G'RI?",
  "isitish muvozanatni qo'ng'ir NO₂ tomonga siljitadi",
  [("isitish muvozanatni N₂O₄ tomonga siljitadi", "unda issiq probirka och rangli bo'lardi"),
   ("harorat rangga ta'sir qilmaydi", "tajribada ranglar aniq farq qiladi"),
   ("sovutish NO₂ ni ko'paytiradi", "sovuq probirka och — NO₂ kamaygan")],
  "T↑ endotermik (teskari) yo'nalishni kuchaytiradi: N₂O₄ → 2NO₂, rang to'qlashadi.",
  dict(arch="no2_sahna"), fig="no2")

# 19 (3) — Kc va harorat
q(3, "o'rta",
  "Harorat ko'tarilganda reaksiyaning Kc qiymati ORTDI. To'g'ri reaksiya haqida qanday xulosa chiqariladi?",
  "endotermik — issiqlik yutib boradi",
  [("ekzotermik — issiqlik chiqaradi", "ekzotermikda T↑ Kc ni kamaytiradi"),
   ("issiqlik effektisiz", "unda Kc haroratga deyarli bog'liq bo'lmasdi"),
   ("katalitik", "katalizator Kc ga ta'sir etmaydi")],
  "T↑ da Kc ortishi — muvozanat o'ngga siljiganini, ya'ni to'g'ri reaksiya endotermik ekanini bildiradi.",
  dict(arch="kc_harorat_oddiy"))

# 20 (2) — jadval o'qish
q(2, "o'rta",
  "Reaksiya davomida mahsulot konsentratsiyasi o'lchab borildi:\n"
  "[JADVAL] t, min | 0 | 5 | 10 | 15 | 20 ;; c, M | 0 | 0,6 | 0,9 | 1,0 | 1,0\n"
  "Sistema qaysi vaqtdan boshlab muvozanatda?",
  "15-minutdan", [("20-minutdan", "1,0 qiymati 15-minutdayoq o'rnatilgan"),
                   ("10-minutdan", "10-min da c hali o'sayotgan edi (0,9 → 1,0)"),
                   ("5-minutdan", "0,6 → 0,9 — o'zgarish davom etgan")],
  "Konsentratsiya o'zgarishdan to'xtagan ilk nuqta — 15-min (1,0 M saqlangan).",
  dict(arch="jadval_oqish"))

# 21 (3) — unum hisobi
check("q21", 100*1.5/2, 75)
q(3, "o'rta",
  "2SO₂ + O₂ ⇌ 2SO₃ reaksiyasida 2 mol SO₂ dan muvozanatda 1,5 mol SO₃ hosil bo'ldi. "
  "SO₃ ning unumini (%) toping.",
  "75", [("50", "asossiz yarim"), ("87,5", "O₂ bo'yicha hisob aralashgan"),
          ("60", "1,5/2,5 xato nisbat")],
  "Nazariy unum 2 mol; amalda 1,5 mol → 1,5/2 · 100% = 75%.",
  dict(arch="unum_hisob"))

# 22 (3) — Kc hisob (SO₃)
check("q22", 0.2**2/(0.2**2*0.1), 10)
q(3, "o'rta",
  "2SO₂ + O₂ ⇌ 2SO₃ muvozanatida: [SO₂]=0,2 M, [O₂]=0,1 M, [SO₃]=0,2 M. Muvozanat konstantasini toping.",
  "10", [("0,1", "teskari nisbat"), ("1", "kvadratlar tushirib qoldirilgan"),
          ("5", "O₂ darajasi 2 deb olingan")],
  "Kc = 0,2²/(0,2²·0,1) = 1/0,1 = 10.",
  dict(arch="kc_so3"))

# 23 (2) — qaytmaslik shartlari
q(2, "o'rta",
  "Quyidagilardan qaysi biri reaksiyaning QAYTMAS borishiga sabab bo'ladi?",
  "cho'kma hosil bo'lib, muhitdan chiqishi",
  [("katalizator ishtirok etishi", "katalizator qaytarlikni o'zgartirmaydi"),
   ("reaksiyaning sekin borishi", "tezlik qaytarlikka bog'liq emas"),
   ("moddalarning rangli bo'lishi", "rang qaytarlik mezoni emas")],
  "Mahsulot muhitni tark etsa (cho'kma, gaz, kam dissotsiyalanuvchi modda) teskari reaksiya imkoni yo'qoladi.",
  dict(arch="qaytmas_shart"))

# 24 (3) — kombinatsiya (o'rgatuvchi)
q(3, "yuqori",
  "N₂ + 3H₂ ⇌ 2NH₃ + Q. NH₃ unumini oshirish uchun QAYSI JUFT chora to'g'ri tanlangan?",
  "bosimni oshirish va haroratni pasaytirish",
  [("bosimni pasaytirish va haroratni oshirish", "ikkalasi ham muvozanatni chapga siljitadi"),
   ("katalizator qo'shish va bosimni pasaytirish", "katalizator siljitmaydi, bosim↓ chapga siljitadi"),
   ("inert gaz qo'shish va isitish", "inert gaz (V=const) siljitmaydi, isitish chapga siljitadi")],
  "Mol kamayadi (4→2): bosim↑ o'ngga; ekzotermik: T↓ o'ngga. Ikkala chora ham unumni oshiradi.",
  dict(arch="kombinatsiya_oddiy"))

# 25 (2) — Kc omillari
q(2, "o'rta",
  "Muvozanat konstantasi Kc quyidagilardan FAQAT qaysi biriga bog'liq?",
  "haroratga",
  [("bosimga", "bosim muvozanatni siljitadi, Kc ni o'zgartirmaydi"),
   ("katalizatorga", "katalizator Kc ga ta'sir etmaydi"),
   ("boshlang'ich konsentratsiyalarga", "qanday boshlansa ham o'sha T da Kc bir xil")],
  "Kc — haroratning funksiyasi: T o'zgarmagach Kc o'zgarmaydi.",
  dict(arch="kc_omil_oddiy"))

# 26 (3) — grafik tanlash: mahsulot konsentratsiyasi
q(3, "o'rta",
  "Yopiq idishga faqat reagentlar solindi. MAHSULOT konsentratsiyasining vaqtga bog'liq grafigi qaysi?",
  "noldan ortib, muvozanatda o'zgarmay qoladi",
  [("doimiy kamayadi", "bu reagent konsentratsiyasining grafigi"),
   ("boshdan oxirigacha o'zgarmas", "mahsulot 0 dan boshlab ortib boradi"),
   ("ortib, keyin nolga tushadi", "muvozanatda mahsulot yo'qolmaydi")],
  "Mahsulot 0 dan ortib boradi va muvozanatda platoga chiqadi (o'sish + plato).",
  svg=dict(correct="rise_flat", d1="fall", d2="flat", d3="rise_fall", xlab="t", ylab="c(mahsulot)"),
  params=dict(arch="grafik_mahsulot"))

# 27 (3) — hajm va tezlik oddiy
check("q27", 2*2, 4)
q(3, "o'rta",
  "A + B ⇌ C sistemasida idish hajmi 2 marta KAMAYTIRILDI. To'g'ri reaksiya tezligi necha marta ortadi?",
  "4", [("2", "faqat bitta modda hisoblangan"), ("8", "uchinchi daraja xato olingan"),
         ("o'zgarmaydi", "konsentratsiyalar ortgani uchun tezlik ham ortadi")],
  "Ikkala konsentratsiya 2 marta ortadi: v = k[A][B] → 2·2 = 4 marta.",
  dict(arch="hajm_oddiy"))

# 28 (2) — rang: isitish
q(2, "o'rta",
  "2NO₂(qo'ng'ir) ⇌ N₂O₄(rangsiz) + Q muvozanatidagi idish ISITILSA rang qanday o'zgaradi?",
  "to'qlashadi — NO₂ ko'payadi",
  [("ochiladi — N₂O₄ ko'payadi", "isitish endotermik (NO₂ hosil bo'lish) yo'nalishini kuchaytiradi"),
   ("o'zgarmaydi", "harorat bu muvozanatni albatta siljitadi"),
   ("rang butunlay yo'qoladi", "NO₂ to'liq yo'qolmaydi")],
  "T↑ issiqlik yutuvchi yo'nalishga (N₂O₄ → 2NO₂) yordam beradi — qo'ng'ir rang kuchayadi.",
  dict(arch="rang_isitish"))

# 29 (3) — teskari Kc
check("q29", 1/5, 0.2)
q(3, "o'rta",
  "To'g'ri reaksiya uchun Kc = 5. Teskari reaksiyaning muvozanat konstantasini toping.",
  "0,2", [("5", "bir xil deb olingan"), ("−5", "konstanta manfiy bo'lmaydi"),
           ("25", "kvadrat olingan")],
  "K(tesk) = 1/K(to'g'ri) = 1/5 = 0,2.",
  dict(arch="teskari_kc_oddiy"))

# 30 (2) — xato fikrni topish
q(2, "o'rta",
  "Muvozanat haqidagi fikrlardan XATOSINI toping.",
  "muvozanatda barcha moddalar konsentratsiyalari o'zaro teng bo'ladi",
  [("muvozanatda konsentratsiyalar o'zgarmas bo'ladi", "bu to'g'ri fikr"),
   ("muvozanat sharoit o'zgarsa siljiydi", "bu to'g'ri fikr (Le Chatelier)"),
   ("muvozanatda ikkala reaksiya davom etadi", "bu to'g'ri fikr (dinamiklik)")],
  "Konsentratsiyalar O'ZGARMAS, lekin o'zaro TENG bo'lishi shart emas — bu keng tarqalgan xato.",
  dict(arch="xato_fikr"))

# 31 (3) — alfa oddiy
check("q31", 100*0.5/2, 25)
q(3, "o'rta",
  "2 mol PCl₅ dan muvozanatga kelguncha 0,5 mol parchalandi. Dissotsiatsiya darajasini (%) toping.",
  "25", [("50", "1 moldan hisoblangan"), ("75", "qolgan ulush olingan"),
          ("0,25", "foizga o'tkazilmagan")],
  "α = 0,5/2 = 0,25 → 25%.",
  dict(arch="alfa_oddiy"))

# 32 (3) — RASMLI: v-t grafigi o'qish
q(3, "o'rta",
  "Rasmda to'g'ri (1) va teskari (2) reaksiya tezliklarining vaqtga bog'liqligi berilgan. "
  "Grafik bo'yicha qaysi xulosa TO'G'RI?",
  "t₁ dan boshlab tezliklar tenglashadi — muvozanat qaror topadi",
  [("t₁ da reaksiyalar to'xtaydi", "tezliklar nolga tushmaydi — teng bo'lib davom etadi"),
   ("teskari reaksiya boshidanoq tez", "teskari tezlik 0 dan boshlanadi"),
   ("to'g'ri tezlik doimo ortib boradi", "reagentlar kamaygani uchun u pasayadi")],
  "1-egri pasayadi, 2-egri ortadi; t₁ da kesishmasdan bir sathga kelib teng davom etadi — muvozanat.",
  dict(arch="vt_oqish"), fig="vt_eq")

# ---------- Y2: limonad (Genri qonuni-lite) ssenariysi ----------
check("y2_33", 1.7*2, 3.4)
check("y2_34", 3.4-1.7, 1.7)
check("y2_35", (3.4-1.7)*0.5, 0.85)
Y2 = dict(
  n=33, tur="Y2", element="I.6",
  ichki_pasport=[dict(n=33, element="I.6", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.6", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.6", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Limonad zavodida suvga CO₂ bosim ostida eritiladi: CO₂(g) ⇌ CO₂(eritma) + Q. 20 °C va 1 atm "
               "bosimda 1 l suvda 1,7 g CO₂ eriydi; erigan gaz massasi bosimga to'g'ri proporsional (Genri qonuni). "
               "33–35-savollarga A–F ro'yxatidan javob tanlang (javoblar — gramm)."),
  savollar_ichki=[
    "33. 2 atm bosimda 1 l suvda necha gramm CO₂ eriydi?",
    "34. 2 atm da tayyorlangan 1 l ichimlik ochilib, bosim 1 atm ga tushsa, necha gramm CO₂ uchib chiqadi?",
    "35. 2 atm da tayyorlangan 0,5 l ichimlik ochilsa-chi?"],
  javoblar_royxati=["A) 1,7", "B) 0,85", "C) 3,4", "D) 6,8", "E) 5,1", "F) 0"],
  javoblar={"33": "C", "34": "A", "35": "B"},
  chalgituvchilar=[dict(variant="D", xato="bosim kvadratga ko'tarilgan (1,7·4)"),
                   dict(variant="E", xato="3,4 + 1,7 — yig'ish xatosi"),
                   dict(variant="F", xato="«hammasi uchib ketadi» degan xato tasavvur")],
  yechim=("33: 1,7·2 = 3,4 g (C). 34: chiqib ketadi 3,4 − 1,7 = 1,7 g (A). "
          "35: 0,5 l uchun hammasi ikki barobar kam → 0,85 g (B)."),
  parametrlar=dict(arch="limonad_ssenariy", s1atm=1.7))

# ---------- O1 ----------
check("o36", 0.4**2/(0.2*0.2), 4)
check("o37", 100*0.3/1, 30)
check("o38", 1-0.4, 0.6)
check("o39", 1/9, 0.111, tol=0.002)
check("o40", 6*2/3, 4)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="H₂ + I₂ ⇌ 2HI muvozanatida [H₂]=0,2 M, [I₂]=0,2 M, [HI]=0,4 M. Muvozanat konstantasini toping.",
      javob="4", yechim="Kc = 0,4²/(0,2·0,2) = 0,16/0,04 = 4.",
      parametrlar=dict(arch="kc_hi")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="1 mol N₂O₄ dan muvozanatga kelguncha 0,3 mol parchalandi. Dissotsiatsiya darajasini (%) toping.",
      javob="30", yechim="α = 0,3/1 = 30%.",
      parametrlar=dict(arch="alfa_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="A ⇌ B + C reaksiyasida boshlang'ich [A] = 1 M. Muvozanatda [B] = 0,4 M bo'lsa, [A] ni toping (M).",
      javob="0,6", yechim="A sarfi = B = 0,4 M → [A] = 1 − 0,4 = 0,6 M.",
      parametrlar=dict(arch="ice_o1")),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="To'g'ri reaksiya uchun Kc = 9. Teskari reaksiya konstantasini toping (yuzdan birgacha).",
      javob="0,11", yechim="K(tesk) = 1/9 ≈ 0,11.",
      parametrlar=dict(arch="teskari_o1")),
 dict(n=40, qiyinlik=3, kognitiv="o'rta",
      savol="N₂ + 3H₂ ⇌ 2NH₃ reaksiyasida muvozanatga kelguncha 6 mol H₂ sarflandi. Necha mol NH₃ hosil bo'lgan?",
      javob="4", yechim="Nisbat 3:2 → NH₃ = 6·2/3 = 4 mol.",
      parametrlar=dict(arch="stex_o1")),
]

# ---------- O2 ----------
check("o41b", 1-0.8, 0.2)
check("o41c", 1.6**2/(0.2*0.2), 64)
check("o41d", 100*0.8/1, 80)
check("o42", 13+9+3, 25)
check("o43b", 0.8**2/0.6, 1.067, tol=0.01)
check("o43c", 100*0.4/1.0, 40)
O2 = [
 dict(n=41, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Hajmi 1 l bo'lgan yopiq idishga 1 mol H₂ va 1 mol I₂ solindi. Muvozanat qaror topganda idishda "
            "1,6 mol HI bor edi (H₂ + I₂ ⇌ 2HI). Bandlar ketma-ket yechiladi — har biri keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) «Boshlang'ich — o'zgarish — muvozanat» (ICE) jadvalini tuzing.",
             yechim=["H₂: 1 → 1−x; I₂: 1 → 1−x; HI: 0 → 2x = 1,6 → x = 0,8"], M=3, A=1),
        dict(savol="b) Muvozanatdagi [H₂] va [I₂] ni toping.",
             yechim=["[H₂] = [I₂] = 1 − 0,8 = 0,2 M"], M=3, A=2),
        dict(savol="c) Muvozanat konstantasini hisoblang.",
             yechim=["Kc = 1,6²/(0,2·0,2) = 64"], M=4, A=3),
        dict(savol="d) H₂ ning necha foizi reaksiyaga kirishganini toping.",
             yechim=["0,8/1 = 80%"], M=2, A=2),
        dict(savol="e) Harorat o'zgartirilsa Kc qiymati o'zgaradimi? Javobingizni izohlang.",
             yechim=["Ha — Kc faqat haroratga bog'liq: T o'zgarsa Kc ham o'zgaradi;",
                     "boshqa omillar (bosim, konsentratsiya, katalizator) uni o'zgartirmaydi."], M=3, A=2),
      ],
      rasmiylashtirish="O'rgatuvchi ICE zanjiri: jadval → konsentratsiya → Kc → % → nazariy izoh; M15+A10.",
      parametrlar=dict(arch="hi_zanjir", h2=1, i2=1, hi=1.6)),
 dict(n=42, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Ammiak zavodida N₂ + 3H₂ ⇌ 2NH₃ + Q jarayoni 450 °C da, 250 atm bosimda, temir katalizator "
            "ishtirokida olib boriladi. Quyidagi savollarga MULOHAZA yuritib javob yozing (hisob talab qilinmaydi)."),
      bandlar=[
        dict(savol="a) Reaksiya ekzotermik bo'lsa-da, nega jarayon past haroratda emas, 450 °C da olib boriladi? "
                   "Muvozanat va tezlik tushunchalarini solishtirib asoslang.",
             yechim=["Past T da unum yuqori (muvozanat o'ngda), lekin tezlik juda sekin — iqtisodiy zarar.",
                     "450 °C — unum va tezlik o'rtasidagi kelishuv (optimal) harorat."], M=13, A=0),
        dict(savol="b) Nega aynan yuqori bosim (250 atm) tanlangan? Mol sonlari orqali tushuntiring.",
             yechim=["4 mol gazdan 2 mol hosil bo'ladi: bosim↑ mol kam tomonga siljitadi — NH₃ unumi ortadi."], M=9, A=0),
        dict(savol="c) Katalizatorning bu jarayondagi rolini bir jumla bilan ayting.",
             yechim=["Muvozanatni siljitmaydi — unga erishish vaqtini keskin qisqartiradi."], M=3, A=0),
      ],
      rasmiylashtirish="Sanoat-mulohaza formati (faqat M): M13+M9+M3 = 25 (rasmiy 42-format).",
      parametrlar=dict(arch="zavod_mulohaza")),
 dict(n=43, tur="O2", element="I.6", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Yopiq idishda N₂O₄ ⇌ 2NO₂ reaksiyasi kuzatildi; konsentratsiyalar jadvalda:\n"
            "[JADVAL] t, s | 0 | 20 | 40 | 60 ;; [N₂O₄], M | 1,0 | 0,7 | 0,6 | 0,6 ;; [NO₂], M | 0 | 0,6 | 0,8 | 0,8\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Sistema qaysi vaqtdan boshlab muvozanatda? Asoslang.",
             yechim=["40-s dan: ikkala konsentratsiya ham o'zgarishdan to'xtagan (0,6 va 0,8)."], M=3, A=1),
        dict(savol="b) Muvozanat konstantasini hisoblang.",
             yechim=["Kc = [NO₂]²/[N₂O₄] = 0,8²/0,6 ≈ 1,07"], M=5, A=4),
        dict(savol="c) Muvozanatga kelguncha N₂O₄ ning necha foizi parchalangan?",
             yechim=["Parchalandi 0,4 M → 0,4/1,0 = 40%"], M=3, A=3),
        dict(savol="d) Nega [NO₂] ning o'sishi [N₂O₄] kamayishidan ikki barobar katta? Stexiometriya orqali izohlang.",
             yechim=["Tenglamada 1 mol N₂O₄ dan 2 mol NO₂ hosil bo'ladi — o'zgarishlar 1:2 nisbatda."], M=4, A=2),
      ],
      rasmiylashtirish="Jadval-tahlil (kuzatuv) formati: M15+A10. B-variantdagi Kc–T jadvalidan farqli.",
      parametrlar=dict(arch="n2o4_jadval")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260607)
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
    variant="mavzu-I6-A", daraja="A", bob=6, bob_nomi="Kimyoviy muvozanat",
    manba=("MS spetsifikatsiyasi I.6; darslik (8-9-sinf) muvozanat bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (limonad, ammiak zavodi, g'or, NO₂ probirkalari) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq sonlar, rasmli hayotiy savollar, o'rgatuvchi "
          "chalg'ituvchilar. B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.6") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
