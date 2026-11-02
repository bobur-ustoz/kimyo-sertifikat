// Organika game bot: receives Telegram updates for the second bot (not the payment bot in
// telegram-webhook.js; one bot token can have only one webhook). All game logic is in _organika.js.
//
// Vercel env vars: ORGANIKA_BOT_TOKEN (from @BotFather), ORGANIKA_WEBHOOK_SECRET (random string,
// also passed to setWebhook as secret_token), SUPABASE_SERVICE_ROLE_KEY, VITE_SUPABASE_URL.
//
// Telegram retries any non-200 reply, so errors are logged and answered with 200.

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";
import { tg } from "./_telegram.js";
import { handleUpdate } from "./_organika.js";

const sameSecret = (a, b) => {
  const x = Buffer.from(String(a));
  const y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
};

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const token = process.env.ORGANIKA_BOT_TOKEN;
  const secret = process.env.ORGANIKA_WEBHOOK_SECRET;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!token || !secret || !serviceKey) return res.status(503).json({ error: "Not configured" });
  if (!sameSecret(req.headers["x-telegram-bot-api-secret-token"] || "", secret)) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const db = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const send = (method, payload) => tg(method, payload, { token });

  try {
    await handleUpdate(req.body || {}, db, send);
  } catch (e) {
    console.error("organika-webhook error:", e.message);
  }
  res.status(200).json({ ok: true });
}
