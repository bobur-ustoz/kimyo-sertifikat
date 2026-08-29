# -*- coding: utf-8 -*-
"""15-bob A-varianti: Metallmaslar. Vodorod. Mineral o'g'itlar (II.5) — O'RGATUVCHI ★★.
Hayotiy sahnalar: gugurt, nashatir spirti, selitra granulalari, «tuxum hidi» (H2S)."""
import json, random

OUT = "mavzu_II5A.json"
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
  "Metallmaslar davriy jadvalning qaysi qismida joylashgan?",
  "o'ng yuqori burchagida",
  [("chap pastki burchagida", "u yer — eng faol metallar"),
   ("faqat o'rtasida", "o'rtada d-metallar"),
   ("faqat 1-davrda", "metallmaslar bir necha davrda bor")],
  "B–At diagonalidan o'ngda va yuqorida — metallmaslar hududi.",
  dict(arch="metallmas_orni"))

# 2 (2)
q(2, "quyi",
  "Vodorod haqida qaysi fikr TO'G'RI?",
  "eng yengil gaz",
  [("eng og'ir gaz", "aksincha — havodan 14,5 marta yengil"),
   ("sariq rangli gaz", "rangsiz"),
   ("o'tkir hidli gaz", "hidsiz")],
  "H₂ — rangsiz, hidsiz, eng yengil gaz; koinotda eng ko'p tarqalgan element.",
  dict(arch="h2_fakt"))

# 3 (2)
q(2, "o'rta",
  "Xlor gazi qanday ko'rinishga ega va u qanday xususiyatli?",
  "sariq-yashil rangli, o'tkir hidli, zaharli",
  [("rangsiz va hidsiz", "aynan rangi va hidi bilan taniladi"),
   ("qo'ng'ir rangli", "qo'ng'ir — NO₂ yoki brom bug'i"),
   ("ko'k rangli, xushbo'y", "xlorda «xushbo'ylik» yo'q")],
  "Cl₂ — «xlorka» hidli zaharli gaz; nomi yunoncha «yashil»dan.",
  dict(arch="cl2_korinish"))

# 4 (2) — SAHNA: gugurt
q(2, "o'rta",
  "Rasmda gugurt cho'pi: boshchasi tarkibida oltingugurt va oksidlovchi (bertole tuzi) bor. "
  "Chaqilganda nima yuz beradi?",
  "ishqalanish issiqligidan aralashma alangalanib, yog'ochni yondiradi",
  [("cho'p o'z-o'zidan yonadi", "ishqalanishsiz yonmaydi"),
   ("boshchada suv bug'lanadi", "yonish reaksiyasi boradi"),
   ("faqat tutun chiqadi", "alanga hosil bo'ladi")],
  "Ishqalanish → mahalliy qizish → S va oksidlovchi reaksiyasi → alanga. Qutidagi qatlamda qizil fosfor bor.",
  dict(arch="gugurt_sahna"), fig="matches")

# 5 (2)
q(2, "o'rta",
  "Laboratoriyada kislorod qanday olinadi?",
  "KMnO₄ ni qizdirib parchalash orqali",
  [("havoni filtrlash orqali", "filtr gazlarni ajratmaydi"),
   ("suvni qaynatish orqali", "qaynash — fizik jarayon"),
   ("ohaktoshni kuydirish orqali", "u CO₂ beradi")],
  "2KMnO₄ → K₂MnO₄ + MnO₂ + O₂↑ (yoki H₂O₂ parchalash).",
  dict(arch="o2_olinish"))

# 6 (2)
q(2, "o'rta",
  "Azot molekulasi (N₂) oddiy sharoitda nega juda INERT?",
  "atomlar orasida mustahkam uch bog' bor",
  [("azot umuman reaksiyaga kirishmaydi", "yuqori haroratda kirishadi"),
   ("molekulasi juda og'ir", "N₂ havodan biroz yengil"),
   ("azot inert gazlar guruhida", "u V A guruhda")],
  "N≡N bog'ini uzish uchun juda katta energiya kerak — shu bois azot «dangasa».",
  dict(arch="n2_inert"))

