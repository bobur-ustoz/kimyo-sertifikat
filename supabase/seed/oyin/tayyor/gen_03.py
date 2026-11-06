from lib import *
E, P, B = ["etilen"], ["propilen"], ["buten"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Etanolning degidratlanishini yozing (konsentrlangan H₂SO₄, 170 °C)", ["C2H5OH"], ["C2H4", "H2O"], "C2H5OH→C2H4+H2O", "Suv ajraladi, qo'shbog' hosil bo'ladi: etilen.", E),
  W("Propanol-1 degidratlanishini yozing (konsentrlangan H₂SO₄, 170 °C)", ["C3H7OH"], ["C3H6", "H2O"], "C3H7OH→C3H6+H2O", "Spirtdan suv ajraladi, propen hosil bo'ladi.", P),
 ]),
 S("o-2", G, "write", 2, [
  W("Xloretanga KOH ning spirtdagi eritmasi ta'sir ettiring", ["C2H5Cl", "KOH"], ["C2H4", "KCl", "H2O"], "C2H5Cl+KOH→C2H4+KCl+H2O", "Spirtli ishqor galogenalkandan HCl ni tortib oladi: alken hosil bo'ladi.", E),
  W("2-brompropanga KOH ning spirtdagi eritmasi ta'sir ettiring", ["C3H7Br", "KOH"], ["C3H6", "KBr", "H2O"], "C3H7Br+KOH→C3H6+KBr+H2O", "HBr ajraladi va qo'shbog' hosil bo'ladi: propen.", P),
 ]),
 S("o-3", G, "choice", 1, [
  C("Laboratoriyada etilen olishning to'g'ri usuli qaysi?", "Etanolni konsentrlangan H₂SO₄ bilan 170 °C da qizdirish", ["Etanolni H₂SO₄ bilan 140 °C da qizdirish", "Etanni xlorlash", "Etanolga natriy ta'sir ettirish"], "170 °C da molekula ichida suv ajraladi va etilen hosil bo'ladi.", E, ("Etanolni H₂SO₄ bilan 140 °C da qizdirish", "140 °C da ikki molekula orasidan suv ajraladi va dietil efir hosil bo'ladi. Etilen uchun 170 °C kerak.")),
  C("Propanni katalizatorda qizdirsak, qaysi alken hosil bo'ladi?", "Propen", ["Propin", "Siklopropan", "Propanol"], "Degidrogenlashda propandan 2 vodorod ajralib propen hosil bo'ladi.", P, ("Propin", "Propin uchun 4 ta vodorod ajralishi kerak, bir bosqichda 2 ta ajraladi.")),
 ]),
 S("o-4", G, "choice", 2, [
  C("1,2-dibrombutanga rux ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "Buten-1", ["Butan", "Butin", "Siklobutan"], "Qo'shni uglerodlardagi ikki bromni rux oladi, qo'shbog' hosil bo'ladi.", B, ("Butan", "Rux vodorod qo'shmaydi, u faqat galogenni oladi. Butan hosil bo'lmaydi.")),
  C("1,3-dibrompropanga rux ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "Siklopropan", ["Propen", "Propan", "Propin"], "Bromlar chetki uglerodlarda joylashgan: ular o'zaro bog'lanib halqa hosil qiladi.", None, ("Propen", "Propen 1,2-dibrompropandan hosil bo'ladi. Bu yerda bromlar chetda, shuning uchun halqa.")),
 ]),
]
G = "Birikish (H₂, galogenlar)"
slots += [
 S("b-1", G, "write", 1, [
  W("Etilenning gidrogenlanishini yozing (Ni, qizdirish)", ["C2H4", "H2"], ["C2H6"], "C2H4+H2→C2H6", "Qo'shbog' ochiladi, ikki vodorod birikadi: etan.", E),
  W("Propenning gidrogenlanishini yozing (Ni, qizdirish)", ["C3H6", "H2"], ["C3H8"], "C3H6+H2→C3H8", "Qo'shbog' ochilib propan hosil bo'ladi.", P),
 ]),
 S("b-2", G, "write", 1, [
  W("Etilenga xlor ta'sir ettiring", ["C2H4", "Cl2"], ["C2H4Cl2"], "C2H4+Cl2→C2H4Cl2", "Xlor qo'shbog'ga birikadi: 1,2-dixloretan.", E),
  W("Propenga brom ta'sir ettiring (oddiy sharoitda)", ["C3H6", "Br2"], ["C3H6Br2"], "C3H6+Br2→C3H6Br2", "Brom qo'shbog'ga birikadi: 1,2-dibrompropan.", P),
 ]),
 S("b-3", G, "choice", 2, [
  C("Qaysi modda bromli suvni rangsizlantiradi?", "Etilen", ["Etan", "Metan", "Siklogeksan"], "Qo'shbog'li moddalar brom bilan birikadi, shuning uchun rang yo'qoladi.", E, ("Siklogeksan", "Siklogeksan bromli suv bilan oddiy sharoitda reaksiyaga kirishmaydi: halqa barqaror.")),
  C("Propen va propanni qaysi reaktiv bilan ajratish mumkin?", "Bromli suv", ["Suv", "Natriy xlorid eritmasi", "Kaliy gidroksid eritmasi"], "Faqat propen bromli suvni rangsizlantiradi.", P, ("Suv", "Ikkala gaz ham suv bilan reaksiyaga kirishmaydi.")),
 ]),
 S("b-4", G, "choice", 3, [
  C("5,6 g etilen (M = 28) bilan necha gramm brom (M = 160) birika oladi?", "32 g", ["16 g", "64 g", "8 g"], "5,6 : 28 = 0,2 mol; 1 : 1 nisbatda 0,2 · 160 = 32 g.", E, ("16 g", "16 g 0,1 mol bromga to'g'ri keladi: bu 2,8 g etilen.")),
  C("8,4 g propen (M = 42) to'liq gidrogenlansa, necha gramm propan (M = 44) hosil bo'ladi?", "8,8 g", ["4,4 g", "17,6 g", "6,4 g"], "8,4 : 42 = 0,2 mol; 1 : 1 nisbatda 0,2 · 44 = 8,8 g.", P, ("17,6 g", "17,6 g 0,4 mol propanga mos: bu 16,8 g propen.")),
 ]),
]
G = "Birikish (HX, Markovnikov)"
slots += [
 S("m-1", G, "write", 2, [
  W("Etilenga HBr ta'sir ettiring", ["C2H4", "HBr"], ["C2H5Br"], "C2H4+HBr→C2H5Br", "H va Br qo'shbog'ga birikadi: bromoetan.", E),
  W("Propenga HCl ta'sir ettiring (Markovnikov qoidasi bo'yicha)", ["C3H6", "HCl"], ["C3H7Cl"], "C3H6+HCl→C3H7Cl", "Vodorod ko'proq vodorodli uglerodga birikadi: 2-xlorpropan.", P),
 ]),
 S("m-2", G, "choice", 2, [
  C("Propenga HBr birikkanda asosiy mahsulot qaysi?", "2-brompropan", ["1-brompropan", "1,2-dibrompropan", "Propanol-2"], "Markovnikov qoidasi: vodorod ko'proq vodorodli uglerodga, brom esa kamroq vodorodli uglerodga birikadi.", P, ("1-brompropan", "Bu qoidaga teskari. Vodorod CH₂ ga (ko'proq H), brom CH ga (kamroq H) birikadi.")),
  C("Buten-1 ga HCl birikkanda asosiy mahsulot qaysi?", "2-xlorbutan", ["1-xlorbutan", "1,2-dixlorbutan", "Butanol-2"], "Xlor ikkinchi uglerodga (kamroq vodorodli) birikadi.", B, ("1-xlorbutan", "Bu Markovnikov qoidasiga zid. Xlor kamroq vodorodli uglerodga birikadi.")),
 ]),
 S("m-3", G, "choice", 2, [
  C("Qaysi alkenga HBr birikkanda mahsulotning izomeri hosil bo'lmaydi?", "Etilen", ["Propen", "Buten-1", "Penten-1"], "Etilen simmetrik: ikkala uglerod bir xil, mahsulot faqat bromoetan.", E, ("Propen", "Propen nosimmetrik: ikki xil mahsulot mumkin (Markovnikov bo'yicha 2-brompropan asosiy).")),
  C("Buten-2 ga HBr birikkanda qaysi modda hosil bo'ladi?", "2-brombutan", ["1-brombutan", "2,3-dibrombutan", "Butanol-2"], "Qo'shbog' 2 va 3 uglerodlar orasida, ikkalasi ham bir xil: brom ikkinchi uglerodga birikadi.", B, ("1-brombutan", "Qo'shbog' markazda, brom chetki uglerodga bormaydi.")),
 ]),
]
G = "Hipogalogenid"
slots += [
 S("h-1", G, "write", 2, [
  W("Etilenga xlorli suv (HOCl) ta'sir ettiring", ["C2H4", "HOCl"], ["C2H5ClO"], "C2H4+HOCl→C2H5ClO", "Cl va OH qo'shbog'ga birikadi: 2-xloretanol.", E),
  W("Propenga hipoxlorit kislota (HOCl) ta'sir ettiring", ["C3H6", "HOCl"], ["C3H7ClO"], "C3H6+HOCl→C3H7ClO", "Cl va OH birikadi: 1-xlorpropanol-2.", P),
 ]),
 S("h-2", G, "choice", 3, [
  C("Etilen xlorli suv bilan reaksiyaga kirishsa, qanday modda hosil bo'ladi?", "2-xloretanol", ["1,2-dixloretan", "Etanol", "Xloretan"], "Xlorli suvda HOCl bor: Cl va OH ikkalasi qo'shbog'ga birikadi.", E, ("1,2-dixloretan", "Dixloretan Cl₂ dan hosil bo'ladi. Xlorli suvda HOCl ishtirok etadi va OH ham birikadi.")),
  C("Propenga HOCl birikkanda asosiy mahsulot qaysi?", "1-xlorpropanol-2", ["2-xlorpropanol-1", "1,2-dixlorpropan", "Propanol-2"], "Markovnikov: OH kamroq vodorodli uglerodga (C2), Cl esa C1 ga.", P, ("2-xlorpropanol-1", "Bu teskari joylashuv. Elektrmanfiy OH kamroq vodorodli uglerodga boradi.")),
 ]),
]
G = "O'rin olish"
slots += [
 S("p-1", G, "write", 2, [
  W("Propenga xlor ta'sir ettiring (500 °C, alil holatda o'rin olish)", ["C3H6", "Cl2"], ["C3H5Cl", "HCl"], "C3H6+Cl2→C3H5Cl+HCl", "Yuqori haroratda qo'shbog'ga qo'shni CH₃ dagi vodorod xlorga almashinadi: alilxlorid.", P),
  W("Buten-1 ga xlor ta'sir ettiring (500 °C, alil holatda o'rin olish)", ["C4H8", "Cl2"], ["C4H7Cl", "HCl"], "C4H8+Cl2→C4H7Cl+HCl", "Qo'shbog'ga qo'shni uglerodning vodorodi almashinadi.", B),
 ]),
 S("p-2", G, "choice", 2, [
  C("Propenga xlor 500 °C da ta'sir etsa, qaysi modda hosil bo'ladi?", "3-xlorpropen", ["1,2-dixlorpropan", "2-xlorpropan", "1-xlorpropan"], "Yuqori haroratda birikish emas, alil uglerodda o'rin olish ketadi.", P, ("1,2-dixlorpropan", "Birikish oddiy haroratda ketadi. 500 °C da esa vodorod almashinadi.")),
  C("Qaysi alken 500 °C da xlor bilan o'rin olish reaksiyasiga kirisha oladi?", "Propen", ["Etilen", "Ikkalasi ham", "Hech biri"], "Propenda qo'shbogga qo'shni CH₃ bor, etilenda esa bunday uglerod yo'q.", P, ("Etilen", "Etilenda qo'shbog'ga qo'shni sp³ uglerod yo'q, o'rin olish bormaydi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Etilenning to'liq yonishini yozing", ["C2H4", "O2"], ["CO2", "H2O"], "C2H4+3O2→2CO2+2H2O", "Kislorod: CO₂ da 4, H₂O da 2 ta atom, jami 6 ta: 3 O₂.", E),
  W("Propenning to'liq yonishini yozing", ["C3H6", "O2"], ["CO2", "H2O"], "2C3H6+9O2→6CO2+6H2O", "Kasr chiqmasligi uchun hammasi ikki baravar: 2C₃H₆ + 9O₂.", P),
 ]),
 S("k-2", G, "write", 2, [
  W("Etilenning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner reaksiyasi)", ["C2H4", "KMnO4", "H2O"], ["C2H6O2", "MnO2", "KOH"], "3C2H4+2KMnO4+4H2O→3C2H6O2+2MnO2+2KOH", "Qo'shbog'ga ikki OH birikadi: etilenglikol, Mn⁺⁷ dan Mn⁺⁴ ga.", E),
  W("Propenning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner reaksiyasi)", ["C3H6", "KMnO4", "H2O"], ["C3H8O2", "MnO2", "KOH"], "3C3H6+2KMnO4+4H2O→3C3H8O2+2MnO2+2KOH", "Propilenglikol hosil bo'ladi.", P),
 ]),
 S("k-3", G, "choice", 2, [
  C("Alkenga KMnO₄ eritmasi (qizil-binafsha) ta'sir ettirilsa, nima kuzatiladi?", "Rang yo'qoladi, qo'ng'ir cho'kma hosil bo'ladi", ["Rang o'zgarmaydi", "Ko'k cho'kma tushadi", "Gaz ajraladi, rang saqlanadi"], "Mn⁺⁷ Mn⁺⁴ ga aylanib MnO₂ cho'kmasi hosil bo'ladi.", E, ("Rang o'zgarmaydi", "Bu alkanlarga xos: ular KMnO₄ ni rangsizlantirmaydi.")),
  C("Neytral KMnO₄ bilan alken oksidlanganda qaysi modda sinfi hosil bo'ladi?", "Ikki atomli spirt (glikol)", ["Aldegid", "Karbon kislota", "Alkan"], "Qo'shbog'ga ikkita OH birikadi.", P, ("Karbon kislota", "Kislota qattiq sharoitda (H⁺, qizdirish), qo'shbog' uzilganda hosil bo'ladi.")),
 ]),
 S("k-4", G, "write", 3, [
  W("Propenning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄, qo'shbog' uziladi)", ["C3H6", "KMnO4", "H2SO4"], ["C2H4O2", "CO2", "MnSO4", "K2SO4", "H2O"], "C3H6+2KMnO4+3H2SO4→C2H4O2+CO2+2MnSO4+K2SO4+4H2O", "Qo'shbog' uziladi: CH₂ ⇒ CO₂, CH ⇒ sirka kislota (jami 10 e, ya'ni 2 KMnO₄).", P),
  W("Buten-2 ning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄, ikki molekula sirka kislota hosil bo'ladi)", ["C4H8", "KMnO4", "H2SO4"], ["C2H4O2", "MnSO4", "K2SO4", "H2O"], "5C4H8+8KMnO4+12H2SO4→10C2H4O2+8MnSO4+4K2SO4+12H2O", "Har CH guruhi COOH ga o'tadi (4 e); jami 8 e, shuning uchun 5 : 8.", B),
 ]),
]
G = "Polimerlanish"
slots += [
 S("l-1", G, "choice", 1, [
  C("Etilenning polimerlanishidan qaysi polimer hosil bo'ladi?", "Polietilen", ["Polivinilxlorid", "Polipropilen", "Polistirol"], "(–CH₂–CH₂–)ₙ: qo'shbog'lar ochilib zanjir hosil qiladi.", E),
  C("Propenning polimerlanishidan qaysi polimer hosil bo'ladi?", "Polipropilen", ["Polietilen", "Polivinilxlorid", "Polistirol"], "(–CH₂–CH(CH₃)–)ₙ: monomer propen.", P),
 ]),
 S("l-2", G, "choice", 2, [
  C("Molyar massasi 280 000 g/mol bo'lgan polietilenning polimerlanish darajasi qancha (M(C₂H₄) = 28)?", "10 000", ["5 000", "28 000", "1 000"], "280 000 : 28 = 10 000.", E, ("28 000", "Bo'linmani noto'g'ri nolga qo'shish. 280 000 : 28 = 10 000.")),
  C("Polipropilenning polimerlanish darajasi 5000 bo'lsa, molyar massasi qancha (M(C₃H₆) = 42)?", "210 000", ["21 000", "420 000", "126 000"], "5000 · 42 = 210 000.", P, ("21 000", "Nolni tushirib qoldirish. 5000 · 42 = 210 000.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H6", "C2H4", "C2H4Br2", "C2H2"]}
cB = {"all": ["C3H8", "C3H6", "C3H6Cl2", "C3H4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (Ni, qizdirish)", ["C2H6"], ["C2H4", "H2"], "C2H6→C2H4+H2", "Etandan vodorod ajraladi: etilen.", E, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Ni, qizdirish)", ["C3H8"], ["C3H6", "H2"], "C3H8→C3H6+H2", "Propandan vodorod ajraladi: propen.", P, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing", ["C2H4", "Br2"], ["C2H4Br2"], "C2H4+Br2→C2H4Br2", "Brom qo'shbog'ga birikadi.", E, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing", ["C3H6", "Cl2"], ["C3H6Cl2"], "C3H6+Cl2→C3H6Cl2", "Xlor qo'shbog'ga birikadi.", P, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (KOH ning spirtli eritmasi, ortiqcha)", ["C2H4Br2", "KOH"], ["C2H2", "KBr", "H2O"], "C2H4Br2+2KOH→C2H2+2KBr+2H2O", "Ikki molekula HBr ajraladi: ikkinchi qo'shbog' hosil bo'lib atsetilen chiqadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (KOH ning spirtli eritmasi, ortiqcha)", ["C3H6Cl2", "KOH"], ["C3H4", "KCl", "H2O"], "C3H6Cl2+2KOH→C3H4+2KCl+2H2O", "Ikki molekula HCl ajraladi: propin hosil bo'ladi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(3, "Alkenlar", ["etilen", "propilen", "buten"], slots)
