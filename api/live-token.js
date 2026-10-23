import { createClient } from "@supabase/supabase-js";

const DAILY = "https://api.daily.co/v1";

async function daily(path, key, body) {
  const r = await fetch(DAILY + path, {
    method: body ? "POST" : "GET",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await r.json().catch(() => ({}));
  return { ok: r.ok, status: r.status, data };
}

// Gives the caller a way into a live lesson's video room. The admin (host) starts the lesson
// and gets an owner token; students get a plain token, and only once the lesson is live and
// their plan (or the lesson's "for everyone" flag) allows it.
export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const url = process.env.VITE_SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const dailyKey = process.env.DAILY_API_KEY;
  if (!serviceKey || !dailyKey) return res.status(503).json({ error: "Jonli dars hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Tizimga kiring" });
  const anon = createClient(url, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: userData, error: userErr } = await anon.auth.getUser(jwt);
  if (userErr || !userData?.user) return res.status(401).json({ error: "Sessiya yaroqsiz" });
  const user = userData.user;

  const { lessonId } = req.body || {};
  if (!lessonId) return res.status(400).json({ error: "lessonId kerak" });

  const admin = createClient(url, serviceKey);
  const [{ data: lesson }, { data: profile }] = await Promise.all([
    admin.from("live_lessons").select("*").eq("id", lessonId).maybeSingle(),
    admin.from("profiles").select("is_admin, plan, full_name, email").eq("id", user.id).maybeSingle(),
  ]);
  if (!lesson) return res.status(404).json({ error: "Dars topilmadi" });

  const isHost = !!profile?.is_admin;
  if (!isHost) {
    if (lesson.status !== "live") return res.status(403).json({ error: lesson.status === "ended" ? "Dars tugagan" : "Dars hali boshlanmadi" });
    if (!lesson.for_all && (profile?.plan || "free") === "free") return res.status(403).json({ error: "Jonli darslar Standart obunachilar uchun" });
  }

  // The room is created the first time the host opens the lesson.
  let roomName = lesson.room_name;
  if (!roomName) {
    if (!isHost) return res.status(403).json({ error: "Dars hali boshlanmadi" });
    roomName = `noor-${lesson.id.slice(0, 8)}`;
    const exp = Math.floor(new Date(lesson.starts_at).getTime() / 1000) + (lesson.duration_min + 240) * 60;
    const made = await daily("/rooms", dailyKey, {
      name: roomName, privacy: "private",
      properties: { exp, enable_chat: true, enable_screenshare: true, enable_prejoin_ui: true, enable_knocking: false, lang: "en" },
    });
    if (!made.ok && made.status !== 400) return res.status(502).json({ error: made.data?.info || "Xona yaratilmadi" });
    await admin.from("live_lessons").update({ room_name: roomName }).eq("id", lesson.id);
  }
  if (isHost && lesson.status !== "live") await admin.from("live_lessons").update({ status: "live" }).eq("id", lesson.id);

  const name = profile?.full_name || (profile?.email || user.email || "O'quvchi").split("@")[0];
  const exp = Math.floor(Date.now() / 1000) + (lesson.duration_min + 240) * 60;
  const tok = await daily("/meeting-tokens", dailyKey, {
    properties: { room_name: roomName, is_owner: isHost, user_name: isHost ? `${name} (ustoz)` : name, exp, enable_screenshare: isHost },
  });
  if (!tok.ok) return res.status(502).json({ error: tok.data?.info || "Token olinmadi" });

  const dom = await daily("/", dailyKey);
  const domain = dom.data?.domain_name;
  if (!domain) return res.status(502).json({ error: "Daily hisobi topilmadi" });
  res.status(200).json({ url: `https://${domain}.daily.co/${roomName}?t=${tok.data.token}`, host: isHost });
}
