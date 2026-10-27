# 20 variantli to'plam — REJA (spetsifikatsiya bo'yicha)

## 1. Umumiy qoidalar
- Har variant: 43 savol, rasmiy spetsifikatsiya tuzilmasi (1–13 umumiy, 14–19 anorganik, 20–29 organik, 30–32 tahlil, 33–35 moslashtirish, 36–40 qisqa javob, 41–43 yozma).
- Manba: faqat siz bergan darsliklar (konspekt). Real variantlardagi (Muhtasham, Samarqand, tushgan) rasmli/jadvalli savol turlari namuna; mazmun va hisoblar o'zimizniki, har javob Python bilan tekshiriladi.
- Organik 20–29: har variantda spetsifikatsiyaning 10 mavzusidan bittadan.
- Har variant fayllari: `.md` (savol+yechim), Tongotarov uslubidagi PDF, Word.

## 2. Rasm / jadval / grafik / laboratoriya kvotasi (har variantda)
| Tur | Soni | Qayerda |
|---|---|---|
| Rasmli (molekula, orbital, asbob, tarozi, idishlar) | 3–4 | 1–13 dan 2, 20–29 dan 1, 30–32 dan 1 |
| Jadvalli | 2–3 | tezlik/muvozanat/eritma, ion juftlari, sifat reaksiya |
| Grafikli | 2 | eruvchanlik, konsentratsiya–vaqt, pH |
| Laboratoriya (asbob rasmi yoki tajriba natijasi) | 3 (30–32) | etilen, ajratish, gaz yig'ish, sifat reaksiya |
| Jami rasm+jadval+grafik | taxminan 9–10 savol/variant | |

