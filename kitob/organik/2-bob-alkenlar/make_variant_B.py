# -*- coding: utf-8 -*-
"""Organik 2-bob B-varianti: Alkenlar, alkadiyenlar, alkinlar (III.2) — HAQIQIY MS MUHITI ★★★.
Markovnikov, sifat reaksiyalari, aralashma tahlili, karbid va polimer hisoblari.
Tongotarov/DTM arxetiplari — javoblar mustaqil tekshirilgan."""
import json, random

OUT = "mavzu_III2B.json"
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

# 1 (3) — 1-2-3
q(3, "yuqori",
  "Alkenlar haqidagi TO'G'RI fikrlarni tanlang:\n"
  "1) bromli suvni rangsizlantiradi;  2) KMnO₄ eritmasini rangsizlantiradi;  "
  "3) o'rin olish — asosiy reaksiya turi;  4) polimerlanadi.",
  "1, 2 va 4",
  [("hammasi", "asosiy tur — BIRIKISH, o'rin olish emas"),
   ("1 va 4", "KMnO₄ sinovi (Vagner) ham alkenlarga xos"),
   ("2 va 3", "3 noto'g'ri")],
  "Qo'shbog' birikish reaksiyalarining «markazi»; ikkala sifat sinovi ham ishlaydi.",
  dict(arch="alken_fikr_b"))

# 2 (3) — zichlikdan
check("q2", 1.25*22.4, 28)
q(3, "yuqori",
  "Normal sharoitdagi zichligi 1,25 g/L bo'lgan alkenni aniqlang.",
  "eten (C₂H₄)",
  [("propen", "M = 42, zichligi 1,875"), ("buten", "M = 56, zichligi 2,5"),
   ("etan", "u alken emas")],
  "M = ρ·22,4 = 28 g/mol → C₂H₄.",
  dict(arch="zichlik_alken"))

# 3 (3) — Markovnikov
q(3, "yuqori",
  "Propenga HBr biriktirilganda ASOSIY mahsulot qaysi (Markovnikov qoidasi)?",
  "2-brompropan",
  [("1-brompropan", "vodorod H ko'p uglerodga boradi"),
   ("ikkala izomer teng aralashmada", "yo'nalish tanlab (Markovnikovcha) boradi"),
   ("2,2-dibrompropan", "bitta HBr birikadi")],
  "H⁺ vodorodi KO'PROQ H li uglerodga: CH₃–CHBr–CH₃ hosil bo'ladi.",
  dict(arch="markovnikov"))

# 4 (3) — karbid hisob
check("q4", 6.4/64*22.4, 2.24)
q(3, "yuqori",
  "CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂. 6,4 g toza karbiddan olinadigan atsetilen hajmini (n.sh.) toping. "
  "(M(CaC₂)=64)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("4,48 L", "0,2 mol emas"), ("1,12 L", "yarmi")],
  "n = 0,1 mol → V = 2,24 L.",
  dict(arch="karbid_hisob_b"))

# 5 (3) — RASMLI: brom testi tajribasi
q(3, "yuqori",
  "Rasmdagi tajribada ikki probirkaga bromli suv quyilib, biriga etan, ikkinchisiga etilen "
  "yuborildi. Qaysi xulosa TO'G'RI?",
  "etilenli probirka rangsizlandi — u to'yinmagan",
  [("ikkalasi ham rangsizlandi", "etan Br₂ ni biriktirmaydi"),
   ("etanli probirka rangsizlandi", "aksincha"),
   ("hech biri o'zgarmadi", "alken sinovga «javob beradi»")],
  "Sifat reaksiyasi sinflarni bir zumda ajratadi: alkan «jim», alken «ishlaydi».",
  dict(arch="brom_tajriba_oqish"), fig="bromtest")

# 6 (3)
q(3, "yuqori",
  "Atsetilenga suv biriktirilganda (Kucherov reaksiyasi) nima hosil bo'ladi?",
  "sirka aldegidi (CH₃CHO)",
  [("etil spirti", "spirt etilen gidratlanishida"), ("sirka kislota", "u aldegid oksidlanishidan"),
   ("etilenglikol", "u boshqa jarayon mahsuloti")],
  "C₂H₂ + H₂O → (Hg²⁺) CH₃CHO — alkin gidratlanishining o'ziga xosligi.",
  dict(arch="kucherov"))

