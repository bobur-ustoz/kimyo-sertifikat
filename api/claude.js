export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });
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
        max_tokens: maxTokens || 1000,
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
