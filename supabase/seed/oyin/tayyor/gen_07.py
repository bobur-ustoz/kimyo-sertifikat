from lib import *
M, E, P = ["metanol"], ["etanol"], ["propanol"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Etilenning gidratlanishini yozing (H₃PO₄, 300 °C)", ["C2H4", "H2O"], ["C2H5OH"], "C2H4+H2O→C2H5OH", "Suv qo'shbog'ga birikadi: etanol.", E),
  W("Propenning gidratlanishini yozing (H₃PO₄, qizdirish)", ["C3H6", "H2O"], ["C3H7OH"], "C3H6+H2O→C3H7OH", "Markovnikov: asosiy mahsulot propanol-2.", P),
 ]),
 S("o-2", G, "write", 1, [
  W("Bromoetanga NaOH ning suvdagi eritmasi ta'sir ettiring", ["C2H5Br", "NaOH"], ["C2H5OH", "NaBr"], "C2H5Br+NaOH→C2H5OH+NaBr", "Brom OH ga almashinadi: etanol.", E),
  W("Xlormetanga NaOH ning suvdagi eritmasi ta'sir ettiring", ["CH3Cl", "NaOH"], ["CH3OH", "NaCl"], "CH3Cl+NaOH→CH3OH+NaCl", "Xlor OH ga almashinadi: metanol.", M),
 ]),
 S("o-3", G, "write", 2, [
  W("Sirka aldegidni gidrogenlang (Ni, qizdirish)", ["C2H4O", "H2"], ["C2H6O"], "C2H4O+H2→C2H6O", "Karbonil guruh spirtga qaytariladi: etanol.", E),
  W("Formaldegidni gidrogenlang (Ni, qizdirish)", ["CH2O", "H2"], ["CH4O"], "CH2O+H2→CH4O", "Formaldegid metanolga qaytariladi.", M),
 ]),
 S("o-4", G, "choice", 2, [
  C("Sanoatda etilendan etanol olishda qaysi katalizator ishlatiladi?", "H₃PO₄", ["Ni", "KMnO₄", "AlCl₃"], "Fosfor kislota katalizator, gidratlanish 300 °C da boradi.", E, ("Ni", "Ni gidrogenlash uchun, gidratlash uchun emas.")),
  C("Sanoatda metanol qaysi gazlar aralashmasidan olinadi?", "CO va H₂", ["CO₂ va H₂", "CH₄ va O₂", "C va H₂O"], "CO + 2H₂ → CH₃OH (katalizator, bosim).", M, ("CO₂ va H₂", "Sanoat usuli uglerod(II) oksid va vodoroddan: CO + 2H₂.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Sintez-gazdan metanol olishni yozing (ZnO, Cr₂O₃, bosim)", ["CO", "H2"], ["CH3OH"], "CO+2H2→CH3OH", "Bitta CO ga ikki H₂ birikadi.", M),
  W("Glyukozaning spirtli bijg'ishini yozing (achitqi)", ["C6H12O6"], ["C2H5OH", "CO2"], "C6H12O6→2C2H5OH+2CO2", "Glyukozadan ikki etanol va ikki CO₂ hosil bo'ladi.", E),
 ]),
 S("x-2", G, "write", 2, [
  W("Etil atsetatga NaOH ta'sir ettiring (gidroliz)", ["C4H8O2", "NaOH"], ["C2H3NaO2", "C2H5OH"], "C4H8O2+NaOH→C2H3NaO2+C2H5OH", "Murakkab efir ishqorda spirt va tuzga ajraladi.", E),
  W("Metil formiatga NaOH ta'sir ettiring (gidroliz)", ["C2H4O2", "NaOH"], ["CHNaO2", "CH3OH"], "C2H4O2+NaOH→CHNaO2+CH3OH", "Gidrolizdan metanol va natriy formiat hosil bo'ladi.", M),
 ]),
 S("x-3", G, "choice", 1, [
  C("Glyukozaning spirtli bijg'ishidan qaysi moddalar hosil bo'ladi?", "Etanol va CO₂", ["Metanol va CO₂", "Sirka kislota va H₂O", "Etanol va O₂"], "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂.", E, ("Metanol va CO₂", "Bijg'ishda metanol emas, etanol hosil bo'ladi.")),
  C("Metanolning boshqa nomi qaysi?", "Yog'och spirti", ["Vino spirti", "Glikol", "Glitserin"], "Metanol qadimda yog'ochni quruq haydashdan olingan.", M, ("Vino spirti", "Vino spirti etanol. Metanol zaharli.")),
 ]),
]
G = "OH hisobiga (metallar)"
slots += [
 S("m-1", G, "write", 1, [
  W("Etanolga natriy ta'sir ettiring", ["C2H5OH", "Na"], ["C2H5ONa", "H2"], "2C2H5OH+2Na→2C2H5ONa+H2", "OH vodorodi natriyga almashinadi: natriy etilat.", E),
  W("Metanolga kaliy ta'sir ettiring", ["CH3OH", "K"], ["CH3OK", "H2"], "2CH3OH+2K→2CH3OK+H2", "Kaliy metilat va vodorod hosil bo'ladi.", M),
 ]),
 S("m-2", G, "write", 2, [
  W("Etanolga alyuminiy ta'sir ettiring (qizdirish)", ["C2H5OH", "Al"], ["(C2H5O)3Al", "H2"], "6C2H5OH+2Al→2(C2H5O)3Al+3H2", "Alyuminiy etilat: har metall atomiga uchta OH.", E),
  W("Propanolga magniy ta'sir ettiring (qizdirish)", ["C3H7OH", "Mg"], ["(C3H7O)2Mg", "H2"], "2C3H7OH+Mg→(C3H7O)2Mg+H2", "Magniy propilat hosil bo'ladi.", P),
 ]),
 S("m-3", G, "choice", 3, [
  C("Natriy etilat suvda erisa, qaysi moddalar hosil bo'ladi?", "Etanol va NaOH", ["Etilen va NaOH", "Dietil efir", "Sirka kislota"], "Alkogolyatlar suv bilan to'liq gidrolizlanadi: spirt ortiq kuchsiz kislota.", E, ("Dietil efir", "Efir hosil bo'lishi uchun H₂SO₄ va qizdirish kerak, suvda emas.")),
  C("Etanol quyidagilardan qaysi biri bilan reaksiyaga kirishmaydi?", "NaOH", ["Na", "K", "Ca"], "Spirt kuchsiz kislota: ishqor bilan reaksiya yo'q, faol metall bilan bor.", E, ("Na", "Natriy etanol bilan reaksiyaga kirishib vodorod chiqaradi.")),
 ]),
]
G = "OH almashinishi (HX)"
slots += [
 S("h-1", G, "write", 1, [
  W("Etanolga HBr ta'sir ettiring (H₂SO₄, qizdirish)", ["C2H5OH", "HBr"], ["C2H5Br", "H2O"], "C2H5OH+HBr→C2H5Br+H2O", "OH brom bilan almashinadi.", E),
  W("Metanolga HCl ta'sir ettiring (ZnCl₂, qizdirish)", ["CH3OH", "HCl"], ["CH3Cl", "H2O"], "CH3OH+HCl→CH3Cl+H2O", "OH xlorga almashinadi.", M),
 ]),
 S("h-2", G, "write", 2, [
  W("Etanolga fosfor(V) xlorid ta'sir ettiring", ["C2H5OH", "PCl5"], ["C2H5Cl", "POCl3", "HCl"], "C2H5OH+PCl5→C2H5Cl+POCl3+HCl", "PCl₅ OH ni xlorga almashtiradi.", E),
  W("Etanolga tionilxlorid (SOCl₂) ta'sir ettiring", ["C2H5OH", "SOCl2"], ["C2H5Cl", "SO2", "HCl"], "C2H5OH+SOCl2→C2H5Cl+SO2+HCl", "Gazlar ajralib chiqib reaksiya oxirigacha ketadi.", E),
 ]),
 S("h-3", G, "choice", 3, [
  C("Propanol-2 ga HBr ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "2-brompropan", ["1-brompropan", "Propen", "Propanal"], "OH shu uglerodning o'zida brom bilan almashinadi.", P, ("1-brompropan", "Almashinishda uglerod skeleti va o'rni o'zgarmaydi: OH qaysi uglerodda bo'lsa, brom shu yerda.")),
  C("Etanolning HBr bilan reaksiyasi qanday tur?", "Almashinish", ["Birikish", "Eliminatsiya", "Polimerlanish"], "OH guruhi bromga almashinadi, suv ajraladi.", E, ("Eliminatsiya", "Eliminatsiyada (degidratlashda) qo'shbog' hosil bo'ladi. Bu yerda esa OH bromga almashadi.")),
 ]),
]
G = "Degidratlanish"
slots += [
 S("d-1", G, "write", 1, [
  W("Etanolning molekula ichida degidratlanishini yozing (H₂SO₄ konts., 170 °C)", ["C2H5OH"], ["C2H4", "H2O"], "C2H5OH→C2H4+H2O", "Suv ajralib alken hosil bo'ladi.", E),
  W("Propanolning molekula ichida degidratlanishini yozing (H₂SO₄ konts., 170 °C)", ["C3H7OH"], ["C3H6", "H2O"], "C3H7OH→C3H6+H2O", "Propen hosil bo'ladi.", P),
 ]),
 S("d-2", G, "write", 2, [
  W("Etanolning molekulalararo degidratlanishini yozing (H₂SO₄, 140 °C)", ["C2H5OH"], ["C4H10O", "H2O"], "2C2H5OH→C4H10O+H2O", "Ikki molekuladan bitta suv ajraladi: dietil efir.", E),
  W("Metanolning molekulalararo degidratlanishini yozing (H₂SO₄, 140 °C)", ["CH3OH"], ["C2H6O", "H2O"], "2CH3OH→C2H6O+H2O", "Dimetil efir hosil bo'ladi.", M),
 ]),
 S("d-3", G, "choice", 2, [
  C("Etanol H₂SO₄ bilan 140 °C gacha qizdirilsa, qaysi modda hosil bo'ladi?", "Dietil efir", ["Etilen", "Etanal", "Sirka kislota"], "Past haroratda ikki molekula birlashadi.", E, ("Etilen", "Etilen 170 °C da hosil bo'ladi.")),
  C("Etanol H₂SO₄ bilan 170 °C gacha qizdirilsa, qaysi modda hosil bo'ladi?", "Etilen", ["Dietil efir", "Etanal", "Etan"], "Yuqori haroratda molekula ichidan suv ajraladi.", E, ("Dietil efir", "Efir 140 °C da hosil bo'ladi.")),
 ]),
 S("d-4", G, "choice", 3, [
  C("Butanol-2 degidratlanganda (Zaytsev qoidasi) asosiy mahsulot qaysi?", "Buten-2", ["Buten-1", "Butanal", "Dietil efir"], "Vodorod kamroq vodorodli qo'shni uglerodan ajraladi: qo'shbog' o'rtada.", None, ("Buten-1", "Buten-1 qo'shimcha mahsulot: Zaytsev bo'yicha mustahkamroq buten-2 asosiy.")),
  C("Propanol-2 degidratlanganda qaysi alken hosil bo'ladi?", "Propen", ["Propin", "Propanal", "Propan"], "Suv ajraladi va qo'shbog' hosil bo'ladi.", P, ("Propanal", "Propanal oksidlanishda hosil bo'ladi, degidratlashda emas.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Etanolning to'liq yonishini yozing", ["C2H5OH", "O2"], ["CO2", "H2O"], "C2H5OH+3O2→2CO2+3H2O", "Kislorod: 4 + 3 − 1 = 6 atom, ya'ni 3 O₂.", E),
  W("Metanolning to'liq yonishini yozing", ["CH3OH", "O2"], ["CO2", "H2O"], "2CH3OH+3O2→2CO2+4H2O", "Kasr chiqmasligi uchun ikki baravar.", M),
 ]),
 S("k-2", G, "write", 2, [
  W("Etanolni CuO bilan oksidlang (qizdirish)", ["C2H5OH", "CuO"], ["C2H4O", "Cu", "H2O"], "C2H5OH+CuO→C2H4O+Cu+H2O", "Birlamchi spirt aldegidga oksidlanadi.", E),
  W("Metanolni CuO bilan oksidlang (qizdirish)", ["CH3OH", "CuO"], ["CH2O", "Cu", "H2O"], "CH3OH+CuO→CH2O+Cu+H2O", "Metanoldan formaldegid hosil bo'ladi.", M),
 ]),
 S("k-3", G, "write", 3, [
  W("Etanolni kaliy dixromat bilan oksidlang (H₂SO₄, aldegidgacha)", ["C2H5OH", "K2Cr2O7", "H2SO4"], ["C2H4O", "Cr2(SO4)3", "K2SO4", "H2O"], "3C2H5OH+K2Cr2O7+4H2SO4→3C2H4O+Cr2(SO4)3+K2SO4+7H2O", "Cr⁺⁶ Cr⁺³ ga o'tadi, har spirt 2 e beradi: 3 : 1.", E),
  W("Propanol-2 ni kaliy dixromat bilan oksidlang (H₂SO₄)", ["C3H8O", "K2Cr2O7", "H2SO4"], ["C3H6O", "Cr2(SO4)3", "K2SO4", "H2O"], "3C3H8O+K2Cr2O7+4H2SO4→3C3H6O+Cr2(SO4)3+K2SO4+7H2O", "Ikkilamchi spirt ketonga oksidlanadi: aseton.", P),
 ]),
 S("k-4", G, "choice", 3, [
  C("Birlamchi spirt yengil oksidlanganda qaysi modda sinfi hosil bo'ladi?", "Aldegid", ["Keton", "Alkan", "Efir"], "CH₂OH guruhi CHO ga o'tadi.", E, ("Keton", "Keton ikkilamchi spirtdan hosil bo'ladi.")),
  C("Ikkilamchi spirt yengil oksidlanganda qaysi modda sinfi hosil bo'ladi?", "Keton", ["Aldegid", "Karbon kislota", "Efir"], "CHOH guruhi C=O ga o'tadi.", P, ("Aldegid", "Aldegid birlamchi spirtdan chiqadi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H5Br", "C2H6O", "C2H5Cl", "C4H10"]}
cB = {"all": ["C3H7Cl", "C3H8O", "C3H6O", "C3H8O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (KOH ning suvdagi eritmasi)", ["C2H5Br", "KOH"], ["C2H6O", "KBr"], "C2H5Br+KOH→C2H6O+KBr", "Brom OH ga almashinadi: etanol.", E, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (KOH ning suvdagi eritmasi)", ["C3H7Cl", "KOH"], ["C3H8O", "KCl"], "C3H7Cl+KOH→C3H8O+KCl", "Xlor OH ga almashinadi: propanol.", P, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (HCl, ZnCl₂)", ["C2H6O", "HCl"], ["C2H5Cl", "H2O"], "C2H6O+HCl→C2H5Cl+H2O", "OH xlorga almashinadi.", E, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (CuO, qizdirish)", ["C3H8O", "CuO"], ["C3H6O", "Cu", "H2O"], "C3H8O+CuO→C3H6O+Cu+H2O", "Spirt oksidlanib karbonilli birikma hosil qiladi.", P, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (Vyurs)", ["C2H5Cl", "Na"], ["C4H10", "NaCl"], "2C2H5Cl+2Na→C4H10+2NaCl", "Ikki etil radikal birlashadi: butan.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Ni, qizdirish)", ["C3H6O", "H2"], ["C3H8O"], "C3H6O+H2→C3H8O", "Karbonil guruh spirtga qaytariladi.", P, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(7, "Bir atomli to'yingan spirtlar", ["metanol", "etanol", "propanol"], slots)
