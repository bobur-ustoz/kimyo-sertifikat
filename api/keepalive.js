// A free-plan Supabase project is paused after about a week without database
// activity, which takes the whole site down until someone notices and restores
// it by hand. One cheap read a day is enough to count as activity.
//
// Scheduled from vercel.json. It reuses the env vars the rest of the API
// already needs, so there is nothing extra to configure.

import { createClient } from "@supabase/supabase-js";
import { tg } from "./_telegram.js";
import { runNazorat } from "./_nazorat.js";
import { runYangilik } from "./_yangilik.js";
import { yoz } from "./_navbat.js";
import { runKanal, KANAL } from "./_kanal.js";
import { runTekshiruv, bunnyRoyxat } from "./_tekshiruv.js";
import { runCeo, yakshanbami } from "./_ceo.js";
import { runMurabbiy } from "./_murabbiy.js";

// Asia/Tashkent bo'yicha bugungi sana: navbatda kuniga bitta yozuv bo'lishi uchun kalit.
const bugun = () => new Date(Date.now() + 5 * 3600e3).toISOString().slice(0, 10);

// ?job=nazorat (second cron): the daily "who to contact" report for the teacher; it shares this
// function because the Hobby plan caps how many functions the project may have.
async function nazorat(res) {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const chat = process.env.TELEGRAM_ADMIN_CHAT_ID;
  if (!serviceKey || !chat || !process.env.TELEGRAM_BOT_TOKEN) return res.status(503).json({ error: "Nazorat sozlanmagan" });
  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  try {
    // Talabaga eslatma sotuv boti orqali (u Telegramni shu bot bilan ulagan); token bo'lmasa faqat hisobot yuboriladi.
    const botToken = process.env.SOTUV_BOT_TOKEN;
    const toStudent = botToken ? (chat_id, text) => tg("sendMessage", { chat_id, text }, { token: botToken }) : null;
    // Murabbiy nazoratchidan oldin: u shaxsiy xabar yuborgan o'quvchiga nazoratchining umumiy eslatmasi ketmaydi
    // (ikkalasi bitta "oxirgi xabar" vaqtiga qaraydi). Murabbiy buzilsa ham nazorat hisoboti ketadi.
    let murabbiy;
    if (toStudent) {
      try { murabbiy = await runMurabbiy(db, toStudent); }
      catch (e) {
        console.error("murabbiy failed:", e.message);
        murabbiy = { ok: false, error: e.message };
        await yoz(db, { agent: "murabbiy", tur: "xato", sarlavha: "O'quvchi murabbiyi ishlamadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod", kalit: `murabbiy-xato:${bugun()}` });
      }
    }
    const r = await runNazorat(db, (text) => tg("sendMessage", { chat_id: chat, text, parse_mode: "HTML", disable_web_page_preview: true }), new Date(), toStudent);
    await yoz(db, { agent: "nazoratchi", tur: "hisobot", sarlavha: `Kunlik tekshiruv: ${r.flagged} ta o'quvchi bilan bog'lanish kerak, ${r.nudged} tasiga eslatma yuborildi`, tafsilot: r, kalit: `nazorat:${bugun()}` });
    // Platforma kamchiliklari: alohida try, shunda u buzilsa ham o'quvchilar hisoboti ketgan bo'ladi.
    let tekshiruv;
    try {
      tekshiruv = await runTekshiruv(db, (text) => tg("sendMessage", { chat_id: chat, text, parse_mode: "HTML", disable_web_page_preview: true }), { bunny: await bunnyRoyxat() });
    } catch (e) {
      console.error("tekshiruv failed:", e.message);
      tekshiruv = { ok: false, error: e.message };
      await yoz(db, { agent: "nazoratchi", tur: "xato", sarlavha: "Platforma tekshiruvi ishlamadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod", kalit: `tekshiruv-xato:${bugun()}` });
    }
    return res.status(200).json({ ok: true, ...r, tekshiruv, murabbiy });
  } catch (e) {
    console.error("nazorat failed:", e.message);
    await yoz(db, { agent: "nazoratchi", tur: "xato", sarlavha: "Kunlik tekshiruv ishlamadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod" });
    return res.status(500).json({ ok: false, error: e.message });
  }
}

// CEO hisoboti: kun yakunida ustozning admin chatiga; yakshanba kuni qo'shimcha haftalik. Alohida kron emas:
// kechki "yangilik" kroni bilan birga ishlaydi, ?job=ceo (&hafta=1) bilan alohida ham chaqiriladi.
// Hech qachon xato otmaydi: hisobot chiqmasa ham kanal va yangilik ishi to'xtamaydi.
async function ceoIsh({ hafta = null } = {}) {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const chat = process.env.TELEGRAM_ADMIN_CHAT_ID;
  if (!serviceKey || !chat || !process.env.TELEGRAM_BOT_TOKEN) return { ok: false, error: "CEO sozlanmagan" };
  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const notify = async (text) => {
    const r = await tg("sendMessage", { chat_id: chat, text, parse_mode: "HTML", disable_web_page_preview: true });
    if (!r?.ok) throw new Error(`Telegram: ${String(r?.description || "yuborilmadi").slice(0, 200)}`);
  };
  try {
    const out = {};
    if (hafta !== true) out.kunlik = await runCeo(db, notify);
    if (hafta === true || (hafta === null && yakshanbami())) out.haftalik = await runCeo(db, notify, { hafta: true });
    return { ok: true, ...out };
  } catch (e) {
    console.error("ceo failed:", e.message);
    await yoz(db, { agent: "ceo", tur: "xato", sarlavha: "CEO hisoboti chiqmadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod" });
    return { ok: false, error: e.message };
  }
}

