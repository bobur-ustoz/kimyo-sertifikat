// Receives the admin's button presses from Telegram and settles purchase requests.
//
//   [✅ Tasdiqlash]  -> status 'paid'      (the variant opens for the student)
//   [❌ Rad etish]   -> status 'rejected'  (the bot then asks for an optional reason;
//                                           replying to that message stores it)
//
// Trust model: Telegram signs every call with the secret_token we gave setWebhook,
// and only the Telegram ids listed in TELEGRAM_ADMIN_IDS (default: the admin chat
// id) are obeyed -- anyone else pressing a button or replying is ignored. Updates
// are guarded by "status = 'pending'", so pressing twice, or racing the /admin
// panel, can never unlock a variant twice or flip a settled request.
//
// Vercel env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_CHAT_ID, TELEGRAM_WEBHOOK_SECRET,
// SUPABASE_SERVICE_ROLE_KEY (and optionally TELEGRAM_ADMIN_IDS). See README.
//
// Telegram retries any non-200 reply, so this answers 200 even when it ignores an update.

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";
import { adminIds, escapeHtml, tg, fmtTime } from "./_telegram.js";

const SUPABASE_URL = process.env.VITE_SUPABASE_URL;
const REASON_PROMPT = "Rad etish sababini shu xabarga reply qilib yozing (ixtiyoriy).";

const sameSecret = (a, b) => {
  const x = Buffer.from(String(a));
  const y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
};

const who = (u) => u?.username ? `@${u.username}` : [u?.first_name, u?.last_name].filter(Boolean).join(" ") || String(u?.id);

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const secret = process.env.TELEGRAM_WEBHOOK_SECRET;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!secret || !serviceKey || !process.env.TELEGRAM_BOT_TOKEN) return res.status(503).json({ error: "Not configured" });
  if (!sameSecret(req.headers["x-telegram-bot-api-secret-token"] || "", secret)) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const update = req.body || {};
  const admin = createClient(SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const allowed = adminIds();

  try {
    if (update.callback_query) await onButton(update.callback_query, admin, allowed);
    else if (update.message?.reply_to_message) await onReply(update.message, admin, allowed);
  } catch (e) {
    console.error("telegram-webhook error:", e.message);
  }
  res.status(200).json({ ok: true });
}

async function onButton(cb, admin, allowed) {
  if (!allowed.includes(String(cb.from?.id))) return;      // not an admin: ignore silently

  const m = /^pay:(ok|no):([0-9a-f-]{36})$/.exec(cb.data || "");
  if (!m) return tg("answerCallbackQuery", { callback_query_id: cb.id });
  const [, action, id] = m;
  const approve = action === "ok";

  const now = new Date();
  const { data: row } = await admin.from("variant_purchases")
    .update({
      status: approve ? "paid" : "rejected",
      paid_at: approve ? now.toISOString() : null,
      reviewed_by: who(cb.from), reviewed_at: now.toISOString(), provider: "manual",
    })
    .eq("id", id).eq("status", "pending")
    .select("id").maybeSingle();

  if (!row) {
    return tg("answerCallbackQuery", { callback_query_id: cb.id, text: "Bu so'rov allaqachon ko'rib chiqilgan", show_alert: true });
  }

  const msg = cb.message;
  const verdict = `\n\n${approve ? "✅ Tasdiqlandi" : "❌ Rad etildi"} (${escapeHtml(who(cb.from))}, ${fmtTime(now)})`;
  const base = escapeHtml(msg?.caption || msg?.text || "");
  const edit = { chat_id: msg.chat.id, message_id: msg.message_id, parse_mode: "HTML", reply_markup: { inline_keyboard: [] } };
  // Re-send the original text (HTML-escaped) plus the verdict; the buttons are removed.
  if (msg?.photo) await tg("editMessageCaption", { ...edit, caption: base + verdict });
  else await tg("editMessageText", { ...edit, text: base + verdict });

  await tg("answerCallbackQuery", { callback_query_id: cb.id, text: approve ? "Tasdiqlandi" : "Rad etildi" });

  if (!approve) {
    await tg("sendMessage", {
      chat_id: msg.chat.id,
      text: `${REASON_PROMPT}\nID: ${id}`,
      reply_markup: { force_reply: true, input_field_placeholder: "Sabab (ixtiyoriy)" },
    });
  }
}

// The admin's reply to the "reason" prompt: store it on the rejected request.
async function onReply(message, admin, allowed) {
  if (!allowed.includes(String(message.from?.id))) return;
  const prompt = message.reply_to_message;
  if (!prompt?.text?.startsWith(REASON_PROMPT) || !message.text) return;

  const id = /ID: ([0-9a-f-]{36})/.exec(prompt.text)?.[1];
  if (!id) return;

  const { data: row } = await admin.from("variant_purchases")
    .update({ reject_reason: message.text.slice(0, 300) })
    .eq("id", id).eq("status", "rejected").select("id").maybeSingle();

  await tg("sendMessage", {
    chat_id: message.chat.id, reply_to_message_id: message.message_id,
    text: row ? "Sabab saqlandi, o'quvchi uni saytda ko'radi." : "Bu so'rov endi rad etilgan holatda emas.",
  });
}
