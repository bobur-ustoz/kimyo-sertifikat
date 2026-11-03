// Ball hisoblash qoidalari (tasdiqlangan):
//  - umumiy XP hech qachon kamaymaydi;
//  - oddiy savol: to'g'ri +10 XP va +10 reyting, xato 0;
//  - stavka (faqat 3-daraja, kuniga 2 tagacha): to'g'ri +20/+20, xato XP 0 va reyting -10 (qalqon bekor qiladi);
//  - qayta o'ynalgan bosqichda to'g'ri javob +3;
//  - tuzoq variant tanlansa: kunlik bonus berilmaydi (jazo emas), tuzoqdan qochgan "Ehtiyotkor" nishonini oladi;
//  - kunlik reyting balli 0 dan pastga tushmaydi.

export const POINTS = { correct: 10, replay: 3, stakeMult: 2, stakeLoss: 10, dailyBonus: 20, maxStakes: 2, late: 5 };

// Savol uchun soniyalar: tanlov 30, yozma 90, stavka 60. Vaqt tugasa ham javob beriladi, lekin to'g'ri javob +5.
export const TIME_LIMIT = { choice: 30, write: 90, build: 90, num: 120, stake: 60 };
export const timeLimit = (type, stake) => (stake ? TIME_LIMIT.stake : TIME_LIMIT[type] || 30);
export const isLate = (ms, type, stake) => Number.isFinite(ms) && ms > (timeLimit(type, stake) + 2) * 1000;

export const canStake = ({ lvl, stakesUsed }) => lvl === 3 && stakesUsed < POINTS.maxStakes;

// -> { xp, rank, stakeLost, shieldUsed }
export function scoreAnswer({ ok, stake = false, replay = false, hasShield = false, late = false }) {
  const base = replay ? POINTS.replay : late ? POINTS.late : POINTS.correct;
  if (ok) {
    const m = stake ? POINTS.stakeMult : 1;
    return { xp: base * m, rank: base * m, stakeLost: false, shieldUsed: false };
  }
  if (!stake) return { xp: 0, rank: 0, stakeLost: false, shieldUsed: false };
  return hasShield
    ? { xp: 0, rank: 0, stakeLost: false, shieldUsed: true }
    : { xp: 0, rank: -POINTS.stakeLoss, stakeLost: true, shieldUsed: false };
}

// Kunlik reyting balli manfiy bo'lmasligi uchun
export const applyRank = (current, delta) => Math.max(0, current + delta);

// Kun tugaganda: tuzoqqa tushgan o'quvchi bonusdan mahrum, qolganlar oladi
export function dailyBonus({ completed, trapHit }) {
  return completed && !trapHit ? POINTS.dailyBonus : 0;
}

export const prudentBadge = ({ trapShown, trapHit }) => trapShown && !trapHit;
