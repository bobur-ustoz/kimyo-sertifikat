from lib import *
G_, N = ["glitserin"], ["nitroglitserin"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Triatsetinning (glitserin triatsetati) NaOH bilan gidrolizini yozing", ["C9H14O6", "NaOH"], ["C3H8O3", "C2H3NaO2"], "C9H14O6+3NaOH→C3H8O3+3C2H3NaO2", "Efir ishqorda glitserin va sirka kislota tuziga ajraladi.", G_),
  W("Tristearinning NaOH bilan gidrolizini yozing (sovunlash)", ["C57H110O6", "NaOH"], ["C3H8O3", "C18H35NaO2"], "C57H110O6+3NaOH→C3H8O3+3C18H35NaO2", "Yog' sovunlanib glitserin va sovun (natriy stearat) hosil qiladi.", G_),
 ]),
 S("o-2", G, "write", 2, [
  W("1,2,3-tribrompropanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C3H5Br3", "NaOH"], ["C3H8O3", "NaBr"], "C3H5Br3+3NaOH→C3H8O3+3NaBr", "Uchala brom OH ga almashinadi.", G_),
  W("1,2,3-trixlorpropanga NaOH ning suvdagi eritmasi (ortiqcha) ta'sir ettiring", ["C3H5Cl3", "NaOH"], ["C3H8O3", "NaCl"], "C3H5Cl3+3NaOH→C3H8O3+3NaCl", "Uchala xlor OH ga almashinadi.", G_),
 ]),
 S("o-3", G, "write", 2, [
  W("Triatsetinning kislotali gidrolizini yozing (H⁺, qizdirish)", ["C9H14O6", "H2O"], ["C3H8O3", "C2H4O2"], "C9H14O6+3H2O→C3H8O3+3C2H4O2", "Kislotali gidrolizda glitserin va erkin sirka kislota hosil bo'ladi.", G_),
  W("Tristearinning kislotali gidrolizini yozing (H⁺, qizdirish)", ["C57H110O6", "H2O"], ["C3H8O3", "C18H36O2"], "C57H110O6+3H2O→C3H8O3+3C18H36O2", "Glitserin va stearin kislota hosil bo'ladi.", G_),
 ]),
 S("o-4", G, "choice", 1, [
  C("Glitserinning tuzilish formulasi qaysi?", "HOCH₂–CH(OH)–CH₂OH", ["HOCH₂–CH₂OH", "CH₃–CH(OH)–CH₂OH", "HOCH₂–CH₂–CH₂OH"], "Uch uglerodli zanjirning har uglerodida bitta OH.", G_, ("CH₃–CH(OH)–CH₂OH", "Bu propilenglikol: ikki atomli spirt.")),
  C("Yog'larning gidrolizidan qaysi spirt hosil bo'ladi?", "Glitserin", ["Etilenglikol", "Etanol", "Metanol"], "Yog'lar glitserin va yuqori kislotalarning efiri.", G_),
 ]),
]
G = "Xususiy olinish"
slots += [
 S("x-1", G, "write", 2, [
  W("Allil spirtning KMnO₄ ning suvli eritmasi bilan oksidlanishini yozing (glitserin olinadi)", ["C3H6O", "KMnO4", "H2O"], ["C3H8O3", "MnO2", "KOH"], "3C3H6O+2KMnO4+4H2O→3C3H8O3+2MnO2+2KOH", "Qo'shbog'ga ikkita OH birikadi.", G_),
  W("Glyukozaning gidrogenolizini yozing (katalizator, bosim): glitserin hosil bo'ladi", ["C6H12O6", "H2"], ["C3H8O3"], "C6H12O6+2H2→2C3H8O3", "Olti uglerodli molekula ikkiga bo'linib ikki glitserin beradi.", G_),
 ]),
 S("x-2", G, "write", 2, [
  W("Epixlorgidrinning gidrolizini yozing", ["C3H5ClO", "H2O"], ["C3H8O3", "HCl"], "C3H5ClO+2H2O→C3H8O3+HCl", "Halqa ochiladi, xlor OH ga almashinadi.", G_),
  W("1,3-dixlor-2-propanolga NaOH ta'sir ettiring (ortiqcha)", ["C3H6Cl2O", "NaOH"], ["C3H8O3", "NaCl"], "C3H6Cl2O+2NaOH→C3H8O3+2NaCl", "Ikkala xlor OH ga almashinadi.", G_),
 ]),
 S("x-3", G, "choice", 1, [
  C("Glitserin sanoatda asosan qanday olinadi?", "Yog'larni gidrolizlab (sovunlash)", ["Etilenni oksidlab", "Propanni xlorlab", "Atsetilendan"], "Yog' gidrolizida glitserin qo'shimcha mahsulot.", G_),
  C("Sovun hosil bo'lishida glitserin qanday rol o'ynaydi?", "Qo'shimcha mahsulot sifatida ajraladi", ["Reagent sifatida kerak", "Katalizator", "Hosil bo'lmaydi"], "Yog' ishqor bilan sovun va glitseringa parchalanadi.", G_, ("Reagent sifatida kerak", "Glitserin reagent emas, mahsulot.")),
 ]),
]
G = "Metallar va Cu(OH)₂"
slots += [
 S("m-1", G, "write", 1, [
  W("Glitseringa ortiqcha natriy ta'sir ettiring", ["C3H8O3", "Na"], ["C3H5Na3O3", "H2"], "2C3H8O3+6Na→2C3H5Na3O3+3H2", "Uchala OH vodorodi natriyga almashinadi.", G_),
  W("Glitseringa 1 mol natriy ta'sir ettiring (bitta OH)", ["C3H8O3", "Na"], ["C3H7NaO3", "H2"], "2C3H8O3+2Na→2C3H7NaO3+H2", "Faqat bitta OH vodorodi almashinadi.", G_),
 ]),
 S("m-2", G, "write", 2, [
  W("Glitseringa mis(II) gidroksid ta'sir ettiring", ["C3H8O3", "Cu(OH)2"], ["C6H14CuO6", "H2O"], "2C3H8O3+Cu(OH)2→C6H14CuO6+2H2O", "To'q ko'k kompleks (mis glitserati) hosil bo'ladi.", G_),
  W("Glitseringa ortiqcha kaliy ta'sir ettiring", ["C3H8O3", "K"], ["C3H5K3O3", "H2"], "2C3H8O3+6K→2C3H5K3O3+3H2", "Uchala OH vodorodi kaliyga almashinadi.", G_),
 ]),
 S("m-3", G, "choice", 2, [
  C("Glitseringa yangi cho'ktirilgan Cu(OH)₂ qo'shilsa, nima kuzatiladi?", "To'q ko'k eritma hosil bo'ladi", ["Qizil cho'kma", "Yashil cho'kma", "Rang o'zgarmaydi"], "Qo'shni OH guruhlari mis bilan kompleks hosil qiladi.", G_, ("Qizil cho'kma", "Qizil cho'kma (Cu₂O) aldegidlarda qizdirganda hosil bo'ladi.")),
  C("Glitserinni aniqlash (sifat reaksiyasi) uchun qaysi reaktiv ishlatiladi?", "Yangi cho'ktirilgan Cu(OH)₂", ["Bromli suv", "AgNO₃ ning ammiakli eritmasi", "FeCl₃"], "To'q ko'k eritma ko'p atomli spirtni bildiradi.", G_, ("AgNO₃ ning ammiakli eritmasi", "Bu aldegidlar uchun \"kumush ko'zgu\" reaktivi.")),
 ]),
]
G = "HX va eterifikatsiya"
slots += [
 S("h-1", G, "write", 1, [
  W("Glitseringa ortiqcha HCl ta'sir ettiring", ["C3H8O3", "HCl"], ["C3H5Cl3", "H2O"], "C3H8O3+3HCl→C3H5Cl3+3H2O", "Uchala OH xlorga almashinadi.", G_),
  W("Glitseringa 1 mol HBr ta'sir ettiring", ["C3H8O3", "HBr"], ["C3H7BrO2", "H2O"], "C3H8O3+HBr→C3H7BrO2+H2O", "Bitta OH bromga almashinadi.", G_),
 ]),
 S("h-2", G, "write", 2, [
  W("Glitserinni nitrolang (HNO₃ + H₂SO₄ aralashmasi): nitroglitserin olinadi", ["C3H8O3", "HNO3"], ["C3H5N3O9", "H2O"], "C3H8O3+3HNO3→C3H5N3O9+3H2O", "Uchala OH nitrat efirga aylanadi.", N),
  W("Glitseringa 1 mol HNO₃ ta'sir ettiring (monoefir)", ["C3H8O3", "HNO3"], ["C3H7NO5", "H2O"], "C3H8O3+HNO3→C3H7NO5+H2O", "Bitta OH nitrat efiriga aylanadi.", G_),
 ]),
 S("h-3", G, "write", 2, [
  W("Glitserin va ortiqcha sirka kislota reaksiyasini yozing (H₂SO₄): triatsetin", ["C3H8O3", "C2H4O2"], ["C9H14O6", "H2O"], "C3H8O3+3C2H4O2→C9H14O6+3H2O", "Uchala OH sirka kislota bilan efir hosil qiladi.", G_),
  W("Glitserin va stearin kislota reaksiyasini yozing (H₂SO₄): tristearin", ["C3H8O3", "C18H36O2"], ["C57H110O6", "H2O"], "C3H8O3+3C18H36O2→C57H110O6+3H2O", "Yog' (tristearin) hosil bo'ladi.", G_),
 ]),
 S("h-4", G, "choice", 3, [
  C("Nitroglitserin kimyoviy jihatdan qaysi sinfga kiradi?", "Murakkab efir (nitrat efiri)", ["Nitrobirikma", "Spirt", "Aldegid"], "Kislorod orqali bog'langan –O–NO₂ guruhlari.", N, ("Nitrobirikma", "Nitrobirikmada azot uglerodga bog'langan (C–NO₂). Nitroglitserinda esa C–O–NO₂.")),
  C("1 mol glitserinni to'liq nitrolash uchun necha mol HNO₃ kerak?", "3 mol", ["1 mol", "2 mol", "4 mol"], "Uchta OH guruhi uchun uchta HNO₃.", N, ("1 mol", "Bu faqat bitta OH uchun.")),
 ]),
]
G = "Degidratlanish"
slots += [
 S("d-1", G, "write", 3, [
  W("Glitserinning molekula ichida bitta suv ajralib degidratlanishini yozing", ["C3H8O3"], ["C3H6O2", "H2O"], "C3H8O3→C3H6O2+H2O", "Bitta suv ajraladi, enol karbonilga izomerlanadi.", G_),
  W("Glitserinning molekulalararo degidratlanishini yozing (diglitserin)", ["C3H8O3"], ["C6H14O5", "H2O"], "2C3H8O3→C6H14O5+H2O", "Ikki molekuladan bitta suv ajraladi.", G_),
 ]),
 S("d-2", G, "choice", 2, [
  C("Glitserinni KHSO₄ bilan qizdirilsa, o'tkir hidli qaysi modda hosil bo'ladi?", "Akrolein", ["Akril kislota", "Aseton", "Propanal"], "Ikkita suv ajralib to'yinmagan aldegid hosil bo'ladi.", G_, ("Propanal", "Akroleinda qo'shbog' bor, propanalda yo'q.")),
  C("Akrolein qaysi sinfga mansub?", "To'yinmagan aldegid", ["Keton", "Spirt", "Karboksilli kislota"], "CH₂=CH–CHO: qo'shbog' va aldegid guruhi.", G_),
 ]),
 S("d-3", G, "write", 3, [
  W("Glitserinning uch molekulasi degidratlanishini yozing (triglitserin)", ["C3H8O3"], ["C9H20O7", "H2O"], "3C3H8O3→C9H20O7+2H2O", "Uch molekuladan ikki suv ajraladi.", G_),
  W("Glitserinning to'rt molekulasi degidratlanishini yozing (tetraglitserin)", ["C3H8O3"], ["C12H26O9", "H2O"], "4C3H8O3→C12H26O9+3H2O", "To'rt molekuladan uch suv ajraladi.", G_),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 2, [
  W("Glitserinning to'liq yonishini yozing", ["C3H8O3", "O2"], ["CO2", "H2O"], "2C3H8O3+7O2→6CO2+8H2O", "Kasr chiqmasligi uchun ikki baravar.", G_),
  W("Nitroglitserinning portlashini yozing (CO₂, H₂O, N₂ va O₂ hosil bo'ladi)", ["C3H5N3O9"], ["CO2", "H2O", "N2", "O2"], "4C3H5N3O9→12CO2+10H2O+6N2+O2", "Qattiq modda bir lahzada gazlarga aylanadi.", N),
 ]),
 S("k-2", G, "write", 2, [
  W("Glitserinni CuO bilan oksidlang (bitta spirt guruhi, qizdirish)", ["C3H8O3", "CuO"], ["C3H6O3", "Cu", "H2O"], "C3H8O3+CuO→C3H6O3+Cu+H2O", "Chetki CH₂OH guruhi aldegidga o'tadi.", G_),
  W("Glitserinni CuO bilan oksidlang (ikki spirt guruhi)", ["C3H8O3", "CuO"], ["C3H4O3", "Cu", "H2O"], "C3H8O3+2CuO→C3H4O3+2Cu+2H2O", "Ikkita guruh karbonilga o'tadi.", G_),
 ]),
 S("k-3", G, "choice", 3, [
  C("1 mol glitserin to'liq yonishi uchun necha mol O₂ kerak?", "3,5", ["3", "4", "4,5"], "3 CO₂ uchun 3 O₂, 4 H₂O uchun 2 O₂, glitserinning 3 ta O atomi 1,5 O₂ beradi: jami 3,5.", G_, ("4", "Glitserinda kislorod borligi hisobga olinmagan.")),
  C("46 g glitserin (M = 92) to'liq yonganda necha litr CO₂ (n.sh.) hosil bo'ladi?", "33,6 l", ["22,4 l", "67,2 l", "11,2 l"], "46 : 92 = 0,5 mol; 3 CO₂ hosil bo'ladi: 1,5 mol · 22,4 = 33,6 l.", G_, ("67,2 l", "67,2 l uchun 1 mol (92 g) glitserin kerak edi.")),
 ]),
 S("k-4", G, "choice", 2, [
  C("Nitroglitserin qayerda ishlatiladi?", "Dinamit tarkibida va (oz miqdorda) yurak dorisi sifatida", ["Sovun ishlab chiqarishda", "Polimerlar monomeri sifatida", "Oziq-ovqat bo'yog'i sifatida"], "Nobel nitroglitserindan dinamit yaratgan.", N),
  C("Nitroglitserin portlaganda qaysi gazlar hosil bo'ladi?", "CO₂, H₂O (bug'), N₂, O₂", ["Faqat CO₂", "CH₄ va H₂", "NO₂ va SO₂"], "Barcha mahsulotlar gaz holida: hajm keskin ortadi.", N),
 ]),
]
G = "Zanjir"
cA = {"all": ["C3H6", "C3H5Cl", "C3H6Cl2O", "C3H8O3"]}
cB = {"all": ["C3H8O3", "C3H4O", "C3H6O", "C3H6Br2O"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (500 °C)", ["C3H6", "Cl2"], ["C3H5Cl", "HCl"], "C3H6+Cl2→C3H5Cl+HCl", "Alil holatda o'rin olish.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (KHSO₄, 200 °C)", ["C3H8O3"], ["C3H4O", "H2O"], "C3H8O3→C3H4O+2H2O", "Ikki suv ajralib akrolein hosil bo'ladi.", G_, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (HOCl)", ["C3H5Cl", "HOCl"], ["C3H6Cl2O"], "C3H5Cl+HOCl→C3H6Cl2O", "Cl va OH qo'shbog'ga birikadi.", None, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (Ni, qisman gidrogenlash)", ["C3H4O", "H2"], ["C3H6O"], "C3H4O+H2→C3H6O", "Faqat C=O qaytariladi: allil spirt.", None, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (KOH ning suvdagi eritmasi, ortiqcha)", ["C3H6Cl2O", "KOH"], ["C3H8O3", "KCl"], "C3H6Cl2O+2KOH→C3H8O3+2KCl", "Ikkala xlor OH ga almashinadi: glitserin.", G_, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing", ["C3H6O", "Br2"], ["C3H6Br2O"], "C3H6O+Br2→C3H6Br2O", "Brom qo'shbog'ga birikadi.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(10, "Uch atomli spirtlar", ["glitserin", "nitroglitserin"], slots)
