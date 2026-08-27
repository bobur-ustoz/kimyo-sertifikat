# Maktab darsliklari — nima olinadi va nima uchun

Kitobning ma'ruzalari "noldan" boshlanadi degan qoida bor. Lekin **qaysi noldan?**
O'quvchi 7–11-sinfda nimani ko'rgan bo'lsa, ma'ruza o'sha yerdan ulanadi:
tanish atama takrorlanmaydi, tanish bo'lmagan tushuncha esa tashlab
ketilmaydi. Shu bog'lanishni aniqlash uchun darsliklar o'rganiladi.

## Holat

Darsliklar hali qo'lda yo'q. Bu sessiyada tashqi saytlardan yuklab bo'lmaydi —
tarmoq siyosati `oliygoh.uz`, `infoedu.uz`, `mbaza.uz` kabi manbalarni
bloklaydi (403). Darsliklar PDF sifatida yuborilishi kerak.

**Kerakli fayllar:** 7, 8, 9, 10 va **11**-sinf kimyo darsliklari.

11-sinf ham kerak: spetsifikatsiya "7–11-sinf materiallari" deydi, va organik
kimyoning katta qismi (spirtlardan polimergacha — III.4…III.10) 10–11-sinfda
o'tiladi. Imtihonda organik 10 ta yopiq savol + 2 ta ochiq + 42-yozma ish (25
ball) beradi, ya'ni 11-sinfsiz xarita yarim qoladi.

## Har darslikdan nima olinadi

1. **To'liq mundarija** — bob va mavzu nomlari, o'zgartirilmagan holda.
2. **Har mavzu → spetsifikatsiya elementi** (`I.1` … `IV.2`) bog'lanishi.
3. **Atama va belgilash** — darslik qaysi atamani ishlatadi (masalan
   "nisbiy molekulyar massa" yoki "molekulyar og'irlik"), formulalar qanday
   yoziladi. Kitob shu bilan bir xil bo'lishi kerak, aks holda o'quvchi
   ikkinchi til o'rganadi.
4. **Chuqurlik darajasi** — mavzu tanishtiriladimi yoki hisob-kitobgacha
   boriladimi. Imtihon darajasi bilan farqi shu yerda ko'rinadi.
5. **Laboratoriya ishlari ro'yxati** — IV.1 va IV.2 elementlari (jihozlar,
   ajratish usullari, sifat reaksiyalari) faqat shu yerdan chiqadi.

## Natija: uch xil xulosa

Har bir mazmun elementi (27 ta) uchun:

| Holat | Ma'nosi | Kitobga ta'siri |
|---|---|---|
| **Tanish** | Maktabda to'liq o'tilgan | Ma'ruza qisqa takrordan boshlanadi, asosiy vaqt tiplarga ketadi |
| **Yuzaki** | Tanishtirilgan, lekin hisob-kitobsiz | Ma'ruza to'liq yoziladi, mashqlar soni oshiriladi |
| **Yo'q** | Darslikda umuman uchramaydi | Noldan yoziladi va "asos bob" deb belgilanadi (16 mashq) |

"Yo'q" toifasidagi elementlar eng xavflisi: o'quvchi ularni imtihonda birinchi
marta ko'radi. v01 variantida shunga o'xshash savollar bor — masalan kvant
sonlar bo'yicha `n+l` hisobi (4-savol) va Kolbe elektrolizi (42-yozma ish) —
ular maktab darajasidan yuqori.

## Fayl formati

Har sinf uchun `sNN.json`:

```json
{"sinf": 8,
 "darslik": "muallif, nashr yili",
 "boblar": [
   {"bob": "1-bob nomi",
    "mavzular": [
      {"nom": "Mavzu nomi", "element": "I.1", "chuqurlik": "tanish|yuzaki|yoq",
       "atamalar": ["..."], "izoh": "..."}
    ]}
 ],
 "laboratoriya": [{"nom": "...", "element": "IV.2"}]}
```

To'ldirilgach `qoplama.py` yozilib, 27 element × 5 sinf matritsasi chiqariladi
va "yo'q" toifasidagi elementlar ro'yxati olinadi.