## 3. Rasm manbalari
- Darslik rasmlari (7-sinf ajratish; 10-sinf etilen, biuret, glitserin; 11-sinf, Tirkashev) skanerdan kesiladi.
- Siz bergan toza chizmalar (ajratish, etilen) qayta ishlatiladi.
- Muhtasham 26 faylidagi rasmlar (orbital, tarozi, grafiklar, balonlar) — mosi qo'shiladi.
- Grafik/jadval — matplotlib bilan bir xil uslubda.
- Yetishmasa: yangi asbob/probirka rasmlari sizdan yoki boshqa fayllardan olinadi (qo'lda sxematik chizmayman — sizga yoqmadi).

## 4. Umumiy kimyo mavzu taqsimoti (20 variant × 13 = 260 o'rin)
| Mavzu | O'rin | Variantiga o'rtacha |
|---|---|---|
| mol/stexiometriya | 26 | 1.3 |
| eritma %/M/eruvchanlik | 28 | 1.4 |
| atom/davriy/izoelektron | 26 | 1.3 |
| kvant/yadro | 12 | 0.6 |
| dissotsilanish/pH/gidroliz | 26 | 1.3 |
| bog'lanish/gibridlanish | 20 | 1.0 |
| muvozanat | 18 | 0.9 |
| tezlik | 12 | 0.6 |
| OQR | 20 | 1.0 |
| elektroliz | 18 | 0.9 |
| qonunlar/gaz/ekvivalent | 26 | 1.3 |
| tushuncha/valentlik | 8 | 0.4 |
| oleum/molyal/normal | 12 | 0.6 |
| kuchlanish qatori | 8 | 0.4 |

(Real statistikada eritma, mol, atom, dissotsilanish eng ko'p; tezlik, OQR, elektroliz kamroq.)

## 5. Variant-ma-variant jadval
| № | Umumiy 1–13 (to'plam) | Anorganik 14–19 | Tahlil 30–32 | 33–35 hikoya | 41 | 43 |
|---|---|---|---|---|---|---|
| 1 | OQR ×2; atom/davriy/izoelektron ×2; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz; eritma %/M/eruvchanlik ×2; kvant/yadro; mol/stexiometriya ×2; muvozanat ×2 | S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al) | laboratoriya xavfsizlik/jihoz; ajratish usullari (rasm); eritma tayyorlash | metall+tuz eritmasi+elektroliz | elektroliz+eritma | probirkalar topishmog'i (anorganik) |
| 2 | atom/davriy/izoelektron ×2; dissotsilanish/pH/gidroliz; eritma %/M/eruvchanlik ×2; kuchlanish qatori; mol/stexiometriya ×2; muvozanat; oleum/molyal/normal; qonunlar/gaz/ekvivalent ×2; tezlik | P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi | anorganik sifat reaksiya (jadval); organik sifat reaksiya; gaz olish/yig'ish (rasm) | aralashma+kislota/ishqor (Al,Zn,Fe) | muvozanat+K+kislota | jadval+metallar (H2S, Na2S, NaOH, Zn) |
| 3 | OQR; atom/davriy/izoelektron; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz ×2; elektroliz; eritma %/M/eruvchanlik; kvant/yadro; mol/stexiometriya ×2; muvozanat ×2; qonunlar/gaz/ekvivalent | IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari | organik olish tajribasi (rasm); moddalarni aniqlash (probirka); laboratoriya xavfsizlik/jihoz | muvozanat (jadval/grafik) | oleum/kristallogidrat | ko'p bosqichli anorganik hikoya |
| 4 | OQR; atom/davriy/izoelektron ×2; bog'lanish/gibridlanish; elektroliz; eritma %/M/eruvchanlik; kuchlanish qatori; kvant/yadro; muvozanat ×2; qonunlar/gaz/ekvivalent; tezlik; tushuncha/valentlik | d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz | ajratish usullari (rasm); eritma tayyorlash; anorganik sifat reaksiya (jadval) | kristallogidrat/eruvchanlik | aralashma+OQR | tahlil: oqsil/uglevod/spirtni aniqlash |
| 5 | OQR ×2; atom/davriy/izoelektron; bog'lanish/gibridlanish ×2; dissotsilanish/pH/gidroliz; elektroliz ×2; eritma %/M/eruvchanlik; mol/stexiometriya; muvozanat ×2; tushuncha/valentlik | oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3 | organik sifat reaksiya; gaz olish/yig'ish (rasm); organik olish tajribasi (rasm) | gaz aralashma/yonish | tezlik+muvozanat jadvali | tahlil: ajratish+eritma tayyorlash |
| 6 | OQR ×2; atom/davriy/izoelektron ×2; bog'lanish/gibridlanish ×2; elektroliz; kuchlanish qatori; mol/stexiometriya; oleum/molyal/normal; qonunlar/gaz/ekvivalent ×2; tezlik | mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar | moddalarni aniqlash (probirka); laboratoriya xavfsizlik/jihoz; ajratish usullari (rasm) | oksid/karbonat+kislota | gaz qonunlari+yonish | tahlil: gaz olish+sifat reaksiya |
| 7 | atom/davriy/izoelektron; dissotsilanish/pH/gidroliz ×2; elektroliz; eritma %/M/eruvchanlik ×2; kvant/yadro; mol/stexiometriya ×2; qonunlar/gaz/ekvivalent; tezlik ×2; tushuncha/valentlik | S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al) | eritma tayyorlash; anorganik sifat reaksiya (jadval); organik sifat reaksiya | metall+tuz eritmasi+elektroliz | elektroliz+eritma | probirkalar topishmog'i (anorganik) |
| 8 | atom/davriy/izoelektron ×2; dissotsilanish/pH/gidroliz ×2; eritma %/M/eruvchanlik ×2; kvant/yadro; muvozanat; oleum/molyal/normal; qonunlar/gaz/ekvivalent ×2; tushuncha/valentlik ×2 | P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi | gaz olish/yig'ish (rasm); organik olish tajribasi (rasm); moddalarni aniqlash (probirka) | aralashma+kislota/ishqor (Al,Zn,Fe) | muvozanat+K+kislota | jadval+metallar (H2S, Na2S, NaOH, Zn) |
| 9 | OQR; atom/davriy/izoelektron; dissotsilanish/pH/gidroliz ×2; elektroliz ×2; mol/stexiometriya ×2; muvozanat; oleum/molyal/normal ×2; tezlik ×2 | IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari | laboratoriya xavfsizlik/jihoz; ajratish usullari (rasm); eritma tayyorlash | muvozanat (jadval/grafik) | oleum/kristallogidrat | ko'p bosqichli anorganik hikoya |
| 10 | OQR; atom/davriy/izoelektron ×2; dissotsilanish/pH/gidroliz ×2; eritma %/M/eruvchanlik ×2; kvant/yadro; mol/stexiometriya ×2; muvozanat; qonunlar/gaz/ekvivalent ×2 | d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz | anorganik sifat reaksiya (jadval); organik sifat reaksiya; gaz olish/yig'ish (rasm) | kristallogidrat/eruvchanlik | aralashma+OQR | tahlil: oqsil/uglevod/spirtni aniqlash |
| 11 | bog'lanish/gibridlanish ×2; dissotsilanish/pH/gidroliz; elektroliz; eritma %/M/eruvchanlik ×2; kvant/yadro ×2; mol/stexiometriya ×2; muvozanat; tushuncha/valentlik ×2 | oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3 | organik olish tajribasi (rasm); moddalarni aniqlash (probirka); laboratoriya xavfsizlik/jihoz | gaz aralashma/yonish | tezlik+muvozanat jadvali | tahlil: ajratish+eritma tayyorlash |
| 12 | OQR; atom/davriy/izoelektron; bog'lanish/gibridlanish ×2; dissotsilanish/pH/gidroliz; eritma %/M/eruvchanlik ×2; kuchlanish qatori ×2; kvant/yadro; mol/stexiometriya ×2; qonunlar/gaz/ekvivalent | mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar | ajratish usullari (rasm); eritma tayyorlash; anorganik sifat reaksiya (jadval) | oksid/karbonat+kislota | gaz qonunlari+yonish | tahlil: gaz olish+sifat reaksiya |
| 13 | atom/davriy/izoelektron ×2; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz; elektroliz ×2; eritma %/M/eruvchanlik; kuchlanish qatori; mol/stexiometriya; muvozanat; qonunlar/gaz/ekvivalent ×2; tezlik | S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al) | organik sifat reaksiya; gaz olish/yig'ish (rasm); organik olish tajribasi (rasm) | metall+tuz eritmasi+elektroliz | elektroliz+eritma | probirkalar topishmog'i (anorganik) |
| 14 | atom/davriy/izoelektron; bog'lanish/gibridlanish; elektroliz ×2; eritma %/M/eruvchanlik; kuchlanish qatori; kvant/yadro ×2; mol/stexiometriya ×2; qonunlar/gaz/ekvivalent ×2; tezlik | P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi | moddalarni aniqlash (probirka); laboratoriya xavfsizlik/jihoz; ajratish usullari (rasm) | aralashma+kislota/ishqor (Al,Zn,Fe) | muvozanat+K+kislota | jadval+metallar (H2S, Na2S, NaOH, Zn) |
| 15 | OQR; atom/davriy/izoelektron ×2; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz; elektroliz; eritma %/M/eruvchanlik ×2; kuchlanish qatori; kvant/yadro; oleum/molyal/normal ×2; qonunlar/gaz/ekvivalent | IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari | eritma tayyorlash; anorganik sifat reaksiya (jadval); organik sifat reaksiya | muvozanat (jadval/grafik) | oleum/kristallogidrat | ko'p bosqichli anorganik hikoya |
| 16 | OQR ×2; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz; elektroliz; eritma %/M/eruvchanlik; mol/stexiometriya; muvozanat; oleum/molyal/normal; qonunlar/gaz/ekvivalent ×2; tezlik ×2 | d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi; oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz | gaz olish/yig'ish (rasm); organik olish tajribasi (rasm); moddalarni aniqlash (probirka) | kristallogidrat/eruvchanlik | aralashma+OQR | tahlil: oqsil/uglevod/spirtni aniqlash |
| 17 | OQR ×2; atom/davriy/izoelektron; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz ×2; eritma %/M/eruvchanlik ×2; mol/stexiometriya; oleum/molyal/normal ×2; qonunlar/gaz/ekvivalent ×2 | oksid/asos/kislota/tuz; genetik zanjir/reaksiya turlari; mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3 | laboratoriya xavfsizlik/jihoz; ajratish usullari (rasm); eritma tayyorlash | gaz aralashma/yonish | tezlik+muvozanat jadvali | tahlil: ajratish+eritma tayyorlash |
| 18 | OQR ×2; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz ×2; elektroliz; eritma %/M/eruvchanlik; mol/stexiometriya; muvozanat; oleum/molyal/normal ×2; qonunlar/gaz/ekvivalent ×2 | mineral o'g'itlar/nodir gazlar; tuzlar termik/gidroliz; S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar | anorganik sifat reaksiya (jadval); organik sifat reaksiya; gaz olish/yig'ish (rasm) | oksid/karbonat+kislota | gaz qonunlari+yonish | tahlil: gaz olish+sifat reaksiya |
| 19 | OQR ×2; atom/davriy/izoelektron ×2; bog'lanish/gibridlanish ×2; dissotsilanish/pH/gidroliz ×2; elektroliz; eritma %/M/eruvchanlik; mol/stexiometriya; qonunlar/gaz/ekvivalent; tezlik | S/SO2/H2SO4; N/NH3/HNO3; P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al) | organik olish tajribasi (rasm); moddalarni aniqlash (probirka); laboratoriya xavfsizlik/jihoz | metall+tuz eritmasi+elektroliz | elektroliz+eritma | probirkalar topishmog'i (anorganik) |
| 20 | atom/davriy/izoelektron; bog'lanish/gibridlanish; dissotsilanish/pH/gidroliz ×2; elektroliz; eritma %/M/eruvchanlik ×2; mol/stexiometriya; muvozanat ×2; qonunlar/gaz/ekvivalent ×2; tushuncha/valentlik | P/C/Si; galogenlar; IA metallar; IIA/IIIA metallar (Ca,Mg,Al); d-metallar (Fe,Cu,Zn,Cr); suv qattiqligi | ajratish usullari (rasm); eritma tayyorlash; anorganik sifat reaksiya (jadval) | aralashma+kislota/ishqor (Al,Zn,Fe) | muvozanat+K+kislota | jadval+metallar (H2S, Na2S, NaOH, Zn) |

