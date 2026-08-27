# Maktab darsliklari tahlili

Kitobning ma'ruzalari "noldan" boshlanadi degan qoida bor. Lekin **qaysi
noldan?** O'quvchi maktabda nimani ko'rgan bo'lsa, ma'ruza o'sha yerdan
ulanadi: tanish atama qaytadan tushuntirilmaydi, tanish bo'lmagan tushuncha
esa tashlab ketilmaydi.

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `sNN.json` | Bitta sinf darsligi: boblar, mavzular, har mavzuning mazmun elementi va chuqurligi |
| `qoplama.py` | 27 element × sinf matritsasi + imtihon chastotasi bilan solishtirish |

Yangi darslik kelganda: `sNN.json` qo'shiladi va `python3 tahlil/darslik/qoplama.py`.

**Chuqurlik** uch qiymat oladi: `tanish` (to'liq o'tilgan) · `yuzaki`
(tanishtirilgan, hisob-kitobsiz) · `yoq` (umuman uchramaydi).

## Holat

| Sinf | Fayl | Holat |
|---|---|---|
| 7 | `kimyo_7_uzb_2022.pdf` | ✅ to'liq, 176 bet (Asqarov va b., 2022) |
| 8 | `kimyo_8_uzb.pdf` | ✅ to'liq, 208 bet (Asqarov va b., 2019) |
| 9 | `9-sinf-kimyo-N.pdf` | ❌ atigi 11 bet — pullik namuna, oxirida to'lov reklamasi |
| 10 | — | ❌ yo'q |
| 11 | — | ❌ yo'q |

9, 10 va 11-sinf darsliklari kerak. Ular bo'lmasa xarita yarim qoladi —
pastdagi jadval nima uchunligini ko'rsatadi.

## 1-topilma: eng og'ir imtihon mavzulari 7–8-sinfda umuman yo'q

`qoplama.py` chiqishi (imtihon ustuni — v01 variantidagi savollar soni):

| Element | 7-sinf | 8-sinf | Imtihon |
|---|---|---|---|
| **II.4** IIA, IIIA, d-metallar | yo'q | yo'q | **5 savol** |
| **I.7** eritmalar, konsentratsiya | yo'q | yo'q | **3 savol** |
| III.1, III.2, III.7 organik | yo'q | yo'q | 2 tadan |
| I.8 dissotsiatsiya, pH | yo'q | yo'q | 1 |
| I.10 elektroliz, Faradey | yo'q | yo'q | 1 |
| II.3 IA metallar | yo'q | yo'q | 1 |
| III.3…III.10 qolgan organik | yo'q / yuzaki | yo'q | 1 tadan |

Ya'ni **variantdagi 43 savoldan 25 tasi** 7–8-sinf darsliklarida asosi
bo'lmagan mavzulardan. Bu kutilgan holat — ular 9–11-sinfda o'tiladi — lekin
qaysi biri qaysi sinfda ekani darsliklar kelmaguncha aniq emas.

## 2-topilma: "tanish" degani "imtihonga tayyor" degani emas

Bu jadvalning eng muhim qatori. Element o'tilgan bo'lsa ham, darslik imtihon
talab qiladigan darajadan past to'xtaydi:

| Element | 8-sinfda bor | 8-sinfda YO'Q | v01 da nima so'ralgan |
|---|---|---|---|
| I.3 | Atom yadrosi, izotop, elektron qavatlar, energetik pog'onachalar (11 §) | **Kvant sonlar, Pauli, Klechkovskiy, Gund, yadro reaksiyalari** | 4-savol: `n+l = 8` bo'lgan elektronlar soni |
| I.4 | Elektromanfiylik, kovalent, ion, kristall panjara | **Donor-akseptor mexanizmi, gibridlanish** | 5-savol (D-A bog'), 6-savol (pi-bog'lar ulushi) |
| I.5 | Tezlikka ta'sir etuvchi omillar — sifat darajasida | **Tezlik qonuni `r = k[X]^m[Y]^n` va hisob** | 7-savol: jadval bo'yicha tezlik hisobi |
| I.6 | Le-Shatelye — sifat darajasida | **Kc va u bilan hisob** | 8 va 36-savollar: Kc orqali hisob |
| I.9 | Oksidlanish darajasi, elektron balans | **Ion-elektron (yarim reaksiya) usuli** | 12-savol: ion ko'rinishdagi OQR |

Xulosa: bu beshta element uchun ma'ruza "noldan" emas, balki **"maktab
to'xtagan joydan"** boshlanadi — va aynan o'sha davomi imtihonning eng qiyin
savollarini beradi. Kitobda ular alohida belgilanadi: *maktabda shu yergacha,
undan keyingisi shu kitobda*.

## 3-topilma: IV.1 bo'shlig'i yopildi

Avvalgi tahlilda IV.1 (laboratoriya jihozlari, ajratish usullari) v01 varianti
bo'yicha bo'shliq bo'lib qolgan edi. 7-sinfning I bobi to'liq shunga
bag'ishlangan: mehnat xavfsizligi, shtativ, spirt lampa, gaz gorelkasi, elektr
isitgich, sof modda va aralashmalar, aralashmadan sof moddani ajratish,
filtrlash, suvni tozalash usullari. Ya'ni bu mavzu maktabda **7-sinfda, kimyo
kursining eng boshida** o'tiladi va uch yil davomida qaytarilmaydi — 43-yozma
ish (25 ball) esa aynan shundan kelishi mumkin.

## 4-topilma: 8-sinf laboratoriya ishlari to'g'ridan-to'g'ri ballga aylanadi

8-sinfda 10 ta laboratoriya ishi bor. Uchtasi v01 savollariga bevosita mos:

| Laboratoriya ishi | v01 dagi savol |
|---|---|
| 3-ish: galogenidlar + `AgNO3`, yod + kraxmal | 31-savol (sariq cho'kma `AgI`) |
| 8-ish: sulfat ionni `BaCl2` bilan aniqlash | 43-yozma ish (4-idish — `BaCl2`) |
| 1-ish: rux gidroksidga kislota va ishqor ta'siri | 43-yozma ish (5, 6, 7-idishlar — amfoterlik) |

Kitobning "Sifat reaksiyalari jadvali" bloki shu laboratoriya ishlaridan
boshlanadi va imtihon darajasigacha kengaytiriladi.

## 5-topilma: atama farqi — kitob qaysi so'zni ishlatadi

Darsliklar **"noorganik"** deydi (8-sinf 2-§ "Noorganik birikmalarning asosiy
sinflari"), spetsifikatsiya esa **"anorganik"**. Boshqa farqlar: darslikda
"energetik pog'onachalar", spetsifikatsiyada "elektron konfiguratsiya";
darslikda "nisbiy elektromanfiylik".

Qoida: kitob **spetsifikatsiya atamasini** asosiy qilib oladi (imtihon shu
so'z bilan yoziladi), lekin birinchi uchraganda darslik atamasini qavs ichida
beradi — masalan "anorganik (darslikda: noorganik)". O'quvchi ikkita atamani
bir narsa deb bilishi kerak, aks holda imtihonda tanimay qoladi.
