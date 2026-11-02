// Kunlik savollarni tanlash: har o'rindan bitta variant, majburiy moddalar qamrovi, 80/20 takror.
// Tanlov deterministik: bir xil o'quvchi + mavsum + kun har doim bir xil to'plamni oladi (qayta yuklasa ham),
// lekin turli o'quvchilarda to'plamlar farq qiladi.
import { questionKey } from "./chem.js";

export function hash(str) {
  let h = 1779033703 ^ str.length;
  for (let i = 0; i < str.length; i++) { h = Math.imul(h ^ str.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
  h = Math.imul(h ^ (h >>> 16), 2246822507); h = Math.imul(h ^ (h >>> 13), 3266489909);
  return (h ^ (h >>> 16)) >>> 0;
}
export const rng = (seed) => () => {
  seed = (seed + 0x6d2b79f5) | 0;
  let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
};
const pick = (rand, arr) => arr[Math.floor(rand() * arr.length)];
export function shuffle(rand, arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

// Yangi mavzu savollarida daraja ulushlari (%): kun sayin 3-daraja oshadi, 1-daraja kamayadi.
export function levelMix(day) {
  const t = (day - 1) / 23, l3 = Math.round(8 + 72 * t), l1 = Math.round(Math.max(0, 45 - 63 * t));
  return [l1, 100 - l1 - l3, l3];
}

export const REVIEW_COUNT = 6;   // 30 savolning 20%

// days: loadDay() natijalari ro'yxati. history: { errors: { [mavzu]: xato ulushi }, seen: [savol id] } (ixtiyoriy)
export function selectDaily({ day, days, userId, season = 1, history = {} }) {
  const cur = days.find((d) => d.day === day);
  if (!cur) throw new Error("kun topilmadi: " + day);
  const seed = `${userId}:${season}:${day}`;
  const rand = rng(hash(seed));

  // 1) zanjir kabi bog'langan o'rinlar: butun guruh uchun bitta to'plam (A yoki B)
  const bundleChoice = {};
  for (const g of new Set(cur.slots.map((s) => s.bundleGroup).filter(Boolean))) {
    const ids = [...new Set(cur.slots.filter((s) => s.bundleGroup === g).flatMap((s) => s.variants.map((v) => v.bundle)))].sort();
    bundleChoice[g] = pick(rand, ids);
  }

  // 2) har o'rindan bittadan variant, takroriy tenglama/nomsiz
  const chosen = {}, used = new Set();
  for (const s of cur.slots) {
    const pool = s.bundleGroup ? s.variants.filter((v) => v.bundle === bundleChoice[s.bundleGroup]) : s.variants;
    const fresh = pool.filter((v) => !used.has(questionKey(v)));
    const v = pick(rand, fresh.length ? fresh : pool);
    chosen[s.slot] = v; used.add(questionKey(v));
  }

  // 3) majburiy moddalar qamrovi: yetishmaganini boshqa o'rindagi variant bilan almashtirib to'ldiramiz
  // Tepalash: avval qamrovni oshiradigan almashtirish, bo'lmasa bitta modda o'rniga boshqasini to'ldiradigan
  // (yetishmaganni qo'shib, boshqasini yo'qotadigan) tasodifiy almashtirish. Cheklangan qadamlar bilan.
  const need = cur.substances, needSet = new Set(need);
  const covered = () => new Set(Object.values(chosen).flatMap((v) => v.uses));
  const score = () => [...covered()].filter((x) => needSet.has(x)).length;
  for (let iter = 0; iter < 40 && score() < need.length; iter++) {
    const base = score(), have = covered(), better = [], sideways = [];
    for (const s of cur.slots) {
      if (s.bundleGroup) continue;
      for (const v of s.variants) {
        if (v === chosen[s.slot]) continue;
        if (Object.entries(chosen).some(([k, c]) => k !== s.slot && questionKey(c) === questionKey(v))) continue;
        const old = chosen[s.slot]; chosen[s.slot] = v; const sc = score(); chosen[s.slot] = old;
        if (sc > base) better.push([s, v]);
        else if (sc === base && v.uses.some((x) => needSet.has(x) && !have.has(x))) sideways.push([s, v]);
      }
    }
    const moves = better.length ? better : sideways;
    if (!moves.length) break;
    const [s, v] = pick(rand, moves); chosen[s.slot] = v;
  }

  const fresh = cur.slots.map((s) => chosen[s.slot]);

  // 4) takrorlash (2-kundan): 3 ta zaif mavzudan, 2 ta 2–7 kun oldingi, 1 ta eng eskisi
  const review = [];
  if (day > 1) {
    const past = days.filter((d) => d.day < day);
    const seen = new Set(history.seen || []);
    const takenSlots = new Set(), takenKeys = new Set(fresh.map(questionKey));
    const take = (dayObj) => {
      const slots = dayObj.slots.filter((s) => !s.bundleGroup && !takenSlots.has(dayObj.day + s.slot));
      for (let t = 0; t < 12 && slots.length; t++) {
        const s = pick(rand, slots);
        const vs = s.variants.filter((v) => !seen.has(v.id) && !takenKeys.has(questionKey(v)));
        const v = pick(rand, vs.length ? vs : s.variants.filter((x) => !takenKeys.has(questionKey(x))));
        if (!v) continue;
        takenSlots.add(dayObj.day + s.slot); takenKeys.add(questionKey(v));
        review.push({ ...v, review: true, fromDay: dayObj.day });
        return true;
      }
      return false;
    };
    const weakTopics = Object.entries(history.errors || {}).sort((a, b) => b[1] - a[1]).map(([t]) => t);
    const weakDays = weakTopics.map((t) => past.find((d) => d.topic === t)).filter(Boolean);
    // 3 ta zaif o'rin: bitta zaif mavzu bo'lsa hammasi shundan; ikkita va undan ko'p bo'lsa eng zaifidan 2 ta, keyingisidan 1 ta
    const alloc = weakDays.length === 0 ? [null, null, null] : weakDays.length === 1 ? [weakDays[0], weakDays[0], weakDays[0]] : [weakDays[0], weakDays[0], weakDays[1]];
    for (const d of alloc) take(d || pick(rand, past));
    const recent = past.filter((d) => d.day >= day - 7 && d.day <= day - 2);
    for (let i = 0; i < 2; i++) take(recent.length ? pick(rand, recent) : pick(rand, past));
    take(past[0]);
    while (review.length < REVIEW_COUNT && review.length < past.length * 2) if (!take(pick(rand, past))) break;
  }

  // 5) variantlar tartibi har o'quvchida alohida
  const items = [...fresh.map((q) => ({ q, review: false })), ...review.map((q) => ({ q, review: true }))].map(({ q, review: rv }) => {
    const order = q.type === "choice" ? shuffle(rng(hash(seed + ":" + q.id)), [0, 1, 2, 3]) : null;
    return { id: q.id, review: rv, fromDay: q.fromDay || null, order };
  });
  return { items, bundle: bundleChoice, missing: need.filter((s) => !new Set([...fresh, ...review].flatMap((v) => v.uses)).has(s)) };
}
