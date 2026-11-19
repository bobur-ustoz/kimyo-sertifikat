// Saytdagi xatolar: o'quvchi brauzerida chiqqan xato (avtomatik) va o'quvchining o'zi yozgan xabari umumiy navbatga
// "kod agentiga" deb tushadi. Ustoz qarori 2026-11-19: sayt buzilsa buni kimdir aytishi kerak.
// Alohida funksiya emas (Vercel Hobby'da funksiya soni chegaralangan): api/purchase-request.js ichidan chaqiriladi.
//
//   { action: "xato", xabar, sahifa, stack?, qurilma }   kirishsiz ham qabul qilinadi (xato kirishdan oldin ham chiqadi)
//   { action: "xato-xabar", matn, sahifa }               faqat kirgan o'quvchidan
//
// Suiiste'moldan himoya: bir xil xato kuniga BITTA yozuv (takrori sanab boriladi), kuniga ko'pi bilan KUN_MAX xil xato,
// matnlar qisqartiriladi, sahifa manzilidan so'rov qismi (?...) olib tashlanadi. Avtomatik xatoda o'quvchi kimligi yozilmaydi:
// faqat tasodifiy qurilma belgisi (nechta qurilmada takrorlanganini sanash uchun).

import crypto from "crypto";
import { createClient } from "@supabase/supabase-js";
import { yoz, JADVAL as NAVBAT } from "./_navbat.js";
import { escapeHtml, telegramConfigured, tg } from "./_telegram.js";

export const KUN_MAX = 30;          // kuniga ko'pi bilan shuncha XIL xato yoziladi
export const SONI_MAX = 200;        // bitta xatoning takrori shundan oshsa sanash to'xtaydi
export const QURILMA_MAX = 20;      // sanaladigan qurilmalar soni chegarasi
export const OGOH_QURILMA = 3;      // shuncha qurilmada takrorlansa ustozga darhol xabar
export const XABAR_KUN_MAX = 3;     // bir o'quvchi kuniga shuncha xabar yoza oladi
const qisqa = (s, n) => String(s ?? "").replace(/\s+/g, " ").trim().slice(0, n);
export const tashkentKun = (d = new Date()) => new Date(d.getTime() + 5 * 3600e3).toISOString().slice(0, 10);

// Sayt aybi bo'lmagan shovqin: brauzer kengaytmalari, internet uzilishi, begona skriptlar.
const SHOVQIN = /^script error\.?$|resizeobserver loop|failed to fetch|load failed|networkerror|network request failed|the operation was aborted|aborterror|extension:\/\/|the user aborted|cancell?ed/i;

// Manzildan faqat yo'l va # qismi (so'rov parametrlarida kod yoki token bo'lishi mumkin).
export function sahifaYol(s) {
  try { const u = new URL(String(s || ""), "https://x"); return qisqa(u.pathname + u.hash.split("?")[0], 120); } catch { return ""; }
}

