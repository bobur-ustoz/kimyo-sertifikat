from lib import *
DE, DM, ME = ["dietil efir"], ["dimetil efir"], ["metiletil efir"]
slots = []
G = "Nomlanish va izomeriya"
slots += [
 S("n-1", G, "choice", 1, [
  C("C₄H₁₀O tarkibli nechta oddiy efir izomeri bor?", "3", ["2", "4", "5"], "Metilpropil, metilizopropil va dietil efir.", DE, ("2", "Metilizopropil efirni unutish xatosi.")),
  C("C₃H₈O tarkibli nechta oddiy efir izomeri bor?", "1", ["2", "3", "0"], "Faqat metiletil efir (CH₃–O–C₂H₅).", ME, ("2", "Propanollar spirt izomeri, efir esa faqat bitta.")),
 ]),
 S("n-2", G, "choice", 1, [
  C("CH₃–O–CH₃ moddaning nomi qaysi?", "Dimetil efir", ["Metanol", "Etanol", "Metilen"], "Kislorod ikki metil guruhini bog'laydi.", DM),
  C("C₂H₅–O–C₂H₅ moddaning nomi qaysi?", "Dietil efir", ["Etilenglikol", "Dimetil efir", "Etilatsetat"], "Kislorod ikki etil guruhini bog'laydi.", DE, ("Dimetil efir", "Dimetil efirda metil guruhlar. Bu yerda etil.")),
 ]),
 S("n-3", G, "choice", 2, [
  C("C₂H₆O formulaga mos ikki izomer qaysilar?", "Etanol va dimetil efir", ["Etanol va etanal", "Metanol va metan", "Dimetil efir va metanol"], "Spirt va efir bir xil formulaga ega bo'lishi mumkin.", DM, ("Etanol va etanal", "Etanalning formulasi C₂H₄O.")),
  C("Efir va spirt orasidagi izomeriya turi qaysi?", "Funksional guruh izomeriyasi", ["Zanjir izomeriyasi", "Fazoviy izomeriya", "Joylashuv izomeriyasi"], "Molekula tarkibi bir xil, funksional guruh turli: –OH va –O–.", DE, ("Zanjir izomeriyasi", "Zanjir izomeriyasida uglerod skeleti farq qiladi, bu yerda esa funksional guruh.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Etanolning molekulalararo degidratlanishini yozing (H₂SO₄, 140 °C)", ["C2H5OH"], ["C4H10O", "H2O"], "2C2H5OH→C4H10O+H2O", "Ikki molekuladan bitta suv ajraladi: dietil efir.", DE),
  W("Metanolning molekulalararo degidratlanishini yozing (H₂SO₄, 140 °C)", ["CH3OH"], ["C2H6O", "H2O"], "2CH3OH→C2H6O+H2O", "Dimetil efir hosil bo'ladi.", DM),
 ]),
 S("o-2", G, "write", 2, [
  W("Natriy metilat va yodmetan reaksiyasini yozing (Vilyamson)", ["CH3ONa", "CH3I"], ["C2H6O", "NaI"], "CH3ONa+CH3I→C2H6O+NaI", "Alkogolyatdagi CH₃O⁻ galogenni almashtiradi.", DM),
  W("Natriy propilat va 1-brompropan reaksiyasini yozing (Vilyamson)", ["C3H7ONa", "C3H7Br"], ["C6H14O", "NaBr"], "C3H7ONa+C3H7Br→C6H14O+NaBr", "Dipropil efir hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Natriy etilat va xlormetan reaksiyasini yozing (Vilyamson)", ["C2H5ONa", "CH3Cl"], ["C3H8O", "NaCl"], "C2H5ONa+CH3Cl→C3H8O+NaCl", "Aralash efir: metiletil efir.", ME),
  W("Natriy metilat va bromoetan reaksiyasini yozing (Vilyamson)", ["CH3ONa", "C2H5Br"], ["C3H8O", "NaBr"], "CH3ONa+C2H5Br→C3H8O+NaBr", "Xuddi shu aralash efir boshqa yo'l bilan.", ME),
 ]),
 S("o-4", G, "write", 2, [
  W("Etilen va etanol reaksiyasini yozing (H⁺ katalizatori)", ["C2H4", "C2H5OH"], ["C4H10O"], "C2H4+C2H5OH→C4H10O", "Spirt qo'shbog'ga birikib efir hosil qiladi.", DE),
  W("Propen va metanol reaksiyasini yozing (H⁺ katalizatori)", ["C3H6", "CH3OH"], ["C4H10O"], "C3H6+CH3OH→C4H10O", "Markovnikov bo'yicha metilizopropil efir.", None),
 ]),
 S("o-5", G, "write", 3, [
  W("Xloretanga kumush oksid ta'sir ettiring (dietil efir hosil bo'ladi)", ["C2H5Cl", "Ag2O"], ["C4H10O", "AgCl"], "2C2H5Cl+Ag2O→C4H10O+2AgCl", "Kislorod ikki etil guruhini bog'laydi.", DE),
  W("Brommetanga kumush oksid ta'sir ettiring (dimetil efir hosil bo'ladi)", ["CH3Br", "Ag2O"], ["C2H6O", "AgBr"], "2CH3Br+Ag2O→C2H6O+2AgBr", "Ag₂O kislorod manbai bo'ladi.", DM),
 ]),
 S("o-6", G, "choice", 1, [
  C("Dietil efirni etanoldan olishda qanday sharoit kerak?", "H₂SO₄ ishtirokida 140 °C", ["H₂SO₄ ishtirokida 170 °C", "Na bilan", "Cu, 300 °C"], "Past haroratda molekulalararo suv ajraladi.", DE, ("H₂SO₄ ishtirokida 170 °C", "170 °C da etilen hosil bo'ladi.")),
  C("Oddiy efirlar spirtdan qanday olinadi?", "Molekulalararo degidratlash", ["Molekula ichidan suv ajratish", "Oksidlash", "Gidrogenlash"], "Ikki spirt molekulasi bitta suv ajratib birlashadi.", DE, ("Molekula ichidan suv ajratish", "Bunda alken hosil bo'ladi.")),
 ]),
 S("o-7", G, "choice", 3, [
  C("Vilyamson reaksiyasi uchun qaysi reagentlar kerak?", "Natriy alkogolyati va galogenalkan", ["Spirt va ishqor", "Alken va suv", "Aldegid va spirt"], "Alkogolyat galogenalkandagi galogenni o'z radikaliga almashtiradi.", DE, ("Spirt va ishqor", "Spirt ishqor bilan reaksiyaga kirishmaydi.")),
  C("Metanol va etanol aralashmasini degidratlaganda nechta har xil oddiy efir hosil bo'ladi?", "3 ta", ["1 ta", "2 ta", "4 ta"], "Dimetil, dietil va metiletil efirlar.", ME, ("1 ta", "Aralash efir ham hosil bo'ladi.")),
 ]),
]
G = "HX ning ta'siri"
slots += [
 S("h-1", G, "write", 2, [
  W("Dietil efirga 1 mol HI ta'sir ettiring", ["C4H10O", "HI"], ["C2H5I", "C2H5OH"], "C4H10O+HI→C2H5I+C2H5OH", "Efir bog'i uziladi: etil yodid va etanol.", DE),
  W("Dimetil efirga 1 mol HI ta'sir ettiring", ["C2H6O", "HI"], ["CH3I", "CH3OH"], "C2H6O+HI→CH3I+CH3OH", "Metil yodid va metanol hosil bo'ladi.", DM),
 ]),
 S("h-2", G, "write", 2, [
  W("Dietil efirga ortiqcha HI ta'sir ettiring", ["C4H10O", "HI"], ["C2H5I", "H2O"], "C4H10O+2HI→2C2H5I+H2O", "Ikkala bog' uziladi: ikki yodid va suv.", DE),
  W("Dimetil efirga ortiqcha HI ta'sir ettiring", ["C2H6O", "HI"], ["CH3I", "H2O"], "C2H6O+2HI→2CH3I+H2O", "Ikki metil yodid va suv hosil bo'ladi.", DM),
 ]),
 S("h-3", G, "write", 3, [
  W("Dietil efirga konsentrlangan HBr ta'sir ettiring (ortiqcha)", ["C4H10O", "HBr"], ["C2H5Br", "H2O"], "C4H10O+2HBr→2C2H5Br+H2O", "Efir bog'ining ikkalasi uziladi.", DE),
  W("Metiletil efirga ortiqcha HBr ta'sir ettiring", ["C3H8O", "HBr"], ["CH3Br", "C2H5Br", "H2O"], "C3H8O+2HBr→CH3Br+C2H5Br+H2O", "Ikki xil bromalkan hosil bo'ladi.", ME),
 ]),
 S("h-4", G, "choice", 2, [
  C("Dietil efirga HI ta'sir etsa (1 mol), qaysi moddalar hosil bo'ladi?", "Etil yodid va etanol", ["Etilen va suv", "Yodoform", "Sirka kislota"], "Efir bog'i uziladi, bir yarmi yodidga, ikkinchisi spirtga aylanadi.", DE, ("Etilen va suv", "Alken efirdan emas, spirtdan degidratlash orqali olinadi.")),
  C("Efir bog'ini uzish uchun qanday reagent kerak?", "Konsentrlangan HI yoki HBr", ["Suv", "NaOH eritmasi", "Natriy (sovuqda)"], "Oddiy efirlar kuchli kislotalarda uziladi.", DE, ("NaOH eritmasi", "Efirlar ishqorga chidamli.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Dietil efirning to'liq yonishini yozing", ["C4H10O", "O2"], ["CO2", "H2O"], "C4H10O+6O2→4CO2+5H2O", "Kislorod: 8 + 5 − 1 = 12 atom, ya'ni 6 O₂.", DE),
  W("Dimetil efirning to'liq yonishini yozing", ["C2H6O", "O2"], ["CO2", "H2O"], "C2H6O+3O2→2CO2+3H2O", "Kislorod: 4 + 3 − 1 = 6 atom, ya'ni 3 O₂.", DM),
 ]),
 S("k-2", G, "write", 2, [
  W("Metiletil efirning to'liq yonishini yozing", ["C3H8O", "O2"], ["CO2", "H2O"], "2C3H8O+9O2→6CO2+8H2O", "Kasr chiqmasligi uchun ikki baravar.", ME),
  W("Dietil efirning havoda oksidlanib peroksid hosil qilishini yozing", ["C4H10O", "O2"], ["C4H10O3"], "C4H10O+O2→C4H10O3", "Havoda uzoq turganda gidroperoksid hosil bo'ladi: portlash xavfi.", DE),
 ]),
 S("k-3", G, "choice", 2, [
  C("Dietil efir havoda uzoq saqlanganda nima hosil bo'ladi?", "Portlovchi peroksidlar", ["Etanol", "Sirka kislota", "Etilen"], "Kislorod ta'sirida peroksidlar yig'iladi.", DE, ("Sirka kislota", "Efir yonganda emas, saqlashda peroksid chiqadi.")),
  C("Dietil efirni qanday saqlash kerak?", "Qorong'i joyda, mahkam yopiq idishda", ["Ochiq idishda", "Yorug'lik tushadigan joyda", "Qizdirib"], "Yorug'lik va havo peroksid hosil bo'lishini tezlatadi.", DE, ("Ochiq idishda", "Ochiq idishda havo bilan tez oksidlanadi.")),
 ]),
]
G = "Xossalari"
slots += [
 S("s-1", G, "choice", 1, [
  C("Dietil efir natriy bilan reaksiyaga kirishadimi?", "Yo'q", ["Ha, vodorod ajraladi", "Ha, alkogolyat hosil bo'ladi", "Faqat qizdirilganda"], "Efirda harakatchan vodorod (OH) yo'q.", DE, ("Ha, vodorod ajraladi", "Spirtlar natriy bilan reaksiyaga kirishadi, efirlar esa yo'q.")),
  C("Dimetil efir ishqor eritmasi bilan reaksiyaga kirishadimi?", "Yo'q: ishqorga chidamli", ["Ha, gidrolizlanadi", "Ha, tuz hosil qiladi", "Faqat qizdirilganda"], "Efir bog'i C–O–C kuchli va ishqorda uzilmaydi.", DM),
 ]),
 S("s-2", G, "choice", 1, [
  C("Dietil efir suvda qanday eriydi?", "Kam eriydi", ["Yaxshi eriydi", "Butunlay erimaydi", "Reaksiyaga kirishadi"], "Vodorod bog'lar kam, suvda kam eriydi.", DE),
  C("Efirning qaynash harorati shu massali spirtnikidan...", "Past", ["Yuqori", "Teng", "Qaynamaydi"], "Efirlarda molekulalararo vodorod bog'lari yo'q.", DE, ("Yuqori", "Spirtlarda vodorod bog'lari bor, efirlarda yo'q.")),
 ]),
 S("s-3", G, "choice", 2, [
  C("Dietil efir qayerda ishlatiladi?", "Erituvchi sifatida", ["Plastmassa ishlab chiqarishda", "O'g'it sifatida", "Rangsiz shisha tayyorlashda"], "Moylar va smolalarni yaxshi eritadi.", DE),
  C("Dimetil efir normal sharoitda qanday agregat holatda?", "Gaz", ["Suyuqlik", "Qattiq", "Yarim qattiq"], "Qaynash harorati −24 °C: oddiy sharoitda gaz.", DM, ("Suyuqlik", "Dietil efir suyuqlik. Dimetil efir esa yengil, gaz.")),
 ]),
 S("s-4", G, "write", 3, [
  W("Etilen oksid va etanol reaksiyasini yozing (efir-spirt hosil bo'ladi)", ["C2H4O", "C2H5OH"], ["C4H10O2"], "C2H4O+C2H5OH→C4H10O2", "Halqa ochiladi: 2-etoksietanol.", DE),
  W("Etilen oksid va metanol reaksiyasini yozing", ["C2H4O", "CH3OH"], ["C3H8O2"], "C2H4O+CH3OH→C3H8O2", "Halqa ochiladi: 2-metoksietanol.", DM),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4", "C2H6O", "C2H5ONa", "C4H10O"]}
cB = {"all": ["CO", "CH4O", "CH3Cl", "C2H6O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (H₃PO₄, 300 °C)", ["C2H4", "H2O"], ["C2H5OH"], "C2H4+H2O→C2H5OH", "Suv qo'shbog'ga birikadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (ZnO, Cr₂O₃, bosim)", ["CO", "H2"], ["CH3OH"], "CO+2H2→CH3OH", "Metanolning sanoat sintezi.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing", ["C2H5OH", "Na"], ["C2H5ONa", "H2"], "2C2H5OH+2Na→2C2H5ONa+H2", "Natriy etilat hosil bo'ladi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (ZnCl₂, qizdirish)", ["CH3OH", "HCl"], ["CH3Cl", "H2O"], "CH3OH+HCl→CH3Cl+H2O", "OH xlorga almashinadi.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (Vilyamson, bromoetan bilan)", ["C2H5ONa", "C2H5Br"], ["C4H10O", "NaBr"], "C2H5ONa+C2H5Br→C4H10O+NaBr", "Dietil efir hosil bo'ladi.", DE, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Vilyamson, natriy metilat bilan)", ["CH3Cl", "CH3ONa"], ["C2H6O", "NaCl"], "CH3Cl+CH3ONa→C2H6O+NaCl", "Dimetil efir hosil bo'ladi.", DM, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(11, "Oddiy efirlar", ["dietil efir", "dimetil efir", "metiletil efir"], slots)