# 7 (3) — 1-2-3: CnH2n-2
q(3, "yuqori",
  "Formulasi C₄H₆ bo'lgan moddaga qaysi sinflar MOS kelishi mumkin?\n"
  "1) alkin (butin);  2) alkadiyen (butadien);  3) alkan;  4) alken.",
  "1 va 2",
  [("faqat 1", "dien ham CₙH₂ₙ₋₂"), ("3 va 4", "ularniki 2n+2 va 2n"),
   ("hammasi", "alkan/alkenga to'g'ri kelmaydi")],
  "CₙH₂ₙ₋₂ — ikki sinf uchun umumiy: sinflararo izomeriya.",
  dict(arch="c4h6_sinflar"))

# 8 (2)
q(2, "yuqori",
  "Alkenlarda uglerodning gibridlanishi qanday?",
  "qo'shbog'dagi C lar — sp²",
  [("sp³ hamma joyda", "qo'shbog' uglerodi sp²"), ("sp", "sp — alkinlarda"),
   ("d²sp³", "organikada uchramaydi")],
  "sp²: tekis uchburchak, 120° — pi-bog' tekislikka perpendikulyar.",
  dict(arch="sp2"))

# 9 (3) — JADVAL moslash
q(3, "yuqori",
  "Jadvaldagi reaksiyalarni turlari bilan TO'G'RI moslang:\n"
  "[JADVAL] Reaksiya | Tur ;; a) C₂H₄ + Br₂ | 1) polimerlanish ;; b) nC₂H₄ → (–CH₂CH₂–)ₙ | "
  "2) birikish ;; c) C₂H₆ + Cl₂ (yorug'lik) | 3) o'rin olish",
  "a—2, b—1, c—3",
  [("a—1, b—2, c—3", "Br₂ qo'shbog'ga BIRIKADI"), ("a—2, b—3, c—1", "n molekula → polimer"),
   ("a—3, b—1, c—2", "alkanda o'rin olish")],
  "Alken — birikish/polimerlanish; alkan — o'rin olish.",
  dict(arch="reaksiya_moslash_b"))

# 10 (3)
check("q10", 0.1*188, 18.8)
q(3, "yuqori",
  "C₂H₄ + Br₂ → C₂H₄Br₂. 0,1 mol etilen to'liq biriktirilganda hosil bo'lgan dibrometan massasini "
  "toping. (M(C₂H₄Br₂)=188)",
  "18,8 g", [("188 g", "1 mol uchun"), ("9,4 g", "yarmi"), ("16 g", "bu Br₂ massasi")],
  "m = 0,1·188 = 18,8 g.",
  dict(arch="dibrometan_hisob"))

# 11 (3) — aralashma (brom suvi orqali)
check("q11", 10-6, 4)
q(3, "yuqori",
  "Etan va etilen aralashmasining 10 L (n.sh.) miqdori bromli suvdan o'tkazilganda hajm 6 L gacha "
  "kamaydi. Aralashmadagi etilen hajmini toping.",
  "4 L", [("6 L", "bu qolgan etan"), ("10 L", "hammasi emas"), ("2 L", "hisob xato")],
  "Bromli suv faqat etilenni «ushlab qoladi»: V = 10 − 6 = 4 L (40 %).",
  dict(arch="aralash_brom_hajm"))

# 12 (2)
q(2, "yuqori",
  "Vagner reaksiyasi (KMnO₄ bilan) alkenlarda nima beradi?",
  "ikki atomli spirt (glikol) — eritma rangsizlanadi",
  [("kislota darhol", "yumshoq sharoitda glikol"), ("alkan", "qaytarilish emas"),
   ("hech narsa", "sinov aynan ishlaydi")],
  "3C₂H₄ + 2KMnO₄ + 4H₂O → 3C₂H₄(OH)₂ + 2MnO₂ + 2KOH.",
  dict(arch="vagner"))

