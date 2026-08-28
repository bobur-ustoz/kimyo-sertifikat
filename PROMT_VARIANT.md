# Promt — Milliy Sertifikat KIMYO variant generatori (43 talik mock-imtihon)

Bu `PROMT_KIMYO.md` (27 bobli darslik) dan **butunlay boshqa vazifa**: mavzu
bo'yicha o'qitish emas, balki **v01 asl variantiga o'xshash, to'liq 43 talik
original mock-imtihon variantlari** yaratish — bo'lim taqsimoti, savol o'rni,
qiyinlik darajasi va uning ketma-ketligi rasmiy spetsifikatsiya va v01
kalibrlashiga qat'iy mos holda.

## PROMT (nusxalash uchun)

Men metodistman. Milliy Sertifikat imtihoniga tayyorgarlik uchun **to'liq,
original 43 talik mock-variantlar** kerak — xuddi haqiqiy imtihon kabi, mavzu
bo'yicha ajratilmagan, bitta yaxlit test sifatida.

### Maqsad

Har bir variant real Milliy Sertifikat imtihonining **aniq nusxasi** bo'lishi
kerak: bir xil bo'lim taqsimoti, bir xil savol turi ketma-ketligi, bir xil
qiyinlik profili va uning pozitsiya bo'yicha taqsimoti. Farq faqat bitta
narsada — **savollarning o'zi original**, hech biri biror manbadan
ko'chirilmagan.

### Imtihon strukturasi (spetsifikatsiya — o'zgarmaydi)

43 topshiriq, 180 daqiqa (1–40 uchun 100 daqiqa, 41–43 uchun 80 daqiqa).

