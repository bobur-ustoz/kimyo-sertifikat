# Izozarrachalar mavzusi: 20 misolning analog savollari (video tushuntirishlariga asoslangan).
import json, pathlib
# (savol, to'g'ri, [3 noto'g'ri], to'g'ri javob harfi, yechim)
Q = [
("Quyidagi atomlardan qaysi biri ³⁵Cl atomiga izotop bo'ladi? (tartib raqamlari: S-16, Cl-17, Ar-18, K-19)",
 "³⁷Cl", ["³⁵S", "⁴⁰Ar", "³⁹K"], "B",
 "Izotoplarning protonlar soni (tartib raqami) bir xil bo'ladi, ya'ni ular bir elementning atomlari. ³⁵Cl va ³⁷Cl ning tartib raqami 17."),
("Uglerod izotoplari ¹²C, ¹³C va ¹⁴C tarkibidagi elektronlar yig'indisini toping.",
 "18", ["6", "12", "39"], "A",
 "Protonlar soni (tartib raqami) o'zgarmaydi, neytral atomda elektron ham 6 ta. Uchta izotopda: 6 + 6 + 6 = 18."),
("Izobarlarning qaysi xususiyatlari turlicha bo'ladi?\n1) atom massasi; 2) protonlar soni; 3) neytronlar soni; 4) massa soni",
 "2, 3", ["1, 2", "1, 4", "3, 4"], "C",
 "Izobarlarda atom massasi (massa soni) bir xil. Massa soni = p + n bo'lgani uchun protonlar va neytronlar soni turlicha bo'ladi."),
("Na⁺, O²⁻ va N³⁻ tarkibida qaysi zarrachalar soni o'zaro teng? (Na: A=23, Z=11; O: A=16, Z=8; N: A=14, Z=7)",
 "elektronlar", ["neytronlar", "protonlar", "massa soni"], "D",
 "Na⁺: e = 11 − 1 = 10; O²⁻: e = 8 + 2 = 10; N³⁻: e = 7 + 3 = 10. Protonlar 11, 8, 7; neytronlar 12, 8, 7; massa soni 23, 16, 14: farqli. Teng bo'lgani elektronlar soni."),
("Massa sonlari bir xil, yadro zaryadlari turlicha bo'lgan atomlar qanday umumiy nom bilan ataladi?",
 "izobarlar", ["izotoplar", "izotonlar", "izoelektronlar"], "A",
 "Izobarlarda atom massasi bir xil, yadro zaryadi (proton soni) har xil bo'ladi. Izotoplarda proton, izotonlarda neytron, izoelektronlarda elektron soni bir xil."),
("Izobarlar joylashgan qatorni ko'rsating.",
 "⁵⁰Ti, ⁵⁰V, ⁵⁰Cr", ["³²S, ³³S, ³⁴S", "¹²C, ¹⁴N, ¹⁶O", "⁴⁰Ar, ³⁹K, ³⁷Cl"], "D",
 "Izobar: atom massalari bir xil. ⁵⁰Ti, ⁵⁰V, ⁵⁰Cr qatorida hammasi 50. Boshqa qatorlarda massalar har xil; ³²S, ³³S, ³⁴S izotoplar."),
("Izobarlarni tanlang.\n1) ⁴⁰Ca; 2) ³⁹K; 3) ⁴⁰Ar; 4) ³⁵Cl; 5) ⁴⁰K; 6) ³⁷Cl",
 "1, 3, 5", ["2, 4", "4, 6", "1, 2, 3"], "A",
 "Izobar: massa soni bir xil. 40 raqami 1-, 3- va 5-zarrachada bor (⁴⁰Ca, ⁴⁰Ar, ⁴⁰K)."),
("Izotonlar keltirilgan qatorni belgilang.",
 "³⁹K (Z=19) va ⁴⁰Ca (Z=20)", ["¹⁶O (Z=8) va ¹⁹F (Z=9)", "³⁵Cl (Z=17) va ³⁷Cl (Z=17)", "²³Na (Z=11) va ²⁷Al (Z=13)"], "C",
 "Neytronlar soni N = A − Z. Na: 23 − 11 = 12, Al: 27 − 13 = 14 (teng emas). O: 8, F: 10. Cl: 18 va 20. K: 39 − 19 = 20, Ca: 40 − 20 = 20. Neytronlari teng qator: ³⁹K va ⁴⁰Ca."),
("Atomlarni mos ravishda a) izotop; b) izoton; c) izobarlarga ajrating.\n1) ⁴⁰Ar (Z=18); 2) ⁴⁰Ca (Z=20); 3) ⁴²Ca (Z=20)",
 "a) 2, 3; b) 1, 3; c) 1, 2", ["a) 1, 2; b) 2, 3; c) 1, 3", "a) 1, 3; b) 1, 2; c) 2, 3", "a) 1, 2; b) 1, 3; c) 2, 3"], "B",
 "Neytronlar: 1) 40 − 18 = 22; 2) 40 − 20 = 20; 3) 42 − 20 = 22. Izotop (Z bir xil): 2 va 3. Izoton (N bir xil): 1 va 3. Izobar (A bir xil): 1 va 2."),
("Izotonlar keltirilgan qatorni toping.",
 "¹⁸O (Z=8), ¹⁹F (Z=9), ²⁰Ne (Z=10)", ["¹²C, ¹³C, ¹⁴C", "¹⁴C (Z=6) va ¹⁴N (Z=7)", "²⁴Mg (Z=12) va ²⁸Si (Z=14)"], "D",
 "Neytron = A − Z. ¹⁸O: 10; ¹⁹F: 10; ²⁰Ne: 10: hammasida teng. Izotonlar neytronlari bir xil atomlar. ¹²C, ¹³C, ¹⁴C izotop; ¹⁴C va ¹⁴N izobar; Mg: 12, Si: 14 teng emas."),
("Atomlarni mos ravishda a) izotop; b) izoton; c) izobarlarga ajrating.\n1) ²⁸Si (Z=14); 2) ²⁹Si (Z=14); 3) ²⁹P (Z=15)",
 "a) 1, 2; b) 1, 3; c) 2, 3", ["a) 1, 3; b) 1, 2; c) 2, 3", "a) 1, 2; b) 2, 3; c) 1, 3", "a) 2, 3; b) 1, 2; c) 1, 3"], "C",
 "Neytronlar: 1) 28 − 14 = 14; 2) 29 − 14 = 15; 3) 29 − 15 = 14. Izotop (Z bir xil): 1 va 2. Izoton (N bir xil): 1 va 3. Izobar (A bir xil): 2 va 3."),
("Izotonlarning qaysi xususiyati bir xil bo'ladi?\n1) protonlar soni; 2) neytronlar soni; 3) massa soni; 4) elektronlar soni",
 "faqat 2", ["faqat 1", "1 va 2", "2 va 3"], "B",
 "Izotonlarda faqat neytronlar soni bir xil. Protonlar, massa soni va elektronlar soni turlicha."),
("Elektronlar soni bir xil bo'lgan zarrachalarni aniqlang.\n1) Ca²⁺; 2) Cl⁻; 3) Na⁺; 4) S²⁻; 5) K⁺",
 "1, 2, 4, 5", ["1, 2, 3", "2, 3, 4", "1, 3, 5"], "A",
 "Ca²⁺: 20 − 2 = 18; Cl⁻: 17 + 1 = 18; Na⁺: 11 − 1 = 10; S²⁻: 16 + 2 = 18; K⁺: 19 − 1 = 18. Na⁺ ajralib turadi."),
("Quyidagi qatorlardan qaysi birida hamma ionlar izoelektron?",
 "Mg²⁺, O²⁻, F⁻", ["Li⁺, Na⁺, K⁺", "Mg²⁺, O²⁻, Cl⁻", "Fe²⁺, Na⁺, F⁻"], "D",
 "Mg²⁺: 12 − 2 = 10; O²⁻: 8 + 2 = 10; F⁻: 9 + 1 = 10. Boshqa qatorlarda sonlar turlicha: Li⁺ 2, Na⁺ 10, K⁺ 18; Cl⁻ 18; Fe²⁺ 24."),
("Elektronlar soni bir xil bo'lgan ionlarni ko'rsating.\n1) Fe³⁺; 2) Mn²⁺; 3) Cr²⁺; 4) Co³⁺; 5) V²⁺",
 "1 va 2", ["2 va 3", "3 va 4", "4 va 5"], "A",
 "Fe³⁺: 26 − 3 = 23; Mn²⁺: 25 − 2 = 23; Cr²⁺: 24 − 2 = 22; Co³⁺: 27 − 3 = 24; V²⁺: 23 − 2 = 21. Teng bo'lgani 1 va 2."),
("Izotoplarga oid to'g'ri fikrlarni aniqlang.\n1) protonlar soni bir xil; 2) neytronlar soni bir xil; 3) elektronlar soni bir xil; 4) massa sonlari turlicha; 5) yadro zaryadi turlicha",
 "1, 3, 4", ["1, 2, 3", "2, 4, 5", "1, 4, 5"], "C",
 "Izotoplarda proton soni (yadro zaryadi) va elektron soni bir xil, neytron soni va massa soni turlicha."),
("Izotoplarning qaysi xususiyatlari turlicha bo'ladi?\n1) protonlar soni; 2) neytronlar soni; 3) elektronlar soni; 4) yadro zaryadi; 5) massa soni",
 "2, 5", ["1, 4", "1, 2, 5", "2, 3, 5"], "B",
 "Izotoplarda protonlar, elektronlar soni va yadro zaryadi bir xil. Turlicha bo'lganlari: neytronlar soni va massa soni."),
("Qaysi atom ³⁹K (Z=19) uchun izotop ham, izobar ham, izoton ham emas? (Z: Ar-18, Ca-20, Cl-17)",
 "³⁵Cl", ["⁴¹K", "³⁹Ar", "⁴⁰Ca"], "D",
 "⁴¹K: Z bir xil, izotop. ³⁹Ar: massa 39, izobar. ⁴⁰Ca: N = 40 − 20 = 20, ³⁹K da N = 39 − 19 = 20, izoton. ³⁵Cl: Z = 17, A = 35, N = 18: hech biriga kirmaydi."),
("Izotop va izobar juftliklarni toping.\n1) ³⁹K (Z=19); 2) ⁴⁰K (Z=19); 3) ⁴⁰Ca (Z=20)",
 "izotop: 1, 2; izobar: 2, 3", ["izotop: 2, 3; izobar: 1, 2", "izotop: 1, 2; izobar: 1, 3", "izotop: 1, 3; izobar: 2, 3"], "C",
 "Izotop: protonlari bir xil, 1 va 2 (ikkalasi kaliy). Izobar: massa soni bir xil (40), 2 va 3."),
("Jadvalga qarab noto'g'ri fikrni aniqlang. X⁻ (p=9, n=10); Y⁺ (p=11, n=12); Z²⁺ (p=12, n=12); T (p=9, n=9).",
 "X⁻ va Y⁺ o'zaro izobar", ["X⁻ va Y⁺ o'zaro izoelektron", "X⁻ va T o'zaro izotop", "Y⁺ va Z²⁺ o'zaro izoton"], "A_",
 "Elektronlar: X⁻ 10, Y⁺ 10: izoelektron (to'g'ri). X va T ning protonlari 9: izotop (to'g'ri). Y⁺ va Z²⁺ da n = 12: izoton (to'g'ri). Massa soni X: 19, Y: 23, izobar emas. Noto'g'ri fikr: X⁻ va Y⁺ izobar."),
]
# javob joylashuvi (har harf teng taqsimlansin): A B C D
POS = "BADCABDACBDACAD".replace(" ","")
POS = ["B","A","C","D","A","D","A","C","B","D","C","B","A","D","A","B","C","D","C","A"]
out = []
for i, (s, ok, bad, _, yech) in enumerate(Q):
    L = POS[i]; idx = "ABCD".index(L)
    opts = bad[:]; opts.insert(idx, ok)
    text = s + "\n" + "\n".join(f"{l}) {o}" for l, o in zip("ABCD", opts))
    out.append({"example_number": i+1, "analog_savol": text, "analog_yechim": yech, "analog_javob": f"{L}) {ok}"})
pathlib.Path(__file__).with_name("izozarrachalar_analog.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(len(out), "".join(POS))
