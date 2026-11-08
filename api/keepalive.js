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
    const r = await runNazorat(db, (text) => tg("sendMessage", { chat_id: chat, text, parse_mode: "HTML", disable_web_page_preview: true }), new Date(), toStudent);
    return res.status(200).json({ ok: true, ...r });
  } catch (e) {
    console.error("nazorat failed:", e.message);
    return res.status(500).json({ ok: false, error: e.message });
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
    const r = await runYangilik(db, send, site, { dryRun: !!req.query?.sinov });
    return res.status(200).json({ ok: true, ...r });
  } catch (e) {
    console.error("yangilik failed:", e.message);
    return res.status(500).json({ ok: false, error: e.message });
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
