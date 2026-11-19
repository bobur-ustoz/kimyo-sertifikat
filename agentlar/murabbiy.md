# O'quvchi murabbiyi: bilim hujjati

Vazifa: pullik rejadagi o'quvchi yo'ldan chiqib qolmasligi uchun unga shaxsiy, qisqa yo'l-yo'riq yuborish. Maqsad sotish emas, o'quvchi olgan narsasidan foyda ko'rishi. Natija ko'rgan o'quvchi o'zi davom etadi.

Kod: `api/_murabbiy.js`. Har kuni ertalab 9:00 da, nazoratchidan oldin ishlaydi. Xabar yordamchi bot (@Boburkimyoyordamchi_bot) orqali ketadi.

O'rgatish shu hujjat orqali: ustoz xabar matni yoki qoidani o'zgartirsa, avval shu yerga yoziladi, keyin kodga ko'chiriladi.

## Kimga yozadi

Faqat shu to'rt shartning hammasi bajarilsa:
1. Rejasi pullik (Premium yoki Standart) va muddati o'tmagan.
2. Telegramni o'zi ulagan (saytdagi tugma orqali).
3. `/stop` demagan.
4. Oxirgi 2 kunda unga xabar yuborilmagan (nazoratchi eslatmasi ham shu hisobga kiradi).

Bepul rejadagi o'quvchiga hech narsa yozilmaydi. Maktab o'quvchilari orasida bepul foydalanuvchilar ko'p, ularga yozish bosim bo'lib ko'rinadi.

## Qaysi xabar ketadi

Bir kunda bitta xabar. Bir nechta sabab bo'lsa, yuqoridagisi ketadi:

| # | Holat | Xabar mazmuni |
|---|---|---|
| 1 | Reja 3 kun ichida tugaydi | Muddat haqida xabar, shu muddat uchun bir marta. "Davom ettirish yoki to'xtatish sizning ixtiyoringiz." |
| 2 | Hali hech narsa ochmagan | Qaysi mavzudan boshlash mumkinligi |
| 3 | 3 kun va undan ko'p kirmagan | Qayerda to'xtagani va keyingi qadam |
| 4 | Bir mavzudan 6+ savol yechib, yarmidan kamini to'g'ri topgan | Shu mavzu darsini qayta ko'rish taklifi |
| 5 | Yakshanba, hafta davomida faol bo'lgan | Haftalik natija va keyingi hafta uchun mavzu |

Faol va muammosiz o'quvchiga oddiy kunda hech narsa yozilmaydi.

**Keyingi qadam qanday tanlanadi:** oxirgi ko'rgan mavzusining hali ko'rmagan misoli (misollar faqat Premium rejada). Misollar tugagan bo'lsa, tartib bo'yicha keyingi videoli mavzu.

## Ohang qoidalari

Ustoz 2026-11-19 da uch namunadan "ustoz ohangi"ni tanladi: xabar botdan emas, ustozdan kelgandek iliq o'qiladi.

- Salomlashish: "Assalomu alaykum, <ism>!" (ismi bo'lmasa "Assalomu alaykum!").
- Avval hol so'raladi ("Hammasi joyidami?"), keyin qayerga yetgani va keyingi qadam.
- So'zlashuv shakli: "yechibsiz", "ko'ribsiz", "chiqibdi". Faol hafta uchun "Barakalla".
- Faktlar bilan: "6 ta savol yechibsiz, 2 tasi to'g'ri chiqibdi". Baho berilmaydi ("yomon", "sust" deyilmaydi).
- Tekshirib bo'lmaydigan gap qo'shilmaydi: "oson mavzu", "ko'pchilik qiynaladi". Bunday gap faqat ustoz aniq mavzu uchun yozib bersa qo'yiladi.
- "Menga yozing" deyilmaydi, "shu yerga yozing" deyiladi: javobni yordamchi bot beradi, kerak bo'lsa ustozga uzatadi. O'quvchi ustoz o'zi javob beradi deb o'ylamasligi kerak.
- Uyaltirish yo'q, taqqoslash yo'q (boshqa o'quvchilar bilan solishtirilmaydi).
- Natija va'dasi yo'q ("albatta o'tasiz" deyilmaydi).
- Bosim yo'q: "shoshiling", "oxirgi imkoniyat", chegirma taklifi yo'q.
- Har xabar oxirida: "Bunday xabarlar kerak bo'lmasa, /stop deb yozing."

Namuna (9 kun kirmagan o'quvchi):
> Assalomu alaykum, Aziza! 9 kundan beri ko'rinmay qoldingiz. Hammasi joyidami? Oxirgi marta "Reaksiyali proporsiya" mavzusigacha yetib kelgan edingiz. Keyingisi: "Beqaror moddalar" mavzusi. Vaqt topsangiz shundan davom eting. Tushunmagan joy bo'lsa shu yerga yozing.

Bu qoidalar testda tekshiriladi: taqiqlangan so'zlar chiqsa test o'tmaydi.

## Nimalarni qilmaydi

- Ota-onaga yozmaydi, guruhga yozmaydi.
- O'quvchi javob yozsa, suhbatni o'zi olib bormaydi: bu sotuv botining ishi.
- Reja, narx va to'lovni o'zgartirmaydi.
- Past natijali o'quvchini ustozga "yomon o'quvchi" deb ko'rsatmaydi. Ustoz hisobotida faqat faktlar bo'ladi (nazoratchi).

## Ustoz uchun

- Har kuni navbatga bitta yozuv tushadi: nechta o'quvchiga, qanday turdagi xabar ketgani. CEO hisobotida "O'quvchi murabbiyi" qatorida ko'rinadi.
- Kim nima olishini oldindan ko'rish: `node agentlar/murabbiy_sinov.mjs` (hech kimga yuborilmaydi). Yakshanba kuni uchun: `--yakshanba`.

## Cheklovlar

- Telegramni ulamagan pullik o'quvchiga yetib bo'lmaydi. Ular nazoratchi hisobotida "o'zingiz bog'laning" deb chiqadi.
- Qiyin mavzu savolning `topic` maydoniga qarab aniqlanadi. Savolda mavzu yozilmagan bo'lsa, u hisobga kirmaydi.
- Baza har video uchun faqat oxirgi ko'rilgan vaqtni saqlaydi, shuning uchun "bu hafta nechta video" soni shu haftada oxirgi marta ochilgan videolar soni.
- Xabarlar qolip asosida yoziladi (AI emas): bir xil holatda bir xil matn. Bu ataylab: o'quvchiga ketadigan har so'z oldindan ma'lum va tekshirilgan.

## O'rganilgan saboqlar

(Birinchi haqiqiy xabarlardan keyin to'ldiriladi: o'quvchilar qanday javob berdi, kim `/stop` qildi.)
