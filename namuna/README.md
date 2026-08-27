# Namuna bob — I.6 Kimyoviy muvozanat

27 mazmun elementidan **bittasining** to'liq namunasi — `PROMT_KIMYO.md`
dagi "Kitob formati" bo'yicha yozilgan. Ma'ruza, tiplar (namunasi bilan),
grafik tahlili, yozma ish, **43 talik mavzuviy mashqlar banki**, xotira
kartalari va qisqartirilgan yakuniy test (7/20 ta).

Mavzu tanlovi tasodifiy emas: I.6 kalibrlash (`tahlil/v01.json`) bo'yicha
ikki marta chiqqan (8 va 36-savol) va 8-sinf darsligida faqat sifat
darajasida o'tilgan — ya'ni maktab to'xtagan joydan davomi kerak bo'lgan
aniq misol (`tahlil/darslik/README.md` dagi 2-topilma).

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `I6-muvozanat.json` | Bobning o'zi — promtdagi JSON sxemasi bo'yicha |
| `verify.py` | Barcha sonli javoblarni mustaqil qayta hisoblab tekshiradi |
| `verify_lib.py` | Tekshiruv uchun umumiy formulalar (Kc, n0/alpha yechuvchi) |
| `render.py` | Har qanday shu sxemadagi bob JSON'ini ikki ustunli, KaTeX+mhchem bilan to'liq render qilingan HTML sahifaga aylantiradi |
| `assets/` | `render.py` uchun inline shrift/JS/CSS (internetga muhtoj emas) |

## Ishlatish

```bash
python3 namuna/verify.py          # barcha sonlarni qayta hisoblab tasdiqlaydi
python3 namuna/render.py namuna/I6-muvozanat.json
```

`render.py` chiqargan HTML faylni to'g'ridan-to'g'ri brauzerda ochsangiz,
`<!doctype>` yo'qligi sababli "quirks mode"da KaTeX ishlamay qolishi mumkin
— bu faqat mahalliy tekshiruvga tegishli, Artifact sifatida nashr
qilinganda muammo yo'q (harness o'zi to'g'ri o'raydi).

## Muhim topilma: mhchem va `+` belgisi

`\ce{}` ichida modda bilan bitishib yozilgan `+` (masalan `H2(g)+I2(g)`)
mhchem tomonidan zaryad belgisi deb noto'g'ri o'qiladi va butunlay boshqa
natija chiqadi. Yechim: **har doim bo'shliq bilan** — `H2(g) + I2(g)`.
Bu qoida `PROMT_KIMYO.md`ning "Kimyoviy yozuv" bo'limiga kiritilgan va
`verify.py` buni avtomatik tekshiradi (`\ce{}` ichida bo'shliqsiz `+`
qolganini qidiradi).

## Nima cheklandi (ataylab)

Yakuniy test to'liq 20 ta o'rniga 7 ta — hajmni boshqarish uchun. Qolgan
26 mazmun elementi hali yozilmagan. Bularning ikkalasi ham promtga
ta'sir qilmaydi — faqat shu bitta namunaviy bobning ko'lami.
