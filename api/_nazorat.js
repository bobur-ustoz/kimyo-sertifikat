// Nazorat hisoboti: har kuni ertalab ustozning admin chatiga "bugun kim bilan bog'lanish kerak" ro'yxati.
// Pullik o'quvchilar uchun: bir necha kundan beri hech narsa ochmagan yoki oxirgi javoblarida foiz past.
// Bu o'quvchiga hech narsa yubormaydi (ularning Telegram aloqasi hali yo'q), faqat ustozni ogohlantiradi.
//
// Ishga tushirish: vercel.json cron -> /api/keepalive?job=nazorat (funksiya soni cheklangani uchun
// keepalive.js ichidan chaqiriladi). Kerakli env: SUPABASE_SERVICE_ROLE_KEY, TELEGRAM_BOT_TOKEN,
// TELEGRAM_ADMIN_CHAT_ID (mavjud admin boti).

import { escapeHtml } from "./_telegram.js";

export const NO_ACTIVITY_DAYS = 3;   // shuncha kun va undan ko'p faolsiz bo'lsa
export const LOW_PERCENT = 40;       // oxirgi javoblarda shundan kam to'g'ri bo'lsa
export const MIN_ANSWERS = 20;       // foiz hisoblash uchun kamida shuncha javob
export const MAX_LINES = 15;         // bitta xabarda ko'pi bilan shuncha o'quvchi
const DAY = 86400e3;

const ms = (t) => (t ? new Date(t).getTime() : 0);
const displayName = (s) => s.full_name || String(s.email || "").split("@")[0] || "Noma'lum";

// students: pullik profillar; views: { student_id, last_at }; answers: { student_id, is_correct, at }.
// Har o'quvchi uchun sabablar ro'yxati (bo'sh bo'lsa bog'lanish shart emas).
export function findFlags({ students, views, answers, now = new Date() }) {
  const t = now.getTime();
  const flags = [];
  for (const s of students) {
    const mine = answers.filter((a) => a.student_id === s.id).sort((a, b) => ms(b.at) - ms(a.at));
    const times = [...views.filter((v) => v.student_id === s.id).map((v) => ms(v.last_at)), ...mine.map((a) => ms(a.at))].filter(Boolean);
    const reasons = [];

    if (times.length) {
      const days = Math.floor((t - Math.max(...times)) / DAY);
      if (days >= NO_ACTIVITY_DAYS) reasons.push(`${days} kundan beri video ochmagan va savol yechmagan`);
    } else {
      // To'lov paytini planning tugash sanasidan (30 kun) topamiz; bo'lmasa hisob ochilgan sanadan.
      const start = s.plan_expires_at ? ms(s.plan_expires_at) - 30 * DAY : ms(s.created_at);
      const days = Math.floor((t - start) / DAY);
      if (days >= NO_ACTIVITY_DAYS) reasons.push(`hali hech narsa ochmagan (${days} kun)`);
    }

    const last = mine.slice(0, MIN_ANSWERS);
    if (last.length >= MIN_ANSWERS) {
      const pct = Math.round((last.filter((a) => a.is_correct).length / last.length) * 100);
      if (pct < LOW_PERCENT) reasons.push(`oxirgi ${MIN_ANSWERS} javobning ${pct}% i to'g'ri`);
    }
    if (reasons.length) flags.push({ student: s, reasons });
  }
  return flags;
}

export function formatReport(flags) {
  if (!flags.length) return null;
  const lines = flags.slice(0, MAX_LINES).map(({ student: s, reasons }) =>
    `• <b>${escapeHtml(displayName(s))}</b> (${escapeHtml(s.email || "email yo'q")}): ${escapeHtml(reasons.join("; "))}`);
  const more = flags.length > MAX_LINES ? [`... va yana ${flags.length - MAX_LINES} ta`] : [];
  return [`🔔 <b>Bugun bog'lanish kerak (${flags.length} ta):</b>`, ...lines, ...more].join("\n");
}

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
// Ba'zi jadvallar (masalan adaptive_answers) hamma bazada qo'llanmagan bo'lishi mumkin: ularsiz ham hisobot chiqadi.
const optional = ({ data, error }) => { if (error) console.warn("nazorat: jadval o'tkazib yuborildi:", error.message); return error ? [] : data || []; };

// Bazadan o'quvchilarni yig'ib, bog'lanish kerak bo'lganlarni qaytaradi (hech narsa yubormaydi).
export async function collect(db, now = new Date()) {
  const profiles = must(await db.from("profiles").select("id, full_name, email, plan, plan_expires_at, created_at, is_admin").neq("plan", "free"));
  const students = profiles.filter((p) => !p.is_admin && (!p.plan_expires_at || new Date(p.plan_expires_at) > now));
  if (!students.length) return [];
  const ids = students.map((s) => s.id);
  const [views, regular, adaptive] = await Promise.all([
    db.from("video_views").select("student_id, last_at").in("student_id", ids).then(must),
    db.from("answers").select("student_id, is_correct, answered_at").in("student_id", ids).order("answered_at", { ascending: false }).limit(5000).then(must),
    db.from("adaptive_answers").select("student_id, is_correct, created_at").in("student_id", ids).order("created_at", { ascending: false }).limit(5000).then(optional),
  ]);
  const answers = [
    ...regular.map((a) => ({ student_id: a.student_id, is_correct: a.is_correct, at: a.answered_at })),
    ...adaptive.map((a) => ({ student_id: a.student_id, is_correct: a.is_correct, at: a.created_at })),
  ];
  return findFlags({ students, views, answers, now });
}

// Ro'yxat bo'sh bo'lsa hech narsa yubormaydi (ustozga bekorga xabar kelmasin).
export async function runNazorat(db, notify, now = new Date()) {
  const flags = await collect(db, now);
  const text = formatReport(flags);
  if (text) await notify(text);
  return { flagged: flags.length, sent: !!text };
}
