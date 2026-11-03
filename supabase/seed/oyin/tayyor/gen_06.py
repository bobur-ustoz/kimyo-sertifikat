from lib import *
B, T, S_ = ["benzol"], ["toluol"], ["stirol"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Geksanning degidrosiklanishini yozing (Pt, qizdirish): benzol hosil bo'ladi", ["C6H14"], ["C6H6", "H2"], "C6H14→C6H6+4H2", "Halqa yopiladi va to'rt molekula vodorod ajraladi.", B),
  W("Geptanning degidrosiklanishini yozing (Pt, qizdirish): toluol hosil bo'ladi", ["C7H16"], ["C7H8", "H2"], "C7H16→C7H8+4H2", "Zanjir halqaga yopiladi, to'rt vodorod ajraladi.", T),
 ]),
 S("o-2", G, "write", 2, [
  W("Brombenzol, brommetan va natriy: toluol olish reaksiyasini yozing (Vyurs–Fittig)", ["C6H5Br", "CH3Br", "Na"], ["C7H8", "NaBr"], "C6H5Br+CH3Br+2Na→C7H8+2NaBr", "Ikkala radikal birlashadi: fenil + metil.", T),
  W("Benzol va xlormetanni reaksiyasini yozing (AlCl₃, Fridel–Krafts)", ["C6H6", "CH3Cl"], ["C7H8", "HCl"], "C6H6+CH3Cl→C7H8+HCl", "Metil guruh halqaga birikadi, HCl ajraladi.", T),
 ]),
 S("o-3", G, "choice", 1, [
  C("Benzolni atsetilendan olish usuli qaysi?", "Atsetilenni 450 °C da aktivlangan ko'mir ustida trimerlash", ["Etilenni polimerlash", "Metanni xlorlash", "Etanolni degidratlash"], "Uch molekula atsetilen bitta benzol halqasiga birlashadi.", B, ("Etilenni polimerlash", "Etilen polietilen beradi, halqa emas.")),
  C("Fridel–Krafts reaksiyasida qanday katalizator ishlatiladi?", "AlCl₃", ["Ni", "H₂SO₄", "KMnO₄"], "Suvsiz alyuminiy xlorid galogenalkanni faollashtiradi.", T, ("H₂SO₄", "H₂SO₄ nitrolash va sulfolash uchun, Fridel–Krafts uchun emas.")),
 ]),
]
G = "Birikish"
slots += [
 S("b-1", G, "write", 1, [
  W("Benzolning gidrogenlanishini yozing (Ni, qizdirish)", ["C6H6", "H2"], ["C6H12"], "C6H6+3H2→C6H12", "Uch molekula vodorod birikib siklogeksan hosil bo'ladi.", B),
  W("Toluolning gidrogenlanishini yozing (Ni, qizdirish)", ["C7H8", "H2"], ["C7H14"], "C7H8+3H2→C7H14", "Halqa to'yinadi: metilsiklogeksan.", T),
 ]),
 S("b-2", G, "write", 2, [
  W("Benzolga yorug'likda xlor ta'sir ettiring (to'liq birikish)", ["C6H6", "Cl2"], ["C6H6Cl6"], "C6H6+3Cl2→C6H6Cl6", "Yorug'likda uch molekula xlor birikadi: geksaxloran.", B),
  W("Stirolga vodorod ta'sir ettiring (yumshoq sharoit, faqat yon zanjir)", ["C8H8", "H2"], ["C8H10"], "C8H8+H2→C8H10", "Yon zanjirdagi qo'shbog' to'yinadi, halqa o'zgarmaydi: etilbenzol.", S_),
 ]),
 S("b-3", G, "choice", 2, [
  C("Benzol bromli suvni rangsizlantiradimi?", "Yo'q: aromatik halqa barqaror", ["Ha: uchta qo'shbog'i bor", "Faqat qizdirilganda", "Ha, tez"], "Benzolda oddiy qo'shbog'lar yo'q: yagona aromatik π-tizim.", B, ("Ha: uchta qo'shbog'i bor", "Kekule formulasi shartli: haqiqatda halqa barqaror, oddiy sharoitda birikish bormaydi.")),
  C("Stirol bromli suvni rangsizlantiradimi?", "Ha: yon zanjirdagi qo'shbog' tufayli", ["Yo'q: aromatik", "Faqat FeBr₃ bilan", "Faqat yorug'likda"], "Qo'shbog' halqada emas, yon zanjirda: u oson birikadi.", S_, ("Yo'q: aromatik", "Halqa barqaror, lekin yon zanjirdagi qo'shbog' brom bilan birikadi.")),
 ]),
]
G = "O'rin olish"
slots += [
 S("p-1", G, "write", 1, [
  W("Benzolga brom ta'sir ettiring (FeBr₃ katalizatori)", ["C6H6", "Br2"], ["C6H5Br", "HBr"], "C6H6+Br2→C6H5Br+HBr", "Vodorod bromga almashinadi, halqa saqlanadi.", B),
  W("Benzolga xlor ta'sir ettiring (FeCl₃ katalizatori)", ["C6H6", "Cl2"], ["C6H5Cl", "HCl"], "C6H6+Cl2→C6H5Cl+HCl", "Vodorod xlorga almashinadi.", B),
 ]),
 S("p-2", G, "write", 2, [
  W("Benzolni nitrolang (HNO₃ + H₂SO₄ aralashmasi)", ["C6H6", "HNO3"], ["C6H5NO2", "H2O"], "C6H6+HNO3→C6H5NO2+H2O", "Nitro guruh halqaga birikadi, suv ajraladi.", B),
  W("Benzolni sulfolang (konsentrlangan H₂SO₄)", ["C6H6", "H2SO4"], ["C6H6O3S", "H2O"], "C6H6+H2SO4→C6H6O3S+H2O", "Benzolsulfokislota hosil bo'ladi.", B),
 ]),
 S("p-3", G, "write", 2, [
  W("Toluolga xlor yorug'likda ta'sir ettiring (yon zanjirda o'rin olish)", ["C7H8", "Cl2"], ["C7H7Cl", "HCl"], "C7H8+Cl2→C7H7Cl+HCl", "Yorug'likda CH₃ guruhidagi vodorod almashinadi: benzilxlorid.", T),
  W("Toluolni mononitrolang (HNO₃ + H₂SO₄)", ["C7H8", "HNO3"], ["C7H7NO2", "H2O"], "C7H8+HNO3→C7H7NO2+H2O", "Nitro guruh o- yoki p- holatga birikadi.", T),
 ]),
 S("p-4", G, "choice", 3, [
  C("Toluolga xlor yorug'likda ta'sir etganda qaysi modda hosil bo'ladi?", "Benzilxlorid", ["o-xlortoluol", "p-xlortoluol", "Benzoy kislota"], "Yorug'lik radikal sharoit yaratadi: yon zanjir almashinadi.", T, ("o-xlortoluol", "Halqaga xlor FeCl₃ bilan boradi, yorug'likda emas.")),
  C("Toluolga FeCl₃ ishtirokida xlor ta'sir etganda asosiy mahsulot nima?", "o- va p-xlortoluol", ["Benzilxlorid", "m-xlortoluol", "Benzaldegid"], "Katalizator halqada almashinishga olib keladi; CH₃ o,p-yo'naltiruvchi.", T, ("Benzilxlorid", "Benzilxlorid yorug'likda hosil bo'ladi, katalizatorda emas.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Benzolning to'liq yonishini yozing", ["C6H6", "O2"], ["CO2", "H2O"], "2C6H6+15O2→12CO2+6H2O", "Kasrdan qutulish uchun ikki baravar: 2C₆H₆ + 15O₂.", B),
  W("Toluolning to'liq yonishini yozing", ["C7H8", "O2"], ["CO2", "H2O"], "C7H8+9O2→7CO2+4H2O", "Kislorod: 14 + 4 = 18 atom, ya'ni 9 O₂.", T),
 ]),
 S("k-2", G, "write", 3, [
  W("Toluolning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄)", ["C7H8", "KMnO4", "H2SO4"], ["C7H6O2", "MnSO4", "K2SO4", "H2O"], "5C7H8+6KMnO4+9H2SO4→5C7H6O2+6MnSO4+3K2SO4+14H2O", "CH₃ guruh COOH ga o'tadi: benzoy kislota.", T),
  W("Etilbenzolning KMnO₄ bilan kislotali muhitda oksidlanishini yozing (H₂SO₄)", ["C8H10", "KMnO4", "H2SO4"], ["C7H6O2", "CO2", "MnSO4", "K2SO4", "H2O"], "5C8H10+12KMnO4+18H2SO4→5C7H6O2+5CO2+12MnSO4+6K2SO4+28H2O", "Yon zanjir uziladi: halqada faqat COOH qoladi, ikkinchi uglerod CO₂ ga.", None),
 ]),
 S("k-3", G, "choice", 2, [
  C("Benzol KMnO₄ eritmasini rangsizlantiradimi?", "Yo'q", ["Ha", "Faqat qizdirilganda", "Faqat kislotali muhitda"], "Aromatik halqa oksidlovchiga chidamli.", B, ("Ha", "Benzol halqasi barqaror: KMnO₄ ni rangsizlantirmaydi.")),
  C("Toluol KMnO₄ bilan oksidlanganda qaysi modda hosil bo'ladi?", "Benzoy kislota", ["Benzaldegid", "Fenol", "Benzol"], "Faqat yon zanjir oksidlanadi, CH₃ guruhi COOH ga aylanadi.", T, ("Fenol", "Halqaga OH birikmaydi: yon zanjir oksidlanadi.")),
 ]),
]
G = "Polimerlanish"
slots += [
 S("l-1", G, "choice", 1, [
  C("Stirolning polimerlanishidan qaysi polimer hosil bo'ladi?", "Polistirol", ["Polietilen", "Polivinilxlorid", "Polipropilen"], "Yon zanjirdagi qo'shbog' ochilib zanjir hosil qiladi.", S_),
  C("Stirolning tuzilish formulasi qaysi?", "C₆H₅–CH=CH₂", ["C₆H₅–CH₃", "C₆H₅–C₂H₅", "C₆H₅–C≡CH"], "Benzol halqasiga vinil guruh birikkan.", S_, ("C₆H₅–C₂H₅", "Bu etilbenzol (to'yingan): qo'shbog' yo'q.")),
 ]),
 S("l-2", G, "choice", 3, [
  C("Molyar massasi 104 000 g/mol bo'lgan polistirolning polimerlanish darajasi qancha (M(C₈H₈) = 104)?", "1000", ["10 000", "100", "2000"], "104 000 : 104 = 1000.", S_, ("10 000", "Nol xatosi. 104 000 : 104 = 1000.")),
  C("Polistirolning polimerlanish darajasi 500 bo'lsa, molyar massasi qancha (M(C₈H₈) = 104)?", "52 000", ["5 200", "104 000", "26 000"], "500 · 104 = 52 000.", S_, ("5 200", "Nol tushib qoldi. 500 · 104 = 52 000.")),
 ]),
]
G = "O'rinbosarlar orientatsiyasi"
slots += [
 S("r-1", G, "choice", 1, [
  C("Qaysi o'rinbosar birinchi tur (orto-, para-yo'naltiruvchi)?", "–CH₃", ["–NO₂", "–COOH", "–SO₃H"], "Alkil guruh elektron beradi va yangi guruhni o- va p- holatga yo'naltiradi.", T, ("–NO₂", "Nitro guruh ikkinchi tur: yangi guruhni meta holatga yo'naltiradi.")),
  C("Qaysi o'rinbosar ikkinchi tur (meta-yo'naltiruvchi)?", "–NO₂", ["–OH", "–CH₃", "–NH₂"], "Elektron tortuvchi guruhlar meta holatga yo'naltiradi.", B, ("–NH₂", "Aminoguruh elektron beradi: o-, p-yo'naltiruvchi.")),
 ]),
 S("r-2", G, "choice", 2, [
  C("Toluolni nitrolaganda asosiy mahsulotlar qaysilar?", "o- va p-nitrotoluol", ["m-nitrotoluol", "Nitrobenzol", "Benzoy kislota"], "CH₃ birinchi tur: yangi guruh orto va para holatga boradi.", T, ("m-nitrotoluol", "Meta holat ikkinchi tur o'rinbosarlar uchun.")),
  C("Nitrobenzolni bromlaganda asosiy mahsulot qaysi?", "m-bromnitrobenzol", ["o-bromnitrobenzol", "p-bromnitrobenzol", "Brombenzol"], "NO₂ ikkinchi tur: yangi guruh meta holatga boradi.", B, ("p-bromnitrobenzol", "Para holat birinchi tur o'rinbosarlar uchun.")),
 ]),
 S("r-3", G, "choice", 2, [
  C("Fenolga ortiqcha bromli suv ta'sir ettirilsa, nima hosil bo'ladi?", "2,4,6-tribromfenol", ["m-bromfenol", "Brombenzol", "Pentabromfenol"], "OH birinchi tur: brom 2, 4, 6 holatlarga boradi (oq cho'kma).", B, ("m-bromfenol", "OH meta holatga yo'naltirmaydi.")),
  C("Benzoy kislotani xlorlaganda asosiy mahsulot qaysi?", "m-xlorbenzoy kislota", ["o-xlorbenzoy kislota", "p-xlorbenzoy kislota", "Benzilxlorid"], "COOH ikkinchi tur, meta-yo'naltiruvchi.", B, ("p-xlorbenzoy kislota", "Para holat birinchi tur o'rinbosarlarga xos.")),
 ]),
 S("r-4", G, "write", 3, [
  W("Toluolni to'liq nitrolang (3 NO₂ guruh, trotil/TNT hosil bo'ladi)", ["C7H8", "HNO3"], ["C7H5N3O6", "H2O"], "C7H8+3HNO3→C7H5N3O6+3H2O", "CH₃ ga nisbatan 2, 4, 6 holatlarga nitro guruhlar birikadi.", T),
  W("Nitrobenzolga brom ta'sir ettiring (FeBr₃, meta holatga)", ["C6H5NO2", "Br2"], ["C6H4BrNO2", "HBr"], "C6H5NO2+Br2→C6H4BrNO2+HBr", "NO₂ meta-yo'naltiruvchi: m-bromnitrobenzol.", B),
 ]),
]
G = "Ko'p halqali arenlar"
slots += [
 S("s-1", G, "choice", 1, [
  C("Naftalinning molekulyar formulasi qaysi?", "C₁₀H₈", ["C₁₂H₁₀", "C₁₄H₁₀", "C₆H₆"], "Ikkita benzol halqasi umumiy bog'ga ega.", None, ("C₁₄H₁₀", "C₁₄H₁₀ antratsen, uch halqali.")),
  C("Naftalin molekulasida nechta benzol halqasi bor?", "2", ["1", "3", "4"], "Ikkita birlashgan (kondensirlangan) halqa.", None, ("3", "Uchta halqa antratsenda.")),
 ]),
 S("s-2", G, "write", 2, [
  W("Naftalinning to'liq yonishini yozing", ["C10H8", "O2"], ["CO2", "H2O"], "C10H8+12O2→10CO2+4H2O", "Kislorod: 20 + 4 = 24 atom, ya'ni 12 O₂.", None),
  W("Naftalinning to'liq gidrogenlanishini yozing (Ni, qizdirish)", ["C10H8", "H2"], ["C10H18"], "C10H8+5H2→C10H18", "Ikkala halqa to'yinadi: dekalin.", None),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H6", "C8H10", "C8H8", "C8H8Br2"]}
cB = {"all": ["C7H8", "C7H7Br", "C7H8O", "C7H6O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (AlCl₃, xloretan bilan)", ["C6H6", "C2H5Cl"], ["C8H10", "HCl"], "C6H6+C2H5Cl→C8H10+HCl", "Etil guruh halqaga birikadi: etilbenzol.", B, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (yorug'likda, yon zanjir)", ["C7H8", "Br2"], ["C7H7Br", "HBr"], "C7H8+Br2→C7H7Br+HBr", "CH₃ guruhidagi vodorod bromga almashinadi: benzilbromid.", T, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (Cr₂O₃, qizdirish)", ["C8H10"], ["C8H8", "H2"], "C8H10→C8H8+H2", "Etilbenzoldan vodorod ajraladi: stirol.", S_, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (NaOH ning suvdagi eritmasi)", ["C7H7Br", "NaOH"], ["C7H8O", "NaBr"], "C7H7Br+NaOH→C7H8O+NaBr", "Brom OH ga almashinadi: benzil spirt.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (CCl₄ da)", ["C8H8", "Br2"], ["C8H8Br2"], "C8H8+Br2→C8H8Br2", "Yon zanjirdagi qo'shbog'ga brom birikadi.", S_, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (CuO, qizdirish)", ["C7H8O", "CuO"], ["C7H6O", "Cu", "H2O"], "C7H8O+CuO→C7H6O+Cu+H2O", "Birlamchi spirt aldegidga oksidlanadi: benzaldegid.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(6, "Arenlar", ["benzol", "toluol", "stirol"], slots)
