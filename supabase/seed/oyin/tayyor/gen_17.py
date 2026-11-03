from lib import *
Sa, Ft, Su = ["sirka angidrid"], ["ftal angidrid"], ["suksinil angidrid"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Sirka kislotaning degidratlanishini yozing (P₂O₅): sirka angidrid olinadi", ["C2H4O2"], ["C4H6O3", "H2O"], "2C2H4O2→C4H6O3+H2O", "Ikki molekuladan bitta suv ajraladi.", Sa),
  W("Propion kislotaning degidratlanishini yozing (P₂O₅): propion angidrid olinadi", ["C3H6O2"], ["C6H10O3", "H2O"], "2C3H6O2→C6H10O3+H2O", "Ikki molekuladan bitta suv ajraladi.", None),
 ]),
 S("o-2", G, "write", 2, [
  W("Propionilxlorid va natriy propionat reaksiyasini yozing: propion angidrid", ["C3H5ClO", "C3H5NaO2"], ["C6H10O3", "NaCl"], "C3H5ClO+C3H5NaO2→C6H10O3+NaCl", "Xlorangidrid va karboksilat tuzi angidrid beradi.", None),
  W("Benzoilxlorid va natriy benzoat reaksiyasini yozing: benzoy angidrid", ["C7H5ClO", "C7H5NaO2"], ["C14H10O3", "NaCl"], "C7H5ClO+C7H5NaO2→C14H10O3+NaCl", "Aromatik angidrid hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Ftal kislotaning qizdirilganda angidridga aylanishini yozing", ["C8H6O4"], ["C8H4O3", "H2O"], "C8H6O4→C8H4O3+H2O", "Ikki qo'shni karboksil beshlik halqa hosil qiladi.", Ft),
  W("Naftalinning havo kislorodi bilan oksidlanishini yozing (V₂O₅): ftal angidrid hosil bo'ladi", ["C10H8", "O2"], ["C8H4O3", "CO2", "H2O"], "2C10H8+9O2→2C8H4O3+4CO2+4H2O", "Bitta halqa uzilib, ikki uglerod CO₂ ga ketadi.", Ft),
 ]),
 S("o-4", G, "write", 2, [
  W("Qahrabo kislotaning qizdirilganda angidridga aylanishini yozing", ["C4H6O4"], ["C4H4O3", "H2O"], "C4H6O4→C4H4O3+H2O", "Besh a'zoli halqa: suksinil angidrid.", Su),
  W("Malein kislotaning qizdirilganda angidridga aylanishini yozing", ["C4H4O4"], ["C4H2O3", "H2O"], "C4H4O4→C4H2O3+H2O", "Cis-izomer osongina halqa hosil qiladi.", None),
 ]),
 S("o-5", G, "choice", 1, [
  C("Sirka angidridning tuzilish formulasi qaysi?", "(CH₃CO)₂O", ["CH₃COOCH₃", "CH₃COCl", "(CH₃)₂O"], "Ikki atsil guruhi bitta kislorod orqali bog'langan.", Sa, ("CH₃COOCH₃", "Bu metil atsetat: murakkab efir.")),
  C("Karbon kislotalardan angidrid qanday hosil bo'ladi?", "Ikki molekuladan bitta suv ajralishi bilan", ["Bitta molekuladan CO₂ ajralishi bilan", "Oksidlanish bilan", "Qaytarilish bilan"], "2RCOOH → (RCO)₂O + H₂O.", Sa, ("Oksidlanish bilan", "Angidrid oksidlanish emas, suv ajralish mahsuloti.")),
 ]),
]
G = "Gidroliz"
slots += [
 S("g-1", G, "write", 1, [
  W("Sirka angidridning gidrolizini yozing", ["C4H6O3", "H2O"], ["C2H4O2"], "C4H6O3+H2O→2C2H4O2", "Angidrid suv bilan ikki molekula kislota beradi.", Sa),
  W("Propion angidridning gidrolizini yozing", ["C6H10O3", "H2O"], ["C3H6O2"], "C6H10O3+H2O→2C3H6O2", "Ikki molekula propion kislota hosil bo'ladi.", None),
 ]),
 S("g-2", G, "write", 1, [
  W("Ftal angidridning gidrolizini yozing", ["C8H4O3", "H2O"], ["C8H6O4"], "C8H4O3+H2O→C8H6O4", "Halqa ochilib ftal kislota hosil bo'ladi.", Ft),
  W("Suksinil angidridning gidrolizini yozing", ["C4H4O3", "H2O"], ["C4H6O4"], "C4H4O3+H2O→C4H6O4", "Halqa ochilib qahrabo kislota hosil bo'ladi.", Su),
 ]),
 S("g-3", G, "write", 2, [
  W("Sirka angidridga ortiqcha NaOH ta'sir ettiring", ["C4H6O3", "NaOH"], ["C2H3NaO2", "H2O"], "C4H6O3+2NaOH→2C2H3NaO2+H2O", "Ishqorda ikki molekula tuz hosil bo'ladi.", Sa),
  W("Ftal angidridga ortiqcha NaOH ta'sir ettiring", ["C8H4O3", "NaOH"], ["C8H4Na2O4", "H2O"], "C8H4O3+2NaOH→C8H4Na2O4+H2O", "Halqa ochilib dinatriy ftalat hosil bo'ladi.", Ft),
 ]),
 S("g-4", G, "choice", 2, [
  C("Sirka angidrid suv bilan reaksiyaga kirishsa, nima hosil bo'ladi?", "Ikki molekula sirka kislota", ["Aldegid", "Efir", "Spirt"], "Angidrid gidrolizi kislota beradi.", Sa, ("Efir", "Efir spirt bilan reaksiyada hosil bo'ladi, suv bilan emas.")),
  C("Ftal angidrid gidrolizi mahsuloti qaysi?", "Ftal kislota", ["Benzoy kislota", "Izoftal kislota", "Salitsil kislota"], "Halqa ochilib ikki COOH guruhi hosil bo'ladi.", Ft, ("Benzoy kislota", "Benzoy kislotada bitta COOH bor, ftalda ikkita.")),
 ]),
]
G = "Alkogoliz"
slots += [
 S("a-1", G, "write", 2, [
  W("Sirka angidridga etanol ta'sir ettiring", ["C4H6O3", "C2H5OH"], ["C4H8O2", "C2H4O2"], "C4H6O3+C2H5OH→C4H8O2+C2H4O2", "Efir va bitta molekula kislota hosil bo'ladi.", Sa),
  W("Sirka angidridga metanol ta'sir ettiring", ["C4H6O3", "CH3OH"], ["C3H6O2", "C2H4O2"], "C4H6O3+CH3OH→C3H6O2+C2H4O2", "Metil atsetat va sirka kislota hosil bo'ladi.", Sa),
 ]),
 S("a-2", G, "write", 2, [
  W("Ftal angidridga 1 mol metanol ta'sir ettiring", ["C8H4O3", "CH3OH"], ["C9H8O4"], "C8H4O3+CH3OH→C9H8O4", "Halqa ochilib monoefir (kislota-efir) hosil bo'ladi.", Ft),
  W("Suksinil angidridga 1 mol etanol ta'sir ettiring", ["C4H4O3", "C2H5OH"], ["C6H10O4"], "C4H4O3+C2H5OH→C6H10O4", "Monoetil suksinat hosil bo'ladi.", Su),
 ]),
 S("a-3", G, "write", 3, [
  W("Ftal angidrid va ortiqcha butanol reaksiyasini yozing (H₂SO₄): dibutilftalat", ["C8H4O3", "C4H9OH"], ["C16H22O4", "H2O"], "C8H4O3+2C4H9OH→C16H22O4+H2O", "Ikkala karboksil esterlanadi: plastifikator.", Ft),
  W("Malein angidrid va ortiqcha etanol reaksiyasini yozing (H₂SO₄)", ["C4H2O3", "C2H5OH"], ["C8H12O4", "H2O"], "C4H2O3+2C2H5OH→C8H12O4+H2O", "Dietil maleat hosil bo'ladi.", None),
 ]),
 S("a-4", G, "choice", 2, [
  C("Sirka angidrid etanol bilan reaksiyaga kirishganda qanday moddalar hosil bo'ladi?", "Etil atsetat va sirka kislota", ["Etil atsetat va suv", "Etilen va sirka kislota", "Dietil efir"], "Suv ajralmaydi: ikkinchi atsil guruhi kislota bo'lib qoladi.", Sa, ("Etil atsetat va suv", "Suv eterifikatsiyada ajraladi, angidrid alkogolizida esa sirka kislota hosil bo'ladi.")),
  C("Ftal angidrid va spirtlardan qanday sanoat moddasi olinadi?", "Dialkilftalat (plastifikator)", ["Polietilen", "Kapron", "Neylon"], "Plastmassalarga elastiklik beradi.", Ft, ("Kapron", "Kapron kaprolaktamdan olinadi.")),
 ]),
]
G = "Ammonoliz"
slots += [
 S("m-1", G, "write", 2, [
  W("Sirka angidridga ammiak ta'sir ettiring", ["C4H6O3", "NH3"], ["C2H5NO", "C2H4O2"], "C4H6O3+NH3→C2H5NO+C2H4O2", "Asetamid va sirka kislota hosil bo'ladi.", Sa),
  W("Propion angidridga ammiak ta'sir ettiring", ["C6H10O3", "NH3"], ["C3H7NO", "C3H6O2"], "C6H10O3+NH3→C3H7NO+C3H6O2", "Propionamid va propion kislota hosil bo'ladi.", None),
 ]),
 S("m-2", G, "write", 2, [
  W("Ftal angidridga ammiak ta'sir ettiring (sovuqda)", ["C8H4O3", "NH3"], ["C8H7NO3"], "C8H4O3+NH3→C8H7NO3", "Halqa ochilib ftalamid kislota hosil bo'ladi.", Ft),
  W("Malein angidridga ammiak ta'sir ettiring (sovuqda)", ["C4H2O3", "NH3"], ["C4H5NO3"], "C4H2O3+NH3→C4H5NO3", "Maleamid kislota hosil bo'ladi.", None),
 ]),
 S("m-3", G, "write", 3, [
  W("Ftal angidrid va ammiakni qizdiring: ftalimid hosil bo'ladi", ["C8H4O3", "NH3"], ["C8H5NO2", "H2O"], "C8H4O3+NH3→C8H5NO2+H2O", "Halqa yopiladi, suv ajraladi.", Ft),
  W("Suksinil angidrid va ammiakni qizdiring: suksinimid hosil bo'ladi", ["C4H4O3", "NH3"], ["C4H5NO2", "H2O"], "C4H4O3+NH3→C4H5NO2+H2O", "Imid hosil bo'ladi, suv ajraladi.", Su),
 ]),
 S("m-4", G, "write", 3, [
  W("Sirka angidridga anilin ta'sir ettiring: atsetanilid hosil bo'ladi", ["C4H6O3", "C6H7N"], ["C8H9NO", "C2H4O2"], "C4H6O3+C6H7N→C8H9NO+C2H4O2", "Aminoguruh atsillanadi.", Sa),
  W("Sirka angidridga metilamin ta'sir ettiring", ["C4H6O3", "CH5N"], ["C3H7NO", "C2H4O2"], "C4H6O3+CH5N→C3H7NO+C2H4O2", "N-metilatsetamid hosil bo'ladi.", Sa),
 ]),
]
G = "Atsillash"
slots += [
 S("f-1", G, "write", 2, [
  W("Fenolga sirka angidrid ta'sir ettiring", ["C6H5OH", "C4H6O3"], ["C8H8O2", "C2H4O2"], "C6H5OH+C4H6O3→C8H8O2+C2H4O2", "Fenilatsetat va sirka kislota hosil bo'ladi.", Sa),
  W("Salitsil kislotaga sirka angidrid ta'sir ettiring: aspirin olinadi", ["C7H6O3", "C4H6O3"], ["C9H8O4", "C2H4O2"], "C7H6O3+C4H6O3→C9H8O4+C2H4O2", "OH guruhi atsillanadi: atsetilsalitsil kislota.", Sa),
 ]),
 S("f-2", G, "write", 3, [
  W("Benzolga sirka angidrid ta'sir ettiring (AlCl₃, Fridel–Krafts)", ["C6H6", "C4H6O3"], ["C8H8O", "C2H4O2"], "C6H6+C4H6O3→C8H8O+C2H4O2", "Atsetofenon hosil bo'ladi: halqaga atsil guruhi birikadi.", Sa),
  W("Benzolga ftal angidrid ta'sir ettiring (AlCl₃)", ["C6H6", "C8H4O3"], ["C14H10O3"], "C6H6+C8H4O3→C14H10O3", "o-benzoilbenzoy kislota hosil bo'ladi.", Ft),
 ]),
 S("f-3", G, "write", 2, [
  W("Glitserin va ortiqcha sirka angidrid reaksiyasini yozing", ["C3H8O3", "C4H6O3"], ["C9H14O6", "C2H4O2"], "C3H8O3+3C4H6O3→C9H14O6+3C2H4O2", "Triatsetin hosil bo'ladi.", Sa),
  W("Etilenglikol va ortiqcha sirka angidrid reaksiyasini yozing", ["C2H6O2", "C4H6O3"], ["C6H10O4", "C2H4O2"], "C2H6O2+2C4H6O3→C6H10O4+2C2H4O2", "Glikol diatsetat hosil bo'ladi.", Sa),
 ]),
 S("f-4", G, "choice", 2, [
  C("Aspirinni olishning usuli qaysi?", "Salitsil kislotani sirka angidrid bilan atsillash", ["Fenolni CO₂ bilan reaksiyasi", "Benzoy kislotani oksidlash", "Anilinni nitrolash"], "OH guruhi atsetil guruhiga almashinadi.", Sa, ("Fenolni CO₂ bilan reaksiyasi", "Bu salitsil kislota olish usuli (Kolbe), aspirin emas.")),
  C("Atsillash nima?", "Molekulaga atsil guruhi (RCO–) kiritish", ["Vodorod ajratish", "Kislorod qo'shish", "Halqani ochish"], "Angidridlar va xlorangidridlar atsillovchi reagentlardir.", Sa, ("Vodorod ajratish", "Bu degidrogenlash.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C2H4O2", "C2H3ClO", "C4H6O3", "C2H3ClO"]}
cB = {"all": ["C8H10", "C8H4O3", "C8H4K2O4", "C8H6O4"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (PCl₃)", ["C2H4O2", "PCl3"], ["C2H3ClO", "H3PO3"], "3C2H4O2+PCl3→3C2H3ClO+H3PO3", "Sirka kislota atsetilxloridga aylanadi.", Sa, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (V₂O₅, 400 °C)", ["C8H10", "O2"], ["C8H4O3", "H2O"], "C8H10+3O2→C8H4O3+3H2O", "o-ksilol oksidlanib ftal angidrid beradi.", Ft, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing", ["C2H3ClO", "C2H3NaO2"], ["C4H6O3", "NaCl"], "C2H3ClO+C2H3NaO2→C4H6O3+NaCl", "Atsetilxlorid va natriy atsetat sirka angidrid beradi.", Sa, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (ortiqcha KOH)", ["C8H4O3", "KOH"], ["C8H4K2O4", "H2O"], "C8H4O3+2KOH→C8H4K2O4+H2O", "Halqa ochilib dikaliy ftalat hosil bo'ladi.", Ft, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (PCl₅)", ["C4H6O3", "PCl5"], ["C2H3ClO", "POCl3"], "C4H6O3+PCl5→2C2H3ClO+POCl3", "Angidrid PCl₅ ta'sirida atsetilxloridga qaytadi.", Sa, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (HCl)", ["C8H4K2O4", "HCl"], ["C8H6O4", "KCl"], "C8H4K2O4+2HCl→C8H6O4+2KCl", "Kuchli kislota ftal kislotani ozod qiladi.", Ft, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(17, "Angidridlar", ["sirka angidrid", "ftal angidrid", "suksinil angidrid"], slots)
