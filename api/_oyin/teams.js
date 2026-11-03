// Jamoalarni qur'a bilan tuzish. Toza funksiyalar: bazaga tegmaydi, shuning uchun sinab ko'rish oson.
//
// Qur'a kuchlari teng bo'lishi uchun qatlamli: o'quvchilar XP bo'yicha tartiblanadi, har k tasi (k = jamoalar soni)
// bitta qatlamga tushadi, qatlam ichida tasodifiy aralashtiriladi va har jamoaga qatlamdan bittadan beriladi.
// Shunda eng kuchlilar bir jamoaga to'planib qolmaydi. Aralashtirish `seed` bilan takrorlanadi (natijani tekshirsa bo'ladi).

export const TEAM_SIZE = 5;       // maqsadli hajm
export const TEAM_MAX = 7;        // kech qo'shilganlar uchun yuqori chegara
export const LATE_LIMIT_DAY = 18; // bu kundan keyin qo'shilganlar jamoaga kirmaydi

export const TEAM_NAMES = ["Metan", "Etan", "Propan", "Butan", "Etilen", "Atsetilen", "Benzol", "Toluol", "Etanol", "Glitserin",
  "Fenol", "Aseton", "Glyukoza", "Kraxmal", "Anilin", "Glitsin", "Neylon", "Izopren", "Stirol", "Sirka", "Efir", "Alkan", "Alken", "Alkin"];

// mulberry32: kichik, tez, seed bo'yicha takrorlanadigan generator
export function rng(seed) {
  let a = (seed >>> 0) || 1;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
export function shuffle(arr, rand) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

export const teamCount = (n, size = TEAM_SIZE) => (n < 2 ? 0 : Math.max(1, Math.round(n / size)));

// players: [{ user_id, xp }] -> [{ name, members: [user_id] }]
export function drawTeams(players, { size = TEAM_SIZE, seed = Date.now() } = {}) {
  const k = teamCount(players.length, size);
  if (!k) return [];
  const rand = rng(seed);
  const sorted = shuffle(players, rand).sort((a, b) => b.xp - a.xp);   // avval aralashtiramiz: XP teng bo'lsa tartib tasodifiy
  const names = shuffle(TEAM_NAMES, rand);
  const teams = Array.from({ length: k }, (_, i) => ({ name: names[i] || `Jamoa ${i + 1}`, members: [] }));
  const sum = (t) => t.members.reduce((acc, u) => acc + (xp.get(u) || 0), 0);
  const xp = new Map(players.map((p) => [p.user_id, p.xp]));
  const mean = players.reduce((acc, p) => acc + p.xp, 0) / players.length;
  for (let i = 0; i < sorted.length; i += k) {
    const tier = shuffle(sorted.slice(i, i + k), rand);
    if (tier.length === k) { tier.forEach((p, j) => teams[j].members.push(p.user_id)); continue; }
    // to'liq bo'lmagan oxirgi qatlam: har o'quvchi (kuchlisidan boshlab) o'rtachasi umumiy o'rtachaga eng yaqin qoladigan jamoaga tushadi
    const used = new Set();
    for (const p of tier.sort((x, y) => y.xp - x.xp)) {
      let best = null, bestGap = Infinity;
      for (const t of teams) {
        if (used.has(t)) continue;
        const gap = Math.abs((sum(t) + p.xp) / (t.members.length + 1) - mean);
        if (gap < bestGap) { best = t; bestGap = gap; }
      }
      best.members.push(p.user_id); used.add(best);
    }
  }
  return teams;
}

// Kech qo'shilgan o'quvchi uchun jamoa: eng kichik (tenglikda tasodifiy). Hammasi TEAM_MAX bo'lsa null: yangi jamoa ochiladi.
export function pickTeamForLate(teams, rand = Math.random) {
  const open = teams.filter((t) => t.size < TEAM_MAX);
  if (!open.length) return null;
  const min = Math.min(...open.map((t) => t.size));
  const best = open.filter((t) => t.size === min);
  return best[Math.floor(rand() * best.length)].id;
}

export const lateAllowed = (joinedDayNumber) => joinedDayNumber <= LATE_LIMIT_DAY;
