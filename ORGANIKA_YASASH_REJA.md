# Organika veb o'yini: qurilish rejasi

24 kunlik o'yin: har kuni yangi mavzu (80% yangi, 20% takror), oshib boruvchi qiyinlik, har o'quvchiga boshqa savollar to'plami (variantlar), maxfiy topshiriq va tuzoq, stavka, jamoa. Namuna: Artifact (bosiladigan dizayn). Mavzular va jadval: `ORGANIKA_MAVZULAR.md`.

## Tuzilma

| Qatlam | Joyi | Vazifasi |
|---|---|---|
| Kontent | `supabase/seed/oyin/kun_NN.json` | Har kun: o'rinlar (slot), har o'rinda 2–3 variant, tuzoq belgisi, majburiy moddalar |
| Dvigatel | `api/_oyin/` | Javobni tekshirish, kunlik to'plam tanlash, ball hisoblash, mijozga javobsiz ko'rinish |
| Baza | `og_*` jadvallari (migratsiya `20261104000000_oyin_game.sql`) | Savollar banki (javoblar `secret` da), o'quvchi holati, kunlik to'plamlar, javoblar |
| Server API | (Faza 2) | Brauzerdan keladigan so'rovlar: bugungi to'plam, javob yuborish |
| Sayt | (Faza 3) `src/Oyin.jsx` | Namunadagi dizaynning React varianti, saytdagi hisob bilan |
| Telegram bot | mavjud `api/organika-webhook.js` | Alohida (ob_* jadvallari); keyin eslatmalar uchun ishlatiladi |

**Xavfsizlik asosi:** to'g'ri javoblar faqat serverda. Mijozga savol matni, rasm va (aralashtirilgan) variantlar boradi, javob esa tekshirilgandan keyin ochiladi. Shu sababli bir o'quvchi boshqasiga "3-savol B" deb javob bera olmaydi va brauzer kodidan javobni ko'rib bo'lmaydi.

## Faza 1: poydevor (TAYYOR)

- [x] **Kontent formati v2:** o'rin + variantlar, `uses` (majburiy moddalar), `trap` (tuzoq variant va izohi), `bundleGroup` (zanjir kabi bog'langan o'rinlar).
- [x] **1-kun (Alkanlar):** 30 o'rin, 64 variant, 7 ta tuzoqli o'rin, 8 ta majburiy modda.
- [x] **Dvigatel** `api/_oyin/`: `chem.js` (tenglama va tuzilish tekshiruvi), `select.js` (80/20 tanlov, variantlar, qamrov, zaif mavzu ustuvorligi), `score.js` (ball qoidalari), `view.js` (javobsiz ko'rinish), `content.js`.
- [x] **Tekshiruv:** `node supabase/seed/oyin/check.mjs <kun.json>` (har variant to'g'riligi, 1000 tasodifiy o'quvchi uchun tanlov). `npm test`: 11 ta sinov.
- [x] **Baza sxemasi** (migratsiya yozilgan, PostgreSQL parseri bilan sintaksisi tekshirilgan, **hali bazada bajarilmagan**).
- [x] **Yuklash skripti** `supabase/seed/oyin/load.mjs` (UTF-8 xavfsiz).

## Faza 2: server API (to'xtab turibdi: Vercel chegarasi)

**Muammo:** Vercel bepul rejada ko'pi bilan **12 ta funksiya**; hozir aynan 12 ta. Yangi API fayli qo'shsak, deploy yiqiladi.

Yo'llar:
1. **`faq.js` va `flag-answer.js` ni bitta funksiyaga birlashtirish** (ikkisi ham video savollar bilan ishlaydi). Eski manzillar `vercel.json` rewrites orqali saqlanadi, sayt kodi o'zgarmaydi. Bitta joy bo'shaydi. *Tavsiya.*
2. Vercel Pro rejasiga o'tish (funksiya chegarasi yo'q).
3. O'yin API'sini mavjud funksiyalardan biriga qo'shish (aralash mas'uliyat, tavsiya etilmaydi).

Rejalashtirilgan API (bitta funksiya, `action` bo'yicha): `today` (bugungi to'plam, mijoz ko'rinishida), `answer` (javob yuborish: serverda tekshiriladi, ball, tuzoq, stavka), `stake` (stavka tanlash), `state` (progress, kalendar). Har javob `(user, mavsum, kun, pozitsiya)` bo'yicha bir marta hisoblanadi (takroriy so'rov XP ni oshirmaydi).

## Faza 3: sayt (React)
Namunadagi ekranlarni `src/Oyin.jsx` ga ko'chirish: xarita, savol, yig'ish, klaviatura bilan tenglama yozish, 24 kunlik kalendar, profil. Saytdagi mavjud kirish tizimi va Premium bilan bog'lash (qaysi kunlar bepul, qaysilari pullik, hal qilinadi).

## Faza 4: o'yin mexanikalari
Stavka (faqat 3-daraja, kuniga 2 ta, xato: kunlik reyting −10, XP kamaymaydi), tuzoq (faqat shaxsiy, kunlik bonusni olib qo'yadi), maxfiy topshiriq (shaxsiy va jamoaviy), seriya va qalqon, xatolar daftari, tezkor raund, xatoni top. Kunlik bonus +20, tuzoqqa tushsa 0.

## Faza 5: jamoalar
Tasodifiy va muvozanatli jamoalarga bo'lish (admin buyrug'i), jamoa balli (oddiy ball, stavka va tuzoq ta'sir qilmaydi), haftalik jamoa boss, reyting.

## Faza 6: kontent, 2–24 kunlar
Har kun fayli `check.mjs` dan o'tishi shart. Kunlik 24 yangi o'rin (+6 takror). Aminokislotalar (24-kun) uchun hujjatdagi bo'shliqlar to'ldirilishi kerak. Kimyo mazmunini har kun uchun siz tekshirasiz.

## Qarorlar (tasdiqlangan)
- 24 kun; yangi kun 00:00 (Toshkent); yopilmagan kunlar kuniga 2 tadan ko'p emas yopiladi; mavsum hamma uchun bir sanada boshlanadi.
- Umumiy XP hech qachon kamaymaydi. Jazo faqat kunlik reyting va bonuslarga.
- Variantlar teng qiyin; majburiy moddalar har o'quvchida bir martadan kam emas uchraydi.
- Tuzoq faqat shaxsiy, jamoaga ko'rinmaydi va ta'sir qilmaydi.

## Ochiq savollar
- Funksiya chegarasi: 1-yo'l (birlashtirish) yoki Pro reja?
- Qaysi kunlar bepul, qaysilari Premium?
- Mavsum boshlanish sanasi.