# 7 (2)
q(2, "o'rta",
  "Ammiak (NH₃) qanday xossalarga ega?",
  "o'tkir hidli, rangsiz, suvda juda yaxshi eriydigan gaz",
  [("hidsiz og'ir gaz", "hidi juda o'tkir, havodan yengil"),
   ("sariq rangli suyuqlik", "oddiy sharoitda gaz"),
   ("suvda erimaydigan gaz", "1 hajm suvda ~700 hajm NH₃ eriydi!")],
  "NH₃ — «nashatir» hidi; eritmasi ishqoriy muhit beradi.",
  dict(arch="nh3_xossa"))

# 8 (2) — SAHNA: nashatir spirti
q(2, "o'rta",
  "Rasmda nashatir spirti flakoni: hushidan ketgan odamga hidlatiladi. Ta'sir mexanizmi qanday?",
  "o'tkir hidli NH₃ nafas retseptorlarini qo'zg'atib, miyani «uyg'otadi»",
  [("NH₃ kislorod beradi", "tarkibida ajraladigan O₂ yo'q"),
   ("suyuqlik yuzni sovutadi", "flakon teriga tekkizilmaydi"),
   ("spirt kayfiyatni ko'taradi", "bu etil spirti emas — ammiak eritmasi")],
  "10 % li NH₃ eritmasi — refleksli qo'zg'atuvchi; ehtiyotkorlik bilan ishlatiladi.",
  dict(arch="nashatir_sahna"), fig="ammonia")

# 9 (2)
q(2, "o'rta",
  "Galogenlar ichida ENG FAOL element qaysi?",
  "F", [("Cl", "ikkinchi o'rinda"), ("Br", "faollik pastga kamayadi"), ("I", "eng passiv (barqaror)")],
  "Ftor — barcha elementlar ichida eng kuchli oksidlovchi; hatto suv bilan reaksiyaga kirishadi.",
  dict(arch="eng_faol_galogen"))

# 10 (3)
check("q10", 2.24/22.4*2*36.5, 7.3)
q(3, "o'rta",
  "H₂ + Cl₂ → 2HCl. 2,24 L (n.sh.) vodorod to'liq reaksiyaga kirishganda necha gramm vodorod xlorid "
  "hosil bo'ladi? (M(HCl)=36,5)",
  "7,3 g", [("3,65 g", "koeffitsiyent 2 unutilgan"), ("36,5 g", "1 mol uchun"), ("14,6 g", "ikki baravar")],
  "n(H₂) = 0,1 → n(HCl) = 0,2 mol → m = 7,3 g.",
  dict(arch="hcl_hisob"))

# 11 (2)
q(2, "o'rta",
  "Fosforning qaysi allotropik shakli ZAHARLI va qorong'ida yog'du sochadi?",
  "oq fosfor", [("qizil fosfor", "u nisbatan xavfsiz — gugurt qutisida"),
                 ("qora fosfor", "barqaror, yog'du sochmaydi"), ("hammasi bir xil", "shakllar keskin farq qiladi")],
  "P₄ (oq) — zaharli, o'z-o'zidan alangalanadi, suv ostida saqlanadi.",
  dict(arch="fosfor_allotrop"))

# 12 (3)
check("q12", 3.2/32*22.4, 2.24)
q(3, "o'rta",
  "S + O₂ → SO₂. 3,2 g oltingugurt yonganda hosil bo'lgan gaz hajmini (n.sh.) toping. (M(S)=32)",
  "2,24 L", [("22,4 L", "1 mol uchun"), ("4,48 L", "ikki baravar"), ("1,12 L", "yarmi")],
  "n = 0,1 mol → V(SO₂) = 2,24 L.",
  dict(arch="so2_hisob"))

# 13 (2) — SAHNA: selitra
q(2, "o'rta",
  "Rasmda ammiakli selitra (NH₄NO₃) granulalari. Bu modda qishloq xo'jaligida nima uchun "
  "qo'llaniladi?",
  "azotli o'g'it — o'simlik ko'kargan massasini oshiradi",
  [("zararkunandalarga qarshi", "u o'g'it, zahar emas"),
   ("tuproqni yumshatish uchun", "mexanik emas — oziqlanish"),
   ("faqat portlovchi sifatida", "asosiy ishlatilishi — o'g'it")],
  "NH₄NO₃ — 35 % azotli eng «to'yimli» o'g'itlardan; quruq, salqin joyda saqlanadi.",
  dict(arch="selitra_sahna"), fig="selitra")

