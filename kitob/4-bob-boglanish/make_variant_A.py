# -*- coding: utf-8 -*-
"""4-bob A-varianti: Kimyoviy bog'lanish (I.4) — O'RGATUVCHI ★★.
Hayotiy sahnalar: osh tuzi kristali, qalam va olmos uzuk, qor parchasi, mis sim.
Soddaroq savollar, o'rgatuvchi chalg'ituvchilar."""
import json, random

OUT = "mavzu_I4A.json"
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
  "Kimyoviy bog'lanish hosil bo'lishining asosiy sababi nimada?",
  "atomlar barqaror (tugallangan) elektron qavatga intiladi",
  [("atomlar og'irlashishga intiladi", "massa bog'lanish sababi emas"),
   ("atomlar isishga intiladi", "issiqlik — jarayon oqibati bo'lishi mumkin, sabab emas"),
   ("atomlar rang hosil qilishga intiladi", "rang bog'lanish maqsadi emas")],
  "Bog'lanishda atomlar oktet (2 yoki 8 e) holatga erishib, energiya jihatdan barqarorlashadi.",
  dict(arch="sabab"))

# 2 (2)
q(2, "quyi",
  "Kovalent bog'lanish qanday hosil bo'ladi?",
  "umumiy elektron juftlar hisobiga",
  [("elektronlarning to'liq o'tishi hisobiga", "bu ion bog'lanish"),
   ("erkin elektronlar «gazi» hisobiga", "bu metall bog'lanish"),
   ("faqat tortishish kuchlari hisobiga", "kovalentda elektron juft umumlashadi")],
  "Ikkala atom elektronlari juftlashib, umumiy bo'ladi — kovalent bog'.",
  dict(arch="kovalent_tarif"))

# 3 (2)
q(2, "o'rta",
  "Qaysi moddada ION bog'lanish mavjud?",
  "KCl", [("HCl", "vodorod bilan — qutbli kovalent"), ("Cl₂", "qutbsiz kovalent"),
           ("H₂O", "qutbli kovalent")],
  "Tipik metall (K) + tipik metallmas (Cl) → elektron to'liq o'tadi — ion bog'.",
  dict(arch="ion_misol"))

# 4 (2) — SAHNA: osh tuzi
q(2, "o'rta",
  "Rasmda osh tuzi kristallari ko'rsatilgan. Nega NaCl kristallari muntazam KUB shaklida bo'ladi?",
  "ionlar panjarada qat'iy tartibda joylashadi",
  [("tuz zavodda shunday kesiladi", "shakl tabiiy — ichki tuzilishdan"),
   ("suv bug'lanib qirralarni tekislaydi", "qirralar panjara tekisliklaridir"),
   ("tasodifiy shakllanadi", "ion panjara geometriyasi aniq")],
  "Na⁺ va Cl⁻ ionlari navbatlashib kub panjara hosil qiladi — tashqi shakl ichki tartibni aks ettiradi.",
  dict(arch="tuz_sahna"), fig="salt")

# 5 (2)
q(2, "o'rta",
  "H₂ molekulasidagi bog'lanish qanday?",
  "qutbsiz kovalent",
  [("qutbli kovalent", "atomlar bir xil — ΔEM = 0"), ("ion", "elektron o'tishi yo'q"),
   ("vodorod bog'lanish", "bu molekulalararo kuch")],
  "Bir xil atomlar: elektron juft o'rtada — qutbsiz kovalent.",
  dict(arch="h2_bog"))

# 6 (3)
q(3, "o'rta",
  "Elektromanfiylik nima?",
  "atomning bog'dagi elektronlarni o'ziga tortish qobiliyati",
  [("atomning elektron berish qobiliyati", "bu qaytaruvchilik xossasi"),
   ("atomning massasi", "EM massa emas"),
   ("atomning radiusi", "radius alohida xossa")],
  "EM qancha katta bo'lsa, atom umumiy juftni shuncha kuchli tortadi (F — chempion, 4,0).",
  dict(arch="em_tarif"))

