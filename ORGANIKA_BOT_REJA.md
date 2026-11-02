# Organika bot — o'yin boti rejasi

Telegramda organik kimyoni o'yin shaklida o'rgatadigan bot: bob xaritasi, XP, jon (❤️), kunlik seriya, boss sinovi va tasodifiy tuzilgan jamoalar o'rtasidagi haftalik musobaqa.

## 1. Qarorlar (kelishilgan)

| Mavzu | Qaror |
|---|---|
| Platforma | Telegram bot |
| Jon | Boshida 3 ta. Xato = −1. Jon tugasa **joriy 10 talik bosqich** qayta boshlanadi, XP saqlanadi. Har 30 daqiqada +1 jon. Boss sinovida 2 ta jon |
| Savollar | 9 darslik doirasidan, har savolga tur belgisi (nomlanish, olinishi, xossa, zanjir, izomer, sinf). Savollarni Claude yozadi, siz tekshirasiz. Samarqand variantlaridan faqat qiyinlik darajasi olinadi, mazmun nusxalanmaydi |
| Jamoa | O'quvchilar tasodifiy, lekin daraja bo'yicha muvozanatli jamoalarga bo'linadi. Qur'ani admin buyruq bilan o'tkazadi. Mavsum 1 hafta |
| Jamoa ball | Jamoa balli = a'zolar XP yig'indisi ÷ a'zolar soni. Kuniga bir kishidan ko'pi bilan 300 XP hisoblanadi. Jamoaning 80% i o'ynasa +20% bonus |
| Formula | 1-bosqichda Unicode matn (CH₃–CH₂–OH). Murakkab tenglamalar keyin rasm bilan |

## 2. Arxitektura

Mavjud `api/telegram-webhook.js` to'lovlarni tasdiqlaydigan admin boti. Bir bot tokeniga bitta webhook ulanadi, shuning uchun:

- **Yangi bot** @BotFather orqali yaratiladi (masalan, `@OrganikaOyin_bot`). Tokenini siz olasiz.
- **Yangi endpoint:** `api/organika-webhook.js`. Barcha buyruq va tugmalar bitta funksiya ichida yo'naltiriladi.
- **Vercel Hobby chegarasi:** 12 ta funksiya. Hozir 11 ta, yangisi 12-chi bo'ladi. Boshqa endpoint qo'shib bo'lmaydi, shuning uchun hammasini bitta faylga joylaymiz (yordamchi modullar `_` bilan boshlanadi).
- **Holat saqlash:** Vercel serverless, xotira saqlanmaydi. Hamma holat Supabase'da (service role bilan). Jon tiklanishi so'rov vaqtida hisoblanadi, cron kerak emas.
- **`api/_telegram.js`:** `tg()` hozir faqat `TELEGRAM_BOT_TOKEN` ni ishlatadi. Unga ixtiyoriy `token` parametri qo'shiladi.
- **Yangi env:** `ORGANIKA_BOT_TOKEN`, `ORGANIKA_WEBHOOK_SECRET`, `ORGANIKA_ADMIN_IDS`.
- **Ulash:** `setWebhook` boshqa URL va boshqa secret bilan.
- **Premium bog'lanishi:** foydalanuvchi saytdagi hisobi bilan bir martalik kod orqali bog'lanadi (`/ulash KOD`). Bog'langanda `plans` jadvali bo'yicha Premium ochiladi.

## 3. Ma'lumotlar bazasi (yangi migratsiya)

Fayl: `supabase/migrations/<sana>_organika_bot.sql`. Barcha jadvalda RLS yoqiladi va faqat service role kiradi (mavjud `admin_lockdown` migratsiyasi uslubida).

| Jadval | Asosiy ustunlar |
|---|---|
| `ob_users` | `tg_id` (PK), `name`, `username`, `level` (1–3), `xp`, `hearts`, `hearts_at`, `streak`, `last_play`, `linked_user_id` (null bo'lishi mumkin), `created_at` |
| `ob_questions` | `id`, `chapter`, `part` (nomlanish / olinishi / xossa / zanjir), `kind`, `difficulty` (1–3), `text`, `options` (jsonb), `correct`, `explanation`, `active` |
| `ob_progress` | `tg_id`, `chapter`, `stage`, `best_score`, `done` |
| `ob_runs` | `tg_id` (PK), `chapter`, `stage`, `q_ids`, `idx`, `correct`, `hearts_left`, `boss`, `msg_id` |
| `ob_answers` | `tg_id`, `q_id`, `ok`, `at` (zaif mavzular tahlili uchun) |
| `ob_seasons` | `id`, `starts_at`, `ends_at`, `team_count`, `status` |
| `ob_teams` | `id`, `season_id`, `name`, `emoji` |
| `ob_team_members` | `season_id`, `tg_id`, `team_id`, `joined_at`, `left_at` |
| `ob_xp_daily` | `tg_id`, `day`, `xp` (kunlik 300 chegara shu yerda) |

Jamoa reytingi `view` bilan hisoblanadi: `ob_xp_daily` + `ob_team_members` + faol a'zolar bonusi.

## 4. Buyruqlar va oqim

**O'quvchi:** `/start` (ro'yxat + kirish testi), `/oyin` (bob xaritasi), `/profil` (XP, jon, seriya), `/jamoa`, `/reyting`, `/yordam`, `/ulash KOD`.

