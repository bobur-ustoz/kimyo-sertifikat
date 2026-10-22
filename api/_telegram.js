// Shared Telegram helpers for the purchase confirmation flow. The leading
// underscore keeps Vercel from exposing this file as an endpoint.
//
// Vercel env vars (server only, never VITE_-prefixed):
//   TELEGRAM_BOT_TOKEN       - from @BotFather
//   TELEGRAM_ADMIN_CHAT_ID   - chat that receives the requests
//   TELEGRAM_ADMIN_IDS       - optional, comma separated Telegram user ids that may
//                              press the buttons; defaults to TELEGRAM_ADMIN_CHAT_ID
//   TELEGRAM_WEBHOOK_SECRET  - random string, also passed to setWebhook as secret_token

export const escapeHtml = (s) =>
  String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export const telegramConfigured = () =>
  !!(process.env.TELEGRAM_BOT_TOKEN && process.env.TELEGRAM_ADMIN_CHAT_ID);

export const adminIds = () =>
  (process.env.TELEGRAM_ADMIN_IDS || process.env.TELEGRAM_ADMIN_CHAT_ID || "")
    .split(",").map((s) => s.trim()).filter(Boolean);

// Calls a Bot API method. Never throws: callers treat Telegram as best effort
// and use the returned { ok } to decide what to tell the student.
export async function tg(method, payload, { form } = {}) {
  const token = process.env.TELEGRAM_BOT_TOKEN;
  if (!token) return { ok: false, description: "bot token missing" };
  try {
    const r = await fetch(`https://api.telegram.org/bot${token}/${method}`, form
      ? { method: "POST", body: form }
      : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
    const json = await r.json().catch(() => ({}));
    if (!json.ok) console.error(`telegram ${method} failed:`, String(json.description || r.status).slice(0, 300));
    return json;
  } catch (e) {
    console.error(`telegram ${method} threw:`, e.message);
    return { ok: false, description: e.message };
  }
}

export const fmtTime = (d = new Date()) =>
  d.toLocaleString("uz-UZ", { timeZone: "Asia/Tashkent", hour12: false });
