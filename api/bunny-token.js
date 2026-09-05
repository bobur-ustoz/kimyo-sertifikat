import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";

const SUPABASE_URL = process.env.VITE_SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.VITE_SUPABASE_ANON_KEY;

const anon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const signToken = (videoId) => {
  const expires = Math.floor(Date.now() / 1000) + 3600;
  const token = crypto.createHash("sha256").update(`${process.env.BUNNY_TOKEN_KEY}${videoId}${expires}`).digest("hex");
  return { token, expires, libraryId: process.env.BUNNY_LIBRARY_ID };
};

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });
  const { videoId } = req.body || {};
  if (!videoId) return res.status(400).json({ error: "Missing videoId" });

  // Which variant does this video belong to? The client never gets to say.
  const { data: question, error } = await anon
    .from("questions")
    .select("variants(id, is_free, price, variant_number)")
    .eq("bunny_video_id", videoId)
    .limit(1)
    .maybeSingle();

  // 42703 = undefined_column: the paid-access migration has not been applied to
  // this database yet, so there is no paywall to enforce. Behave exactly like the
  // previous version until it lands, rather than locking every video out.
  if (error?.code === "42703") return res.status(200).json(signToken(videoId));

  const variant = question?.variants;
  if (!variant) return res.status(404).json({ error: "Video topilmadi" });

  if (variant.is_free) return res.status(200).json(signToken(videoId));

  const locked = { locked: true, price: variant.price, variantNumber: variant.variant_number };

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ ...locked, error: "Bu variant pullik. Avval hisobingizga kiring." });

  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ ...locked, error: "Sessiya eskirgan. Qayta kiring." });

  // Read as the user, so row-level security decides what they can see.
  const asUser = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    global: { headers: { Authorization: `Bearer ${jwt}` } },
  });
  const [{ data: profile }, { data: purchase }] = await Promise.all([
    asUser.from("profiles").select("is_admin").eq("id", userData.user.id).maybeSingle(),
    asUser.from("variant_purchases").select("status").eq("student_id", userData.user.id).eq("variant_id", variant.id).maybeSingle(),
  ]);

  // No plan grants a blanket unlock: every non-free variant needs its own paid
  // purchase row (the Premium "everything free" tier has been removed).
  const unlocked = profile?.is_admin || purchase?.status === "paid";
  if (!unlocked) return res.status(403).json({ ...locked, error: "Bu variant hali sotib olinmagan." });

  res.status(200).json(signToken(videoId));
}
