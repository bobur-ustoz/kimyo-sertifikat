from lib import *
Gl, Ri = ["glyukoza"], ["riboza"]
slots = []
G = "Tuzilish va izomeriya"
slots += [
 S("t-1", G, "choice", 1, [
  C("Glyukozaning molekulyar formulasi qaysi?", "C₆H₁₂O₆", ["C₁₂H₂₂O₁₁", "C₅H₁₀O₅", "C₆H₁₀O₅"], "Olti uglerodli monosaxarid (geksoza).", Gl, ("C₅H₁₀O₅", "Bu pentoza (riboza) formulasi.")),
  C("Ribozaning molekulyar formulasi qaysi?", "C₅H₁₀O₅", ["C₆H₁₂O₆", "C₅H₁₀O₄", "C₁₂H₂₂O₁₁"], "Besh uglerodli monosaxarid (pentoza).", Ri, ("C₆H₁₂O₆", "Bu geksoza (glyukoza, fruktoza) formulasi.")),
 ]),
 S("t-2", G, "choice", 1, [
  C("Glyukoza molekulasida qanday funksional guruhlar bor?", "Aldegid guruhi va 5 ta OH", ["Keton guruhi va 5 ta OH", "Aldegid guruhi va 4 ta OH", "Karboksil guruhi va 5 ta OH"], "Glyukoza aldogeksoza: aldegid va besh gidroksil.", Gl, ("Keton guruhi va 5 ta OH", "Keton guruhi fruktozada bor.")),
  C("Fruktoza molekulasida qanday karbonil guruhi bor?", "Keton guruhi", ["Aldegid guruhi", "Ikkita keton guruhi", "Karboksil guruhi"], "Fruktoza ketogeksoza.", Gl, ("Aldegid guruhi", "Aldegid guruhi glyukozada, fruktozada keton.")),
 ]),
 S("t-3", G, "choice", 2, [
  C("Glyukoza va fruktoza o'zaro qanday moddalar?", "Funksional guruh izomerlari", ["Zanjir izomerlari", "Bir xil modda", "Gomologlar"], "Formula bir xil (C₆H₁₂O₆), karbonil guruhi farq qiladi: aldegid va keton.", Gl, ("Gomologlar", "Gomologlar CH₂ guruhiga farq qiladi, bular esa bir xil formulali.")),
  C("Riboza va dezoksiriboza orasida qanday farq bor?", "Dezoksiribozada bitta kislorod atomi kam (2-holatda OH yo'q)", ["Dezoksiribozada bitta uglerod kam", "Ular bir xil modda", "Dezoksiribozada aldegid guruhi yo'q"], "Dezoksiriboza DNK tarkibiga, riboza RNK tarkibiga kiradi.", Ri, ("Dezoksiribozada bitta uglerod kam", "Uglerod soni bir xil (5), kislorod kam.")),
 ]),
 S("t-4", G, "choice", 3, [
  C("Glyukozaning halqali shaklida hosil bo'lgan yangi OH guruhi qanday ataladi?", "Glikozid (yarim atsetal) gidroksili", ["Spirt gidroksili", "Karboksil gidroksili", "Fenol gidroksili"], "Karbonil guruh bilan OH birikib yarim atsetal hosil qiladi: u eng faol OH.", Gl, ("Spirt gidroksili", "U oddiy spirt OH dan farq qiladi: yarim atsetal.")),
  C("Ochiq zanjirli glyukozada nechta asimmetrik uglerod atomi bor?", "4", ["3", "5", "6"], "C2, C3, C4 va C5.", Gl, ("5", "C6 va C1 asimmetrik emas, jami 4 ta.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Fotosintez reaksiyasini yozing (glyukoza hosil bo'ladi)", ["CO2", "H2O"], ["C6H12O6", "O2"], "6CO2+6H2O→C6H12O6+6O2", "Quyosh nuri energiyasi bilan CO₂ va suvdan glyukoza va kislorod hosil bo'ladi.", Gl),
  W("Pentozaning fotosintez (sxematik) hosil bo'lishini yozing: riboza", ["CO2", "H2O"], ["C5H10O5", "O2"], "5CO2+5H2O→C5H10O5+5O2", "Besh CO₂ va besh suvdan riboza va kislorod.", Ri),
 ]),
 S("o-2", G, "write", 2, [
  W("Formaldegiddan glyukoza olishni yozing (Butlerov sintezi, Ca(OH)₂)", ["CH2O"], ["C6H12O6"], "6CH2O→C6H12O6", "Oltita formaldegid molekulasi birlashadi.", Gl),
  W("Formaldegiddan riboza (pentoza) sxematik hosil bo'lishini yozing", ["CH2O"], ["C5H10O5"], "5CH2O→C5H10O5", "Beshta formaldegid molekulasi birlashadi.", Ri),
 ]),
 S("o-3", G, "write", 2, [
  W("Kraxmal (yoki sellyuloza) bir zvenosining gidrolizini yozing (H⁺)", ["C6H10O5", "H2O"], ["C6H12O6"], "C6H10O5+H2O→C6H12O6", "Har bir zveno suv biriktirib glyukoza beradi.", Gl),
  W("Sorbitning oksidlanishini (degidrogenlanishini) yozing", ["C6H14O6"], ["C6H12O6", "H2"], "C6H14O6→C6H12O6+H2", "Ko'p atomli spirt bitta guruhni karbonilga aylantiradi.", Gl),
 ]),
 S("o-4", G, "choice", 2, [
  C("Sanoatda glyukoza qaysi xomashyodan olinadi?", "Kraxmal yoki sellyulozaning gidrolizidan", ["Metandan", "Etanoldan", "Glitserindan"], "Kislotali gidrolizda polimer glyukozagacha parchalanadi.", Gl, ("Etanoldan", "Etanol glyukozadan hosil bo'ladi, aksincha emas.")),
  C("Fotosintez uchun nimalar kerak?", "CO₂, suv va quyosh nuri", ["O₂ va suv", "Faqat CO₂", "N₂ va H₂"], "Xlorofill nur energiyasini kimyoviy energiyaga aylantiradi.", Gl, ("O₂ va suv", "Kislorod fotosintezda hosil bo'ladi, sarflanmaydi.")),
 ]),
 S("o-5", G, "choice", 2, [
  C("Butlerov sintezi nimadan nimani beradi?", "Formaldegiddan ohakli suv ishtirokida shakarsimon moddalarni", ["Glyukozadan spirtni", "Kraxmaldan glyukozani", "Sellyulozadan atsetatni"], "Formaldegidning polikondensatsiyasi.", Gl, ("Kraxmaldan glyukozani", "Bu gidroliz, Butlerov sintezi emas.")),
  C("Fotosintezda qaysi gaz ajralib chiqadi?", "O₂", ["CO₂", "N₂", "H₂"], "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂.", Gl, ("CO₂", "CO₂ fotosintezda iste'mol qilinadi.")),
 ]),
]
G = "Aldegid guruhiga xos"
slots += [
 S("a-1", G, "write", 2, [
  W("Glyukozaga kumush oksidning ammiakli eritmasi ta'sir ettiring (kumush ko'zgu)", ["C6H12O6", "Ag2O"], ["C6H12O7", "Ag"], "C6H12O6+Ag2O→C6H12O7+2Ag", "Aldegid guruhi glyukon kislotaga oksidlanadi.", Gl),
  W("Ribozaga kumush oksidning ammiakli eritmasi ta'sir ettiring", ["C5H10O5", "Ag2O"], ["C5H10O6", "Ag"], "C5H10O5+Ag2O→C5H10O6+2Ag", "Riboza kislotaga oksidlanadi.", Ri),
 ]),
 S("a-2", G, "write", 2, [
  W("Glyukozaga mis(II) gidroksid ta'sir ettiring (qizdirish)", ["C6H12O6", "Cu(OH)2"], ["C6H12O7", "Cu2O", "H2O"], "C6H12O6+2Cu(OH)2→C6H12O7+Cu2O+2H2O", "Qizil cho'kma (Cu₂O) hosil bo'ladi.", Gl),
  W("Ribozaga mis(II) gidroksid ta'sir ettiring (qizdirish)", ["C5H10O5", "Cu(OH)2"], ["C5H10O6", "Cu2O", "H2O"], "C5H10O5+2Cu(OH)2→C5H10O6+Cu2O+2H2O", "Qizil cho'kma hosil bo'ladi.", Ri),
 ]),
 S("a-3", G, "write", 2, [
  W("Glyukozani gidrogenlang (Ni, qizdirish): sorbit", ["C6H12O6", "H2"], ["C6H14O6"], "C6H12O6+H2→C6H14O6", "Aldegid guruhi spirtga qaytariladi.", Gl),
  W("Ribozani gidrogenlang (Ni): ribit", ["C5H10O5", "H2"], ["C5H12O5"], "C5H10O5+H2→C5H12O5", "Besh atomli spirt hosil bo'ladi.", Ri),
 ]),
 S("a-4", G, "write", 3, [
  W("Glyukozaga bromli suv ta'sir ettiring", ["C6H12O6", "Br2", "H2O"], ["C6H12O7", "HBr"], "C6H12O6+Br2+H2O→C6H12O7+2HBr", "Aldegid guruhi kislotaga oksidlanadi (ketonlarda bu reaksiya bormaydi).", Gl),
  W("Ribozaga bromli suv ta'sir ettiring", ["C5H10O5", "Br2", "H2O"], ["C5H10O6", "HBr"], "C5H10O5+Br2+H2O→C5H10O6+2HBr", "Riboza ribon kislotaga oksidlanadi.", Ri),
 ]),
 S("a-5", G, "write", 3, [
  W("Glyukozaga gidroksilamin (NH₂OH) ta'sir ettiring", ["C6H12O6", "NH2OH"], ["C6H13NO6", "H2O"], "C6H12O6+NH2OH→C6H13NO6+H2O", "Aldegid guruhi oksimga aylanadi.", Gl),
  W("Glyukozaga fenilgidrazin ta'sir ettiring", ["C6H12O6", "C6H8N2"], ["C12H18N2O5", "H2O"], "C6H12O6+C6H8N2→C12H18N2O5+H2O", "Fenilgidrazon hosil bo'ladi.", Gl),
 ]),
]
G = "Gidroksil guruhiga xos"
slots += [
 S("h-1", G, "write", 2, [
  W("Glyukozaga mis(II) gidroksid ta'sir ettiring (sovuqda)", ["C6H12O6", "Cu(OH)2"], ["C12H22CuO12", "H2O"], "2C6H12O6+Cu(OH)2→C12H22CuO12+2H2O", "Ko'p atomli spirt kabi to'q ko'k mis kompleksi hosil qiladi.", Gl),
  W("Ribozaga mis(II) gidroksid ta'sir ettiring (sovuqda)", ["C5H10O5", "Cu(OH)2"], ["C10H18CuO10", "H2O"], "2C5H10O5+Cu(OH)2→C10H18CuO10+2H2O", "To'q ko'k eritma hosil bo'ladi.", Ri),
 ]),
 S("h-2", G, "write", 2, [
  W("Glyukozaga ortiqcha sirka angidrid ta'sir ettiring (pentaatsetat)", ["C6H12O6", "C4H6O3"], ["C16H22O11", "C2H4O2"], "C6H12O6+5C4H6O3→C16H22O11+5C2H4O2", "Beshta OH guruhi atsillanadi.", Gl),
  W("Glyukozaga konsentrlangan nitrat kislota ta'sir ettiring (pentanitrat)", ["C6H12O6", "HNO3"], ["C6H7N5O16", "H2O"], "C6H12O6+5HNO3→C6H7N5O16+5H2O", "Beshta OH nitrat efirga aylanadi.", Gl),
 ]),
 S("h-3", G, "write", 3, [
  W("Glyukozaga metanol ta'sir ettiring (HCl): metilglikozid", ["C6H12O6", "CH3OH"], ["C7H14O6", "H2O"], "C6H12O6+CH3OH→C7H14O6+H2O", "Yarim atsetal OH si metilga almashadi.", Gl),
  W("Glyukozaga etanol ta'sir ettiring (HCl): etilglikozid", ["C6H12O6", "C2H5OH"], ["C8H16O6", "H2O"], "C6H12O6+C2H5OH→C8H16O6+H2O", "Glikozid hosil bo'ladi.", Gl),
 ]),
 S("h-4", G, "choice", 2, [
  C("Glyukozaga Cu(OH)₂ sovuqda ta'sir ettirilsa, nima kuzatiladi?", "To'q ko'k eritma (ko'p atomli spirt)", ["Qizil cho'kma", "Rang va cho'kma yo'q", "Yashil cho'kma"], "Poliolga xos kompleks hosil bo'ladi.", Gl, ("Qizil cho'kma", "Qizil cho'kma qizdirilganda aldegid guruhi hisobiga hosil bo'ladi.")),
  C("Glyukozada aldegid guruhi borligini qaysi reaksiya ko'rsatadi?", "Kumush ko'zgu", ["FeCl₃ bilan binafsha rang", "Bromli suv bilan cho'kma", "Natriy bilan vodorod ajralishi"], "Faqat aldegidlar bu reaksiyani beradi.", Gl, ("Natriy bilan vodorod ajralishi", "Bu OH guruhi borligini ko'rsatadi, aldegid emas.")),
 ]),
]
G = "Bijg'ish"
slots += [
 S("b-1", G, "write", 1, [
  W("Glyukozaning sut kislotali bijg'ishini yozing", ["C6H12O6"], ["C3H6O3"], "C6H12O6→2C3H6O3", "Bakteriyalar ta'sirida ikki molekula sut kislota hosil bo'ladi.", Gl),
  W("Glyukozaning sirka kislotali bijg'ishini yozing", ["C6H12O6"], ["C2H4O2"], "C6H12O6→3C2H4O2", "Uch molekula sirka kislota hosil bo'ladi.", Gl),
 ]),
 S("b-2", G, "write", 2, [
  W("Glyukozaning moy kislotali bijg'ishini yozing", ["C6H12O6"], ["C4H8O2", "CO2", "H2"], "C6H12O6→C4H8O2+2CO2+2H2", "Moy kislota, CO₂ va vodorod hosil bo'ladi.", Gl),
  W("Glyukozaning limon kislotali bijg'ishini yozing (O₂ ishtirokida)", ["C6H12O6", "O2"], ["C6H8O7", "H2O"], "2C6H12O6+3O2→2C6H8O7+4H2O", "Mog'or zamburug'lari limon kislota hosil qiladi.", Gl),
 ]),
 S("b-3", G, "choice", 2, [
  C("Glyukozaning spirtli bijg'ishida qaysi gaz ajraladi?", "CO₂", ["O₂", "H₂", "CH₄"], "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂.", Gl, ("H₂", "Vodorod moy kislotali bijg'ishda ajraladi.")),
  C("Moy kislotali bijg'ishda qaysi gazlar ajraladi?", "CO₂ va H₂", ["CO₂ va O₂", "CH₄ va CO₂", "N₂ va H₂"], "C₆H₁₂O₆ → C₃H₇COOH + 2CO₂ + 2H₂.", Gl, ("CH₄ va CO₂", "Metan bijg'ishda emas, boshqa jarayonlarda hosil bo'ladi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H12O6", "C2H6O", "C2H4O", "C2H4O2"]}
cB = {"all": ["C6H12O6", "C7H13NO6", "C7H14O8", "C7H12O7"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (achitqi)", ["C6H12O6"], ["C2H6O", "CO2"], "C6H12O6→2C2H6O+2CO2", "Spirtli bijg'ish: etanol va CO₂.", Gl, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Kiliani–Fisher: sianid kislota)", ["C6H12O6", "HCN"], ["C7H13NO6"], "C6H12O6+HCN→C7H13NO6", "Siangidrin hosil bo'ladi: zanjir bir uglerodga uzayadi.", Gl, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (CuO, qizdirish)", ["C2H6O", "CuO"], ["C2H4O", "Cu", "H2O"], "C2H6O+CuO→C2H4O+Cu+H2O", "Etanol sirka aldegidga oksidlanadi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (H⁺, suv)", ["C7H13NO6", "H2O"], ["C7H14O8", "NH3"], "C7H13NO6+2H2O→C7H14O8+NH3", "Nitril gidrolizlanib aldon kislota hosil bo'ladi.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (kumush oksidning ammiakli eritmasi)", ["C2H4O", "Ag2O"], ["C2H4O2", "Ag"], "C2H4O+Ag2O→C2H4O2+2Ag", "Aldegid kislotaga oksidlanadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (qizdirish)", ["C7H14O8"], ["C7H12O7", "H2O"], "C7H14O8→C7H12O7+H2O", "Kislotaning OH guruhi bilan halqa hosil bo'ladi: lakton.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(20, "Monosaxaridlar", ["glyukoza", "riboza"], slots)
