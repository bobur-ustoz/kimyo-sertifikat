from lib import *
A, P, B = ["atsetilen"], ["propin"], ["butin"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Metanning yuqori haroratda (1500 °C) parchalanib atsetilen hosil qilishini yozing", ["CH4"], ["C2H2", "H2"], "2CH4→C2H2+3H2", "Ikki metan molekulasidan atsetilen va uch molekula vodorod hosil bo'ladi.", A),
  W("1,2-dibrompropanga KOH ning spirtli eritmasini (ortiqcha) ta'sir ettiring", ["C3H6Br2", "KOH"], ["C3H4", "KBr", "H2O"], "C3H6Br2+2KOH→C3H4+2KBr+2H2O", "Ikki molekula HBr ajraladi va uchbog' hosil bo'ladi: propin.", P),
 ]),
 S("o-2", G, "write", 2, [
  W("1,2-dibrombutanga KOH ning spirtli eritmasini (ortiqcha) ta'sir ettiring", ["C4H8Br2", "KOH"], ["C4H6", "KBr", "H2O"], "C4H8Br2+2KOH→C4H6+2KBr+2H2O", "Ikki HBr ajraladi: butin hosil bo'ladi.", B),
  W("1,2-dixloretanga KOH ning spirtli eritmasini (ortiqcha) ta'sir ettiring", ["C2H4Cl2", "KOH"], ["C2H2", "KCl", "H2O"], "C2H4Cl2+2KOH→C2H2+2KCl+2H2O", "Ikki HCl ajraladi va atsetilen hosil bo'ladi.", A),
 ]),
 S("o-3", G, "choice", 1, [
  C("Laboratoriyada atsetilen qanday olinadi?", "Kalsiy karbidga suv ta'sir ettirib", ["Etanolni degidratlab", "Metanni xlorlab", "Etilenni gidrogenlab"], "CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂: qulay usul.", A, ("Etanolni degidratlab", "Etanoldan suv ajralsa etilen hosil bo'ladi, atsetilen emas.")),
  C("Sanoatda atsetilen metandan qaysi haroratda olinadi?", "1500 °C", ["170 °C", "500 °C", "80 °C"], "Metan juda yuqori haroratda (1500 °C) atsetilenga aylanadi.", A, ("170 °C", "170 °C etanolni degidratlab etilen olish harorati.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 1, [
  W("Kalsiy oksidning koks bilan reaksiyasini yozing (elektr pechida, kalsiy karbid olinadi)", ["CaO", "C"], ["CaC2", "CO"], "CaO+3C→CaC2+CO", "Uglerod kalsiy karbidga va uglerod(II) oksidga o'tadi.", A),
  W("Kalsiyning koks bilan reaksiyasini yozing (kalsiy karbid olinadi)", ["Ca", "C"], ["CaC2"], "Ca+2C→CaC2", "Karbid: Ca²⁺ va C₂²⁻ ionlaridan tuzilgan.", A),
 ]),
 S("x-2", G, "write", 1, [
  W("Kalsiy karbidga suv ta'sir ettiring", ["CaC2", "H2O"], ["C2H2", "Ca(OH)2"], "CaC2+2H2O→C2H2+Ca(OH)2", "Karbid gidrolizlanib atsetilen va ohak hosil qiladi.", A),
  W("Kalsiy karbidga xlorid kislota ta'sir ettiring", ["CaC2", "HCl"], ["C2H2", "CaCl2"], "CaC2+2HCl→C2H2+CaCl2", "Kislota ham karbidni parchalab atsetilen beradi.", A),
 ]),
]
G = "Birikish"
slots += [
 S("b-1", G, "write", 1, [
  W("Atsetilenning to'liq gidrogenlanishini yozing (Ni, qizdirish)", ["C2H2", "H2"], ["C2H6"], "C2H2+2H2→C2H6", "Uchbog' to'liq to'yinadi: ikki molekula vodorod birikadi.", A),
  W("Propinning to'liq gidrogenlanishini yozing (Ni, qizdirish)", ["C3H4", "H2"], ["C3H8"], "C3H4+2H2→C3H8", "Uchbog'ga ikki molekula vodorod birikib propan hosil bo'ladi.", P),
 ]),
 S("b-2", G, "write", 2, [
  W("Atsetilenga ortiqcha brom ta'sir ettiring", ["C2H2", "Br2"], ["C2H2Br4"], "C2H2+2Br2→C2H2Br4", "Ikki bosqichda 2 molekula brom birikadi: 1,1,2,2-tetrabrometan.", A),
  W("Propinga ortiqcha xlor ta'sir ettiring", ["C3H4", "Cl2"], ["C3H4Cl4"], "C3H4+2Cl2→C3H4Cl4", "Uchbog'ga ikki molekula xlor birikadi.", P),
 ]),
 S("b-3", G, "write", 1, [
  W("Atsetilenga 1 mol HCl ta'sir ettiring (HgCl₂ katalizatori)", ["C2H2", "HCl"], ["C2H3Cl"], "C2H2+HCl→C2H3Cl", "Vinilxlorid hosil bo'ladi.", A),
  W("Propinga 1 mol HBr ta'sir ettiring", ["C3H4", "HBr"], ["C3H5Br"], "C3H4+HBr→C3H5Br", "Markovnikov qoidasi bilan 2-brompropen hosil bo'ladi.", P),
 ]),
 S("b-4", G, "choice", 2, [
  C("Propinga 2 mol HBr birikkanda qaysi modda hosil bo'ladi?", "2,2-dibrompropan", ["1,2-dibrompropan", "1,1-dibrompropan", "2-brompropen"], "Markovnikov: ikkala brom ham kamroq vodorodli uglerodga birikadi.", P, ("1,2-dibrompropan", "Ikkinchi brom ham birinchisi bilan bitta uglerodga birikadi.")),
  C("Atsetilenga HCN birikishidan hosil bo'lgan modda qaysi?", "Akrilonitril CH₂=CH–CN", ["CH₃–CH₂–CN", "CH₂=CH–Cl", "CH₂=CH–COOH"], "HCN uchbog'ga birikib nitril guruhli alken hosil qiladi.", A, ("CH₂=CH–Cl", "Vinilxlorid HCl dan hosil bo'ladi, HCN dan emas.")),
 ]),
]
G = "Gidratlash (Kucherov)"
slots += [
 S("g-1", G, "write", 1, [
  W("Atsetilenning gidratlanishini yozing (Kucherov reaksiyasi, HgSO₄, H₂SO₄)", ["C2H2", "H2O"], ["C2H4O"], "C2H2+H2O→C2H4O", "Vinil spirt beqaror, u sirka aldegidga o'tadi.", A),
  W("Propinning gidratlanishini yozing (Kucherov reaksiyasi)", ["C3H4", "H2O"], ["C3H6O"], "C3H4+H2O→C3H6O", "Markovnikov: OH ikkinchi uglerodda, mahsulot aseton.", P),
 ]),
 S("g-2", G, "choice", 2, [
  C("Atsetilenning gidratlanish mahsuloti (Kucherov) qaysi?", "Sirka aldegid", ["Etanol", "Aseton", "Sirka kislota"], "Hosil bo'lgan vinil spirt aldegidga o'tadi.", A, ("Etanol", "Etanol alkenning gidratlanishidan hosil bo'ladi. Uchbog'da enol, keyin aldegid.")),
  C("Propin gidratlansa, qanday modda hosil bo'ladi?", "Aseton", ["Propanal", "Propanol-2", "Propan kislota"], "Markovnikov: OH kamroq vodorodli uglerodga birikib, keton hosil qiladi.", P, ("Propanal", "Propanal aldegid: faqat atsetilendan aldegid hosil bo'ladi.")),
 ]),
 S("g-3", G, "choice", 3, [
  C("Qaysi alkin gidratlanganda aldegid hosil bo'ladi?", "Atsetilen", ["Propin", "Butin-1", "Butin-2"], "Faqat atsetilenda uchbog' chetki: boshqa alkinlardan keton hosil bo'ladi.", A, ("Propin", "Propindan aseton, ya'ni keton hosil bo'ladi.")),
  C("Butin-1 gidratlansa, qaysi modda hosil bo'ladi?", "Butanon", ["Butanal", "Butanol-2", "Butan kislota"], "Markovnikov: OH ikkinchi uglerodga, keton hosil bo'ladi.", B, ("Butanal", "Aldegid faqat atsetilendan chiqadi, boshqa alkinlardan keton.")),
 ]),
]
G = "O'rin olish"
slots += [
 S("a-1", G, "write", 2, [
  W("Atsetilenga natriy ta'sir ettiring (bir vodorod almashinadi)", ["C2H2", "Na"], ["C2HNa", "H2"], "2C2H2+2Na→2C2HNa+H2", "Uchbog' uglerodidagi vodorod harakatchan: u natriyga almashinadi.", A),
  W("Propinga natriy ta'sir ettiring", ["C3H4", "Na"], ["C3H3Na", "H2"], "2C3H4+2Na→2C3H3Na+H2", "Faqat uchbog'dagi vodorod almashinadi.", P),
 ]),
 S("a-2", G, "write", 2, [
  W("Atsetilenga kumush oksid ta'sir ettiring (atsetilenid cho'kmasi)", ["C2H2", "Ag2O"], ["C2Ag2", "H2O"], "C2H2+Ag2O→C2Ag2+H2O", "Ikkala vodorod ham kumushga almashinadi: oq cho'kma.", A),
  W("Butin-1 ga kumush oksid ta'sir ettiring", ["C4H6", "Ag2O"], ["C4H5Ag", "H2O"], "2C4H6+Ag2O→2C4H5Ag+H2O", "Chetki uchbog'dagi bitta vodorod almashinadi.", B),
 ]),
]
G = "Izomerlanish"
slots += [
 S("i-1", G, "choice", 1, [
  C("C₄H₆ tarkibli nechta alkin izomeri bor?", "2", ["1", "3", "4"], "Butin-1 va butin-2.", B, ("3", "Uchinchisi yo'q: uchbog'ni boshqa joyga qo'yib bo'lmaydi.")),
  C("C₅H₈ tarkibli nechta alkin izomeri bor?", "3", ["2", "4", "5"], "Pentin-1, pentin-2 va 3-metilbutin-1.", None, ("2", "Tarmoqlangan izomer ham bor: 3-metilbutin-1.")),
 ]),
 S("i-2", G, "choice", 3, [
  C("Quyidagilardan qaysi biri butin-1 ning izomeri?", "Butin-2", ["Buten-1", "Butan", "Siklobutan"], "Ikkalasi C₄H₆: faqat uchbog' o'rni farq qiladi.", B, ("Buten-1", "Buten-1 ning formulasi C₄H₈: boshqa modda.")),
  C("C₄H₆ tarkibli alkinning sinfdosh bo'lmagan izomeri qaysi?", "Butadien-1,3", ["Buten-1", "Siklobutan", "Butan"], "Alkinlar va alkadienlar bir xil C<sub>n</sub>H<sub>2n−2</sub> formulaga ega.", B, ("Buten-1", "Buten C₄H₈: izomer emas.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Atsetilenning to'liq yonishini yozing", ["C2H2", "O2"], ["CO2", "H2O"], "2C2H2+5O2→4CO2+2H2O", "Kasrdan qutulish uchun hammasi ikki baravar: 2C₂H₂ + 5O₂.", A),
  W("Propinning to'liq yonishini yozing", ["C3H4", "O2"], ["CO2", "H2O"], "C3H4+4O2→3CO2+2H2O", "Kislorod: 6 + 2 = 8 ta atom, ya'ni 4 O₂.", P),
 ]),
 S("k-2", G, "choice", 2, [
  C("Atsetilen–kislorod alangasi qayerda ishlatiladi?", "Metallarni payvandlash va kesishda", ["Oziq-ovqat saqlashda", "Suvni tozalashda", "Polimer sintezida"], "Alanga harorati ~3000 °C ga yetadi.", A),
  C("Atsetilen havoda yonganda alanga nega qurumli?", "Uglerod ulushi yuqori, kislorod yetishmaydi", ["Vodorod juda ko'p", "Azot yonadi", "Suv hosil bo'ladi"], "Ko'p uglerod to'liq yonishga ulgurmaydi va qurum bo'ladi.", A),
 ]),
 S("k-3", G, "write", 3, [
  W("Atsetilenning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄)", ["C2H2", "KMnO4", "H2SO4"], ["CO2", "MnSO4", "K2SO4", "H2O"], "C2H2+2KMnO4+3H2SO4→2CO2+2MnSO4+K2SO4+4H2O", "Har uglerod 5 e beradi: C₂H₂ uchun 10 e, ya'ni 2 KMnO₄.", A),
  W("Butin-2 ning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄)", ["C4H6", "KMnO4", "H2SO4"], ["C2H4O2", "MnSO4", "K2SO4", "H2O"], "5C4H6+6KMnO4+9H2SO4→10C2H4O2+6MnSO4+3K2SO4+4H2O", "Uchbog' uzilib ikki molekula sirka kislota hosil bo'ladi.", B),
 ]),
]
G = "Polimerlanish"
slots += [
 S("l-1", G, "write", 1, [
  W("Atsetilendan benzol hosil bo'lishini yozing (Zelinskiy, 450 °C, aktivlangan ko'mir)", ["C2H2"], ["C6H6"], "3C2H2→C6H6", "Uch molekula atsetilen halqaga birlashadi.", A),
  W("Atsetilenning dimerlanishini yozing (CuCl, NH₄Cl)", ["C2H2"], ["C4H4"], "2C2H2→C4H4", "Vinilatsetilen hosil bo'ladi.", A),
 ]),
 S("l-2", G, "choice", 3, [
  C("78 g benzol hosil bo'lishi uchun necha gramm atsetilen kerak (M(C₆H₆) = 78)?", "78 g", ["26 g", "39 g", "234 g"], "3C₂H₂ → C₆H₆: massa saqlanadi, 3 · 26 = 78 g.", A, ("26 g", "26 g bir mol atsetilen, lekin benzol uchun uch mol kerak.")),
  C("44,8 l (n.sh.) atsetilendan necha gramm benzol hosil bo'ladi (M(C₆H₆) = 78)?", "52 g", ["78 g", "26 g", "156 g"], "44,8 : 22,4 = 2 mol; benzol 2 : 3 mol, 2/3 · 78 = 52 g.", A, ("78 g", "78 g uch mol atsetilenga, ya'ni 67,2 l ga to'g'ri keladi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H2", "C2H4", "C2H4Br2", "C2H2"]}
cB = {"all": ["C3H4", "C3H6", "C3H6Cl2", "C3H4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (Pd, qisman gidrogenlash)", ["C2H2", "H2"], ["C2H4"], "C2H2+H2→C2H4", "Uchbog' qo'shbog'gacha gidrogenlanadi.", A, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Pd, qisman gidrogenlash)", ["C3H4", "H2"], ["C3H6"], "C3H4+H2→C3H6", "Propin propenga aylanadi.", P, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing", ["C2H4", "Br2"], ["C2H4Br2"], "C2H4+Br2→C2H4Br2", "Brom qo'shbog'ga birikadi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing", ["C3H6", "Cl2"], ["C3H6Cl2"], "C3H6+Cl2→C3H6Cl2", "Xlor qo'shbog'ga birikadi.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (KOH ning spirtli eritmasi, ortiqcha)", ["C2H4Br2", "KOH"], ["C2H2", "KBr", "H2O"], "C2H4Br2+2KOH→C2H2+2KBr+2H2O", "Ikki HBr ajralib uchbog' qayta hosil bo'ladi.", A, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (KOH ning spirtli eritmasi, ortiqcha)", ["C3H6Cl2", "KOH"], ["C3H4", "KCl", "H2O"], "C3H6Cl2+2KOH→C3H4+2KCl+2H2O", "Ikki HCl ajraladi: propin.", P, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(4, "Alkinlar", ["atsetilen", "propin", "butin"], slots)
