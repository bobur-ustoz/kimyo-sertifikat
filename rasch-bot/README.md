# 🧪 Kimyo Milliy Sertifikat — Rasch Bot

Kimyo fanidan milliy sertifikat uslubidagi test natijalarini **Rasch modeli**
asosida baholaydigan Telegram bot. Yopiq testlar (1-40) qo'lda kiritilgan
raqam sifatida, yozma ishlar (41-43) esa rasm/PDF ko'rinishida yuborilib,
**Claude AI (vision)** yordamida avtomatik baholanadi.

> ⚠️ **DIQQAT: AI baholash tajribaviy hisoblanadi.** Bu bot rasmiy Bilim va
> malakalarni baholash agentligi tizimi emas — natijalar faqat taxminiy
> ko'rsatkich sifatida qaralishi kerak. Yakuniy baho albatta o'qituvchi
> tomonidan tekshirilishi tavsiya etiladi.

---

## 📁 Loyiha tuzilmasi

```
rasch-bot/
├── bot.py           - Telegram bot asosiy logikasi (ConversationHandler)
├── rasch.py         - Rasch modeli hisob-kitoblari
├── grading.py       - AI orqali yozma ish baholash (Claude vision)
├── requirements.txt - Python kutubxonalari
├── .env.example     - muhit o'zgaruvchilari namunasi
├── README.md        - ushbu fayl
└── data/            - natijalar saqlanadigan JSON papka (students.json)
```

---

## 🚀 O'rnatish

### 1-qadam — Python o'rnating

Python 3.11 yoki undan yuqori versiya kerak: https://python.org

```bash
python3 --version
```

### 2-qadam — Loyihani va kutubxonalarni o'rnating

```bash
cd rasch-bot
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3-qadam — Telegram bot tokenini oling

1. Telegramda [@BotFather](https://t.me/BotFather) ga yozing
2. `/newbot` buyrug'ini yuboring va ko'rsatmalarga amal qiling
3. Sizga beriladigan tokenni saqlab qo'ying (masalan `123456:ABC-DEF...`)

### 4-qadam — Anthropic (Claude) API kalitini oling

1. https://console.anthropic.com saytida ro'yxatdan o'ting
2. **API Keys** bo'limidan yangi kalit yarating

### 5-qadam — `.env` faylini sozlang

```bash
cp .env.example .env
```

`.env` faylini oching va quyidagicha to'ldiring:

```
TELEGRAM_BOT_TOKEN=123456:ABC-DEF_sizning_tokeningiz
ANTHROPIC_API_KEY=sk-ant-sizning_kalitingiz
```

---

## ▶️ Botni ishga tushirish

```bash
python bot.py
```

Konsolda `Bot ishga tushdi...` xabari chiqsa, bot ishlayapti. Telegramda
botingizga `/start` yuboring.

---

## 📖 Foydalanish yo'riqnomasi

1. **`/start`** — bot ism-familiyangizni so'raydi
2. Ismni kiritgach, **1-40 savollardan nechtasiga to'g'ri javob bergan**
   bo'lsangiz, shu sonni kiriting (0 dan 40 gacha)
3. Bot navbat bilan **41, 42, 43-savollar** uchun qo'lyozma yechimingizni
   rasm yoki PDF sifatida yuborishni so'raydi
   - Har bir fayl yuborilgandan so'ng, AI baholash boshlanadi
     ("🤖 AI orqali baholanmoqda..." xabari chiqadi)
   - Baholash natijasi (ball + qisqa izoh) darhol ko'rsatiladi
   - Agar AI baholashda xatolik yuz bersa, bot sizdan ballni **qo'lda**
     kiritishni so'raydi (dastur to'xtab qolmaydi)
4. Barcha uchta yozma ish baholangandan so'ng, bot **Rasch modeli**
   asosida yakuniy natijani chiqaradi:
   - Test qismi: xom ball → logit → skalalangan ball
   - Yozma ish qismi: xom ball → logit → skalalangan ball
   - Umumiy ball (ikkala qismning o'rtachasi) va Daraja
5. Natija avtomatik ravishda `data/students.json` fayliga saqlanadi
6. **`/royxat`** — barcha saqlangan talabgorlarni jadval ko'rinishida
   ko'rsatadi (Ism | Umumiy ball | Daraja)
7. **`/bekor`** — joriy suhbatni bekor qiladi

---

## 🧮 Rasch modeli haqida (rasch.py)

- **Test qismi (1-40):** 40 ta item, har biri 1 ballik, qiyinlik
  parametrlari -2.0 dan +2.0 gacha tekis taqsimlangan
- **Yozma ish qismi (41-43):** 3 ta item, har biri 25 ballik
- Xom balldan **logit (theta)** topish uchun bisection (binary search)
  ishlatiladi
- Logit skalalangan ballga chiziqli formula bilan o'giriladi:
  `scaled = 50 + 10 * logit` (0-100 oralig'iga cheklangan)
- Test va yozma ish qismlari uchun **alohida** hisoblanadi, so'ng
  ularning **oddiy o'rtachasi** umumiy ball hisoblanadi
- Daraja jadvali: `70+ = A+`, `65-69.9 = A`, `60-64.9 = B+`, `55-59.9 = B`,
  `50-54.9 = C+`, `46-49.9 = C`, `46 dan past = Sertifikat berilmaydi`

> ⚠️ `rasch.py` faylidagi item qiyinlik parametrlari va skalalash
> formulasidagi `50`, `10` sonlari **ILLYUSTRATIV/taxminiy qiymatlar** —
> rasmiy Bilim va malakalarni baholash agentligi formulasi emas. Ular
> alohida konstantalar (`SCALE_INTERCEPT`, `SCALE_SLOPE`, `TEST_ITEMS`,
> `YOZMA_ITEMS`) sifatida ajratilgan, shuning uchun kerak bo'lsa rasmiy
> qiymatlar bilan osongina almashtirishingiz mumkin.

Hisob-kitob mantiqini sinab ko'rish uchun:

```bash
python rasch.py
```

---

## 🤖 AI baholash haqida (grading.py)

- 41 va 43-topshiriqlar: **M (metodika) + A (arifmetika)** alohida
  baholanib, qo'shiladi (jami 25 ball)
- 42-topshiriq: faqat **M (metodika/mantiq)** baholanadi (jami 25 ball)
- Agar yechim yo'li ko'rsatilmasdan faqat javob yozilgan bo'lsa yoki
  topshiriq to'liq xato yechilgan bo'lsa — **0 ball**
- Claude'dan faqat JSON formatda javob so'raladi:
  `{"ball": 0-25, "izoh": "..."}`
- JSON formatida xatolik bo'lsa, dastur qulamaydi — 0 ball va xato xabari
  bilan qaytariladi, foydalanuvchidan qo'lda ball kiritish so'raladi

---

## ❗ Muammolarni bartaraf etish

- `TELEGRAM_BOT_TOKEN topilmadi` — `.env` faylida tokenni to'g'ri
  kiritganingizni tekshiring
- `ANTHROPIC_API_KEY topilmadi` — Claude API kaliti to'g'ri ekanini
  tekshiring, balansda mablag' borligiga ishonch hosil qiling
- Bot javob bermasa — konsoldagi log xabarlarini tekshiring, internet
  aloqasini tasdiqlang

---

*Kimyo Milliy Sertifikat · Rasch Bot — tajribaviy AI baholash tizimi*