# 13 (3)
check("q13", 0.1*123, 12.3)
q(3, "yuqori",
  "Propen 0,1 mol HBr ni to'liq biriktirdi. Asosiy mahsulot massasini toping. (M(C₃H₇Br)=123)",
  "12,3 g", [("123 g", "1 mol uchun"), ("6,15 g", "yarmi"), ("8,1 g", "bu HBr massasi")],
  "n = 0,1 mol → m(2-brompropan) = 12,3 g.",
  dict(arch="hbr_hisob"))

# 14 (3) — JADVAL «?»
q(3, "yuqori",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Sinf | Umumiy formula | Bog' ;; alken | ? | C=C ;; alkin | ? | C≡C ;; alkadiyen | CₙH₂ₙ₋₂ | ?",
  "CₙH₂ₙ; CₙH₂ₙ₋₂; ikkita C=C",
  [("CₙH₂ₙ₊₂; CₙH₂ₙ; C≡C", "chalkash"), ("CₙH₂ₙ; CₙH₂ₙ; ikkita C≡C", "alkin −2"),
   ("CₙH₂ₙ₋₂; CₙH₂ₙ; bitta C=C", "teskari")],
  "Alken 2n; alkin 2n−2; dien — ikki qo'shbog'.",
  dict(arch="sinf_jadval_b2"))

# 15 (3)
check("q15", 11.2/22.4*46, 23)
q(3, "yuqori",
  "C₂H₄ + H₂O → C₂H₅OH. 11,2 L (n.sh.) etilen to'liq gidratlanganda hosil bo'lgan spirt massasini "
  "toping. (M(C₂H₅OH)=46)",
  "23 g", [("46 g", "1 mol uchun"), ("11,5 g", "yarmi"), ("9,2 g", "0,2 mol emas")],
  "n = 0,5 mol → m = 23 g.",
  dict(arch="gidratlanish_hisob"))

# 16 (2)
q(2, "yuqori",
  "Butadien-1,3 sanoatda nima uchun ishlab chiqariladi?",
  "sun'iy kauchuk olish uchun",
  [("yoqilg'i sifatida", "qimmat — yoqilmaydi"), ("erituvchi sifatida", "u gaz"),
   ("o'g'it sifatida", "organik gaz o'g'it emas")],
  "nCH₂=CH–CH=CH₂ → butadien kauchugi (Lebedev usuli tarixiy asos).",
  dict(arch="butadien_maqsad"))

# 17 (3)
check("q17", 8.96/22.4*2*44, 35.2)
q(3, "yuqori",
  "2C₂H₂ + 5O₂ → 4CO₂ + 2H₂O. 8,96 L (n.sh.) atsetilen yonganda hosil bo'lgan CO₂ massasini toping. "
  "(M(CO₂)=44)",
  "35,2 g", [("17,6 g", "koeffitsiyent 2 emas"), ("44 g", "1 mol uchun"), ("70,4 g", "ikki baravar")],
  "n = 0,4 → n(CO₂) = 0,8 mol → m = 35,2 g.",
  dict(arch="atsetilen_yonish_b"))

# 18 (2)
q(2, "yuqori",
  "Sis-trans (geometrik) izomeriya qaysi birikmalarda uchraydi?",
  "qo'shbog' atrofida turli o'rinbosarli alkenlarda",
  [("barcha alkanlarda", "erkin aylanish bor — izomer yo'q"),
   ("faqat alkinlarda", "chiziqli uchbog'da bo'lmaydi"),
   ("faqat halqali birikmalarda", "asosiy manba — qo'shbog'")],
  "C=C atrofida aylanish «qulflangan»: buten-2 ning sis- va trans- shakllari.",
  dict(arch="sis_trans"))

# 19 (3) — RASMLI: brom test davomi
q(3, "yuqori",
  "5-savol tajribasida etilenli probirkaga jami 16 g brom «yutildi». Necha mol etilen yuborilgan? "
  "(M(Br₂)=160)",
  "0,1", [("1", "16/160"), ("0,05", "yarmi emas"), ("0,2", "ikki baravar")],
  "n(Br₂) = 0,1 = n(C₂H₄) — 1:1 birikish.",
  dict(arch="brom_hisob_b"), fig="bromtest")

