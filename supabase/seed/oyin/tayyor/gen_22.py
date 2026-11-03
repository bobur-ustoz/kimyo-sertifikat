from lib import *
M, E, A = ["metilamin"], ["etilamin"], ["anilin"]
slots = []
G = "Izomeriya va nomlanish"
slots += [
 S("n-1", G, "choice", 1, [
  C("CH₃NH₂ moddaning nomi qaysi?", "Metilamin", ["Etilamin", "Dimetilamin", "Metanol"], "Metil radikalga NH₂ guruhi birikkan.", M, ("Dimetilamin", "Dimetilaminda ikkita metil radikal bor: (CH₃)₂NH.")),
  C("C₆H₅NH₂ moddaning nomi qaysi?", "Anilin", ["Fenol", "Toluidin", "Benzilamin"], "Benzol halqasiga bevosita NH₂ guruhi birikkan.", A, ("Benzilamin", "Benzilaminda NH₂ yon zanjirda: C₆H₅CH₂NH₂.")),
 ]),
 S("n-2", G, "choice", 2, [
  C("C₂H₇N formulaga mos ikkita amin izomeri qaysilar?", "Etilamin va dimetilamin", ["Etilamin va trimetilamin", "Metilamin va etilamin", "Dimetilamin va metilamin"], "Birlamchi (C₂H₅NH₂) va ikkilamchi ((CH₃)₂NH).", E, ("Etilamin va trimetilamin", "Trimetilaminning formulasi C₃H₉N.")),
  C("(CH₃)₃N qanday amin?", "Uchlamchi amin", ["Birlamchi amin", "Ikkilamchi amin", "Amid"], "Azotda uchta radikal bor.", M, ("Ikkilamchi amin", "Ikkilamchida ikkita radikal va bitta vodorod.")),
 ]),
 S("n-3", G, "choice", 3, [
  C("C₃H₉N tarkibli nechta amin izomeri bor?", "4", ["3", "2", "5"], "Propilamin, izopropilamin, metiletilamin va trimetilamin.", E, ("3", "To'rtinchisini unutish: trimetilamin yoki metiletilamin.")),
  C("C₄H₁₁N tarkibli nechta birlamchi amin izomeri bor?", "4", ["2", "3", "5"], "n-butil-, sek-butil-, izobutil- va tret-butilamin.", E, ("3", "Uchlamchi butilamin ham bor.")),
 ]),
]
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Bromoetanga ammiak ta'sir ettiring (Gofman)", ["C2H5Br", "NH3"], ["C2H7N", "HBr"], "C2H5Br+NH3→C2H7N+HBr", "Galogen NH₂ guruhi bilan almashinadi: etilamin.", E),
  W("Xlormetanga ammiak ta'sir ettiring (Gofman)", ["CH3Cl", "NH3"], ["CH5N", "HCl"], "CH3Cl+NH3→CH5N+HCl", "Metilamin hosil bo'ladi.", M),
 ]),
 S("o-2", G, "write", 2, [
  W("Nitroetanni vodorod bilan qaytaring (katalizator)", ["C2H5NO2", "H2"], ["C2H7N", "H2O"], "C2H5NO2+3H2→C2H7N+2H2O", "Nitro guruh aminoguruhga qaytariladi.", E),
  W("Nitrometanni vodorod bilan qaytaring (katalizator)", ["CH3NO2", "H2"], ["CH5N", "H2O"], "CH3NO2+3H2→CH5N+2H2O", "Metilamin hosil bo'ladi.", M),
 ]),
 S("o-3", G, "write", 2, [
  W("Asetonitrilni vodorod bilan qaytaring (Ni)", ["C2H3N", "H2"], ["C2H7N"], "C2H3N+2H2→C2H7N", "Nitril guruh CH₂NH₂ ga qaytariladi: etilamin.", E),
  W("Propionitrilni vodorod bilan qaytaring (Ni)", ["C3H5N", "H2"], ["C3H9N"], "C3H5N+2H2→C3H9N", "Propilamin hosil bo'ladi.", None),
 ]),
 S("o-4", G, "write", 3, [
  W("Atsetamidga brom va NaOH ta'sir ettiring (Gofman bo'yicha parchalanish): metilamin", ["C2H5NO", "Br2", "NaOH"], ["CH5N", "Na2CO3", "NaBr", "H2O"], "C2H5NO+Br2+4NaOH→CH5N+Na2CO3+2NaBr+2H2O", "Uglerod soni bittaga kamayadi: amid → bir uglerod kam amin.", M),
  W("Propionamidga brom va NaOH ta'sir ettiring (Gofman)", ["C3H7NO", "Br2", "NaOH"], ["C2H7N", "Na2CO3", "NaBr", "H2O"], "C3H7NO+Br2+4NaOH→C2H7N+Na2CO3+2NaBr+2H2O", "Etilamin hosil bo'ladi.", E),
 ]),
]
G = "Anilin olinishi"
slots += [
 S("x-1", G, "write", 2, [
  W("Nitrobenzolni vodorod bilan qaytaring (Ni, qizdirish)", ["C6H5NO2", "H2"], ["C6H7N", "H2O"], "C6H5NO2+3H2→C6H7N+2H2O", "Nitro guruh aminoguruhga qaytariladi.", A),
  W("Nitrobenzolni temir va xlorid kislota bilan qaytaring (Zinin)", ["C6H5NO2", "Fe", "HCl"], ["C6H7N", "FeCl2", "H2O"], "C6H5NO2+3Fe+6HCl→C6H7N+3FeCl2+2H2O", "Temir qaytaruvchi, HCl muhit hosil qiladi.", A),
 ]),
 S("x-2", G, "write", 2, [
  W("Xlorbenzolga ammiak ta'sir ettiring (yuqori harorat va bosim, Cu)", ["C6H5Cl", "NH3"], ["C6H7N", "NH4Cl"], "C6H5Cl+2NH3→C6H7N+NH4Cl", "Galogen aminoguruhga almashinadi; ikkinchi ammiak HCl ni biriktiradi.", A),
  W("Brombenzolga ammiak ta'sir ettiring (Cu, bosim)", ["C6H5Br", "NH3"], ["C6H7N", "NH4Br"], "C6H5Br+2NH3→C6H7N+NH4Br", "Anilin va ammoniy bromid hosil bo'ladi.", A),
 ]),
 S("x-3", G, "choice", 2, [
  C("Anilinni nitrobenzoldan olish reaksiyasi kim nomi bilan ataladi?", "Zinin reaksiyasi", ["Vyurs reaksiyasi", "Kucherov reaksiyasi", "Konovalov reaksiyasi"], "Nitrobenzolning qaytarilishi: N. N. Zinin.", A, ("Konovalov reaksiyasi", "Konovalov reaksiyasi alkanlarni nitrolashga tegishli.")),
  C("Zinin reaksiyasida nitro guruhni qaytarish uchun nima ishlatiladi?", "Temir va HCl (yoki vodorod katalizatorda)", ["O₂", "NaOH", "KMnO₄"], "Qaytaruvchi kerak: nitro guruh aminoguruhga o'tadi.", A, ("KMnO₄", "KMnO₄ oksidlovchi, qaytaruvchi emas.")),
 ]),
]
G = "Asoslik va tuz hosil qilish"
slots += [
 S("t-1", G, "write", 1, [
  W("Metilaminga xlorid kislota ta'sir ettiring", ["CH5N", "HCl"], ["CH6ClN"], "CH5N+HCl→CH6ClN", "Metilammoniy xlorid tuzi hosil bo'ladi.", M),
  W("Etilaminga sulfat kislota ta'sir ettiring (ortiqcha amin)", ["C2H7N", "H2SO4"], ["C4H16N2O4S"], "2C2H7N+H2SO4→C4H16N2O4S", "Etilammoniy sulfat hosil bo'ladi.", E),
 ]),
 S("t-2", G, "write", 1, [
  W("Anilinga xlorid kislota ta'sir ettiring", ["C6H7N", "HCl"], ["C6H8ClN"], "C6H7N+HCl→C6H8ClN", "Anilin gidroxlorid (fenilammoniy xlorid) hosil bo'ladi.", A),
  W("Anilinga bromid kislota ta'sir ettiring", ["C6H7N", "HBr"], ["C6H8BrN"], "C6H7N+HBr→C6H8BrN", "Anilin gidrobromid hosil bo'ladi.", A),
 ]),
 S("t-3", G, "write", 2, [
  W("Fenilammoniy xloridga NaOH ta'sir ettiring", ["C6H8ClN", "NaOH"], ["C6H7N", "NaCl", "H2O"], "C6H8ClN+NaOH→C6H7N+NaCl+H2O", "Kuchli asos zaif asosni tuzidan siqib chiqaradi.", A),
  W("Metilammoniy xloridga NaOH ta'sir ettiring", ["CH6ClN", "NaOH"], ["CH5N", "NaCl", "H2O"], "CH6ClN+NaOH→CH5N+NaCl+H2O", "Metilamin ozod bo'ladi.", M),
 ]),
 S("t-4", G, "choice", 2, [
  C("Quyidagilardan qaysi biri eng kuchli asos?", "Metilamin", ["Ammiak", "Anilin", "Suv"], "Metil guruh azotga elektron beradi: asoslik ammiakdan kuchli.", M, ("Ammiak", "Alifatik aminlar ammiakdan kuchliroq asos.")),
  C("Anilinning asoslik xossasi ammiakka nisbatan qanday?", "Kuchsizroq", ["Kuchliroq", "Metilamindan kuchliroq", "Asos emas"], "Benzol halqasi azotning elektron juftini tortadi.", A, ("Kuchliroq", "Aromatik halqa asoslikni pasaytiradi.")),
 ]),
]
G = "Nitrit kislota ta'siri"
slots += [
 S("h-1", G, "write", 2, [
  W("Etilaminga nitrit kislota ta'sir ettiring", ["C2H7N", "HNO2"], ["C2H6O", "N2", "H2O"], "C2H7N+HNO2→C2H6O+N2+H2O", "Birlamchi alifatik amin spirtga aylanadi, azot ajraladi.", E),
  W("Metilaminga nitrit kislota ta'sir ettiring", ["CH5N", "HNO2"], ["CH4O", "N2", "H2O"], "CH5N+HNO2→CH4O+N2+H2O", "Metanol hosil bo'ladi, azot gazi ajraladi.", M),
 ]),
 S("h-2", G, "write", 2, [
  W("Anilinga nitrit kislota va xlorid kislota ta'sir ettiring (0–5 °C)", ["C6H7N", "HNO2", "HCl"], ["C6H5ClN2", "H2O"], "C6H7N+HNO2+HCl→C6H5ClN2+2H2O", "Diazoniy tuzi hosil bo'ladi.", A),
  W("Anilinga nitrit kislota ta'sir ettiring (qizdirish)", ["C6H7N", "HNO2"], ["C6H6O", "N2", "H2O"], "C6H7N+HNO2→C6H6O+N2+H2O", "Yuqori haroratda fenol va azot hosil bo'ladi.", A),
 ]),
 S("h-3", G, "choice", 3, [
  C("Ikkilamchi aminga nitrit kislota ta'sir ettirilsa, nima hosil bo'ladi?", "N-nitrozoamin (sariq yog'simon modda)", ["Spirt va N₂", "Diazoniy tuzi", "Tuz"], "Azotda bitta vodorod bor, u NO guruhi bilan almashinadi.", E, ("Spirt va N₂", "Spirt va N₂ birlamchi alifatik aminlardan hosil bo'ladi.")),
  C("Uchlamchi aminga nitrit kislota ta'sir ettirilsa, nima hosil bo'ladi?", "Faqat tuz (nitrit)", ["N₂ ajraladi", "Nitrozoamin", "Diazoniy tuzi"], "Uchlamchi aminda almashinadigan vodorod yo'q: faqat tuz hosil bo'ladi.", M, ("Nitrozoamin", "Nitrozoamin ikkilamchi aminlardan hosil bo'ladi.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 2, [
  W("Metilaminning to'liq yonishini yozing (azot erkin holda ajraladi)", ["CH5N", "O2"], ["CO2", "H2O", "N2"], "4CH5N+9O2→4CO2+10H2O+2N2", "Azot atomlari N₂ ga birikadi: koeffitsientlar 4, 9, 4, 10, 2.", M),
  W("Etilaminning to'liq yonishini yozing (azot erkin holda ajraladi)", ["C2H7N", "O2"], ["CO2", "H2O", "N2"], "4C2H7N+15O2→8CO2+14H2O+2N2", "Azot atomlari N₂ ga birikadi.", E),
 ]),
 S("k-2", G, "choice", 2, [
  C("Anilin havoda uzoq turganda nima bo'ladi?", "Oksidlanib qorayadi", ["Rangsiz qoladi", "Qizaradi", "Ko'karadi"], "Aromatik aminlar havo kislorodida oksidlanadi.", A, ("Rangsiz qoladi", "Anilin oksidlanuvchan: rangi qorayadi.")),
  C("Anilinga bromli suv ta'sir ettirilsa, nima kuzatiladi?", "Oq cho'kma (2,4,6-tribromanilin)", ["Rang o'zgarmaydi", "Binafsha rang", "Gaz ajraladi"], "NH₂ guruhi halqani faollashtiradi: uchala o,p-holat bromlanadi.", A, ("Rang o'zgarmaydi", "Anilin benzoldan ancha faol: bromli suv bilan darhol reaksiya.")),
 ]),
]
G = "Almashinish va atsillash"
slots += [
 S("a-1", G, "write", 2, [
  W("Anilinga ortiqcha bromli suv ta'sir ettiring", ["C6H7N", "Br2"], ["C6H4Br3N", "HBr"], "C6H7N+3Br2→C6H4Br3N+3HBr", "NH₂ o,p-yo'naltiruvchi: 2, 4, 6 holatlar bromlanadi.", A),
  W("Anilinga konsentrlangan H₂SO₄ ta'sir ettiring (sulfolash)", ["C6H7N", "H2SO4"], ["C6H7NO3S", "H2O"], "C6H7N+H2SO4→C6H7NO3S+H2O", "Sulfanil kislota hosil bo'ladi.", A),
 ]),
 S("a-2", G, "write", 3, [
  W("Etilaminga atsetilxlorid ta'sir ettiring", ["C2H7N", "C2H3ClO"], ["C4H9NO", "HCl"], "C2H7N+C2H3ClO→C4H9NO+HCl", "N-etilatsetamid (atsillash) hosil bo'ladi.", E),
  W("Anilinga atsetilxlorid ta'sir ettiring", ["C6H7N", "C2H3ClO"], ["C8H9NO", "HCl"], "C6H7N+C2H3ClO→C8H9NO+HCl", "Atsetanilid hosil bo'ladi.", A),
 ]),
]
G = "Zanjir"
cA = {"all": ["C6H6", "C6H5NO2", "C6H7N", "C8H9NO"]}
cB = {"all": ["C2H4", "C2H5Br", "C2H7N", "C3H9N"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (H₂SO₄, nitrolash)", ["C6H6", "HNO3"], ["C6H5NO2", "H2O"], "C6H6+HNO3→C6H5NO2+H2O", "Nitro guruh halqaga birikadi.", A, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing", ["C2H4", "HBr"], ["C2H5Br"], "C2H4+HBr→C2H5Br", "Etilenga HBr birikadi.", None, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (rux va xlorid kislota)", ["C6H5NO2", "Zn", "HCl"], ["C6H7N", "ZnCl2", "H2O"], "C6H5NO2+3Zn+6HCl→C6H7N+3ZnCl2+2H2O", "Rux qaytaruvchi: nitro guruh aminoguruhga o'tadi.", A, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (ortiqcha ammiak)", ["C2H5Br", "NH3"], ["C2H7N", "NH4Br"], "C2H5Br+2NH3→C2H7N+NH4Br", "Etilamin va ammoniy bromid hosil bo'ladi.", E, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing (sirka angidrid)", ["C6H7N", "C4H6O3"], ["C8H9NO", "C2H4O2"], "C6H7N+C4H6O3→C8H9NO+C2H4O2", "Anilin atsillanadi: atsetanilid.", A, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (yodmetan, alkillash)", ["C2H7N", "CH3I"], ["C3H9N", "HI"], "C2H7N+CH3I→C3H9N+HI", "Azotdagi vodorod metilga almashinadi.", E, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(22, "Aminlar", ["metilamin", "etilamin", "anilin"], slots)
