// Removes a video from the Bunny library. Replacing a question's video used to
// leave the old one behind, billed for and invisible; nothing in the codebase
// ever deleted one.
//
// Admin-only, same check as the upload authorisation: the Bunny API key stays
// on the server and is never handed to the browser.

import { createClient } from "@supabase/supabase-js";

const SUPABASE_URL = process.env.VITE_SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.VITE_SUPABASE_ANON_KEY;

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const { videoId } = req.body || {};
  if (!videoId) return res.status(400).json({ error: "Missing videoId" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Not authenticated" });

  const anon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Invalid session" });

  const asUser = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    global: { headers: { Authorization: `Bearer ${jwt}` } },
  });
  const { data: profile } = await asUser.from("profiles").select("is_admin").eq("id", userData.user.id).maybeSingle();
  if (!profile?.is_admin) return res.status(403).json({ error: "Admin only" });

  // Refuse to delete a video a question still points at, so a mistaken call
  // cannot blank out working content.
  const { data: inUse } = await anon.from("questions").select("id").eq("bunny_video_id", videoId).limit(1).maybeSingle();
  if (inUse) return res.status(409).json({ error: "Bu video hali savolga bog'langan" });

  const r = await fetch(`https://video.bunnycdn.com/library/${process.env.BUNNY_LIBRARY_ID}/videos/${videoId}`, {
    method: "DELETE",
    headers: { AccessKey: process.env.BUNNY_API_KEY },
  });
  if (!r.ok && r.status !== 404) {
    const body = await r.text();
    return res.status(502).json({ error: `Bunny o'chira olmadi: ${body.slice(0, 200)}` });
  }

  res.status(200).json({ ok: true });
}
