from lib import *
Sx, Ma, Kr, Se = ["saxaroza"], ["maltoza"], ["kraxmal"], ["sellyuloza"]
slots = []
G = "Disaxaridlarning tuzilishi"
slots += [
 S("t-1", G, "choice", 1, [
  C("Saxarozaning molekulyar formulasi qaysi?", "C₁₂H₂₂O₁₁", ["C₆H₁₂O₆", "C₁₂H₂₄O₁₂", "(C₆H₁₀O₅)ₙ"], "Ikki monosaxaridning birikishidan bitta suv ajraladi.", Sx, ("C₆H₁₂O₆", "Bu monosaxarid formulasi. Disaxarid ikkita monosaxariddan hosil bo'ladi.")),
  C("Maltozaning molekulyar formulasi qaysi?", "C₁₂H₂₂O₁₁", ["C₆H₁₂O₆", "C₁₂H₂₄O₁₂", "C₁₂H₂₂O₁₀"], "Saxaroza bilan izomer.", Ma, ("C₁₂H₂₄O₁₂", "Ikki monosaxariddan bitta suv ajraladi, shuning uchun kislorod va vodorod kam.")),
 ]),
 S("t-2", G, "choice", 2, [
  C("Saxaroza qaysi monosaxaridlardan tuzilgan?", "Glyukoza va fruktoza", ["Ikki glyukoza", "Glyukoza va galaktoza", "Ikki fruktoza"], "α-glyukoza va β-fruktoza qoldiqlari.", Sx, ("Ikki glyukoza", "Ikki glyukoza qoldig'i maltozada.")),
  C("Maltoza qaysi monosaxaridlardan tuzilgan?", "Ikki glyukoza", ["Glyukoza va fruktoza", "Glyukoza va galaktoza", "Fruktoza va galaktoza"], "Ikki α-glyukoza qoldig'i.", Ma, ("Glyukoza va fruktoza", "Bu saxarozaning tarkibi.")),
 ]),
 S("t-3", G, "choice", 3, [
  C("Quyidagi disaxaridlardan qaysi biri qaytaruvchi emas?", "Saxaroza", ["Maltoza", "Laktoza", "Sellobioza"], "Saxarozada ikkala monosaxaridning yarim atsetal OH lari bog' hosil qilishda ishtirok etgan: erkin aldegid guruhi yo'q.", Sx, ("Maltoza", "Maltozada bitta zvenoning aldegid guruhi erkin: kumush ko'zgu beradi.")),
  C("Quyidagilardan qaysi biri qaytaruvchi disaxarid?", "Maltoza", ["Saxaroza", "Trehaloza", "Kraxmal"], "Maltozada erkin yarim atsetal OH bor.", Ma, ("Saxaroza", "Saxarozada erkin yarim atsetal OH yo'q.")),
 ]),
 S("t-4", G, "choice", 2, [
  C("Laktoza qayerda uchraydi?", "Sutda", ["Qand lavlagida", "Solodda", "Asalda"], "Sut shakari: glyukoza va galaktozadan.", None, ("Qand lavlagida", "Qand lavlagida saxaroza bor.")),
  C("Maltoza manbai qaysi?", "Solod (o'sgan don)", ["Sut", "Qand qamish", "Asal"], "Kraxmalning amilaza bilan qisman gidrolizidan hosil bo'ladi.", Ma, ("Qand qamish", "Qand qamishda saxaroza bor.")),
 ]),
]
G = "Disaxaridlarning reaksiyalari"
slots += [
 S("g-1", G, "choice", 1, [
  C("Saxarozaning gidrolizida qanday monosaxaridlar hosil bo'ladi?", "Glyukoza va fruktoza", ["Ikki glyukoza", "Glyukoza va galaktoza", "Ikki fruktoza"], "Gidrolizdan invert shakar (glyukoza + fruktoza) hosil bo'ladi.", Sx, ("Ikki glyukoza", "Ikki glyukoza maltoza gidrolizida hosil bo'ladi.")),
  C("Maltozaning gidrolizida nima hosil bo'ladi?", "Ikki molekula glyukoza", ["Glyukoza va fruktoza", "Glyukoza va galaktoza", "Fruktoza va galaktoza"], "Ikkala qoldiq ham glyukoza.", Ma, ("Glyukoza va fruktoza", "Bu saxarozaning gidroliz mahsuloti.")),
 ]),
 S("g-2", G, "write", 2, [
  W("Saxarozaning gidrolizini yozing (H⁺, qizdirish). Mahsulotlarni 2C₆H₁₂O₆ deb yozing", ["C12H22O11", "H2O"], ["C6H12O6"], "C12H22O11+H2O→2C6H12O6", "Glyukoza va fruktoza hosil bo'ladi (ikkalasi ham C₆H₁₂O₆).", Sx),
  W("Saxarozaga kalsiy oksid ta'sir ettiring (shakar kalsiy saxarati)", ["C12H22O11", "CaO"], ["C12H22CaO12"], "C12H22O11+CaO→C12H22CaO12", "Saxaroza kalsiy bilan eruvchan saxarat hosil qiladi.", Sx),
 ]),
 S("g-3", G, "write", 2, [
  W("Saxarozaning to'liq yonishini yozing", ["C12H22O11", "O2"], ["CO2", "H2O"], "C12H22O11+12O2→12CO2+11H2O", "Kislorod: 24 + 11 − 11 = 24 atom, ya'ni 12 O₂.", Sx),
  W("Saxarozaga konsentrlangan H₂SO₄ ta'sir ettiring (ko'mirlanish)", ["C12H22O11"], ["C", "H2O"], "C12H22O11→12C+11H2O", "Sulfat kislota suvni tortib oladi: qora ko'mir qoladi.", Sx),
 ]),
 S("g-4", G, "write", 3, [
  W("Saxarozaga ortiqcha sirka angidrid ta'sir ettiring (oktaatsetat)", ["C12H22O11", "C4H6O3"], ["C28H38O19", "C2H4O2"], "C12H22O11+8C4H6O3→C28H38O19+8C2H4O2", "Sakkizta OH guruhi atsillanadi.", Sx),
  W("Maltozaga kumush oksidning ammiakli eritmasi ta'sir ettiring", ["C12H22O11", "Ag2O"], ["C12H22O12", "Ag"], "C12H22O11+Ag2O→C12H22O12+2Ag", "Maltozaning erkin aldegid guruhi oksidlanadi: kumush ko'zgu.", Ma),
 ]),
 S("g-5", G, "choice", 2, [
  C("Saxaroza kumush ko'zgu reaksiyasini beradimi?", "Yo'q", ["Ha", "Faqat qizdirilganda", "Faqat ishqorda"], "Saxarozada erkin aldegid guruhi yo'q (gidroliz bo'lmaguncha).", Sx, ("Ha", "Aldegid guruhi bog' hosil qilishda ishtirok etgan, shuning uchun qaytaruvchi emas.")),
  C("Invert shakar nima?", "Saxaroza gidrolizidan hosil bo'lgan glyukoza va fruktoza aralashmasi", ["Maltoza", "Kraxmal", "Laktoza"], "Asal tarkibining asosiy qismi shunday aralashma.", Sx, ("Maltoza", "Maltoza kraxmal gidrolizidan chiqadi.")),
 ]),
]
G = "Kraxmal"
slots += [
 S("k-1", G, "write", 1, [
  W("Kraxmalning qisman gidrolizini yozing (amilaza): maltoza hosil bo'ladi", ["C6H10O5", "H2O"], ["C12H22O11"], "2C6H10O5+H2O→C12H22O11", "Ikki zveno bitta suv biriktirib maltoza beradi.", Ma),
  W("Kraxmalning to'liq gidrolizini yozing (H⁺, qizdirish)", ["C6H10O5", "H2O"], ["C6H12O6"], "C6H10O5+H2O→C6H12O6", "Har zveno suv biriktirib glyukoza beradi.", Kr),
 ]),
 S("k-2", G, "write", 2, [
  W("Kraxmal zvenosining to'liq yonishini yozing", ["C6H10O5", "O2"], ["CO2", "H2O"], "C6H10O5+6O2→6CO2+5H2O", "Kislorod: 12 + 5 − 5 = 12 atom, ya'ni 6 O₂.", Kr),
  W("Kraxmal zvenosiga konsentrlangan H₂SO₄ ta'sir ettiring (ko'mirlanish)", ["C6H10O5"], ["C", "H2O"], "C6H10O5→6C+5H2O", "Suv ajralib uglerod qoladi.", Kr),
 ]),
 S("k-3", G, "choice", 1, [
  C("Kraxmalga yod eritmasi ta'sir ettirilsa, qanday rang paydo bo'ladi?", "Ko'k", ["Qizil", "Sariq", "Yashil"], "Yod amiloza spiralida to'planib ko'k kompleks hosil qiladi.", Kr, ("Qizil", "Qizil rang glikogen yoki dekstrin bilan.")),
  C("Kraxmalning monomeri qaysi?", "α-glyukoza", ["β-glyukoza", "Fruktoza", "Riboza"], "α-glyukoza qoldiqlari zanjir hosil qiladi.", Kr, ("β-glyukoza", "β-glyukoza qoldiqlari sellyulozani hosil qiladi.")),
 ]),
 S("k-4", G, "choice", 2, [
  C("Kraxmal qanday polimerlardan iborat?", "Amiloza va amilopektin", ["Faqat amiloza", "Sellobioza va maltoza", "Glikogen va xitin"], "Amiloza chiziqli, amilopektin tarmoqlangan.", Kr, ("Faqat amiloza", "Kraxmalda amilopektin ham bor.")),
  C("Glikogen nima?", "Hayvonlar kraxmali", ["O'simlik kraxmali", "Sellyuloza analogi", "Oqsil"], "Jigar va muskullarda zaxira polisaxarid.", Kr, ("O'simlik kraxmali", "O'simlikda kraxmal, hayvonlarda glikogen.")),
 ]),
]
G = "Sellyuloza"
slots += [
 S("s-1", G, "write", 2, [
  W("Sellyuloza zvenosiga nitrat kislota ta'sir ettiring (trinitrosellyuloza, piroksilin)", ["C6H10O5", "HNO3"], ["C6H7N3O11", "H2O"], "C6H10O5+3HNO3→C6H7N3O11+3H2O", "Uchala OH nitrat efirga aylanadi: portlovchi modda.", Se),
  W("Sellyuloza zvenosiga sirka angidrid ta'sir ettiring (triatsetat)", ["C6H10O5", "C4H6O3"], ["C12H16O8", "C2H4O2"], "C6H10O5+3C4H6O3→C12H16O8+3C2H4O2", "Atsetat tolasi olinadi.", Se),
 ]),
 S("s-2", G, "write", 2, [
  W("Sellyulozaning mononitrat hosil qilishini yozing", ["C6H10O5", "HNO3"], ["C6H9NO7", "H2O"], "C6H10O5+HNO3→C6H9NO7+H2O", "Bitta OH nitrat efirga aylanadi.", Se),
  W("Sellyulozaning dinitrat (kolloksilin) hosil qilishini yozing", ["C6H10O5", "HNO3"], ["C6H8N2O9", "H2O"], "C6H10O5+2HNO3→C6H8N2O9+2H2O", "Ikki OH nitrat efirga aylanadi: kolloksilin.", Se),
 ]),
 S("s-3", G, "choice", 1, [
  C("Sellyuloza va kraxmalning asosiy farqi nimada?", "Glyukoza zvenolari β va α shaklda bog'langan", ["Sellyuloza oqsil", "Kraxmal glyukozadan tuzilmagan", "Farqi yo'q"], "Sellyulozada β-1,4, kraxmalda α-1,4 bog'lar.", Se, ("Farqi yo'q", "Bog' turi farq qiladi: shuning uchun xossalari ham farq qiladi.")),
  C("Sellyulozadan qanday sun'iy tolalar olinadi?", "Viskoza va atsetat tola", ["Kapron", "Lavsan", "Neylon"], "Kimyoviy qayta ishlangan sellyuloza.", Se, ("Kapron", "Kapron sintetik tola (poliamid).")),
 ]),
 S("s-4", G, "choice", 2, [
  C("Piroksilin nima?", "Sellyulozaning trinitrati (portlovchi modda)", ["Nitroglitserin", "TNT", "Pikrin kislota"], "Tutunsiz porox asosi.", Se, ("Nitroglitserin", "Nitroglitserin glitserin efiri, piroksilin esa sellyuloza efiri.")),
  C("Viskoza tolasi sellyulozadan qanday olinadi?", "NaOH va CS₂ bilan ishlov berib, so'ng kislotada qayta cho'ktirib", ["Kapron bilan aralashtirib", "Polimerlash orqali", "Pishirish orqali"], "Ksantogenat orqali eruvchan sellyuloza hosil bo'ladi.", Se, ("Polimerlash orqali", "Sellyuloza tayyor polimer, uni faqat eritib qayta cho'ktiriladi.")),
 ]),
 S("s-5", G, "choice", 3, [
  C("Sellyulozada glyukoza zvenolari qanday bog' bilan bog'langan?", "β-1,4-glikozid bog'i", ["α-1,4-glikozid bog'i", "α-1,6-glikozid bog'i", "Peptid bog'i"], "β-konfiguratsiya zanjirni to'g'ri chiziqli qiladi.", Se, ("α-1,4-glikozid bog'i", "α-1,4 bog' kraxmalda.")),
  C("Kraxmalning amilozasida zvenolar qanday bog' bilan bog'langan?", "α-1,4-glikozid bog'i", ["β-1,4-glikozid bog'i", "Peptid bog'i", "Efir bog'i"], "α-konfiguratsiya zanjirni spiral qiladi.", Kr, ("β-1,4-glikozid bog'i", "β-1,4 bog' sellyulozada.")),
 ]),
]
G = "Gidroliz va boshqa"
slots += [
 S("q-1", G, "choice", 2, [
  C("Sellyulozaning to'liq gidrolizidan (H₂SO₄) qaysi modda hosil bo'ladi?", "Glyukoza", ["Fruktoza", "Saxaroza", "Maltoza"], "Ko'p zvenoli polimer glyukozagacha parchalanadi.", Se, ("Maltoza", "Maltoza kraxmalning qisman gidrolizidan chiqadi.")),
  C("Kraxmalning fermentativ (amilaza) gidrolizida asosiy mahsulot qaysi?", "Maltoza", ["Glyukoza", "Fruktoza", "Saxaroza"], "Amilaza zanjirni ikki glyukoza birligiga bo'ladi.", Kr, ("Glyukoza", "To'liq gidrolizda glyukoza, amilaza esa maltoza beradi.")),
 ]),
 S("q-2", G, "write", 3, [
  W("Kraxmaldan etanol olishning umumiy tenglamasini yozing (gidroliz va bijg'ish)", ["C6H10O5", "H2O"], ["C2H6O", "CO2"], "C6H10O5+H2O→2C2H6O+2CO2", "Kraxmal zvenosidan glyukoza, undan ikki etanol va ikki CO₂ hosil bo'ladi.", Kr),
  W("Sellyuloza zvenosining gidrolizi va gidrogenlanishini yozing (sorbit)", ["C6H10O5", "H2O", "H2"], ["C6H14O6"], "C6H10O5+H2O+H2→C6H14O6", "Glyukoza hosil bo'lib, sorbitga qaytariladi.", Se),
 ]),
 S("q-3", G, "choice", 2, [
  C("Kraxmal odam organizmida qayerda hazm bo'la boshlaydi?", "Og'iz bo'shlig'ida (amilaza ta'sirida)", ["Oshqozonda pepsin bilan", "Ichakda lipaza bilan", "Hazm bo'lmaydi"], "So'lak amilazasi kraxmalni maltozagacha parchalaydi.", Kr, ("Oshqozonda pepsin bilan", "Pepsin oqsillarni parchalaydi.")),
  C("Sellyuloza odam organizmida qanday holatda?", "Hazm bo'lmaydi (to'qima tolasi sifatida)", ["Glyukozagacha hazm bo'ladi", "Oqsilga aylanadi", "Yog'ga aylanadi"], "Odamda β-glikozid bog'ni parchalovchi ferment yo'q.", Se, ("Glyukozagacha hazm bo'ladi", "Faqat ruminantlar bakteriyalari yordamida hazm qiladi.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H12O6", "C6H14O6", "C6H10O4", "C6H8Na2O4"]}
cB = {"all": ["C6H10O5", "C6H9NaO5", "C7H9NaO5S2", "C6H10O5"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (Ni, qizdirish)", ["C6H12O6", "H2"], ["C6H14O6"], "C6H12O6+H2→C6H14O6", "Glyukoza sorbitga qaytariladi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (sellyulozani ishqorlash)", ["C6H10O5", "NaOH"], ["C6H9NaO5", "H2O"], "C6H10O5+NaOH→C6H9NaO5+H2O", "Ishqor sellyulozaning OH guruhini natriy tuziga o'tkazadi.", Se, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (degidratlanish, H⁺)", ["C6H14O6"], ["C6H10O4", "H2O"], "C6H14O6→C6H10O4+2H2O", "Sorbit ichki degidratlanib izosorbid hosil qiladi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (uglerod sulfid)", ["C6H9NaO5", "CS2"], ["C7H9NaO5S2"], "C6H9NaO5+CS2→C7H9NaO5S2", "Ksantogenat (viskoza) hosil bo'ladi.", Se, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (natriy)", ["C6H10O4", "Na"], ["C6H8Na2O4", "H2"], "C6H10O4+2Na→C6H8Na2O4+H2", "Ikkala OH vodorodi natriyga almashinadi.", None, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (H₂SO₄): sellyuloza qayta tiklanadi", ["C7H9NaO5S2", "H2SO4"], ["C6H10O5", "CS2", "NaHSO4"], "C7H9NaO5S2+H2SO4→C6H10O5+CS2+NaHSO4", "Kislota ta'sirida ksantogenat parchalanib sellyuloza (viskoza tola) hosil bo'ladi.", Se, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(21, "Di- va polisaxaridlar", ["saxaroza", "maltoza", "kraxmal", "sellyuloza"], slots)
