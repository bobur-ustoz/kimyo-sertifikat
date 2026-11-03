# AI ishchilar tizimi — Bobur brendi

Maqsad: ustozning shaxsiy brendini Telegram va Instagram orqali o'stirish va platformadagi (kimyo-sertifikat.vercel.app) Premiumni sotish. Hammasi o'quvchining o'z ixtiyori bilan, majburlashsiz.

## Kanallar va roli
| Kanal | Vazifa |
|---|---|
| Instagram | Yangi odamlarni jalb qilish va ishonch (reels, karusel) |
| Telegram kanal (t.me/KimyogarBobur, ~799 obunachi) | Iliq auditoriya, yangilik, eslatma |
| Telegram bot | Lid bilan suhbat, bepul sinov, to'lovga olib borish |

Voronka: Instagram/Kanal -> bot -> bepul sinov -> Premium (200 000 so'm / 30 kun).

## Auditoriya guruhlari
1. Avvalgi o'quvchilar (ustozni biladi) — eng arzon va tez yo'l.
2. Maktabdagi o'quvchilar — sotish mumkin, lekin faqat o'zi so'rasa. Bosim yo'q.
3. Sovuq auditoriya (Instagram) — hali isbotlanmagan, kichik test bilan sinaymiz.

Hozirgi holat: ~51 ta hisob, 3 ta Premium (2 tasi avvalgi o'quvchi, 1 tasi tashqi).

## Agentlar
| Agent | Hujjat | Holat |
|---|---|---|
| Sotuv menejeri (Telegram bot) | `sotuv.md` | Bilim hujjati qoralama |
| Kontentchi | `kontentchi.md` | Qoidalar va 2 haftalik reja qoralama |
| Direktor (kunlik hisobot) | — | Keyin |
| Targetolog, qo'ng'iroq, Bitrix | — | Hozir kerak emas |

## Qat'iy qoidalar (barcha agentlar uchun)
- Majburlash yo'q. Taklif bir marta, rad etilsa to'xtaydi.
- Bo'lmagan natija, chegirma yoki kafolat va'da qilmaydi.
- Ustoz yozmagan ma'lumotni (narx, shart, sana) o'zidan to'qimaydi. Bilmasa odamga uzatadi.
- Maktab o'quvchisiga o'zi so'ramaguncha sotuv xabari yubormaydi.
- Narx va to'lov tartibini o'zgartirmaydi, hech qachon karta/parol so'ramaydi.
- Deploy va yuborish faqat ustoz aytgandan keyin.

## Sotuv botni ishga tushirish (kod tayyor, deploy qilinmagan)
Kod: `api/_sotuv.js`, `api/organika-webhook.js?bot=sotuv`, `supabase/migrations/20261106000000_sotuv_bot.sql`.
Bilimni o'zgartirsangiz: `agentlar/sotuv.md` ni tahrirlang, keyin `node agentlar/sync_prompt.mjs`.

1. @BotFather'da yangi bot yarating, tokenni oling.
2. Supabase SQL Editor'da migratsiyani ishga tushiring.
3. Vercel env: `SOTUV_BOT_TOKEN`, `SOTUV_WEBHOOK_SECRET` (tasodifiy qator), `ANTHROPIC_API_KEY` (bor bo'lishi kerak), ixtiyoriy `SOTUV_MODEL`, `SITE_URL`.
4. Deploy, keyin `setWebhook`: url `https://<sayt>/api/organika-webhook?bot=sotuv`, `secret_token` = `SOTUV_WEBHOOK_SECRET`.
5. Botga o'zingiz yozib sinab ko'ring; ustozga xabarlar mavjud admin chatga keladi.

## Tartib
1. Sotuv agenti bilim hujjatini to'ldirish (ustoz tekshiradi, 3 ta Premium o'quvchi suhbati bilan boyitiladi).
2. Kontentchi bilan 2 haftalik Instagram + Telegram reja.
3. Telegram orqali kirish va botni platformaga ulash.
4. Sotuv bot, keyin Direktor hisoboti.
