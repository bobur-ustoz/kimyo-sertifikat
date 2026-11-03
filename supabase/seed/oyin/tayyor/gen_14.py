from lib import *
S_, C_, P_ = ["sirka kislota"], ["chumoli kislota"], ["propion kislota"]
slots = []
G = "Umumiy olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Sirka aldegidning kislorod bilan oksidlanishini yozing (katalizator)", ["C2H4O", "O2"], ["C2H4O2"], "2C2H4O+O2→2C2H4O2", "Aldegid kislotaga oksidlanadi.", S_),
  W("Propanalning kislorod bilan oksidlanishini yozing (katalizator)", ["C3H6O", "O2"], ["C3H6O2"], "2C3H6O+O2→2C3H6O2", "Propion kislota hosil bo'ladi.", P_),
 ]),
 S("o-2", G, "write", 2, [
  W("Asetonitrilning to'liq gidrolizini yozing (H⁺, qizdirish)", ["C2H3N", "H2O"], ["C2H4O2", "NH3"], "C2H3N+2H2O→C2H4O2+NH3", "Nitril kislotaga gidrolizlanadi, ammiak ajraladi.", S_),
  W("Butironitrilning to'liq gidrolizini yozing (H⁺, qizdirish)", ["C4H7N", "H2O"], ["C4H8O2", "NH3"], "C4H7N+2H2O→C4H8O2+NH3", "Moy kislota hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Metilmagniy bromidga CO₂ ta'sir ettiring", ["CH3MgBr", "CO2"], ["C2H3BrMgO2"], "CH3MgBr+CO2→C2H3BrMgO2", "Karboksilat hosil bo'ladi: uglerod zanjiri bir atomga uzayadi.", S_),
  W("Hosil bo'lgan magniyli tuzni suv bilan gidrolizlang", ["C2H3BrMgO2", "H2O"], ["C2H4O2", "Mg(OH)Br"], "C2H3BrMgO2+H2O→C2H4O2+Mg(OH)Br", "Gidrolizdan sirka kislota hosil bo'ladi.", S_),
 ]),
 S("o-4", G, "write", 3, [
  W("Etanolni kaliy dixromat bilan kislotagacha oksidlang (H₂SO₄, ortiqcha oksidlovchi)", ["C2H5OH", "K2Cr2O7", "H2SO4"], ["C2H4O2", "Cr2(SO4)3", "K2SO4", "H2O"], "3C2H5OH+2K2Cr2O7+8H2SO4→3C2H4O2+2Cr2(SO4)3+2K2SO4+11H2O", "Spirt to'liq oksidlanadi (4 e): 3 : 2.", S_),
  W("Propanol-1 ni kaliy dixromat bilan kislotagacha oksidlang (H₂SO₄)", ["C3H8O", "K2Cr2O7", "H2SO4"], ["C3H6O2", "Cr2(SO4)3", "K2SO4", "H2O"], "3C3H8O+2K2Cr2O7+8H2SO4→3C3H6O2+2Cr2(SO4)3+2K2SO4+11H2O", "Birlamchi spirt kislotaga oksidlanadi.", P_),
 ]),
 S("o-5", G, "choice", 1, [
  C("Aldegid oksidlanganda qaysi modda hosil bo'ladi?", "Karbon kislota", ["Spirt", "Keton", "Efir"], "CHO guruhi COOH ga o'tadi.", S_, ("Spirt", "Spirt aldegidni qaytarganda hosil bo'ladi.")),
  C("Sirka kislotani sanoatda qaysi moddalardan olish mumkin?", "Metanol va CO", ["Etanol va O₂ (sanoat usuli emas)", "Atsetilen va suv", "Metan va Cl₂"], "CH₃OH + CO → CH₃COOH (katalizator, bosim).", S_, ("Atsetilen va suv", "Atsetilen va suv sirka aldegid beradi, kislota uchun yana oksidlash kerak.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Metanol va uglerod(II) oksid reaksiyasini yozing (katalizator, bosim)", ["CH4O", "CO"], ["C2H4O2"], "CH4O+CO→C2H4O2", "Sirka kislotaning sanoat sintezi.", S_),
  W("Natriy gidroksid va uglerod(II) oksid reaksiyasini yozing (qizdirish, bosim): chumoli kislota tuzi", ["NaOH", "CO"], ["CHNaO2"], "NaOH+CO→CHNaO2", "Natriy formiat hosil bo'ladi.", C_),
 ]),
 S("x-2", G, "write", 2, [
  W("Natriy formiatga sulfat kislota ta'sir ettiring", ["CHNaO2", "H2SO4"], ["CH2O2", "Na2SO4"], "2CHNaO2+H2SO4→2CH2O2+Na2SO4", "Kuchli kislota zaif kislotani tuzidan siqib chiqaradi.", C_),
  W("Natriy atsetatga sulfat kislota ta'sir ettiring", ["C2H3NaO2", "H2SO4"], ["C2H4O2", "Na2SO4"], "2C2H3NaO2+H2SO4→2C2H4O2+Na2SO4", "Sirka kislota hosil bo'ladi.", S_),
 ]),
 S("x-3", G, "choice", 1, [
  C("Oziq-ovqat sirkasining asosiy tarkibiy qismi qaysi kislota?", "Sirka kislota", ["Chumoli kislota", "Limon kislota", "Sulfat kislota"], "3–9% li sirka kislota eritmasi.", S_, ("Chumoli kislota", "Chumoli kislota ham bor, lekin sirka sirka kislotadan iborat.")),
  C("Chumoli kislota qayerda uchraydi?", "Chumolilar va qichitqi o'tda", ["Sut mahsulotlarida", "Mevalarda", "Tuxumda"], "Nomi chumolidan olingan.", C_),
 ]),
]
G = "Karboksil guruhiga xos"
slots += [
 S("c-1", G, "write", 1, [
  W("Sirka kislotaga magniy ta'sir ettiring", ["C2H4O2", "Mg"], ["C4H6MgO4", "H2"], "2C2H4O2+Mg→C4H6MgO4+H2", "Magniy atsetat va vodorod hosil bo'ladi.", S_),
  W("Chumoli kislotaga rux ta'sir ettiring", ["CH2O2", "Zn"], ["C2H2O4Zn", "H2"], "2CH2O2+Zn→C2H2O4Zn+H2", "Rux formiat va vodorod hosil bo'ladi.", C_),
 ]),
 S("c-2", G, "write", 1, [
  W("Sirka kislotaga NaOH eritmasi ta'sir ettiring", ["C2H4O2", "NaOH"], ["C2H3NaO2", "H2O"], "C2H4O2+NaOH→C2H3NaO2+H2O", "Neytrallanish: natriy atsetat.", S_),
  W("Chumoli kislotaga KOH eritmasi ta'sir ettiring", ["CH2O2", "KOH"], ["CHKO2", "H2O"], "CH2O2+KOH→CHKO2+H2O", "Kaliy formiat hosil bo'ladi.", C_),
 ]),
 S("c-3", G, "write", 2, [
  W("Sirka kislotaga mis(II) oksid ta'sir ettiring", ["C2H4O2", "CuO"], ["C4H6CuO4", "H2O"], "2C2H4O2+CuO→C4H6CuO4+H2O", "Mis atsetat hosil bo'ladi.", S_),
  W("Sirka kislotaga soda (Na₂CO₃) ta'sir ettiring", ["C2H4O2", "Na2CO3"], ["C2H3NaO2", "CO2", "H2O"], "2C2H4O2+Na2CO3→2C2H3NaO2+CO2+H2O", "Karbonat kislotani siqib chiqaradi: CO₂ ajraladi.", S_),
 ]),
 S("c-4", G, "write", 2, [
  W("Sirka kislota va etanol reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["C2H4O2", "C2H5OH"], ["C4H8O2", "H2O"], "C2H4O2+C2H5OH→C4H8O2+H2O", "Etil atsetat hosil bo'ladi.", S_),
  W("Chumoli kislota va metanol reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["CH2O2", "CH3OH"], ["C2H4O2", "H2O"], "CH2O2+CH3OH→C2H4O2+H2O", "Metil formiat hosil bo'ladi.", C_),
 ]),
 S("c-5", G, "write", 3, [
  W("Sirka kislotaga fosfor(V) xlorid ta'sir ettiring", ["C2H4O2", "PCl5"], ["C2H3ClO", "POCl3", "HCl"], "C2H4O2+PCl5→C2H3ClO+POCl3+HCl", "OH xlorga almashinadi: atsetilxlorid.", S_),
  W("Sirka kislotaga tionilxlorid ta'sir ettiring", ["C2H4O2", "SOCl2"], ["C2H3ClO", "SO2", "HCl"], "C2H4O2+SOCl2→C2H3ClO+SO2+HCl", "Gazlar ajraladi, atsetilxlorid hosil bo'ladi.", S_),
 ]),
 S("c-6", G, "choice", 2, [
  C("Sirka kislota NaHCO₃ bilan reaksiyaga kirishsa, nima kuzatiladi?", "CO₂ gazi ajraladi", ["H₂ gazi ajraladi", "Cho'kma tushadi", "Reaksiya bormaydi"], "Kislota karbonat kislotani siqib chiqaradi.", S_, ("H₂ gazi ajraladi", "Vodorod faol metallar bilan ajraladi, karbonatlar bilan CO₂.")),
  C("Qaysi qatorda kislotalilik kamayib boradi?", "HCOOH > CH₃COOH > C₂H₅OH", ["CH₃COOH > HCOOH > C₂H₅OH", "C₂H₅OH > HCOOH > CH₃COOH", "CH₃COOH > C₂H₅OH > HCOOH"], "Chumoli kislota sirka kislotadan kuchli, spirt esa eng kuchsiz.", C_, ("CH₃COOH > HCOOH > C₂H₅OH", "Metil guruh elektron beradi: sirka kislota chumolidan kuchsiz.")),
 ]),
]
G = "Radikalga xos"
slots += [
 S("a-1", G, "write", 2, [
  W("Sirka kislotaga xlor ta'sir ettiring (qizil fosfor, α-holat)", ["C2H4O2", "Cl2"], ["C2H3ClO2", "HCl"], "C2H4O2+Cl2→C2H3ClO2+HCl", "Karboksilga qo'shni uglerodning vodorodi xlorga almashinadi.", S_),
  W("Propion kislotaga xlor ta'sir ettiring (qizil fosfor, α-holat)", ["C3H6O2", "Cl2"], ["C3H5ClO2", "HCl"], "C3H6O2+Cl2→C3H5ClO2+HCl", "2-xlorpropion kislota hosil bo'ladi.", P_),
 ]),
 S("a-2", G, "write", 3, [
  W("Sirka kislotaga ortiqcha xlor ta'sir ettiring (uchala vodorod almashinadi)", ["C2H4O2", "Cl2"], ["C2HCl3O2", "HCl"], "C2H4O2+3Cl2→C2HCl3O2+3HCl", "Trixlorsirka kislota hosil bo'ladi.", S_),
  W("Sirka kislotaga 2 mol xlor ta'sir ettiring", ["C2H4O2", "Cl2"], ["C2H2Cl2O2", "HCl"], "C2H4O2+2Cl2→C2H2Cl2O2+2HCl", "Dixlorsirka kislota hosil bo'ladi.", S_),
 ]),
 S("a-3", G, "choice", 2, [
  C("Xlorsirka kislota sirka kislotaga nisbatan qanday?", "Kuchliroq kislota", ["Kuchsizroq", "Bir xil kuchda", "Kislota emas"], "Elektronmanfiy xlor karboksilni yanada kislotali qiladi.", S_, ("Kuchsizroq", "Xlor elektron tortadi va kislotalilikni oshiradi.")),
  C("Qaysi kislota eng kuchli?", "Trixlorsirka kislota", ["Sirka kislota", "Monoxlorsirka kislota", "Propion kislota"], "Uchta xlor atomi eng kuchli ta'sir ko'rsatadi.", S_, ("Monoxlorsirka kislota", "Uchta xlor bittadan ko'ra kuchliroq.")),
 ]),
]
G = "Xususiy reaksiyalar"
slots += [
 S("r-1", G, "write", 2, [
  W("Chumoli kislotaga kumush oksidning ammiakli eritmasi ta'sir ettiring", ["CH2O2", "Ag2O"], ["CO2", "H2O", "Ag"], "CH2O2+Ag2O→CO2+H2O+2Ag", "Chumoli kislotada aldegid guruhi bor: kumush ko'zgu.", C_),
  W("Chumoli kislotaga mis(II) gidroksid ta'sir ettiring (qizdirish)", ["CH2O2", "Cu(OH)2"], ["CO2", "Cu2O", "H2O"], "CH2O2+2Cu(OH)2→CO2+Cu2O+3H2O", "Qizil cho'kma (Cu₂O) hosil bo'ladi.", C_),
 ]),
 S("r-2", G, "write", 2, [
  W("Chumoli kislotaning konsentrlangan H₂SO₄ bilan degidratlanishini yozing", ["CH2O2"], ["CO", "H2O"], "CH2O2→CO+H2O", "Laboratoriyada CO olish usuli.", C_),
  W("Sirka kislotaning degidratlanishini yozing (P₂O₅): angidrid hosil bo'ladi", ["C2H4O2"], ["C4H6O3", "H2O"], "2C2H4O2→C4H6O3+H2O", "Ikki molekuladan bitta suv ajraladi.", S_),
 ]),
 S("r-3", G, "write", 3, [
  W("Natriy atsetatni NaOH bilan qizdiring (quruq): metan hosil bo'ladi", ["C2H3NaO2", "NaOH"], ["CH4", "Na2CO3"], "C2H3NaO2+NaOH→CH4+Na2CO3", "Dekarboksillanish: bitta uglerod kam alkan.", S_),
  W("Natriy atsetat eritmasini elektroliz qiling (Kolbe): etan hosil bo'ladi", ["C2H3NaO2", "H2O"], ["C2H6", "CO2", "H2", "NaOH"], "2C2H3NaO2+2H2O→C2H6+2CO2+H2+2NaOH", "Anodda radikallar birlashadi.", S_),
 ]),
 S("r-4", G, "choice", 3, [
  C("Faqat chumoli kislotaga xos bo'lgan reaksiya qaysi?", "Kumush ko'zgu reaksiyasi", ["Natriy bilan reaksiya", "Eterifikatsiya", "NaOH bilan neytrallanish"], "Chumoli kislotada aldegid guruhi ham bor.", C_, ("Eterifikatsiya", "Eterifikatsiya barcha karbon kislotalarga xos.")),
  C("Chumoli kislota to'liq oksidlansa, qaysi moddalar hosil bo'ladi?", "CO₂ va H₂O", ["CO va H₂", "CH₃OH", "CH₃COOH"], "Oxirgi mahsulot: uglerod(IV) oksid va suv.", C_, ("CO va H₂", "To'liq oksidlanishda CO₂ hosil bo'ladi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H6O", "C2H4O", "C2H4O2", "C2H7NO2"]}
cB = {"all": ["C2H5Br", "C3H5N", "C3H6O2", "C3H5BrO2"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (CuO, qizdirish)", ["C2H5OH", "CuO"], ["C2H4O", "Cu", "H2O"], "C2H5OH+CuO→C2H4O+Cu+H2O", "Etanol sirka aldegidga oksidlanadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (spirtli eritma)", ["C2H5Br", "KCN"], ["C3H5N", "KBr"], "C2H5Br+KCN→C3H5N+KBr", "Brom CN ga almashinadi: uglerod zanjiri uzayadi.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (mis(II) gidroksid, qizdirish)", ["C2H4O", "Cu(OH)2"], ["C2H4O2", "Cu2O", "H2O"], "C2H4O+2Cu(OH)2→C2H4O2+Cu2O+2H2O", "Aldegid kislotaga oksidlanadi.", S_, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (H⁺, qizdirish)", ["C3H5N", "H2O"], ["C3H6O2", "NH3"], "C3H5N+2H2O→C3H6O2+NH3", "Nitril kislotaga gidrolizlanadi.", P_, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing", ["C2H4O2", "NH3"], ["C2H7NO2"], "C2H4O2+NH3→C2H7NO2", "Ammiak bilan ammoniy atsetat tuzi hosil bo'ladi.", S_, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (qizil fosfor, α-holat)", ["C3H6O2", "Br2"], ["C3H5BrO2", "HBr"], "C3H6O2+Br2→C3H5BrO2+HBr", "2-brompropion kislota hosil bo'ladi.", P_, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(14, "Karbon kislotalar", ["sirka kislota", "chumoli kislota", "propion kislota"], slots)
