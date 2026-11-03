from lib import *
A, M, O = ["akril kislota"], ["metakril kislota"], ["olein kislota"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Akroleinning oksidlanishini yozing (kislorod, katalizator)", ["C3H4O", "O2"], ["C3H4O2"], "2C3H4O+O2→2C3H4O2", "Aldegid guruhi COOH ga o'tadi, qo'shbog' saqlanadi.", A),
  W("Metakroleinning oksidlanishini yozing (kislorod, katalizator)", ["C4H6O", "O2"], ["C4H6O2"], "2C4H6O+O2→2C4H6O2", "Metakril kislota hosil bo'ladi.", M),
 ]),
 S("o-2", G, "write", 2, [
  W("Sut kislotaning degidratlanishini yozing (H₂SO₄, qizdirish): akril kislota", ["C3H6O3"], ["C3H4O2", "H2O"], "C3H6O3→C3H4O2+H2O", "OH guruhi va qo'shni vodorod suv holida ajraladi.", A),
  W("2-gidroksiizomoy kislotaning degidratlanishini yozing: metakril kislota", ["C4H8O3"], ["C4H6O2", "H2O"], "C4H8O3→C4H6O2+H2O", "Suv ajralib qo'shbog' hosil bo'ladi.", M),
 ]),
 S("o-3", G, "write", 2, [
  W("Akrilonitrilning to'liq gidrolizini yozing (H⁺, qizdirish)", ["C3H3N", "H2O"], ["C3H4O2", "NH3"], "C3H3N+2H2O→C3H4O2+NH3", "Nitril guruhi COOH ga gidrolizlanadi.", A),
  W("Metakrilonitrilning to'liq gidrolizini yozing (H⁺, qizdirish)", ["C4H5N", "H2O"], ["C4H6O2", "NH3"], "C4H5N+2H2O→C4H6O2+NH3", "Metakril kislota hosil bo'ladi.", M),
 ]),
 S("o-4", G, "write", 2, [
  W("Atsetilen, CO va suv reaksiyasini yozing (Ni(CO)₄, Reppe)", ["C2H2", "CO", "H2O"], ["C3H4O2"], "C2H2+CO+H2O→C3H4O2", "Uchbog'ga H va COOH birikadi: akril kislota.", A),
  W("Propin, CO va suv reaksiyasini yozing (Ni(CO)₄)", ["C3H4", "CO", "H2O"], ["C4H6O2"], "C3H4+CO+H2O→C4H6O2", "Metakril kislota hosil bo'ladi.", M),
 ]),
 S("o-5", G, "choice", 1, [
  C("Akril kislotaning tuzilish formulasi qaysi?", "CH₂=CH–COOH", ["CH₃–CH₂–COOH", "CH₂=CH–CH₂OH", "CH₃–CH=CH₂"], "Qo'shbog' va karboksil guruhi.", A, ("CH₃–CH₂–COOH", "Bu propion kislota: qo'shbog'siz.")),
  C("Olein kislotaning formulasi qaysi?", "C₁₇H₃₃COOH", ["C₁₇H₃₅COOH", "C₁₅H₃₁COOH", "C₁₇H₃₁COOH"], "Stearin kislota C₁₇H₃₅COOH dan ikki vodorod kam: bitta qo'shbog'.", O, ("C₁₇H₃₅COOH", "Bu stearin kislota (to'yingan).")),
 ]),
]
G = "Birikish (H₂, galogenlar)"
slots += [
 S("b-1", G, "write", 1, [
  W("Akril kislotani gidrogenlang (Ni)", ["C3H4O2", "H2"], ["C3H6O2"], "C3H4O2+H2→C3H6O2", "Qo'shbog' to'yinadi: propion kislota.", A),
  W("Metakril kislotani gidrogenlang (Ni)", ["C4H6O2", "H2"], ["C4H8O2"], "C4H6O2+H2→C4H8O2", "Izomoy kislota hosil bo'ladi.", M),
 ]),
 S("b-2", G, "write", 1, [
  W("Akril kislotaga brom ta'sir ettiring", ["C3H4O2", "Br2"], ["C3H4Br2O2"], "C3H4O2+Br2→C3H4Br2O2", "Brom qo'shbog'ga birikadi: 2,3-dibrompropion kislota.", A),
  W("Metakril kislotaga brom ta'sir ettiring", ["C4H6O2", "Br2"], ["C4H6Br2O2"], "C4H6O2+Br2→C4H6Br2O2", "Brom qo'shbog'ga birikadi.", M),
 ]),
 S("b-3", G, "write", 2, [
  W("Olein kislotani gidrogenlang (Ni, qizdirish)", ["C18H34O2", "H2"], ["C18H36O2"], "C18H34O2+H2→C18H36O2", "Stearin kislota hosil bo'ladi.", O),
  W("Olein kislotaga brom ta'sir ettiring", ["C18H34O2", "Br2"], ["C18H34Br2O2"], "C18H34O2+Br2→C18H34Br2O2", "Brom qo'shbog'ga birikadi.", O),
 ]),
 S("b-4", G, "choice", 2, [
  C("Olein kislota bromli suvni rangsizlantiradimi?", "Ha", ["Yo'q", "Faqat qizdirilganda", "Faqat yorug'likda"], "Molekulada qo'shbog' bor: brom birikadi.", O, ("Yo'q", "Stearin kislota rangsizlantirmaydi, olein esa qo'shbog'li.")),
  C("Olein kislotadan stearin kislota olish qanday reaksiya?", "Gidrogenlash", ["Degidratlash", "Oksidlanish", "Eterifikatsiya"], "Vodorod qo'shbog'ga birikadi (suyuq yog'dan qattiq yog' olish asosi).", O, ("Oksidlanish", "Oksidlanishda qo'shbog' uziladi, gidrogenlashda to'yinadi.")),
 ]),
]
G = "HX va boshqa birikishlar"
slots += [
 S("h-1", G, "write", 2, [
  W("Akril kislotaga HBr ta'sir ettiring", ["C3H4O2", "HBr"], ["C3H5BrO2"], "C3H4O2+HBr→C3H5BrO2", "Vodorod va brom qo'shbog'ga birikadi.", A),
  W("Metakril kislotaga HCl ta'sir ettiring", ["C4H6O2", "HCl"], ["C4H7ClO2"], "C4H6O2+HCl→C4H7ClO2", "Vodorod va xlor qo'shbog'ga birikadi.", M),
 ]),
 S("h-2", G, "choice", 3, [
  C("Akril kislotaga HBr birikkanda asosiy mahsulot qaysi?", "3-brompropion kislota", ["2-brompropion kislota", "Propion kislota", "Bromoetan"], "Karboksil elektron tortadi: Markovnikov qoidasiga teskari, brom chetki uglerodga.", A, ("2-brompropion kislota", "Karboksil guruhi yo'nalishni o'zgartiradi: brom uzoqroq uglerodga birikadi.")),
  C("Metakril kislotaga HBr birikkanda asosiy mahsulot qaysi?", "3-brom-2-metilpropion kislota", ["2-brom-2-metilpropion kislota", "Brompropan", "Metakril bromid"], "Karboksilning ta'siri tufayli brom CH₂ uglerodga birikadi.", M, ("2-brom-2-metilpropion kislota", "Bu oddiy Markovnikov natijasi, ammo karboksil uni teskari qiladi.")),
 ]),
 S("h-3", G, "write", 3, [
  W("Akril kislotaga HCN ta'sir ettiring", ["C3H4O2", "HCN"], ["C4H5NO2"], "C3H4O2+HCN→C4H5NO2", "CN guruhi qo'shbog'ning uzoq uglerodiga birikadi.", A),
  W("Akril kislotaga ammiak ta'sir ettiring", ["C3H4O2", "NH3"], ["C3H7NO2"], "C3H4O2+NH3→C3H7NO2", "Ammiak qo'shbog'ga birikadi: β-alanin.", A),
 ]),
]
G = "Karboksil guruhiga xos"
slots += [
 S("c-1", G, "write", 1, [
  W("Akril kislotaga NaOH eritmasi ta'sir ettiring", ["C3H4O2", "NaOH"], ["C3H3NaO2", "H2O"], "C3H4O2+NaOH→C3H3NaO2+H2O", "Natriy akrilat hosil bo'ladi.", A),
  W("Metakril kislotaga KOH eritmasi ta'sir ettiring", ["C4H6O2", "KOH"], ["C4H5KO2", "H2O"], "C4H6O2+KOH→C4H5KO2+H2O", "Kaliy metakrilat hosil bo'ladi.", M),
 ]),
 S("c-2", G, "write", 2, [
  W("Akril kislota va metanol reaksiyasini yozing (H₂SO₄)", ["C3H4O2", "CH3OH"], ["C4H6O2", "H2O"], "C3H4O2+CH3OH→C4H6O2+H2O", "Metil akrilat hosil bo'ladi.", A),
  W("Metakril kislota va metanol reaksiyasini yozing (H₂SO₄)", ["C4H6O2", "CH3OH"], ["C5H8O2", "H2O"], "C4H6O2+CH3OH→C5H8O2+H2O", "Metilmetakrilat (organik shisha monomeri) hosil bo'ladi.", M),
 ]),
 S("c-3", G, "write", 2, [
  W("Akril kislotaga magniy ta'sir ettiring", ["C3H4O2", "Mg"], ["C6H6MgO4", "H2"], "2C3H4O2+Mg→C6H6MgO4+H2", "Magniy akrilat va vodorod hosil bo'ladi.", A),
  W("Olein kislotaga NaOH ta'sir ettiring (sovun hosil bo'ladi)", ["C18H34O2", "NaOH"], ["C18H33NaO2", "H2O"], "C18H34O2+NaOH→C18H33NaO2+H2O", "Natriy oleat: suyuq sovun.", O),
 ]),
 S("c-4", G, "write", 3, [
  W("Akril kislotaga PCl₅ ta'sir ettiring", ["C3H4O2", "PCl5"], ["C3H3ClO", "POCl3", "HCl"], "C3H4O2+PCl5→C3H3ClO+POCl3+HCl", "Akriloilxlorid hosil bo'ladi.", A),
  W("Akril kislotaga tionilxlorid ta'sir ettiring", ["C3H4O2", "SOCl2"], ["C3H3ClO", "SO2", "HCl"], "C3H4O2+SOCl2→C3H3ClO+SO2+HCl", "Gazlar ajralib, akriloilxlorid hosil bo'ladi.", A),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 2, [
  W("Akril kislotaning to'liq yonishini yozing", ["C3H4O2", "O2"], ["CO2", "H2O"], "C3H4O2+3O2→3CO2+2H2O", "Kislorod: 6 + 2 − 2 = 6 atom, ya'ni 3 O₂.", A),
  W("Olein kislotaning to'liq yonishini yozing", ["C18H34O2", "O2"], ["CO2", "H2O"], "2C18H34O2+51O2→36CO2+34H2O", "Kasr chiqmasligi uchun ikki baravar.", O),
 ]),
 S("k-2", G, "write", 3, [
  W("Olein kislotaning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (qo'shbog' uziladi)", ["C18H34O2", "KMnO4", "H2SO4"], ["C9H18O2", "C9H16O4", "MnSO4", "K2SO4", "H2O"], "5C18H34O2+8KMnO4+12H2SO4→5C9H18O2+5C9H16O4+8MnSO4+4K2SO4+12H2O", "Qo'shbog' uzilib pelargon va azelain kislotalar hosil bo'ladi.", O),
  W("Olein kislotaning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner)", ["C18H34O2", "KMnO4", "H2O"], ["C18H36O4", "MnO2", "KOH"], "3C18H34O2+2KMnO4+4H2O→3C18H36O4+2MnO2+2KOH", "Qo'shbog'ga ikki OH birikadi: dioksistearin kislota.", O),
 ]),
 S("k-3", G, "choice", 2, [
  C("Olein kislota neytral KMnO₄ bilan yumshoq oksidlansa, nima hosil bo'ladi?", "Dioksistearin kislota", ["Stearin kislota", "Pelargon kislota", "Natriy oleat"], "Qo'shbog'ga ikkita OH birikadi.", O, ("Stearin kislota", "Stearin kislota gidrogenlashdan hosil bo'ladi.")),
  C("Olein kislotaning qo'shbog'i kuchli oksidlovchi bilan nima bo'ladi?", "Uzilib, ikkita kislota hosil qiladi", ["Hech narsa bo'lmaydi", "Stearin kislotaga aylanadi", "Glitserin hosil bo'ladi"], "C=C uziladi va har uglerod COOH ga o'tadi.", O, ("Stearin kislotaga aylanadi", "Bu qaytarilish: oksidlanishda emas.")),
 ]),
]
G = "Polimerlanish"
slots += [
 S("l-1", G, "choice", 1, [
  C("Metilmetakrilat polimeri qanday nom bilan ataladi?", "Organik shisha (pleksiglas)", ["Kapron", "Polietilen", "Neylon"], "Shaffof, sinmaydigan polimer.", M),
  C("Akril kislotaning polimerlanishidan nima hosil bo'ladi?", "Poliakril kislota", ["Polietilen", "Polistirol", "Polivinilxlorid"], "Qo'shbog' ochilib zanjir hosil qiladi.", A),
 ]),
 S("l-2", G, "choice", 3, [
  C("Molyar massasi 100 000 g/mol bo'lgan polimetilmetakrilatning polimerlanish darajasi qancha (M(C₅H₈O₂) = 100)?", "1000", ["10 000", "100", "500"], "100 000 : 100 = 1000.", M, ("10 000", "Nol xatosi. 100 000 : 100 = 1000.")),
  C("Poliakril kislotaning polimerlanish darajasi 200 bo'lsa, molyar massasi qancha (M(C₃H₄O₂) = 72)?", "14 400", ["1 440", "7 200", "28 800"], "200 · 72 = 14 400.", A, ("7 200", "Bu 100 · 72. Daraja 200.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C3H6O", "C3H4O", "C3H4O2", "C5H8O2"]}
cB = {"all": ["C18H36O2", "C18H34O2", "C18H33KO2", "C36H66CaO4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (CuO, qizdirish)", ["C3H6O", "CuO"], ["C3H4O", "Cu", "H2O"], "C3H6O+CuO→C3H4O+Cu+H2O", "Allil spirt akroleinga oksidlanadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (degidrogenlash)", ["C18H36O2"], ["C18H34O2", "H2"], "C18H36O2→C18H34O2+H2", "Stearin kislotadan vodorod ajralib olein kislota hosil bo'ladi.", O, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (kumush oksidning ammiakli eritmasi)", ["C3H4O", "Ag2O"], ["C3H4O2", "Ag"], "C3H4O+Ag2O→C3H4O2+2Ag", "Aldegid kislotaga oksidlanadi.", A, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing", ["C18H34O2", "KOH"], ["C18H33KO2", "H2O"], "C18H34O2+KOH→C18H33KO2+H2O", "Kaliy oleat hosil bo'ladi.", O, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (etanol, H₂SO₄)", ["C3H4O2", "C2H5OH"], ["C5H8O2", "H2O"], "C3H4O2+C2H5OH→C5H8O2+H2O", "Etil akrilat hosil bo'ladi.", A, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (almashinish)", ["C18H33KO2", "CaCl2"], ["C36H66CaO4", "KCl"], "2C18H33KO2+CaCl2→C36H66CaO4+2KCl", "Kalsiy oleat cho'kmaga tushadi.", O, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(15, "To'yinmagan bir asosli kislotalar", ["akril kislota", "metakril kislota", "olein kislota"], slots)