# 14 (2)
q(2, "o'rta",
  "Olmos va grafit bir elementning shakllari. Bu qaysi element va hodisa nomi?",
  "uglerod; allotropiya",
  [("kremniy; izomeriya", "element ham, atama ham noto'g'ri"),
   ("uglerod; izotopiya", "izotoplar yadro farqi, bu — tuzilish farqi"),
   ("fosfor; allotropiya", "olmos-grafit fosfor emas")],
  "Bitta element — har xil kristall tuzilish: eng qattiq (olmos) va yumshoq (grafit).",
  dict(arch="uglerod_allotrop"))

# 15 (2)
q(2, "o'rta",
  "Vodorod gazini probirkaga qanday yig'ish to'g'ri?",
  "probirkani TESKARI (og'zi pastga) tutib",
  [("og'zi yuqoriga tutib", "yengil gaz uchib chiqib ketadi"),
   ("suv ostida yig'ib bo'lmaydi", "suv ustida ham yig'sa bo'ladi — erimaydi"),
   ("farqi yo'q", "zichlik farqi muhim")],
  "H₂ havodan yengil — teskari idishda «to'planib» qoladi.",
  dict(arch="h2_yigish"))

# 16 (3)
q(3, "o'rta",
  "Jadvaldagi «?» kataklarni to'ldiring:\n"
  "[JADVAL] Gaz | Rangi ;; Cl₂ | ? ;; NH₃ | ? ;; NO₂ | qo'ng'ir",
  "sariq-yashil; rangsiz",
  [("rangsiz; sariq-yashil", "teskari"), ("qo'ng'ir; rangsiz", "qo'ng'ir — NO₂"),
   ("sariq-yashil; ko'k", "NH₃ rangsiz")],
  "Cl₂ — sariq-yashil; NH₃ — rangsiz (lekin o'tkir hidli).",
  dict(arch="gaz_rang_jadval"))

# 17 (2)
q(2, "quyi",
  "Mineral o'g'itlar qaysi uch asosiy oziq elementni beradi?",
  "N, P, K", [("H, O, C", "bularni o'simlik havo-suvdan oladi"), ("Fe, Cu, Zn", "bular mikroelementlar"),
               ("Na, Cl, S", "asosiy uchlik emas")],
  "Azotli, fosforli va kaliyli o'g'itlar — «NPK» formulasi.",
  dict(arch="npk"))

# 18 (2) — SAHNA: tuxum hidi
q(2, "o'rta",
  "Rasmda buloq suvi: undan «palag'da tuxum» hidi keladi. Bu hid qaysi gazdan?",
  "vodorod sulfid (H₂S)",
  [("ammiak", "NH₃ hidi boshqacha — «nashatir»"),
   ("karbonat angidrid", "CO₂ hidsiz"),
   ("xlor", "xlor hidi «xlorka»day")],
  "H₂S — zaharli gaz; ozgina miqdori ham kuchli hid beradi — bu tabiiy «ogohlantirish».",
  dict(arch="h2s_sahna"), fig="egg")

# 19 (3)
check("q19", 0.3/3*2*22.4, 4.48)
q(3, "o'rta",
  "N₂ + 3H₂ → 2NH₃. 0,3 mol vodorod to'liq reaksiyaga kirishganda hosil bo'lgan ammiak hajmini "
  "(n.sh.) toping.",
  "4,48 L", [("6,72 L", "nisbat 3:2, teng emas"), ("2,24 L", "0,1 mol deb olingan"),
              ("22,4 L", "1 mol uchun")],
  "n(NH₃) = 0,3·2/3 = 0,2 mol → V = 4,48 L.",
  dict(arch="nh3_hajm_hisob"))

# 20 (2)
q(2, "o'rta",
  "Kremniy qaysi sohaning «asosiy materiali» hisoblanadi?",
  "elektronika — mikrosxemalar (yarimo'tkazgich)",
  [("oziq-ovqat sanoati", "Si iste'mol qilinmaydi"),
   ("yoqilg'i sanoati", "kremniy yonilg'i emas"),
   ("to'qimachilik", "mato Si dan emas")],
  "Si — yarimo'tkazgich: protsessorlar, quyosh panellari.",
  dict(arch="si_ishlatish"))