// Kelgan xatoni tozalaydi. Yaroqsiz yoki shovqin bo'lsa null.
export function tayyorla(body = {}) {
  const xabar = qisqa(body.xabar, 300);
  if (xabar.length < 3 || SHOVQIN.test(xabar)) return null;
  const stack = String(body.stack ?? "").slice(0, 800);
  if (/extension:\/\//.test(stack)) return null;
  const qurilma = /^[a-z0-9]{6,24}$/i.test(String(body.qurilma || "")) ? String(body.qurilma) : null;
  return { xabar, sahifa: sahifaYol(body.sahifa), stack, qurilma };
}

// Bir xil xato (matn + sahifa) uchun kunlik barqaror kalit. Matndagi sonlar almashtiriladi: "id 123" va "id 456" bitta xato.
export function kalit(sana, x) {
  const h = crypto.createHash("sha1").update(`${x.xabar.replace(/\d+/g, "N")}|${x.sahifa.replace(/[0-9a-f-]{8,}/gi, "ID")}`).digest("hex").slice(0, 12);
  return `sayt-xato:${sana}:${h}`;
}

// Takror kelgan xatoni mavjud yozuvga qo'shadi. -> { tafsilot, ogoh }: ogoh = aynan hozir OGOH_QURILMA ga yetdi.
export function qosh(tafsilot = {}, qurilma) {
  const t = { ...tafsilot, soni: (tafsilot.soni || 1) + 1 }, q = [...(tafsilot.qurilmalar || [])];
  let ogoh = false;
  if (qurilma && !q.includes(qurilma) && q.length < QURILMA_MAX) { q.push(qurilma); ogoh = q.length === OGOH_QURILMA; }
  return { tafsilot: { ...t, qurilmalar: q }, ogoh };
}

const admin = () => createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const ustozga = async (text) => {
  if (!telegramConfigured?.() || !process.env.TELEGRAM_ADMIN_CHAT_ID) return;
  try { await tg("sendMessage", { chat_id: process.env.TELEGRAM_ADMIN_CHAT_ID, text, parse_mode: "HTML", disable_web_page_preview: true }); } catch { /* xabar ketmasa ham yozuv navbatda */ }
};

// Avtomatik xato. db va ogohlantir sinov uchun almashtiriladi. Har doim { ok: true } (o'quvchi brauzeriga tafsilot qaytarilmaydi).
export async function xatoYoz(db, body, { now = new Date(), ogohlantir = ustozga, brauzer = "" } = {}) {
  const x = tayyorla(body);
  if (!x) return { ok: true, sabab: "shovqin" };
  const sana = tashkentKun(now), k = kalit(sana, x);
  const { data: bor } = await db.from(NAVBAT).select("id,tafsilot").eq("kalit", k).maybeSingle();
  if (bor) {
    if ((bor.tafsilot?.soni || 1) >= SONI_MAX) return { ok: true, sabab: "chegara" };
    const { tafsilot, ogoh } = qosh(bor.tafsilot, x.qurilma);
    await db.from(NAVBAT).update({ tafsilot }).eq("id", bor.id);
    if (ogoh) await ogohlantir(`⚠️ <b>Saytda xato ${OGOH_QURILMA} ta qurilmada takrorlandi</b>\n${escapeHtml(x.xabar)}\nSahifa: ${escapeHtml(x.sahifa || "noma'lum")}\n\nKod agentiga "navbatni ko'r" deng.`);
    return { ok: true, takror: true, ogoh };
  }
  const kunBoshi = new Date(`${sana}T00:00:00+05:00`).toISOString();
  const { count } = await db.from(NAVBAT).select("id", { count: "exact", head: true }).eq("agent", "sayt").eq("tur", "xato").gte("created_at", kunBoshi);
  if ((count || 0) >= KUN_MAX) return { ok: true, sabab: "kunlik chegara" };
  await yoz(db, { agent: "sayt", tur: "xato", sarlavha: `Saytda xato: ${x.xabar.slice(0, 140)}${x.sahifa ? ` (${x.sahifa})` : ""}`,
    tafsilot: { xabar: x.xabar, sahifa: x.sahifa, stack: x.stack, brauzer: qisqa(brauzer, 160), soni: 1, qurilmalar: x.qurilma ? [x.qurilma] : [] }, kimga: "kod", kalit: k });
  return { ok: true, yangi: true };
}

// O'quvchi yozgan xabar. -> { ok } | { error, status }
export async function xabarYoz(db, { matn, sahifa }, user, { now = new Date(), ogohlantir = ustozga, brauzer = "" } = {}) {
  const m = String(matn ?? "").trim().slice(0, 1000);
  if (m.length < 5) return { status: 400, error: "Nima bo'lganini qisqacha yozing" };
  const kunBoshi = new Date(`${tashkentKun(now)}T00:00:00+05:00`).toISOString();
  const { data: bugun } = await db.from(NAVBAT).select("tafsilot").eq("agent", "sayt").eq("tur", "savol").gte("created_at", kunBoshi).limit(500);
  if ((bugun || []).filter((r) => r.tafsilot?.student_id === user.id).length >= XABAR_KUN_MAX) return { status: 429, error: "Bugun yetarlicha xabar yubordingiz. Rahmat, ko'rib chiqamiz." };
  const r = await yoz(db, { agent: "sayt", tur: "savol", sarlavha: `O'quvchi xabari: ${qisqa(m, 100)}`, tafsilot: { matn: m, sahifa: sahifaYol(sahifa), student_id: user.id, brauzer: qisqa(brauzer, 160) }, kimga: "kod" });
  if (!r.ok) return { status: 500, error: "Xabar saqlanmadi. Keyinroq urinib ko'ring." };
  const { data: p } = await db.from("profiles").select("full_name").eq("id", user.id).maybeSingle();
  await ogohlantir(`🐞 <b>O'quvchi saytdagi muammo haqida yozdi</b>\n${escapeHtml(p?.full_name || "Ismsiz")}: ${escapeHtml(m)}\nSahifa: ${escapeHtml(sahifaYol(sahifa) || "noma'lum")}`);
  return { ok: true };
}

export async function handleXato(req, res) {
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) return res.status(200).json({ ok: true });
  const brauzer = req.headers["user-agent"] || "";
  try {
    if (req.body?.action === "xato") { await xatoYoz(admin(), req.body, { brauzer }); return res.status(200).json({ ok: true }); }
    const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
    if (!jwt) return res.status(401).json({ error: "Avval hisobingizga kiring" });
    const { data: who, error } = await createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY).auth.getUser(jwt);
    if (error || !who?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
    const r = await xabarYoz(admin(), req.body || {}, who.user, { brauzer });
    return r.ok ? res.status(200).json({ ok: true }) : res.status(r.status).json({ error: r.error });
  } catch (e) {
    console.error("xato qabul qilinmadi:", e.message);
    return res.status(200).json({ ok: true });      // xato haqidagi xabarning o'zi o'quvchiga xato ko'rsatmasin
  }
}