| Savol | Turi | Bo'lim | Soni |
|---|---|---|---|
| 1–13 | Y1 | Umumiy kimyo | 13 |
| 14–19 | Y1 | Anorganik kimyo | 6 |
| 20–29 | Y1 | Organik kimyo | 10 |
| 30–32 | Y1 | Kimyoviy tahlil | 3 |
| 33–35 | Y2 | Umumiy + anorganik + organik | 3 |
| 36–37 | O1 | Umumiy kimyo | 2 |
| 38 | O1 | Anorganik kimyo | 1 |
| 39–40 | O1 | Organik kimyo | 2 |
| 41 | O2 | Umumiy kimyo (25 ball, bandlarga bo'lingan) | 1 |
| 42 | O2 | Organik kimyo (25 ball, hisobsiz) | 1 |
| 43 | O2 | Anorganik **yoki** kimyoviy tahlil (25 ball) | 1 |

1–40 Rash modeli bilan baholanadi (qiyinlik hisobga olinadi). Qisman ball
1–40 da yo'q; noto'g'ri javobga ball ayirilmaydi.

### Qiyinlik ketma-ketligi — v01 kalibrlashidan aniqlangan naqsh

**Diqqat: bu bitta variant (`tahlil/v01.json`) asosidagi kuzatish.** Naqsh
ishonchli, lekin qat'iy qonun emas — yangi variant kelganda tasdiqlanadi yoki
aniqlashtiriladi. Shunga qaramay, generatsiya shu naqshni **standart shablon**
sifatida qo'llaydi.

**Umumiy taqsimot (43 ta savol bo'yicha):** ~7 sodda (16%) · ~18 o'rta (42%) ·
~18 murakkab (42%). Sodda savollar kam — ular asosan bo'lim CHEGARALARIDA
uchraydi.

**Bo'lim ichidagi naqsh:**

| Bo'lim | Pozitsiya | Naqsh |
|---|---|---|
| **I. Umumiy (1–13)** | 1–3 | Boshlanish — o'rtacha (2,1,2) |
| | 4 | Birinchi cho'qqi — murakkab (odatda atom tuzilishi/kvant sonlar) |
| | 5–11 | Barqaror o'rtacha (asosan 2, bitta-ikkita 1 yoki 3) |
| | 12 | Ikkinchi cho'qqi — murakkab (odatda OQR) |
| | 13 | Yumshoq tugash — o'rtacha |
| **II. Anorganik (14–19)** | 14 | Eng sodda boshlanish (1) |
| | 15–19 | Deyarli monoton o'sish, 17 va 19 — eng murakkab (II.4, metallar) |
| **III. Organik (20–29)** | 20 | O'rtacha kirish (2) |
| | **21–26** | **Uzluksiz murakkab plato — barcha 6 ta savol ham qiyinlik 3** |
| | 27–29 | Yumshoq tugash (2, 1, 2) |
| **IV. Tahlil (30–32)** | 30 | Sodda kirish (1) — organik platodan keyingi "dam olish" |
| | 31–32 | O'rtacha-murakkab (ikkalasi ham sifat reaksiyalari, yuqori kognitiv) |
| **Y2 (33–35)** | — | Manba bo'limiga qarab aralash (odatda 1–2 ta murakkab, 1 ta sodda) |
| **O1 (36–40)** | 36 | Nisbatan yengilroq (2) |
| | 37–40 | Deyarli barchasi murakkab (3) — ochiq javob formatining o'zi qiyinlikni oshiradi |
| **O2 (41–43)** | — | Har uchalasi ham murakkab, yuqori kognitiv (tuzilishi bo'yicha shart) |

**Kognitiv daraja (quyi/yuqori) taqsimoti ham pozitsion naqshga ega:** "quyi"
deyarli faqat Y1 ichida va bo'lim CHEGARALARIDA (boshida yoki oxirida)
uchraydi — 1, 2, 3, 5, 9, 10, 13, 14, 16, 18, 28, 29, 30, 34-pozitsiyalar.
"Yuqori" esa bo'lim ICHIDA, ayniqsa murakkab cho'qqilarda va butun O1/O2
qismida. Xulosa: **har bo'lim "sodda kirish → murakkab o'zak → yumshoq
chiqish" arkasiga ega**, organik bo'lim esa bundan mustasno — u boshidan
oxirigacha yuqori kognitiv talab qiladi va faqat pozitsiya 28–29 da
yengillashadi.

### Generatsiya qoidasi: shablonni to'ldirish

Har yangi variant uchun:
1. Yuqoridagi jadvaldagi **43 pozitsiyaning har biriga** mos qiyinlik va
   kognitiv daraja beriladi (jadvaldagi naqshga muvofiq, ± bitta daraja
   tafovut bilan — mashina kabi qattiq emas, tabiiy variatsiya saqlanadi).
2. Har pozitsiyaga mos **mazmun elementi** (I.1–IV.2) tanlanadi. Birinchi
   navbatda v01 dagi pozitsiya→element xaritasidan foydalaniladi (masalan
   17-pozitsiya — II.4); agar bir nechta variant to'plansa, elementlar
   variantlar orasida biroz aylantiriladi (bir xil element har doim bir xil
   pozitsiyada bo'lavermaydi, lekin bo'lim va taxminiy qiyinlik saqlanadi).
   **Bu faqat elementning raqamiga emas — savolning FORMATIGA ham tegishli.**
   Bizda faqat BITTA haqiqiy variant (v01) bor, shuning uchun ba'zi
   pozitsiyalarning haqiqiy formati (masalan 43-topshiriq — v01'da "raqamlangan
   idishlardagi tuzlarni sifat reaksiyalari jadvali orqali aniqlash" ko'rinishida
   kelgan) faqat BITTA namunaviy ko'rinish, umumiy qonun emas: rasmiy
   spetsifikatsiyada IV bo'lim ikki elementdan iborat — IV.1 (laboratoriya
   jihozlari/xavfsizlik, aralashmalarni ajratish, eritma tayyorlash) va IV.2
   (moddalarni olish usullari, shu jumladan sifat reaksiyalari) — va IV.2'ning
   o'zi ham "jadval orqali tuz aniqlash"dan tashqari boshqa ko'rinishlarda
   (masalan modda olish zanjiri/sintez yo'li) kelishi mumkin. **Bir nechta
   variant yaratilganda, bir xil pozitsiyaning FORMATI ham har safar aynan
   takrorlanmasligi kerak** — aks holda haqiqiy MSning xilma-xilligi noto'g'ri
   toraytiriladi (v02/v03/v04'da 43-topshiriq uchtasida ham bir xil "jadval"
   formatida yozilgan edi — bu xato aniqlanib, v03 IV.1 (ajratish/eritma
   tayyorlash hisobi) ga, v04 esa IV.2'ning boshqa ko'rinishi — modda olish
   zanjiriga — o'tkazildi; v02 jadval formatida qoldirildi).
3. Shu element va qiyinlik darajasiga mos **original savol** yoziladi —
   modda, sonlar, kontekst butunlay yangi.
4. Savol ikki mustaqil usul bilan tekshiriladi (pastga qarang).

### Original savol yaratish — qat'iy taqiq

Men senga o'tgan yillar variantlarini (v01 va hokazo) beraman. Ular **faqat**
pozitsiya→bo'lim→element→qiyinlik naqshini o'lchash uchun ishlatiladi. Asl
savol matni, sonlari, moddalari hech qanday shaklda yangi variantga
o'tmaydi — hatto "o'xshash" darajada ham emas. Yangi variant butunlay
mustaqil savollardan iborat bo'lishi kerak; faqat **statistik naqsh**
(qaysi pozitsiyada qaysi bo'limdan qanday qiyinlikda savol kelishi)
takrorlanadi.

### Javob tekshirish protokoli (PROMT_KIMYO.md bilan bir xil)

Har bir savol ikki mustaqil usul bilan tekshiriladi:

**1-usul — skript:** molyar massa parseri, tenglama koeffitsientlari
(`sympy` nullspace), stexiometriya/eritma/gaz hisoblari (`Fraction` yoki
`mpmath`), OQR — elektron balans.

**2-usul — skriptdan mustaqil:** massa va zaryad saqlanishi, atomlar sanog'i,
teskari qo'yish, birlik tahlili, chegara tekshiruvi (foiz 0–100%, unum
≤100%, pH 0–14).

Ikkalasi bir xil natija bermasa — savol variantga kirmaydi.

### Y1 va Y2 uchun qo'shimcha qoidalar

- Har bir Y1 savolning **4 varianti** bo'ladi (A/B/C/D), faqat bittasi
  to'g'ri. Qolgan uchtasi **chalg'ituvchi** — har biri "qaysi xatodan kelib
  chiqadi" degan izoh bilan yoziladi (masalan: "koeffitsientni hisobga
  olmagan", "hajmga bo'lishni unutgan"). Tasodifiy son taqiqlanadi.
- Bitta savolda ikkitadan ortiq to'g'ri variant qolmaganini tekshirish
  majburiy.
- Y2 (33–35) uchun umumiy A–F javoblar ro'yxati tuziladi (odatda 6 ta,
  3 tasi to'g'ri javob, 3 tasi chalg'ituvchi) — bitta stsenariy asosida uch
  savol so'raladi (v01 dagi 33–35 kabi: bitta masala matni, uchta savol).

### O1 va O2 uchun qo'shimcha qoidalar

- O1 (36–40): qisqa javob, yechim ko'rsatilmaydi (faqat yakuniy son), lekin
  ichki tekshiruv uchun to'liq yechim saqlanadi.
- O2 (41–43): har biri 25 ball, 3–7 bandga bo'linadi, har band **M
  (usul)** va **A (arifmetika)** ballariga ega (41 va 43 da M>A, 42 da A=0).
  "Rasmiylashtirish" namunasi beriladi: qaysi qadam yozilmasa ball
  yo'qolishi ko'rsatiladi.

### Kimyoviy yozuv qoidalari (qat'iy — mhchem xatosi tasdiqlangan)

- Formulalar va tenglamalar `\ce{...}` (mhchem) ichida:
  `$\ce{2H2 + O2 -> 2H2O}$`.
- **`+` belgisi atrofida bo'shliq MAJBURIY:** `$\ce{N2 + 3H2 <=> 2NH3}$` —
  `$\ce{N2+3H2<=>2NH3}$` EMAS. Bo'shliqsiz yozilsa, mhchem `+`ni zaryad
  belgisi deb noto'g'ri o'qib, butunlay boshqa natija chiqaradi (masalan
  `H2(g)+I2(g)` → `H₂(g)⁺I₂(g)` bo'lib qoladi). Bu amalda tekshirilgan va
  tasdiqlangan xato — har variant tayyor bo'lgach, barcha `\ce{}` bloklari
  bo'shliqsiz `+` uchun skript bilan skanerlanadi.
- Unicode kimyoviy/matematik belgilar (₂, →, ↑) ishlatilmaydi.
- O'nlik kasr `$0{,}25$` ko'rinishida.
- Molyar massalar yagona IUPAC jadvalidan, bir xil yaxlitlash bilan.

### Variant JSON tuzilmasi

```json
{"variant": "v02", "manba": "original, kalibrlash: v01",
 "savollar": [
   {"n": 1, "tur": "Y1", "bolim": "I", "element": "I.1",
    "qiyinlik": 2, "kognitiv": "quyi",
    "savol": "...", "variantlar": ["","","",""], "javob": "A",
    "chalgituvchilar": [{"variant": "B", "xato": "..."}],
    "tekshiruv": {"usul1": "...", "usul2": "..."}},
   ...
   {"n": 33, "tur": "Y2", "bolim": "II", "element": "II.4",
    "matn_umumiy": "...", "savollar_ichki": ["33-savol matni","34-savol matni","35-savol matni"],
    "javoblar_royxati": ["A) ...","B) ...","C) ...","D) ...","E) ...","F) ..."],
    "javoblar": {"33":"B","34":"C","35":"E"}},
   ...
   {"n": 41, "tur": "O2", "bolim": "I", "matn": "...",
    "bandlar": [{"savol":"...","yechim":["..."],"M":8,"A":4}],
    "jami": 25}
 ]}
```

### Ishlash tartibi

1. Men senga oldingi variant(lar)ni beraman — sen ularni pasportlaysan
   (`tahlil/vNN.json` formatida, `tahlil/chastota.py` bilan mos).
2. Shu pasportdan pozitsiya→qiyinlik→element shablonini chiqarasan (yuqoridagi
   jadvalga o'xshash, lekin barcha to'plangan variantlar bo'yicha
   o'rtachalashtirilgan).
3. Yangi variant shu shablon asosida, original savollar bilan to'ldiriladi.
4. Har savol ikki usulda tekshiriladi, Y1/Y2 uchun chalg'ituvchilar
   izohlanadi, O2 uchun bandlar va M/A ballari qo'yiladi.
5. Variant menga ko'rsatiladi — tasdiqlanmaguncha keyingisiga o'tilmaydi.
6. Katta qarorni (masalan shablonni o'zgartirish, yangi bo'lim qo'shish)
   o'zboshimchalik bilan qabul qilma — metodist bilan kelish.