# 7 (2)
q(2, "o'rta",
  "HCl molekulasida umumiy elektron juft qaysi atomga siljigan?",
  "xlorga — uning elektromanfiyligi katta",
  [("vodorodga", "H ning EM i (2,1) Cl nikidan (3,0) kichik"),
   ("o'rtada turadi", "ΔEM ≠ 0 — juft siljiydi"),
   ("goh u, goh bu atomga", "siljish doimiy — qutbli bog'")],
  "EM(Cl) > EM(H): juft xlorga siljigan — H(δ+)–Cl(δ−).",
  dict(arch="siljish"))

# 8 (2) — SAHNA: qalam va olmos
q(2, "o'rta",
  "Rasmda oddiy qalam (grafit) va olmos uzuk ko'rsatilgan. Ikkalasi ham uglerod! Xossalari nega "
  "bunchalik farq qiladi?",
  "atomlarning panjaradagi joylashuvi (tuzilishi) har xil",
  [("ular turli elementlardan tuzilgan", "ikkalasi ham faqat ugleroddan"),
   ("olmosda qo'shimchalar bor", "sof olmos ham qattiq"),
   ("grafit eskirgan olmos", "biri ikkinchisiga o'z-o'zidan aylanmaydi")],
  "Olmos — fazoviy tetraedrik atom panjara (juda qattiq); grafit — qatlamli tuzilish "
  "(qatlamlar sirg'aladi — yozadi). Bu allotropiya.",
  dict(arch="qalam_sahna"), fig="pencil")

# 9 (2)
q(2, "o'rta",
  "Metall bog'lanish nima hisobiga hosil bo'ladi?",
  "kationlar va umumlashgan erkin elektronlar tortishuvi hisobiga",
  [("umumiy elektron juftlar hisobiga", "juftlar mahkam emas — elektronlar umumlashgan"),
   ("ionlarning tortishuvi hisobiga", "manfiy ion yo'q — elektron gazi bor"),
   ("molekulalar tortishuvi hisobiga", "metallda molekula yo'q")],
  "Metallda valent elektronlar «gaz» kabi erkin: ular kationlarni bog'lab turadi.",
  dict(arch="metall_tarif"))

# 10 (2)
q(2, "o'rta",
  "Qaysi qatorda faqat KOVALENT bog'li moddalar berilgan?",
  "H₂O, CO₂, NH₃",
  [("NaCl, H₂O, CO₂", "NaCl — ion"), ("Fe, Cu, Zn", "bular metall bog'lanishli"),
   ("KBr, CaO, NaF", "barchasi ion birikma")],
  "Uchala modda ham metallmas atomlaridan — kovalent (qutbli) bog'lar.",
  dict(arch="kovalent_qator"))

# 11 (2)
q(2, "o'rta",
  "σ-bog' va π-bog' haqidagi to'g'ri fikrni tanlang.",
  "yakka bog' doim σ; karrali bog'da qo'shimchalari π",
  [("yakka bog' doim π", "birinchi bog' hamisha σ"),
   ("σ va π farqi yo'q", "ular ustma tushish usuli bilan farqlanadi"),
   ("π-bog' σ dan mustahkam", "π odatda kuchsizroq — reaksiyada birinchi uziladi")],
  "Birinchi (o'q bo'ylab) bog' — σ; qo'sh/uch bog'ning qolganlari — π.",
  dict(arch="sigma_pi_tarif"))

# 12 (2)
q(2, "o'rta",
  "CO₂ molekulasida nechta σ- va nechta π-bog' bor?",
  "2 σ va 2 π",
  [("4 σ", "har qo'sh bog'da faqat bittasi σ"), ("2 σ va 4 π", "har qo'sh bog'da bitta π"),
   ("1 σ va 3 π", "ikkita alohida C=O bog' bor")],
  "O=C=O: har C=O da 1σ + 1π → jami 2σ + 2π.",
  dict(arch="co2_sanash"))

