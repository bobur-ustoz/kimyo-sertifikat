// Telegram webhook for the two public bots (not the payment bot in telegram-webhook.js; one bot token
// can have only one webhook, and the Vercel Hobby plan caps the number of functions, so both share this file):
//   /api/organika-webhook              -> Organika game bot, logic in _organika.js
//   /api/organika-webhook?bot=sotuv    -> sales bot, logic in _sotuv.js
//
// Vercel env vars: ORGANIKA_BOT_TOKEN, ORGANIKA_WEBHOOK_SECRET (game bot);
// SOTUV_BOT_TOKEN, SOTUV_WEBHOOK_SECRET, ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN + TELEGRAM_ADMIN_CHAT_ID
// (sales bot; the teacher is notified through the existing admin bot);
// both: SUPABASE_SERVICE_ROLE_KEY, VITE_SUPABASE_URL. Each setWebhook passes its own secret_token.
//
// Telegram retries any non-200 reply, so errors are logged and answered with 200.

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";
import { tg } from "./_telegram.js";
import { handleUpdate } from "./_organika.js";
import { handleUpdate as handleSotuv, supabaseStore, askClaude } from "./_sotuv.js";

export const config = { maxDuration: 60 };   // the sales bot waits for a Claude reply

const sameSecret = (a, b) => {
  const x = Buffer.from(String(a));
  const y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
};

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const sotuv = req.query?.bot === "sotuv";
  const token = sotuv ? process.env.SOTUV_BOT_TOKEN : process.env.ORGANIKA_BOT_TOKEN;
  const secret = sotuv ? process.env.SOTUV_WEBHOOK_SECRET : process.env.ORGANIKA_WEBHOOK_SECRET;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!token || !secret || !serviceKey || (sotuv && !process.env.ANTHROPIC_API_KEY)) return res.status(503).json({ error: "Not configured" });
  if (!sameSecret(req.headers["x-telegram-bot-api-secret-token"] || "", secret)) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const send = (method, payload) => tg(method, payload, { token });

  try {
    if (sotuv) {
      // Heads-up goes to the teacher's admin chat through the payment bot's token.
      const notify = (text) => process.env.TELEGRAM_ADMIN_CHAT_ID
        ? tg("sendMessage", { chat_id: process.env.TELEGRAM_ADMIN_CHAT_ID, text, parse_mode: "HTML", disable_web_page_preview: true })
        : Promise.resolve();
      await handleSotuv(req.body || {}, { store: supabaseStore(db), send, ask: askClaude, notify });
    } else {
      await handleUpdate(req.body || {}, db, send);
    }
  } catch (e) {
    console.error(`${sotuv ? "sotuv" : "organika"}-webhook error:`, e.message);
  }
  res.status(200).json({ ok: true });
}
