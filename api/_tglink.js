// "Telegramni ulash": saytdagi profil tugmasi uchun server tomoni. Alohida funksiya emas (Vercel Hobby'da funksiya
// soni chegaralangan), api/purchase-request.js ichidan chaqiriladi: { action: "tg-link" | "tg-status" }.
//
//   tg-link   -> bir martalik kod yaratadi va botga ochiladigan havolani qaytaradi (kod 15 daqiqa amal qiladi)
//   tg-status -> { linked, remind }: hisob Telegramga ulanganmi va eslatmalar yoqilganmi

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";

const CODE_MINUTES = 15;
export const botUsername = () => process.env.SOTUV_BOT_USERNAME || "Boburkimyoyordamchi_bot";
// 12 belgi, faqat A-Z a-z 0-9 _ - (Telegram /start parametri shularga ruxsat beradi).
export const newCode = () => crypto.randomBytes(9).toString("base64url");
export const deepLink = (code) => `https://t.me/${botUsername()}?start=ulash_${code}`;

export async function handleTgLink(req, res) {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return res.status(503).json({ error: "Hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Avval hisobingizga kiring" });
  const anon = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: who, error: whoErr } = await anon.auth.getUser(jwt);
  if (whoErr || !who?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
  const userId = who.user.id;

  const admin = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });

  if (req.body?.action === "tg-status") {
    const { data } = await admin.from("sotuv_leads").select("remind").eq("linked_user_id", userId).maybeSingle();
    return res.status(200).json({ linked: !!data, remind: !!data?.remind });
  }

  // Eski ishlatilmagan kodlar o'chiriladi: bir vaqtda faqat bitta amal qiluvchi kod.
  await admin.from("tg_link_codes").delete().eq("user_id", userId).eq("used", false);
  const code = newCode();
  const { error } = await admin.from("tg_link_codes").insert({ code, user_id: userId, expires_at: new Date(Date.now() + CODE_MINUTES * 60e3).toISOString() });
  if (error) return res.status(500).json({ error: "Kod yaratilmadi. Birozdan so'ng urinib ko'ring." });
  return res.status(200).json({ url: deepLink(code), minutes: CODE_MINUTES });
}
