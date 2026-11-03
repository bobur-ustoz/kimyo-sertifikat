from lib import *
D, I = ["butadien"], ["izopren"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Etanoldan butadien-1,3 olish reaksiyasini yozing (Lebedev: ZnO + Al₂O₃, 425 °C)", ["C2H5OH"], ["C4H6", "H2", "H2O"], "2C2H5OH→C4H6+H2+2H2O", "Ikki etanol molekulasidan butadien, vodorod va ikki suv hosil bo'ladi.", D),
  W("Izopentenning (C₅H₁₀) degidrogenlanib izopren hosil qilishini yozing", ["C5H10"], ["C5H8", "H2"], "C5H10→C5H8+H2", "Bitta vodorod molekulasi ajralib ikkinchi qo'shbog' hosil bo'ladi.", I),
 ]),
 S("o-2", G, "write", 1, [
  W("Butenning degidrogenlanishini yozing (katalizator, qizdirish)", ["C4H8"], ["C4H6", "H2"], "C4H8→C4H6+H2", "Buten-1 dan vodorod ajralib butadien hosil bo'ladi.", D),
  W("Butanning to'liq degidrogenlanishini yozing (Cr₂O₃, 600 °C)", ["C4H10"], ["C4H6", "H2"], "C4H10→C4H6+2H2", "Ikki molekula vodorod ajraladi va ikkita qo'shbog' hosil bo'ladi.", D),
 ]),
 S("o-3", G, "choice", 2, [
  C("Lebedev usulida butadien qaysi moddadan olinadi?", "Etanol", ["Metan", "Butanol", "Etilen"], "2C₂H₅OH → C₄H₆ + H₂ + 2H₂O.", D, ("Butanol", "Butanoldan butadien emas, buten hosil bo'ladi. Lebedev usuli etanoldan.")),
  C("Lebedev reaksiyasi uchun qanday katalizator ishlatiladi?", "ZnO va Al₂O₃ aralashmasi", ["Ni", "KMnO₄", "H₂SO₄ (konsentrlangan)"], "Spirt degidrogenlanadi va degidratlanadi.", D, ("H₂SO₄ (konsentrlangan)", "Bu katalizator etilen olish uchun, 170 °C da. Lebedev usuli oksidli katalizator.")),
 ]),
 S("o-4", G, "choice", 3, [
  C("92 g etanoldan necha gramm butadien (M = 54) olish mumkin (unum 100%)?", "54 g", ["27 g", "108 g", "46 g"], "92 : 46 = 2 mol etanol; 2C₂H₅OH → 1 C₄H₆, ya'ni 1 mol butadien = 54 g.", D, ("27 g", "27 g yarim mol: bu 1 mol (46 g) etanoldan chiqadi. 92 g esa 2 mol.")),
  C("184 g etanoldan 80% unum bilan necha gramm butadien (M = 54) hosil bo'ladi?", "86,4 g", ["108 g", "43,2 g", "54 g"], "184 : 46 = 4 mol etanol, nazariy 2 mol butadien = 108 g; 80% = 86,4 g.", D, ("108 g", "Bu nazariy massa. Unum 80% bo'lgani uchun amalda kamroq.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Vinilatsetilenni gidrogenlab butadien olishni yozing", ["C4H4", "H2"], ["C4H6"], "C4H4+H2→C4H6", "Uchbog' qo'shbog'ga o'tadi: butadien-1,3.", D),
  W("Vinilatsetilenga HCl ta'sir ettiring (CuCl, xloropren olinadi)", ["C4H4", "HCl"], ["C4H5Cl"], "C4H4+HCl→C4H5Cl", "Xloropren hosil bo'ladi: neopren kauchuk monomeri.", None),
 ]),
 S("x-2", G, "choice", 1, [
  C("Sintetik kauchuk (SK) olinadigan asosiy monomer qaysi?", "Butadien-1,3", ["Etilen", "Propilen", "Atsetilen"], "Butadien polimerlanib sintetik kauchuk beradi.", D),
  C("Tabiiy kauchukning monomeri qaysi?", "Izopren", ["Butadien", "Stirol", "Xloropren"], "Tabiiy kauchuk izoprenning polimeri (2-metilbutadien-1,3).", I, ("Butadien", "Butadien sintetik kauchuk monomeri. Tabiiy kauchukda metil guruh bor: izopren.")),
 ]),
 S("x-3", G, "choice", 2, [
  C("Vinilatsetilenning tuzilishi qaysi?", "CH₂=CH–C≡CH", ["CH₂=CH–CH=CH₂", "CH₃–C≡C–CH₃", "CH≡C–CH₂–CH₃"], "Bir qo'shbog' va bir uchbog' bor.", None, ("CH₂=CH–CH=CH₂", "Bu butadien: ikkita qo'shbog'li, uchbog'siz.")),
  C("Xloropren qaysi moddadan olinadi?", "Vinilatsetilen", ["Butan", "Etilen", "Stirol"], "Vinilatsetilenga HCl birikadi.", None),
 ]),
]
G = "Birikish (H₂, galogenlar)"
slots += [
 S("b-1", G, "write", 1, [
  W("Butadien-1,3 ga 1 mol vodorod ta'sir ettiring (1,2-birikish)", ["C4H6", "H2"], ["C4H8"], "C4H6+H2→C4H8", "Bitta qo'shbog' to'yinadi: buten.", D),
  W("Izoprenga 1 mol vodorod ta'sir ettiring", ["C5H8", "H2"], ["C5H10"], "C5H8+H2→C5H10", "Bitta qo'shbog' to'yinadi.", I),
 ]),
 S("b-2", G, "write", 1, [
  W("Butadien-1,3 ning to'liq gidrogenlanishini yozing (Ni)", ["C4H6", "H2"], ["C4H10"], "C4H6+2H2→C4H10", "Ikkala qo'shbog' to'yinadi: butan.", D),
  W("Izoprenning to'liq gidrogenlanishini yozing (Ni)", ["C5H8", "H2"], ["C5H12"], "C5H8+2H2→C5H12", "Ikkala qo'shbog' to'yinadi: izopentan.", I),
 ]),
 S("b-3", G, "write", 2, [
  W("Butadien-1,3 ga 1 mol xlor ta'sir ettiring", ["C4H6", "Cl2"], ["C4H6Cl2"], "C4H6+Cl2→C4H6Cl2", "Xlor bir qo'shbog'ga (1,2) yoki chetlarga (1,4) birikadi.", D),
  W("Izoprenga 1 mol brom ta'sir ettiring", ["C5H8", "Br2"], ["C5H8Br2"], "C5H8+Br2→C5H8Br2", "Brom dienga 1,2- yoki 1,4-holatda birikadi.", I),
 ]),
 S("b-4", G, "choice", 3, [
  C("Butadien-1,3 ga 1 mol Br₂ ni 1,4-holatda birikishidan qaysi modda hosil bo'ladi?", "1,4-dibrombuten-2", ["3,4-dibrombuten-1", "1,2-dibrombutan", "1,4-dibrombutan"], "Brom chetlarga birikadi va qo'shbog' o'rtaga o'tadi.", D, ("1,4-dibrombutan", "1,4-holatda qo'shbog' yo'qolmaydi, u 2-3 uglerodlar orasiga siljiydi.")),
  C("Butadien-1,3 ga 2 mol Br₂ ortiqcha birikadi. Mahsulot qaysi?", "1,2,3,4-tetrabrombutan", ["1,4-dibrombuten-2", "3,4-dibrombuten-1", "Dibrombutan"], "Ikkala qo'shbog' ham to'liq brom bilan to'yinadi.", D, ("1,4-dibrombuten-2", "Bu 1 mol brom birikkandagi mahsulot.")),
 ]),
]
G = "HX va hipogalogenid"
slots += [
 S("h-1", G, "write", 2, [
  W("Butadien-1,3 ga 1 mol HBr ta'sir ettiring", ["C4H6", "HBr"], ["C4H7Br"], "C4H6+HBr→C4H7Br", "Vodorod va brom bir qo'shbog'ga (yoki 1,4) birikadi.", D),
  W("Izoprenga 1 mol HCl ta'sir ettiring", ["C5H8", "HCl"], ["C5H9Cl"], "C5H8+HCl→C5H9Cl", "Bitta qo'shbog'ga birikish.", I),
 ]),
 S("h-2", G, "write", 2, [
  W("Butadien-1,3 ga 1 mol HOCl ta'sir ettiring", ["C4H6", "HOCl"], ["C4H7ClO"], "C4H6+HOCl→C4H7ClO", "Cl va OH qo'shbog'ga birikadi.", D),
  W("Izoprenga 1 mol HOCl ta'sir ettiring", ["C5H8", "HOCl"], ["C5H9ClO"], "C5H8+HOCl→C5H9ClO", "Cl va OH qo'shbog'ga birikadi.", I),
 ]),
 S("h-3", G, "choice", 2, [
  C("Butadien-1,3 ga HBr 1,4-holatda birikkanda qaysi modda hosil bo'ladi?", "1-brombuten-2", ["3-brombuten-1", "2-brombutan", "1-brombutan"], "H birinchi uglerodga, Br to'rtinchiga birikadi, qo'shbog' o'rtada qoladi.", D, ("3-brombuten-1", "Bu 1,2-birikish mahsuloti: qo'shbog' chetda qoladi.")),
  C("Alkadienlarning umumiy formulasi qaysi?", "CₙH₂ₙ₋₂", ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₆"], "Alkinlar bilan bir xil: ikkita qo'shbog' yoki bitta uchbog'.", D, ("CₙH₂ₙ", "Bu alkenlar formulasi: bitta qo'shbog'.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Butadien-1,3 ning to'liq yonishini yozing", ["C4H6", "O2"], ["CO2", "H2O"], "2C4H6+11O2→8CO2+6H2O", "Kislorod: 16 + 6 = 22 atom, ikki baravarga 11 O₂.", D),
  W("Izoprenning to'liq yonishini yozing", ["C5H8", "O2"], ["CO2", "H2O"], "C5H8+7O2→5CO2+4H2O", "Kislorod: 10 + 4 = 14 atom, ya'ni 7 O₂.", I),
 ]),
 S("k-2", G, "write", 2, [
  W("Butadien-1,3 ning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing", ["C4H6", "KMnO4", "H2O"], ["C4H10O4", "MnO2", "KOH"], "3C4H6+4KMnO4+8H2O→3C4H10O4+4MnO2+4KOH", "Ikkala qo'shbog'ga to'rtta OH birikadi: tetraol.", D),
  W("Izoprenning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing", ["C5H8", "KMnO4", "H2O"], ["C5H12O4", "MnO2", "KOH"], "3C5H8+4KMnO4+8H2O→3C5H12O4+4MnO2+4KOH", "Ikkala qo'shbog' glikol hosil qiladi.", I),
 ]),
 S("k-3", G, "choice", 3, [
  C("1 mol butadien-1,3 to'liq yonishi uchun necha mol O₂ kerak?", "5,5", ["4", "6", "6,5"], "4 CO₂ uchun 4 O₂, 3 H₂O uchun 1,5 O₂: jami 5,5 mol.", D, ("6", "6 mol O₂ butanning yonishiga yaqin: diende vodorod kam.")),
  C("Izopren yonganda hosil bo'lgan CO₂ va H₂O ning mol nisbati qanday?", "5 : 4", ["4 : 5", "5 : 8", "1 : 1"], "C₅H₈ dan 5 CO₂ va 4 H₂O.", I, ("5 : 8", "Vodorod atomlari soni 8, suv esa 4 mol.")),
 ]),
]
G = "Polimerlanish"
slots += [
 S("l-1", G, "choice", 1, [
  C("Butadien-1,3 ning polimerlanishidan nima hosil bo'ladi?", "Sintetik kauchuk (polibutadien)", ["Polietilen", "Kapron", "Neylon"], "Qo'shbog'lar ochilib polimer zanjir hosil qiladi.", D),
  C("Izoprenning polimerlanishidan nima hosil bo'ladi?", "Izopren kauchuk", ["Polistirol", "Polivinilxlorid", "Lavsan"], "Tabiiy kauchukning sun'iy analogi.", I),
 ]),
 S("l-2", G, "choice", 2, [
  C("Butadien va stirolning sopolimerlanishidan qaysi kauchuk hosil bo'ladi?", "Butadien-stirol kauchuk", ["Polistirol", "Neopren", "Nitril kauchuk"], "Ikki xil monomer birlashadi.", D, ("Polistirol", "Polistirol faqat stirolning o'zidan. Bu yerda ikkala monomer ham bor.")),
  C("Butadien va akrilonitrilning sopolimeri qaysi?", "Nitril-butadien kauchuk", ["Butadien-stirol kauchuk", "Neopren", "Polietilen"], "Nitril guruhi moyga chidamlilik beradi.", D, ("Butadien-stirol kauchuk", "Stirol emas, akrilonitril ishtirok etadi.")),
 ]),
 S("l-3", G, "choice", 2, [
  C("Kauchukni vulkanlash uchun nima qo'shiladi?", "Oltingugurt", ["Kislorod", "Xlor", "Azot"], "Oltingugurt zanjirlarni ko'ndalang bog'lab \"tikadi\".", None),
  C("Vulkanlashdan keyin kauchuk qanday xossaga ega bo'ladi?", "Mustahkam va elastik rezinaga aylanadi", ["Eruvchan bo'ladi", "Qattiq plastmassaga o'tadi", "Suyuqlanib ketadi"], "Zanjirlar orasida ko'ndalang bog'lar hosil bo'ladi.", None),
 ]),
 S("l-4", G, "choice", 3, [
  C("Molyar massasi 162 000 g/mol bo'lgan polibutadienning polimerlanish darajasi qancha (M(C₄H₆) = 54)?", "3000", ["30 000", "1500", "6000"], "162 000 : 54 = 3000.", D, ("30 000", "Nol xatosi. 162 000 : 54 = 3000.")),
  C("Izopren kauchukning polimerlanish darajasi 1500 bo'lsa, molyar massasi qancha (M(C₅H₈) = 68)?", "102 000", ["10 200", "204 000", "68 000"], "1500 · 68 = 102 000.", I, ("10 200", "Nol tushib qoldi. 1500 · 68 = 102 000.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C4H10O2", "C4H6", "C4H6Br2", "C4H6"]}
cB = {"all": ["C5H12", "C5H8", "C5H8Cl2", "C5H8"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (Al₂O₃, qizdirish, butandiol-1,3 degidratlanadi)", ["C4H10O2"], ["C4H6", "H2O"], "C4H10O2→C4H6+2H2O", "Ikkala OH suv holida ajraladi: butadien.", D, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Cr₂O₃, qizdirish)", ["C5H12"], ["C5H8", "H2"], "C5H12→C5H8+2H2", "Ikki molekula vodorod ajralib izopren hosil bo'ladi.", I, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (1,4-birikish)", ["C4H6", "Br2"], ["C4H6Br2"], "C4H6+Br2→C4H6Br2", "Brom 1,4-holatda birikadi: 1,4-dibrombuten-2.", D, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing", ["C5H8", "Cl2"], ["C5H8Cl2"], "C5H8+Cl2→C5H8Cl2", "Xlor dienga birikadi.", I, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (rux)", ["C4H6Br2", "Zn"], ["C4H6", "ZnBr2"], "C4H6Br2+Zn→C4H6+ZnBr2", "Rux ikkala bromni olib, diyenni qayta tiklaydi.", D, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (rux)", ["C5H8Cl2", "Zn"], ["C5H8", "ZnCl2"], "C5H8Cl2+Zn→C5H8+ZnCl2", "Rux xlorni olib dienni qayta hosil qiladi.", I, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(5, "Alkadienlar", ["butadien", "izopren"], slots)
