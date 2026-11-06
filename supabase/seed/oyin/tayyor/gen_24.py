from lib import *
Gi, Al = ["glitsin"], ["alanin"]
slots = []
G = "Izomeriya va nomlanish"
slots += [
 S("n-1", G, "choice", 1, [
  C("Glitsinning tuzilish formulasi qaysi?", "H₂N–CH₂–COOH", ["CH₃–CH(NH₂)–COOH", "H₂N–CH₂–CH₂–COOH", "CH₃–CH₂–NH₂"], "Eng oddiy aminokislota: aminosirka kislota.", Gi, ("CH₃–CH(NH₂)–COOH", "Bu alanin: radikali CH₃.")),
  C("Alaninning tuzilish formulasi qaysi?", "CH₃–CH(NH₂)–COOH", ["H₂N–CH₂–COOH", "H₂N–CH₂–CH₂–COOH", "CH₃–CH(OH)–COOH"], "α-aminopropion kislota.", Al, ("CH₃–CH(OH)–COOH", "Bu sut kislota: NH₂ o'rniga OH.")),
 ]),
 S("n-2", G, "choice", 2, [
  C("α-aminokislotada aminoguruh qayerda joylashgan?", "Karboksilga qo'shni (2-) uglerodda", ["Oxirgi uglerodda", "Karboksil uglerodida", "3-uglerodda"], "Alfa holat: karboksildan keyingi birinchi uglerod.", Gi, ("3-uglerodda", "3-holat β-aminokislotalarga xos.")),
  C("C₃H₇NO₂ formulaga mos ikki aminokislota izomeri qaysilar?", "α-alanin va β-alanin", ["Alanin va glitsin", "Alanin va valin", "β-alanin va serin"], "NH₂ guruhi 2- yoki 3-holatda.", Al, ("Alanin va glitsin", "Glitsinning formulasi C₂H₅NO₂.")),
 ]),
 S("n-3", G, "choice", 3, [
  C("Quyidagi aminokislotalardan qaysi birida asimmetrik uglerod atomi yo'q?", "Glitsin", ["Alanin", "Valin", "Serin"], "Glitsinda α-uglerodda ikkita vodorod bor.", Gi, ("Alanin", "Alaninda α-uglerodda H, NH₂, COOH, CH₃: to'rt xil o'rinbosar.")),
  C("Alaninning nechta optik izomeri bor?", "2 (D va L)", ["1", "3", "4"], "Bitta asimmetrik uglerod: ikkita ko'zgusimon izomer.", Al, ("1", "Asimmetrik uglerod bor, shuning uchun ikkita izomer.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Bromsirka kislotaga ortiqcha ammiak ta'sir ettiring", ["C2H3BrO2", "NH3"], ["C2H5NO2", "NH4Br"], "C2H3BrO2+2NH3→C2H5NO2+NH4Br", "Brom aminoguruhga almashinadi: glitsin.", Gi),
  W("2-xlorpropion kislotaga ortiqcha ammiak ta'sir ettiring", ["C3H5ClO2", "NH3"], ["C3H7NO2", "NH4Cl"], "C3H5ClO2+2NH3→C3H7NO2+NH4Cl", "Xlor aminoguruhga almashinadi: alanin.", Al),
 ]),
 S("o-2", G, "write", 2, [
  W("Aminoasetonitrilni to'liq gidrolizlang (H⁺, qizdirish)", ["C2H4N2", "H2O"], ["C2H5NO2", "NH3"], "C2H4N2+2H2O→C2H5NO2+NH3", "Nitril COOH ga o'tadi: glitsin.", Gi),
  W("2-aminobutironitrilni to'liq gidrolizlang (H⁺, qizdirish)", ["C4H8N2", "H2O"], ["C4H9NO2", "NH3"], "C4H8N2+2H2O→C4H9NO2+NH3", "2-aminobutan kislota hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Nitrosirka kislotani vodorod bilan qaytaring", ["C2H3NO4", "H2"], ["C2H5NO2", "H2O"], "C2H3NO4+3H2→C2H5NO2+2H2O", "Nitro guruh aminoguruhga qaytariladi.", Gi),
  W("2-nitropropion kislotani vodorod bilan qaytaring", ["C3H5NO4", "H2"], ["C3H7NO2", "H2O"], "C3H5NO4+3H2→C3H7NO2+2H2O", "Alanin hosil bo'ladi.", Al),
 ]),
 S("o-4", G, "write", 3, [
  W("Sirka aldegid, ammiak va sianid kislota reaksiyasini yozing (Streker sintezi)", ["C2H4O", "NH3", "HCN"], ["C3H6N2", "H2O"], "C2H4O+NH3+HCN→C3H6N2+H2O", "α-aminonitril hosil bo'ladi (keyin gidroliz bilan alanin).", Al),
  W("Formaldegid, ammiak va sianid kislota reaksiyasini yozing (Streker)", ["CH2O", "NH3", "HCN"], ["C2H4N2", "H2O"], "CH2O+NH3+HCN→C2H4N2+H2O", "Aminoasetonitril hosil bo'ladi (keyin gidroliz bilan glitsin).", Gi),
 ]),
]
G = "Amfoter xossa"
slots += [
 S("m-1", G, "write", 1, [
  W("Glitsinga xlorid kislota ta'sir ettiring", ["C2H5NO2", "HCl"], ["C2H6ClNO2"], "C2H5NO2+HCl→C2H6ClNO2", "Aminoguruh proton biriktiradi: glitsin gidroxlorid.", Gi),
  W("Alaninga bromid kislota ta'sir ettiring", ["C3H7NO2", "HBr"], ["C3H8BrNO2"], "C3H7NO2+HBr→C3H8BrNO2", "Alanin gidrobromid hosil bo'ladi.", Al),
 ]),
 S("m-2", G, "write", 1, [
  W("Glitsinga NaOH ta'sir ettiring", ["C2H5NO2", "NaOH"], ["C2H4NNaO2", "H2O"], "C2H5NO2+NaOH→C2H4NNaO2+H2O", "Karboksil neytrallanadi: natriy glitsinat.", Gi),
  W("Alaninga KOH ta'sir ettiring", ["C3H7NO2", "KOH"], ["C3H6KNO2", "H2O"], "C3H7NO2+KOH→C3H6KNO2+H2O", "Kaliy alaninat hosil bo'ladi.", Al),
 ]),
 S("m-3", G, "write", 2, [
  W("Glitsinga soda (Na₂CO₃) ta'sir ettiring", ["C2H5NO2", "Na2CO3"], ["C2H4NNaO2", "CO2", "H2O"], "2C2H5NO2+Na2CO3→2C2H4NNaO2+CO2+H2O", "Karboksil guruhi karbonatni parchalaydi: CO₂ ajraladi.", Gi),
  W("Alaninga magniy ta'sir ettiring", ["C3H7NO2", "Mg"], ["C6H12MgN2O4", "H2"], "2C3H7NO2+Mg→C6H12MgN2O4+H2", "Magniy alaninat va vodorod hosil bo'ladi.", Al),
 ]),
 S("m-4", G, "choice", 2, [
  C("Aminokislotalar qanday xossaga ega?", "Amfoter: kislota ham, asos ham xossasini ko'rsatadi", ["Faqat kislotali", "Faqat asosli", "Neytral"], "Karboksil kislota, aminoguruh esa asos xossasini beradi.", Gi, ("Faqat kislotali", "Aminoguruh asos xossasini ham beradi.")),
  C("Aminokislotaning ichki tuzi (bipolyar ion) qanday yoziladi?", "H₃N⁺–CH₂–COO⁻", ["H₂N–CH₂–COOH (neytral)", "H₃N⁺–CH₂–COOH", "H₂N–CH₂–COO⁻"], "Proton karboksildan aminoguruhga o'tadi.", Gi, ("H₂N–CH₂–COOH (neytral)", "Qattiq holatda va neytral eritmada bipolyar ion ko'proq.")),
 ]),
]
G = "Esterlanish"
slots += [
 S("e-1", G, "write", 2, [
  W("Glitsin va metanol reaksiyasini yozing (H⁺)", ["C2H5NO2", "CH3OH"], ["C3H7NO2", "H2O"], "C2H5NO2+CH3OH→C3H7NO2+H2O", "Glitsinning metil efiri hosil bo'ladi.", Gi),
  W("Alanin va etanol reaksiyasini yozing (H⁺)", ["C3H7NO2", "C2H5OH"], ["C5H11NO2", "H2O"], "C3H7NO2+C2H5OH→C5H11NO2+H2O", "Alaninning etil efiri hosil bo'ladi.", Al),
 ]),
 S("e-2", G, "write", 2, [
  W("Glitsin, etanol va HCl reaksiyasini yozing (efir gidroxloridi)", ["C2H5NO2", "C2H5OH", "HCl"], ["C4H10ClNO2", "H2O"], "C2H5NO2+C2H5OH+HCl→C4H10ClNO2+H2O", "HCl aminoguruhni himoya qilib, efir tuzi hosil qiladi.", Gi),
  W("Alanin, metanol va HCl reaksiyasini yozing (efir gidroxloridi)", ["C3H7NO2", "CH3OH", "HCl"], ["C4H10ClNO2", "H2O"], "C3H7NO2+CH3OH+HCl→C4H10ClNO2+H2O", "Alanin metil efirining gidroxloridi hosil bo'ladi.", Al),
 ]),
 S("e-3", G, "choice", 2, [
  C("Aminokislota esterlanganda qaysi guruh efirga aylanadi?", "Karboksil guruhi", ["Aminoguruh", "Ikkala guruh", "Hech biri"], "Spirt –COOH bilan reaksiyaga kirishadi, aminoguruh saqlanadi.", Gi, ("Aminoguruh", "Aminoguruh amid bog'i hosil qiladi, efir esa karboksildan.")),
  C("Aminokislotani esterlashdan asosiy maqsad nima bo'lishi mumkin?", "Karboksil guruhini himoya qilish (peptid sintezida)", ["Aminoguruhni oksidlash", "Halqa hosil qilish", "Polimer olish"], "Efir shaklida karboksil boshqa reaksiyalarda qatnashmaydi.", Gi, ("Halqa hosil qilish", "Halqa boshqa reaksiyalardan chiqadi.")),
 ]),
]
G = "Peptid bog'i va oqsil gidrolizi"
slots += [
 S("p-1", G, "write", 2, [
  W("Ikki molekula alanindan dipeptid hosil bo'lishini yozing", ["C3H7NO2"], ["C6H12N2O3", "H2O"], "2C3H7NO2→C6H12N2O3+H2O", "Karboksil va aminoguruh orasida peptid bog'i hosil bo'ladi.", Al),
  W("Alanin va glitsindan dipeptid hosil bo'lishini yozing", ["C3H7NO2", "C2H5NO2"], ["C5H10N2O3", "H2O"], "C3H7NO2+C2H5NO2→C5H10N2O3+H2O", "Alanilglitsin hosil bo'ladi, suv ajraladi.", Al),
 ]),
 S("p-2", G, "write", 3, [
  W("Uch molekula glitsindan tripeptid hosil bo'lishini yozing", ["C2H5NO2"], ["C6H11N3O4", "H2O"], "3C2H5NO2→C6H11N3O4+2H2O", "Ikkita peptid bog'i hosil bo'ladi: ikki molekula suv ajraladi.", Gi),
  W("Uch molekula alanindan tripeptid hosil bo'lishini yozing", ["C3H7NO2"], ["C9H17N3O4", "H2O"], "3C3H7NO2→C9H17N3O4+2H2O", "Ikki molekula suv ajraladi.", Al),
 ]),
 S("p-3", G, "write", 2, [
  W("Diglitsinning to'liq gidrolizini yozing", ["C4H8N2O3", "H2O"], ["C2H5NO2"], "C4H8N2O3+H2O→2C2H5NO2", "Peptid bog'i uzilib ikki molekula glitsin hosil bo'ladi.", Gi),
  W("Alanilglitsinning to'liq gidrolizini yozing", ["C5H10N2O3", "H2O"], ["C3H7NO2", "C2H5NO2"], "C5H10N2O3+H2O→C3H7NO2+C2H5NO2", "Alanin va glitsin hosil bo'ladi.", Al),
 ]),
 S("p-4", G, "choice", 2, [
  C("Peptid bog'i qaysi guruhdan iborat?", "–CO–NH–", ["–CO–O–", "–NH–NH–", "–CH=N–"], "Amid guruhi: bitta aminokislotaning COOH i boshqasining NH₂ si bilan.", Gi, ("–CO–O–", "Bu murakkab efir bog'i.")),
  C("Oqsilning to'liq gidrolizidan nima hosil bo'ladi?", "α-aminokislotalar aralashmasi", ["Glyukoza", "Yog' kislotalari", "Glitserin"], "Barcha peptid bog'lari uziladi.", Gi, ("Glyukoza", "Glyukoza polisaxaridlar gidrolizida hosil bo'ladi.")),
 ]),
]
G = "Dezaminlash va dekarboksillanish"
slots += [
 S("d-1", G, "write", 2, [
  W("Glitsinga nitrit kislota ta'sir ettiring", ["C2H5NO2", "HNO2"], ["C2H4O3", "N2", "H2O"], "C2H5NO2+HNO2→C2H4O3+N2+H2O", "NH₂ guruh OH ga almashinadi: glikol kislota.", Gi),
  W("Alaninga nitrit kislota ta'sir ettiring", ["C3H7NO2", "HNO2"], ["C3H6O3", "N2", "H2O"], "C3H7NO2+HNO2→C3H6O3+N2+H2O", "Sut kislota hosil bo'ladi, azot ajraladi.", Al),
 ]),
 S("d-2", G, "write", 2, [
  W("Glitsinning dekarboksillanishini yozing (Ba(OH)₂, qizdirish)", ["C2H5NO2"], ["CH5N", "CO2"], "C2H5NO2→CH5N+CO2", "Karboksil CO₂ holida ajraladi: metilamin.", Gi),
  W("Alaninning dekarboksillanishini yozing (qizdirish)", ["C3H7NO2"], ["C2H7N", "CO2"], "C3H7NO2→C2H7N+CO2", "Etilamin hosil bo'ladi.", Al),
 ]),
 S("d-3", G, "write", 3, [
  W("Alaninning dezaminlanishini yozing (ammiak ajraladi): akril kislota", ["C3H7NO2"], ["C3H4O2", "NH3"], "C3H7NO2→C3H4O2+NH3", "Aminoguruh va qo'shni vodorod ajralib qo'shbog' hosil bo'ladi.", Al),
  W("Valinning dezaminlanishini yozing (ammiak ajraladi)", ["C5H11NO2"], ["C5H8O2", "NH3"], "C5H11NO2→C5H8O2+NH3", "To'yinmagan kislota hosil bo'ladi.", None),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4O2", "C2H3ClO2", "C2H5NO2", "C4H8N2O3"]}
cB = {"all": ["C2H4O", "C2H5N", "C3H6N2", "C3H7NO2"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (qizil fosfor)", ["C2H4O2", "Cl2"], ["C2H3ClO2", "HCl"], "C2H4O2+Cl2→C2H3ClO2+HCl", "α-holatda xlorlash.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (sirka aldegid va ammiak)", ["C2H4O", "NH3"], ["C2H5N", "H2O"], "C2H4O+NH3→C2H5N+H2O", "Imin hosil bo'ladi.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (ortiqcha ammiak)", ["C2H3ClO2", "NH3"], ["C2H5NO2", "NH4Cl"], "C2H3ClO2+2NH3→C2H5NO2+NH4Cl", "Xlor aminoguruhga almashinadi: glitsin.", Gi, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (sianid kislota)", ["C2H5N", "HCN"], ["C3H6N2"], "C2H5N+HCN→C3H6N2", "α-aminonitril hosil bo'ladi.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (peptid bog'i)", ["C2H5NO2"], ["C4H8N2O3", "H2O"], "2C2H5NO2→C4H8N2O3+H2O", "Diglitsin hosil bo'ladi.", Gi, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (H⁺, qizdirish)", ["C3H6N2", "H2O"], ["C3H7NO2", "NH3"], "C3H6N2+2H2O→C3H7NO2+NH3", "Nitril COOH ga gidrolizlanadi: alanin.", Al, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(24, "Aminokislotalar", ["glitsin", "alanin"], slots)
