# Loyiha promti — Milliy Sertifikat KIMYO darsligi (maqsad: A / A+)

Bu fayl matematika darsligi promtining kimyo va **A / A+ daraja** uchun qayta yozilgan
varianti. Yangi suhbatda ishni boshlash yoki davom ettirish uchun pastdagi
**PROMT** blokini to'liq nusxalab yuboring.

---

## Yuborishdan oldin to'ldiriladigan joylar

Promt ichida `[T1]`…`[T6]` belgilari bor. Ular — men tasdiqlay olmagan, rasmiy
manbadan olinishi shart bo'lgan raqamlar. Ularni to'ldirmasangiz ham promt
ishlaydi (agent birinchi navbatda shularni so'raydi), lekin to'ldirilgani yaxshi.

| Belgi | Nima kerak | Qayerdan olinadi |
|---|---|---|
| `[T1]` | Imtihon davomiyligi (daqiqa) | Rasmiy imtihon reglamenti |
| `[T2]` | Har bir savol turining ball qiymati (yopiq / moslashtirish / ochiq / yozma) | Rasmiy reglament |
| `[T3]` | Yozma ishda qisman ball bormi, yo'qmi | Rasmiy reglament / kuzatuv |
| `[T4]` | A va A+ ning xom ball bo'sag'asi | O'tgan yil statistikasi |
| `[T5]` | Tayyorgarlik muddati va haftalik soat | Sizning reja |
| `[T6]` | O'quvchilarning hozirgi darajasi (diagnostika testi natijasi) | Kirish testi |

---

## PROMT (nusxalash uchun)

Men metodistman. Milliy Sertifikat imtihoniga **kimyo** fanidan o'quvchilarni
tayyorlayapman. Sen bilan darslik (kitob) yozamiz. Loyiha davom etadi — quyidagi
qoidalar doirasida ishlaysan.

### Maqsad

**Kafolatlangan A, mo'ljal A+.** C yoki B maqsad emas — ular yo'l-yo'lakay
olinadi. Bu bitta narsani anglatadi: **dastur to'liq yopiladi, hech bir mavzu
"qiyin" degani uchun tashlab ketilmaydi.** A+ da xatolik byudjeti juda kichik,
shuning uchun kitob nafaqat "tushuntirish", balki **tezlik, aniqlik va tuzoqlarni
tanish** ustida ishlaydi.

Tayyorgarlik muddati: `[T5]`. O'quvchilarning boshlang'ich darajasi: `[T6]`.
Agar `[T6]` past bo'lsa — kitob baribir A+ gacha olib chiqadigan qilib yoziladi,
lekin ma'ruzalar noldan boshlanadi va "asos" boblarda mashqlar soni oshiriladi.

### Qat'iy qarorlar (muhokama qilinmaydi)

1. **Dastur 100% yopiladi.** Noorganik, organik, umumiy kimyo, hisoblash
   masalalari, amaliy/sifat qismi — hammasi. A+ da bitta tashlangan mavzu =
   yo'qotilgan daraja. Agar biror mavzu og'ir bo'lsa, yechim uni olib tashlash
   emas, balki unga ko'proq tip va mashq berish.
2. **Manba fayllardan birorta savol ko'chirilmaydi.** Menda Milliy Sertifikatga
   ilgari tushgan savollar bor — men ularni senga beraman. Ular **faqat mavzu,
   qiyinlik va savol tipini kalibrlash uchun** o'qiladi. Kitobdagi har bir savol
   original: raqamlar, moddalar, kontekst — hammasi almashtirilgan. Asl savol
   matni na kitobga, na javoblar bo'limiga, na test bazasiga tushmaydi.
3. **Har bir javob ikki marta, ikki mustaqil usul bilan tekshiriladi.** Kimyoda
   bu quyidagini anglatadi (batafsili "Javob tekshirish protokoli" bo'limida):
   biri — skript orqali (sympy/Fraction bilan stexiometriya, tenglama
   koeffitsientlari matritsa usulida), ikkinchisi — undan **mustaqil** yo'l
   (massa va zaryad saqlanishi, teskari qo'yish, birlik tahlili, qo'lda qayta
   hisob). Ikkalasi bir xil natija bermasa — savol kitobga kirmaydi.
4. **Bot hozircha qilinmaydi** — avval kitob mukammal bo'lsin. QR kod uchun joy
   qoldiriladi.
5. **Har bir tip va har bir testda vaqt normativi bo'ladi.** A+ ning yarmi —
   bilim, yarmi — tezlik. Normativsiz mashq to'liq hisoblanmaydi.
6. **Yodlash va tushunish ajratiladi.** Tushuntirish — ma'ruzada; yodlanishi
   shart bo'lgan narsa (eruvchanlik, rang, sifat reaksiyalari, nomlar,
   konstantalar) — alohida "Xotira kartalari" blokida, siqilgan holda.

### Imtihon faktlari (kimyo)

**43 topshiriq**, `[T1]` daqiqa.

| Savollar | Turi | Soni |
|---|---|---|
| 1–32 | Yopiq test, A/B/C/D | 32 |
| 33–35 | Moslashtirish (umumiy A–F javoblar ro'yxatidan) | 3 |
| 36–40 | Ochiq javob (faqat yakuniy natija yoziladi) | 5 |
| 41–43 | Yozma ish (to'liq yechim yoziladi) | 3 |

Ball taqsimoti: `[T2]`. A / A+ bo'sag'asi: `[T4]`.

Qat'iy tamoyillar:
- **Yopiq va ochiq savollarda qisman ball yo'q** — yarim yechim 0 ball. Yozma
  ishda: `[T3]`.
- **Noto'g'ri javobga ball ayirilmaydi** — bo'sh qoldirish har doim zarar. Hatto
  vaqt tugayotganda ham har bir yopiq savolda belgi qo'yiladi.
- Moslashtirish savollarida javoblar umumiy ro'yxatdan olinadi — bitta javob
  bir necha savolga to'g'ri kelishi mumkin, shuning uchun "chiqarib tashlash"
  usuli har doim ham ishlamaydi.

### A+ ball modeli (kitobning butun mantiqi shunga qurilgan)

A+ olish uchun o'quvchi amalda quyidagini bajarishi kerak:

- 1–32 (yopiq): **30–32 to'g'ri.** Ya'ni butun imtihon davomida yopiqda 0–2 xato.
- 33–35 (moslashtirish): **3/3.** Bu qism eng arzon ball — tayyorgarlik bilan
  yo'qotib bo'lmaydi.
- 36–40 (ochiq): **4–5 to'g'ri.** Bu yerda eng ko'p ball hisoblash xatosidan
  ketadi, bilimsizlikdan emas.
- 41–43 (yozma): **kamida 2 tasi to'liq**, uchinchisi qisman.

Bundan kelib chiqadigan kitob talablari:
1. Har bir mavzuda **"Tipik tuzoqlar"** bloki majburiy — A+ ni yo'qotadigan
   narsa bilmaslik emas, e'tiborsizlik.
2. Har bir hisoblash tipida **birlik va yaxlitlash qoidasi** aniq yoziladi.
3. **Yozma ish uchun alohida "Rasmiylashtirish" bo'limi** — javob qanday
   yoziladi, qaysi qadam yozilmasa ball ketadi.
4. Har bob oxirida **vaqt bo'yicha sinov** (masalan: 20 savol / 30 daqiqa).

### Kitob formati

Har bir mavzu qat'iy shu tartibda yoziladi:

1. **Ma'ruza** — nazariy tushuntirish, noldan, lekin A darajagacha ko'tariladi.
2. **Asosiy formulalar va konstantalar** — bir joyda, jadval ko'rinishida.
3. **Reaksiya tenglamalari bazasi** — mavzuga oid, yodlanishi kerak bo'lgan
   tenglamalar (koeffitsientlari bilan, sharoiti ko'rsatilgan).
4. **Sifat reaksiyalari jadvali** — reagent → belgi (rang, cho'kma, gaz, hid).
   Faqat tegishli boblarda.
5. **Eslatmalar** va **Xatolar** bo'limi — "xato → nega bo'ladi → tuzatish".
6. **Tiplar** — mavzu savol turlariga bo'linadi. Har bir tipda:
   - qisqa qoida (bir-ikki jumla) + formula;
   - bitta oxirigacha ishlangan namuna (qadamma-qadam + "Diqqat" ogohlantirishi);
   - **"Tez yechish"** — shu tipni 30–60 soniyada yechish usuli (nisbat, ustunlik
     qoidasi, variantlarni baholash);
   - **12 mashq** (asos boblarda 16);
   - **+4 ta "A daraja" mashqi** — imtihonning eng qiyin savollari darajasida,
     yulduzcha bilan belgilanadi.
7. **Yakuniy test — 20 ta**, imtihon formatida va nisbatida: 14 yopiq +
   2 moslashtirish + 3 ochiq + 1 yozma. Vaqt normativi ko'rsatiladi.
8. **Xotira kartalari** — shu mavzudan yodlanishi shart bo'lgan minimum
   (10–15 qator, siqilgan).
9. **QR kod joyi** (bot keyinroq).

### Uslub qoidalari

- Takrorlanadigan shart mashq oldida yozilmaydi. U MASHQLAR sarlavhasida bir
  marta chiqadi ("MASHQLAR — Moddaning molyar massasini toping"), mashqning o'zi
  yalang'och bo'ladi: `1.1 H2SO4`.
- Ortiqcha bezak yo'q, zich bo'lsin. Mashqlar va formulalar ikki ustunda.
- Qoida uzun tushuntirish emas — qisqa formula + ishlangan namuna yetarli.
- Javoblar o'zbekcha, lotin alifbosida.

**Kimyoviy yozuv qoidalari (qat'iy):**
- Barcha formulalar va tenglamalar LaTeX `\ce{...}` (mhchem) ichida:
  `$\ce{H2SO4}$`, `$\ce{2H2 + O2 -> 2H2O}$`, `$\ce{CaCO3 v}$`, `$\ce{NH3 ^}$`.
- Matematik ifodalar `$...$` ichida. Unicode kimyoviy/matematik belgilar
  (₂, →, ↑, ≠) **ishlatilmaydi** — Chrome PDF da buziladi.
- O'nlik kasr `$0{,}25$` ko'rinishida (vergul bilan).
- Birliklar: `$12{,}5\,\text{g/mol}$` — son va birlik orasida `\,`.
- Molyar massalar yagona jadvaldan olinadi (IUPAC), hisoblarda bir xil
  yaxlitlash: `$M(\ce{H})=1$`, `$M(\ce{O})=16$`, `$M(\ce{S})=32$` va h.k. —
  jadval kitob oxirida ilova qilinadi.
- Sharoit strelka ustida: `$\ce{->[\text{kat., }t^\circ]}$`.

### Javob tekshirish protokoli (majburiy)

Har bir mashq, namuna va test savoli kitobga kirishdan oldin quyidagidan o'tadi.
**Ikki usul mustaqil bo'lishi shart** — bittasi ikkinchisining natijasini
ishlatmaydi.

**1-usul — skript:**
- Molyar massa: yagona element jadvalidan avtomatik hisoblanadi (formula
  parseri), qo'lda kiritilmaydi.
- Tenglama koeffitsientlari: element-matritsa tuzilib, `sympy` bilan nullspace
  orqali topiladi; natija butun va eng kichik nisbatda bo'lishi tekshiriladi.
- Stexiometriya, eritma, gaz qonunlari, termokimyo: `Fraction` yoki `mpmath`
  bilan hisob (float yaxlitlash xatosidan qochish uchun).
- Redoks: oksidlanish darajalari balansi va elektronlar soni tekshiriladi.

**2-usul — skriptdan mustaqil:**
- **Massa saqlanishi:** reaksiyaga kirgan massa = hosil bo'lgan massa.
- **Zaryad saqlanishi:** ion tenglamalarida ikki tomon zaryadi teng.
- **Atomlar sanog'i:** har bir element uchun chap va o'ng tomon qo'lda sanaladi.
- **Teskari qo'yish:** topilgan javob shartga qaytarib qo'yiladi.
- **Birlik tahlili:** javobning o'lchov birligi mantiqan to'g'rimi.
- **Chegara tekshiruvi:** massa ulushi 0–100% oralig'ida, unum 100% dan oshmaydi,
  molyar massa manfiy emas, eritma konsentratsiyasi eruvchanlikdan oshmaydi.

**Qo'shimcha qoidalar:**
- Test savolining **noto'g'ri variantlari ham hisoblanadi** — har bir chalg'ituvchi
  variant "qanday xatodan kelib chiqadi" degan izoh bilan yoziladi. Tasodifiy son
  qo'yilmaydi.
- Bitta savolda ikkitadan ortiq to'g'ri variant bo'lib qolmasligi tekshiriladi.
- Har bir tekshiruv logi saqlanadi.
- Har o'zgarishdan keyin `validate.py` (tuzilma: mashq soni, test soni, kalitlar,
  `\ce{}` sintaksisi, javob formati) ishga tushiriladi.

### Bobning JSON tuzilmasi

```json
{"n": 12, "bolim": "...", "mavzu": "...", "savol_orni": "1-32 / 36-40 / 41-43",
 "maruza": ["..."],
 "asosiy_formulalar": [{"f": "...", "izoh": "...", "birlik": "..."}],
 "tenglamalar": [{"tenglama": "$\\ce{...}$", "sharoit": "...", "izoh": "..."}],
 "sifat_reaksiyalari": [{"reagent": "...", "belgi": "...", "tenglama": "..."}],
 "eslatmalar": [{"joy": "...", "matn": "..."}],
 "xatolar": [{"xato": "...", "sabab": "...", "tuzatish": "..."}],
 "tiplar": [{"nom": "...", "qoida": "...", "formula": "...",
             "topshiriq": "Hisoblang",
             "tez_yechish": "...", "vaqt_soniya": 60,
             "namuna": {"savol": "...", "qadamlar": ["..."], "javob": "...", "izoh": "..."},
             "mashqlar": [{"savol": "...", "javob": "...", "daraja": 1}]}],
 "xotira_kartalari": ["..."],
 "test": [{"matn": "...", "tur": "yopiq|moslashtirish|ochiq|yozma",
           "variantlar": ["","","",""], "javob": "A",
           "chalgituvchilar": [{"variant": "B", "xato": "..."}],
           "yechim": "...", "vaqt_soniya": 90}]}
```

### Milliy Sertifikatga tushgan savollardan foydalanish tartibi

Men senga o'tgan imtihonlardagi savollarni beraman. Ular bilan ishlash tartibi:

1. **Pasportlash.** Har bir savol uchun: mavzu · tip · qiyinlik (1–3) · kerakli
   qadamlar soni · taxminiy vaqt · tuzoq turi · savol o'rni (1–32 / 33–35 /
   36–40 / 41–43).
2. **Chastota jadvali.** Qaysi mavzudan necha marta va qaysi o'rinda kelgani
   sanaladi. Shu jadval mavzular ustuvorligini (`tiers.json`) belgilaydi.
3. **Analog yaratish.** Har bir asl savolga **3 ta original analog** yoziladi.
   Analog deb hisoblanishi uchun kamida ikkita parametr o'zgarishi shart: modda,
   son, kontekst, so'ralayotgan kattalik yoki qadamlar yo'nalishi (masalan,
   massadan mol emas, moldan massa).
4. **Taqiq.** Asl savol matni hech qayerga ko'chirilmaydi. Agar analog asl
   savolga so'zma-so'z o'xshab qolsa — qayta yoziladi.
5. **Bo'shliq tahlili.** Chastota jadvalidan chiqmagan, lekin rasmiy dasturda
   bor mavzular alohida ro'yxatga olinadi — ular ham yoziladi (A+ da "kelmaydi"
   degan mavzu yo'q).

### Ishlash uslubi

- Ko'p bob ustida ishlaganda parallel agentlardan foydalan, lekin **bitta faylga
  ikki agent yozmasin** — avvalgi loyihada 8 ta bobda to'qnashuv bo'lgan.
- Har o'zgarishdan keyin `validate.py` ishlat.
- **Katta qarorni o'zboshimchalik bilan qabul qilma — metodist bilan kelish.**
  Buning ichiga kiradi: mavzular ro'yxatini o'zgartirish, mashqlar sonini
  kamaytirish, formatni o'zgartirish, tekshirish protokolini yengillashtirish.
- Ishonchsiz kimyoviy fakt (kam uchraydigan reaksiya, aniq bo'lmagan sharoit)
  uchraganda taxmin qilma — belgilab qo'y va mendan so'ra.

### Bob tayyor deb hisoblanadi, agar

- [ ] Barcha mashq va testlar ikki mustaqil usuldan o'tgan;
- [ ] Har bir tipda "Tez yechish" va vaqt normativi bor;
- [ ] "Tipik tuzoqlar" bloki bo'sh emas;
- [ ] Har bir yopiq testda chalg'ituvchi variantlar izohlangan;
- [ ] Yakuniy test imtihon nisbatida (14/2/3/1);
- [ ] Xotira kartalari bor;
- [ ] `validate.py` xatosiz o'tgan;
- [ ] Barcha formulalar `\ce{}` ichida, Unicode belgi yo'q.

### Birinchi qadam

Ishni boshlashdan oldin mendan quyidagini so'ra:
1. `[T1]`–`[T4]` raqamlari (imtihon vaqti, ball taqsimoti, yozma ishda qisman
   ball, A/A+ bo'sag'asi);
2. tayyorgarlik muddati va haftalik soat;
3. o'quvchilarning diagnostika natijasi;
4. rasmiy dastur (mavzular ro'yxati) fayli bormi;
5. o'tgan imtihon savollari to'plami — qaysi shaklda beraman.

Keyin mavzular ro'yxati va ustuvorlik jadvalini taklif qil, men tasdiqlaganimdan
keyin bob yozishga o't.

---

## Matematika promtidan nima o'zgardi

| Matematika promti (C/B) | Kimyo promti (A/A+) |
|---|---|
| Geometriya olib tashlangan (32,2 ball qurbon qilingan) | Hech bir mavzu tashlanmaydi — dastur 100% yopiladi |
| 45 topshiriq: 32 yopiq + 3 moslashtirish + 10 ochiq | 43 topshiriq: 32 yopiq + 3 moslashtirish + 5 ochiq + 3 yozma ish |
| Maqsad: C kafolat, imkon bo'lsa B | Maqsad: A kafolat, mo'ljal A+ |
| Tekshiruv: sympy + brute-force | Tekshiruv: molyar massa parseri, matritsa balansi, `Fraction`/`mpmath` + massa/zaryad saqlanishi, teskari qo'yish, chegara tekshiruvi |
| Har tipda: qoida + namuna + 12 mashq | Qo'shildi: "Tez yechish" usuli, vaqt normativi, +4 ta "A daraja" mashqi |
| Yakuniy test: 20 ta aralash | Yakuniy test: 20 ta, imtihon nisbatida 14/2/3/1 + vaqt normativi |
| — | Qo'shildi: reaksiya tenglamalari bazasi, sifat reaksiyalari jadvali, xotira kartalari, yozma ishni rasmiylashtirish |
| — | Qo'shildi: chalg'ituvchi variantlar izohlanadi (har biri qaysi xatodan kelib chiqadi) |
| LaTeX matematik yozuv | `\ce{}` (mhchem) kimyoviy yozuv + birlik va yaxlitlash qoidalari |
| Manba savollari faqat qiyinlik o'lchash uchun | Qo'shildi: pasportlash → chastota jadvali → 3 ta analog → bo'shliq tahlili |
