# Variantni PDF ga aylantirish

`variantlar/vNN.json` formatidagi istalgan variantni chop etishga tayyor,
ikki qismli PDF ga aylantiradi: (1) toza test varag'i — javobsiz, talabaga
berish uchun; (2) javoblar kaliti + har savol bo'yicha to'liq yechim va
chalg'ituvchi izohlari — metodist/o'qituvchi uchun.

## Ishlatish

```bash
# 1) HTML yasash (self-contained — internet kerak emas, shrift/JS inline)
python3 variantlar/pdf/build.py variantlar/v02.json exam.html

# 2) PDF ga aylantirish (Chrome/Chromium kerak)
chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf=v02.pdf --run-all-compositor-stages-before-draw \
  --virtual-time-budget=10000 "file://$(pwd)/exam.html"
```

Argumentlar ixtiyoriy: `build.py` standart holda `variantlar/v02.json` ni
o'qiydi va `<variant>.exam.html` nomi bilan yozadi.

## Muhim: Chrome flag

**`--no-pdf-header-footer`** — to'g'ri flag shu. `--print-to-pdf-no-header`
degan flag YO'Q (Chrome uni jimgina e'tiborsiz qoldiradi va sarlavha/sana/
fayl-yo'li avtomatik footer sifatida har sahifaga chiqib qoladi).

## Fayllar

| Fayl | Vazifasi |
|---|---|
| `build.py` | JSON'ni o'qib, ikkala qismni (test + javoblar) HTML ga yig'adi |
| `exam_shell.html` | A4 chop etish shabloni (sarlavha sahifa, ikki ustun, jadval uslublari) |

KaTeX/mhchem assetlari `namuna/assets/` dan olinadi (bir marta yozilgan,
qayta ishlatiladi).

## Sinab ko'rilgan tekshiruvlar

- Barcha matn maydonlari KaTeX+mhchem orqali 0 parse xatosi bilan render
  qilingan.
- 1 va 18-savollarda variantlar (A/B/C/D) matn ichida TAKRORLANMASLIGI
  tekshirilgan (`savol` maydonida variantlar yozilmasligi kerak — ular
  alohida `variantlar` massividan chiqadi).
- PDF matn qatlamida sarlavha/footer yo'qligi tasdiqlangan.
