// A free-plan Supabase project is paused after about a week without database
// activity, which takes the whole site down until someone notices and restores
// it by hand. One cheap read a day is enough to count as activity.
//
// Scheduled from vercel.json. It reuses the env vars the rest of the API
// already needs, so there is nothing extra to configure.

import { createClient } from "@supabase/supabase-js";

export default async function handler(req, res) {
  // Vercel signs its own cron calls; if a secret is configured, require it.
  const secret = process.env.CRON_SECRET;
  if (secret && req.headers.authorization !== `Bearer ${secret}` && !req.headers["x-vercel-cron"]) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const url = process.env.VITE_SUPABASE_URL;
  const key = process.env.VITE_SUPABASE_ANON_KEY;
  if (!url || !key) return res.status(503).json({ error: "Supabase env vars are not set" });

  const supabase = createClient(url, key, { auth: { persistSession: false } });

  // Cheapest read that still reaches Postgres: a count, no rows returned.
  const { count, error } = await supabase.from("teachers").select("id", { count: "exact", head: true });

  if (error) {
    console.error("keepalive failed:", error.message);
    return res.status(500).json({ ok: false, error: error.message });
  }
  res.status(200).json({ ok: true, teachers: count, at: new Date().toISOString() });
}