## 6. Organik 20–29 (har variantda)
- 20: alkan/sikloalkan
- 21: alken/alkadiyen/alkin
- 22: aren/neft/gaz/ko'mir
- 23: spirt/fenol
- 24: aldegid/keton
- 25: karbon kislota
- 26: efir/yog'/sovun
- 27: uglevod
- 28: nitro/amin/aminokislota/oqsil
- 29: polimer/kauchuk/tola
Ichki tur (nomlash / olinish / xossa / hisob / izomeriya / rasm) variantlar bo'ylab aylantiriladi.

## 7. Ish tartibi
1. Siz reja va kvotani tasdiqlaysiz.
2. 4 partiya (5 variantdan): savollar tuziladi, Python bilan tekshiriladi, yechimlar yoziladi.
3. Har partiyadan keyin 1–2 variantni ko'rib fikr bildirasiz — keyingilar shunga moslanadi.
4. Oxirida: 20 ta PDF (Tongotarov uslubi) + yig'ma Word + javoblar kaliti + mavzu qamrovi hisoboti.
5. Hajm: 20 variant = 860 savol + yechim; bir sessiyada 1–2 variant realroq, shuning uchun ish bir necha sessiyaga bo'linadi.

## 8. Tekshiruv
- Har savol hisobi Python bilan; A–D javoblar teng taqsimlanadi (rasmli A–E bundan mustasno).
- Har yechimda manba bo'limi ko'rsatiladi; darslik xatolari (konspektda belgilangan) ishlatilmaydi.
- Variantlar orasida savol takrorlanmaydi (raqamlar va moddalar o'zgaradi).
