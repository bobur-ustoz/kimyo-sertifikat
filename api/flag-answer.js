import { createClient } from "@supabase/supabase-js";

// A student reports an AI answer as wrong. The answer stops being served from the
// cache immediately and shows up as "flagged" for a reviewer. Answers a reviewer
// already approved cannot be flagged this way.
export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const url = process.env.VITE_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return res.status(503).json({ error: "Hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Tizimga kiring" });
  const anon = createClient(url, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Sessiya yaroqsiz. Qayta kiring." });

  const { questionId } = req.body || {};
  if (!questionId || typeof questionId !== "string") return res.status(400).json({ error: "questionId kerak" });

  const admin = createClient(url, serviceKey);
  const { error } = await admin.from("video_questions")
    .update({ status: "flagged" })
    .eq("id", questionId).eq("status", "auto");
  if (error) return res.status(500).json({ error: error.message });
  res.status(200).json({ ok: true });
}