**Admin:** `/qura N` (mavsumni N jamoaga bo'lish), `/mavsum_yop`, `/stat` (faol o'quvchilar, eng ko'p xato qilingan savollar).

**Savol oqimi:** bitta xabar `editMessageText` bilan yangilanadi, chat to'lib ketmaydi. Tugma `callback_data` 64 bayt bilan cheklangan, shuning uchun qisqa format: `a:<run>:<idx>:<variant>`. Javobdan keyin: to'g'ri/noto'g'ri, izoh, jon va XP o'zgarishi, «Keyingi» tugmasi.

**Qur'a algoritmi:** o'quvchilar darajasi bo'yicha saralanadi (3, 2, 1), har daraja ichida tasodifiy aralashtiriladi, har biri hozirgi eng kichik jamoaga qo'shiladi. Jamoa nomlari tasodifiy (Alkanlar, Alkenlar, Alkinlar, ...). Har o'quvchiga shaxsiy xabar boradi.

## 5. Kontent rejasi

11 bob: Alkanlar, Alkenlar, Alkinlar, Arenlar, Spirtlar, Aldegidlar va ketonlar, Karbon kislotalar, Efirlar va yog'lar, Aminlar, Aminokislotalar va oqsillar, Polimerlar.

Har bob: 3 qism (nomlanish, olinishi, xossalari) × 10 savol + 10 savollik boss = 40 savol. Jami ≈ 440 savol. Kirish testi: 5 savol.

Savollar JSON/SQL seed fayl sifatida yoziladi: `supabase/seed/organika_bob_01.sql`. Sizning tekshiruvingizdan keyin bazaga yuklanadi.

## 6. Bosqichlar

| # | Bosqich | Natija | Qabul sharti |
|---|---|---|---|
| 0 | Tayyorgarlik | @BotFather'da bot, env o'zgaruvchilar, bo'sh webhook | `/start` ga bot javob beradi |
| 1 | MVP yakka o'yin | Migratsiya, `/start`, kirish testi, 1-bob (Alkanlar, 40 savol), jon, XP, seriya, `/profil` | O'zingiz 1-bobni boshidan oxirigacha o'ynab chiqasiz |
| 2 | Jamoalar | `/qura`, jamoa ballari, kunlik chegara, `/jamoa`, `/reyting`, haftalik yakun e'loni | 12 sinov akkauntda qur'a muvozanatli chiqadi |
| 3 | Kontent | 2–11 boblar (har biri alohida seed fayl, sizning tekshiruvingiz bilan) | Har bob alohida ochiladi |
| 4 | Premium | `/ulash`, bepul: 1-bob + kunlik 5 savol; Premium: barcha boblar | Bepul akkaunt 2-bobni ocholmaydi |
| 5 | Qo'shimcha | 1v1 duel, umumiy boss, zaif mavzu tavsiyasi, tenglama rasmlari | Alohida rejalashtiriladi |

## 7. Xavflar va ehtiyot choralar

- **Telegram qayta yuborish:** javob 200 bo'lmasa update takrorlanadi. Har javob `ob_runs.idx` bilan tekshiriladi, bir savolga ikki marta hisoblanmaydi.
- **Bir vaqtda ikki bosish:** yangilash `where idx = <kutilgan>` sharti bilan, mavjud `status = 'pending'` himoyasi uslubida.
- **Bot bloklangan:** `tg()` xato qaytarsa, o'quvchi jamoa ro'yxatida qoladi, lekin xabar yuborilmaydi.
- **Haftalik yakun:** `vercel.json` ga haftalik cron (Hobby'da kuniga bir marta ruxsat). Kerak bo'lmasa admin `/mavsum_yop` bilan qo'lda yopadi.
- **Savol sifati:** noto'g'ri javobli savol o'quvchini adashtiradi. Har savolda `Xato haqida xabar` tugmasi bo'ladi, `ob_answers` bo'yicha 40% dan past to'g'ri javob olgan savollar admin ro'yxatiga tushadi.
- **Maxfiylik:** faqat Telegram ID, ism va username saqlanadi. Telefon raqami so'ralmaydi.

## 8. Sizdan kerak bo'lgan narsalar

1. @BotFather'da bot yaratish va tokenni berish (yoki shu qadamda yordam so'rash).
2. O'zingizning Telegram ID raqamingiz (admin uchun).
3. Bot nomi va jamoa nomlari ro'yxati (taklifim: kimyo bo'limlari nomlari).
4. 1-bob savollarini tekshirish (bosqich 1 ichida).
