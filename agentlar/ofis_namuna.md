# "AI ofis" namunasi (ustoz 2026-11-19 da yuborgan ekran yozuvi)

Manba: @yulduz_aiproducer Reelsi, 45 soniya. Ovoz matni: `agentlar/instagram/namunalar/namuna3.txt`. Kadrma-kadr ko'rildi; ekran telefonga noutbukdan olingan, mayda yozuvlar o'qilmadi.

## Nima ko'rsatilgan

Agentlar jamoasi uchun ko'rgazmali boshqaruv sahifasi ("AI agentlar jamoasi"). Uch qatlam:

1. **Ofis (bosh sahifa).** Tepadan ko'rinadigan 3D ofis: har agentning o'z xonasi va yorlig'i (Direktor, Strateg, Ssenarist, Montajyor, Dizayner, Targetolog va boshqalar, jami 8 ta). Pastda agentlar tugmalari qatori (Ofis, Brifing, Voronka, Direktor, Strateg, Ssenarist, Prognozchi, Montajyor, Dizayner).
2. **Agent xonasi.** Agent bosilsa xonasi yaqinlashadi (robot qahramon, stol, ekranlar) va kichik karta chiqadi: nomi, roli, hozir nima qilayotgani ("Kutmoqda. Oxirgi: ..."), ikki-uch raqam va "Kabinetni ochish" tugmasi.
3. **Kabinet.** Agentning to'liq sahifasi:
   - samaradorlik (foiz) va o'rtacha bajarish vaqti ("1 daq 55 s");
   - hozirgi holati va oxirgi vazifasining matni;
   - qobiliyatlari (skillari);
   - raqamlar: jami vazifalar, portfeldagi ishlar, eng tez natija ("15 s");
   - "Ishlari": bajargan ishlarining rasmli galereyasi, tur bo'yicha saralash (Post, Sayt, Rasm, Bot).

Muallif aytgani: har agentning nima bilan band ekani, oxirgi ishlari va bugungi vazifalari ko'rinadi; kabinetda skillari va shu paytgacha qilgan ishlari; rekord natija 15 soniya; 8 agent bilan media jamoani boshqarsa bo'ladi; agentlar direktor agent orqali bir-biriga vazifa uzatadi (buni 22-noyabr seminarida ko'rsatmoqchi).

## Bizda nima bor, nima yo'q

| Namunadagi narsa | Bizda |
|---|---|
| Agentlar ro'yxati va rollari | bor: 15 agent (`agentlar/README.md`) |
| Hozir nima qilayotgani, oxirgi ishlari | bor: `agent_navbat` jadvali (ish, xato, savol, hisobot) |
| Bugungi vazifalar, ustozdan kutilayotgan ishlar | bor: navbatdagi ochiq yozuvlar, CEO hisoboti |
| Qobiliyatlari (skillar) | bor: har agentning bilim hujjati |
| Ishlar galereyasi | qisman: fayllar bor (Reels, muqova, PDF), lekin bir joyga yig'ilmagan |
| Bajarish vaqti, rekord, samaradorlik foizi | yo'q: navbatda ish qancha vaqt olgani yozilmaydi |
| Direktor agent vazifa tarqatishi | qisman: CEO faqat hisobot beradi, vazifa bermaydi |
| Ko'rgazmali sahifa (ofis, xona, kabinet) | yo'q |

## Xulosa

Namunaning kuchi ma'lumotda emas, ko'rsatishda: ustoz bitta sahifada hamma agentni ko'radi va bosib ichiga kiradi. Bizda ma'lumot bor, sahifa yo'q. Qurilsa, brend uslubida (tungi ko'k + sariq) bo'ladi. 3D ofis va robot qahramonlar bezak: asosiy foyda agent kartalari va kabinetda.
