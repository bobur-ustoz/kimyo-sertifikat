from lib import *
E, P = ["etilenglikol"], ["propilenglikol"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("1,2-dibrometanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C2H4Br2", "NaOH"], ["C2H6O2", "NaBr"], "C2H4Br2+2NaOH→C2H6O2+2NaBr", "Ikkala brom OH ga almashinadi: etilenglikol.", E),
  W("1,2-dibrompropanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C3H6Br2", "NaOH"], ["C3H8O2", "NaBr"], "C3H6Br2+2NaOH→C3H8O2+2NaBr", "Ikkala brom OH ga almashinadi: propilenglikol.", P),
 ]),
 S("o-2", G, "write", 2, [
  W("Etilen oksidning gidratlanishini yozing (H⁺, suv)", ["C2H4O", "H2O"], ["C2H6O2"], "C2H4O+H2O→C2H6O2", "Uch a'zoli halqa ochiladi: etilenglikol.", E),
  W("Propilen oksidning gidratlanishini yozing (H⁺, suv)", ["C3H6O", "H2O"], ["C3H8O2"], "C3H6O+H2O→C3H8O2", "Halqa ochiladi: propilenglikol.", P),
 ]),
 S("o-3", G, "write", 2, [
  W("Etilenning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner)", ["C2H4", "KMnO4", "H2O"], ["C2H6O2", "MnO2", "KOH"], "3C2H4+2KMnO4+4H2O→3C2H6O2+2MnO2+2KOH", "Qo'shbog'ga ikki OH birikadi.", E),
  W("Propenning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner)", ["C3H6", "KMnO4", "H2O"], ["C3H8O2", "MnO2", "KOH"], "3C3H6+2KMnO4+4H2O→3C3H8O2+2MnO2+2KOH", "Propilenglikol hosil bo'ladi.", P),
 ]),
 S("o-4", G, "choice", 1, [
  C("Etilenglikolning tuzilish formulasi qaysi?", "HOCH₂–CH₂OH", ["CH₃CH₂OH", "HOCH₂–CH(OH)–CH₂OH", "CH₃–CH(OH)₂"], "Ikki OH guruhi turli uglerodlarda.", E, ("CH₃–CH(OH)₂", "Bitta uglerodda ikkita OH beqaror: suv ajralib aldegid hosil bo'ladi.")),
  C("\"Glikol\" so'zi qanday spirtni bildiradi?", "Ikki atomli spirt", ["Uch atomli spirt", "To'yinmagan spirt", "Murakkab efir"], "Glikollarda ikkita OH guruhi bor.", E),
 ]),
 S("o-5", G, "choice", 2, [
  C("1,2-dixloretanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir etganda qaysi modda hosil bo'ladi?", "Etilenglikol", ["Etanol", "Etilen", "Sirka aldegid"], "Ikkala xlor OH ga almashinadi.", E, ("Etilen", "Etilen spirtli ishqor ta'sirida hosil bo'lardi.")),
  C("Eng oddiy glikol qaysi?", "Etilenglikol", ["Propilenglikol", "Glitserin", "Etanol"], "Ikki uglerodli, ikki OH guruhli.", E, ("Glitserin", "Glitserin uch atomli spirt.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Etilenning kislorod bilan katalitik oksidlanishini yozing (Ag, 250 °C): etilen oksid hosil bo'ladi", ["C2H4", "O2"], ["C2H4O"], "2C2H4+O2→2C2H4O", "Kislorod qo'shbog'ga birikib uch a'zoli halqa hosil qiladi.", E),
  W("Etilenga xlorli suv (HOCl) ta'sir ettiring", ["C2H4", "HOCl"], ["C2H5ClO"], "C2H4+HOCl→C2H5ClO", "2-xloretanol (xlorgidrin) hosil bo'ladi.", E),
 ]),
 S("x-2", G, "write", 3, [
  W("Glioksalni gidrogenlang (Ni, qizdirish)", ["C2H2O2", "H2"], ["C2H6O2"], "C2H2O2+2H2→C2H6O2", "Ikkala aldegid guruhi spirtga qaytariladi.", E),
  W("Metilglioksalni gidrogenlang (Ni, qizdirish)", ["C3H4O2", "H2"], ["C3H8O2"], "C3H4O2+2H2→C3H8O2", "Karbonil guruhlari qaytariladi.", P),
 ]),
 S("x-3", G, "choice", 1, [
  C("Etilenglikol sanoatda qaysi moddadan olinadi?", "Etilen oksid", ["Etanol", "Etilen", "Atsetilen"], "Etilen oksid gidratlanib glikol beradi.", E),
  C("Antifrizning (muzlamaydigan suyuqlik) asosiy komponenti qaysi?", "Etilenglikol", ["Etanol", "Glitserin", "Metanol"], "Suv bilan aralashmasi juda past haroratda muzlaydi.", E, ("Etanol", "Etanol ham muzlamaydi, lekin antifriz asosi etilenglikol.")),
 ]),
]
G = "OH hisobiga"
slots += [
 S("m-1", G, "write", 1, [
  W("Etilenglikolga ortiqcha natriy ta'sir ettiring", ["C2H6O2", "Na"], ["C2H4Na2O2", "H2"], "C2H6O2+2Na→C2H4Na2O2+H2", "Ikkala OH vodorodi natriyga almashinadi.", E),
  W("Etilenglikolga 1 mol natriy ta'sir ettiring (bitta OH)", ["C2H6O2", "Na"], ["C2H5NaO2", "H2"], "2C2H6O2+2Na→2C2H5NaO2+H2", "Faqat bitta OH vodorodi almashinadi.", E),
 ]),
 S("m-2", G, "write", 2, [
  W("Etilenglikolga mis(II) gidroksid ta'sir ettiring", ["C2H6O2", "Cu(OH)2"], ["C4H10CuO4", "H2O"], "2C2H6O2+Cu(OH)2→C4H10CuO4+2H2O", "To'q ko'k kompleks (mis glikolyat) hosil bo'ladi.", E),
  W("Propilenglikolga mis(II) gidroksid ta'sir ettiring", ["C3H8O2", "Cu(OH)2"], ["C6H14CuO4", "H2O"], "2C3H8O2+Cu(OH)2→C6H14CuO4+2H2O", "To'q ko'k eritma hosil bo'ladi.", P),
 ]),
 S("m-3", G, "choice", 2, [
  C("Glikolga yangi cho'ktirilgan Cu(OH)₂ ta'sir ettirilganda nima kuzatiladi?", "Cho'kma erib, to'q ko'k eritma hosil bo'ladi", ["Qizil cho'kma", "Rang o'zgarmaydi", "Gaz ajraladi"], "Mis atomi ikki OH bilan kompleks hosil qiladi.", E, ("Qizil cho'kma", "Qizil cho'kma (Cu₂O) aldegidlarga xos, glikolga emas.")),
  C("Yangi cho'ktirilgan Cu(OH)₂ qaysi modda sinfi uchun sifat reaksiyasi?", "Ko'p atomli spirtlar", ["Bir atomli spirtlar", "Alkenlar", "Oddiy efirlar"], "Qo'shni OH guruhlari to'q ko'k kompleks beradi.", E, ("Bir atomli spirtlar", "Bir atomli spirt Cu(OH)₂ bilan reaksiyaga kirishmaydi.")),
 ]),
]
G = "Almashinish va eterifikatsiya"
slots += [
 S("h-1", G, "write", 2, [
  W("Etilenglikolga ortiqcha HCl ta'sir ettiring", ["C2H6O2", "HCl"], ["C2H4Cl2", "H2O"], "C2H6O2+2HCl→C2H4Cl2+2H2O", "Ikkala OH xlorga almashinadi.", E),
  W("Propilenglikolga ortiqcha HBr ta'sir ettiring", ["C3H8O2", "HBr"], ["C3H6Br2", "H2O"], "C3H8O2+2HBr→C3H6Br2+2H2O", "Ikkala OH bromga almashinadi.", P),
 ]),
 S("h-2", G, "write", 2, [
  W("Etilenglikol va ortiqcha sirka kislota (H₂SO₄): diefir hosil bo'lishini yozing", ["C2H6O2", "C2H4O2"], ["C6H10O4", "H2O"], "C2H6O2+2C2H4O2→C6H10O4+2H2O", "Ikkala OH sirka kislota bilan efir hosil qiladi.", E),
  W("Etilenglikol va 1 mol sirka kislota (H₂SO₄): monoefir hosil bo'lishini yozing", ["C2H6O2", "C2H4O2"], ["C4H8O3", "H2O"], "C2H6O2+C2H4O2→C4H8O3+H2O", "Bitta OH esterlanadi.", E),
 ]),
 S("h-3", G, "choice", 3, [
  C("Etilenglikolga 1 mol HCl ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "2-xloretanol", ["1,2-dixloretan", "Xloretan", "Etilen oksid"], "Faqat bitta OH xlorga almashinadi.", E, ("1,2-dixloretan", "Dixloretan uchun ikki mol HCl kerak.")),
  C("Etilenglikol konsentrlangan HNO₃ bilan reaksiyaga kirishsa, qaysi modda hosil bo'ladi?", "Etilenglikol dinitrati", ["Nitroetan", "Glioksal", "Nitrobenzol"], "OH guruhlari nitrat efirga aylanadi (portlovchi modda).", E, ("Nitroetan", "Nitroetanda N uglerodga bog'langan. Nitrat efirda esa kislorod orqali.")),
 ]),
]
G = "Degidratlanish"
slots += [
 S("d-1", G, "write", 2, [
  W("Etilenglikolning molekulalararo degidratlanishini yozing (diglikol)", ["C2H6O2"], ["C4H10O3", "H2O"], "2C2H6O2→C4H10O3+H2O", "Ikki molekuladan bitta suv ajraladi: efir va spirt guruhli diglikol.", E),
  W("Propilenglikolning molekulalararo degidratlanishini yozing", ["C3H8O2"], ["C6H14O3", "H2O"], "2C3H8O2→C6H14O3+H2O", "Dipropilenglikol hosil bo'ladi.", P),
 ]),
 S("d-2", G, "write", 3, [
  W("Etilenglikolning ikki molekulasidan dioksan hosil bo'lishini yozing (H₂SO₄)", ["C2H6O2"], ["C4H8O2", "H2O"], "2C2H6O2→C4H8O2+2H2O", "Ikki molekuladan ikki suv ajraladi: olti a'zoli halqa, 1,4-dioksan.", E),
  W("Propilenglikolning molekula ichida degidratlanishini yozing (H₂SO₄)", ["C3H8O2"], ["C3H6O", "H2O"], "C3H8O2→C3H6O+H2O", "Bitta suv ajraladi, enol karbonilga izomerlanadi.", P),
 ]),
 S("d-3", G, "choice", 3, [
  C("Etilenglikolning ikki molekulasi to'liq degidratlansa, qaysi halqali modda hosil bo'ladi?", "1,4-dioksan", ["Etilen oksid", "Dietil efir", "Etilen"], "Ikki molekuladan ikki suv ajralib olti a'zoli halqa hosil bo'ladi.", E, ("Etilen oksid", "Etilen oksid bir molekulali uch a'zoli halqa. Bu yerda ikki molekula qatnashadi.")),
  C("Diglikol (HOCH₂CH₂–O–CH₂CH₂OH) qaysi sinflarga mansub?", "Oddiy efir va spirt", ["Keton", "Aldegid", "Karbon kislota"], "Molekulada –O– bog'i va ikkita OH guruhi bor.", E),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Etilenglikolning to'liq yonishini yozing", ["C2H6O2", "O2"], ["CO2", "H2O"], "2C2H6O2+5O2→4CO2+6H2O", "Kasr chiqmasligi uchun ikki baravar.", E),
  W("Propilenglikolning to'liq yonishini yozing", ["C3H8O2", "O2"], ["CO2", "H2O"], "C3H8O2+4O2→3CO2+4H2O", "Kislorod: 6 + 4 − 2 = 8 atom, ya'ni 4 O₂.", P),
 ]),
 S("k-2", G, "write", 2, [
  W("Etilenglikolni CuO bilan oksidlang (qizdirish): glioksal hosil bo'ladi", ["C2H6O2", "CuO"], ["C2H2O2", "Cu", "H2O"], "C2H6O2+2CuO→C2H2O2+2Cu+2H2O", "Ikkala birlamchi spirt guruhi aldegidga o'tadi.", E),
  W("Propilenglikolni CuO bilan oksidlang (qizdirish)", ["C3H8O2", "CuO"], ["C3H4O2", "Cu", "H2O"], "C3H8O2+2CuO→C3H4O2+2Cu+2H2O", "Metilglioksal hosil bo'ladi.", P),
 ]),
 S("k-3", G, "write", 3, [
  W("Etilenglikolni KMnO₄ bilan kislotali muhitda oksidlang (oksalat kislota)", ["C2H6O2", "KMnO4", "H2SO4"], ["C2H2O4", "MnSO4", "K2SO4", "H2O"], "5C2H6O2+8KMnO4+12H2SO4→5C2H2O4+8MnSO4+4K2SO4+22H2O", "Har CH₂OH guruhi COOH ga o'tadi (4 e), glikol 8 e beradi; Mn⁺⁷ 5 e oladi: 5 : 8.", E),
  W("Etilenglikolni konsentrlangan HNO₃ bilan oksidlang (oksalat kislota, NO ajraladi)", ["C2H6O2", "HNO3"], ["C2H2O4", "NO", "H2O"], "3C2H6O2+8HNO3→3C2H2O4+8NO+10H2O", "N⁺⁵ N⁺² ga o'tadi (3 e), glikol 8 e beradi: 3 : 8.", E),
 ]),
 S("k-4", G, "choice", 3, [
  C("Etilenglikol CuO bilan yengil oksidlansa, qaysi modda hosil bo'ladi?", "Glioksal", ["Sirka kislota", "Oksalat kislota", "Etanal"], "Ikkala CH₂OH guruhi CHO ga o'tadi.", E, ("Oksalat kislota", "Kislota kuchli oksidlovchilar bilan hosil bo'ladi.")),
  C("Etilenglikolni to'liq oksidlasak, qaysi dikarbon kislota hosil bo'ladi?", "Oksalat kislota", ["Malon kislota", "Sirka kislota", "Chumoli kislota"], "Ikki uglerodli dikarbon kislota: HOOC–COOH.", E, ("Malon kislota", "Malon kislota uch uglerodli.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4", "C2H4Cl2", "C2H6O2", "C2H4Br2"]}
cB = {"all": ["C2H4O", "C2H5ClO", "C2H6O2", "C2H4O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing", ["C2H4", "Cl2"], ["C2H4Cl2"], "C2H4+Cl2→C2H4Cl2", "Xlor qo'shbog'ga birikadi.", E, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing", ["C2H4O", "HCl"], ["C2H5ClO"], "C2H4O+HCl→C2H5ClO", "Halqa ochiladi: 2-xloretanol.", E, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (NaOH ning suvdagi eritmasi, ortiqcha)", ["C2H4Cl2", "NaOH"], ["C2H6O2", "NaCl"], "C2H4Cl2+2NaOH→C2H6O2+2NaCl", "Ikkala xlor OH ga almashinadi.", E, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (NaOH ning suvdagi eritmasi)", ["C2H5ClO", "NaOH"], ["C2H6O2", "NaCl"], "C2H5ClO+NaOH→C2H6O2+NaCl", "Xlor OH ga almashinadi.", E, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (HBr, ortiqcha)", ["C2H6O2", "HBr"], ["C2H4Br2", "H2O"], "C2H6O2+2HBr→C2H4Br2+2H2O", "Ikkala OH bromga almashinadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (H₂SO₄, qizdirish)", ["C2H6O2"], ["C2H4O", "H2O"], "C2H6O2→C2H4O+H2O", "Suv ajraladi, enol sirka aldegidga o'tadi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(9, "Ikki atomli spirtlar", ["etilenglikol", "propilenglikol"], slots)