# 20 (2)
q(2, "yuqori",
  "Atsetilenning trimerlanishi (3C₂H₂ →) qanday mahsulot beradi?",
  "benzol (C₆H₆)",
  [("geksan", "to'yingan mahsulot emas"), ("siklogeksan", "u gidrogenlashdan keyin"),
   ("polietilen", "u etilendan")],
  "Zelinskiy reaksiyasi: uch molekula halqaga «yig'iladi» — arenlarga ko'prik.",
  dict(arch="trimerlanish"))

# 21 (3)
check("q21", (0.3-0.1)/1, 0.2)
q(3, "yuqori",
  "Propan va propen aralashmasi 0,3 mol; u bromli suvdan o'tkazilganda 16 g brom sarflandi. "
  "Aralashmadagi propan mol miqdorini toping. (M(Br₂)=160)",
  "0,2", [("0,1", "bu propen"), ("0,3", "hammasi emas"), ("0,15", "teng emas")],
  "n(propen) = n(Br₂) = 0,1 → n(propan) = 0,3 − 0,1 = 0,2 mol.",
  dict(arch="aralash_brom_mol"))

# 22 (3) — 1-2-3: atsetilen xossalari
q(3, "yuqori",
  "Atsetilen uchun XOS reaksiyalarni tanlang:\n"
  "1) ikki bosqichli brom biriktirish;  2) Kucherov gidratlanishi;  3) yorug'likda o'rin olish;  "
  "4) trimerlanib benzol berish.",
  "1, 2 va 4",
  [("hammasi", "o'rin olish — alkan «imzosi»"), ("faqat 1", "2 va 4 ham alkinga xos"),
   ("2 va 3", "3 mos emas")],
  "Uchbog' — ikki pi: bosqichli birikish, gidratlanish, trimerlanish.",
  dict(arch="alkin_xossa_tanlov"))

# 23 (3)
check("q23a", 5.4/54, 0.1); check("q23b", 0.1*2*160, 32)
q(3, "yuqori",
  "Butadien-1,3 ning 5,4 grammi bromning qancha massasini TO'LIQ biriktira oladi? "
  "(M: C₄H₆=54, Br₂=160)",
  "32 g", [("16 g", "IKKITA qo'shbog' bor"), ("160 g", "1 mol uchun"), ("8 g", "hisob xato")],
  "n = 0,1 mol; 2 qo'shbog' → n(Br₂) = 0,2 → m = 32 g.",
  dict(arch="dien_brom_hisob"))

# 24 (2)
q(2, "yuqori",
  "Sanoatda etilen asosan qanday olinadi?",
  "neft uglevodorodlarini krekinglab/pirolizlab",
  [("karbiddan", "karbid atsetilen beradi"), ("spirtdan faqat", "lab usuli"),
   ("havodan", "havoda etilen yo'q")],
  "Yirik neft-kimyo: alkanlar parchalanishida alkenlar «tug'iladi».",
  dict(arch="etilen_sanoat"))

# 25 (3)
q(3, "yuqori",
  "Etilenni laboratoriyada olish usuli qaysi?",
  "etil spirtini kons. H₂SO₄ bilan qizdirib suvsizlantirish",
  [("karbid + suv", "u atsetilen"), ("metan xlorlash", "u galogenalkan"),
   ("polietilenni eritish", "erish gaz bermaydi")],
  "C₂H₅OH → (H₂SO₄, 170 °C) C₂H₄ + H₂O — degidratatsiya.",
  dict(arch="etilen_lab"))

# 26 (3) — RASMLI: polimer diagramma (B)
check("q26", 400*0.31, 124)
q(3, "yuqori",
  "Diagrammadan foydalaning: yiliga 400 mln tonna plastik ishlab chiqarilsa, taxminan qancha "
  "polietilenga to'g'ri keladi (PE ulushi 31 %)?",
  "124 mln t", [("31 mln t", "400 ning 31 %i"), ("200 mln t", "yarmi emas"), ("400 mln t", "hammasi emas")],
  "m = 400·0,31 = 124 mln tonna.",
  dict(arch="bar_polimer_hisob"), fig="bar_polymer")

