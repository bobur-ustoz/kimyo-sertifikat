from lib import *
Su, Sa, Gl = ["sut kislota"], ["salitsil kislota"], ["glikol kislota"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Xlorsirka kislotaga NaOH ning suvdagi eritmasi ta'sir ettiring", ["C2H3ClO2", "NaOH"], ["C2H4O3", "NaCl"], "C2H3ClO2+NaOH→C2H4O3+NaCl", "Xlor OH ga almashinadi: glikol kislota.", Gl),
  W("2-xlorpropion kislotaga NaOH ning suvdagi eritmasi ta'sir ettiring", ["C3H5ClO2", "NaOH"], ["C3H6O3", "NaCl"], "C3H5ClO2+NaOH→C3H6O3+NaCl", "Xlor OH ga almashinadi: sut kislota.", Su),
 ]),
 S("o-2", G, "write", 2, [
  W("Glikolonitrilning to'liq gidrolizini yozing", ["C2H3NO", "H2O"], ["C2H4O3", "NH3"], "C2H3NO+2H2O→C2H4O3+NH3", "Nitril COOH ga o'tadi.", Gl),
  W("2-gidroksibutironitrilning to'liq gidrolizini yozing", ["C4H7NO", "H2O"], ["C4H8O3", "NH3"], "C4H7NO+2H2O→C4H8O3+NH3", "2-gidroksimoy kislota hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Glyukozaning sut kislotali bijg'ishini yozing", ["C6H12O6"], ["C3H6O3"], "C6H12O6→2C3H6O3", "Glyukozadan ikki molekula sut kislota hosil bo'ladi.", Su),
  W("Laktidning to'liq gidrolizini yozing", ["C6H8O4", "H2O"], ["C3H6O3"], "C6H8O4+2H2O→2C3H6O3", "Halqa ochilib ikki molekula sut kislota hosil bo'ladi.", Su),
 ]),
 S("o-4", G, "write", 2, [
  W("Kaliy fenolyatga CO₂ ta'sir ettiring (Kolbe–Shmidt, bosim, 125 °C)", ["C6H5OK", "CO2"], ["C7H5KO3"], "C6H5OK+CO2→C7H5KO3", "COOH guruhi orto holatga birikadi: kaliy salitsilat.", Sa),
  W("Kaliy salitsilatga HCl ta'sir ettiring", ["C7H5KO3", "HCl"], ["C7H6O3", "KCl"], "C7H5KO3+HCl→C7H6O3+KCl", "Kislota ozod bo'ladi: salitsil kislota.", Sa),
 ]),
 S("o-5", G, "choice", 1, [
  C("Sut kislotaning tuzilish formulasi qaysi?", "CH₃–CH(OH)–COOH", ["CH₂(OH)–CH₂–COOH", "CH₃–CH₂–COOH", "HOOC–CH₂–COOH"], "OH guruhi α-holatda (2-uglerodda).", Su, ("CH₂(OH)–CH₂–COOH", "Bu 3-gidroksipropion kislota. Sut kislotada OH ikkinchi uglerodda.")),
  C("Salitsil kislota qaysi sinflarga mansub?", "Fenol va karbon kislota", ["Faqat spirt", "Aldegid va kislota", "Efir"], "Benzol halqasida OH va COOH (orto holatda).", Sa, ("Faqat spirt", "OH halqada: bu fenol.")),
 ]),
]
G = "Karboksil guruhiga xos"
slots += [
 S("c-1", G, "write", 1, [
  W("Sut kislotaga magniy ta'sir ettiring", ["C3H6O3", "Mg"], ["C6H10MgO6", "H2"], "2C3H6O3+Mg→C6H10MgO6+H2", "Magniy laktat va vodorod hosil bo'ladi.", Su),
  W("Glikol kislotaga NaOH ta'sir ettiring", ["C2H4O3", "NaOH"], ["C2H3NaO3", "H2O"], "C2H4O3+NaOH→C2H3NaO3+H2O", "Natriy glikolat hosil bo'ladi.", Gl),
 ]),
 S("c-2", G, "write", 2, [
  W("Sut kislotaga etanol ta'sir ettiring (H₂SO₄, eterifikatsiya)", ["C3H6O3", "C2H5OH"], ["C5H10O3", "H2O"], "C3H6O3+C2H5OH→C5H10O3+H2O", "Etil laktat hosil bo'ladi.", Su),
  W("Salitsil kislotaga metanol ta'sir ettiring (H₂SO₄)", ["C7H6O3", "CH3OH"], ["C8H8O3", "H2O"], "C7H6O3+CH3OH→C8H8O3+H2O", "Metil salitsilat (qishki yashil moyi) hosil bo'ladi.", Sa),
 ]),
 S("c-3", G, "write", 2, [
  W("Sut kislotaga ichimlik sodasi (NaHCO₃) ta'sir ettiring", ["C3H6O3", "NaHCO3"], ["C3H5NaO3", "CO2", "H2O"], "C3H6O3+NaHCO3→C3H5NaO3+CO2+H2O", "CO₂ ajraladi: karboksil guruhining isboti.", Su),
  W("Vino kislotaga ortiqcha NaOH ta'sir ettiring", ["C4H6O6", "NaOH"], ["C4H4Na2O6", "H2O"], "C4H6O6+2NaOH→C4H4Na2O6+2H2O", "Natriy tartrat hosil bo'ladi.", None),
 ]),
 S("c-4", G, "choice", 2, [
  C("Sut kislota qayerda hosil bo'ladi?", "Sut mahsulotlarida bijg'ish natijasida", ["Qand lavlagida", "Yog'larda", "Tuzda"], "Sut qandi bakteriyalar ta'sirida sut kislotaga aylanadi.", Su),
  C("Sut kislotaning nechta optik izomeri bor?", "2 (D va L)", ["1", "3", "4"], "Ikkinchi uglerod asimmetrik (to'rt xil o'rinbosar).", Su, ("1", "Asimmetrik uglerod bor, shuning uchun ikkita ko'zgusimon izomer.")),
 ]),
]
G = "Gidroksil guruhiga xos"
slots += [
 S("h-1", G, "write", 2, [
  W("Sut kislotani CuO bilan oksidlang (qizdirish)", ["C3H6O3", "CuO"], ["C3H4O3", "Cu", "H2O"], "C3H6O3+CuO→C3H4O3+Cu+H2O", "Ikkilamchi spirt guruhi ketonga o'tadi: pirouzum kislota.", Su),
  W("Glikol kislotani CuO bilan oksidlang (qizdirish)", ["C2H4O3", "CuO"], ["C2H2O3", "Cu", "H2O"], "C2H4O3+CuO→C2H2O3+Cu+H2O", "Glioksal kislota hosil bo'ladi.", Gl),
 ]),
 S("h-2", G, "write", 2, [
  W("Sut kislotaga HBr ta'sir ettiring", ["C3H6O3", "HBr"], ["C3H5BrO2", "H2O"], "C3H6O3+HBr→C3H5BrO2+H2O", "OH bromga almashinadi: 2-brompropion kislota.", Su),
  W("Glikol kislotaga HCl ta'sir ettiring", ["C2H4O3", "HCl"], ["C2H3ClO2", "H2O"], "C2H4O3+HCl→C2H3ClO2+H2O", "OH xlorga almashinadi.", Gl),
 ]),
 S("h-3", G, "write", 3, [
  W("Sut kislotaga sirka kislota ta'sir ettiring (OH esterlanadi)", ["C3H6O3", "C2H4O2"], ["C5H8O4", "H2O"], "C3H6O3+C2H4O2→C5H8O4+H2O", "Gidroksil guruhi sirka kislota bilan efir hosil qiladi.", Su),
  W("Sut kislotaga sirka angidrid ta'sir ettiring", ["C3H6O3", "C4H6O3"], ["C5H8O4", "C2H4O2"], "C3H6O3+C4H6O3→C5H8O4+C2H4O2", "Gidroksil guruhi atsillanadi.", Su),
 ]),
 S("h-4", G, "write", 3, [
  W("Sut kislotani KMnO₄ bilan kislotali muhitda oksidlang (pirouzum kislota)", ["C3H6O3", "KMnO4", "H2SO4"], ["C3H4O3", "MnSO4", "K2SO4", "H2O"], "5C3H6O3+2KMnO4+3H2SO4→5C3H4O3+2MnSO4+K2SO4+8H2O", "Spirt guruhi ketonga oksidlanadi (2 e): 5 : 2.", Su),
  W("Glikol kislotani KMnO₄ bilan kislotali muhitda oksidlang", ["C2H4O3", "KMnO4", "H2SO4"], ["C2H2O3", "MnSO4", "K2SO4", "H2O"], "5C2H4O3+2KMnO4+3H2SO4→5C2H2O3+2MnSO4+K2SO4+8H2O", "Glioksal kislota hosil bo'ladi.", Gl),
 ]),
]
G = "Degidratlanish"
slots += [
 S("d-1", G, "write", 2, [
  W("Glikol kislotaning molekulalararo degidratlanishini yozing (halqali eter)", ["C2H4O3"], ["C4H4O4", "H2O"], "2C2H4O3→C4H4O4+2H2O", "Olti a'zoli halqa: glikolid.", Gl),
  W("2-gidroksimoy kislotaning molekulalararo degidratlanishini yozing (halqali eter)", ["C4H8O3"], ["C8H12O4", "H2O"], "2C4H8O3→C8H12O4+2H2O", "Olti a'zoli halqali dieter hosil bo'ladi.", None),
 ]),
 S("d-2", G, "write", 2, [
  W("Sut kislotaning ichki degidratlanishini yozing (H₂SO₄)", ["C3H6O3"], ["C3H4O2", "H2O"], "C3H6O3→C3H4O2+H2O", "Suv ajralib qo'shbog' hosil bo'ladi: akril kislota.", Su),
  W("Sut kislotaning molekulalararo degidratlanishini yozing (chiziqli dimer)", ["C3H6O3"], ["C6H10O5", "H2O"], "2C3H6O3→C6H10O5+H2O", "Efir bog'i hosil bo'ladi, zanjir uzayadi.", Su),
 ]),
 S("d-3", G, "write", 3, [
  W("Sut kislotaning konsentrlangan H₂SO₄ bilan qizdirilganda parchalanishini yozing", ["C3H6O3"], ["C2H4O", "CH2O2"], "C3H6O3→C2H4O+CH2O2", "Sirka aldegid va chumoli kislota hosil bo'ladi.", Su),
  W("Sut kislotaning kuchli qizdirilganda parchalanishini yozing", ["C3H6O3"], ["C2H4O", "CO", "H2O"], "C3H6O3→C2H4O+CO+H2O", "Sirka aldegid, CO va suv hosil bo'ladi.", Su),
 ]),
 S("d-4", G, "choice", 2, [
  C("Laktid nima?", "Sut kislotaning halqali dieteri", ["Sut kislotaning angidridi", "Propion kislota", "Aldol"], "Ikki molekula sut kislotadan olti a'zoli halqa.", Su, ("Sut kislotaning angidridi", "Angidridda COOH guruhlar birlashadi, laktidda esa COOH va OH.")),
  C("Polilaktid (PLA) qanday material?", "Biologik parchalanadigan plastmassa", ["Portlovchi modda", "Elektr o'tkazuvchi metall", "Sintetik kauchuk"], "Sut kislota polimeri: tabiatda parchalanadi.", Su),
 ]),
]
G = "Salitsil kislota"
slots += [
 S("s-1", G, "write", 2, [
  W("Salitsil kislotaga ortiqcha bromli suv ta'sir ettiring", ["C7H6O3", "Br2"], ["C7H3Br3O3", "HBr"], "C7H6O3+3Br2→C7H3Br3O3+3HBr", "Uch vodorod bromga almashinadi.", Sa),
  W("Salitsil kislotani nitrolang (HNO₃)", ["C7H6O3", "HNO3"], ["C7H5NO5", "H2O"], "C7H6O3+HNO3→C7H5NO5+H2O", "Nitro guruh halqaga birikadi.", Sa),
 ]),
 S("s-2", G, "write", 2, [
  W("Salitsil kislotaga sirka angidrid ta'sir ettiring: aspirin", ["C7H6O3", "C4H6O3"], ["C9H8O4", "C2H4O2"], "C7H6O3+C4H6O3→C9H8O4+C2H4O2", "Atsetilsalitsil kislota (aspirin) hosil bo'ladi.", Sa),
  W("Salitsil kislotaga atsetilxlorid ta'sir ettiring", ["C7H6O3", "C2H3ClO"], ["C9H8O4", "HCl"], "C7H6O3+C2H3ClO→C9H8O4+HCl", "Aspirin hosil bo'ladi, HCl ajraladi.", Sa),
 ]),
 S("s-3", G, "write", 3, [
  W("Aspirinning gidrolizini yozing (H⁺ yoki namlik)", ["C9H8O4", "H2O"], ["C7H6O3", "C2H4O2"], "C9H8O4+H2O→C7H6O3+C2H4O2", "Aspirin namlikda salitsil va sirka kislotaga parchalanadi.", Sa),
  W("Aspiringa ortiqcha NaOH ta'sir ettiring (qizdirish)", ["C9H8O4", "NaOH"], ["C7H4Na2O3", "C2H3NaO2", "H2O"], "C9H8O4+3NaOH→C7H4Na2O3+C2H3NaO2+2H2O", "Karboksil neytrallanadi, efir gidrolizlanadi va fenol OH ham ishqor bilan tuz hosil qiladi.", Sa),
 ]),
 S("s-4", G, "choice", 2, [
  C("Salitsil kislotani FeCl₃ bilan tekshirsak nima kuzatiladi?", "Binafsha rang", ["Ko'k cho'kma", "Qizil cho'kma", "Rang o'zgarmaydi"], "Erkin fenol OH guruhi bor.", Sa, ("Rang o'zgarmaydi", "Fenol OH bor: FeCl₃ bilan binafsha rang beradi.")),
  C("Toza aspirin FeCl₃ bilan rang beradimi?", "Yo'q: fenol OH atsillangan", ["Ha, binafsha rang beradi", "Ha, qizil rang", "Ha, ko'k cho'kma"], "OH atsetil guruh bilan band: rang paydo bo'lsa, aspirin gidrolizlangan.", Sa, ("Ha, binafsha rang beradi", "Binafsha rang erkin fenol OH ga xos, aspirinda u yo'q.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4O", "C3H5NO", "C3H6O3", "C6H8O4"]}
cB = {"all": ["C6H5ONa", "C7H5NaO3", "C7H6O3", "C9H10O3"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (sirka aldegidga HCN)", ["C2H4O", "HCN"], ["C3H5NO"], "C2H4O+HCN→C3H5NO", "Siangidrin hosil bo'ladi.", Su, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (natriy fenolyatga CO₂)", ["C6H5ONa", "CO2"], ["C7H5NaO3"], "C6H5ONa+CO2→C7H5NaO3", "Natriy salitsilat hosil bo'ladi.", Sa, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (H⁺, suv)", ["C3H5NO", "H2O"], ["C3H6O3", "NH3"], "C3H5NO+2H2O→C3H6O3+NH3", "Nitril guruhi COOH ga gidrolizlanadi: sut kislota.", Su, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (HCl)", ["C7H5NaO3", "HCl"], ["C7H6O3", "NaCl"], "C7H5NaO3+HCl→C7H6O3+NaCl", "Salitsil kislota ozod bo'ladi.", Sa, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (degidratlanish)", ["C3H6O3"], ["C6H8O4", "H2O"], "2C3H6O3→C6H8O4+2H2O", "Ikki molekuladan halqali dieter: laktid.", Su, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (etanol, H₂SO₄)", ["C7H6O3", "C2H5OH"], ["C9H10O3", "H2O"], "C7H6O3+C2H5OH→C9H10O3+H2O", "Etil salitsilat hosil bo'ladi.", Sa, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(18, "Oksikarbon kislotalar", ["sut kislota", "salitsil kislota", "glikol kislota"], slots)
