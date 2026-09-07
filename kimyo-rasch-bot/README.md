# Kimyogar bot (qayta tiklangan)

Bu papka `@Kimyo_Rasch_bot`ning tiklangan (qayta yozilgan) versiyasi. Asl kod
hech qachon GitHub'ga yuklanmagan va Railway trial tugagach yo'qolgan edi —
faqat ma'lumotlar bazasi (`/data/exam_bot.db`, Railway volume'da) omon qoldi.
Ushbu kod o'sha bazaning tuzilishiga asoslanib qayta yozilgan; asl matnlar va
ba'zi tafsilotlar bir xil bo'lmasligi mumkin.

## Fayllar

- `exam_bot.py` — asosiy Telegram bot (polling rejimida).
- `webapp/server.py` — Telegram Mini App uchun oddiy natijalar sahifasi.
- `db.py` — SQLite ustidagi yordamchi funksiyalar (jadval tuzilishi asl baza bilan bir xil).
- `grading.py` — Claude (Anthropic) orqali rasm asosida baholash va AI savol-javob.

## Kerakli muhit o'zgaruvchilari (Railway → Variables)

| O'zgaruvchi | Tavsif |
|---|---|
| `BOT_TOKEN` | @BotFather bergan Telegram bot tokeni |
| `ADMIN_IDS` | Admin(lar)ning Telegram user ID'lari, vergul bilan: `123,456` |
| `CLAUDE_API_KEY` | Anthropic API kaliti (rasm baholash va AI savol-javob uchun) |
| `DB_PATH` | SQLite fayl yo'li, odatda `/data/exam_bot.db` (volume ichida) |
| `CHANNEL_ID` | (ixtiyoriy) e'lonlar uchun kanal ID |
| `WEBAPP_URL` | (ixtiyoriy) Mini App manzili |
| `PORT` | webapp server porti (Railway avtomatik beradi) |

`VOYAGE_API_KEY` asl loyihada `solved_examples` jadvali uchun (RAG/semantik
qidiruv) ishlatilgan bo'lishi mumkin, lekin bu jadval bo'sh edi va hozirgi
qayta tiklangan kodda ishlatilmagan — kerak bo'lsa keyinroq qo'shish mumkin.

## Ishga tushirish (Railway)

Custom Start Command:

```
python3 webapp/server.py & python3 exam_bot.py
```

Root Directory: `/kimyo-rasch-bot`

## Mahalliy sinov

```bash
pip install -r requirements.txt
export BOT_TOKEN=... ADMIN_IDS=... CLAUDE_API_KEY=... DB_PATH=./exam_bot.db
python exam_bot.py
```