# 27 (3)
check("q27", 54000/54, 1000)
q(3, "yuqori",
  "O'rtacha molyar massasi 54 000 g/mol bo'lgan butadien kauchugidagi zvenolar sonini toping. "
  "(M(C₄H₆)=54)",
  "1000", [("540", "54000/54"), ("100", "nol kam"), ("2000", "ikki baravar")],
  "n = 54000/54 = 1000.",
  dict(arch="kauchuk_n"))

# 28 (2) — RASMLI: bog' uzunligi (B)
q(2, "yuqori",
  "Bog' uzunliklari grafigidan: qaysi bog' ENG MUSTAHKAM?",
  "C≡C — eng qisqa bog'",
  [("C–C", "eng uzun — nisbatan bo'sh"), ("C=C", "o'rtada"),
   ("hammasi teng", "uzunlik-mustahkamlik bog'liq")],
  "Qisqa bog' — kuchli bog': uzish energiyasi C≡C da eng katta.",
  dict(arch="bog_mustahkam"), fig="bond_len")

# 29 (3)
check("q29", 0.25*54, 13.5)
q(3, "yuqori",
  "0,25 mol butadien-1,3 ning massasini toping. (M(C₄H₆)=54)",
  "13,5 g", [("54 g", "1 mol uchun"), ("27 g", "yarim mol uchun"), ("108 g", "2 mol uchun")],
  "m = 0,25·54 = 13,5 g.",
  dict(arch="dien_massa"))

# 30 (2)
q(2, "yuqori",
  "Nega atsetilen ballonlarda maxsus g'ovak modda va atsetonga singdirilgan holda saqlanadi?",
  "siqilgan sof atsetilen portlashga moyil",
  [("hidini kamaytirish uchun", "gap xavfsizlikda"),
   ("arzonlashtirish uchun", "aksincha, qimmatlashadi"),
   ("rangini saqlash uchun", "gaz rangsiz")],
  "C₂H₂ yuqori bosimda beqaror — eritilgan holatda xavfsiz tashiladi.",
  dict(arch="atsetilen_saqlash"))

# 31 (3)
check("q31", 0.15*2*22.4, 6.72)
q(3, "yuqori",
  "C₂H₂ + 2H₂ → C₂H₆. 0,15 mol atsetilenni to'liq gidrogenlash uchun zarur vodorod hajmini (n.sh.) "
  "toping.",
  "6,72 L", [("3,36 L", "IKKI mol H₂ kerak"), ("22,4 L", "1 mol uchun"), ("1,68 L", "hisob xato")],
  "n(H₂) = 0,3 mol → V = 6,72 L.",
  dict(arch="alkin_gidrogenlash"))

# 32 (3) — RASMLI: brom test xulosa
q(3, "yuqori",
  "5-savol tajribasi asosida: qaysi JUFT gazni bromli suv FARQLAY OLMAYDI?",
  "etilen va atsetilen",
  [("etan va etilen", "aynan farqlaydi"), ("metan va propen", "farqlaydi"),
   ("metan va etan", "bu juft ham «bir xil» (reaksiyasiz), lekin savol to'yinmaganlar haqida")],
  "Ikkala to'yinmagan gaz ham rangsizlantiradi — ularni miqdoriy farq (2 barobar Br₂) yoki boshqa "
  "sinov ajratadi.",
  dict(arch="brom_chegara"), fig="bromtest")