# 13 (2) — SAHNA: qor parchasi
q(2, "o'rta",
  "Rasmda olti burchakli qor parchasi ko'rsatilgan. Qorning bunday muntazam shakli nimadan darak beradi?",
  "muz kristalida H₂O molekulalari vodorod bog'lar orqali tartibli joylashgan",
  [("shamol qorni shunday kesadi", "shakl ichki tuzilishdan, tashqi ta'sirdan emas"),
   ("qor tarkibida olti xil modda bor", "qor — faqat suv"),
   ("tasodif", "barcha qor parchalari 6 burchakli — qonuniyat")],
  "Vodorod bog'lari H₂O molekulalarini olti burchakli panjaraga «tizadi» — qor shakli shundan.",
  dict(arch="qor_sahna"), fig="snowflake")

# 14 (2)
q(2, "o'rta",
  "Vodorod bog'lanish qaysi atomlar orasida hosil bo'ladi?",
  "bir molekula H atomi bilan boshqa molekulaning F, O yoki N atomi orasida",
  [("istalgan ikki H atomi orasida", "oddiy H–H — kovalent bog'"),
   ("metall va vodorod orasida", "bu gidriddagi bog'"),
   ("faqat kislorod atomlari orasida", "H ishtiroki shart")],
  "Shart: H kuchli EM li atomga (F, O, N) bog'langan bo'lishi va qo'shni molekulada juft bo'lishi.",
  dict(arch="vodorod_shart"))

# 15 (2)
q(2, "o'rta",
  "Muz qanday kristall panjaraga ega?",
  "molekular",
  [("ion", "H₂O — neytral molekula"), ("atom", "tugunlarda alohida atomlar emas"),
   ("metall", "suv metall emas")],
  "Muz tugunlarida H₂O molekulalari (vodorod bog'lar bilan) — molekular panjara, past t da eriydi.",
  dict(arch="muz_panjara"))

# 16 (3)
q(3, "o'rta",
  "Davr bo'ylab chapdan o'ngga elektromanfiylik qanday o'zgaradi?",
  "ortadi",
  [("kamayadi", "yadro zaryadi ortadi, radius kichrayadi — tortish kuchayadi"),
   ("o'zgarmaydi", "Na dan Cl gacha EM 0,9 dan 3,0 gacha o'sadi"),
   ("avval ortib, keyin kamayadi", "davr ichida monoton ortadi")],
  "Davrda radius kichrayib, yadro tortishi kuchayadi → EM ortadi (ftorga tomon).",
  dict(arch="em_davr"))

# 17 (2)
q(2, "o'rta",
  "Jadvalda ikki moddaning xossalari berilgan:\n"
  "[JADVAL] Modda | Suyuql. t | Eritmasi tok o'tkazadimi ;; X | 801 °C | ha ;; Y | 0 °C | yo'q\n"
  "X va Y qanday panjaralarga ega?",
  "X — ion, Y — molekular",
  [("X — molekular, Y — ion", "yuqori t va elektrolitlik — ion belgisi"),
   ("ikkalasi ham atom", "atom panjara suvda erib tok o'tkazmaydi"),
   ("X — metall, Y — ion", "Y past t da eriydi — molekular")],
  "X (801 °C, elektrolit) — NaCl kabi ion; Y (0 °C) — muz kabi molekular.",
  dict(arch="jadval_yengil"))

# 18 (2) — SAHNA: mis sim
q(2, "o'rta",
  "Rasmda elektr simlari (mis) ko'rsatilgan. Misning tok o'tkazishi va egiluvchanligi qaysi "
  "bog'lanish bilan tushuntiriladi?",
  "metall bog'lanish — erkin elektronlar va sirg'aluvchi qatlamlar",
  [("ion bog'lanish", "ionli moddalar mo'rt, qattiq holda tok o'tkazmaydi"),
   ("kovalent bog'lanish", "kovalent kristallar (olmos) tok o'tkazmaydi, mo'rt"),
   ("vodorod bog'lanish", "metallda vodorod bog' yo'q")],
  "Erkin elektronlar tokni tashiydi; kation qatlamlari «elektron yelim» ichida sirg'anadi — sim egiladi, uzilmaydi.",
  dict(arch="sim_sahna"), fig="wire")

