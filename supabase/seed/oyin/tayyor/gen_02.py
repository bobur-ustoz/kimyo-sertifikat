from lib import *
sp, sb, sc, sg = ["siklopropan"], ["siklobutan"], ["siklopentan"], ["siklogeksan"]
slots = []
G = "Tuzilish"
slots += [
 S("t-1", G, "choice", 1, [
  C("Siklobutanning molekulyar formulasi qaysi?", "C₄H₈", ["C₄H₁₀", "C₄H₆", "C₃H₆"], "To'rt uglerodli halqa: CₙH₂ₙ da n = 4.", sb, ("C₄H₁₀", "C₄H₁₀ butan (alkan). Halqa ikkita vodorodni kamaytiradi.")),
  C("Siklopentanning molekulyar formulasi qaysi?", "C₅H₁₀", ["C₅H₁₂", "C₅H₈", "C₆H₁₀"], "Besh uglerodli halqa: CₙH₂ₙ da n = 5.", sc, ("C₅H₁₂", "C₅H₁₂ pentan (alkan) formulasi.")),
 ]),
 S("t-2", G, "choice", 1, [
  C("Qaysi siklalkan eng zo'riqqan va faol?", "Siklopropan", ["Siklobutan", "Siklopentan", "Siklogeksan"], "Uch a'zoli halqada bog' burchagi 60° (normal 109°).", sp, ("Siklobutan", "Siklobutan ham zo'riqqan, lekin siklopropan eng kuchli zo'riqqan.")),
  C("Qaysi siklalkan eng barqaror (zo'riqishsiz, kreslo shakli)?", "Siklogeksan", ["Siklopropan", "Siklobutan", "Siklopentan"], "Olti a'zoli halqa burchaklari deyarli normal.", sg, ("Siklopropan", "Siklopropan eng kam barqaror.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("1,3-dibrompropanga rux ta'sir ettiring", ["C3H6Br2", "Zn"], ["C3H6", "ZnBr2"], "C3H6Br2+Zn→C3H6+ZnBr2", "Chetki uglerodlar bog'lanib uch a'zoli halqa hosil qiladi.", sp),
  W("1,4-dibrombutanga rux ta'sir ettiring", ["C4H8Br2", "Zn"], ["C4H8", "ZnBr2"], "C4H8Br2+Zn→C4H8+ZnBr2", "To'rt uglerod halqaga yopiladi: siklobutan.", sb),
 ]),
 S("o-2", G, "write", 2, [
  W("1,4-dibrombutanga natriy ta'sir ettiring (ichki Vyurs)", ["C4H8Br2", "Na"], ["C4H8", "NaBr"], "C4H8Br2+2Na→C4H8+2NaBr", "Natriy ikkala bromni oladi, uchlar bog'lanadi.", sb),
  W("1,5-dibrompentanga natriy ta'sir ettiring (ichki Vyurs)", ["C5H10Br2", "Na"], ["C5H10", "NaBr"], "C5H10Br2+2Na→C5H10+2NaBr", "Besh a'zoli halqa hosil bo'ladi.", sc),
 ]),
 S("o-3", G, "write", 2, [
  W("Geksanning degidrosiklanishini yozing (Pt, qizdirish)", ["C6H14"], ["C6H12", "H2"], "C6H14→C6H12+H2", "Zanjir uchlari bog'lanib halqa yopiladi.", sg),
  W("Pentanning degidrosiklanishini yozing (Pt, qizdirish)", ["C5H12"], ["C5H10", "H2"], "C5H12→C5H10+H2", "Besh a'zoli halqa hosil bo'ladi.", sc),
 ]),
 S("o-4", G, "choice", 2, [
  C("1,3-dibrompropanga rux ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "Siklopropan", ["Propen", "Propan", "Propin"], "Chetki bromlar olinib uglerodlar halqaga bog'lanadi.", sp, ("Propen", "Propen 1,2-dibrompropandan hosil bo'ladi.")),
  C("1,4-dibrombutanga rux ta'sir ettirilsa, qaysi modda hosil bo'ladi?", "Siklobutan", ["Butan", "Buten", "Butadien"], "To'rt uglerod halqaga yopiladi.", sb, ("Butan", "Rux vodorod qo'shmaydi: faqat galogenni oladi.")),
 ]),
 S("o-5", G, "choice", 1, [
  C("Dihalogenalkandan siklalkan olishda qaysi metall ishlatiladi?", "Rux", ["Kaliy", "Kalsiy", "Alyuminiy"], "Rux ikkita galogenni olib halqa hosil bo'lishiga imkon beradi.", None),
  C("Benzolni to'liq gidrogenlasak, qaysi siklalkan hosil bo'ladi?", "Siklogeksan", ["Siklopentan", "Siklobutan", "Siklopropan"], "Olti uglerodli halqa saqlanadi: C₆H₆ + 3H₂ → C₆H₁₂.", sg, ("Siklopentan", "Uglerod soni o'zgarmaydi: oltita.")),
 ]),
]
G = "Galogenlarning ta'siri"
slots += [
 S("g-1", G, "write", 1, [
  W("Siklopropanga brom ta'sir ettiring (halqa ochiladi)", ["C3H6", "Br2"], ["C3H6Br2"], "C3H6+Br2→C3H6Br2", "Halqa uziladi: 1,3-dibrompropan.", sp),
  W("Siklopropanga xlor ta'sir ettiring (halqa ochiladi)", ["C3H6", "Cl2"], ["C3H6Cl2"], "C3H6+Cl2→C3H6Cl2", "Halqa uziladi: 1,3-dixlorpropan.", sp),
 ]),
 S("g-2", G, "write", 2, [
  W("Siklopentanga xlor yorug'likda ta'sir ettiring (bitta vodorod almashinadi)", ["C5H10", "Cl2"], ["C5H9Cl", "HCl"], "C5H10+Cl2→C5H9Cl+HCl", "Zo'riqmagan halqa alkanga o'xshab o'rin olish reaksiyasiga kirishadi.", sc),
  W("Siklogeksanga brom yorug'likda ta'sir ettiring (bitta vodorod almashinadi)", ["C6H12", "Br2"], ["C6H11Br", "HBr"], "C6H12+Br2→C6H11Br+HBr", "Halqa saqlanadi, vodorod bromga almashinadi.", sg),
 ]),
 S("g-3", G, "choice", 2, [
  C("Brom bilan oddiy sharoitda qaysi siklalkanda halqa ochiladi?", "Siklopropan", ["Siklopentan", "Siklogeksan", "Metan"], "Faqat zo'riqqan uch a'zoli halqa birikish bilan ochiladi.", sp, ("Siklogeksan", "Siklogeksan alkanga o'xshaydi: faqat o'rin olish.")),
  C("Siklopentan xlor bilan yorug'likda qanday reaksiyaga kirishadi?", "O'rin olish", ["Birikish (halqa ochiladi)", "Polimerlanish", "Reaksiyaga kirishmaydi"], "Beshlik halqa zo'riqmagan.", sc, ("Birikish (halqa ochiladi)", "Bu faqat siklopropanga xos.")),
 ]),
 S("g-4", G, "choice", 3, [
  C("8,4 g siklopropanga (M = 42) ortiqcha xlor ta'sir ettirilsa, necha gramm 1,3-dixlorpropan (M = 113) hosil bo'ladi?", "22,6 g", ["11,3 g", "45,2 g", "16,8 g"], "8,4 : 42 = 0,2 mol; 1 : 1 nisbatda 0,2 · 113 = 22,6 g.", sp, ("11,3 g", "11,3 g 0,1 mol mahsulotga to'g'ri keladi: bu 4,2 g siklopropandan.")),
  C("4,2 g siklopropanga HBr ta'sir ettirilsa, necha gramm 1-brompropan (M = 123) hosil bo'ladi?", "12,3 g", ["6,15 g", "24,6 g", "4,2 g"], "4,2 : 42 = 0,1 mol; 1 : 1 nisbatda 0,1 · 123 = 12,3 g.", sp, ("24,6 g", "24,6 g 0,2 mol uchun, ya'ni 8,4 g siklopropandan.")),
 ]),
]
G = "HX ning ta'siri"
slots += [
 S("h-1", G, "write", 1, [
  W("Siklopropanga HCl ta'sir ettiring (halqa ochiladi)", ["C3H6", "HCl"], ["C3H7Cl"], "C3H6+HCl→C3H7Cl", "Halqa uziladi: 1-xlorpropan.", sp),
  W("Siklopropanga HI ta'sir ettiring (halqa ochiladi)", ["C3H6", "HI"], ["C3H7I"], "C3H6+HI→C3H7I", "Halqa uziladi: 1-yodpropan.", sp),
 ]),
 S("h-2", G, "choice", 2, [
  C("Qaysi siklalkan HBr bilan oddiy sharoitda reaksiyaga kirishadi?", "Siklopropan", ["Siklopentan", "Siklogeksan", "Siklogeptan"], "Uch a'zoli halqa zo'riqqan va ochiladi.", sp, ("Siklopentan", "Beshlik va olti a'zoli halqalar HBr bilan reaksiyaga kirishmaydi.")),
  C("Siklopropan HBr bilan reaksiyaga kirishsa, qaysi modda hosil bo'ladi?", "1-brompropan", ["2-brompropan", "1,3-dibrompropan", "Brombenzol"], "Halqa uziladi, uchlariga H va Br birikadi.", sp, ("1,3-dibrompropan", "Dibromid Br₂ dan hosil bo'ladi.")),
 ]),
 S("h-3", G, "choice", 3, [
  C("Siklopropanga HBr, so'ng natriy (Vyurs) ta'sir ettirilsa, qaysi alkan hosil bo'ladi?", "Geksan", ["Propan", "Butan", "Pentan"], "1-brompropan Vyursda uglerod sonini ikki baravar oshiradi.", sp, ("Propan", "Vyursda zanjir uzayadi, propan hosil bo'lmaydi.")),
  C("Siklopropanga HI, so'ng natriy ta'sir ettirilsa, oxirgi alkanning molyar massasi qancha?", "86 g/mol", ["44 g/mol", "58 g/mol", "72 g/mol"], "Oxirgi modda geksan C₆H₁₄: 6 · 12 + 14 = 86.", sp, ("44 g/mol", "44 propanning massasi: Vyursda esa geksan hosil bo'ladi.")),
 ]),
]
G = "Gidrogenlash"
slots += [
 S("r-1", G, "write", 2, [
  W("Siklopropanning gidrogenlanishini yozing (Ni, ~80 °C)", ["C3H6", "H2"], ["C3H8"], "C3H6+H2→C3H8", "Uch a'zoli halqa uziladi: propan.", sp),
  W("Siklobutanning gidrogenlanishini yozing (Ni, ~120 °C)", ["C4H8", "H2"], ["C4H10"], "C4H8+H2→C4H10", "To'rt a'zoli halqa uziladi: butan.", sb),
 ]),
 S("r-2", G, "write", 2, [
  W("Siklopentanning gidrogenlanishini yozing (Ni, ~300 °C)", ["C5H10", "H2"], ["C5H12"], "C5H10+H2→C5H12", "Zo'riqmagan halqani ochish uchun qattiq sharoit kerak.", sc),
  W("Siklogeksanning degidrogenlanishini yozing (Pt, 300 °C)", ["C6H12"], ["C6H6", "H2"], "C6H12→C6H6+3H2", "Aromatik halqa hosil bo'ladi.", sg),
 ]),
 S("r-3", G, "choice", 2, [
  C("Siklopropanning gidrogenlash sharoiti qanday?", "Yumshoq (~80 °C)", ["Qattiq (~300 °C)", "Reaksiya bormaydi", "Faqat yorug'likda"], "Zo'riqqan halqa tez ochiladi.", sp, ("Qattiq (~300 °C)", "Qattiq sharoit siklopentan uchun.")),
  C("Siklogeksanni Pt ustida 300 °C da qizdirilsa, qaysi modda hosil bo'ladi?", "Benzol", ["Geksan", "Geksen", "Toluol"], "Degidrogenlashda 3 molekula vodorod ajraladi.", sg, ("Geksan", "Geksan hosil bo'lishi uchun vodorod birikishi kerak edi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Siklopropanning to'liq yonishini yozing", ["C3H6", "O2"], ["CO2", "H2O"], "2C3H6+9O2→6CO2+6H2O", "Kasr chiqmasligi uchun ikki baravar.", sp),
  W("Siklobutanning to'liq yonishini yozing", ["C4H8", "O2"], ["CO2", "H2O"], "C4H8+6O2→4CO2+4H2O", "Kislorod: 8 + 4 = 12 atom, ya'ni 6 O₂.", sb),
 ]),
 S("k-2", G, "write", 2, [
  W("Siklopentanning to'liq yonishini yozing", ["C5H10", "O2"], ["CO2", "H2O"], "2C5H10+15O2→10CO2+10H2O", "Kasr chiqmasligi uchun ikki baravar.", sc),
  W("Siklogeksanning to'liq yonishini yozing", ["C6H12", "O2"], ["CO2", "H2O"], "C6H12+9O2→6CO2+6H2O", "Kislorod: 12 + 6 = 18 atom, ya'ni 9 O₂.", sg),
 ]),
 S("k-3", G, "write", 2, [
  W("Siklogeksanni havo kislorodi bilan siklogeksanolgacha oksidlang (katalizator)", ["C6H12", "O2"], ["C6H12O"], "2C6H12+O2→2C6H12O", "Bitta vodorod OH guruhiga o'tadi.", sg),
  W("Siklogeksanni siklogeksanongacha oksidlang (katalizator)", ["C6H12", "O2"], ["C6H10O", "H2O"], "C6H12+O2→C6H10O+H2O", "Ketongacha oksidlanadi, suv ajraladi.", sg),
 ]),
 S("k-4", G, "choice", 3, [
  C("1 mol siklogeksan to'liq yonishiga necha mol O₂ kerak?", "9", ["6", "8", "10"], "6 CO₂ uchun 6 O₂, 6 H₂O uchun yana 3 O₂.", sg, ("6", "6 faqat CO₂ dagi kislorod. Suvdagisi ham kerak.")),
  C("Siklopropan va propen yonganda hosil bo'lgan CO₂ va H₂O ning mol nisbati qanday?", "1 : 1", ["3 : 4", "1 : 2", "2 : 1"], "Ikkalasi ham C₃H₆: 3 CO₂ va 3 H₂O.", sp, ("3 : 4", "3 : 4 propan (C₃H₈) uchun.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C3H6Br2", "C3H6", "C3H7Br", "C6H14"]}
cB = {"all": ["C6H6", "C6H12", "C6H11Cl", "C12H22"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (natriy)", ["C3H6Br2", "Na"], ["C3H6", "NaBr"], "C3H6Br2+2Na→C3H6+2NaBr", "Uch a'zoli halqa hosil bo'ladi.", sp, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Ni, qizdirish)", ["C6H6", "H2"], ["C6H12"], "C6H6+3H2→C6H12", "Benzolga uch molekula vodorod birikadi.", sg, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (HBr, halqa ochiladi)", ["C3H6", "HBr"], ["C3H7Br"], "C3H6+HBr→C3H7Br", "1-brompropan hosil bo'ladi.", sp, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (yorug'likda)", ["C6H12", "Cl2"], ["C6H11Cl", "HCl"], "C6H12+Cl2→C6H11Cl+HCl", "Siklogeksandagi vodorod xlorga almashinadi.", sg, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (Vyurs)", ["C3H7Br", "Na"], ["C6H14", "NaBr"], "2C3H7Br+2Na→C6H14+2NaBr", "Ikki propil radikal birlashadi: geksan.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Vyurs)", ["C6H11Cl", "Na"], ["C12H22", "NaCl"], "2C6H11Cl+2Na→C12H22+2NaCl", "Ikki siklogeksil radikal birlashadi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(2, "Sikloalkanlar", ["siklopropan", "siklobutan", "siklopentan", "siklogeksan"], slots)
