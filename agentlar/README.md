# Agentlar tizimi: Kimyogar Bobur

Maqsad: ustozning shaxsiy brendini Instagram va Telegram orqali o'stirish, nooracademy platformasini (kimyo-sertifikat.vercel.app) yuritish va Premiumni sotish. Hammasi o'quvchining o'z ixtiyori bilan, majburlashsiz.

Holat sanasi: 2026-11-19. Qurilish tugadi, endi o'rgatish va birin-ketin sinash bosqichi.

## Agentlar

| Guruh | Agent | Qayerda ishlaydi | Bilim hujjati | Kod | Holat |
|---|---|---|---|---|---|
| Kontent | Marketolog | Kompyuter ("boshla") | `marketolog.md` | `marketing_lib.mjs`, `marketing_malumot.mjs` | Qurilgan, sinalmagan |
| Kontent | Montaj | Kompyuter | `.claude/agents/montaj-agent.md` | `~/reels-tool/` | Ishlaydi |
| Kontent | Reels montajchisi | Kompyuter | `reels_montaj.md` | `instagram/asboblar/reels_montaj.py`, `instagram/hyperframes/sahna.py` | O'rgatildi (uslub tanlangan), sinov video chiqdi |
| Kontent | Instagram agenti | Kompyuter, Chrome | `instagram_agent.md` | `instagram/asboblar/` | Qurilgan, 1 paket "joyla" kutyapti |
| Kontent | Kanal postchisi | Server, 20:00 | `kanal_postlar/README.md` | `api/_kanal.js`, `kanal.mjs` | Deploy kutyapti, 4 qoralama |
| Kontent | Izoh javobchisi | | | | Meta ilovasini kutadi |
| Platforma | Platforma agenti | Kompyuter ("boshla") | `platforma_agent.md` | `platforma.mjs`, `transkript.mjs` | Qurilgan, haqiqiy yuklash sinalmagan |
| Platforma | Imtihon tuzuvchi | Kompyuter | `.claude/agents/imtihon-agent.md` | | Ishlaydi |
| Platforma | PDF dizayneri | Kompyuter | `pdf_dizayn.md` | `pdf/pdf_yasash.py` | O'rgatildi (uslub tanlangan), sinov PDF chiqdi |
| Platforma | Ovozli yechim | Kompyuter | `video/namuna/USLUB.md` | | Yarim tayyor (ElevenLabs) |
| O'quvchilar | Sotuv boti | Server, doim | `sotuv.md` | `api/_sotuv.js` | Ishlaydi (saytda) |
| O'quvchilar | O'quvchi murabbiyi | Server, 09:00 | `murabbiy.md` | `api/_murabbiy.js` | O'rgatildi (ustoz ohangi), deploy kutyapti |
| Nazorat | Nazoratchi | Server, 09:00 | | `api/_nazorat.js`, `api/_tekshiruv.js` | O'quvchilar hisoboti ishlaydi; xato qidirish deploy kutyapti |
| Nazorat | Kod agenti | Kompyuter (Claude Code) | | | Ishlaydi; navbatdan o'zi olishi yo'q |
| Nazorat | Hisobchi | Server, 20:00 | `ceo.md` | `api/_hisobchi.js` | Deploy kutyapti |
| Nazorat | CEO | Server, 20:00 (yakshanba: haftalik) | `ceo.md` | `api/_ceo.js` | O'rgatildi (qisqa kunlik hisobot, e'tibor qoidalari), deploy kutyapti |

Umumiy navbat (`agent_navbat` jadvali, `api/_navbat.js`, `navbat.mjs`) saytda ishlayapti: har agent ishini, xatosini va ustozga savolini shu yerga yozadi.

## AI ofis (2026-11-19)

Hamma agentni bitta sahifada ko'rsatadigan 3D ofis: 16 xona, har birida robot va kasbiga mos buyumlar. Xonalar to'rt bo'limga ajratilgan, har biri alohida maydonchada: Kontent (6), O'quvchilar (2), Platforma (4), Nazorat (4). Bo'lim nomi bosilsa kamera shu bo'limga yaqinlashadi. Agent bosilsa karta (hozirgi holati, oxirgi ishi), undan kabinet (qobiliyatlari, oxirgi ishlari, ustozdan kutayotgan narsalari).

```bash
node agentlar/ofis.mjs          # keyin brauzerda http://localhost:5183
```

- Faqat shu kompyuterda ishlaydi, faqat o'qiydi. Ma'lumot `agent_navbat` jadvalidan (oxirgi 30 kun), sahifa har ochilganda yangilanadi.
- Agentlar ro'yxati va qobiliyatlari `agentlar/ofis.mjs` dagi `AGENTLAR` da: yangi agent qo'shilsa yoki holati o'zgarsa shu yer yangilanadi.
- Agent ishini navbatga yozmasa, ofisda ko'rinmaydi.
- Bajarish tezligi va rekord yo'q: navbatga ish boshlangan vaqt yozilmaydi.
- Saytning admin qismiga hali qo'yilmagan (telefondan ko'rish uchun deploy kerak).
- Namuna va undan o'rganilgani: `agentlar/ofis_namuna.md`. Bitta xonali birinchi sinov: `agentlar/ofis/sinov_xona.html`.

## Quruq sinovlar (hech narsa o'zgarmaydi, hech kimga yuborilmaydi)

```bash
node agentlar/navbat.mjs xulosa --kun 7
node agentlar/ceo_sinov.mjs [--hafta]
node agentlar/tekshiruv_sinov.mjs
node agentlar/murabbiy_sinov.mjs [--yakshanba]
node agentlar/marketing_malumot.mjs [--kun 30]
node agentlar/platforma.mjs holat
node agentlar/kanal.mjs royxat
npm test
```

## Qat'iy qoidalar (barcha agentlar uchun)

- Majburlash yo'q. Taklif bir marta, rad etilsa to'xtaydi.
- Bo'lmagan natija, chegirma yoki kafolat va'da qilinmaydi.
- Ustoz yozmagan ma'lumot (narx, shart, sana) o'ylab topilmaydi. Bilmasa odamga uzatadi.
- Maktab o'quvchisiga o'zi so'ramaguncha sotuv xabari yuborilmaydi.
- Narx va to'lov tartibi o'zgartirilmaydi, karta yoki parol so'ralmaydi.
- Tasdiqlar: Instagram va platformaga joylashdan oldin "joyla", kanal postiga "tasdiqlayman", saytga chiqarishdan (deploy) oldin "ha".
- Hech narsa o'chirilmaydi: video, mavzu, matn, asl fayl.
- Kalit va tokenlar chatga yozilmaydi.

## O'rgatish

O'rgatish har agentning bilim hujjatini yaxshilash orqali. Manbalar, foydasi bo'yicha: ustozning tajribasi va qoidalari, haqiqiy natijalar, mutaxassislar darslari (tamoyil olinadi, nusxa emas; YouTube videosining faqat subtitr matni o'qiladi).

## Deploy kutayotgan ishlar

Bitta deployga jamlanadi, ustozning "ha" so'zidan keyin:
- Kanal postchisi, platforma tekshiruvi, CEO va Hisobchi, O'quvchi murabbiyi (hammasi `api/keepalive.js` orqali mavjud ikki kronga ulangan, yangi kron yo'q).
- SQL: `supabase/migrations/20261119010000_murabbiy.sql` (ixtiyoriy, usiz ham ishlaydi). `kanal_postlar` va `agent_navbat` jadvallari yaratilgan.
- Botning kanalga adminligi (faqat Post Messages) saqlanganini tekshirish.
