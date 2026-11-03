from lib import *
def Bd(p, name, w, uses=None):
    v = {"p": p, "build": name, "w": w}
    if uses: v["uses"] = uses
    return v
Me, Et, Pr, Bu, Ib = ["metan"], ["etan"], ["propan"], ["butan"], ["izobutan"]
slots = []
G = "Nomlanish"
slots += [
 S("nom-1", G, "build", 1, [
  Bd("2-metilpropan (izobutan) yig'ing", "2-metilpropan", "Asosiy zanjir 3 ta uglerod, ikkinchi uglerodda bitta metil: C₄H₁₀.", Ib),
  Bd("2-metilbutan yig'ing", "2-metilbutan", "Asosiy zanjir 4 ta uglerod, ikkinchi uglerodda bitta metil: C₅H₁₂."),
 ]),
 S("nom-2", G, "build", 1, [
  Bd("2,2-dimetilpropan yig'ing", "2,2-dimetilpropan", "Uch uglerodli zanjirning o'rtasida ikkita metil: markaziy uglerod to'rt uglerodga bog'langan (neopentan)."),
  Bd("2-metilpentan yig'ing", "2-metilpentan", "Asosiy zanjir 5 ta uglerod, ikkinchi uglerodda metil: C₆H₁₄."),
 ]),
 S("nom-3", G, "build", 2, [
  Bd("2,3-dimetilbutan yig'ing", "2,3-dimetilbutan", "To'rt uglerodli zanjirning 2- va 3-uglerodlarida bittadan metil: C₆H₁₄."),
  Bd("3-metilpentan yig'ing", "3-metilpentan", "Besh uglerodli zanjirning o'rtasida (3-uglerodda) metil: C₆H₁₄."),
 ]),
 S("nom-4", G, "choice", 1, [
  C("CH₃–CH₂–CH₂–CH₃ moddaning nomi qaysi?", "Butan", ["Izobutan", "Propan", "Pentan"], "To'rt uglerodli to'g'ri zanjir: butan.", Bu, ("Izobutan", "Izobutanda zanjir tarmoqlangan: CH₃–CH(CH₃)–CH₃.")),
  C("Alkanlarning umumiy formulasi qaysi?", "CₙH₂ₙ₊₂", ["CₙH₂ₙ", "CₙH₂ₙ₋₂", "CₙHₙ"], "To'yingan uglevodorodlar: vodorod soni uglerodnikidan ikki karra va yana ikkitaga ortiq.", Me, ("CₙH₂ₙ", "Bu alkenlar formulasi (bitta qo'shbog' bor).")),
 ]),
]
G = "Olinish: umumiy"
slots += [
 S("o-1", G, "write", 1, [
  W("1-brompropanga natriy ta'sir ettiring (Vyurs)", ["C3H7Br", "Na"], ["C6H14", "NaBr"], "2C3H7Br+2Na→C6H14+2NaBr", "Ikkita propil radikal birlashadi: uglerod soni ikki baravar ortadi.", None),
  W("Bromoetanga natriy ta'sir ettiring (Vyurs)", ["C2H5Br", "Na"], ["C4H10", "NaBr"], "2C2H5Br+2Na→C4H10+2NaBr", "Ikkita etil radikal birlashadi: butan.", Bu),
 ]),
 S("o-2", G, "write", 2, [
  W("Natriy atsetatni NaOH bilan qizdiring (quruq): metan hosil bo'ladi", ["C2H3NaO2", "NaOH"], ["CH4", "Na2CO3"], "C2H3NaO2+NaOH→CH4+Na2CO3", "Karboksil CO₂ holida ketadi (soda sifatida), bitta uglerod kam alkan hosil bo'ladi.", Me),
  W("Natriy propionatni NaOH bilan qizdiring (quruq): etan hosil bo'ladi", ["C3H5NaO2", "NaOH"], ["C2H6", "Na2CO3"], "C3H5NaO2+NaOH→C2H6+Na2CO3", "Bitta uglerod kam alkan hosil bo'ladi.", Et),
 ]),
 S("o-3", G, "write", 2, [
  W("Etilenning gidrogenlanishini yozing (Ni, qizdirish)", ["C2H4", "H2"], ["C2H6"], "C2H4+H2→C2H6", "Qo'shbog' to'yinadi: etan.", Et),
  W("Propenning gidrogenlanishini yozing (Ni, qizdirish)", ["C3H6", "H2"], ["C3H8"], "C3H6+H2→C3H8", "Qo'shbog' to'yinadi: propan.", Pr),
 ]),
 S("o-4", G, "choice", 1, [
  C("Laboratoriyada metan qanday olinadi?", "Natriy atsetatni NaOH bilan qizdirib", ["Etanolni degidratlab", "Atsetilenni gidratlab", "Etilenni gidrogenlab"], "CH₃COONa + NaOH → CH₄ + Na₂CO₃.", Me, ("Etanolni degidratlab", "Etanoldan suv ajralsa etilen hosil bo'ladi.")),
  C("Alkanlarni alkenlardan olishning usuli qaysi?", "Gidrogenlash", ["Gidratlash", "Degidratlash", "Polimerlash"], "Qo'shbog'ga vodorod birikib alkan hosil qiladi.", Et, ("Gidratlash", "Gidratlashda suv birikadi va spirt hosil bo'ladi.")),
 ]),
 S("o-5", G, "write", 3, [
  W("Natriy atsetat eritmasini elektroliz qiling (Kolbe): etan hosil bo'ladi", ["C2H3NaO2", "H2O"], ["C2H6", "CO2", "H2", "NaOH"], "2C2H3NaO2+2H2O→C2H6+2CO2+H2+2NaOH", "Anodda ikki metil radikal birlashadi.", Et),
  W("Natriy propionat eritmasini elektroliz qiling (Kolbe): butan hosil bo'ladi", ["C3H5NaO2", "H2O"], ["C4H10", "CO2", "H2", "NaOH"], "2C3H5NaO2+2H2O→C4H10+2CO2+H2+2NaOH", "Ikki etil radikal birlashadi.", Bu),
 ]),
]
G = "Olinish: xususiy"
slots += [
 S("x-1", G, "write", 2, [
  W("Alyuminiy karbidga suv ta'sir ettiring: metan hosil bo'ladi", ["Al4C3", "H2O"], ["CH4", "Al(OH)3"], "Al4C3+12H2O→3CH4+4Al(OH)3", "Karbid gidrolizlanib metan va alyuminiy gidroksid beradi.", Me),
  W("Uglerod va vodoroddan metan olishni yozing (Ni, 500 °C)", ["C", "H2"], ["CH4"], "C+2H2→CH4", "Sintez: bitta uglerodga ikki molekula vodorod.", Me),
 ]),
 S("x-2", G, "write", 2, [
  W("Uglerod(II) oksid va vodoroddan metan olishni yozing (Ni, 250 °C)", ["CO", "H2"], ["CH4", "H2O"], "CO+3H2→CH4+H2O", "Kislorod suv holida ajraladi.", Me),
  W("Uglerod(IV) oksid va vodoroddan metan olishni yozing (Sabatye)", ["CO2", "H2"], ["CH4", "H2O"], "CO2+4H2→CH4+2H2O", "Ikki kislorod ikki suv holida ajraladi.", Me),
 ]),
 S("x-3", G, "choice", 1, [
  C("Tabiiy gazning asosiy qismi qaysi modda?", "Metan", ["Etan", "Propan", "Butan"], "Tabiiy gazda taxminan 90–98% metan bor.", Me, ("Propan", "Propan va butan suyultirilgan gaz (ballon gazi) tarkibida.")),
  C("Yo'ldosh neft gazida qaysi alkanlar ko'p bo'ladi?", "Etan, propan, butan", ["Faqat metan", "Atsetilen", "Etilen"], "Neft bilan chiqadigan gazda metan bilan birga og'irroq alkanlar bor.", Pr, ("Atsetilen", "Atsetilen alkin: u tabiiy gazning tarkibiy qismi emas.")),
 ]),
]
G = "Almashinish"
slots += [
 S("a-1", G, "write", 1, [
  W("Metanga xlor ta'sir ettiring (yorug'likda, 1-bosqich)", ["CH4", "Cl2"], ["CH3Cl", "HCl"], "CH4+Cl2→CH3Cl+HCl", "Bitta vodorod xlorga almashinadi.", Me),
  W("Etanga brom ta'sir ettiring (yorug'likda, 1-bosqich)", ["C2H6", "Br2"], ["C2H5Br", "HBr"], "C2H6+Br2→C2H5Br+HBr", "Bitta vodorod bromga almashinadi.", Et),
 ]),
 S("a-2", G, "write", 2, [
  W("Metanga ortiqcha xlorning ikkinchi bosqichini yozing", ["CH4", "Cl2"], ["CH2Cl2", "HCl"], "CH4+2Cl2→CH2Cl2+2HCl", "Ikki vodorod xlorga almashinadi: dixlormetan.", Me),
  W("Metanning to'liq xlorlanishini yozing", ["CH4", "Cl2"], ["CCl4", "HCl"], "CH4+4Cl2→CCl4+4HCl", "Barcha to'rt vodorod almashinadi: uglerod tetraxlorid.", Me),
 ]),
 S("a-3", G, "write", 2, [
  W("Metanni nitrolang (HNO₃, qizdirish, bosim): Konovalov reaksiyasi", ["CH4", "HNO3"], ["CH3NO2", "H2O"], "CH4+HNO3→CH3NO2+H2O", "Vodorod nitro guruhga almashinadi.", Me),
  W("Propanni nitrolang (HNO₃, qizdirish)", ["C3H8", "HNO3"], ["C3H7NO2", "H2O"], "C3H8+HNO3→C3H7NO2+H2O", "Nitropropan hosil bo'ladi.", Pr),
 ]),
 S("a-4", G, "choice", 3, [
  C("Metanning xlorlanishi necha bosqichda boradi?", "To'rt bosqichda", ["Bir bosqichda", "Ikki bosqichda", "Uch bosqichda"], "CH₃Cl, CH₂Cl₂, CHCl₃, CCl₄ ketma-ket hosil bo'ladi.", Me, ("Bir bosqichda", "Reaksiya to'xtamaydi: barcha vodorodlar ketma-ket almashadi.")),
  C("Qaysi alkanda uchlamchi (3°) uglerodning vodorodi eng oson almashadi?", "Izobutan", ["Metan", "Etan", "Propan"], "Faqat izobutanda uchlamchi uglerod bor: radikal eng barqaror.", Ib, ("Etan", "Etanda faqat birlamchi uglerodlar bor.")),
 ]),
]
G = "Parchalanish"
slots += [
 S("p-1", G, "write", 1, [
  W("Metanning yuqori haroratda parchalanishini yozing (1000 °C)", ["CH4"], ["C", "H2"], "CH4→C+2H2", "Elementlarga parchalanadi: qurum va vodorod.", Me),
  W("Etanning degidrogenlanishini yozing (Ni, qizdirish)", ["C2H6"], ["C2H4", "H2"], "C2H6→C2H4+H2", "Vodorod ajralib alken hosil bo'ladi.", Et),
 ]),
 S("p-2", G, "write", 2, [
  W("Butanning krekingini yozing (alkan va alken hosil bo'ladi)", ["C4H10"], ["C2H6", "C2H4"], "C4H10→C2H6+C2H4", "Uglerod zanjiri o'rtasidan uziladi.", Bu),
  W("Propanning krekingini yozing", ["C3H8"], ["CH4", "C2H4"], "C3H8→CH4+C2H4", "Metan va etilen hosil bo'ladi.", Pr),
 ]),
 S("p-3", G, "choice", 1, [
  C("Krekking nima?", "Alkanlarni yuqori haroratda parchalash", ["Alkanni xlorlash", "Alkanni yoqish", "Alkanni gidrogenlash"], "Uzun zanjirli alkanlardan qisqa alkan va alkenlar olinadi.", Bu, ("Alkanni yoqish", "Yoqish oksidlanish, krekking esa termik parchalanish.")),
  C("Metanni 1500 °C gacha tez qizdirib, keyin keskin sovutsak, qaysi modda hosil bo'ladi?", "Atsetilen", ["Etan", "Etilen", "Benzol"], "2CH₄ → C₂H₂ + 3H₂.", Me, ("Etilen", "Etilen 1500 °C da emas, boshqa sharoitda hosil bo'ladi.")),
 ]),
]
G = "Izomerlanish"
slots += [
 S("i-1", G, "choice", 1, [
  C("C₄H₁₀ tarkibli nechta izomer bor?", "2", ["1", "3", "4"], "Butan va izobutan.", Bu, ("3", "Uchinchisi yo'q: faqat to'g'ri va bitta tarmoqli zanjir.")),
  C("C₅H₁₂ tarkibli nechta izomer bor?", "3", ["2", "4", "5"], "Pentan, 2-metilbutan, 2,2-dimetilpropan.", None, ("2", "Uchinchi, eng tarmoqli izomerni unutish xatosi.")),
 ]),
 S("i-2", G, "build", 2, [
  Bd("Geksanning tarmoqlangan izomeri 2,2-dimetilbutanni yig'ing", "2,2-dimetilbutan", "To'rt uglerodli zanjirning ikkinchi uglerodida ikkita metil: C₆H₁₄."),
  Bd("2,4-dimetilpentan yig'ing", "2,4-dimetilpentan", "Besh uglerodli zanjirning 2- va 4-uglerodlarida bittadan metil: C₇H₁₆."),
 ]),
 S("i-3", G, "choice", 2, [
  C("n-butanni izobutanga aylantirish uchun qanday katalizator ishlatiladi?", "AlCl₃", ["Ni", "KMnO₄", "H₂SO₄"], "Alyuminiy xlorid (qizdirishda) izomerlanishni tezlashtiradi.", Ib, ("Ni", "Ni gidrogenlash uchun.")),
  C("Alkanlar izomerlanganda oktan soni qanday o'zgaradi?", "Ortadi (tarmoqlangan izomerlar detonatsiyaga chidamliroq)", ["Kamayadi", "O'zgarmaydi", "Nolga teng bo'ladi"], "Benzin sifati tarmoqlangan izomerlar hisobiga yaxshilanadi.", Bu, ("Kamayadi", "Tarmoqlangan izomerlar yaxshiroq yonadi: oktan soni oshadi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Metanning to'liq yonishini yozing", ["CH4", "O2"], ["CO2", "H2O"], "CH4+2O2→CO2+2H2O", "Kislorod: 2 + 2 = 4 atom, ya'ni 2 O₂.", Me),
  W("Etanning to'liq yonishini yozing", ["C2H6", "O2"], ["CO2", "H2O"], "2C2H6+7O2→4CO2+6H2O", "Kasr chiqmasligi uchun ikki baravar.", Et),
 ]),
 S("k-2", G, "write", 2, [
  W("Propanning to'liq yonishini yozing", ["C3H8", "O2"], ["CO2", "H2O"], "C3H8+5O2→3CO2+4H2O", "Kislorod: 6 + 4 = 10 atom, ya'ni 5 O₂.", Pr),
  W("Butanning to'liq yonishini yozing", ["C4H10", "O2"], ["CO2", "H2O"], "2C4H10+13O2→8CO2+10H2O", "Kasr chiqmasligi uchun ikki baravar.", Bu),
 ]),
 S("k-3", G, "write", 2, [
  W("Metanning yetishmagan kislorodda yonishini yozing (CO hosil bo'ladi)", ["CH4", "O2"], ["CO", "H2O"], "2CH4+3O2→2CO+4H2O", "Uglerod CO gacha oksidlanadi.", Me),
  W("Metanning qurum hosil qilib yonishini yozing", ["CH4", "O2"], ["C", "H2O"], "CH4+O2→C+2H2O", "Juda kam kislorodda faqat vodorod yonadi, uglerod qurum bo'lib qoladi.", Me),
 ]),
 S("k-4", G, "choice", 1, [
  C("Alkanlar KMnO₄ eritmasini rangsizlantiradimi?", "Yo'q", ["Ha", "Faqat qizdirilganda", "Faqat kislotali muhitda"], "To'yingan uglevodorodlar oksidlovchilarga chidamli.", Pr, ("Ha", "Rangsizlantirish alkenlarga xos (qo'shbog' bor).")),
  C("Metan havoda yonganda alanga qanday bo'ladi?", "Ko'kimtir", ["Qurumli sariq", "Yashil", "Qizil"], "Metan toza yonadi: uglerod ulushi kam.", Me, ("Qurumli sariq", "Qurumli alanga uglerod ko'p moddalarda (masalan, atsetilen).")),
 ]),
]
G = "Zanjir"
cA = {"all": ["CH4", "CH3Br", "C2H6", "C2H5Cl", "C4H10"]}
cB = {"all": ["C3H8", "C3H7Cl", "C6H14", "C6H13Br", "C6H12"]}
slots += [
 S("z-1", G, "write", 1, [
  W("Zanjirning 1-reaksiyasini yozing (yorug'likda)", ["CH4", "Br2"], ["CH3Br", "HBr"], "CH4+Br2→CH3Br+HBr", "Vodorod bromga almashinadi.", Me, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (yorug'likda)", ["C3H8", "Cl2"], ["C3H7Cl", "HCl"], "C3H8+Cl2→C3H7Cl+HCl", "Bitta vodorod xlorga almashinadi.", Pr, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (Vyurs)", ["CH3Br", "Na"], ["C2H6", "NaBr"], "2CH3Br+2Na→C2H6+2NaBr", "Ikki metil radikal birlashadi.", Et, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (Vyurs)", ["C3H7Cl", "Na"], ["C6H14", "NaCl"], "2C3H7Cl+2Na→C6H14+2NaCl", "Uglerod soni ikki baravar ortadi: geksan.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 2, [
  W("Zanjirning 3-reaksiyasini yozing (yorug'likda)", ["C2H6", "Cl2"], ["C2H5Cl", "HCl"], "C2H6+Cl2→C2H5Cl+HCl", "Etanning bitta vodorodi xlorga almashinadi.", Et, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (yorug'likda)", ["C6H14", "Br2"], ["C6H13Br", "HBr"], "C6H14+Br2→C6H13Br+HBr", "Geksanning bitta vodorodi bromga almashinadi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
 S("z-4", G, "write", 3, [
  W("Zanjirning 4-reaksiyasini yozing (Vyurs)", ["C2H5Cl", "Na"], ["C4H10", "NaCl"], "2C2H5Cl+2Na→C4H10+2NaCl", "Ikki etil radikal birlashadi: butan.", Bu, {**cA, "at": 3}, "A"),
  W("Zanjirning 4-reaksiyasini yozing (KOH ning spirtdagi eritmasi)", ["C6H13Br", "KOH"], ["C6H12", "KBr", "H2O"], "C6H13Br+KOH→C6H12+KBr+H2O", "HBr ajralib qo'shbog' hosil bo'ladi: geksen.", None, {**cB, "at": 3}, "B"),
 ], "zanjir"),
]
save(1, "Alkanlar", ["metan", "etan", "propan", "butan", "izobutan"], slots)