# 21 (2)
q(2, "o'rta",
  "Superfosfat qaysi turdagi o'g'it?",
  "fosforli", [("azotli", "tarkibida asosiy element — P"), ("kaliyli", "K yo'q"),
                ("mikroo'g'it", "asosiy (makro) o'g'it")],
  "Superfosfat — Ca(H₂PO₄)₂ asosidagi eng keng tarqalgan fosforli o'g'it.",
  dict(arch="superfosfat"))

# 22 (2)
q(2, "o'rta",
  "Kislorod (O₂) va ozon (O₃) bir-biriga nisbatan nima hisoblanadi?",
  "bitta elementning allotropik shakllari",
  [("izotoplar", "izotop — yadro farqi"), ("izomerlar", "atama organik kimyodan"),
   ("har xil elementlar", "ikkalasi ham kislorod elementi")],
  "O₂ — nafas gazi; O₃ — o'tkir hidli, kuchli oksidlovchi «momaqaldiroq gazi».",
  dict(arch="ozon_allotrop"))

# 23 (3)
check("q23", 6.2/31/4*2*142, 14.2)
q(3, "o'rta",
  "4P + 5O₂ → 2P₂O₅. 6,2 g fosfor yonganda hosil bo'lgan oksid massasini toping. (M: P=31, P₂O₅=142)",
  "14,2 g", [("28,4 g", "nisbat 4:2 = 2:1"), ("142 g", "1 mol uchun"), ("7,1 g", "yana ikkiga bo'lingan")],
  "n(P) = 0,2 → n(P₂O₅) = 0,1 mol → m = 14,2 g.",
  dict(arch="p2o5_hisob"))

# 24 (2)
q(2, "o'rta",
  "Ichimlik suvini zararsizlantirishda qaysi metallmas (yoki uning birikmalari) ishlatiladi?",
  "xlor", [("azot", "inert — mikroblarni o'ldirmaydi"), ("uglerod", "ko'mir faqat filtrlaydi"),
            ("kremniy", "qum ham faqat mexanik filtr")],
  "Xlorlash (yoki ozonlash) — mikroorganizmlarni yo'q qiladi.",
  dict(arch="suv_xlorlash"))

# 25 (3)
q(3, "o'rta",
  "Nitrat kislota ishlab chiqarish zanjiridagi X ni aniqlang: NH₃ → NO → X → HNO₃.",
  "NO₂", [("N₂O", "«kuldiruvchi gaz» bu zanjirda emas"), ("N₂", "azotga qaytish emas"),
           ("NH₄NO₃", "tuz — zanjir mahsuloti emas")],
  "2NO + O₂ → 2NO₂; 4NO₂ + O₂ + 2H₂O → 4HNO₃.",
  dict(arch="hno3_zanjir_x"))

# 26 (3) — RASMLI: havo tarkibi
q(3, "o'rta",
  "Diagrammada quruq havoning tarkibi berilgan. Havoda ENG KO'P gaz qaysi?",
  "azot (78 %)", [("kislorod (21 %)", "ikkinchi o'rinda"), ("argon (~1 %)", "uchinchi"),
                   ("karbonat angidrid", "atigi 0,04 %")],
  "Havo — asosan azot: shu bois yonish «sekinlashtirilgan».",
  dict(arch="bar_havo_oqish"), fig="bar_havo")

# 27 (3)
check("q27", 2.4/12*22.4, 4.48)
q(3, "o'rta",
  "C + O₂ → CO₂. 2,4 g ko'mir to'liq yonganda hosil bo'lgan gaz hajmini (n.sh.) toping. (M(C)=12)",
  "4,48 L", [("2,24 L", "0,1 mol deb olingan"), ("22,4 L", "1 mol uchun"), ("44,8 L", "nol adashgan")],
  "n = 0,2 mol → V(CO₂) = 4,48 L.",
  dict(arch="co2_hajm_hisob"))

