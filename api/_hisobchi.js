// Hisobchi: to'lovlar va rejalar bo'yicha hisob (faqat hisoblaydi, hech narsani o'zgartirmaydi va hech kimga yozmaydi).
// Natijasi CEO hisobotiga (api/_ceo.js) kiradi.
//
// Manba: variant_purchases (status, amount, paid_at, plan_id) va profiles (plan, plan_expires_at).
// Cheklov: reja to'lovi har o'quvchi uchun BITTA qator (student_id + plan_id yagona). O'quvchi rejani uzaytirsa
// o'sha qator yangilanadi, eski to'lov sanasi yo'qoladi. Shuning uchun o'tgan oylar tushumi uzaytirishlardan keyin
// kam ko'rinishi mumkin: aniq tarix uchun alohida to'lovlar jurnali kerak (hali yo'q).

const DAY = 86400e3;
export const TUGASH_KUN = 7;      // reja shuncha kun ichida tugasa ogohlantiriladi
const ms = (t) => (t ? new Date(t).getTime() : 0);
export const som = (n) => `${Math.round(n).toLocaleString("ru-RU").replace(/ |,/g, " ")} so'm`;
// Asia/Tashkent (UTC+5, yozgi vaqt yo'q) bo'yicha oy boshi.
export const oyBoshi = (now) => { const t = new Date(now.getTime() + 5 * 3600e3); return new Date(Date.UTC(t.getUTCFullYear(), t.getUTCMonth(), 1) - 5 * 3600e3); };
const ism = (p) => p.full_name || String(p.email || "").split("@")[0] || "Noma'lum";

// purchases: variant_purchases qatorlari; profiles: barcha profillar; boshi..now: hisobot davri.
export function moliya({ purchases = [], profiles = [], now = new Date(), boshi }) {
  const t = now.getTime(), b = boshi ? boshi.getTime() : t - DAY, oy = oyBoshi(now).getTime();
  const paid = purchases.filter((p) => p.status === "paid" && p.paid_at);
  const yig = (rows) => rows.reduce((s, p) => s + (Number(p.amount) || 0), 0);
  const davr = paid.filter((p) => ms(p.paid_at) >= b && ms(p.paid_at) <= t);
  const tur = (p) => p.plan_id || (p.live_lesson_id ? "jonli dars" : "variant");
  const turlar = {};
  for (const p of davr) { const k = tur(p); (turlar[k] ||= { soni: 0, summa: 0 }); turlar[k].soni++; turlar[k].summa += Number(p.amount) || 0; }

  const talaba = profiles.filter((p) => !p.is_admin && p.plan && p.plan !== "free");
  const faolmi = (p) => !p.plan_expires_at || ms(p.plan_expires_at) > t;
  const faol = { premium: 0, standart: 0 };
  for (const p of talaba) if (faolmi(p) && p.plan in faol) faol[p.plan]++;
  const kun = (p) => Math.ceil((ms(p.plan_expires_at) - t) / DAY);
  const tugaydi = talaba.filter((p) => p.plan_expires_at && faolmi(p) && kun(p) <= TUGASH_KUN)
    .map((p) => ({ ism: ism(p), plan: p.plan, kun: kun(p) })).sort((x, y) => x.kun - y.kun);
  // Muddati o'tgan, lekin rejasi hali "free" ga qaytarilmagan: uzaytirmagan o'quvchilar.
  const tugagan = talaba.filter((p) => p.plan_expires_at && !faolmi(p) && t - ms(p.plan_expires_at) <= TUGASH_KUN * DAY)
    .map((p) => ({ ism: ism(p), plan: p.plan, kun: Math.floor((t - ms(p.plan_expires_at)) / DAY) }));
  const kutmoqda = purchases.filter((p) => p.status === "pending");

  return {
    davr: { summa: yig(davr), soni: davr.length, turlar },
    oy: { summa: yig(paid.filter((p) => ms(p.paid_at) >= oy && ms(p.paid_at) <= t)) },
    jami: { summa: yig(paid), soni: paid.length },
    faol, tugaydi, tugagan,
    kutmoqda: { soni: kutmoqda.length, summa: yig(kutmoqda) },
  };
}

// Hisobotning "Pul" bo'limi (HTML emas, oddiy qatorlar; CEO o'zi qochiradi).
export function moliyaQatorlar(m, { haftalik = false } = {}) {
  const q = [];
  const turlar = Object.entries(m.davr.turlar).map(([k, v]) => `${k} ${v.soni} ta`).join(", ");
  q.push(m.davr.soni ? `${haftalik ? "Hafta" : "Bugun"} tushum: ${som(m.davr.summa)} (${turlar})` : `${haftalik ? "Bu hafta" : "Bugun"} to'lov bo'lmadi`);
  q.push(`Shu oy: ${som(m.oy.summa)}`);
  q.push(`Faol rejalar: Premium ${m.faol.premium} ta, Standart ${m.faol.standart} ta`);
  if (m.kutmoqda.soni) q.push(`Tasdiq kutayotgan to'lov: ${m.kutmoqda.soni} ta (${som(m.kutmoqda.summa)})`);
  for (const x of m.tugaydi) q.push(`⏳ ${x.ism}: ${x.plan} ${x.kun <= 0 ? "bugun tugaydi" : `${x.kun} kunda tugaydi`}`);
  for (const x of m.tugagan) q.push(`⚠️ ${x.ism}: ${x.plan} ${x.kun === 0 ? "bugun tugadi" : `${x.kun} kun oldin tugadi`}, uzaytirmagan`);
  return q;
}
