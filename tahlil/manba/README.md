# Xom manba materiallar (foydalanuvchi yuklagan)

Bu katalog foydalanuvchi (metodist) yuklagan xom kirish materiallarini saqlaydi —
`tahlil/darslik/` (maktab darsliklari) dan farqli, bular **haqiqiy imtihon
savollari banki**, lekin hali tekshirilmagan/javobsiz holda.

## Fayllar

| Fayl | Manba | Element | Savol soni | Holat |
|---|---|---|---|---|
| `ok_qay.json` | 2019-2021 mavzulashtirilgan bank (.docx) | I.9 (OQR) | 149 | Javob kaliti YO'Q |
| `elektroliz.json` | 2019-2021 mavzulashtirilgan bank (.docx) | I.10 (Elektroliz) | 106 | Javob kaliti YO'Q |
| `boglanish.json` | 2019-2021 mavzulashtirilgan bank (.docx) | I.4 (Kimyoviy bog'lanish) | 130 | Javob kaliti YO'Q |
| `eritma.json` | 2019-2021 mavzulashtirilgan bank (.docx) | I.7/I.8 (Eritmalar + gidroliz aralash) | 218 | Javob kaliti YO'Q |
| `tezlik.json` | 2019-2021 mavzulashtirilgan bank (.docx) | I.5 (Reaksiya tezligi) | 162 | Javob kaliti YO'Q |

Jami: **765 ta savol**, aynan hozirgi navbatning eng yuqori pog'onasidagi
elementlarga (I.4, I.5, I.7, I.8, I.9, I.10 — barchasi darslikda "yo'q" yoki
"yuzaki") to'g'ridan-to'g'ri mos keladi.

**Muhim:** bu fayllardagi savollarning HECH BIRIDA javob ustuni to'ldirilmagan
(manba .docx da 3- va 4-ustunlar bo'sh edi). `"javob"` maydoni yo'q — shuning
uchun bu bank hozircha faqat **savol matnlari manbasi** sifatida ishlatiladi
(masalan mavzulashtirilgan 43-talik test yozishda "qanday arxetiplar
imtihonda haqiqatan chiqqan" ma'lumoti sifatida), lekin tayyor javob manbai
sifatida ISHLATILMAYDI — har bir foydalaniladigan savol PROMT_MAVZU_VARIANT.md
dagi ikki mustaqil usul protokoli bilan qaytadan yechilishi kerak.

## DTM baza (2012, 2014, 2016, 2017, 2018) — hali qayta ishlanmagan

Foydalanuvchi "DTM baza" deb yuklagan 5 ta PDF (2012/2014/2016/2017/2018,
har biri 15-19 sahifa, 13-15 MB) — bular **skanerlangan rasm sahifalar**,
matn qatlami yo'q (`pypdf` bilan tekshirilganda har bir sahifadan 0 ta belgi
chiqadi, lekin har sahifada 2 tadan rasm bor). Bular eski Davlat Test
Markazi (DTM, MSgacha bo'lgan qabul imtihoni tizimi) test kitobchalari
bo'lishi mumkin.

Bu fayllar hozircha **qayta ishlanmagan** — matn qatlami yo'qligi sababli
oddiy ekstraksiya ishlamaydi, OCR yoki sahifama-sahifa vizual o'qish kerak
bo'ladi. Foydalanuvchi ko'proq material yuklashni davom ettirmoqda
("yana tashlayman"), shuning uchun bu ishni hammasi kelgach boshlash
maqsadga muvofiq — aks holda jarayonni ikki marta takrorlashga to'g'ri
keladi. Original PDF fayllar repo ga committ qilinmagan (repo faqat
ekstraksiya qilingan JSON/tahlil saqlaydi, xom PDF/docx emas — darslik
fayllari bilan bir xil konvensiya).
