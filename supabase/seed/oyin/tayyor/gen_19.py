from lib import *
Ea, Ma, Mf = ["etil atsetat"], ["metil atsetat"], ["metil formiat"]
slots = []
G = "Olinish (eterifikatsiya)"
slots += [
 S("o-1", G, "write", 1, [
  W("Sirka kislota va etanol reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["C2H4O2", "C2H5OH"], ["C4H8O2", "H2O"], "C2H4O2+C2H5OH→C4H8O2+H2O", "Etil atsetat va suv hosil bo'ladi.", Ea),
  W("Chumoli kislota va metanol reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["CH2O2", "CH3OH"], ["C2H4O2", "H2O"], "CH2O2+CH3OH→C2H4O2+H2O", "Metil formiat hosil bo'ladi.", Mf),
 ]),
 S("o-2", G, "write", 1, [
  W("Sirka kislota va metanol reaksiyasini yozing (H₂SO₄)", ["C2H4O2", "CH3OH"], ["C3H6O2", "H2O"], "C2H4O2+CH3OH→C3H6O2+H2O", "Metil atsetat hosil bo'ladi.", Ma),
  W("Chumoli kislota va etanol reaksiyasini yozing (H₂SO₄)", ["CH2O2", "C2H5OH"], ["C3H6O2", "H2O"], "CH2O2+C2H5OH→C3H6O2+H2O", "Etil formiat hosil bo'ladi.", None),
 ]),
 S("o-3", G, "write", 2, [
  W("Atsetilxlorid va etanol reaksiyasini yozing", ["C2H3ClO", "C2H5OH"], ["C4H8O2", "HCl"], "C2H3ClO+C2H5OH→C4H8O2+HCl", "Xlorangidrid spirt bilan tez efir hosil qiladi.", Ea),
  W("Atsetilxlorid va metanol reaksiyasini yozing", ["C2H3ClO", "CH3OH"], ["C3H6O2", "HCl"], "C2H3ClO+CH3OH→C3H6O2+HCl", "Metil atsetat va HCl hosil bo'ladi.", Ma),
 ]),
 S("o-4", G, "write", 2, [
  W("Sirka angidrid va etanol reaksiyasini yozing", ["C4H6O3", "C2H5OH"], ["C4H8O2", "C2H4O2"], "C4H6O3+C2H5OH→C4H8O2+C2H4O2", "Efir va bitta molekula sirka kislota hosil bo'ladi.", Ea),
  W("Natriy atsetat va bromoetan reaksiyasini yozing", ["C2H3NaO2", "C2H5Br"], ["C4H8O2", "NaBr"], "C2H3NaO2+C2H5Br→C4H8O2+NaBr", "Karboksilat galogenalkandagi galogenni almashtiradi.", Ea),
 ]),
 S("o-5", G, "write", 3, [
  W("Sirka aldegidning Tishchenko reaksiyasini yozing (Al(OC₂H₅)₃)", ["C2H4O"], ["C4H8O2"], "2C2H4O→C4H8O2", "Ikki aldegid molekulasi bitta efirga birlashadi.", Ea),
  W("Formaldegidning Tishchenko reaksiyasini yozing (katalizator)", ["CH2O"], ["C2H4O2"], "2CH2O→C2H4O2", "Metil formiat hosil bo'ladi.", Mf),
 ]),
 S("o-6", G, "choice", 1, [
  C("Eterifikatsiya reaksiyasida qaysi katalizator ishlatiladi?", "Konsentrlangan H₂SO₄", ["NaOH", "Ni", "KMnO₄"], "Kislota protonlari karbonilni faollashtiradi.", Ea, ("NaOH", "Ishqor efirni gidrolizlaydi, hosil qilmaydi.")),
  C("Eterifikatsiya muvozanatini efir tomon siljitish uchun nima qilinadi?", "Suvni chiqarib yuboriladi yoki spirt ortiqcha olinadi", ["Harorat keskin tushiriladi", "Bosim pasaytiriladi", "Katalizator olib tashlanadi"], "Le Shatelye prinsipi: mahsulot chiqarib turilsa muvozanat o'ngga siljiydi.", Ea, ("Katalizator olib tashlanadi", "Katalizator muvozanatni siljitmaydi, faqat tezlashtiradi.")),
 ]),
]
G = "Gidrolizlanish"
slots += [
 S("g-1", G, "write", 1, [
  W("Propil atsetatning gidrolizini yozing (H⁺)", ["C5H10O2", "H2O"], ["C2H4O2", "C3H8O"], "C5H10O2+H2O→C2H4O2+C3H8O", "Efir kislota va spirtga gidrolizlanadi.", None),
  W("Metil propionatning gidrolizini yozing (H⁺)", ["C4H8O2", "H2O"], ["C3H6O2", "CH3OH"], "C4H8O2+H2O→C3H6O2+CH3OH", "Propion kislota va metanol hosil bo'ladi.", None),
 ]),
 S("g-2", G, "write", 2, [
  W("Etil atsetatga NaOH ta'sir ettiring (qizdirish)", ["C4H8O2", "NaOH"], ["C2H3NaO2", "C2H5OH"], "C4H8O2+NaOH→C2H3NaO2+C2H5OH", "Ishqoriy gidroliz qaytmas: tuz va spirt.", Ea),
  W("Metil formiatga NaOH ta'sir ettiring (qizdirish)", ["C2H4O2", "NaOH"], ["CHNaO2", "CH3OH"], "C2H4O2+NaOH→CHNaO2+CH3OH", "Natriy formiat va metanol hosil bo'ladi.", Mf),
 ]),
 S("g-3", G, "write", 2, [
  W("Metil atsetatga KOH ta'sir ettiring (qizdirish)", ["C3H6O2", "KOH"], ["C2H3KO2", "CH3OH"], "C3H6O2+KOH→C2H3KO2+CH3OH", "Kaliy atsetat va metanol hosil bo'ladi.", Ma),
  W("Etil formiatga NaOH ta'sir ettiring (qizdirish)", ["C3H6O2", "NaOH"], ["CHNaO2", "C2H5OH"], "C3H6O2+NaOH→CHNaO2+C2H5OH", "Natriy formiat va etanol hosil bo'ladi.", None),
 ]),
 S("g-4", G, "write", 3, [
  W("Vinil atsetatga NaOH ta'sir ettiring", ["C4H6O2", "NaOH"], ["C2H3NaO2", "C2H4O"], "C4H6O2+NaOH→C2H3NaO2+C2H4O", "Hosil bo'lgan vinil spirt sirka aldegidga o'tadi.", None),
  W("Fenil atsetatga ortiqcha NaOH ta'sir ettiring", ["C8H8O2", "NaOH"], ["C2H3NaO2", "C6H5ONa", "H2O"], "C8H8O2+2NaOH→C2H3NaO2+C6H5ONa+H2O", "Fenol ishqor bilan tuz hosil qiladi: ikki ekvivalent NaOH kerak.", None),
 ]),
 S("g-5", G, "choice", 2, [
  C("Murakkab efirning ishqoriy gidrolizi qanday ataladi?", "Sovunlanish", ["Eterifikatsiya", "Gidrogenlash", "Polimerlanish"], "Yog'larning ishqoriy gidrolizi sovun beradi.", Ea, ("Eterifikatsiya", "Eterifikatsiya efir hosil bo'lish reaksiyasi, gidroliz teskari.")),
  C("Murakkab efirning kislotali gidrolizi qanday xususiyatga ega?", "Qaytar reaksiya", ["Qaytmas reaksiya", "Faqat qizdirilganda boradi", "Portlash bilan boradi"], "Kislota katalizator: muvozanat holati o'rnatiladi.", Ea, ("Qaytmas reaksiya", "Qaytmas bo'lgani ishqoriy gidroliz.")),
 ]),
]
G = "Alkogoliz va ammonoliz"
slots += [
 S("a-1", G, "write", 2, [
  W("Etil atsetatga metanol ta'sir ettiring (transeterifikatsiya)", ["C4H8O2", "CH3OH"], ["C3H6O2", "C2H5OH"], "C4H8O2+CH3OH→C3H6O2+C2H5OH", "Spirt radikali almashadi.", Ea),
  W("Metil formiatga etanol ta'sir ettiring (transeterifikatsiya)", ["C2H4O2", "C2H5OH"], ["C3H6O2", "CH3OH"], "C2H4O2+C2H5OH→C3H6O2+CH3OH", "Etil formiat va metanol hosil bo'ladi.", Mf),
 ]),
 S("a-2", G, "write", 2, [
  W("Etil atsetatga ammiak ta'sir ettiring", ["C4H8O2", "NH3"], ["C2H5NO", "C2H5OH"], "C4H8O2+NH3→C2H5NO+C2H5OH", "Atsetamid va etanol hosil bo'ladi.", Ea),
  W("Metil atsetatga ammiak ta'sir ettiring", ["C3H6O2", "NH3"], ["C2H5NO", "CH3OH"], "C3H6O2+NH3→C2H5NO+CH3OH", "Atsetamid va metanol hosil bo'ladi.", Ma),
 ]),
 S("a-3", G, "write", 3, [
  W("Etil atsetatga metilamin ta'sir ettiring", ["C4H8O2", "CH5N"], ["C3H7NO", "C2H5OH"], "C4H8O2+CH5N→C3H7NO+C2H5OH", "N-metilatsetamid hosil bo'ladi.", Ea),
  W("Etil atsetatga gidrazin ta'sir ettiring", ["C4H8O2", "N2H4"], ["C2H6N2O", "C2H5OH"], "C4H8O2+N2H4→C2H6N2O+C2H5OH", "Atsetgidrazid hosil bo'ladi.", Ea),
 ]),
 S("a-4", G, "choice", 2, [
  C("Murakkab efir ammiak bilan reaksiyaga kirishsa, qanday mahsulotlar hosil bo'ladi?", "Amid va spirt", ["Amin va kislota", "Nitril va suv", "Tuz va spirt"], "OR guruhi NH₂ ga almashinadi.", Ea, ("Tuz va spirt", "Tuz ishqor bilan gidrolizda hosil bo'ladi, ammiak bilan amid.")),
  C("Transeterifikatsiya nima?", "Efir va spirt reaksiyasi: spirt radikali almashadi", ["Efirning suv bilan parchalanishi", "Efirning gidrogenlanishi", "Efirning polimerlanishi"], "Boshqa spirt bilan yangi efir olinadi.", Ea, ("Efirning suv bilan parchalanishi", "Bu gidroliz, transeterifikatsiya esa spirt bilan.")),
 ]),
]
G = "Grinyar reaktivi"
slots += [
 S("m-1", G, "write", 3, [
  W("Etil atsetatga ortiqcha metilmagniy bromid ta'sir ettiring", ["C4H8O2", "CH3MgBr"], ["C4H9BrMgO", "C2H5BrMgO"], "C4H8O2+2CH3MgBr→C4H9BrMgO+C2H5BrMgO", "Ikki molekula Grinyar reaktivi: ikki metil birikadi, uchlamchi alkogolyat hosil bo'ladi.", Ea),
  W("Metil formiatga ortiqcha metilmagniy bromid ta'sir ettiring", ["C2H4O2", "CH3MgBr"], ["C3H7BrMgO", "CH3BrMgO"], "C2H4O2+2CH3MgBr→C3H7BrMgO+CH3BrMgO", "Formiatdan ikkilamchi alkogolyat hosil bo'ladi.", Mf),
 ]),
 S("m-2", G, "write", 3, [
  W("Uchlamchi magniy alkogolyatini gidrolizlang", ["C4H9BrMgO", "H2O"], ["C4H10O", "Mg(OH)Br"], "C4H9BrMgO+H2O→C4H10O+Mg(OH)Br", "Uchlamchi butil spirt (2-metilpropanol-2) hosil bo'ladi.", Ea),
  W("Ikkilamchi magniy alkogolyatini gidrolizlang", ["C3H7BrMgO", "H2O"], ["C3H8O", "Mg(OH)Br"], "C3H7BrMgO+H2O→C3H8O+Mg(OH)Br", "Propanol-2 hosil bo'ladi.", Mf),
 ]),
 S("m-3", G, "choice", 3, [
  C("Murakkab efirga ortiqcha Grinyar reaktivi ta'sir etsa (formiatdan boshqa), qanday spirt hosil bo'ladi?", "Uchlamchi spirt", ["Birlamchi spirt", "Ikkilamchi spirt", "Aldegid"], "Ikkita radikal bitta uglerodga birikadi: u uch uglerodga bog'langan bo'ladi.", Ea, ("Ikkilamchi spirt", "Ikkilamchi spirt formiatlardan chiqadi, boshqa efirlardan uchlamchi.")),
  C("Metil formiatga ortiqcha Grinyar reaktivi ta'sir etsa, qanday spirt hosil bo'ladi?", "Ikkilamchi spirt", ["Birlamchi spirt", "Uchlamchi spirt", "Keton"], "Formiatda uglerodda bitta vodorod bor: u ikkilamchi spirt beradi.", Mf, ("Uchlamchi spirt", "Formiatning uglerodida vodorod qoladi.")),
 ]),
]
G = "Gidrogenlash"
slots += [
 S("r-1", G, "write", 2, [
  W("Etil atsetatning gidrogenlanishini yozing (katalizator, bosim)", ["C4H8O2", "H2"], ["C2H6O"], "C4H8O2+2H2→2C2H6O", "Efir ikki spirtga qaytariladi: ikki molekula etanol.", Ea),
  W("Metil atsetatning gidrogenlanishini yozing (katalizator, bosim)", ["C3H6O2", "H2"], ["C2H6O", "CH4O"], "C3H6O2+2H2→C2H6O+CH4O", "Etanol va metanol hosil bo'ladi.", Ma),
 ]),
 S("r-2", G, "write", 2, [
  W("Metil formiatning gidrogenlanishini yozing", ["C2H4O2", "H2"], ["CH4O"], "C2H4O2+2H2→2CH4O", "Ikki molekula metanol hosil bo'ladi.", Mf),
  W("Metil benzoatning gidrogenlanishini yozing", ["C8H8O2", "H2"], ["C7H8O", "CH4O"], "C8H8O2+2H2→C7H8O+CH4O", "Benzil spirt va metanol hosil bo'ladi.", None),
 ]),
 S("r-3", G, "choice", 2, [
  C("Murakkab efir gidrogenlanganda qanday moddalar hosil bo'ladi?", "Ikki spirt", ["Alkan", "Aldegid", "Karbon kislota"], "Kislota qismi ham spirtga qaytariladi.", Ea, ("Karbon kislota", "Kislota qismi spirtga qaytariladi, kislota hosil bo'lmaydi.")),
  C("Suyuq yog'larni gidrogenlash natijasi qanday?", "Qo'shbog'lar to'yinadi va yog' qattiqlashadi", ["Yog' parchalanadi", "Glitserin hosil bo'ladi", "Sovun hosil bo'ladi"], "Margarin ishlab chiqarish asosi.", Ea),
 ]),
]
G = "Zanjir"
cA = {"all": ["C4H8O2", "C2H6O", "C2H4O", "C2H4O2"]}
cB = {"all": ["CO", "C2H4O2", "CH3NO", "HCN"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (H⁺, qizdirish)", ["C4H8O2", "H2O"], ["C2H4O2", "C2H6O"], "C4H8O2+H2O→C2H4O2+C2H6O", "Etil atsetat kislota va spirtga gidrolizlanadi.", Ea, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (katalizator, bosim)", ["CO", "CH3OH"], ["C2H4O2"], "CO+CH3OH→C2H4O2", "Metil formiat hosil bo'ladi.", Mf, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (CuO, qizdirish)", ["C2H6O", "CuO"], ["C2H4O", "Cu", "H2O"], "C2H6O+CuO→C2H4O+Cu+H2O", "Etanol sirka aldegidga oksidlanadi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing", ["C2H4O2", "NH3"], ["CH3NO", "CH4O"], "C2H4O2+NH3→CH3NO+CH4O", "Formamid va metanol hosil bo'ladi.", Mf, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (kumush oksidning ammiakli eritmasi)", ["C2H4O", "Ag2O"], ["C2H4O2", "Ag"], "C2H4O+Ag2O→C2H4O2+2Ag", "Aldegid sirka kislotaga oksidlanadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (P₂O₅, qizdirish)", ["CH3NO"], ["HCN", "H2O"], "CH3NO→HCN+H2O", "Formamid degidratlanib sianid kislota beradi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(19, "Murakkab efirlar", ["etil atsetat", "metil atsetat", "metil formiat"], slots)
