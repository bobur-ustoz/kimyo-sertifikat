import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";

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
