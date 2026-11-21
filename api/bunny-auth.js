import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";
import { ofisMalumot } from "./_ofis.js";
import { adminAmal } from "./_vazifa.js";

const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const authHeader = req.headers.authorization || "";
  const jwt = authHeader.replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Not authenticated" });

  const { data: userData, error: userErr } = await supabase.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Invalid session" });

  const supabaseAsUser = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY, {
    global: { headers: { Authorization: `Bearer ${jwt}` } },
  });
  const { data: profile } = await supabaseAsUser.from("profiles").select("is_admin").eq("id", userData.user.id).single();
  if (!profile?.is_admin) return res.status(403).json({ error: "Admin only" });

  // { vazifa: { amal, ... } }: homework and exams (what can be assigned, assign, results). Merged here for the same
  // reason as the office: this function already checks that the caller is an admin.
  if (req.body?.vazifa) {
    if (!process.env.SUPABASE_SERVICE_ROLE_KEY) return res.status(503).json({ error: "Server sozlanmagan" });
    const admin = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
    res.setHeader("Cache-Control", "no-store");
    try { const r = await adminAmal(admin, userData.user.id, req.body.vazifa); return res.status(r.status).json(r.body); }
    catch (e) { console.error("vazifa admin failed:", e.message); return res.status(500).json({ error: /does not exist|schema cache/.test(e.message) ? "Vazifalar jadvali hali yaratilmagan (SQL ishga tushirilmagan)" : "Xatolik yuz berdi" }); }
  }

  // { ofis: true } returns the AI office data (agents and their queue entries) for the admin panel.
  // Merged here for the same reason as delete: this function already checks that the caller is an admin.
  if (req.body?.ofis) {
    if (!process.env.SUPABASE_SERVICE_ROLE_KEY) return res.status(503).json({ error: "Server sozlanmagan" });
    const admin = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
    res.setHeader("Cache-Control", "no-store");
    return res.status(200).json(await ofisMalumot(admin));
  }

  // { videoId, delete: true } removes a video (merged here to stay under the Hobby plan's
  // serverless function limit). Refuses to delete one a question still points at.
  if (req.body?.delete && req.body?.videoId) {
    const { videoId } = req.body;
    const { data: inUse } = await supabase.from("questions").select("id").eq("bunny_video_id", videoId).limit(1).maybeSingle();
    if (inUse) return res.status(409).json({ error: "Bu video hali savolga bog'langan" });
    const r = await fetch(`https://video.bunnycdn.com/library/${process.env.BUNNY_LIBRARY_ID}/videos/${videoId}`, {
      method: "DELETE", headers: { AccessKey: process.env.BUNNY_API_KEY },
    });
    if (!r.ok && r.status !== 404) return res.status(502).json({ error: `Bunny o'chira olmadi: ${(await r.text()).slice(0, 200)}` });
    return res.status(200).json({ ok: true });
  }

  const { title } = req.body || {};
  if (!title) return res.status(400).json({ error: "Missing title" });

  const libraryId = process.env.BUNNY_LIBRARY_ID;
  const apiKey = process.env.BUNNY_API_KEY;

  const createRes = await fetch(`https://video.bunnycdn.com/library/${libraryId}/videos`, {
    method: "POST",
    headers: { AccessKey: apiKey, "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  const created = await createRes.json();
  if (!createRes.ok || !created.guid) return res.status(500).json({ error: created.Message || "Failed to create video" });

  // Six hours: a 500 MB video on a slow line can take longer than one, and the
  // signature only authorises an upload to this one freshly created video id.
  const expires = Math.floor(Date.now() / 1000) + 6 * 3600;
  const signature = crypto.createHash("sha256").update(`${libraryId}${apiKey}${expires}${created.guid}`).digest("hex");

  res.status(200).json({
    videoId: created.guid,
    libraryId,
    authorizationSignature: signature,
    authorizationExpire: expires,
  });
}
