import json
def C(p, ok, no, w, uses=None, trap=None):
    v = {"p": p, "ok": ok, "no": no, "w": w}
    if uses: v["uses"] = uses
    if trap: v["trap"] = {"opt": trap[0], "why": trap[1]}
    return v
def W(p, re, pr, ans, w, uses=None, chain=None, bundle=None):
    v = {"p": p, "re": re, "pr": pr, "ans": ans, "w": w}
    if chain: v["chain"] = chain
    if bundle: v["bundle"] = bundle
    if uses: v["uses"] = uses
    return v
S = lambda slot, group, type, lvl, variants, bg=None: {"slot": slot, "group": group, "type": type, "lvl": lvl, **({"bundleGroup": bg} if bg else {}), "variants": variants}
sp, sb, sc, sg = ["siklopropan"], ["siklobutan"], ["siklopentan"], ["siklogeksan"]
slots = []
G = "Tuzilish"
slots += [
 S("t-1", G, "choice", 1, [
  C("Siklalkanlarning (bir halqali) umumiy formulasi qaysi?", "CₙH₂ₙ", ["CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂", "CₙH₂ₙ₋₆"], "Halqa hosil bo'lishi ikkita vodorodni kamaytiradi: alkan C<sub>n</sub>H<sub>2n+2</sub> dan C<sub>n</sub>H<sub>2n</sub> hosil bo'ladi.", None, ("CₙH₂ₙ₊₂", "Bu alkanlarning formulasi. Siklik tuzilishda uglerodlar yopiq halqa hosil qilgani uchun ikkita vodorod kam.")),
  C("Siklopentanning molekulyar formulasi qaysi?", "C₅H₁₀", ["C₅H₁₂", "C₅H₈", "C₄H₈"], "Besh uglerodli halqa: C<sub>n</sub>H<sub>2n</sub> da n = 5, ya'ni C<sub>5</sub>H<sub>10</sub>.", sc, ("C₅H₁₂", "C₅H₁₂ pentan (alkan) formulasi. Halqada ikki vodorod kam bo'ladi.")),
 ]),
 S("t-2", G, "choice", 1, [
  C("Eng kichik halqali siklalkan qaysi?", "Siklopropan", ["Siklobutan", "Siklopentan", "Siklogeksan"], "Halqa kamida uch uglerod atomidan tuziladi: eng kichigi siklopropan.", sp, ("Siklobutan", "Eng kichik halqa to'rtta deb o'ylash. Aslida uchta uglerod ham yopiq halqa hosil qiladi.")),
  C("Siklobutan molekulasida nechta vodorod atomi bor?", "8", ["10", "6", "4"], "C<sub>n</sub>H<sub>2n</sub> da n = 4 bo'lsa, vodorod 8 ta: C<sub>4</sub>H<sub>8</sub>.", sb, ("10", "10 ta vodorod butanda (alkan). Halqa ikkita vodorodni kamaytiradi.")),
  C("Siklogeksanning molekulyar formulasi qaysi?", "C₆H₁₂", ["C₆H₁₄", "C₆H₆", "C₆H₁₀"], "Olti uglerodli halqa: C<sub>6</sub>H<sub>12</sub>.", sg, ("C₆H₆", "C₆H₆ benzol: u aromatik modda, siklogeksan emas.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("1,3-dibrompropan va rux: siklopropan olish reaksiyasini yozing", ["C3H6Br2", "Zn"], ["C3H6", "ZnBr2"], "C3H6Br2+Zn→C3H6+ZnBr2", "Rux ikkala bromni oladi, chetki uglerodlar o'zaro bog'lanib uch a'zoli halqa hosil bo'ladi.", sp),
  W("1,3-dixlorpropan va rux: siklopropan olish reaksiyasini yozing", ["C3H6Cl2", "Zn"], ["C3H6", "ZnCl2"], "C3H6Cl2+Zn→C3H6+ZnCl2", "Rux ikkala xlorni oladi, chetki uglerodlar bog'lanib halqa hosil qiladi.", sp),
 ]),
 S("o-2", G, "write", 2, [
  W("1,5-dibrompentan va rux: siklopentan olish reaksiyasini yozing", ["C5H10Br2", "Zn"], ["C5H10", "ZnBr2"], "C5H10Br2+Zn→C5H10+ZnBr2", "Besh uglerodli zanjirning ikki uchi bog'lanib besh a'zoli halqa hosil bo'ladi.", sc),
  W("1,6-dibromgeksan va rux: siklogeksan olish reaksiyasini yozing", ["C6H12Br2", "Zn"], ["C6H12", "ZnBr2"], "C6H12Br2+Zn→C6H12+ZnBr2", "Olti uglerodli zanjirning ikki uchi bog'lanib olti a'zoli halqa hosil bo'ladi.", sg),
 ]),
 S("o-3", G, "choice", 1, [
  C("Rux bilan reaksiyada siklopropan beradigan modda qaysi?", "1,3-dibrompropan", ["1,2-dibrompropan", "1,4-dibrombutan", "2,2-dibrompropan"], "Halqa hosil bo'lishi uchun brom chetki (1 va 3) uglerodlarda bo'lishi kerak.", sp, ("1,2-dibrompropan", "Qo'shni uglerodlardagi ikkita brom ruxda alken (propen) beradi, halqa emas.")),
  C("1,4-dibrombutan va ruxdan qaysi siklalkan hosil bo'ladi?", "Siklobutan", ["Siklopropan", "Siklopentan", "Siklogeksan"], "To'rt uglerodli zanjir uchlari bog'lanadi: halqadagi uglerodlar soni zanjir uzunligiga teng.", sb, ("Siklopropan", "Halqaga uglerod yo'qolmaydi: to'rt uglerod to'rt a'zoli halqani beradi.")),
 ]),
 S("o-4", G, "write", 2, [
  W("Geksanning degidrosiklanishini yozing (katalizator, qizdirish): siklogeksan va vodorod hosil bo'ladi", ["C6H14"], ["C6H12", "H2"], "C6H14→C6H12+H2", "Zanjirning ikki uchidagi vodorodlar ajraladi va uchlar halqaga bog'lanadi.", sg),
  W("Pentanning degidrosiklanishini yozing (katalizator, qizdirish): siklopentan va vodorod hosil bo'ladi", ["C5H12"], ["C5H10", "H2"], "C5H12→C5H10+H2", "Ikki chetki vodorod ajraladi, uglerod zanjiri besh a'zoli halqaga yopiladi.", sc),
 ]),
 S("o-5", G, "choice", 1, [
  C("Dihalogenalkandan siklalkan olishda qaysi metall ishlatiladi?", "Rux", ["Kaliy", "Kalsiy", "Alyuminiy"], "Rux ikkita galogenni olib, halqa hosil bo'lishiga imkon beradi.", None),
  C("Benzolni gidrogenlab siklogeksan olishda qaysi gaz kerak?", "Vodorod", ["Kislorod", "Azot", "Karbonat angidrid"], "Benzolga uch molekula vodorod birikadi (Ni, qizdirish).", sg),
 ]),
]
G = "Galogenlarning ta'siri"
slots += [
 S("g-1", G, "write", 1, [
  W("Siklopropanga brom ta'sir ettiring (halqa ochiladi)", ["C3H6", "Br2"], ["C3H6Br2"], "C3H6+Br2→C3H6Br2", "Uch a'zoli halqa zo'riqqan: u uziladi va brom ikki uchiga birikadi (1,3-dibrompropan).", sp),
  W("Siklopropanga xlor ta'sir ettiring (halqa ochiladi)", ["C3H6", "Cl2"], ["C3H6Cl2"], "C3H6+Cl2→C3H6Cl2", "Halqa uziladi, xlor ikki uchiga birikadi (1,3-dixlorpropan).", sp),
 ]),
 S("g-2", G, "write", 2, [
  W("Siklopentanga brom yorug'likda ta'sir ettiring (bitta vodorod almashinadi)", ["C5H10", "Br2"], ["C5H9Br", "HBr"], "C5H10+Br2→C5H9Br+HBr", "Beshlik halqa zo'riqmagan, u alkanga o'xshab o'rin olish reaksiyasiga kirishadi.", sc),
  W("Siklogeksanga brom yorug'likda ta'sir ettiring (bitta vodorod almashinadi)", ["C6H12", "Br2"], ["C6H11Br", "HBr"], "C6H12+Br2→C6H11Br+HBr", "Oltilik halqa barqaror: halqa ochilmaydi, vodorod bromga almashinadi.", sg),
 ]),
 S("g-3", G, "choice", 2, [
  C("Brom bilan reaksiyada qaysi siklalkanda halqa ochiladi?", "Siklopropan", ["Siklopentan", "Siklogeksan", "Metan"], "Faqat uch (va qisman to'rt) a'zoli halqa zo'riqqan bo'lib, birikish bilan ochiladi.", sp, ("Siklogeksan", "Siklogeksan alkanga o'xshaydi: faqat o'rin olish, halqa uzilmaydi.")),
  C("Siklogeksan xlor bilan yorug'likda qanday reaksiyaga kirishadi?", "O'rin olish", ["Birikish (halqa ochiladi)", "Polimerlanish", "Reaksiyaga kirishmaydi"], "Oltilik halqa barqaror: vodorod xlorga almashinadi, HCl ajraladi.", sg, ("Birikish (halqa ochiladi)", "Bu faqat siklopropanga xos. Siklogeksanda halqa zo'riqmagan.")),
 ]),
 S("g-4", G, "choice", 3, [
  C("2,1 g siklopropanga (M = 42) ortiqcha brom ta'sir ettirilsa, necha gramm 1,3-dibrompropan (M = 202) hosil bo'ladi?", "10,1 g", ["5,05 g", "20,2 g", "8,4 g"], "2,1 : 42 = 0,05 mol; birikishda 1 : 1 nisbat, 0,05 · 202 = 10,1 g.", sp, ("20,2 g", "20,2 g 0,1 mol dibromidga to'g'ri keladi; bu 4,2 g siklopropandan chiqadi.")),
  C("4,2 g siklopropanga ortiqcha brom ta'sir ettirilsa, necha gramm 1,3-dibrompropan (M = 202) hosil bo'ladi?", "20,2 g", ["10,1 g", "40,4 g", "16,8 g"], "4,2 : 42 = 0,1 mol; 1 : 1 nisbatda 0,1 · 202 = 20,2 g.", sp, ("10,1 g", "10,1 g 2,1 g siklopropandan chiqadi; massa ikki baravar katta.")),
 ]),
]
G = "HX ning ta'siri"
slots += [
 S("h-1", G, "write", 1, [
  W("Siklopropanga HBr ta'sir ettiring (halqa ochiladi)", ["C3H6", "HBr"], ["C3H7Br"], "C3H6+HBr→C3H7Br", "Halqa uziladi, HBr ikki uchiga birikadi: 1-brompropan hosil bo'ladi.", sp),
  W("Siklopropanga HCl ta'sir ettiring (halqa ochiladi)", ["C3H6", "HCl"], ["C3H7Cl"], "C3H6+HCl→C3H7Cl", "Halqa uziladi, 1-xlorpropan hosil bo'ladi.", sp),
 ]),
 S("h-2", G, "choice", 2, [
  C("Qaysi siklalkan HBr bilan oddiy sharoitda reaksiyaga kirishadi?", "Siklopropan", ["Siklopentan", "Siklogeksan", "Siklogeptan"], "Uch a'zoli halqa zo'riqqan va HBr ta'sirida ochiladi.", sp, ("Siklopentan", "Besh va olti a'zoli halqalar zo'riqmagan, HBr ularni ochmaydi.")),
  C("Siklopropan HBr bilan reaksiyaga kirishsa, qanday modda hosil bo'ladi?", "1-brompropan", ["2-brompropan", "1,3-dibrompropan", "Brombenzol"], "Halqa uziladi, uchlariga H va Br birikadi: CH₃CH₂CH₂Br.", sp, ("1,3-dibrompropan", "Dibromid Br₂ dan hosil bo'ladi. HBr faqat bitta brom beradi.")),
 ]),
 S("h-3", G, "choice", 3, [
  C("Siklopropanga HBr, hosil bo'lgan moddaga Na (Vyurs) ta'sir ettirilsa, qaysi alkan hosil bo'ladi?", "Geksan", ["Propan", "Butan", "Pentan"], "HBr 1-brompropan beradi; Vyurs reaksiyasida uglerod soni ikki baravar ortadi (2C₃ → C₆).", sp, ("Propan", "Propan Vyursda emas, galogenalkanning gidrogenlanishida hosil bo'ladi. Vyursda zanjir uzayadi.")),
  C("Siklopropanga HBr, so'ng Na (Vyurs) ta'sir ettirilsa, oxirgi alkanning molyar massasi qancha?", "86 g/mol", ["44 g/mol", "58 g/mol", "72 g/mol"], "Oxirgi modda geksan C₆H₁₄: 6 · 12 + 14 = 86.", sp, ("44 g/mol", "44 propanning massasi. Vyursda uglerod soni ikki baravar ortadi, shuning uchun geksan hosil bo'ladi.")),
 ]),
]
G = "Gidrogenlash"
slots += [
 S("r-1", G, "choice", 1, [
  C("Siklopropan vodorod bilan (Ni, ~80 °C) qaysi moddani beradi?", "Propan", ["Siklopentan", "Etan", "Propen"], "Uch a'zoli halqa uziladi va ikki vodorod birikadi: C₃H₈.", sp, ("Propen", "Propen alken bo'lardi. Gidrogenlashda halqa ochiladi va to'yingan alkan hosil bo'ladi.")),
  C("Siklobutan vodorod bilan (Ni, ~120 °C) qaysi moddani beradi?", "Butan", ["Propan", "Siklobutan hosil bo'lmaydi", "Buten"], "To'rt a'zoli halqa uziladi: C₄H₁₀.", sb, ("Propan", "Halqa ochilganda uglerod soni o'zgarmaydi: to'rt uglerod, butan.")),
 ]),
 S("r-2", G, "choice", 2, [
  C("Qaysi siklalkan gidrogenlanganda propan hosil bo'ladi?", "Siklopropan", ["Siklobutan", "Siklopentan", "Siklogeksan"], "Uglerod soni saqlanadi: uch uglerodli halqa propan beradi.", sp, ("Siklobutan", "Siklobutan butan beradi: uglerod soni halqa ochilganda o'zgarmaydi.")),
  C("Siklobutanni gidrogenlash mahsuloti qaysi?", "Butan", ["Propan", "Pentan", "Izobutan"], "Halqa uziladi, uglerod skeleti o'zgarmaydi: to'g'ri zanjirli butan.", sb, ("Izobutan", "Halqa skelet tarmoqlanishini hosil qilmaydi: to'g'ri zanjirli butan chiqadi.")),
 ]),
 S("r-3", G, "choice", 2, [
  C("Siklopentanning gidrogenlanishi siklopropanga nisbatan qanday?", "Qiyinroq: yuqori harorat kerak", ["Osonroq", "Bir xil sharoitda", "Hech qachon bormaydi"], "Beshlik halqa zo'riqmagan, shuning uchun gidrogenlash qattiq sharoit (~300 °C) talab qiladi.", sc, ("Bir xil sharoitda", "Siklopropan zo'riqqan, shu uchun yumshoq sharoitda gidrogenlanadi. Siklopentanga ko'proq harorat kerak.")),
  C("Siklopentanni gidrogenlash mahsuloti qaysi?", "Pentan", ["Butan", "Geksan", "Izopentan"], "Besh uglerodli halqa uziladi: to'g'ri zanjirli pentan.", sc, ("Izopentan", "Halqani ochish tarmoqlanishni hosil qilmaydi, uglerod skeleti to'g'ri zanjirli.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Siklopropanning to'liq yonishini koeffitsientlar bilan yozing", ["C3H6", "O2"], ["CO2", "H2O"], "2C3H6+9O2→6CO2+6H2O", "Avval uglerod, keyin vodorod, oxirida kislorod tenglashtiriladi: 2C₃H₆ ga 9 O₂.", sp),
  W("Siklobutanning to'liq yonishini koeffitsientlar bilan yozing", ["C4H8", "O2"], ["CO2", "H2O"], "C4H8+6O2→4CO2+4H2O", "CO₂ va H₂O ning kislorodi: 8 + 4 = 12 ta atom, ya'ni 6 O₂.", sb),
 ]),
 S("k-2", G, "write", 2, [
  W("Siklopentanning to'liq yonishini koeffitsientlar bilan yozing", ["C5H10", "O2"], ["CO2", "H2O"], "2C5H10+15O2→10CO2+10H2O", "Kislorod soni kasr (7,5) chiqadi, shuning uchun hammasi ikki baravar: 2C₅H₁₀ + 15O₂.", sc),
  W("Siklogeksanning to'liq yonishini koeffitsientlar bilan yozing", ["C6H12", "O2"], ["CO2", "H2O"], "C6H12+9O2→6CO2+6H2O", "Kislorod: 12 + 6 = 18 ta atom, ya'ni 9 O₂.", sg),
 ]),
 S("k-3", G, "choice", 1, [
  C("Siklogeksan to'liq yonganda qaysi moddalar hosil bo'ladi?", "CO₂ va H₂O", ["CO va H₂", "C va H₂O", "CO₂ va H₂"], "To'liq yonishda uglerod CO₂ ga, vodorod H₂O ga aylanadi.", sg, ("CO va H₂", "CO yetishmagan kislorodda hosil bo'ladi. To'liq yonishda faqat CO₂ va H₂O.")),
  C("Siklopropan yonganda hosil bo'lgan CO₂ va H₂O ning mol nisbati qanday?", "1 : 1", ["3 : 4", "1 : 2", "2 : 1"], "C₃H₆ dan 3 CO₂ va 3 H₂O: nisbat 1 : 1.", sp, ("3 : 4", "3 : 4 propan (alkan) uchun. Siklopropanda vodorod 6 ta, shuning uchun 3 H₂O.")),
 ]),
 S("k-4", G, "choice", 3, [
  C("1 mol siklogeksan to'liq yonishiga necha mol O₂ kerak?", "9", ["6", "8", "10"], "6 CO₂ uchun 6 O₂, 6 H₂O uchun yana 3 O₂: jami 9 mol.", sg, ("6", "6 faqat CO₂ dagi kislorod. Suvdagi kislorod ham hisobga olinadi.")),
  C("1 mol siklopentan to'liq yonishiga necha mol O₂ kerak?", "7,5", ["5", "10", "6"], "5 CO₂ uchun 5 O₂, 5 H₂O uchun yana 2,5 O₂: jami 7,5 mol.", sc, ("5", "5 faqat CO₂ uchun yetadi. Suv hosil bo'lishiga ham kislorod ketadi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C4H8Br2", "C4H8", "C4H10", "C4H9Cl"]}
cB = {"all": ["C6H6", "C6H12", "C6H11Cl", "C12H22"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (rux)", ["C4H8Br2", "Zn"], ["C4H8", "ZnBr2"], "C4H8Br2+Zn→C4H8+ZnBr2", "Rux ikkala bromni oladi, to'rt uglerod halqaga yopiladi: siklobutan.", sb, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Ni, qizdirish)", ["C6H6", "H2"], ["C6H12"], "C6H6+3H2→C6H12", "Benzolga uch molekula vodorod birikib siklogeksan hosil qiladi.", sg, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (Ni, ~120 °C)", ["C4H8", "H2"], ["C4H10"], "C4H8+H2→C4H10", "Siklobutan halqasi uziladi: butan hosil bo'ladi.", sb, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (yorug'likda)", ["C6H12", "Cl2"], ["C6H11Cl", "HCl"], "C6H12+Cl2→C6H11Cl+HCl", "Siklogeksanning bitta vodorodi xlorga almashinadi.", sg, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 2, [
  W("Zanjirning 3-reaksiyasini yozing (yorug'likda)", ["C4H10", "Cl2"], ["C4H9Cl", "HCl"], "C4H10+Cl2→C4H9Cl+HCl", "Butanning bitta vodorodi xlorga almashinadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Vyurs)", ["C6H11Cl", "Na"], ["C12H22", "NaCl"], "2C6H11Cl+2Na→C12H22+2NaCl", "Ikki siklogeksil radikal birlashadi: uglerod soni ikki baravar ortadi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
day = {"version": 2, "day": 2, "topic": "Sikloalkanlar", "substances": ["siklopropan", "siklobutan", "siklopentan", "siklogeksan"], "slots": slots}
json.dump(day, open("kun_02.json", "w"), ensure_ascii=False, indent=1)
print(len(slots))
