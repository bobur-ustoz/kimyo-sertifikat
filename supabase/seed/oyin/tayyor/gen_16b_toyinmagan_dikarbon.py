from lib import *
Ml, Fu, An = ["malein kislota"], ["fumar kislota"], ["malein angidrid"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 2, [
  W("Benzolning havo kislorodi bilan oksidlanishini yozing (V₂O₅, 450 °C): malein angidrid hosil bo'ladi", ["C6H6", "O2"], ["C4H2O3", "CO2", "H2O"], "2C6H6+9O2→2C4H2O3+4CO2+4H2O", "Halqa uziladi, ikki uglerod CO₂ ga ketadi.", An),
  W("Butanning havo kislorodi bilan oksidlanishini yozing (V₂O₅ katalizatori): malein angidrid hosil bo'ladi", ["C4H10", "O2"], ["C4H2O3", "H2O"], "2C4H10+7O2→2C4H2O3+8H2O", "Sanoatda butandan malein angidrid olinadi.", An),
 ]),
 S("o-2", G, "write", 2, [
  W("Malein angidridning gidrolizini yozing", ["C4H2O3", "H2O"], ["C4H4O4"], "C4H2O3+H2O→C4H4O4", "Angidrid suv bilan malein kislotaga aylanadi.", An),
  W("Alma kislotaning degidratlanishini yozing (qizdirish): fumar kislota hosil bo'ladi", ["C4H6O5"], ["C4H4O4", "H2O"], "C4H6O5→C4H4O4+H2O", "Suv ajralib qo'shbog' hosil bo'ladi.", Fu),
 ]),
 S("o-3", G, "write", 2, [
  W("Atsetilen, CO va suv reaksiyasini yozing (Ni(CO)₄, 2 mol CO): qahrabo kislota olinadi", ["C2H2", "CO", "H2O"], ["C4H6O4"], "C2H2+2CO+2H2O→C4H6O4", "Atsetilenga ikki karboksil guruhi va vodorod birikadi; keyin degidrogenlab to'yinmagan kislota olinadi.", None),
  W("Qahrabo kislotaning degidrogenlanishini yozing", ["C4H6O4"], ["C4H4O4", "H2"], "C4H6O4→C4H4O4+H2", "Ikki vodorod ajralib qo'shbog' hosil bo'ladi.", Fu),
 ]),
 S("o-4", G, "choice", 1, [
  C("Malein kislotaning tuzilish formulasi qaysi?", "HOOC–CH=CH–COOH", ["HOOC–CH₂–CH₂–COOH", "HOOC–COOH", "CH₂=C(COOH)₂"], "Qo'shbog'li to'yinmagan dikarbon kislota.", Ml, ("HOOC–CH₂–CH₂–COOH", "Bu qahrabo kislota: qo'shbog'siz.")),
  C("Quyidagilardan qaysi biri to'yinmagan dikarbon kislota?", "Fumar kislota", ["Qahrabo kislota", "Oksalat kislota", "Adipin kislota"], "HOOC–CH=CH–COOH (trans).", Fu, ("Qahrabo kislota", "Qahrabo kislota to'yingan.")),
 ]),
 S("o-5", G, "choice", 2, [
  C("Malein angidrid sanoatda qaysi moddalardan olinadi?", "Benzol yoki butanni oksidlab", ["Etanolni oksidlab", "Glitserindan", "Metandan"], "V₂O₅ katalizatorida havo kislorodi bilan.", An, ("Etanolni oksidlab", "Etanol oksidlansa sirka kislota hosil bo'ladi.")),
  C("Malein kislotaning izomeri qaysi?", "Fumar kislota", ["Qahrabo kislota", "Malon kislota", "Oksalat kislota"], "Ikkalasi C₄H₄O₄: faqat fazoviy joylashuvi farq qiladi.", Fu, ("Qahrabo kislota", "Qahrabo kislotaning formulasi C₄H₆O₄.")),
 ]),
]
G = "Cis-trans izomeriya"
slots += [
 S("i-1", G, "choice", 1, [
  C("Malein kislota qanday izomer?", "Cis-izomer", ["Trans-izomer", "Optik izomer", "Zanjir izomeri"], "Ikkala COOH bir tomonda.", Ml),
  C("Fumar kislota qanday izomer?", "Trans-izomer", ["Cis-izomer", "Optik izomer", "Zanjir izomeri"], "COOH guruhlar qarama-qarshi tomonda.", Fu, ("Cis-izomer", "Cis-izomer malein kislota.")),
 ]),
 S("i-2", G, "choice", 2, [
  C("Qaysi biri suvda yaxshiroq eriydi?", "Malein kislota (cis)", ["Fumar kislota (trans)", "Ikkalasi teng", "Ikkalasi erimaydi"], "Cis-izomer qutbliroq, suvda ancha yaxshi eriydi.", Ml, ("Fumar kislota (trans)", "Trans-izomer simmetrik va suvda kam eriydi.")),
  C("Qaysi birining suyuqlanish harorati yuqori?", "Fumar kislota", ["Malein kislota", "Teng", "Ikkalasi suyuqlanmaydi"], "Simmetrik trans-izomer kristallarda zich joylashadi.", Fu, ("Malein kislota", "Cis-izomerda suyuqlanish harorati ancha past.")),
 ]),
 S("i-3", G, "choice", 3, [
  C("Cis-trans izomeriya uchun qanday shart bajarilishi kerak?", "Qo'shbog'dagi har bir uglerodda ikki xil o'rinbosar bo'lishi kerak", ["Qo'shbog' bo'lishining o'zi kifoya", "Uchbog' bo'lishi kerak", "Halqa bo'lishi shart"], "Qo'shbog' atrofida aylanish yo'q va har tomonda har xil guruhlar bor.", Ml, ("Qo'shbog' bo'lishining o'zi kifoya", "Etilenda ikkala uglerodda ham bir xil vodorodlar: izomeriya yo'q.")),
  C("Quyidagilardan qaysi biri cis-trans izomeriyaga ega?", "Buten-2", ["Buten-1", "Propen", "Etilen"], "Ikkala qo'shbog'li uglerodda H va CH₃.", Fu, ("Buten-1", "Bitta uglerodda ikkita H: izomer yo'q.")),
 ]),
]
G = "Kislotali xossalar"
slots += [
 S("m-1", G, "write", 1, [
  W("Malein kislotaga ortiqcha NaOH ta'sir ettiring", ["C4H4O4", "NaOH"], ["C4H2Na2O4", "H2O"], "C4H4O4+2NaOH→C4H2Na2O4+2H2O", "Natriy maleat hosil bo'ladi.", Ml),
  W("Fumar kislotaga ortiqcha KOH ta'sir ettiring", ["C4H4O4", "KOH"], ["C4H2K2O4", "H2O"], "C4H4O4+2KOH→C4H2K2O4+2H2O", "Kaliy fumarat hosil bo'ladi.", Fu),
 ]),
 S("m-2", G, "write", 2, [
  W("Malein kislota va ortiqcha metanol reaksiyasini yozing (H₂SO₄)", ["C4H4O4", "CH3OH"], ["C6H8O4", "H2O"], "C4H4O4+2CH3OH→C6H8O4+2H2O", "Dimetil maleat hosil bo'ladi.", Ml),
  W("Fumar kislota va ortiqcha etanol reaksiyasini yozing (H₂SO₄)", ["C4H4O4", "C2H5OH"], ["C8H12O4", "H2O"], "C4H4O4+2C2H5OH→C8H12O4+2H2O", "Dietil fumarat hosil bo'ladi.", Fu),
 ]),
 S("m-3", G, "write", 2, [
  W("Malein kislotaga rux ta'sir ettiring", ["C4H4O4", "Zn"], ["C4H2O4Zn", "H2"], "C4H4O4+Zn→C4H2O4Zn+H2", "Rux maleat va vodorod hosil bo'ladi.", Ml),
  W("Fumar kislotaga magniy ta'sir ettiring", ["C4H4O4", "Mg"], ["C4H2MgO4", "H2"], "C4H4O4+Mg→C4H2MgO4+H2", "Magniy fumarat va vodorod hosil bo'ladi.", Fu),
 ]),
]
G = "Birikish"
slots += [
 S("b-1", G, "write", 1, [
  W("Malein kislotani gidrogenlang (Ni)", ["C4H4O4", "H2"], ["C4H6O4"], "C4H4O4+H2→C4H6O4", "Qo'shbog' to'yinadi: qahrabo kislota.", Ml),
  W("Malein angidridni gidrogenlang (Ni)", ["C4H2O3", "H2"], ["C4H4O3"], "C4H2O3+H2→C4H4O3", "Suksinil angidrid hosil bo'ladi.", An),
 ]),
 S("b-2", G, "write", 1, [
  W("Malein kislotaga xlor ta'sir ettiring", ["C4H4O4", "Cl2"], ["C4H4Cl2O4"], "C4H4O4+Cl2→C4H4Cl2O4", "Xlor qo'shbog'ga birikadi.", Ml),
  W("Fumar kislotaga yod ta'sir ettiring", ["C4H4O4", "I2"], ["C4H4I2O4"], "C4H4O4+I2→C4H4I2O4", "Yod qo'shbog'ga birikadi.", Fu),
 ]),
 S("b-3", G, "write", 2, [
  W("Malein kislotaga HBr ta'sir ettiring", ["C4H4O4", "HBr"], ["C4H5BrO4"], "C4H4O4+HBr→C4H5BrO4", "Brom va vodorod qo'shbog'ga birikadi.", Ml),
  W("Fumar kislotaga suv birikishini yozing (fumaraza, organizmda)", ["C4H4O4", "H2O"], ["C4H6O5"], "C4H4O4+H2O→C4H6O5", "Alma kislota hosil bo'ladi: hujayra nafasi (Krebs sikli) bosqichi.", Fu),
 ]),
 S("b-4", G, "choice", 3, [
  C("Fumar kislotaga suv birikishidan qaysi kislota hosil bo'ladi?", "Alma kislota (oksiqahrabo)", ["Limon kislota", "Sut kislota", "Qahrabo kislota"], "Suv qo'shbog'ga birikib bitta OH guruhini beradi.", Fu, ("Qahrabo kislota", "Qahrabo kislota gidrogenlashdan hosil bo'ladi, gidratlashdan emas.")),
  C("Malein kislota gidrogenlansa, qaysi modda hosil bo'ladi?", "Qahrabo kislota", ["Fumar kislota", "Alma kislota", "Adipin kislota"], "Qo'shbog' to'yinadi, to'rt uglerodli to'yingan dikarbon kislota.", Ml, ("Fumar kislota", "Fumar kislota malein kislotaning izomeri, gidrogenlash mahsuloti emas.")),
 ]),
]
G = "Angidrid va qizdirish"
slots += [
 S("t-1", G, "write", 2, [
  W("Malein kislotaning qizdirilganda angidridga aylanishini yozing", ["C4H4O4"], ["C4H2O3", "H2O"], "C4H4O4→C4H2O3+H2O", "Cis-izomer halqa hosil qilib suv ajratadi.", Ml),
  W("Malein angidrid va ortiqcha metanol reaksiyasini yozing", ["C4H2O3", "CH3OH"], ["C6H8O4", "H2O"], "C4H2O3+2CH3OH→C6H8O4+H2O", "Dimetil maleat hosil bo'ladi.", An),
 ]),
 S("t-2", G, "write", 2, [
  W("Malein angidridga ortiqcha NaOH ta'sir ettiring", ["C4H2O3", "NaOH"], ["C4H2Na2O4", "H2O"], "C4H2O3+2NaOH→C4H2Na2O4+H2O", "Angidrid ochilib natriy maleat hosil bo'ladi.", An),
  W("Malein angidridga ammiak ta'sir ettiring", ["C4H2O3", "NH3"], ["C4H5NO3"], "C4H2O3+NH3→C4H5NO3", "Halqa ochilib amid-kislota hosil bo'ladi.", An),
 ]),
 S("t-3", G, "choice", 2, [
  C("Malein angidrid suv bilan reaksiyaga kirishsa, nima hosil bo'ladi?", "Malein kislota", ["Fumar kislota", "Qahrabo kislota", "Sirka kislota"], "Angidrid gidrolizlanib dikarbon kislota beradi.", An, ("Fumar kislota", "Halqa ochilganda cis-konfiguratsiya saqlanadi: malein kislota.")),
  C("Qaysi izomer qizdirilganda osongina angidrid hosil qiladi?", "Malein kislota", ["Fumar kislota", "Ikkalasi birdek", "Hech biri"], "Cis-izomerda ikkala COOH bir tomonda va halqa hosil qila oladi.", Ml, ("Fumar kislota", "Trans-izomerda COOH guruhlar halqa hosil qila olmaydi.")),
 ]),
]
G = "Oksidlanish va qo'llanilishi"
slots += [
 S("k-1", G, "write", 2, [
  W("Malein kislotaning to'liq yonishini yozing", ["C4H4O4", "O2"], ["CO2", "H2O"], "C4H4O4+3O2→4CO2+2H2O", "Kislorod: 8 + 2 − 4 = 6 atom, ya'ni 3 O₂.", Ml),
  W("Malein angidridning to'liq yonishini yozing", ["C4H2O3", "O2"], ["CO2", "H2O"], "C4H2O3+3O2→4CO2+H2O", "Kislorod: 8 + 1 − 3 = 6 atom, ya'ni 3 O₂.", An),
 ]),
 S("k-2", G, "write", 3, [
  W("Malein kislotaning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (Vagner)", ["C4H4O4", "KMnO4", "H2O"], ["C4H6O6", "MnO2", "KOH"], "3C4H4O4+2KMnO4+4H2O→3C4H6O6+2MnO2+2KOH", "Qo'shbog'ga ikkita OH birikadi: vino kislota.", Ml),
  W("Fumar kislotaga vodorod peroksid ta'sir ettiring (gidroksillash)", ["C4H4O4", "H2O2"], ["C4H6O6"], "C4H4O4+H2O2→C4H6O6", "Ikkita OH guruhi birikadi: vino kislota.", Fu),
 ]),
 S("k-3", G, "choice", 1, [
  C("Malein angidrid qayerda ishlatiladi?", "Alkid va poliefir smolalar ishlab chiqarishda", ["Oziq-ovqat bo'yog'ida", "Portlovchi moddalarda", "O'g'itlarda"], "Smolalar va sopolimerlar uchun monomer.", An),
  C("Fumar kislota oziq-ovqat sanoatida qanday vazifani bajaradi?", "Kislotalilik regulyatori (E297)", ["Qand o'rnini bosuvchi", "Tuz", "Bo'yoq"], "Nordon ta'm beradi va pH ni boshqaradi.", Fu),
 ]),
]
G = "Zanjir"
cA = {"all": ["C4H4O4", "C4H2Cl2O2", "C6H8O4", "C6H10O4"]}
cB = {"all": ["C4H4O4", "C4H4Br2O4", "C4K2O4", "C4H2O4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (ortiqcha PCl₅)", ["C4H4O4", "PCl5"], ["C4H2Cl2O2", "POCl3", "HCl"], "C4H4O4+2PCl5→C4H2Cl2O2+2POCl3+2HCl", "Ikkala OH xlorga almashinadi: dixlorangidrid.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing", ["C4H4O4", "Br2"], ["C4H4Br2O4"], "C4H4O4+Br2→C4H4Br2O4", "Brom qo'shbog'ga birikadi.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (metanol)", ["C4H2Cl2O2", "CH3OH"], ["C6H8O4", "HCl"], "C4H2Cl2O2+2CH3OH→C6H8O4+2HCl", "Xlorangidrid metanol bilan dimetil efir hosil qiladi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (KOH ning spirtdagi eritmasi, ortiqcha)", ["C4H4Br2O4", "KOH"], ["C4K2O4", "KBr", "H2O"], "C4H4Br2O4+4KOH→C4K2O4+2KBr+4H2O", "Ikki HBr ajralib uchbog' hosil bo'ladi.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (Ni, qizdirish)", ["C6H8O4", "H2"], ["C6H10O4"], "C6H8O4+H2→C6H10O4", "Qo'shbog' to'yinadi: dimetil suksinat.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (H₂SO₄)", ["C4K2O4", "H2SO4"], ["C4H2O4", "K2SO4"], "C4K2O4+H2SO4→C4H2O4+K2SO4", "Atsetilendikarbon kislota hosil bo'ladi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(17, "To'yinmagan dikarbon kislotalar (qo'shimcha)", ["malein kislota", "fumar kislota", "malein angidrid"], slots)
