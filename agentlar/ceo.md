# CEO va Hisobchi: bilim hujjati

Vazifa: ustozga har kuni va har hafta bitta xabarda butun tizim holatini aytish. CEO hech narsani o'zi hal qilmaydi va hech kimga yozmaydi: faqat ustozga hisobot beradi. Pul raqamlarini Hisobchi hisoblaydi (`api/_hisobchi.js`), CEO ularni hisobotga qo'yadi.

Kod: `api/_ceo.js`. Kunlik hisobot har kuni 20:00 da (Toshkent), haftalik yakshanba kuni. Xabar ustozning Telegramiga ketadi.

O'rgatish shu hujjat orqali: ustoz hisobotda nimani ko'rishni xohlasa, avval shu yerga yoziladi, keyin kodga ko'chiriladi.

## Kunlik hisobot: qisqa (ustoz 2026-11-19 da ikki ko'rinishdan tanlagan)

Har kuni o'qiladigan xabar qisqa bo'ladi. Tartib:

1. **Sizdan kutilmoqda.** Ustoz biror narsa qilishi kerak bo'lgan ishlar: tasdiq kutayotgan paketlar, botdan uzatilgan savollar, kanaldagi qoralamalar. Bo'lmasa "Sizdan hech narsa kutilmayapti".
2. **O'zgargani.** Yangi o'quvchi, faol o'quvchi, yangi lid, bugungi to'lov, bugun joylangan kontent (bo'lsa).
3. **E'tibor.** Faqat quyidagi qoidalardan biri ishlasa chiqadi.
4. Oxirida: to'liq raqamlar haftalik hisobotda.

Nol bo'lgan qatorlar (masalan "Instagram 0") kunlik hisobotda ko'rsatilmaydi.

## E'tibor qoidalari

Har qator bitta fakt. Baho ("yomon", "past") va maslahat qo'shilmaydi: nima qilishni ustoz hal qiladi.

| Qoida | Qachon chiqadi |
|---|---|
| Pullik o'quvchi kirmayapti | pullik rejadagi o'quvchi 7 kundan beri hech narsa ochmagan |
| To'lov tasdiq kutyapti | tasdiqlanmagan to'lov bor |
| Reja tugayapti yoki tugagan | 3 kun ichida tugaydi yoki tugab, uzaytirilmagan |
| Agentda xato | shu davrda agent xato yozgan |
| Reels joylanmadi | 2026-11-23 dan boshlab, shu kuni Reels joylanmagan bo'lsa (reja: kuniga 1 ta). Faqat kunlik hisobotda |
| Agentlar navbatida ochiq ish | kod yoki platforma agentida hal qilinmagan ish bor |

## Haftalik hisobot: to'liq

Yakshanba kuni: o'quvchilar, sotuv boti, pul, kontent, agentlar ishi, sizdan kutilayotgan ishlar va E'tibor. Yangi hisob va lidlar o'tgan hafta bilan taqqoslanadi. Faol o'quvchilar soni taqqoslanmaydi (baza o'tgan davr uchun ishonchli emas).

## Nimalarni qilmaydi

- O'quvchi, ota-ona yoki mijozga yozmaydi.
- Narx, reja, to'lovni o'zgartirmaydi.
- Sotuv bo'yicha maslahat bermaydi: hozir sotuv yopiq (brend qo'llanmasi), hisobotda faqat faktlar.
- Bo'lmagan raqamni ko'rsatmaydi: ma'lumot olinmasa qator chiqmaydi.
- Bir kunda (haftada) ikki marta yubormaydi.

## Sinov

```bash
node agentlar/ceo_sinov.mjs            # kunlik, hech kimga yuborilmaydi
node agentlar/ceo_sinov.mjs --hafta    # haftalik
```

## Cheklovlar

- Instagram va platformaga joylangan kontent faqat agentlar navbatga "Joylandi" deb yozganda sanaladi. Qo'lda joylangan narsa ko'rinmaydi.
- Pullik o'quvchilarning ismi ko'rsatilmaydi, faqat soni. Kim ekanini nazoratchi hisoboti aytadi.
- Holat: kod tayyor, testdan o'tgan, saytga chiqarilmagan (deploy ustozning "ha" so'zini kutadi).

## O'rganilgan saboqlar

- 2026-11-19, quruq sinov (haqiqiy ma'lumot): eski ko'rinishda yetti qatorning ko'pi nol edi, shuning uchun ustoz qisqa ko'rinishni tanladi. Yangi ko'rinishda birinchi marta "2 ta pullik o'quvchi 7 kundan beri kirmayapti (jami 3)" degan qator chiqdi.
