import { createClient } from "@supabase/supabase-js";

export const config = { maxDuration: 60 };

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  // Only signed-in users may spend the Claude budget.
  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Tizimga kiring" });
  const anon = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
  const { data: who, error: whoErr } = await anon.auth.getUser(jwt);
  if (whoErr || !who?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
  const { prompt, maxTokens } = req.body || {};
  if (!prompt || typeof prompt !== "string") return res.status(400).json({ error: "Missing prompt" });

  try {
    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-5",
        max_tokens: Math.min(Number(maxTokens) || 1000, 2000),
        messages: [{ role: "user", content: prompt }],
      }),
    });
    const data = await r.json();
    if (!r.ok) return res.status(r.status).json({ error: data.error?.message || "Anthropic API error" });
    const textBlock = (data.content || []).find((b) => b.type === "text");
    res.status(200).json({ text: textBlock?.text || "" });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
}