// ?job=yangilik (third cron): one digest a day to Premium students who linked Telegram.
// ?sinov=1 only returns the text that would be sent and records nothing.
async function yangilik(req, res) {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const botToken = process.env.SOTUV_BOT_TOKEN;
  if (!serviceKey || !botToken) return res.status(503).json({ error: "Yangilik sozlanmagan" });
  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const site = process.env.SITE_URL || "https://kimyo-sertifikat.vercel.app";
  try {
    const send = (chat_id, text, btn) => tg("sendMessage", { chat_id, text, parse_mode: "HTML", disable_web_page_preview: true, reply_markup: { inline_keyboard: [[btn]] } }, { token: botToken });
    const dryRun = !!req.query?.sinov;
    const kanal = dryRun ? undefined : await kanalIsh();
    const r = await runYangilik(db, send, site, { dryRun });
    if (!dryRun && r.items) await yoz(db, { agent: "yangilik", tur: "hisobot", sarlavha: `Yangiliklar xabari: ${r.sent} o'quvchiga yuborildi, ${r.failed} tasiga yetmadi`, tafsilot: { sent: r.sent, failed: r.failed, items: r.items }, kalit: `yangilik:${bugun()}` });
    // Kun yakuni hisoboti eng oxirida: bugungi kanal posti va yangilik xabari ham unga kiradi.
    const ceo = dryRun ? undefined : await ceoIsh();
    return res.status(200).json({ ok: true, ...r, kanal, ceo });
  } catch (e) {
    console.error("yangilik failed:", e.message);
    await yoz(db, { agent: "yangilik", tur: "xato", sarlavha: "Yangiliklar xabari ishlamadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod" });
    return res.status(500).json({ ok: false, error: e.message });
  }
}

// Kanal postchisi: kuniga ko'pi bilan bitta tasdiqlangan post, yordamchi bot orqali. Alohida kron emas
// (Hobby rejasida kronlar soni cheklangan): kechki "yangilik" kroni bilan birga ishlaydi, ?job=kanal bilan alohida ham chaqiriladi.
// Hech qachon xato otmaydi: kanal ishlamasa ham yangilik xabari ketaveradi.
async function kanalIsh() {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const botToken = process.env.SOTUV_BOT_TOKEN;
  if (!serviceKey || !botToken) return { ok: false, error: "Kanal sozlanmagan" };
  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  try {
    const r = await runKanal(db, (method, payload) => tg(method, payload, { token: botToken }), { chat: process.env.KANAL_CHAT_ID || KANAL });
    return { ok: true, ...r };
  } catch (e) {
    console.error("kanal failed:", e.message);
    await yoz(db, { agent: "kanal", tur: "xato", sarlavha: "Kanal postchisi ishlamadi", tafsilot: { xato: String(e.message).slice(0, 300) }, kimga: "kod" });
    return { ok: false, error: e.message };
  }
}

export default async function handler(req, res) {
  // Vercel signs its own cron calls; if a secret is configured, require it.
  const secret = process.env.CRON_SECRET;
  if (secret && req.headers.authorization !== `Bearer ${secret}` && !req.headers["x-vercel-cron"]) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  if (req.query?.job === "nazorat") return nazorat(res);
  if (req.query?.job === "yangilik") return yangilik(req, res);
  if (req.query?.job === "ceo") { const r = await ceoIsh({ hafta: req.query?.hafta ? true : false }); return res.status(r.ok ? 200 : 500).json(r); }
  if (req.query?.job === "kanal") { const r = await kanalIsh(); return res.status(r.ok ? 200 : 500).json(r); }

  const url = process.env.VITE_SUPABASE_URL;
  const key = process.env.VITE_SUPABASE_ANON_KEY;
  if (!url || !key) return res.status(503).json({ error: "Supabase env vars are not set" });

  const supabase = createClient(url, key, { auth: { persistSession: false } });

  // Cheapest read that still reaches Postgres: a count, no rows returned.
  const { count, error } = await supabase.from("teachers").select("id", { count: "exact", head: true });

  if (error) {
    console.error("keepalive failed:", error.message);
    return res.status(500).json({ ok: false, error: error.message });
  }
  res.status(200).json({ ok: true, teachers: count, at: new Date().toISOString() });
}