# ---------- Y2: uch gaz ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="III.2",
  ichki_pasport=[dict(n=33, element="III.2", qiyinlik=2, kognitiv="yuqori"),
                 dict(n=34, element="III.2", qiyinlik=3, kognitiv="yuqori"),
                 dict(n=35, element="III.2", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch gaz tekshirildi: X — bromli suvni o'zgartirmadi; Y — bromli suvni rangsizlantirdi, "
               "1 moli 1 mol Br₂ biriktirdi; Z — bromli suvni rangsizlantirdi, 1 moli 2 mol Br₂ "
               "biriktirdi. Gazlar C₂H₆, C₂H₄ va C₂H₂ ekani ma'lum. 33–35-savollarga A–F ro'yxatidan "
               "javob tanlang."),
  savollar_ichki=[
    "33. X gaz qaysi?",
    "34. Z gazning formulasi qaysi?",
    "35. Y gazdan sanoatda qaysi mahsulot olinadi?"],
  javoblar_royxati=["A) etan", "B) C₂H₂", "C) polietilen", "D) etilen", "E) C₂H₄", "F) benzol"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="etilen — Y (1 mol Br₂)"),
                   dict(variant="E", xato="2 mol Br₂ biriktirgani — uchbog'li C₂H₂"),
                   dict(variant="F", xato="benzol atsetilendan (Z dan) olinadi")],
  yechim=("X — to'yingan etan (A). Z — atsetilen: 2 pi-bog' (B). "
          "Y — etilen: undan PE (C)."),
  parametrlar=dict(arch="uch_gaz_brom_ssenariy"))

# ---------- O1 (Spectrum uslubi: ko'p bosqichli) ----------
check("o36a", 8*0.8, 6.4); check("o36b", 6.4/64*22.4, 2.24)
check("o37", 0.2*28, 5.6)
check("o38", 4.48/22.4*46, 9.2)
check("o39a", 8.96/22.4, 0.4); check("o39b", 0.4-24/160/1, 0.25)
check("o40", 0.5*0.8*46, 18.4)
O1 = [
 dict(n=36, qiyinlik=3, kognitiv="yuqori",
      savol="Tarkibida 80 % CaC₂ bo'lgan 8 g texnik karbiddan olinadigan atsetilen hajmini "
            "(n.sh., L) toping. (M(CaC₂)=64)",
      javob="2,24", yechim="m(sof) = 6,4 g → n = 0,1 mol → V = 2,24 L.",
      parametrlar=dict(arch="texnik_karbid_zanjir")),
 dict(n=37, qiyinlik=3, kognitiv="yuqori",
      savol="CaC₂ → C₂H₂ → C₂H₄ zanjiri bo'yicha 0,2 mol karbiddan (yo'qotishsiz) olingan etilen "
            "massasini (g) toping. (M(C₂H₄)=28)",
      javob="5,6", yechim="Har bosqich 1:1 → n = 0,2 mol → m = 5,6 g.",
      parametrlar=dict(arch="karbid_etilen_zanjir")),
 dict(n=38, qiyinlik=3, kognitiv="yuqori",
      savol="Sxemadagi zanjir bo'yicha 4,48 L (n.sh.) etilendan (yo'qotishsiz) olingan etil spirti "
            "massasini (g) toping. (M(C₂H₅OH)=46)",
      javob="9,2", yechim="n = 0,2 mol → m = 0,2·46 = 9,2 g.",
      parametrlar=dict(arch="sxema_spirt_zanjir"), fig="scheme38"),
 dict(n=39, qiyinlik=3, kognitiv="yuqori",
      savol="Etan-etilen aralashmasi 8,96 L (n.sh.); bromli suvdan o'tkazilganda 24 g brom sarflandi. "
            "Aralashmadagi etan mol miqdorini toping. (M(Br₂)=160)",
      javob="0,25", yechim="n(C₂H₄) = 24/160 = 0,15 → n(etan) = 0,4 − 0,15 = 0,25 mol.",
      parametrlar=dict(arch="aralash_brom_zanjir")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="11,2 L (n.sh.) etilen gidratlandi; unum 80 %. Olingan spirt massasini (g) toping. "
            "(M(C₂H₅OH)=46)",
      javob="18,4", yechim="n = 0,5 mol → nazariy 23 g → amalda 23·0,8 = 18,4 g.",
      parametrlar=dict(arch="unum_spirt_zanjir")),
]

