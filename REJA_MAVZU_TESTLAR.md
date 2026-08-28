# Reja — mavzulashtirilgan 43 talik testlar ketma-ketligi

27 ta mazmun elementining har biriga bitta 43 talik test
(`PROMT_MAVZU_VARIANT.md` bo'yicha). **I.6 tayyor** (`variantlar/mavzu_I6.json`),
qolgani **26 ta**.

Tartib taxmin emas — `tahlil/navbat.py` uni uchta o'lchovdan hisoblaydi va
ekranga chiqaradi (`python3 tahlil/navbat.py`):

```
BALL = 2×savol + 1,5×qiyinlik + 2×darslik_bo'shlig'i + 3×yozma_ish
```

| O'lchov | Manba | Nega |
|---|---|---|
| **savol** | `tahlil/v01.json` | Elementdan imtihonda nechta savol chiqadi |
| **qiyinlik** | `tahlil/v01.json` | O'rtacha 1–3; qiyin mavzu ko'proq mashq talab qiladi |
| **darslik bo'shlig'i** | `tahlil/darslik/s0*.json` | Maktab qoplamasa, butun yuk kitobga tushadi |
| **yozma ish** | `tahlil/v01.json` (41/42/43) | 25 ballik topshiriq — eng qimmat savollar |

---

## Ikki xil tartib — chalkashtirmaslik kerak

**YOZISH tartibi** (quyidagi to'lqinlar) — qiymat bo'yicha: eng ko'p ball
keltiradigan, maktab eng ko'p tashlab ketgan mavzu birinchi yoziladi. Har bir
test mustaqil, shuning uchun bu tartibda yozish mumkin.

**O'QISH tartibi** (o'quvchiga berish) — bog'liqlik bo'yicha, ya'ni
spetsifikatsiya tartibining o'zi: I.1 → I.2 → … → IV.2. Muvozanat (I.6)
tezlikdan (I.5) keyin, elektroliz (I.10) OQRdan (I.9) keyin, murakkab efir
(III.7) karbon kislotadan (III.6) keyin tushuniladi.

Ya'ni: **II.4 ni birinchi yozamiz, lekin o'quvchiga birinchi bermaymiz.**

---

## 1-to'lqin — eng katta yutuq (4 ta test)

| # | Element | Mavzu | Ball | Nega birinchi |
|---|---|---|---|---|
| 1 | **II.4** | IIA, IIIA, d-metallar, suv qattiqligi | 21,0 | **7 savol** — imtihonning 16%i, bitta elementdan. Maktab darsligida **umuman yo'q** |
| 2 | **III.1** | Tuzilish nazariyasi, izomeriya, alkanlar | 14,8 | 42-yozma ishni (25 ball) beradi; darslikda yo'q |
| 3 | **I.7** | Eritmalar, konsentratsiya, eruvchanlik | 14,2 | 4 savol; darslikda yo'q; 37-topshiriqda ham chiqadi |
| 4 | **I.9** | Oksidlanish darajasi, OQR | 13,5 | Qiyinlik **3,0** (eng yuqori); 41-yozma ishni beradi. Maktab elektron balansda to'xtaydi, imtihon ion-elektron so'raydi |

Bu to'rttasi tugagach, imtihon ballining eng katta va eng himoyasiz qismi
yopiladi.

## 2-to'lqin — organik plato (7 ta test)

Imtihonning **21–26-pozitsiyalari — uzluksiz eng qiyin blok**, oltala savol
ham qiyinlik 3. Va ular aynan shu elementlarga tegishli:
`21=III.2 · 22=III.3 · 23=III.4 · 24=III.5 · 25=III.6 · 26=III.7`.
Hammasi darslikda yo'q. O'quvchi ball yo'qotadigan asosiy joy shu.

| # | Element | Mavzu | Ball |
|---|---|---|---|
| 5 | III.2 | Alkenlar, alkadiyenlar, alkinlar | 13,0 |
| 6 | III.7 | Efirlar, sovunlar, yog'lar | 12,5 |
| 7 | **IV.2** | Sifat reaksiyalari, tajribalar | 12,5 |
| 8 | III.3 | Arenlar, neft, gaz | 10,5 |
| 9 | III.4 | Spirtlar, fenollar | 10,5 |
| 10 | III.5 | Aldegid va ketonlar | 10,5 |
| 11 | III.6 | Karbon kislotalar | 10,2 |

IV.2 shu to'lqinda, chunki u 43-yozma ishni (25 ball) beradi va 31–32
pozitsiyalarni ham egallaydi.

## 3-to'lqin — qolgan og'ir umumiy kimyo (6 ta test)

| # | Element | Mavzu | Ball |
|---|---|---|---|
| 12 | I.3 | Atom tuzilishi, kvant sonlar | 9,8 |
| 13 | I.10 | Elektroliz, Faradey | 9,0 |
| 14 | I.4 | Kimyoviy bog'lanish, gibridlanish | 9,0 |
| 15 | I.8 | Dissotsiatsiya, pH, gidroliz | 9,0 |
| 16 | II.3 | Metallar, IA guruh | 9,0 |
| 17 | III.10 | Polimerlar | 9,0 |

I.3 va I.4 darslikda "tanish", lekin imtihon darajasidan past to'xtaydi
(kvant sonlar, donor-akseptor, gibridlanish yo'q) — shuning uchun ular ham
shu yerda, pastda emas.

## 4-to'lqin — o'rta og'irlik (5 ta test)

| # | Element | Mavzu | Ball |
|---|---|---|---|
| 18 | III.8 | Uglevodlar | 7,0 |
| 19 | III.9 | Aminlar, aminokislotalar, oqsillar | 6,8 |
| 20 | II.5 | Metallmaslar, vodorod, o'g'itlar | 6,2 |
| 21 | I.2 | Asosiy qonunlar, Avogadro, ekvivalent | 5,5 |
| 22 | I.5 | Reaksiya tezligi | 5,5 |

## 5-to'lqin — yengil yakun (4 ta test)

| # | Element | Mavzu | Ball |
|---|---|---|---|
| 23 | II.2 | Oksid, asos, kislota, tuzlar | 5,5 |
| 24 | **IV.1** | Laboratoriya jihozlari, ajratish usullari | 5,5 ⚠ |
| 25 | I.1 | Asosiy tushunchalar: mol, valentlik | 5,0 |
| 26 | II.1 | Anorganik sinflar, genetik bog'lanish | 3,5 |

⚠ **IV.1 — ehtiyot bo'ling.** U v01 da umuman chiqmagan, shuning uchun ball
past. Lekin bu "chiqmaydi" degani emas: bizda atigi **bitta** haqiqiy variant
bor, n=1 da tanlanma xatosi juda katta. IV.1 spetsifikatsiyada bor va 25
ballik 43-topshiriqni berishi mumkin (v03 ning 43-topshirig'i aynan shunday
yozilgan). Agar yangi haqiqiy variantda IV.1 chiqsa — u darhol yuqoriga
ko'tariladi.

---

## Har bir test qanday yoziladi (bir xil tartib)

1. `PROMT_MAVZU_VARIANT.md` dagi promtni olib, mavzuni ayting.
2. 1–32 (Y1) uchun qiyinlik/kognitiv `tahlil/v01.json` dagi **o'sha
   pozitsiyaning** qiymatidan olinadi.
3. 32 ta Y1 yozilgach — javob harflarini A/B/C/D bo'yicha tenglashtirish
   (8/8/8/8 ga yaqin) va harf to'g'ri variantga ishora qilishini dasturiy
   tekshirish.
4. 33–35 (Y2 jadval) → 36–40 (O1) → 41–43 (O2: 41 chuqur, 42 oddiyroq,
   43 ko'p bandli).
5. `variantlar/verify_mavzu_XXX.py` — har sonli javob ikki mustaqil usulda.
6. mhchem `+` bo'shliq skaneri.
7. PDF: `variantlar/pdf/build.py` → Chrome `--no-pdf-header-footer`.

**Nazorat nuqtasi:** har to'lqin oxirida to'xtab, natijani ko'rsataman —
tasdiqlanmaguncha keyingi to'lqinga o'tmayman.

---

## Tartib qachon o'zgaradi

Bu reja **bitta** haqiqiy variantga (v01) tayanadi. Ikkita narsa uni
o'zgartiradi:

- **Yangi haqiqiy variant kelsa** — pasportlanadi, `tahlil/navbat.py` qayta
  ishga tushiriladi; chastota o'rtachalashadi va tartib aniqlashadi (ayniqsa
  hozir 1 savolli ko'ringan elementlar).
- **9–11-sinf darsliklari kelsa** — `tahlil/darslik/` ga qo'shiladi; hozir
  "yo'q" deb turgan ko'p element aslida 9–11 da o'tilishi mumkin, bu
  darslik bo'shlig'i ballini pasaytiradi va tartibni siljitadi.

Ikkalasi ham bir buyruq bilan qayta hisoblanadi — reja qotib qolmaydi.
