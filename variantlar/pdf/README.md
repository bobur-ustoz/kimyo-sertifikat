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

## Dizayn: 33–35 (Y2) va 41–43 (O2)

Haqiqiy imtihon (`Milliy_sertifikat_2027_1variant.pdf`) namunasi bilan
solishtirib, quyidagi elementlar original chizilishga moslashtirilgan:

- **33–35 (Y2, moslashtirish savoli):** yagona jadval — chap ustunda umumiy
  ssenariy + har bir kichik savol alohida qatorda, o'ng ustunda A–F javob
  variantlari bitta katakka (`rowspan`) yig'ilgan — xuddi asl imtihondagi
  kabi.
- **41–43 (O2):** `matn` maydoni ichidagi reaksiya sxemasi (`->[n]` bilan
  yozilgan) alohida markazlashtirilgan qatorda, tajriba-natija jadvali
  (`|` bilan ajratilgan qatorlar) haqiqiy `<table>` sifatida chiziladi —
  matn ichida "|" belgilari ko'rinib qolmaydi.

`build.py`dagi `split_o2_matn()` funksiyasi `matn` maydonini kirish matni /
sxema / jadval qismlariga avtomatik ajratadi.

## Muhim: 33–35 savoli qayta yozilgan (no-copy qoidasi buzilgan edi)

Birinchi versiyada 33–35 (Y2) blokining ssenariy matni va sonlari haqiqiy
1-variant imtihonidan (`eef26950-Milliy_sertifikat_2027_1variant.pdf`, 4-bet)
so'zma-so'z ko'chirilgan edi — bu loyihaning o'z-o'ziga qo'ygan "hech qanday
savol matni ko'chirilmasin" qoidasini buzgan. Aniqlanishi bilan butunlay
yangi ssenariy yozildi (boshqa metall — Mg o'rniga edi Zn, boshqa sonlar),
faqat pasport (bo'lim=II, elementlar=II.4/I.2/II.4, qiyinlik=2/1/3, tuzoq
turi) saqlab qolindi. Yangi yechim ikki mustaqil usulda (to'g'ridan-to'g'ri
va `sympy` bilan teskari yechish) qayta tekshirilgan —
`variantlar/verify_v02.py`.

## Sinab ko'rilgan tekshiruvlar

- Barcha matn maydonlari KaTeX+mhchem orqali 0 parse xatosi bilan render
  qilingan.
- 1 va 18-savollarda variantlar (A/B/C/D) matn ichida TAKRORLANMASLIGI
  tekshirilgan (`savol` maydonida variantlar yozilmasligi kerak — ular
  alohida `variantlar` massividan chiqadi).
- 33–35 endi original (haqiqiy imtihondan ko'chirilmagan) va ikki usulda
  tekshirilgan.
- PDF matn qatlamida sarlavha/footer yo'qligi tasdiqlangan.