# 28 (2) — RASMLI: havo reuse
q(2, "o'rta",
  "26-savol diagrammasidan: nafas olishimiz uchun zarur kislorod havoning qancha qismini tashkil "
  "etadi?",
  "taxminan beshdan bir qismini (21 %)",
  [("yarmini", "yarmi emas — 21 %"), ("deyarli hammasini", "asosiy qism — azot"),
   ("mingdan birini", "bu CO₂ ulushiga yaqin")],
  "O₂ — 21 %: shu «beshdan bir» butun tiriklikni ta'minlaydi.",
  dict(arch="bar_havo_o2"), fig="bar_havo")

# 29 (3) — grafik tanlash
q(3, "o'rta",
  "Galogenlar qatorида (F₂ → Cl₂ → Br₂ → I₂) qaynash harorati qanday o'zgaradi? Grafikni tanlang.",
  "ortib boradi",
  [("kamayadi", "molekula og'irlashgani sari qaynash qiyinlashadi"),
   ("o'zgarmaydi", "F₂ gaz, I₂ esa qattiq-ku"),
   ("avval kamayib, keyin ortadi", "monoton ortadi")],
  "Molekulalararo tortishuv kattalashadi: F₂, Cl₂ — gaz; Br₂ — suyuq; I₂ — qattiq.",
  svg=dict(correct="rise", d1="fall", d2="flat", d3="u", xlab="F₂→I₂", ylab="t(qayn.)"),
  params=dict(arch="galogen_grafik"))

# 30 (2)
q(2, "o'rta",
  "Vodorod bilan ishlashda qaysi xavf hisobga olinadi?",
  "havo bilan aralashmasi portlovchi («qaldiroq gaz»)",
  [("zaharliligi", "H₂ zaharsiz"), ("o'tkir hidi", "hidsiz"),
   ("suvda kuchli erishi", "deyarli erimaydi")],
  "2H₂ + O₂ aralashmasi uchqundan portlaydi — tozalikni «pop» sinovi bilan tekshirishadi.",
  dict(arch="h2_xavf"))

# 31 (3)
check("q31", 0.1*53.5, 5.35)
q(3, "o'rta",
  "NH₃ + HCl → NH₄Cl. 0,1 mol ammiak to'liq reaksiyaga kirishganda hosil bo'lgan tuz massasini "
  "toping. (M(NH₄Cl)=53,5)",
  "5,35 g", [("53,5 g", "1 mol uchun"), ("10,7 g", "ikki baravar"), ("3,65 g", "bu HCl dan olingan xato")],
  "n = 0,1 mol → m = 5,35 g — «oq tutun» reaksiyasi.",
  dict(arch="nh4cl_hisob"))

# 32 (3) — RASMLI: havo hisob
check("q32", 100*0.78, 78)
q(3, "o'rta",
  "26-savol diagrammasidan foydalaning: 100 L havoda taxminan necha litr azot bor?",
  "78 L", [("21 L", "bu kislorod"), ("50 L", "azot ko'proq"), ("100 L", "havo faqat azot emas")],
  "V(N₂) = 100 · 0,78 = 78 L.",
  dict(arch="bar_havo_hisob"), fig="bar_havo")

# ---------- Y2: uch gaz ssenariysi ----------
Y2 = dict(
  n=33, tur="Y2", element="II.5",
  ichki_pasport=[dict(n=33, element="II.5", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=34, element="II.5", qiyinlik=2, kognitiv="o'rta"),
                 dict(n=35, element="II.5", qiyinlik=3, kognitiv="yuqori")],
  matn_umumiy=("Uch probirkada rangsiz gazlar bor: X — cho'g'lanib turgan cho'pni alangalatib "
               "yuboradi; Y — yoqilganda «pop» tovush beradi; Z — o'tkir hidli, nam lakmus qog'ozni "
               "ko'kartiradi. 33–35-savollarga A–F ro'yxatidan javob tanlang."),
  savollar_ichki=[
    "33. X gaz qaysi?",
    "34. Y gaz qaysi?",
    "35. Z gaz suvda eriganida qanday muhit hosil bo'ladi?"],
  javoblar_royxati=["A) O₂", "B) H₂", "C) ishqoriy", "D) CO₂", "E) N₂", "F) kislotali"],
  javoblar={"33": "A", "34": "B", "35": "C"},
  chalgituvchilar=[dict(variant="D", xato="CO₂ cho'pni o'chiradi, alangalatmaydi"),
                   dict(variant="E", xato="N₂ «pop» bermaydi — u yonmaydi"),
                   dict(variant="F", xato="NH₃ eritmasi ishqoriy — lakmus shuning uchun ko'k")],
  yechim=("X — kislorod (yonishni quvvatlaydi). Y — vodorod («pop»). "
          "Z — ammiak: NH₃ + H₂O ⇄ NH₄OH — ishqoriy muhit (C)."),
  parametrlar=dict(arch="uch_gaz_ssenariy"))

