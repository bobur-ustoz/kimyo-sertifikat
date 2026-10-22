// Tells a signed-in student which card to pay to. The card lives in server env so
// it is not hard-coded in the repo or shipped in the browser bundle, and is only
// shown to logged-in users.
//
// Vercel env vars: PAYMENT_CARD_NUMBER, PAYMENT_CARD_HOLDER

import { createClient } from "@supabase/supabase-js";

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const card = process.env.PAYMENT_CARD_NUMBER;
  const holder = process.env.PAYMENT_CARD_HOLDER;
  if (!card) return res.status(503).json({ error: "To'lov rekvizitlari hali sozlanmagan" });

  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Avval hisobingizga kiring" });
  const anon = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
  const { data, error } = await anon.auth.getUser(jwt);
  if (error || !data?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });

  res.status(200).json({ card, holder: holder || "" });
}
