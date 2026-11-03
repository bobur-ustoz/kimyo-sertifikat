from lib import *
E, F, A = ["etanal"], ["formaldegid"], ["aseton"]
slots = []
G = "Umumiy olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Etanolni CuO bilan oksidlang (qizdirish)", ["C2H5OH", "CuO"], ["C2H4O", "Cu", "H2O"], "C2H5OH+CuO→C2H4O+Cu+H2O", "Birlamchi spirt aldegidga oksidlanadi.", E),
  W("Metanolni CuO bilan oksidlang (qizdirish)", ["CH3OH", "CuO"], ["CH2O", "Cu", "H2O"], "CH3OH+CuO→CH2O+Cu+H2O", "Metanoldan formaldegid hosil bo'ladi.", F),
 ]),
 S("o-2", G, "write", 2, [
  W("Atsetilenning gidratlanishini yozing (Kucherov: HgSO₄, H₂SO₄)", ["C2H2", "H2O"], ["C2H4O"], "C2H2+H2O→C2H4O", "Vinil spirt beqaror: sirka aldegidga o'tadi.", E),
  W("Propinning gidratlanishini yozing (Kucherov)", ["C3H4", "H2O"], ["C3H6O"], "C3H4+H2O→C3H6O", "Markovnikov: OH ikkinchi uglerodga, mahsulot aseton.", A),
 ]),
 S("o-3", G, "write", 2, [
  W("1,1-dixloretanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C2H4Cl2", "NaOH"], ["C2H4O", "NaCl", "H2O"], "C2H4Cl2+2NaOH→C2H4O+2NaCl+H2O", "Bitta uglerodda ikkita OH beqaror: suv ajralib aldegid hosil bo'ladi.", E),
  W("2,2-dixlorpropanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C3H6Cl2", "NaOH"], ["C3H6O", "NaCl", "H2O"], "C3H6Cl2+2NaOH→C3H6O+2NaCl+H2O", "Ikkinchi uglerodda ikki OH: suv ajraladi, keton hosil bo'ladi.", A),
 ]),
 S("o-4", G, "write", 2, [
  W("Kalsiy atsetatni qizdiring (quruq haydash): aseton hosil bo'ladi", ["C4H6CaO4"], ["C3H6O", "CaCO3"], "C4H6CaO4→C3H6O+CaCO3", "Kalsiy tuzi parchalanib keton va karbonat hosil qiladi.", A),
  W("Kalsiy formiat va kalsiy atsetat aralashmasini qizdiring: sirka aldegid hosil bo'ladi", ["C2H2CaO4", "C4H6CaO4"], ["C2H4O", "CaCO3"], "C2H2CaO4+C4H6CaO4→2C2H4O+2CaCO3", "Aralash tuz piroliz qilinganda aldegid olinadi.", E),
 ]),
 S("o-5", G, "choice", 1, [
  C("Birlamchi spirt yengil oksidlanganda qaysi modda hosil bo'ladi?", "Aldegid", ["Keton", "Efir", "Karbon kislota"], "CH₂OH guruhi CHO ga o'tadi.", E, ("Keton", "Keton ikkilamchi spirtdan hosil bo'ladi.")),
  C("Ikkilamchi spirt yengil oksidlanganda qaysi modda hosil bo'ladi?", "Keton", ["Aldegid", "Karbon kislota", "Efir"], "CHOH guruhi C=O ga o'tadi.", A, ("Aldegid", "Aldegid birlamchi spirtdan chiqadi.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 3, [
  W("Etanolning degidrogenlanishini yozing (Cu, 300 °C)", ["C2H5OH"], ["C2H4O", "H2"], "C2H5OH→C2H4O+H2", "Spirtdan vodorod ajralib aldegid hosil bo'ladi.", E),
  W("Propanol-2 ning degidrogenlanishini yozing (Cu, 300 °C)", ["C3H7OH"], ["C3H6O", "H2"], "C3H7OH→C3H6O+H2", "Ikkilamchi spirt ketonga aylanadi.", A),
 ]),
 S("x-2", G, "write", 2, [
  W("Metanolning havo kislorodi bilan oksidlanishini yozing (Ag, 600 °C)", ["CH3OH", "O2"], ["CH2O", "H2O"], "2CH3OH+O2→2CH2O+2H2O", "Formaldegidning sanoat usuli.", F),
  W("Propanol-2 ning havo kislorodi bilan oksidlanishini yozing (katalizator)", ["C3H8O", "O2"], ["C3H6O", "H2O"], "2C3H8O+O2→2C3H6O+2H2O", "Aseton hosil bo'ladi.", A),
 ]),
 S("x-3", G, "choice", 1, [
  C("Formalin nima?", "Formaldegidning 40% li suvli eritmasi", ["Etanolning 40% li eritmasi", "Aseton eritmasi", "Sirka kislota eritmasi"], "Formaldegid gaz, u suvda eritib ishlatiladi.", F),
  C("Sirka aldegidning formulasi qaysi?", "CH₃CHO", ["CH₃COCH₃", "HCHO", "CH₃COOH"], "Metil guruh va aldegid guruhi.", E, ("CH₃COCH₃", "Bu aseton: keton.")),
 ]),
]
G = "Karbonil guruhiga xos"
slots += [
 S("c-1", G, "write", 1, [
  W("Sirka aldegidni gidrogenlang (Ni, qizdirish)", ["C2H4O", "H2"], ["C2H6O"], "C2H4O+H2→C2H6O", "Karbonil guruh spirtga qaytariladi.", E),
  W("Formaldegidni gidrogenlang (Ni, qizdirish)", ["CH2O", "H2"], ["CH4O"], "CH2O+H2→CH4O", "Formaldegid metanolga qaytariladi.", F),
 ]),
 S("c-2", G, "write", 2, [
  W("Sirka aldegidga sianid kislota (HCN) ta'sir ettiring", ["C2H4O", "HCN"], ["C3H5NO"], "C2H4O+HCN→C3H5NO", "Siangidrin hosil bo'ladi: C=O ga birikish.", E),
  W("Asetonga sianid kislota (HCN) ta'sir ettiring", ["C3H6O", "HCN"], ["C4H7NO"], "C3H6O+HCN→C4H7NO", "Aseton siangidrini hosil bo'ladi.", A),
 ]),
 S("c-3", G, "write", 3, [
  W("Sirka aldegidga natriy gidrosulfit ta'sir ettiring", ["C2H4O", "NaHSO3"], ["C2H5NaO4S"], "C2H4O+NaHSO3→C2H5NaO4S", "Kristall gidrosulfit birikma hosil bo'ladi.", E),
  W("Asetonga natriy gidrosulfit ta'sir ettiring", ["C3H6O", "NaHSO3"], ["C3H7NaO4S"], "C3H6O+NaHSO3→C3H7NaO4S", "Gidrosulfit birikma hosil bo'ladi.", A),
 ]),
 S("c-4", G, "write", 3, [
  W("Sirka aldegidga 1 mol etanol ta'sir ettiring (yarim atsetal)", ["C2H4O", "C2H5OH"], ["C4H10O2"], "C2H4O+C2H5OH→C4H10O2", "Spirt karbonilga birikib yarim atsetal hosil qiladi.", E),
  W("Sirka aldegidga ortiqcha etanol ta'sir ettiring (H⁺, atsetal)", ["C2H4O", "C2H5OH"], ["C6H14O2", "H2O"], "C2H4O+2C2H5OH→C6H14O2+H2O", "Atsetal hosil bo'ladi, suv ajraladi.", E),
 ]),
 S("c-5", G, "write", 3, [
  W("Sirka aldegidga metilmagniy bromid (Grinyar) ta'sir ettiring", ["C2H4O", "CH3MgBr"], ["C3H7BrMgO"], "C2H4O+CH3MgBr→C3H7BrMgO", "Alkogolyat hosil bo'ladi: uglerod zanjiri uzayadi.", E),
  W("Hosil bo'lgan magniyli alkogolyatni suv bilan gidrolizlang", ["C3H7BrMgO", "H2O"], ["C3H8O", "Mg(OH)Br"], "C3H7BrMgO+H2O→C3H8O+Mg(OH)Br", "Gidrolizdan propanol-2 hosil bo'ladi.", E),
 ]),
]
G = "Karbonilga qo'shni vodorodga xos"
slots += [
 S("a-1", G, "write", 2, [
  W("Sirka aldegidga xlor ta'sir ettiring (α-vodorod almashinadi)", ["C2H4O", "Cl2"], ["C2H3ClO", "HCl"], "C2H4O+Cl2→C2H3ClO+HCl", "Karbonilga qo'shni uglerodning vodorodi xlorga almashinadi.", E),
  W("Asetonga brom ta'sir ettiring (α-vodorod almashinadi)", ["C3H6O", "Br2"], ["C3H5BrO", "HBr"], "C3H6O+Br2→C3H5BrO+HBr", "Bromatseton hosil bo'ladi.", A),
 ]),
 S("a-2", G, "write", 3, [
  W("Sirka aldegidning aldol kondensatsiyasini yozing (suyultirilgan ishqor)", ["C2H4O"], ["C4H8O2"], "2C2H4O→C4H8O2", "Aldol: 3-gidroksibutanal.", E),
  W("Asetonning aldol kondensatsiyasini yozing (Ba(OH)₂)", ["C3H6O"], ["C6H12O2"], "2C3H6O→C6H12O2", "Diatsetonspirt hosil bo'ladi.", A),
 ]),
 S("a-3", G, "choice", 3, [
  C("Aldol kondensatsiyada qaysi vodorod ishtirok etadi?", "Karbonilga qo'shni (α) uglerodning vodorodi", ["Aldegid guruhining vodorodi", "Gidroksil vodorodi", "Har qanday metil vodorodi"], "α-vodorod ishqorda harakatchan bo'ladi.", E, ("Aldegid guruhining vodorodi", "Aldegid vodorodi emas, qo'shni uglerodning vodorodi.")),
  C("Formaldegid aldol kondensatsiyaga kirishadimi?", "Yo'q: α-vodorodi yo'q", ["Ha", "Faqat ishqorda", "Faqat kislotada"], "Karbonilga qo'shni uglerod yo'q.", F, ("Ha", "Aldol uchun α-vodorod kerak, formaldegidda u yo'q.")),
 ]),
]
G = "Xususiy reaksiyalar"
slots += [
 S("r-1", G, "write", 3, [
  W("Sirka aldegidga kumush oksidning ammiakli eritmasi ta'sir ettiring (kumush ko'zgu)", ["C2H4O", "Ag2O"], ["C2H4O2", "Ag"], "C2H4O+Ag2O→C2H4O2+2Ag", "Aldegid kislotaga oksidlanadi, kumush ajraladi.", E),
  W("Formaldegidga ortiqcha kumush oksid ta'sir ettiring (kumush ko'zgu)", ["CH2O", "Ag2O"], ["CO2", "H2O", "Ag"], "CH2O+2Ag2O→CO2+H2O+4Ag", "Formaldegid to'liq oksidlanadi: 1 mol dan 4 mol kumush.", F),
 ]),
 S("r-2", G, "write", 2, [
  W("Sirka aldegidga mis(II) gidroksid ta'sir ettiring (qizdirish)", ["C2H4O", "Cu(OH)2"], ["C2H4O2", "Cu2O", "H2O"], "C2H4O+2Cu(OH)2→C2H4O2+Cu2O+2H2O", "Qizil cho'kma (Cu₂O) hosil bo'ladi.", E),
  W("Formaldegidga ortiqcha mis(II) gidroksid ta'sir ettiring (qizdirish)", ["CH2O", "Cu(OH)2"], ["CO2", "Cu2O", "H2O"], "CH2O+4Cu(OH)2→CO2+2Cu2O+5H2O", "To'liq oksidlanish: 4 mol Cu(OH)₂ sarflanadi.", F),
 ]),
 S("r-3", G, "write", 3, [
  W("Sirka aldegidni KMnO₄ bilan kislotali muhitda oksidlang (H₂SO₄)", ["C2H4O", "KMnO4", "H2SO4"], ["C2H4O2", "MnSO4", "K2SO4", "H2O"], "5C2H4O+2KMnO4+3H2SO4→5C2H4O2+2MnSO4+K2SO4+3H2O", "Aldegid sirka kislotaga o'tadi (2 e), Mn⁺⁷ 5 e oladi: 5 : 2.", E),
  W("Formaldegidni KMnO₄ bilan kislotali muhitda oksidlang (H₂SO₄)", ["CH2O", "KMnO4", "H2SO4"], ["CO2", "MnSO4", "K2SO4", "H2O"], "5CH2O+4KMnO4+6H2SO4→5CO2+4MnSO4+2K2SO4+11H2O", "Formaldegid CO₂ gacha oksidlanadi (4 e): 5 : 4.", F),
 ]),
 S("r-4", G, "choice", 2, [
  C("\"Kumush ko'zgu\" reaksiyasi qaysi modda sinfi uchun xos?", "Aldegidlar", ["Ketonlar", "Spirtlar", "Efirlar"], "Aldegid kumush oksidni qaytarib, kumush ko'zgu hosil qiladi.", E, ("Ketonlar", "Ketonlar oson oksidlanmaydi, kumush ko'zgu bermaydi.")),
  C("Aseton kumush oksidning ammiakli eritmasi bilan reaksiyaga kirishadimi?", "Yo'q", ["Ha", "Faqat qizdirilganda", "Faqat ishqorda"], "Keton oson oksidlanmaydi.", A, ("Ha", "Faqat aldegidlar bu reaksiyaga kirishadi.")),
 ]),
 S("r-5", G, "choice", 3, [
  C("1 mol formaldegid kumush oksidning ammiakli eritmasi bilan to'liq reaksiyaga kirishganda necha mol kumush hosil bo'ladi?", "4", ["1", "2", "3"], "Formaldegidda ikkita aldegid vodorodi bor: u CO₂ gacha oksidlanadi.", F, ("2", "2 mol sirka aldegiddan chiqadi. Formaldegid ikki bosqichda oksidlanib 4 mol kumush beradi.")),
  C("1 mol sirka aldegid kumush oksid bilan reaksiyaga kirishganda necha mol kumush hosil bo'ladi?", "2", ["1", "4", "3"], "Bitta aldegid guruhi: 2 mol Ag.", E, ("4", "4 mol faqat formaldegidga xos.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4", "C2H6O", "C2H4O", "C4H10O2"]}
cB = {"all": ["C3H6", "C3H8O", "C3H6O", "C3H8O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (H₃PO₄, 300 °C)", ["C2H4", "H2O"], ["C2H6O"], "C2H4+H2O→C2H6O", "Etanol hosil bo'ladi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (H₃PO₄, qizdirish)", ["C3H6", "H2O"], ["C3H8O"], "C3H6+H2O→C3H8O", "Markovnikov: propanol-2.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (Cu, katalizator)", ["C2H6O", "O2"], ["C2H4O", "H2O"], "2C2H6O+O2→2C2H4O+2H2O", "Etanol sirka aldegidga oksidlanadi.", E, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (CuO, qizdirish)", ["C3H8O", "CuO"], ["C3H6O", "Cu", "H2O"], "C3H8O+CuO→C3H6O+Cu+H2O", "Ikkilamchi spirt ketonga o'tadi.", A, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (metanol, H⁺)", ["C2H4O", "CH3OH"], ["C4H10O2", "H2O"], "C2H4O+2CH3OH→C4H10O2+H2O", "Dimetilatsetal hosil bo'ladi.", E, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Ni, qizdirish)", ["C3H6O", "H2"], ["C3H8O"], "C3H6O+H2→C3H8O", "Aseton qaytarilib propanol-2 hosil qiladi.", A, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(13, "Aldegidlar va ketonlar", ["etanal", "formaldegid", "aseton"], slots)