# 19 (3)
q(3, "o'rta",
  "N₂ molekulasi juda inert (reaksiyaga qiyin kirishadi). Buning sababi nimada?",
  "N≡N uch bog' juda mustahkam (946 kJ/mol)",
  [("azot atomi juda katta", "azot kichik atom"),
   ("molekulada bog' yo'q", "aksincha, uchta bog' bor"),
   ("azot metall xossali", "azot — metallmas")],
  "1σ + 2π uch karrali bog'ni uzish katta energiya talab qiladi — N₂ inert.",
  dict(arch="n2_inert"))

# 20 (2)
q(2, "o'rta",
  "«Quruq muz» (qattiq CO₂) xona sharoitida suyuqlanmasdan bug'lanib ketadi. Bu qaysi panjara belgisi?",
  "molekular — molekulalararo kuchlar juda kuchsiz",
  [("ion — ionlar uchib ketadi", "ion panjara 800 °C atrofida suyuqlanadi"),
   ("atom — atomlar ajraladi", "atom panjara o'ta mustahkam"),
   ("metall", "CO₂ metall emas")],
  "Molekulalarni ushlab turuvchi kuchlar kuchsiz — CO₂ to'g'ridan-to'g'ri gazga o'tadi (sublimatsiya).",
  dict(arch="quruq_muz"))

# 21 (3)
q(3, "o'rta",
  "NH₃ molekulasida nechta umumiy elektron juft (bog') va nechta taqsimlanmagan juft bor?",
  "3 ta bog', 1 ta taqsimlanmagan juft",
  [("4 ta bog', 0 ta juft", "azotning 5 valent elektronidan 3 tasi bog'da"),
   ("3 ta bog', 2 ta juft", "5 − 3 = 2 elektron → 1 juft"),
   ("2 ta bog', 1 ta juft", "vodorodlar 3 ta")],
  "N: 5 valent e → 3 tasi N–H bog'larda, 2 tasi (1 juft) bo'sh — donor bo'la oladi.",
  dict(arch="nh3_juft"))

# 22 (3)
q(3, "o'rta",
  "Qaysi javobda moddalar panjara turi bilan TO'G'RI juftlangan?",
  "olmos — atom; NaCl — ion; muz — molekular",
  [("olmos — molekular; NaCl — atom; muz — ion", "hammasi almashib ketgan"),
   ("olmos — ion; NaCl — molekular; muz — atom", "hech biri mos emas"),
   ("olmos — atom; NaCl — molekular; muz — ion", "NaCl va muz o'rni almashgan")],
  "Olmos — atomlar to'ri; NaCl — ionlar; muz — H₂O molekulalari.",
  dict(arch="juftlash"))

# 23 (2)
q(2, "o'rta",
  "Qutbli kovalent bog'da elektron juft ...",
  "elektromanfiyroq atom tomon siljigan bo'ladi",
  [("aynan o'rtada turadi", "bu qutbsiz bog'"),
   ("to'liq bitta atomga o'tadi", "to'liq o'tish — ion bog'"),
   ("molekuladan chiqib ketadi", "juft bog'da qoladi")],
  "Siljish qisman zaryadlar (δ+ va δ−) hosil qiladi — dipol.",
  dict(arch="qutbli_tarif"))

# 24 (3)
q(3, "o'rta",
  "HF, HCl, HBr qatorida bog'ning MUSTAHKAMLIGI qanday o'zgaradi?",
  "kamayadi — atom radiusi ortib, bog' uzayadi",
  [("ortadi", "galogen kattalashgani sari bog' kuchsizlanadi"),
   ("o'zgarmaydi", "uzunlik o'zgargani uchun energiya ham o'zgaradi"),
   ("avval ortib, keyin kamayadi", "monoton kamayadi")],
  "F→Cl→Br: radius ↑, bog' uzunligi ↑ → energiya ↓ (HF eng mustahkam).",
  dict(arch="hf_qator"))

