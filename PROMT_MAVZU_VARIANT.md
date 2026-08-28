# Promt — Mavzulashtirilgan 43 talik test generatori (bitta mavzu, MS strukturasi)

Bu `PROMT_VARIANT.md` (27 elementga tarqalgan to'liq mock-variant) dan farqli
vazifa: **barcha 43 savol BITTA mazmun elementiga (masalan I.6) bag'ishlanadi**,
lekin Milliy Sertifikatning aniq 43-pozitsion strukturasi, savol turlari
(Y1/Y2/O1/O2), formatlari va qiyinlik/kognitiv ketma-ketligi to'liq saqlanadi.
Maqsad — bitta mavzuni chuqur, imtihon shakli va qiyinlik zichligida mashq
qildirish (masalan takrorlash haftasida, yoki o'quvchi bitta mavzuda
qiynalayotganda).

## PROMT (nusxalash uchun)

Men metodistman. **Bitta mavzu bo'yicha, lekin Milliy Sertifikatning to'liq
43-savolli strukturasida** original mashq-variant kerak — imtihondagi kabi
savol turlari va joylashuvi, lekin mazmuni bitta mavzuga qaratilgan.

### Maqsad

43 ta savolning HAMMASI bitta mazmun elementiga (masalan I.6, Kimyoviy
muvozanat) tegishli bo'ladi. Lekin quyidagilar imtihon strukturasidan
o'zgarmasdan olinadi:
- pozitsiya → savol turi (Y1/Y2/O1/O2) xaritasi,
- 1–32 (Y1) uchun `tahlil/v01.json`dagi **aynan o'sha pozitsiyaning**
  qiyinlik va kognitiv qiymati,
- 33–35 (Y2) va 41–43 (O2) uchun MSning STRUKTURAL formati (jadval,
  ko'p-bandli yozma ish) — lekin MAZMUN bitta mavzuga moslashtiriladi.

### Imtihon strukturasi (o'zgarmaydi)

43 topshiriq, 180 daqiqa (1–40 uchun 100 daqiqa, 41–43 uchun 80 daqiqa).

| Pozitsiya | Turi | Format |
|---|---|---|
| 1–32 | Y1 | 4 variant (A/B/C/D), bittasi to'g'ri |
| 33–35 | Y2 | Bitta ssenariy + 3 ichki savol, umumiy A–F javob ro'yxati (6 ta, 3 to'g'ri) |
| 36–40 | O1 | Qisqa javob (faqat son/atama), ichki tekshiruv uchun to'liq yechim saqlanadi |
| 41–43 | O2 | Har biri 25 ball, bandlarga bo'lingan, M (usul) + A (arifmetika) ballari |

### Qiyinlik/kognitiv — pozitsiyadan TO'G'RIDAN-TO'G'RI olinadi

`PROMT_VARIANT.md`dan farqli (u yerda naqsh "taxminiy shablon"), bu yerda
1–32 uchun **`tahlil/v01.json`dagi aynan o'sha pozitsiyaning qiyinlik va
kognitiv qiymati** ishlatiladi — chunki bitta mavzuga tor bo'lgani uchun
"bo'lim ichidagi naqsh" tushunchasi yo'qoladi, faqat pozitsiya qat'iy
qoladi. Masalan (I.6 uchun sinalgan misol):

```
1:(2,quyi) 2:(1,quyi) 3:(2,quyi) 4:(3,yuqori) 5:(2,quyi) 6:(2,yuqori)
7:(1,yuqori) 8:(2,yuqori) 9:(1,quyi) 10:(2,quyi) 11:(2,yuqori) 12:(3,yuqori)
13:(2,quyi) 14:(1,quyi) 15:(2,yuqori) 16:(2,quyi) 17:(3,yuqori) 18:(2,quyi)
19:(3,yuqori) 20:(2,yuqori) 21–26:(3,yuqori — uzluksiz murakkab plato)
27:(2,yuqori) 28:(1,quyi) 29:(2,quyi) 30:(1,quyi) 31:(2,yuqori) 32:(2,yuqori)
```

33–35 va 36–40 uchun ham xuddi shunday — v01'dagi shu pozitsiyalarning
qiyinlik/kognitiv qiymati (odatda 33:2/yuqori, 34:1/quyi, 35:3/yuqori;
36:2/yuqori, 37–40: barchasi 3/yuqori).

### 33–35 (Y2) — mavzu ichida guruhlangan savol

Bitta ssenariy yozilib, undan 3 ta bog'liq savol so'raladi (masalan: bosqich-1
hisobidan bosqich-2, bosqich-2dan bosqich-3). Javoblar A–F ro'yxatida (6 ta,
3 tasi to'g'ri, 3 tasi chalg'ituvchi — boshqa xil xatodan kelib chiqqan
sonlar, tasodifiy emas).

### 41–43 (O2) — MSning strukturasidan foydalanish, lekin mazmunni majburlamaslik

Bu eng muhim va ko'p xato qilinadigan joy. MSning haqiqiy 41/42/43'si turli
formatlarda keladi (41 — ko'p bosqichli OQR/hisob, 42 — organik zanjir, 43 —
sifat reaksiyalari jadvali) — bular **faqat murakkablik/format namunasi**,
mazmuni majburiy emas. Amaliy qoida (sinalgan):

- **41** — bitta mavzu asosida, chinakam ko'p bosqichli (4–5 band): asosiy
  hisobdan boshlab, keyingi bandlar oldingisining natijasiga tayanadi, oxirgi
  band ko'pincha SIFAT/SABAB tushuntirish talab qiladigan konseptual band
  bo'lsin (faqat son emas).
- **42** — CHUQUR KETMA: bitta oddiy-o'rtacha reaksiya/hisobga asoslangan,
  2–3 band, ortiqcha murakkablashtirilmaydi. (Foydalanuvchi so'rovi: "42 ga
  ko'p chuqur kirma, balki mavzuning o'zi bilan cheklan".)
- **43** — MSning "jadval" ruhini saqlaydi, lekin mavzuga mos shaklda: agar
  mavzu sifat-reaksiyaviy bo'lsa xuddi shunday jadval; agar mavzu (masalan
  muvozanat) buni tabiiy qabul qilmasa, ekvivalent "har bir holat uchun
  yo'nalish + sabab" formatidagi ko'p-bandli jadvalga aylantiriladi (masalan:
  "N ta turli ta'sir — har biri uchun siljish yo'nalishi va sababini
  aniqlang").

### Original savol yaratish — qat'iy taqiq (PROMT_VARIANT.md bilan bir xil)

Manba sifatida faqat pozitsiya→tur→qiyinlik→format naqshi olinadi. Savol
matni, sonlari, moddalari original bo'ladi.

### Y1 javob-harfi taqsimoti — MAJBURIY tekshiruv

**Sinalgan xato:** agar har savolning to'g'ri javobi tabiiy yozilsa (odatda
birinchi hisoblangan variant), deyarli barchasi "A" bo'lib qoladi — bu
haqiqiy imtihon uslubiga zid va o'quvchiga bilinmas signal beradi. Shuning
uchun:
1. Barcha 32 ta Y1 savoli yozib bo'lingach, to'g'ri javoblar harfini A/B/C/D
   bo'yicha **taxminan teng taqsimlang** (8/8/8/8 ga yaqin).
2. Variantlar matnini qayta joylashtirish orqali qiling (chalg'ituvchilarning
   matni ham mos harfga ko'chsin), sonlarni/matnni o'zgartirmang.
3. Qayta joylashtirgandan keyin, har bir savol uchun "javob" harfi haqiqatan
   ham to'g'ri variant matniga ishora qilishini **dasturiy tekshiring**
   (pastdagi tekshiruv skriptida alohida band sifatida).

### Javob tekshirish protokoli

`PROMT_VARIANT.md` bilan bir xil (ikki mustaqil usul), qo'shimcha bilan:
- Har bir sonli javob uchun xom generatsiya parametrlari (masalan
  `{"arch": "...", "kc": ..., "a0": ...}`) `"parametrlar"` maydonida
  saqlanadi — shunda mustaqil tekshiruv skripti "javob" matniga ishonmasdan,
  tenglamani noldan (yangi sympy sozlash bilan) qayta yechadi.
- Y1 javob-harfi tekshiruvi yuqoridagi bandga ko'ra alohida bajariladi.

### Kimyoviy yozuv qoidalari

`PROMT_VARIANT.md` bilan bir xil — `\ce{}` ichida `+` atrofida bo'shliq
majburiy, unicode belgilar yo'q, o'nlik kasr vergul bilan.

### Variant JSON tuzilmasi

```json
{"variant": "mavzu-I6",
 "manba": "original — mavzulashtirilgan mock (faqat I.6), MS 43-savol tuzilmasi asosida",
 "izoh": "...",
 "savollar": [
   {"n": 1, "tur": "Y1", "element": "I.6", "qiyinlik": 2, "kognitiv": "quyi",
    "savol": "...", "variantlar": ["","","",""], "javob": "A",
    "chalgituvchilar": [{"variant": "B", "xato": "..."}], "yechim": "..."},
   ...
   {"n": 33, "tur": "Y2", "element": "I.6",
    "ichki_pasport": [{"n":33,"element":"I.6","qiyinlik":2,"kognitiv":"yuqori"}, ...],
    "matn_umumiy": "...", "savollar_ichki": ["33-savol","34-savol","35-savol"],
    "javoblar_royxati": ["A) ...", ..., "F) ..."],
    "javoblar": {"33":"A","34":"C","35":"E"}, "yechim": "..."},
   ...
   {"n": 36, "tur": "O1", "element": "I.6", "qiyinlik": 2, "kognitiv": "yuqori",
    "savol": "...", "javob": "...", "yechim": "..."},
   ...
   {"n": 41, "tur": "O2", "element": "I.6", "qiyinlik": 3, "kognitiv": "yuqori",
    "matn": "...",
    "bandlar": [{"savol": "...", "yechim": ["..."], "M": 3, "A": 2}, ...],
    "jami": 25, "rasmiylashtirish": "..."}
 ]}
```

### PDF chiqarish

`variantlar/pdf/build.py` shu JSON sxemasini to'g'ridan-to'g'ri qabul qiladi
(o'zgartirish shart emas) — faqat variant nomi `vNN` formatida bo'lmasa,
sarlavha sahifasi variant nomini o'qiladigan holatda ko'rsatadi (masalan
"mavzu-I6" → "MAVZU I6"), "N-VARIANT" degan chalg'ituvchi yozuvga aylanmaydi.

```bash
python3 variantlar/pdf/build.py variantlar/mavzu_XXX.json exam.html
chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=natija.pdf --run-all-compositor-stages-before-draw \
  --virtual-time-budget=12000 "file://$(pwd)/exam.html"
```

### Ishlash tartibi

1. Mavzu (mazmun elementi, masalan I.6) tanlanadi.
2. `tahlil/v01.json`dan shu pozitsiyalarning qiyinlik/kognitiv qiymatlari
   olinadi (1–32, 33–35, 36–40 uchun).
3. 32 ta Y1 savoli yoziladi — mavzu ichida, lekin xilma-xil arxetiplarda
   (oddiy formuladan tortib ko'p bosqichli kvadrat tenglamagacha), qiyinlik
   pozitsiyaga mos.
4. Javob harflari A/B/C/D bo'yicha teng taqsimlanadi (yuqoridagi band).
5. Y2 guruhi (33–35) — bitta ssenariy, 3 bog'liq savol, ABCDEF javob
   ro'yxati.
6. O1 (36–40) — qisqa javobli, qiyin (odatda barchasi 3-daraja).
7. O2 (41–43) — MSning STRUKTURASIGA (murakkablik profiliga) mos, lekin
   mazmuni bitta mavzu: 41 chuqur ko'p bosqichli, 42 oddiyroq (bitta
   reaksiya/hisob), 43 ko'p-bandli jadval/sabab-tushuntirish formatida.
8. Har savol ikki mustaqil usulda tekshiriladi; xom parametrlar
   `"parametrlar"` maydonida saqlanadi.
9. mhchem `+` bo'shliq skaneri ishga tushiriladi.
10. PDF yasaladi va ko'rib chiqiladi.
