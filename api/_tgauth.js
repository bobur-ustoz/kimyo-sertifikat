// Telegram orqali ro'yxatdan o'tish / kirish: server tomoni. Alohida funksiya emas (Vercel Hobby'da funksiya soni
// chegaralangan), api/purchase-request.js ichidan chaqiriladi: { action: "tg-login-start" | "tg-login-poll" } (kirishsiz).
//
//   tg-login-start { secret } -> { code, url }: botga ochiladigan havola; sir faqat shu brauzerda qoladi
//   tg-login-poll  { code, secret } -> { status: "pending" | "expired" | "ok", token_hash? }
//   tg-login-finish { token } -> { status: "expired" | "ok", token_hash? }: botdagi "Saytga kirish" tugmasi (asl oyna yo'qolganda ham ishlaydi)
//
// Bot tomoni (telefon ulashish, hisob yaratish) api/_sotuv.js da. Kirish tokeni bir marta beriladi va brauzer uni
// supabase.auth.verifyOtp({ token_hash, type: "magiclink" }) bilan sessiyaga aylantiradi.

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";
import { botUsername, newCode } from "./_tglink.js";

const LOGIN_MINUTES = 10;
const MAX_PENDING = 500;     // kirishsiz endpoint: ortiqcha qatorlar yig'ilib ketmasin
export const loginLink = (code) => `https://t.me/${botUsername()}?start=kirish_${code}`;
export const hashSecret = (s) => crypto.createHash("sha256").update(String(s)).digest("hex");

// Telegram orqali ochilgan hisobning email'i: haqiqiy pochta emas (example.com ga xat hech qachon bormaydi).
export const tgEmail = (tgId) => `tg${tgId}@example.com`;
export const isTgEmail = (email) => /^tg\d+@example\.com$/.test(String(email || ""));

// "Saytga kirish" havolasi: bot kirishni tasdiqlagach shu tugmani beradi. Havolani Telegram ichki brauzerida ochgan odamning
// asl oynasi (sir saqlangan joy) yo'qolgan bo'lishi mumkin, shuning uchun sirsiz, lekin imzolangan va bir martalik token.
const FINISH_MINUTES = 15;
const signFinish = (s) => crypto.createHmac("sha256", process.env.SUPABASE_SERVICE_ROLE_KEY || "x").update(s).digest("hex").slice(0, 32);
export const finishToken = (code, now = Date.now()) => { const exp = now + FINISH_MINUTES * 60e3; return `${code}.${exp}.${signFinish(`${code}.${exp}`)}`; };
export function parseFinishToken(t, now = Date.now()) {
  const m = /^([A-Za-z0-9_-]{8,64})\.(\d{10,16})\.([0-9a-f]{32})$/.exec(String(t || ""));
  if (!m || Number(m[2]) < now) return null;
  return sameHash(m[3], signFinish(`${m[1]}.${m[2]}`)) ? m[1] : null;
}
export const finishLink = (site, code) => `${site}/?kirish=${finishToken(code)}`;

const sameHash = (a, b) => {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
};

export async function handleTgLogin(req, res) {
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return res.status(503).json({ error: "Hali sozlanmagan" });
  const admin = createClient(process.env.VITE_SUPABASE_URL, serviceKey, { auth: { persistSession: false } });
  const { action, secret, token } = req.body || {};
  let { code } = req.body || {};
  const goodSecret = typeof secret === "string" && secret.length >= 16 && secret.length <= 128;

  if (action === "tg-login-start") {
    if (!goodSecret) return res.status(400).json({ error: "Noto'g'ri so'rov" });
    await admin.from("tg_logins").delete().lt("expires_at", new Date().toISOString());
    const { count } = await admin.from("tg_logins").select("code", { count: "exact", head: true });
    if ((count || 0) > MAX_PENDING) return res.status(429).json({ error: "Hozir band, birozdan so'ng urinib ko'ring." });
    const c = newCode();
    const { error } = await admin.from("tg_logins").insert({ code: c, secret_hash: hashSecret(secret), expires_at: new Date(Date.now() + LOGIN_MINUTES * 60e3).toISOString() });
    if (error) return res.status(500).json({ error: "Havola yaratilmadi. Birozdan so'ng urinib ko'ring." });
    return res.status(200).json({ code: c, url: loginLink(c), minutes: LOGIN_MINUTES });
  }

  // tg-login-finish: botdagi "Saytga kirish" tugmasi (sirsiz, imzolangan havola)
  if (action === "tg-login-finish") {
    code = parseFinishToken(token);
    if (!code) return res.status(200).json({ status: "expired" });
    const { data: row } = await admin.from("tg_logins").select("*").eq("code", code).maybeSingle();
    if (!row || !row.user_id || row.consumed) return res.status(200).json({ status: "expired" });
    return issueToken(admin, res, row);
  }

  // tg-login-poll
  if (!goodSecret || typeof code !== "string" || !/^[A-Za-z0-9_-]{8,64}$/.test(code)) return res.status(400).json({ error: "Noto'g'ri so'rov" });
  const { data: row } = await admin.from("tg_logins").select("*").eq("code", code).maybeSingle();
  if (!row || !sameHash(row.secret_hash, hashSecret(secret)) || row.consumed || new Date(row.expires_at) < new Date()) {
    return res.status(200).json({ status: "expired" });
  }
  if (!row.user_id) return res.status(200).json({ status: "pending" });
  return issueToken(admin, res, row);
}

async function issueToken(admin, res, row) {
  const code = row.code;
  // Token bir marta: kim birinchi "consumed" qila olsa, o oladi.
  const { data: won } = await admin.from("tg_logins").update({ consumed: true }).eq("code", code).eq("consumed", false).select("user_id").maybeSingle();
  if (!won) return res.status(200).json({ status: "expired" });
  const { data: u, error: uErr } = await admin.auth.admin.getUserById(row.user_id);
  if (uErr || !u?.user?.email) { console.error("tg-login: user not found:", uErr?.message); return res.status(500).json({ error: "Hisob topilmadi" }); }
  const { data: link, error: lErr } = await admin.auth.admin.generateLink({ type: "magiclink", email: u.user.email });
  const tokenHash = link?.properties?.hashed_token;
  if (lErr || !tokenHash) { console.error("tg-login: generateLink failed:", lErr?.message); return res.status(500).json({ error: "Kirish tokeni yaratilmadi" }); }
  return res.status(200).json({ status: "ok", token_hash: tokenHash });
}