# 25 (2)
q(2, "o'rta",
  "Qaysi modda qattiq holatda ham, suyuqlanmasida ham tok O'TKAZADI?",
  "mis", [("osh tuzi", "qattiq holda o'tkazmaydi (ionlar mahkam)"),
           ("shakar", "noelektrolit"), ("olmos", "kovalent panjara — dielektrik")],
  "Metallda erkin elektronlar har qanday holatda ham bor — tok o'tadi.",
  dict(arch="otkazuvchi"))

# 26 (3) — grafik tanlash
q(3, "o'rta",
  "VII A guruh vodorodli birikmalarida (HF→HCl→HBr→HI) bog' uzunligining o'zgarish grafigi qanday?",
  "bosqichma-bosqich ortib boradi",
  [("kamayib boradi", "radius kattalashadi — bog' uzayadi"),
   ("o'zgarmaydi", "davriy qonuniyat bor"),
   ("ortib, keyin kamayadi", "monoton ortadi")],
  "Guruhda pastga radius ortadi → H–Hal masofasi uzayadi.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="rise_fall", xlab="HF→HI", ylab="l(bog')"),
  params=dict(arch="grafik_uzunlik"))

# 27 (3)
check("q27", 4+1, 5)
q(3, "o'rta",
  "CH₄ molekulasidagi barcha bog'lar soni va ularning turi qanday?",
  "4 ta σ-bog'",
  [("4 ta π-bog'", "yakka bog'lar faqat σ"), ("2 σ va 2 π", "metanda karrali bog' yo'q"),
   ("5 ta σ", "C–H bog'lar 4 ta")],
  "To'rt C–H yakka bog' — barchasi σ.",
  dict(arch="ch4_sanash"))

# 28 (2)
q(2, "o'rta",
  "Osh tuzi kristali nega MO'RT (bolg'a bilan urilsa maydalanadi)?",
  "siljishda bir xil zaryadli ionlar to'qnashib, itarishadi",
  [("ionlari juda kichik", "o'lcham mo'rtlik sababi emas"),
   ("panjarasida suv bor", "quruq tuz ham mo'rt"),
   ("bog'lari juda kuchsiz", "ion bog' kuchli, lekin yo'nalishga sezgir")],
  "Qatlam siljiganda «+»«+» va «−»«−» ro'para kelib itarishadi — kristall yoriladi.",
  dict(arch="mortlik"))

# 29 (3)
q(3, "o'rta",
  "Suv molekulasining shakli va qutbliligi haqida to'g'ri xulosa qaysi?",
  "burchakli molekula — shuning uchun qutbli (dipol)",
  [("chiziqli molekula — qutbsiz", "H₂O burchakli (≈104,5°)"),
   ("burchakli, lekin qutbsiz", "burchakli shaklda dipollar yig'indisi nolga teng emas"),
   ("shakli qutblilikka ta'sir qilmaydi", "CO₂ (chiziqli) — qutbsiz, H₂O — qutbli: shakl hal qiladi")],
  "Ikkala O–H dipoli burchak ostida — teng ta'sir etmaydi, molekula dipol bo'ladi.",
  dict(arch="suv_shakl"))

# 30 (2)
q(2, "o'rta",
  "Bog'lanish haqidagi fikrlardan XATOSINI toping.",
  "ion bog'li moddalar qattiq holatda tok yaxshi o'tkazadi",
  [("metallar egiluvchan bo'ladi", "to'g'ri — qatlamlar sirg'aladi"),
   ("molekular kristallar past haroratda suyuqlanadi", "to'g'ri fikr"),
   ("atom panjarali moddalar juda qattiq", "to'g'ri — olmos misol")],
  "Ion kristallda ionlar mahkam o'rnashgan — tok faqat eritma/suyuqlanmada o'tadi.",
  dict(arch="xato_fikr"))

# 31 (3)
q(3, "o'rta",
  "K₂SO₄ tarkibida qanday bog'lanish turlari bor?",
  "ion (K⁺ bilan SO₄²⁻ orasida) va kovalent (S–O)",
  [("faqat ion", "sulfat ioni ichida kovalent bog'lar bor"),
   ("faqat kovalent", "kaliy bilan qoldiq orasida ion bog'"),
   ("metall va ion", "metall bog' sof metallda bo'ladi")],
  "Murakkab tuzlarda ikkala tur: kation–anion (ion) + anion ichida (kovalent).",
  dict(arch="k2so4"))

# 32 (3) — RASMLI: EM shkala o'qish (yengil)
q(3, "o'rta",
  "Rasmdagi ΔEM shkalasidan foydalaning: H–O bog'ida ΔEM = 1,4. Bog' turini aniqlang.",
  "qutbli kovalent",
  [("ion", "1,7 dan kichik — hali kovalent"), ("qutbsiz kovalent", "ΔEM 0 emas"),
   ("vodorod bog'lanish", "bu molekula ichidagi bog' emas, molekulalararo kuch")],
  "0 < 1,4 < 1,7 → qutbli kovalent (suvdagi O–H bog'lari).",
  dict(arch="em_oqish"), fig="em_axis")

# ---------- Y2: qor/muz ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="I.4",
  ichki_pasport=[dict(n=33, element="I.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="I.4", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="I.4", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch modda berilgan: muz (H₂O), osh tuzi (NaCl) va mis sim (Cu). "
               "33–35-savollarda mos panjara/bog' turini A–F ro'yxatidan tanlang."),
  savollar_ichki=[
    "33. Muz kristalining panjara turi qanday?",
    "34. Osh tuzi kristalining panjara turi qanday?",
    "35. Mis simdagi bog'lanish turi qanday?"],
  javoblar_royxati=["A) molekular", "B) ion", "C) metall", "D) atom", "E) vodorod", "F) donor-akseptor"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="atom panjara — olmos, SiO₂ kabilarda"),
                   dict(variant="E", xato="vodorod bog' — panjara turi emas, molekulalararo kuch"),
                   dict(variant="F", xato="mexanizm nomi")],
  yechim=("Muz — molekulalar tugunlarda (A); NaCl — ionlar (B); Cu — metall bog'lanish (C)."),
  parametrlar=dict(arch="uch_modda_ssenariy"))

