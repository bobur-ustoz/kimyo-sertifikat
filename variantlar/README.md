# Variantlar — to'liq 43 talik mock-imtihonlar

`PROMT_VARIANT.md` shabloni bo'yicha yaratilgan, original 43 talik variantlar.
Har biri v01 (`tahlil/v01.json`) bilan bir xil bo'lim taqsimoti, savol o'rni
va qiyinlik ketma-ketligiga ega — lekin barcha savollar original.

## v02

Birinchi generatsiya qilingan variant. 32 Y1 (har biri 4 variant + 3
chalg'ituvchi izohi bilan) + 1 Y2 (33–35, umumiy A–F javoblar ro'yxati bilan)
+ 5 O1 + 3 O2 (bandlarga bo'lingan, M/A ballari bilan).

**Tekshiruv:** barcha sonli javoblar `verify_v02.py` orqali mustaqil qayta
hisoblanadi (formuladan to'g'ridan-to'g'ri, ba'zilarida qo'shimcha sympy
tenglama yechimi bilan). Ishga tushirish:

```bash
python3 variantlar/verify_v02.py
```

## Kimyoviy yozuv formati

Barcha formulalar va tenglamalar `$\ce{...}$` (LaTeX mhchem) ko'rinishida —
`PROMT_KIMYO.md` va `PROMT_VARIANT.md` talabiga mos. `+` belgisi har doim
moddalardan bo'shliq bilan ajratilgan (`namuna/` papkasidagi mhchem xatosiga
qarang). Barcha 654 ta matn maydoni KaTeX+mhchem orqali render qilinib,
0 parse xatosi bilan tekshirilgan — `namuna/assets/` dagi bir xil asboblar
bilan (`python3 namuna/render.py variantlar/v02.json` ishlatib ko'rish
mumkin, chunki JSON sxemasi bob va variant fayllari uchun bir xil emas —
`render.py` bevosita ishlamaydi, lekin xuddi shu KaTeX/mhchem inline
asboblaridan foydalanib mahalliy render/tekshiruv o'tkazilgan).

## Pozitsiya→element xaritasi (v01 bilan bir xil)

| Pozitsiya | Element | Pozitsiya | Element | Pozitsiya | Element |
|---|---|---|---|---|---|
| 1 | I.1 | 16 | II.3 | 31 | IV.2 |
| 2 | I.2 | 17 | II.4 | 32 | IV.2 |
| 3–4 | I.3 | 18 | II.5 | 33,35 | II.4 (Y2) |
| 5–6 | I.4 | 19 | II.4 | 34 | I.2 (Y2) |
| 7 | I.5 | 20 | III.1 | 36 | I.6 (O1) |
| 8 | I.6 | 21 | III.2 | 37 | I.7 (O1) |
| 9–10 | I.7 | 22 | III.3 | 38 | II.4 (O1) |
| 11 | I.8 | 23 | III.4 | 39 | III.2 (O1) |
| 12 | I.9 | 24 | III.5 | 40 | III.7 (O1) |
| 13 | I.10 | 25 | III.6 | 41 | I.9 (O2) |
| 14 | II.1 | 26 | III.7 | 42 | III.1 (O2) |
| 15 | II.2 | 27 | III.8 | 43 | IV.2 (O2) |
| | | 28 | III.9 | | |
| | | 29 | III.10 | | |
| | | 30 | II.5 | | |

## Keyingi qadam

Ikkinchi variant (v03) kelsa, `chastota.py` uslubida ikkala variantning
pozitsiya→qiyinlik→element xaritasini solishtirib, `PROMT_VARIANT.md`dagi
"standart shablon"ni yangilash mumkin bo'ladi.
