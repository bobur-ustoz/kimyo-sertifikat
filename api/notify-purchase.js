// Tells the admin on Telegram that a student wants to buy a variant, so the
// request does not sit unseen in the panel until someone thinks to look.
//
// The browser cannot be trusted to say what happened, so this re-reads the
// request from the database as the caller and only sends what it finds there.
// Never fails the purchase: the student's request is already saved by the time
// this runs, and a missing bot token or a Telegram outage must not look like a
// failed purchase.
//
// Vercel env vars (endpoint is inert until both are set):
//   TELEGRAM_BOT_TOKEN       - from @BotFather
//   TELEGRAM_ADMIN_CHAT_ID   - the chat that should receive the messages

import { createClient } from "@supabase/supabase-js";

const SUPABASE_URL = process.env.VITE_SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.VITE_SUPABASE_ANON_KEY;

const escapeHtml = (s) =>
  String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const token = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_ADMIN_CHAT_ID;
  if (!token || !chatId) return res.status(200).json({ ok: false, reason: "not configured" });

  const { variantId } = req.body || {};
  if (!variantId) return res.status(400).json({ error: "Missing variantId" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Not authenticated" });

  const anon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Invalid session" });

  // Read the request back as the student: row-level security means they can
  // only ever surface their own, and only one that really exists.
  const asUser = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    global: { headers: { Authorization: `Bearer ${jwt}` } },
  });
  const { data: purchase } = await asUser
    .from("variant_purchases")
    .select("amount, contact, status, variants(variant_number, teachers(name))")
    .eq("student_id", userData.user.id)
    .eq("variant_id", variantId)
    .maybeSingle();

  if (!purchase || purchase.status !== "pending") {
    return res.status(200).json({ ok: false, reason: "no pending request" });
  }

  const text = [
    "🔔 <b>Yangi sotib olish so'rovi</b>",
    "",
    `👨‍🏫 ${escapeHtml(purchase.variants?.teachers?.name || "—")}`,
    `📘 ${escapeHtml(purchase.variants?.variant_number)}-variant`,
    `💰 ${Number(purchase.amount || 0).toLocaleString("ru-RU")} so'm`,
    `📞 ${escapeHtml(purchase.contact || "telefon qoldirilmagan")}`,
    `✉️ ${escapeHtml(userData.user.email || "—")}`,
    "",
    "To'lovni qabul qilgach admin panelda \"To'landi\" bosing.",
  ].join("\n");

  try {
    const r = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ chat_id: chatId, text, parse_mode: "HTML" }),
    });
    if (!r.ok) {
      const body = await r.text();
      console.error("telegram sendMessage failed:", body.slice(0, 300));
      return res.status(200).json({ ok: false, reason: "telegram rejected" });
    }
  } catch (e) {
    console.error("telegram sendMessage threw:", e.message);
    return res.status(200).json({ ok: false, reason: "telegram unreachable" });
  }

  res.status(200).json({ ok: true });
}