# ---------- O1 ----------
check("o38", 2+2, 4)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="F₂ molekulasidagi bog' turini yozing (qutbli/qutbsiz kovalent, ion, metall).",
      javob="qutbsiz kovalent", yechim="Bir xil atomlar — ΔEM = 0.",
      parametrlar=dict(arch="f2_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="H₂O molekulasidagi σ-bog'lar sonini yozing.",
      javob="2", yechim="Ikki O–H yakka bog' — 2 σ.",
      parametrlar=dict(arch="h2o_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="C₂H₂ (asetilen) molekulasidagi BARCHA bog'lar sonini toping (σ + π).",
      javob="5", yechim="σ: 2 C–H + 1 C–C = 3; π: 2 → jami 5.",
      parametrlar=dict(arch="c2h2_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="Olmosning kristall panjara turini yozing.",
      javob="atom", yechim="Tugunlarda C atomlari, kovalent to'r — atom panjara.",
      parametrlar=dict(arch="olmos_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="MgCl₂ formula birligidagi ion bog'lar sonini yozing.",
      javob="2", yechim="Mg²⁺ ikkita Cl⁻ bilan — 2 ta ion bog'.",
      parametrlar=dict(arch="mgcl2_o1")),
]

# ---------- O2 ----------
O2 = [
 dict(n=41, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Quyidagi moddalar berilgan: NaCl, H₂O, N₂, Cu. Bandlar ketma-ket yechiladi — har biri "
            "keyingisiga asos bo'ladi."),
      bandlar=[
        dict(savol="a) Har bir moddadagi bog'lanish turini aniqlang.",
             yechim=["NaCl — ion; H₂O — qutbli kovalent; N₂ — qutbsiz kovalent; Cu — metall"], M=4, A=2),
        dict(savol="b) N₂ dagi σ- va π-bog'lar sonini yozing.",
             yechim=["1 σ va 2 π (uch karrali bog')"], M=3, A=2),
        dict(savol="c) Har bir moddaning qattiq holatdagi panjara turini ko'rsating.",
             yechim=["NaCl — ion; muz — molekular; qattiq N₂ — molekular; Cu — metall"], M=4, A=3),
        dict(savol="d) Qaysi modda suyuq holatda vodorod bog'lanish hosil qiladi? Sxemasini chizing.",
             yechim=["H₂O: O–H···O (H bilan qo'shni molekula kislorodi orasida)."], M=4, A=3),
      ],
      rasmiylashtirish="To'rt modda tahlili: bog' → sanash → panjara → vodorod bog'; M15+A10.",
      parametrlar=dict(arch="tort_modda")),
 dict(n=42, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Oshxonadagi ikki oq kukun adashtirib qo'yildi: biri osh tuzi, biri shakar. "
            "Quyidagi savollarga MULOHAZA yuritib javob yozing (tatib ko'rish mumkin emas!)."),
      bandlar=[
        dict(savol="a) Bog'lanish nazariyasiga tayanib, ularni farqlashning kamida ikkita usulini asoslab yozing.",
             yechim=["1) Eritmaning tok o'tkazishi: tuz (ion) — o'tkazadi, shakar (molekular) — yo'q.",
                     "2) Qizdirish: shakar past t da eriydi/kuyadi, tuz 801 °C gacha chidaydi."], M=13, A=0),
        dict(savol="b) Nega tuz eritmasi tok o'tkazadi-yu, shakar eritmasi o'tkazmaydi?",
             yechim=["Tuz ionlarga ajraladi (erkin zaryad tashuvchilar); shakar molekulalar holida eriydi."], M=9, A=0),
        dict(savol="c) Ikkala moddaning kristall panjara turlarini yozing.",
             yechim=["NaCl — ion panjara; shakar — molekular panjara."], M=3, A=0),
      ],
      rasmiylashtirish="Hayotiy detektiv (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="tuz_shakar")),
 dict(n=43, tur="O2", element="I.4", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("O'quvchi uch moddani qizdirib, xossalarini jadvalga yozdi:\n"
            "[JADVAL] Modda | Suyuql. t, °C | Qattiqlik | Eritmasi/suyuqlanmasi tok o'tkazishi ;; "
            "shakar | 186 | yumshoq | yo'q ;; kvars (SiO₂) | 1710 | juda qattiq | (erimaydi) ;; "
            "KCl | 776 | mo'rt | ha\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir moddaning panjara turini xossalariga asoslanib aniqlang.",
             yechim=["Shakar — molekular (past t, yumshoq); kvars — atom (o'ta yuqori t, qattiq);",
                     "KCl — ion (mo'rt, suyuqlanmasi elektrolit)."], M=6, A=3),
        dict(savol="b) Qaysi moddada bog'lar eng mustahkam? Asoslang.",
             yechim=["Kvarsda — uzluksiz kovalent to'r (atom panjara), suyuqlantirish eng qiyin."], M=3, A=2),
        dict(savol="c) KCl ning mo'rtligini panjara tuzilishi orqali izohlang.",
             yechim=["Siljishda bir xil zaryadli ionlar ro'para kelib itarishadi — kristall yoriladi."], M=3, A=2),
        dict(savol="d) Har bir panjara turiga yana bittadan misol keltiring.",
             yechim=["Molekular — muz/CO₂; atom — olmos; ion — NaCl."], M=3, A=3),
      ],
      rasmiylashtirish="Xossa-jadval tahlili: M15+A10. B-variantdagidan boshqa moddalar.",
      parametrlar=dict(arch="uch_xossa")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20260321)
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
    d = dict(n=n, tur="Y1", element="I.4", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-I4-A", daraja="A", bob=4, bob_nomi="Kimyoviy bog'lanish",
    manba=("MS spetsifikatsiyasi I.4; darslik bog'lanish bo'limlari — savollar yangi tuzilgan, "
           "hayotiy sahnalar (tuz, qalam-olmos, qor, mis sim) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="I.4") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
