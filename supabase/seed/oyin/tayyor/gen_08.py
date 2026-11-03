from lib import *
A, R, K = ["allil spirt"], ["propargil spirt"], ["krotil spirt"]
slots = []
G = "Olinish"
slots += [
 S("o-1", G, "write", 1, [
  W("Allilxloridga NaOH ning suvdagi eritmasi ta'sir ettiring", ["C3H5Cl", "NaOH"], ["C3H6O", "NaCl"], "C3H5Cl+NaOH→C3H6O+NaCl", "Xlor OH ga almashinadi, qo'shbog' saqlanadi: allil spirt.", A),
  W("Propargilbromidga NaOH ning suvdagi eritmasi ta'sir ettiring", ["C3H3Br", "NaOH"], ["C3H4O", "NaBr"], "C3H3Br+NaOH→C3H4O+NaBr", "Brom OH ga almashinadi, uchbog' saqlanadi: propargil spirt.", R),
 ]),
 S("o-2", G, "write", 2, [
  W("Allilbromidga KOH ning suvdagi eritmasi ta'sir ettiring", ["C3H5Br", "KOH"], ["C3H6O", "KBr"], "C3H5Br+KOH→C3H6O+KBr", "Brom OH ga almashinadi: allil spirt.", A),
  W("Krotonaldegidni gidrogenlang (faqat aldegid guruhi qaytariladi)", ["C4H6O", "H2"], ["C4H8O"], "C4H6O+H2→C4H8O", "Krotil spirt hosil bo'ladi.", K),
 ]),
 S("o-3", G, "write", 2, [
  W("Atsetilen va formaldegid reaksiyasini yozing (Cu₂C₂, Reppe): propargil spirt olinadi", ["C2H2", "CH2O"], ["C3H4O"], "C2H2+CH2O→C3H4O", "Formaldegid atsetilenning uchbog'dagi vodorodiga birikadi.", R),
  W("Atsetilen va aseton reaksiyasini yozing (KOH, Favorskiy)", ["C2H2", "C3H6O"], ["C5H8O"], "C2H2+C3H6O→C5H8O", "Aseton karbonili atsetilenga birikib 2-metilbutin-3-ol-2 hosil qiladi.", None),
 ]),
 S("o-4", G, "choice", 1, [
  C("Allil spirtning tuzilish formulasi qaysi?", "CH₂=CH–CH₂OH", ["CH₃–CH=CH–OH", "CH₃–CH₂–CH₂OH", "CH₂=C(OH)–CH₃"], "Qo'shbog' va OH guruhi turli uglerodlarda.", A, ("CH₃–CH=CH–OH", "OH qo'shbog'li uglerodda: bunday enol beqaror, aldegidga o'tadi.")),
  C("Propargil spirtning tuzilish formulasi qaysi?", "HC≡C–CH₂OH", ["CH₂=CH–CH₂OH", "CH₃–C≡C–OH", "HC≡C–CH₃"], "Uchbog' va OH guruhi turli uglerodlarda.", R, ("CH₃–C≡C–OH", "OH uchbog'li uglerodda bo'lmaydi: beqaror.")),
 ]),
 S("o-5", G, "choice", 2, [
  C("Atsetilen va formaldegiddan propargil spirt olishda qaysi katalizator ishlatiladi?", "Cu₂C₂ (mis atsetilenidi)", ["Ni", "H₂SO₄", "AlCl₃"], "Mis atsetilenidi atsetilen bilan karbonil birikmasini bog'laydi.", R),
  C("Allilxloriddan allil spirt olish qaysi sharoitda amalga oshadi?", "NaOH ning suvdagi eritmasi", ["NaOH ning spirtdagi eritmasi", "H₂SO₄ (konsentrlangan)", "HCl"], "Suvli ishqorda almashinish bo'ladi.", A, ("NaOH ning spirtdagi eritmasi", "Spirtli ishqor galogenalkandan HCl ni ajratib dien beradi.")),
 ]),
]
G = "Birikish"
slots += [
 S("b-1", G, "write", 1, [
  W("Allil spirtni gidrogenlang (Ni)", ["C3H6O", "H2"], ["C3H8O"], "C3H6O+H2→C3H8O", "Qo'shbog' to'yinadi: propanol-1.", A),
  W("Krotil spirtni gidrogenlang (Ni)", ["C4H8O", "H2"], ["C4H10O"], "C4H8O+H2→C4H10O", "Qo'shbog' to'yinadi: butanol-1.", K),
 ]),
 S("b-2", G, "write", 1, [
  W("Allil spirtga brom ta'sir ettiring", ["C3H6O", "Br2"], ["C3H6Br2O"], "C3H6O+Br2→C3H6Br2O", "Brom qo'shbog'ga birikadi: 2,3-dibrompropanol-1.", A),
  W("Propargil spirtga ortiqcha brom ta'sir ettiring", ["C3H4O", "Br2"], ["C3H4Br4O"], "C3H4O+2Br2→C3H4Br4O", "Uchbog'ga ikki molekula brom birikadi.", R),
 ]),
 S("b-3", G, "write", 2, [
  W("Allil spirtga HBr ta'sir ettiring (qo'shbog'ga birikish)", ["C3H6O", "HBr"], ["C3H7BrO"], "C3H6O+HBr→C3H7BrO", "H va Br qo'shbog'ga birikadi.", A),
  W("Propargil spirtni to'liq gidrogenlang (Ni)", ["C3H4O", "H2"], ["C3H8O"], "C3H4O+2H2→C3H8O", "Uchbog' to'liq to'yinadi: propanol-1.", R),
 ]),
 S("b-4", G, "choice", 2, [
  C("Allil spirt bromli suvni rangsizlantiradimi?", "Ha", ["Yo'q", "Faqat qizdirilganda", "Faqat yorug'likda"], "Molekulada qo'shbog' bor: brom oson birikadi.", A, ("Yo'q", "To'yingan spirtlar rangsizlantirmaydi, lekin allil spirtda qo'shbog' bor.")),
  C("Propargil spirt KMnO₄ eritmasini rangsizlantiradimi?", "Ha: uchbog' tufayli", ["Yo'q", "Faqat sovuqda", "Faqat ishqoriy muhitda"], "Uchbog' oksidlanadi, eritma rangsizlanadi.", R, ("Yo'q", "Ko'p bog'li moddalar KMnO₄ ni oson rangsizlantiradi.")),
 ]),
 S("b-5", G, "choice", 3, [
  C("0,1 mol allil spirt necha gramm brom (M = 160) biriktira oladi?", "16 g", ["8 g", "32 g", "160 g"], "Bitta qo'shbog'ga 1 mol brom: 0,1 · 160 = 16 g.", A, ("32 g", "32 g ikki qo'shbog'ga to'g'ri kelardi. Allil spirtda bitta qo'shbog' bor.")),
  C("0,1 mol propargil spirtga ortiqcha brom ta'sir etsa, necha gramm brom (M = 160) birikadi?", "32 g", ["16 g", "8 g", "64 g"], "Uchbog'ga 2 mol brom: 0,2 · 160 = 32 g.", R, ("16 g", "16 g bitta mol bromning yarmi: bitta qo'shbog'ga to'g'ri keladi, uchbog'ga emas.")),
 ]),
]
G = "OH hisobiga"
slots += [
 S("m-1", G, "write", 1, [
  W("Allil spirtga natriy ta'sir ettiring", ["C3H6O", "Na"], ["C3H5NaO", "H2"], "2C3H6O+2Na→2C3H5NaO+H2", "OH vodorodi natriyga almashinadi: natriy allilat.", A),
  W("Krotil spirtga natriy ta'sir ettiring", ["C4H8O", "Na"], ["C4H7NaO", "H2"], "2C4H8O+2Na→2C4H7NaO+H2", "Natriy krotilat va vodorod hosil bo'ladi.", K),
 ]),
 S("m-2", G, "write", 2, [
  W("Allil spirt va sirka kislota reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["C3H6O", "C2H4O2"], ["C5H8O2", "H2O"], "C3H6O+C2H4O2→C5H8O2+H2O", "Allil atsetat hosil bo'ladi, suv ajraladi.", A),
  W("Propargil spirt va sirka kislota reaksiyasini yozing (H₂SO₄, eterifikatsiya)", ["C3H4O", "C2H4O2"], ["C5H6O2", "H2O"], "C3H4O+C2H4O2→C5H6O2+H2O", "Propargil atsetat hosil bo'ladi.", R),
 ]),
 S("m-3", G, "write", 2, [
  W("Allil spirtga fosfor(V) xlorid ta'sir ettiring", ["C3H6O", "PCl5"], ["C3H5Cl", "POCl3", "HCl"], "C3H6O+PCl5→C3H5Cl+POCl3+HCl", "OH xlorga almashinadi, qo'shbog' saqlanadi.", A),
  W("Allil spirtga tionilxlorid ta'sir ettiring", ["C3H6O", "SOCl2"], ["C3H5Cl", "SO2", "HCl"], "C3H6O+SOCl2→C3H5Cl+SO2+HCl", "Gazlar ajraladi, allilxlorid hosil bo'ladi.", A),
 ]),
 S("m-4", G, "choice", 3, [
  C("Allil spirt molekulasida qaysi funksional guruhlar bor?", "–OH va C=C", ["–OH va C≡C", "–CHO va C=C", "–COOH va C=C"], "Spirt guruhi va qo'shbog'.", A, ("–OH va C≡C", "Uchbog' propargil spirtda.")),
  C("Propargil spirt molekulasida qaysi funksional guruhlar bor?", "–OH va C≡C", ["–OH va C=C", "–CHO va C≡C", "–OH va C=O"], "Spirt guruhi va uchbog'.", R, ("–OH va C=C", "Qo'shbog' allil spirtda.")),
 ]),
]
G = "Oksidlanish"
slots += [
 S("k-1", G, "write", 1, [
  W("Allil spirtning to'liq yonishini yozing", ["C3H6O", "O2"], ["CO2", "H2O"], "C3H6O+4O2→3CO2+3H2O", "Kislorod: 6 + 3 − 1 = 8 atom, ya'ni 4 O₂.", A),
  W("Propargil spirtning to'liq yonishini yozing", ["C3H4O", "O2"], ["CO2", "H2O"], "2C3H4O+7O2→6CO2+4H2O", "Kasr chiqadi (3,5): ikki baravar qilinadi.", R),
 ]),
 S("k-2", G, "write", 2, [
  W("Allil spirtni CuO bilan oksidlang (qizdirish)", ["C3H6O", "CuO"], ["C3H4O", "Cu", "H2O"], "C3H6O+CuO→C3H4O+Cu+H2O", "Spirt guruhi aldegidga o'tadi, qo'shbog' saqlanadi: akrolein.", A),
  W("Krotil spirtni CuO bilan oksidlang (qizdirish)", ["C4H8O", "CuO"], ["C4H6O", "Cu", "H2O"], "C4H8O+CuO→C4H6O+Cu+H2O", "Krotonaldegid hosil bo'ladi.", K),
 ]),
 S("k-3", G, "write", 3, [
  W("Allil spirtni KMnO₄ ning suvli eritmasi bilan oksidlang (Vagner)", ["C3H6O", "KMnO4", "H2O"], ["C3H8O3", "MnO2", "KOH"], "3C3H6O+2KMnO4+4H2O→3C3H8O3+2MnO2+2KOH", "Qo'shbog'ga ikkita OH birikadi: glitserin hosil bo'ladi.", A),
  W("Krotil spirtni KMnO₄ ning suvli eritmasi bilan oksidlang (Vagner)", ["C4H8O", "KMnO4", "H2O"], ["C4H10O3", "MnO2", "KOH"], "3C4H8O+2KMnO4+4H2O→3C4H10O3+2MnO2+2KOH", "Qo'shbog' glikolga aylanadi: uch atomli spirt.", K),
 ]),
 S("k-4", G, "choice", 3, [
  C("Allil spirt CuO bilan yengil oksidlansa, qaysi modda hosil bo'ladi?", "Akrolein (propenal)", ["Propanal", "Akril kislota", "Aseton"], "Faqat spirt guruhi oksidlanadi, qo'shbog' saqlanadi.", A, ("Propanal", "Propanal qo'shbog'siz modda: u gidrogenlashda ham chiqadi, bu yerda esa qo'shbog' qoladi.")),
  C("Akroleinni (CH₂=CH–CHO) faqat aldegid guruhi bo'yicha qaytarsak, qaysi modda hosil bo'ladi?", "Allil spirt", ["Propanol-1", "Propanol-2", "Propanal"], "Qo'shbog' saqlanadi, C=O dan CH₂OH hosil bo'ladi.", A, ("Propanol-1", "Propanol-1 hosil bo'lishi uchun qo'shbog' ham gidrogenlanishi kerak edi.")),
 ]),
]
G = "Enol–keton izomerlanishi"
slots += [
 S("e-1", G, "choice", 1, [
  C("Vinil spirt (CH₂=CH–OH) barqarormi?", "Yo'q: sirka aldegidga izomerlanadi", ["Ha: barqaror", "Ha, suvda eriydi", "Yo'q: alkenga aylanadi"], "OH qo'shbog'li uglerodda bo'lsa, vodorod ko'chib karbonil guruhi hosil bo'ladi.", None, ("Ha: barqaror", "Eltekov qoidasi: bunday enol darhol karbonil birikmaga o'tadi.")),
  C("Eltekov qoidasi nimani bildiradi?", "OH qo'shbog'li uglerodda bo'lsa, enol karbonilga izomerlanadi", ["Vodorod kamroq vodorodli uglerodga birikadi", "Qo'shbog' o'rtada barqarorroq", "Spirt degidratlanib alken hosil qiladi"], "Enol shaklidan karbonil shakliga o'tish.", None, ("Vodorod kamroq vodorodli uglerodga birikadi", "Bu Markovnikov qoidasi.")),
 ]),
 S("e-2", G, "write", 2, [
  W("Vinilatsetatning gidrolizini yozing (CH₃COOCH=CH₂ + suv)", ["C4H6O2", "H2O"], ["C2H4O2", "C2H4O"], "C4H6O2+H2O→C2H4O2+C2H4O", "Hosil bo'lgan vinil spirt aldegidga o'tadi.", None),
  W("Izopropenilatsetatning gidrolizini yozing (suv ta'sirida)", ["C5H8O2", "H2O"], ["C2H4O2", "C3H6O"], "C5H8O2+H2O→C2H4O2+C3H6O", "Enol aseton (keton) ga izomerlanadi.", None),
 ]),
 S("e-3", G, "choice", 3, [
  C("Propin gidratlanganda aseton hosil bo'lishi qaysi qoidaga asoslangan?", "Eltekov: enol → keton", ["Markovnikov", "Zaytsev", "Vyurs"], "Dastlab enol hosil bo'ladi va keton shakliga o'tadi.", None, ("Markovnikov", "Markovnikov OH ning joylashuvini belgilaydi. Enolning ketonga o'tishi esa Eltekov qoidasi.")),
  C("CH₂=C(OH)–CH₃ izomerlanib qaysi modda hosil qiladi?", "Aseton", ["Propanal", "Allil spirt", "Propanol-2"], "OH qo'shbog'li uglerodda: karbonil shaklga o'tadi.", None, ("Propanal", "Propanal aldegid, enolda OH ikkinchi uglerodda, shuning uchun keton.")),
 ]),
]
G = "Zanjir"
cA = {"all": ["C3H6", "C3H5Cl", "C3H6O", "C3H6Cl2O"]}
cB = {"all": ["C3H4O", "C3H6O", "C3H5Br", "C6H10"]}
slots += [
 S("z-1", G, "write", 2, [
  W("Zanjirning 1-reaksiyasini yozing (500 °C)", ["C3H6", "Cl2"], ["C3H5Cl", "HCl"], "C3H6+Cl2→C3H5Cl+HCl", "Yuqori haroratda alil holatdagi vodorod xlorga almashinadi.", None, {**cA, "at": 0}, "A"),
  W("Zanjirning 1-reaksiyasini yozing (Pd, qisman gidrogenlash)", ["C3H4O", "H2"], ["C3H6O"], "C3H4O+H2→C3H6O", "Uchbog' qo'shbog'gacha qaytariladi: allil spirt.", R, {**cB, "at": 0}, "B"),
 ], "zanjir"),
 S("z-2", G, "write", 2, [
  W("Zanjirning 2-reaksiyasini yozing (KOH ning suvdagi eritmasi)", ["C3H5Cl", "KOH"], ["C3H6O", "KCl"], "C3H5Cl+KOH→C3H6O+KCl", "Xlor OH ga almashinadi: allil spirt.", A, {**cA, "at": 1}, "A"),
  W("Zanjirning 2-reaksiyasini yozing (HBr, qizdirish)", ["C3H6O", "HBr"], ["C3H5Br", "H2O"], "C3H6O+HBr→C3H5Br+H2O", "OH bromga almashinadi: allilbromid.", A, {**cB, "at": 1}, "B"),
 ], "zanjir"),
 S("z-3", G, "write", 3, [
  W("Zanjirning 3-reaksiyasini yozing", ["C3H6O", "Cl2"], ["C3H6Cl2O"], "C3H6O+Cl2→C3H6Cl2O", "Xlor qo'shbog'ga birikadi.", A, {**cA, "at": 2}, "A"),
  W("Zanjirning 3-reaksiyasini yozing (Vyurs)", ["C3H5Br", "Na"], ["C6H10", "NaBr"], "2C3H5Br+2Na→C6H10+2NaBr", "Ikki allil radikal birlashadi: geksadien-1,5.", None, {**cB, "at": 2}, "B"),
 ], "zanjir"),
]
save(8, "Bir atomli to'yinmagan spirtlar", ["allil spirt", "propargil spirt", "krotil spirt"], slots)
