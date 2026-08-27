# Tushgan savollar tahlili

Bu katalog Milliy Sertifikat kimyo savollarini **kalibrlash** uchun. Har variant
bitta `vNN.json` fayl bo'ladi.

**Savol matni bu yerda saqlanmaydi.** Faqat pasport: mavzu tavsifi, mazmun
elementi, tur, qiyinlik, tuzoq va tekshirilgan javob. Kitobga savol ko'chirish
taqiqlangan — bu fayllar analog yozish uchun o'lchov, nusxa emas.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `vNN.json` | Bitta variant pasporti (43 savol) |
| `chastota.py` | Barcha `v*.json` dan chastota jadvalini yig'adi |

Yangi variant kelganda: `vNN.json` qo'shiladi va `python3 tahlil/chastota.py`
ishlatiladi — boshqa hech narsa o'zgartirilmaydi.

## Pasport maydonlari

| Maydon | Ma'nosi |
|---|---|
| `n` | Savol raqami (1–43) |
| `tur` | Y1 / Y2 / O1 / O2 |
| `bolim` | I umumiy · II anorganik · III organik · IV kimyoviy tahlil |
| `element` | Spetsifikatsiyadagi mazmun elementi (`I.1` … `IV.2`) |
| `mavzu` | Savol nimani tekshiradi — qisqa tavsif |
| `qiyinlik` | 1 sodda · 2 o'rta · 3 murakkab |
| `kognitiv` | quyi / yuqori (spetsifikatsiya bo'yicha) |
| `qadamlar` / `bandlar` | Yechim qadamlari soni; yozma ishda bandlar soni |
| `vaqt_s` | Yechishga ketadigan taxminiy vaqt (soniya) |
| `tuzoq` | Savol qayerda tuzoq qo'ygan |
| `javob` | Ikki usulda tekshirilgan javob |
| `qamrov` | Yozma ishda tegib o'tilgan qo'shimcha mazmun elementlari |

## v01 — asosiy topilmalar

**Manba:** Ma'ruf Tongotarov, Kimyo 2027 Milliy sertifikat, 1-variant.

### 1. Savol o'rni mazmun elementiga qat'iy bog'langan

Bu variantda savollar spetsifikatsiyadagi element tartibida ketadi:

| Savol | Element |
|---|---|
| 1–13 | I.1 · I.2 · I.3 · I.3 · I.4 · I.4 · I.5 · I.6 · I.7 · I.7 · I.8 · I.9 · I.10 |
| 14–19 | II.1 · II.2 · II.3 · II.4 · II.5 · (+1 qo'shimcha, II.4) |
| 20–29 | III.1 · III.2 · III.3 · III.4 · III.5 · III.6 · III.7 · III.8 · III.9 · III.10 |
| 30–32 | (30 — mazmuni anorganik) · IV.2 · IV.2 |

**Organik bo'limda har bir elementdan roppa-rosa bittadan savol** — ya'ni bitta
zaif mavzu = kafolatlangan yo'qotilgan ball. Umumiy kimyoda I.3, I.4 va I.7
ikkitadan chiqqan.

Bu bitta variant asosidagi kuzatish. Ikkinchi variant kelganda tasdiqlanadi yoki
rad etiladi — `chastota.py` "Savol o'rinlari" bo'limi shuni ko'rsatadi.

### 2. Vaqt yetmaydi — bu asosiy qiyinchilik

1–40 topshiriqni bosim ostida emas, tinch yechish uchun **~134 daqiqa** kerak.
Rasmiy vaqt — **100 daqiqa**. Ya'ni bilim yetarli bo'lgan o'quvchi ham vaqt
tugab qolgani uchun ball yo'qotadi.

Xulosa: "Tez yechish" usullari va vaqt normativlari kitobning bezagi emas,
asosiy qismi. Har tipda 1–2 qadamda javobga chiqish yo'li ko'rsatilishi shart.

### 3. Qiyinlik profili A+ talabini tasdiqlaydi

| | Soni (1–40 dan) |
|---|---|
| Qiyinlik 3 (murakkab) | 15 |
| Qiyinlik 2 | 18 |
| Qiyinlik 1 (sodda) | 7 |
| Yuqori kognitiv daraja | 26 |

Sodda savollar atigi 7 ta. Faqat ularni olib B ga ham chiqib bo'lmaydi.

### 4. Eng og'ir mazmun elementlari

| Element | Asosiy | Qo'shimcha | O'rtacha qiyinlik |
|---|---|---|---|
| II.4 — IIA, IIIA, d-metallar | 5 | 2 | 2,8 |
| I.7 — eritmalar, eruvchanlik | 3 | 1 | 2,0 |
| IV.2 — sifat reaksiyalari | 3 | 0 | 2,3 |
| I.9 — OQR | 2 | 0 | 3,0 |
| III.2, III.7 | 2 | — | 3,0 |

**II.4 — variantning eng zich mavzusi:** 17, 19, 33–35, 38-savollar va 41-yozma
ishning bir qismi. Kitobda unga mos ravishda ko'p tip va mashq kerak.

### 5. Bo'shliq

**IV.1** (laboratoriya jihozlari, aralashmalarni ajratish, eritma tayyorlash)
bu variantda umuman chiqmadi. Spetsifikatsiyada bor, demak kitobda ham bo'ladi —
lekin hozircha past ustuvorlikda.

### 6. Yozma ishlar (41–43) — takrorlanadigan uch qolip

| Topshiriq | Qolip | Bandlar |
|---|---|---|
| 41 | Aralashma + kons. kislota bilan OQR → tuzlar massasi → plastinka massasi o'zgarishi → kristallogidrat | 5 |
| 42 | Organik zanjir, hisobsiz, har band bitta tenglama | 7 |
| 43 | Nomerlangan idishlardagi tuzlarni sifat belgilari jadvalidan aniqlash + tenglamalar | 6 |

42 va 43 da **arifmetika deyarli yo'q** — 50 ball sof bilim va tenglama
yozishdan iborat. Bu A+ ning eng ishonchli qismi: yodlangan reaksiyalar va sifat
belgilar to'g'ridan-to'g'ri ballga aylanadi. Kitobning "Reaksiya tenglamalari
bazasi" va "Sifat reaksiyalari jadvali" bloklari aynan shuni ta'minlaydi.

### 7. Savol sifatiga oid ikki eslatma

- **8-savol:** muvozanat tenglamasida `NO2` oldidagi 2 koeffitsienti tushib
  qolgan va idish hajmi berilmagan (1 litr deb olinsa javob D chiqadi). Kitobga
  bunday savol kiritilmaydi — shart to'liq yoziladi.
- **1-savol:** to'g'ri javob C (`KO2` — nadperoksid), lekin `CuI2` ham barqaror
  emas. Bu yaxshi muhokama mavzusi, imtihon savoli sifatida esa noaniqlik.