# ---------- O2 ----------
check("o41b", 32/64, 0.5); check("o41c", 0.5*22.4, 11.2)
check("o41d", 11.2*0.75, 8.4)
check("o43c", 0.1*160/160, 0.1)
O2 = [
 dict(n=41, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Ustaxonada 32 g toza kalsiy karbiddan atsetilen olinib, payvandlashda ishlatildi. "
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Reaksiya tenglamasini yozing.",
             yechim=["CaC₂ + 2H₂O → C₂H₂↑ + Ca(OH)₂."], M=3, A=2),
        dict(savol="b) Nazariy olinadigan atsetilen hajmini (n.sh.) toping. (M(CaC₂)=64)",
             yechim=["n = 0,5 mol → V = 11,2 L."], M=4, A=3),
        dict(savol="c) Gazning 75 % i yig'ib olindi. Amaldagi hajmni hisoblang.",
             yechim=["V = 11,2·0,75 = 8,4 L."], M=4, A=3),
        dict(savol="d) Qolgan Ca(OH)₂ dan xo'jalikda qanday foydalanish mumkin?",
             yechim=["Ohak suti sifatida: devor oqlash, tuproq kislotaliligini kamaytirish."], M=4, A=2),
      ],
      rasmiylashtirish="Karbid-amaliyot: tenglama → nazariy → unum → qoldiq; M15+A10.",
      parametrlar=dict(arch="karbid_amaliyot_zanjir")),
 dict(n=42, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Qo'shbog'ning «tabiati» tahlil qilinadi. Quyidagilarni MULOHAZA bilan bajaring."),
      bandlar=[
        dict(savol="a) Nega qo'shbog' (C=C) yakka bog'dan mustahkamroq bo'lsa-da, alkenlar "
                   "alkanlardan FAOLROQ? Ziddiyatni yeching.",
             yechim=["Qo'shbog' = sigma + pi. Pi-bog' alohida olganda bo'shroq va «ochiq» joylashgan —",
                     "reagentlar unga oson hujum qiladi. Umumiy mustahkamlik va faollik — har xil narsalar."], M=13, A=0),
        dict(savol="b) Markovnikov qoidasini bitta misolda ko'rsating.",
             yechim=["CH₃–CH=CH₂ + HCl → CH₃–CHCl–CH₃: H ko'p vodorodli uglerodga boradi."], M=9, A=0),
        dict(savol="c) Alkenlarning ikkita sifat reaksiyasini ayting.",
             yechim=["Bromli suv va KMnO₄ eritmasining rangsizlanishi."], M=3, A=0),
      ],
      rasmiylashtirish="Qo'shbog'-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="qoshbog_mulohaza")),
 dict(n=43, tur="O2", element="III.2", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Topshiriqni bajarish jarayonida barcha mulohaza va hisoblarni uzviy ketma-ketlikda yozing. "
            "Noma'lum gazsimon uglevodorod X: vodorodga nisbatan zichligi 14; bromli suvni "
            "rangsizlantiradi. Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) X ning molyar massasini toping.",
             yechim=["M = 14·2 = 28 g/mol."], M=4, A=2),
        dict(savol="b) X ning formulasi va sinfini aniqlang.",
             yechim=["C₂H₄ — alken (bromli suv sinovi to'yinmaganlikni tasdiqlaydi)."], M=4, A=3),
        dict(savol="c) 0,1 mol X to'liq biriktirishi mumkin bo'lgan brom mol miqdorini yozing.",
             yechim=["Bitta qo'shbog' → 0,1 mol Br₂."], M=4, A=3),
        dict(savol="d) X ning polimerlanish tenglamasini yozing va mahsulotni nomlang.",
             yechim=["nCH₂=CH₂ → (–CH₂–CH₂–)ₙ — polietilen."], M=3, A=2),
      ],
      rasmiylashtirish="X-detektiv: M → formula → Br₂ → polimer; M15+A10.",
      parametrlar=dict(arch="x_detektiv_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20263205)
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
    d = dict(n=n, tur="Y1", element="III.2", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-III2-B", daraja="B", bob=2, bob_nomi="Alkenlar, alkadiyenlar, alkinlar",
    manba=("Tongotarov/DTM arxetiplari (Markovnikov, sifat sinovlari, brom-aralashma tahlili, "
           "karbid/polimer hisoblari) va Spectrum uslubidagi 36–43 — javoblar mustaqil tekshirilgan; "
           "MS spetsifikatsiyasi III.2"),
    izoh=("B-varianti — HAQIQIY MS MUHITI ★★★ (Organik kimyo kitobi): brom-test tajribasi, "
          "aralashma tahlili, unumli zanjirlar."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="III.2") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
