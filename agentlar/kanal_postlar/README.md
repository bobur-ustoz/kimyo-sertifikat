# Kanal postlari (qoralamalar manbasi)

Har fayl bitta post, Telegram HTML'da. Oxiridagi "Yordamchi bot | Telegram | Instagram" bloki avtomatik qo'shiladi,
shuning uchun faylga yozilmaydi. `01_bot_tanishtiruv.txt` bundan mustasno: uning o'z bloki bor (bot havolasi `?start=kanal`),
u `--imzosiz` bilan qo'shiladi va chiqqach kanalda qo'lda qadab qo'yiladi.

```bash
node agentlar/kanal.mjs qosh 2026-11-20 agentlar/kanal_postlar/01_bot_tanishtiruv.txt --imzosiz
node agentlar/kanal.mjs qosh 2026-11-21 agentlar/kanal_postlar/02_kun_savoli.txt
node agentlar/kanal.mjs royxat
node agentlar/kanal.mjs korsat 1
node agentlar/kanal.mjs tasdiqla 1     # faqat ustoz "tasdiqlayman" degandan keyin
```

Post har kuni 20:00 da (Toshkent), kuniga bittadan chiqadi. So'rovnoma (poll) hozircha qo'llanmaydi, uni ustoz o'zi joylaydi.
