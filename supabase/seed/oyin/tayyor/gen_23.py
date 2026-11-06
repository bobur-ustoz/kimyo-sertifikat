from lib import *
Ed, Gm, Fe = ["etilendiamin"], ["geksametilendiamin"], ["fenilendiamin"]
slots = []
G = "Nomlanish"
slots += [
 S("n-1", G, "choice", 1, [
  C("Etilendiaminning tuzilish formulasi qaysi?", "H₂N–CH₂–CH₂–NH₂", ["CH₃–CH(NH₂)₂", "H₂N–CH₂–NH₂", "H₂N–(CH₂)₃–NH₂"], "Ikki uglerodli zanjirning har uchida NH₂.", Ed, ("CH₃–CH(NH₂)₂", "Bitta uglerodda ikki NH₂ guruhi (gem-diamin) beqaror.")),
  C("Geksametilendiaminning tuzilish formulasi qaysi?", "H₂N–(CH₂)₆–NH₂", ["H₂N–(CH₂)₄–NH₂", "H₂N–(CH₂)₅–NH₂", "H₂N–(CH₂)₈–NH₂"], "Olti uglerodli zanjir.", Gm, ("H₂N–(CH₂)₅–NH₂", "Besh uglerodli: kadaverin (pentametilendiamin).")),
 ]),
 S("n-2", G, "choice", 2, [
  C("To'yingan diaminlarning umumiy formulasi qaysi?", "CₙH₂ₙ₊₄N₂", ["CₙH₂ₙ₊₃N", "CₙH₂ₙ₊₂N₂", "CₙH₂ₙ₊₂N"], "Alkan (CₙH₂ₙ₊₂) da ikki vodorod NH₂ ga almashgan: CₙH₂ₙ(NH₂)₂.", Ed, ("CₙH₂ₙ₊₂N₂", "NH₂ guruhlari ikki vodorodni emas, ikkita NH₂ ni qo'shadi: vodorod soni 2n + 4.")),
  C("Putressin (tetrametilendiamin) formulasi qaysi?", "C₄H₁₂N₂", ["C₄H₁₀N₂", "C₅H₁₄N₂", "C₄H₁₁N"], "H₂N–(CH₂)₄–NH₂: C₄H₁₂N₂.", Ed, ("C₅H₁₄N₂", "Bu kadaverin (pentametilendiamin).")),
 ]),
 S("n-3", G, "choice", 3, [
  C("Kadaverin nima?", "Pentametilendiamin (oqsil chirishida hosil bo'ladi)", ["Geksametilendiamin", "Etilendiamin", "Putressin"], "H₂N–(CH₂)₅–NH₂: o'tkir hidli modda.", Ed, ("Putressin", "Putressin to'rt uglerodli diamin.")),
  C("C₆H₁₆N₂ formulali to'g'ri zanjirli diaminning nomi qaysi?", "Geksametilendiamin", ["Pentametilendiamin", "Etilendiamin", "Butandiamin"], "Olti uglerodli zanjir, ikki chetda NH₂.", Gm, ("Pentametilendiamin", "Pentametilendiaminda 5 uglerod: C₅H₁₄N₂.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 2, [
  W("1,2-dixloretanga ortiqcha ammiak ta'sir ettiring", ["C2H4Cl2", "NH3"], ["C2H8N2", "NH4Cl"], "C2H4Cl2+4NH3→C2H8N2+2NH4Cl", "Ikki xlor aminoguruhga almashinadi, ammiak HCl ni biriktiradi.", Ed),
  W("1,6-dibromgeksanga ortiqcha ammiak ta'sir ettiring", ["C6H12Br2", "NH3"], ["C6H16N2", "NH4Br"], "C6H12Br2+4NH3→C6H16N2+2NH4Br", "Geksametilendiamin va ammoniy bromid hosil bo'ladi.", Gm),
 ]),
 S("o-2", G, "write", 2, [
  W("Suksinonitrilni vodorod bilan qaytaring (Ni, bosim): putressin", ["C4H4N2", "H2"], ["C4H12N2"], "C4H4N2+4H2→C4H12N2", "Ikkala nitril guruhi CH₂NH₂ ga qaytariladi.", None),
  W("Glutaronitrilni vodorod bilan qaytaring (Ni, bosim): kadaverin", ["C5H6N2", "H2"], ["C5H14N2"], "C5H6N2+4H2→C5H14N2", "Pentametilendiamin hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("p-dinitrobenzolni vodorod bilan qaytaring", ["C6H4N2O4", "H2"], ["C6H8N2", "H2O"], "C6H4N2O4+6H2→C6H8N2+4H2O", "Ikkala nitro guruh aminoguruhga qaytariladi: p-fenilendiamin.", Fe),
  W("p-nitroanilinni vodorod bilan qaytaring", ["C6H6N2O2", "H2"], ["C6H8N2", "H2O"], "C6H6N2O2+3H2→C6H8N2+2H2O", "Qolgan nitro guruh ham qaytariladi.", Fe),
 ]),
 S("o-4", G, "write", 3, [
  W("Adipin kislotaga ortiqcha ammiak ta'sir ettiring (qizdirish): adiponitril", ["C6H10O4", "NH3"], ["C6H8N2", "H2O"], "C6H10O4+2NH3→C6H8N2+4H2O", "Karboksil guruhlari nitrilga aylanadi: neylon sintezining oraliq mahsuloti.", Gm),
  W("Qahrabo kislotaga ortiqcha ammiak ta'sir ettiring (qizdirish): suksinonitril", ["C4H6O4", "NH3"], ["C4H4N2", "H2O"], "C4H6O4+2NH3→C4H4N2+4H2O", "Ikkala COOH nitrilga aylanadi.", None),
 ]),
]
G = "Asoslik va tuz hosil qilish"
slots += [
 S("t-1", G, "write", 1, [
  W("Etilendiaminga ortiqcha xlorid kislota ta'sir ettiring", ["C2H8N2", "HCl"], ["C2H10Cl2N2"], "C2H8N2+2HCl→C2H10Cl2N2", "Ikkala aminoguruh proton biriktiradi.", Ed),
  W("Geksametilendiaminga ortiqcha xlorid kislota ta'sir ettiring", ["C6H16N2", "HCl"], ["C6H18Cl2N2"], "C6H16N2+2HCl→C6H18Cl2N2", "Dixlorid tuzi hosil bo'ladi.", Gm),
 ]),
 S("t-2", G, "write", 1, [
  W("Etilendiaminga 1 mol xlorid kislota ta'sir ettiring", ["C2H8N2", "HCl"], ["C2H9ClN2"], "C2H8N2+HCl→C2H9ClN2", "Faqat bitta aminoguruh protonlanadi.", Ed),
  W("Putressinga sulfat kislota ta'sir ettiring", ["C4H12N2", "H2SO4"], ["C4H14N2O4S"], "C4H12N2+H2SO4→C4H14N2O4S", "Putressin sulfat hosil bo'ladi.", None),
 ]),
 S("t-3", G, "write", 2, [
  W("Etilendiamin dixloridiga ortiqcha NaOH ta'sir ettiring", ["C2H10Cl2N2", "NaOH"], ["C2H8N2", "NaCl", "H2O"], "C2H10Cl2N2+2NaOH→C2H8N2+2NaCl+2H2O", "Erkin diamin ajraladi.", Ed),
  W("Geksametilendiamin dixloridiga ortiqcha NaOH ta'sir ettiring", ["C6H18Cl2N2", "NaOH"], ["C6H16N2", "NaCl", "H2O"], "C6H18Cl2N2+2NaOH→C6H16N2+2NaCl+2H2O", "Diamin ozod bo'ladi.", Gm),
 ]),
 S("t-4", G, "choice", 2, [
  C("Etilendiamin molekulasida nechta asos markazi bor?", "Ikkita", ["Bitta", "Hech biri", "Uchta"], "Har bir azot atomida erkin elektron juft bor.", Ed, ("Bitta", "Ikkita NH₂ guruhi: ikki asos markazi.")),
  C("Geksametilendiamin va p-fenilendiamindan qaysi biri kuchliroq asos?", "Geksametilendiamin", ["Fenilendiamin", "Teng", "Ikkalasi neytral"], "Alifatik aminlar aromatik aminlardan kuchliroq asos.", Gm + Fe, ("Fenilendiamin", "Aromatik halqa azotning elektron juftini tortib, asoslikni pasaytiradi.")),
 ]),
]
G = "Atsillash va alkillash"
slots += [
 S("a-1", G, "write", 2, [
  W("Etilendiaminga ortiqcha atsetilxlorid ta'sir ettiring", ["C2H8N2", "C2H3ClO"], ["C6H12N2O2", "HCl"], "C2H8N2+2C2H3ClO→C6H12N2O2+2HCl", "Ikkala aminoguruh atsillanadi: diamid.", Ed),
  W("Geksametilendiaminga ortiqcha sirka angidrid ta'sir ettiring", ["C6H16N2", "C4H6O3"], ["C10H20N2O2", "C2H4O2"], "C6H16N2+2C4H6O3→C10H20N2O2+2C2H4O2", "Ikkala aminoguruh atsillanadi.", Gm),
 ]),
 S("a-2", G, "write", 2, [
  W("Etilendiaminga ortiqcha yodmetan ta'sir ettiring (bitta vodorodga ikkita guruh)", ["C2H8N2", "CH3I"], ["C4H12N2", "HI"], "C2H8N2+2CH3I→C4H12N2+2HI", "Har azot atomida bitta vodorod metilga almashinadi.", Ed),
  W("Geksametilendiaminga bromoetan ta'sir ettiring (2 mol)", ["C6H16N2", "C2H5Br"], ["C10H24N2", "HBr"], "C6H16N2+2C2H5Br→C10H24N2+2HBr", "Ikkala azotda alkillash.", Gm),
 ]),
 S("a-3", G, "write", 3, [
  W("Etilendiaminga ikki mol sirka aldegid ta'sir ettiring (Shiff asosi)", ["C2H8N2", "C2H4O"], ["C6H12N2", "H2O"], "C2H8N2+2C2H4O→C6H12N2+2H2O", "Aminoguruh karbonil bilan reaksiyaga kirib suv ajratadi.", Ed),
  W("Etilendiaminga ikki mol benzaldegid ta'sir ettiring (Shiff asosi)", ["C2H8N2", "C7H6O"], ["C16H16N2", "H2O"], "C2H8N2+2C7H6O→C16H16N2+2H2O", "Diimin hosil bo'ladi.", Ed),
 ]),
]
G = "Nitrit kislota ta'siri"
slots += [
 S("h-1", G, "write", 2, [
  W("Etilendiaminga ortiqcha nitrit kislota ta'sir ettiring", ["C2H8N2", "HNO2"], ["C2H6O2", "N2", "H2O"], "C2H8N2+2HNO2→C2H6O2+2N2+2H2O", "Ikkala aminoguruh OH ga almashinadi: etilenglikol.", Ed),
  W("Putressinga ortiqcha nitrit kislota ta'sir ettiring", ["C4H12N2", "HNO2"], ["C4H10O2", "N2", "H2O"], "C4H12N2+2HNO2→C4H10O2+2N2+2H2O", "Butandiol hosil bo'ladi, azot ajraladi.", None),
 ]),
 S("h-2", G, "choice", 2, [
  C("Etilendiaminga ortiqcha HNO₂ ta'sir etganda qaysi moddalar hosil bo'ladi?", "Etilenglikol va N₂", ["Etanol va N₂", "Diazoniy tuzi", "Nitroetan"], "Ikkala NH₂ OH ga almashinadi.", Ed, ("Etanol va N₂", "Ikki aminoguruh ikki OH ga o'tadi: ikki atomli spirt.")),
  C("p-fenilendiaminga HNO₂ (0–5 °C, HCl) ta'sir etganda nima hosil bo'ladi?", "Bis-diazoniy tuzi", ["Fenol va N₂", "Nitrozoamin", "Spirt"], "Past haroratda aromatik aminlar diazoniy tuzi beradi.", Fe, ("Fenol va N₂", "Fenol faqat qizdirilganda hosil bo'ladi.")),
 ]),
]
G = "Poliamidlar (neylon)"
slots += [
 S("p-1", G, "choice", 1, [
  C("Geksametilendiamin va adipin kislotaning polikondensatsiyasidan qaysi polimer hosil bo'ladi?", "Neylon (poliamid 6,6)", ["Kapron", "Lavsan", "Polietilen"], "Amid bog'i orqali bog'langan zanjir.", Gm, ("Kapron", "Kapron bitta monomerdan (kaprolaktam) olinadi.")),
  C("Neylon olish reaksiyasi qanday turga kiradi?", "Polikondensatsiya", ["Polimerlanish", "Gidroliz", "Oksidlanish"], "Har bir bog' hosil bo'lishida past molekulyar modda (suv) ajraladi.", Gm, ("Polimerlanish", "Polimerlanishda hech narsa ajralmaydi, polikondensatsiyada suv ajraladi.")),
 ]),
 S("p-2", G, "write", 3, [
  W("Geksametilendiamin va adipin kislotaning birinchi bosqich reaksiyasini yozing (amid hosil bo'lishi)", ["C6H16N2", "C6H10O4"], ["C12H24N2O3", "H2O"], "C6H16N2+C6H10O4→C12H24N2O3+H2O", "Bitta amid bog'i hosil bo'ladi, suv ajraladi.", Gm),
  W("Etilendiamin va oksalat kislotaning birinchi bosqich reaksiyasini yozing", ["C2H8N2", "C2H2O4"], ["C4H8N2O3", "H2O"], "C2H8N2+C2H2O4→C4H8N2O3+H2O", "Amid bog'i hosil bo'ladi.", Ed),
 ]),
 S("p-3", G, "choice", 3, [
  C("Neylon 6,6 sintezida monomerlar qanday mol nisbatda olinadi?", "1 : 1", ["1 : 2", "2 : 1", "1 : 3"], "Diamin va dikarbon kislota bir xil miqdorda: zanjir ikki uchi ham funksional.", Gm, ("2 : 1", "Nisbat 1 : 1, aks holda zanjir qisqa qoladi.")),
  C("Neylon hosil bo'lishida har bir amid bog'i bilan qaysi modda ajraladi?", "Suv", ["CO₂", "NH₃", "H₂"], "–COOH + H₂N– → –CONH– + H₂O.", Gm, ("NH₃", "Ammiak ajralmaydi: u amid tarkibida qoladi.")),
 ]),
]
G = "Yonish va qo'llanilishi"
slots += [
 S("k-1", G, "write", 2, [
  W("Etilendiaminning to'liq yonishini yozing (azot erkin holda ajraladi)", ["C2H8N2", "O2"], ["CO2", "H2O", "N2"], "C2H8N2+4O2→2CO2+4H2O+N2", "Azot atomlari N₂ ga birikadi.", Ed),
  W("Geksametilendiaminning to'liq yonishini yozing (azot erkin holda ajraladi)", ["C6H16N2", "O2"], ["CO2", "H2O", "N2"], "C6H16N2+10O2→6CO2+8H2O+N2", "Kislorod: 12 + 8 = 20 atom, ya'ni 10 O₂.", Gm),
 ]),
 S("k-2", G, "choice", 2, [
  C("Etilendiamin qayerda ishlatiladi?", "EDTA va polimerlar sintezida", ["Yoqilg'i sifatida", "Oziq-ovqat bo'yog'i sifatida", "Antifriz sifatida"], "Kompleks hosil qiluvchi EDTA ning xomashyosi.", Ed),
  C("Putressin va kadaverin qayerda hosil bo'ladi?", "Oqsillar chiriganda", ["Kraxmal bijg'ishida", "Yog' gidrolizida", "Fotosintezda"], "Aminokislotalar dekarboksillanishidan: o'tkir hidli \"murda zahari\".", None, ("Yog' gidrolizida", "Yog' gidrolizidan glitserin va kislotalar chiqadi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4", "C2H4Br2", "C2H8N2", "C6H16N2O4"]}
cB = {"all": ["C6H10O4", "C6H16N2O4", "C6H8N2", "C6H16N2"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing", ["C2H4", "Br2"], ["C2H4Br2"], "C2H4+Br2→C2H4Br2", "Brom qo'shbog'ga birikadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (ammiak bilan tuz)", ["C6H10O4", "NH3"], ["C6H16N2O4"], "C6H10O4+2NH3→C6H16N2O4", "Adipin kislota ammiak bilan diammoniy adipinat hosil qiladi.", Gm, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (ortiqcha ammiak)", ["C2H4Br2", "NH3"], ["C2H8N2", "NH4Br"], "C2H4Br2+4NH3→C2H8N2+2NH4Br", "Ikkala brom aminoguruhga almashinadi.", Ed, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (qizdirish, katalizator)", ["C6H16N2O4"], ["C6H8N2", "H2O"], "C6H16N2O4→C6H8N2+4H2O", "Ammoniy tuzi degidratlanib dinitril beradi.", Gm, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (sirka kislota)", ["C2H8N2", "C2H4O2"], ["C6H16N2O4"], "C2H8N2+2C2H4O2→C6H16N2O4", "Diamin ikki molekula sirka kislota bilan tuz hosil qiladi.", Ed, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Ni, bosim)", ["C6H8N2", "H2"], ["C6H16N2"], "C6H8N2+4H2→C6H16N2", "Adiponitril geksametilendiaminga qaytariladi.", Gm, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(23, "Diaminlar", ["etilendiamin", "geksametilendiamin", "fenilendiamin"], slots)