# ---------- O1 ----------
check("o36", 0.2*17, 3.4)
check("o37", 4.48/22.4, 0.2)
check("o38", 4.48/22.4*18, 3.6)
check("o39", 5.6/28*2*22.4, 8.96)
check("o40", 1.6/32*64, 3.2)
O1 = [
 dict(n=36, qiyinlik=2, kognitiv="o'rta",
      savol="0,2 mol ammiakning massasini (g) toping. (M(NH₃)=17)",
      javob="3,4", yechim="m = 0,2·17 = 3,4 g.",
      parametrlar=dict(arch="nh3_massa_o1")),
 dict(n=37, qiyinlik=2, kognitiv="o'rta",
      savol="4,48 L (n.sh.) xlor gazi necha mol bo'ladi?",
      javob="0,2", yechim="n = 4,48/22,4 = 0,2 mol.",
      parametrlar=dict(arch="cl2_mol_o1")),
 dict(n=38, qiyinlik=3, kognitiv="o'rta",
      savol="2H₂ + O₂ → 2H₂O. 4,48 L (n.sh.) vodorod yonganda hosil bo'lgan suv massasini (g) toping. "
            "(M(H₂O)=18)",
      javob="3,6", yechim="n(H₂) = 0,2 → n(H₂O) = 0,2 mol → m = 3,6 g.",
      parametrlar=dict(arch="suv_hisob_o1")),
 dict(n=39, qiyinlik=3, kognitiv="o'rta",
      savol="N₂ + 3H₂ → 2NH₃. 5,6 g azot to'liq reaksiyaga kirishganda hosil bo'lgan ammiak hajmini "
            "(n.sh., L) toping. (M(N₂)=28)",
      javob="8,96", yechim="n(N₂) = 0,2 → NH₃ 0,4 mol → V = 8,96 L.",
      parametrlar=dict(arch="nh3_o1")),
 dict(n=40, qiyinlik=3, kognitiv="yuqori",
      savol="S + O₂ → SO₂. 1,6 g oltingugurt yonganda hosil bo'lgan gaz massasini (g) toping. "
            "(M: S=32, SO₂=64)",
      javob="3,2", yechim="n = 0,05 mol → m(SO₂) = 3,2 g.",
      parametrlar=dict(arch="so2_massa_o1")),
]

