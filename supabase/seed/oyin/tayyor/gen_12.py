from lib import *
F, K = ["fenol"], ["krezol"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Brombenzolga NaOH ta'sir ettiring (yuqori harorat va bosim)", ["C6H5Br", "NaOH"], ["C6H5ONa", "NaBr", "H2O"], "C6H5Br+2NaOH→C6H5ONa+NaBr+H2O", "Brom OH ga almashinadi, ortiqcha ishqor fenolni natriy fenolyatga aylantiradi.", F),
  W("Natriy fenolyatga xlorid kislota ta'sir ettiring", ["C6H5ONa", "HCl"], ["C6H5OH", "NaCl"], "C6H5ONa+HCl→C6H5OH+NaCl", "Kuchli kislota fenolyatdan fenolni siqib chiqaradi.", F),
 ]),
 S("o-2", G, "write", 2, [
  W("Kumolning havo kislorodi bilan oksidlanishini yozing (kumol gidroperoksid hosil bo'ladi)", ["C9H12", "O2"], ["C9H12O2"], "C9H12+O2→C9H12O2", "Kumol usulining birinchi bosqichi.", F),
  W("Kumol gidroperoksidning kislotali parchalanishini yozing (fenol va aseton)", ["C9H12O2"], ["C6H6O", "C3H6O"], "C9H12O2→C6H6O+C3H6O", "Kumol usulining ikkinchi bosqichi: fenol va aseton.", F),
 ]),
 S("o-3", G, "write", 2, [
  W("Natriy benzolsulfonatni NaOH bilan eritish: fenolyat hosil bo'ladi", ["C6H5NaO3S", "NaOH"], ["C6H5NaO", "Na2SO3", "H2O"], "C6H5NaO3S+2NaOH→C6H5NaO+Na2SO3+H2O", "Sulfo guruh OH ga almashinadi (qizdirib eritish).", F),
  W("Natriy toluolsulfonatni NaOH bilan eritish: krezolyat hosil bo'ladi", ["C7H7NaO3S", "NaOH"], ["C7H7NaO", "Na2SO3", "H2O"], "C7H7NaO3S+2NaOH→C7H7NaO+Na2SO3+H2O", "Sulfo guruh OH ga almashinadi.", K),
 ]),
 S("o-4", G, "write", 3, [
  W("Anilinga nitrit kislota ta'sir ettiring (qizdirish): fenol hosil bo'ladi", ["C6H7N", "HNO2"], ["C6H6O", "N2", "H2O"], "C6H7N+HNO2→C6H6O+N2+H2O", "Diazoniy tuzi suv bilan parchalanib fenol beradi.", F),
  W("Toluidinga nitrit kislota ta'sir ettiring (qizdirish): krezol hosil bo'ladi", ["C7H9N", "HNO2"], ["C7H8O", "N2", "H2O"], "C7H9N+HNO2→C7H8O+N2+H2O", "Azot gaz holida ajraladi.", K),
 ]),
 S("o-5", G, "choice", 1, [
  C("Sanoatda fenol olishning asosiy usuli qaysi?", "Kumol usuli", ["Gidratlash", "Bijg'ish", "Vyurs reaksiyasi"], "Kumol havo bilan oksidlanib, keyin fenol va aseton beradi.", F),
  C("Kumol usulida fenol bilan birga qaysi modda hosil bo'ladi?", "Aseton", ["Sirka kislota", "Metanol", "Formaldegid"], "Kumol gidroperoksid fenol va asetonga parchalanadi.", F, ("Sirka kislota", "Qo'shimcha mahsulot aseton.")),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Fenolga xlormetan ta'sir ettiring (AlCl₃): krezol hosil bo'ladi", ["C6H5OH", "CH3Cl"], ["C7H8O", "HCl"], "C6H5OH+CH3Cl→C7H8O+HCl", "Metil guruh halqaga (o- yoki p-) birikadi.", K),
  W("Fenolga xloretan ta'sir ettiring (AlCl₃)", ["C6H5OH", "C2H5Cl"], ["C8H10O", "HCl"], "C6H5OH+C2H5Cl→C8H10O+HCl", "Etil guruh halqaga birikadi: etilfenol.", F),
 ]),
 S("x-2", G, "choice", 1, [
  C("Fenolning formulasi qaysi?", "C₆H₅OH", ["C₆H₅CH₂OH", "C₆H₁₁OH", "C₆H₅CH₃"], "OH guruhi bevosita benzol halqasiga birikkan.", F, ("C₆H₅CH₂OH", "Bu benzil spirt: OH yon zanjirda.")),
  C("Krezolning tuzilishi qaysi?", "CH₃–C₆H₄–OH", ["C₆H₅–CH₂OH", "C₆H₅–O–CH₃", "C₆H₅–C₂H₅"], "Metilfenol: halqada CH₃ va OH.", K, ("C₆H₅–CH₂OH", "Benzil spirtda OH yon zanjirda.")),
 ]),
 S("x-3", G, "choice", 3, [
  C("Fenol benzil spirtdan nimasi bilan farq qiladi?", "OH guruhi to'g'ridan-to'g'ri benzol halqasida", ["OH guruhi yon zanjirda", "Fenolda OH guruhi yo'q", "Benzil spirt NaOH bilan reaksiyaga kirishadi"], "Shu sababli fenol kislotali xossa ko'rsatadi.", F, ("OH guruhi yon zanjirda", "OH yon zanjirda bo'lsa, bu benzil spirt.")),
  C("Fenol NaOH eritmasi bilan reaksiyaga kirishadi. Bu nimani ko'rsatadi?", "Fenol kuchsiz kislota", ["Fenol ishqor", "Fenol neytral", "Fenol efir"], "Benzol halqasi OH dagi vodorodni harakatchan qiladi.", F),
 ]),
]
G = "OH hisobiga reaksiyalar"
slots += [
 S("m-1", G, "write", 1, [
  W("Fenolga natriy ta'sir ettiring", ["C6H5OH", "Na"], ["C6H5ONa", "H2"], "2C6H5OH+2Na→2C6H5ONa+H2", "Natriy fenolyat va vodorod hosil bo'ladi.", F),
  W("Krezolga natriy ta'sir ettiring", ["C7H8O", "Na"], ["C7H7NaO", "H2"], "2C7H8O+2Na→2C7H7NaO+H2", "Natriy krezolyat va vodorod hosil bo'ladi.", K),
 ]),
 S("m-2", G, "write", 1, [
  W("Fenolga NaOH eritmasi ta'sir ettiring", ["C6H5OH", "NaOH"], ["C6H5ONa", "H2O"], "C6H5OH+NaOH→C6H5ONa+H2O", "Fenol kuchsiz kislota: ishqor bilan tuz hosil qiladi.", F),
  W("Krezolga KOH eritmasi ta'sir ettiring", ["C7H8O", "KOH"], ["C7H7KO", "H2O"], "C7H8O+KOH→C7H7KO+H2O", "Kaliy krezolyat hosil bo'ladi.", K),
 ]),
 S("m-3", G, "write", 2, [
  W("Natriy fenolyatga CO₂ va suv ta'sir ettiring", ["C6H5ONa", "CO2", "H2O"], ["C6H5OH", "NaHCO3"], "C6H5ONa+CO2+H2O→C6H5OH+NaHCO3", "Karbonat kislota fenoldan kuchli: fenolni siqib chiqaradi.", F),
  W("Natriy fenolyatga sulfat kislota ta'sir ettiring", ["C6H5ONa", "H2SO4"], ["C6H5OH", "Na2SO4"], "2C6H5ONa+H2SO4→2C6H5OH+Na2SO4", "Kuchli kislota fenolni siqib chiqaradi.", F),
 ]),
 S("m-4", G, "write", 3, [
  W("Fenolga sirka angidrid ta'sir ettiring (atsillash)", ["C6H5OH", "C4H6O3"], ["C8H8O2", "C2H4O2"], "C6H5OH+C4H6O3→C8H8O2+C2H4O2", "Fenilatsetat va sirka kislota hosil bo'ladi.", F),
  W("Fenolga atsetilxlorid ta'sir ettiring", ["C6H5OH", "CH3COCl"], ["C8H8O2", "HCl"], "C6H5OH+CH3COCl→C8H8O2+HCl", "Fenilatsetat hosil bo'ladi, HCl ajraladi.", F),
 ]),
 S("m-5", G, "choice", 2, [
  C("Fenolning kislotaliligi qanday?", "H₂CO₃ dan kuchsiz, H₂O dan kuchli", ["H₂CO₃ dan kuchli", "Suvdan kuchsiz", "Sirka kislotadan kuchli"], "Fenol ishqor bilan reaksiyaga kirishadi, lekin karbonat kislota fenolyatdan fenolni chiqaradi.", F, ("H₂CO₃ dan kuchli", "Aksincha: CO₂ + suv fenolyatdan fenolni siqib chiqaradi.")),
  C("Natriy fenolyat suvda eritilsa, muhit qanday bo'ladi?", "Ishqoriy (gidroliz)", ["Neytral", "Kislotali", "Gaz ajraladi"], "Kuchsiz kislota tuzi gidrolizlanib ishqoriy muhit beradi.", F, ("Neytral", "Kuchsiz kislota tuzi gidrolizlanadi, muhit ishqoriy.")),
 ]),
]
G = "Benzol halqasiga xos reaksiyalar"
slots += [
 S("b-1", G, "write", 2, [
  W("Fenolga ortiqcha bromli suv ta'sir ettiring", ["C6H5OH", "Br2"], ["C6H3Br3O", "HBr"], "C6H5OH+3Br2→C6H3Br3O+3HBr", "Brom 2, 4, 6 holatlarga birikadi: oq cho'kma.", F),
  W("Krezolga ortiqcha bromli suv ta'sir ettiring", ["C7H8O", "Br2"], ["C7H5Br3O", "HBr"], "C7H8O+3Br2→C7H5Br3O+3HBr", "Uch vodorod bromga almashinadi.", K),
 ]),
 S("b-2", G, "write", 2, [
  W("Fenolni to'liq nitrolang (konsentrlangan HNO₃, H₂SO₄): pikrin kislota", ["C6H5OH", "HNO3"], ["C6H3N3O7", "H2O"], "C6H5OH+3HNO3→C6H3N3O7+3H2O", "2, 4, 6-trinitrofenol (pikrin kislota).", F),
  W("Fenolni mononitrolang (suyultirilgan HNO₃)", ["C6H5OH", "HNO3"], ["C6H5NO3", "H2O"], "C6H5OH+HNO3→C6H5NO3+H2O", "o- va p-nitrofenol hosil bo'ladi.", F),
 ]),
 S("b-3", G, "write", 2, [
  W("Fenolni gidrogenlang (Ni, qizdirish)", ["C6H5OH", "H2"], ["C6H12O"], "C6H5OH+3H2→C6H12O", "Halqa to'yinadi: siklogeksanol.", F),
  W("Krezolni gidrogenlang (Ni, qizdirish)", ["C7H8O", "H2"], ["C7H14O"], "C7H8O+3H2→C7H14O", "Metilsiklogeksanol hosil bo'ladi.", K),
 ]),
 S("b-4", G, "write", 3, [
  W("Fenol va formaldegid reaksiyasini yozing (birinchi bosqich, H⁺ yoki OH⁻)", ["C6H5OH", "CH2O"], ["C7H8O2"], "C6H5OH+CH2O→C7H8O2", "o-gidroksimetilfenol: fenolformaldegid smolasi boshlanishi.", F),
  W("Ikki molekula fenol va formaldegid reaksiyasini yozing (suv ajraladi)", ["C6H5OH", "CH2O"], ["C13H12O2", "H2O"], "2C6H5OH+CH2O→C13H12O2+H2O", "Dioksidifenilmetan hosil bo'ladi: polikondensatsiya zanjiri.", F),
 ]),
 S("b-5", G, "choice", 2, [
  C("Fenolni aniqlash uchun qaysi reaktiv ishlatiladi?", "FeCl₃ (binafsha rang)", ["Cu(OH)₂ (ko'k eritma)", "AgNO₃ ning ammiakli eritmasi", "KMnO₄ ning rangsizlanishi"], "Fenollar FeCl₃ bilan binafsha kompleks hosil qiladi.", F, ("Cu(OH)₂ (ko'k eritma)", "Cu(OH)₂ ko'p atomli spirtlar uchun.")),
  C("Fenolga bromli suv ta'sir ettirilsa, nima kuzatiladi?", "Oq cho'kma (2,4,6-tribromfenol)", ["Sariq cho'kma", "Rang o'zgarmaydi", "Binafsha rang"], "Uch brom birikib, suvda erimaydigan oq modda hosil bo'ladi.", F, ("Binafsha rang", "Binafsha rang FeCl₃ bilan hosil bo'ladi.")),
 ]),
 S("b-6", G, "choice", 3, [
  C("Fenol bromli suv bilan reaksiyaga kirishganda nechta vodorod bromga almashadi?", "3", ["1", "2", "4"], "OH guruhi o,p-yo'naltiruvchi: 2, 4 va 6 holatlar.", F, ("2", "Ikkita o-holat va bitta p-holat: jami uchta.")),
  C("Fenoldagi OH guruhi qaysi turdagi o'rinbosar?", "Birinchi tur (orto-, para-yo'naltiruvchi)", ["Ikkinchi tur (meta-)", "Yo'naltirmaydi", "Faqat meta-yo'naltiruvchi"], "Elektron beruvchi guruh o va p holatlarni faollashtiradi.", F, ("Ikkinchi tur (meta-)", "OH elektron beradi, shuning uchun o,p-yo'naltiruvchi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Fenolning to'liq yonishini yozing", ["C6H5OH", "O2"], ["CO2", "H2O"], "C6H5OH+7O2→6CO2+3H2O", "Kislorod: 12 + 3 − 1 = 14 atom, ya'ni 7 O₂.", F),
  W("Krezolning to'liq yonishini yozing", ["C7H8O", "O2"], ["CO2", "H2O"], "2C7H8O+17O2→14CO2+8H2O", "Kasr chiqmasligi uchun ikki baravar.", K),
 ]),
 S("k-2", G, "choice", 3, [
  C("Fenol uzoq vaqt havoda turganda rangi qanday o'zgaradi?", "Pushti-qo'ng'ir tusga kiradi (oksidlanadi)", ["Rangsiz qoladi", "Ko'k bo'ladi", "Qorayadi va qotadi"], "Fenol havo kislorodi ta'sirida asta oksidlanadi.", F),
  C("Fenol KMnO₄ eritmasini rangsizlantiradimi?", "Ha: oson oksidlanadi", ["Yo'q", "Faqat sovuqda", "Faqat ishqoriy muhitda"], "OH guruhi halqani faollashtiradi, fenol benzoldan osonroq oksidlanadi.", F, ("Yo'q", "Benzol rangsizlantirmaydi, fenol esa oson oksidlanadi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H6", "C6H5Cl", "C6H5ONa", "C6H5OH"]}
cB = {"all": ["C6H6", "C6H6O3S", "C6H5ONa", "C7H8O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (FeCl₃)", ["C6H6", "Cl2"], ["C6H5Cl", "HCl"], "C6H6+Cl2→C6H5Cl+HCl", "Vodorod xlorga almashinadi.", F, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (konsentrlangan H₂SO₄)", ["C6H6", "H2SO4"], ["C6H6O3S", "H2O"], "C6H6+H2SO4→C6H6O3S+H2O", "Benzolsulfokislota hosil bo'ladi.", F, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (NaOH, yuqori harorat va bosim)", ["C6H5Cl", "NaOH"], ["C6H5ONa", "NaCl", "H2O"], "C6H5Cl+2NaOH→C6H5ONa+NaCl+H2O", "Xlor OH ga almashinadi, fenolyat hosil bo'ladi.", F, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (NaOH bilan eritish)", ["C6H6O3S", "NaOH"], ["C6H5NaO", "Na2SO3", "H2O"], "C6H6O3S+3NaOH→C6H5NaO+Na2SO3+2H2O", "Sulfokislota ishqor bilan fenolyat beradi.", F, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (suv ta'sirida gidroliz)", ["C6H5ONa", "H2O"], ["C6H5OH", "NaOH"], "C6H5ONa+H2O→C6H5OH+NaOH", "Fenolyat gidrolizlanib fenol hosil qiladi.", F, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (yodmetan bilan)", ["C6H5ONa", "CH3I"], ["C7H8O", "NaI"], "C6H5ONa+CH3I→C7H8O+NaI", "Anizol (metilfenil efir) hosil bo'ladi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(12, "Fenollar", ["fenol", "krezol"], slots)
