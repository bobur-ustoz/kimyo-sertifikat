import { createClient } from "@supabase/supabase-js";

// Reviewer-approved questions for one video, ready to show as quick buttons.
// Only the question, answer and video position leave the server: never who asked.
export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const url = process.env.VITE_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceKey) return res.status(503).json({ error: "Hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Tizimga kiring" });
  const anon = createClient(url, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Sessiya yaroqsiz" });

  const { topicId, exampleId } = req.body || {};
  if (!topicId === !exampleId) return res.status(400).json({ error: "topicId yoki exampleId kerak" });

  const admin = createClient(url, serviceKey);
  const col = topicId ? "topic_id" : "example_id";
  const { data, error } = await admin.from("video_questions")
    .select("id,question,answer,video_seconds,hits")
    .eq(col, topicId || exampleId).eq("status", "approved")
    .order("hits", { ascending: false }).limit(200);
  if (error) return res.status(500).json({ error: error.message });
  res.status(200).json({ items: data || [] });
}
