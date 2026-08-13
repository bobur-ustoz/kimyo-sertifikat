import crypto from "crypto";

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });
  const { videoId } = req.body || {};
  if (!videoId) return res.status(400).json({ error: "Missing videoId" });

  const expires = Math.floor(Date.now() / 1000) + 3600;
  const token = crypto.createHash("sha256").update(`${process.env.BUNNY_TOKEN_KEY}${videoId}${expires}`).digest("hex");

  res.status(200).json({ token, expires, libraryId: process.env.BUNNY_LIBRARY_ID });
}