# ---------- O2 ----------
check("o41b", 6.5/65*22.4, 2.24)
O2 = [
 dict(n=41, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Laboratoriyada vodorod olish va tekshirish topshirig'i berildi. Bandlar ketma-ket "
            "yechiladi."),
      bandlar=[
        dict(savol="a) Vodorod olishning laboratoriya usuli tenglamasini yozing.",
             yechim=["Zn + 2HCl → ZnCl₂ + H₂↑."], M=4, A=2),
        dict(savol="b) 6,5 g rux ishlatilganda ajraladigan vodorod hajmini hisoblang. (M(Zn)=65)",
             yechim=["n = 0,1 mol → V = 2,24 L."], M=4, A=3),
        dict(savol="c) Gazni qanday yig'ish va tozaligini qanday tekshirish kerak?",
             yechim=["Teskari probirkada (havodan yengil); alangaga tutilganda «pop» tovushi."], M=4, A=3),
        dict(savol="d) Toza vodorod yonishining tenglamasini yozing va mahsulotni ayting.",
             yechim=["2H₂ + O₂ → 2H₂O — faqat suv («eng toza yoqilg'i»)."], M=3, A=2),
      ],
      rasmiylashtirish="Vodorod zanjiri: olinish → hisob → yig'ish/sinash → yonish; M15+A10.",
      parametrlar=dict(arch="h2_lab_zanjir")),
 dict(n=42, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Havo 78 % azotdan iborat, lekin dehqonlar azotli o'g'itlarga pul sarflaydi. "
            "Quyidagilarga MULOHAZA yuritib javob yozing."),
      bandlar=[
        dict(savol="a) Nega o'simliklar havodagi azotni bevosita o'zlashtira olmaydi va bu muammo "
                   "qanday hal qilinadi?",
             yechim=["N₂ dagi uch bog' juda mustahkam — o'simlik uni «ochib» ololmaydi.",
                     "Sanoatda azot NH₃ ga bog'lanadi (Gaber usuli) va o'g'itlarga aylantiriladi."], M=13, A=0),
        dict(savol="b) Nega momaqaldiroqli yomg'irdan keyin o'simliklar yaxshi ko'karadi?",
             yechim=["Chaqmoq energiyasida N₂ + O₂ → 2NO; keyin NO₂ va nitrat hosil bo'lib, yomg'ir "
                     "bilan tuproqqa «tabiiy o'g'it» tushadi."], M=9, A=0),
        dict(savol="c) Ikkita azotli o'g'it formulasini yozing.",
             yechim=["NH₄NO₃, (NH₄)₂SO₄ (yoki CO(NH₂)₂)."], M=3, A=0),
      ],
      rasmiylashtirish="Azot-mulohaza (faqat M): M13+M9+M3 = 25.",
      parametrlar=dict(arch="azot_mulohaza")),
 dict(n=43, tur="O2", element="II.5", qiyinlik=3, kognitiv="yuqori", jami=25,
      matn=("Uch mineral o'g'it jadvalda berilgan:\n"
            "[JADVAL] № | O'g'it | Formula ;; 1 | ammiakli selitra | NH₄NO₃ ;; "
            "2 | superfosfat (asosi) | Ca(H₂PO₄)₂ ;; 3 | silvin | KCl\n"
            "Bandlar ketma-ket yechiladi."),
      bandlar=[
        dict(savol="a) Har bir o'g'it qaysi oziq elementni berishini aniqlang.",
             yechim=["1 — azot (N); 2 — fosfor (P); 3 — kaliy (K)."], M=4, A=2),
        dict(savol="b) Har bir o'g'itdagi tuz sinfini ayting.",
             yechim=["NH₄NO₃ — o'rta tuz; Ca(H₂PO₄)₂ — nordon tuz; KCl — o'rta tuz."], M=4, A=3),
        dict(savol="c) Qaysi o'g'it kislotali tuproqlarga ehtiyotkorlik bilan solinadi va nima uchun?",
             yechim=["Ammiakli selitra — u tuproqni yana nordonlashtirishi mumkin."], M=4, A=3),
        dict(savol="d) «NPK 16:16:16» yozuvli kompleks o'g'it nimani bildiradi?",
             yechim=["Har uch elementdan (N, P₂O₅, K₂O hisobida) 16 % dan borligini."], M=3, A=2),
      ],
      rasmiylashtirish="O'g'itlar jadvali: element → sinf → qo'llash → NPK; M15+A10.",
      parametrlar=dict(arch="ogit_jadval_o2")),
]

# ---------- harflar ----------
letters = "ABCD"
rng = random.Random(20261503)
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
    d = dict(n=n, tur="Y1", element="II.5", qiyinlik=item["qiyinlik"], kognitiv=item["kognitiv"],
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
    variant="mavzu-II5-A", daraja="A", bob=15, bob_nomi="Metallmaslar. Vodorod. Mineral o'g'itlar",
    manba=("MS spetsifikatsiyasi II.5; 8-9-sinf darslik metallmaslar bo'limlari — savollar yangi "
           "tuzilgan, hayotiy sahnalar (gugurt, nashatir, selitra, H₂S hidi) bilan"),
    izoh=("A-varianti — O'RGATUVCHI ★★: soddaroq savollar, rasmli hayotiy misollar. "
          "B-variantdan arxetip-pozitsiya jihatidan farqli."),
    savollar=final_y1 + [Y2] + [dict(x, tur="O1", element="II.5") for x in O1] + O2,
)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(variant, f, ensure_ascii=False, indent=1)
print("Yozildi:", OUT)
