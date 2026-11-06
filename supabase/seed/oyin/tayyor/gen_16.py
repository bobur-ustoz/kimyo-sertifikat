from lib import *
Ox, Ma, Qa, Ad = ["oksalat kislota"], ["malon kislota"], ["qahrabo kislota"], ["adipin kislota"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 2, [
  W("Disianning (C₂N₂) to'liq gidrolizini yozing", ["C2N2", "H2O"], ["C2H2O4", "NH3"], "C2N2+4H2O→C2H2O4+2NH3", "Ikkala nitril guruhi COOH ga gidrolizlanadi: oksalat kislota.", Ox),
  W("Malononitrilning to'liq gidrolizini yozing", ["C3H2N2", "H2O"], ["C3H4O4", "NH3"], "C3H2N2+4H2O→C3H4O4+2NH3", "Ikkala nitril guruhi COOH ga o'tadi: malon kislota.", Ma),
 ]),
 S("o-2", G, "write", 3, [
  W("Dimetil oksalatning to'liq gidrolizini yozing", ["C4H6O4", "H2O"], ["C2H2O4", "CH3OH"], "C4H6O4+2H2O→C2H2O4+2CH3OH", "Murakkab efir kislota va spirtga gidrolizlanadi.", Ox),
  W("Dietil malonatning to'liq gidrolizini yozing", ["C7H12O4", "H2O"], ["C3H4O4", "C2H5OH"], "C7H12O4+2H2O→C3H4O4+2C2H5OH", "Malon kislota va ikki molekula etanol hosil bo'ladi.", Ma),
 ]),
 S("o-3", G, "write", 3, [
  W("Propandiol-1,3 ni konsentrlangan HNO₃ bilan oksidlang (NO ajraladi): malon kislota", ["C3H8O2", "HNO3"], ["C3H4O4", "NO", "H2O"], "3C3H8O2+8HNO3→3C3H4O4+8NO+10H2O", "Ikkala CH₂OH guruhi COOH ga oksidlanadi (8 e).", Ma),
  W("Butandiol-1,4 ni konsentrlangan HNO₃ bilan oksidlang (NO ajraladi): qahrabo kislota", ["C4H10O2", "HNO3"], ["C4H6O4", "NO", "H2O"], "3C4H10O2+8HNO3→3C4H6O4+8NO+10H2O", "Ikkala CH₂OH guruhi COOH ga oksidlanadi.", Qa),
 ]),
 S("o-4", G, "choice", 2, [
  C("Oksalat kislotaning tuzilish formulasi qaysi?", "HOOC–COOH", ["HOOC–CH₂–COOH", "CH₃COOH", "HOOC–(CH₂)₂–COOH"], "Ikkita karboksil guruhi to'g'ridan-to'g'ri bog'langan.", Ox, ("HOOC–CH₂–COOH", "Bu malon kislota: oraliqda CH₂ bor.")),
  C("Malon kislotaning tuzilish formulasi qaysi?", "HOOC–CH₂–COOH", ["HOOC–COOH", "HOOC–(CH₂)₂–COOH", "CH₃–CH(COOH)₂"], "Ikki karboksil orasida bitta CH₂ guruhi.", Ma, ("HOOC–COOH", "Bu oksalat kislota: oraliq uglerod yo'q.")),
 ]),
 S("o-5", G, "choice", 1, [
  C("Eng oddiy dikarbon kislota qaysi?", "Oksalat (shavel) kislota", ["Malon kislota", "Qahrabo kislota", "Adipin kislota"], "Faqat ikkita uglerod: HOOC–COOH.", Ox, ("Malon kislota", "Malon kislota uch uglerodli.")),
  C("Adipin kislota qaysi polimerning monomeri?", "Neylon (poliamid 6,6)", ["Kapron", "Lavsan", "Polietilen"], "Adipin kislota geksametilendiamin bilan neylon hosil qiladi.", Ad, ("Kapron", "Kapron kaprolaktamdan olinadi.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Xlorsirka kislotaga kaliy sianid ta'sir ettiring", ["C2H3ClO2", "KCN"], ["C3H3NO2", "KCl"], "C2H3ClO2+KCN→C3H3NO2+KCl", "Xlor CN ga almashinadi: siansirka kislota.", Ma),
  W("Siansirka kislotani gidrolizlang (H⁺, qizdirish)", ["C3H3NO2", "H2O"], ["C3H4O4", "NH3"], "C3H3NO2+2H2O→C3H4O4+NH3", "Nitril guruhi COOH ga o'tadi: malon kislota.", Ma),
 ]),
 S("x-2", G, "write", 2, [
  W("1,2-dibrometanga kaliy sianid ta'sir ettiring", ["C2H4Br2", "KCN"], ["C4H4N2", "KBr"], "C2H4Br2+2KCN→C4H4N2+2KBr", "Ikki brom CN ga almashinadi: suksinonitril.", Qa),
  W("Suksinonitrilni to'liq gidrolizlang (H⁺, qizdirish)", ["C4H4N2", "H2O"], ["C4H6O4", "NH3"], "C4H4N2+4H2O→C4H6O4+2NH3", "Ikkala nitril COOH ga o'tadi: qahrabo kislota.", Qa),
 ]),
 S("x-3", G, "choice", 1, [
  C("Oksalat kislota tabiatda qayerda ko'p uchraydi?", "Shovul va rovoch o'simliklarida", ["Sutda", "Asalda", "Tuxumda"], "Shovul kislotasi deb ham ataladi.", Ox),
  C("Qahrabo kislota nomini qaysi moddadan olgan?", "Qahrabo (amber)", ["Suyak", "Yog'och", "Tuz"], "Qahrabo smolasini quruq haydashdan topilgan.", Qa),
 ]),
]
G = "Kislotali xossalar"
slots += [
 S("m-1", G, "write", 1, [
  W("Oksalat kislotaga ortiqcha NaOH ta'sir ettiring", ["C2H2O4", "NaOH"], ["C2Na2O4", "H2O"], "C2H2O4+2NaOH→C2Na2O4+2H2O", "Ikkala karboksil neytrallanadi: natriy oksalat.", Ox),
  W("Malon kislotaga ortiqcha KOH ta'sir ettiring", ["C3H4O4", "KOH"], ["C3H2K2O4", "H2O"], "C3H4O4+2KOH→C3H2K2O4+2H2O", "Kaliy malonat hosil bo'ladi.", Ma),
 ]),
 S("m-2", G, "write", 1, [
  W("Qahrabo kislotaga ortiqcha NaOH ta'sir ettiring", ["C4H6O4", "NaOH"], ["C4H4Na2O4", "H2O"], "C4H6O4+2NaOH→C4H4Na2O4+2H2O", "Natriy suksinat hosil bo'ladi.", Qa),
  W("Adipin kislotaga ortiqcha NaOH ta'sir ettiring", ["C6H10O4", "NaOH"], ["C6H8Na2O4", "H2O"], "C6H10O4+2NaOH→C6H8Na2O4+2H2O", "Natriy adipinat hosil bo'ladi.", Ad),
 ]),
 S("m-3", G, "write", 2, [
  W("Oksalat kislotaga rux ta'sir ettiring", ["C2H2O4", "Zn"], ["C2O4Zn", "H2"], "C2H2O4+Zn→C2O4Zn+H2", "Rux oksalat va vodorod hosil bo'ladi.", Ox),
  W("Malon kislotaga magniy ta'sir ettiring", ["C3H4O4", "Mg"], ["C3H2MgO4", "H2"], "C3H4O4+Mg→C3H2MgO4+H2", "Magniy malonat va vodorod hosil bo'ladi.", Ma),
 ]),
 S("m-4", G, "write", 3, [
  W("Oksalat kislotaga 1 mol NaOH ta'sir ettiring (nordon tuz)", ["C2H2O4", "NaOH"], ["C2HNaO4", "H2O"], "C2H2O4+NaOH→C2HNaO4+H2O", "Faqat bitta karboksil neytrallanadi: gidrooksalat.", Ox),
  W("Malon kislotaga 1 mol NaOH ta'sir ettiring (nordon tuz)", ["C3H4O4", "NaOH"], ["C3H3NaO4", "H2O"], "C3H4O4+NaOH→C3H3NaO4+H2O", "Natriy gidromalonat hosil bo'ladi.", Ma),
 ]),
]
G = "Efir va amid"
slots += [
 S("e-1", G, "write", 2, [
  W("Oksalat kislota va ortiqcha metanol reaksiyasini yozing (H₂SO₄)", ["C2H2O4", "CH3OH"], ["C4H6O4", "H2O"], "C2H2O4+2CH3OH→C4H6O4+2H2O", "Dimetil oksalat hosil bo'ladi.", Ox),
  W("Malon kislota va ortiqcha etanol reaksiyasini yozing (H₂SO₄)", ["C3H4O4", "C2H5OH"], ["C7H12O4", "H2O"], "C3H4O4+2C2H5OH→C7H12O4+2H2O", "Dietil malonat hosil bo'ladi.", Ma),
 ]),
 S("e-2", G, "write", 2, [
  W("Oksalat kislotaga ammiak ta'sir ettiring (ortiqcha)", ["C2H2O4", "NH3"], ["C2H8N2O4"], "C2H2O4+2NH3→C2H8N2O4", "Ammoniy oksalat tuzi hosil bo'ladi.", Ox),
  W("Qahrabo kislotaga ammiak ta'sir ettiring (ortiqcha)", ["C4H6O4", "NH3"], ["C4H12N2O4"], "C4H6O4+2NH3→C4H12N2O4", "Ammoniy suksinat hosil bo'ladi.", Qa),
 ]),
 S("e-3", G, "write", 3, [
  W("Oksalat kislotaga ortiqcha PCl₅ ta'sir ettiring", ["C2H2O4", "PCl5"], ["C2Cl2O2", "POCl3", "HCl"], "C2H2O4+2PCl5→C2Cl2O2+2POCl3+2HCl", "Ikkala OH xlorga almashinadi: oksalilxlorid.", Ox),
  W("Malon kislotaga ortiqcha tionilxlorid ta'sir ettiring", ["C3H4O4", "SOCl2"], ["C3H2Cl2O2", "SO2", "HCl"], "C3H4O4+2SOCl2→C3H2Cl2O2+2SO2+2HCl", "Malonilxlorid hosil bo'ladi.", Ma),
 ]),
]
G = "Qizdirish"
slots += [
 S("t-1", G, "write", 2, [
  W("Oksalat kislotaning konsentrlangan H₂SO₄ bilan qizdirilganda parchalanishini yozing", ["C2H2O4"], ["CO2", "CO", "H2O"], "C2H2O4→CO2+CO+H2O", "Gazlar va suv ajraladi.", Ox),
  W("Oksalat kislotaning qizdirilganda chumoli kislota va CO₂ ga parchalanishini yozing", ["C2H2O4"], ["CH2O2", "CO2"], "C2H2O4→CH2O2+CO2", "Bitta karboksil CO₂ holida ajraladi.", Ox),
 ]),
 S("t-2", G, "write", 2, [
  W("Malon kislotaning qizdirilganda dekarboksillanishini yozing", ["C3H4O4"], ["C2H4O2", "CO2"], "C3H4O4→C2H4O2+CO2", "Bitta karboksil CO₂ holida ketadi: sirka kislota.", Ma),
  W("Metilmalon kislotaning qizdirilganda dekarboksillanishini yozing", ["C4H6O4"], ["C3H6O2", "CO2"], "C4H6O4→C3H6O2+CO2", "Propion kislota va CO₂ hosil bo'ladi.", None),
 ]),
 S("t-3", G, "write", 3, [
  W("Qahrabo kislotaning qizdirilganda angidridga aylanishini yozing", ["C4H6O4"], ["C4H4O3", "H2O"], "C4H6O4→C4H4O3+H2O", "Besh a'zoli halqa: suksinil angidrid.", Qa),
  W("Adipin kislotaning Ba(OH)₂ ishtirokida qizdirilishini yozing (siklopentanon)", ["C6H10O4"], ["C5H8O", "CO2", "H2O"], "C6H10O4→C5H8O+CO2+H2O", "Halqa yopiladi, CO₂ va suv ajraladi.", Ad),
 ]),
 S("t-4", G, "choice", 3, [
  C("Qizdirilganda CO₂ ajratib, bir asosli kislota beradigan dikarbon kislota qaysi?", "Malon kislota", ["Qahrabo kislota", "Adipin kislota", "Metan kislota"], "Ikki karboksil bitta uglerod orqali bog'langan: bittasi osongina CO₂ ga ketadi.", Ma, ("Qahrabo kislota", "Qahrabo kislota qizdirilganda angidrid hosil qiladi.")),
  C("Qahrabo kislota qizdirilganda nima hosil bo'ladi?", "Besh a'zoli halqali angidrid", ["Keton", "Sirka kislota va CO₂", "Hech narsa"], "Ikki karboksil orasida to'rt uglerod, besh a'zoli halqa barqaror.", Qa, ("Sirka kislota va CO₂", "Bu malon kislotaning qizdirish natijasi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 3, [
  W("Oksalat kislotani KMnO₄ bilan kislotali muhitda oksidlang (H₂SO₄)", ["C2H2O4", "KMnO4", "H2SO4"], ["CO2", "MnSO4", "K2SO4", "H2O"], "5C2H2O4+2KMnO4+3H2SO4→10CO2+2MnSO4+K2SO4+8H2O", "Har oksalat 2 e beradi, Mn⁺⁷ 5 e oladi: 5 : 2.", Ox),
  W("Oksalat kislotaning kislorod bilan to'liq yonishini yozing", ["C2H2O4", "O2"], ["CO2", "H2O"], "2C2H2O4+O2→4CO2+2H2O", "Oksalat kislota CO₂ va H₂O ga yonadi.", Ox),
 ]),
 S("k-2", G, "choice", 2, [
  C("Oksalat kislota KMnO₄ ni rangsizlantirganda qaysi gaz ajraladi?", "CO₂", ["CO", "H₂", "O₂"], "Oksalat to'liq CO₂ gacha oksidlanadi.", Ox, ("CO", "To'liq oksidlanishda CO₂ hosil bo'ladi.")),
  C("Malon kislota yonganda hosil bo'lgan CO₂ va H₂O ning mol nisbati qanday?", "3 : 2", ["2 : 3", "3 : 4", "1 : 1"], "C₃H₄O₄ dan 3 CO₂ va 2 H₂O.", Ma, ("3 : 4", "Vodorod 4 ta: suv 2 mol.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H12", "C6H11Cl", "C6H12O", "C6H10O4"]}
cB = {"all": ["CHNaO2", "C2Na2O4", "C2H2O4", "C2CaO4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (yorug'likda)", ["C6H12", "Cl2"], ["C6H11Cl", "HCl"], "C6H12+Cl2→C6H11Cl+HCl", "Siklogeksandagi vodorod xlorga almashinadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (qizdirish)", ["CHNaO2"], ["C2Na2O4", "H2"], "2CHNaO2→C2Na2O4+H2", "Natriy formiat qizdirilganda natriy oksalat va vodorod beradi.", Ox, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (NaOH ning suvdagi eritmasi)", ["C6H11Cl", "NaOH"], ["C6H12O", "NaCl"], "C6H11Cl+NaOH→C6H12O+NaCl", "Xlor OH ga almashinadi: siklogeksanol.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (H₂SO₄)", ["C2Na2O4", "H2SO4"], ["C2H2O4", "Na2SO4"], "C2Na2O4+H2SO4→C2H2O4+Na2SO4", "Kuchli kislota zaif kislotani siqib chiqaradi.", Ox, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (konsentrlangan HNO₃, NO ajraladi)", ["C6H12O", "HNO3"], ["C6H10O4", "NO", "H2O"], "3C6H12O+8HNO3→3C6H10O4+8NO+7H2O", "Halqa ochilib adipin kislota hosil bo'ladi.", Ad, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (ohakli suv)", ["C2H2O4", "Ca(OH)2"], ["C2CaO4", "H2O"], "C2H2O4+Ca(OH)2→C2CaO4+2H2O", "Kalsiy oksalat cho'kmasi: oksalat kislotaning sifat reaksiyasi.", Ox, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(16, "To'yingan dikarbon kislotalar", ["oksalat kislota", "malon kislota", "qahrabo kislota", "adipin kislota"], slots)
