// Files a variant purchase request: the student has already uploaded a receipt to
// the private "payment-proofs" bucket; this validates it, records a pending
// request and posts it to the admin's Telegram chat with Approve / Reject buttons.
//
// Requests are created here and only here (service role), so the receipt cannot be
// skipped. A Telegram outage never loses the request: it is saved first and the
// admin can still confirm it in /admin -> To'lovlar.
//
// Vercel env vars: SUPABASE_SERVICE_ROLE_KEY, plus the Telegram ones in _telegram.js
// (without them the request is saved and simply not announced).
//
// POST body: { variantId | lessonId, contact, proofPath }  (lessonId = a live-lesson recording)

import { createClient } from "@supabase/supabase-js";
import { escapeHtml, telegramConfigured, tg, fmtTime } from "./_telegram.js";

const SUPABASE_URL = process.env.VITE_SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.VITE_SUPABASE_ANON_KEY;
const BUCKET = "payment-proofs";
const MAX_PENDING_PER_STUDENT = 5;
const MIME = { jpg: "image/jpeg", jpeg: "image/jpeg", png: "image/png", webp: "image/webp" };

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  // { action: "info" }: which card to pay to. Merged here because the Hobby plan caps the
  // number of serverless functions; the card is only shown to signed-in users.
  if (req.body?.action === "info") {
    const card = process.env.PAYMENT_CARD_NUMBER;
    if (!card) return res.status(503).json({ error: "To'lov rekvizitlari hali sozlanmagan" });
    const j = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
    if (!j) return res.status(401).json({ error: "Avval hisobingizga kiring" });
    const a = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    const { data: who, error: whoErr } = await a.auth.getUser(j);
    if (whoErr || !who?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
    return res.status(200).json({ card, holder: process.env.PAYMENT_CARD_HOLDER || "" });
  }

  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return res.status(503).json({ error: "To'lov hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Avval hisobingizga kiring" });
  const anon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
  const user = userData.user;

  const { variantId, lessonId, contact, proofPath } = req.body || {};
  const phone = typeof contact === "string" ? contact.trim().slice(0, 40) : "";
  const isLesson = !!lessonId;
  if (!isLesson && (!variantId || typeof variantId !== "string")) return res.status(400).json({ error: "Variant ko'rsatilmagan" });
  if (!phone) return res.status(400).json({ error: "Telefon raqamingizni kiriting" });

  // The receipt must sit in the student's own folder and be a plain image path.
  if (typeof proofPath !== "string" || !proofPath.startsWith(`${user.id}/`) || proofPath.includes("..")) {
    return res.status(400).json({ error: "Chek rasmi yuklanmagan" });
  }
  const ext = proofPath.split(".").pop().toLowerCase();
  if (!MIME[ext]) return res.status(400).json({ error: "Chek rasmi jpg, png yoki webp bo'lishi kerak" });

  const admin = createClient(SUPABASE_URL, serviceKey, { auth: { persistSession: false } });

  // Storage already enforced size and type on upload; this confirms the file exists.
  const fileName = proofPath.slice(user.id.length + 1);
  const { data: files } = await admin.storage.from(BUCKET).list(user.id, { search: fileName, limit: 5 });
  if (!files?.some((f) => f.name === fileName)) return res.status(400).json({ error: "Chek rasmi topilmadi. Qayta yuklang." });

  // What is being bought: a variant, or the recording of a live lesson.
  let target;   // { price, label, col, id }
  if (isLesson) {
    const { data: lesson } = await admin.from("live_lessons")
      .select("id, title, price, recording_video_id").eq("id", lessonId).maybeSingle();
    if (!lesson || !lesson.recording_video_id) return res.status(404).json({ error: "Dars yozuvi topilmadi" });
    if (!(lesson.price > 0)) return res.status(400).json({ error: "Bu yozuv bepul" });
    target = { price: lesson.price, label: `🎥 Dars yozuvi: ${escapeHtml(lesson.title)}`, col: "live_lesson_id", id: lesson.id };
  } else {
    const { data: variant } = await admin.from("variants")
      .select("id, variant_number, price, is_free, teachers(name)").eq("id", variantId).maybeSingle();
    if (!variant) return res.status(404).json({ error: "Variant topilmadi" });
    if (variant.is_free) return res.status(400).json({ error: "Bu variant bepul" });
    target = { price: variant.price, label: `📘 ${escapeHtml(variant.teachers?.name || "—")} · ${escapeHtml(variant.variant_number)}-variant`, col: "variant_id", id: variant.id };
  }

  const { data: existing } = await admin.from("variant_purchases")
    .select("id, status").eq("student_id", user.id).eq(target.col, target.id).maybeSingle();
  if (existing?.status === "paid") return res.status(409).json({ error: "Bu allaqachon ochilgan" });
  if (existing?.status === "pending") return res.status(409).json({ error: "So'rovingiz allaqachon yuborilgan va ko'rib chiqilmoqda" });

  const { count } = await admin.from("variant_purchases")
    .select("id", { count: "exact", head: true }).eq("student_id", user.id).eq("status", "pending");
  if ((count || 0) >= MAX_PENDING_PER_STUDENT) {
    return res.status(429).json({ error: "Ko'rib chiqilayotgan so'rovlaringiz ko'p. Avval ularning natijasini kuting." });
  }

  const fresh = {
    amount: target.price, status: "pending", provider: "manual", contact: phone, proof_path: proofPath,
    reject_reason: null, reviewed_by: null, reviewed_at: null, paid_at: null,
    tg_chat_id: null, tg_message_id: null, created_at: new Date().toISOString(),
  };

  // A rejected or cancelled request is reopened; a paid or pending one was refused above.
  const { data: saved, error: saveErr } = existing
    ? await admin.from("variant_purchases").update(fresh).eq("id", existing.id).in("status", ["rejected", "cancelled"]).select("id").maybeSingle()
    : await admin.from("variant_purchases").insert({ student_id: user.id, [target.col]: target.id, ...fresh }).select("id").maybeSingle();
  if (saveErr?.code === "23505") return res.status(409).json({ error: "So'rovingiz allaqachon yuborilgan" });
  if (saveErr || !saved) return res.status(500).json({ error: "So'rov saqlanmadi. Qayta urinib ko'ring." });

  let announced = false;
  if (telegramConfigured()) {
    const caption = [
      "🔔 <b>Yangi to'lov so'rovi</b>",
      "",
      `👤 ${escapeHtml(user.user_metadata?.full_name || user.email || "—")}`,
      `✉️ ${escapeHtml(user.email || "—")}`,
      `📞 ${escapeHtml(phone)}`,
      target.label,
      `💰 ${Number(target.price || 0).toLocaleString("ru-RU")} so'm`,
      `🕒 ${fmtTime()}`,
    ].join("\n");

    const { data: blob } = await admin.storage.from(BUCKET).download(proofPath);
    const form = new FormData();
    form.append("chat_id", process.env.TELEGRAM_ADMIN_CHAT_ID);
    form.append("caption", caption);
    form.append("parse_mode", "HTML");
    form.append("reply_markup", JSON.stringify({
      inline_keyboard: [[
        { text: "✅ Tasdiqlash", callback_data: `pay:ok:${saved.id}` },
        { text: "❌ Rad etish", callback_data: `pay:no:${saved.id}` },
      ]],
    }));
    if (blob) form.append("photo", new Blob([await blob.arrayBuffer()], { type: MIME[ext] }), `chek.${ext}`);

    // No receipt bytes (should not happen) -> still announce as text so the admin sees it.
    const sent = blob
      ? await tg("sendPhoto", null, { form })
      : await tg("sendMessage", { chat_id: process.env.TELEGRAM_ADMIN_CHAT_ID, text: caption, parse_mode: "HTML",
          reply_markup: JSON.parse(form.get("reply_markup")) });
    if (sent.ok) {
      announced = true;
      await admin.from("variant_purchases")
        .update({ tg_chat_id: sent.result.chat.id, tg_message_id: sent.result.message_id }).eq("id", saved.id);
    }
  }

  res.status(200).json({ ok: true, announced });
}
