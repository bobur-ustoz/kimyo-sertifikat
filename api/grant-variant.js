// Server-side unlock endpoint: marks a variant purchase as paid.
//
// This is the single plug point for automated payments. A Click or Payme
// adapter (once merchant credentials exist) verifies the provider's own
// signature and then POSTs here; until then the admin panel does the same job
// by hand. It is deliberately not reachable from the browser: it needs both a
// shared secret and the Supabase service-role key, neither of which ships to
// the client.
//
// Required Vercel env vars (endpoint returns 503 until all are set):
//   PAYMENT_WEBHOOK_SECRET     - long random string, sent as x-payment-secret
//   SUPABASE_SERVICE_ROLE_KEY  - Supabase service_role key (bypasses RLS)
//
// POST body: { studentId, variantId, amount, provider, providerTxnId }

import { createClient } from "@supabase/supabase-js";
import crypto from "crypto";

const PROVIDERS = ["manual", "click", "payme"];

const timingSafeEqual = (a, b) => {
  const bufA = Buffer.from(String(a));
  const bufB = Buffer.from(String(b));
  if (bufA.length !== bufB.length) return false;
  return crypto.timingSafeEqual(bufA, bufB);
};

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const secret = process.env.PAYMENT_WEBHOOK_SECRET;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
  const supabaseUrl = process.env.VITE_SUPABASE_URL;
  if (!secret || !serviceKey || !supabaseUrl) return res.status(503).json({ error: "Payment endpoint not configured" });

  if (!timingSafeEqual(req.headers["x-payment-secret"] || "", secret)) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const { studentId, variantId, amount, provider = "click", providerTxnId } = req.body || {};
  if (!studentId || !variantId) return res.status(400).json({ error: "Missing studentId or variantId" });
  if (!PROVIDERS.includes(provider)) return res.status(400).json({ error: "Unknown provider" });

  const admin = createClient(supabaseUrl, serviceKey, { auth: { persistSession: false } });

  const { data: variant } = await admin.from("variants").select("price").eq("id", variantId).maybeSingle();
  if (!variant) return res.status(404).json({ error: "Variant not found" });
  if (amount != null && Number(amount) < variant.price) {
    return res.status(400).json({ error: "Amount below variant price" });
  }

  const { error } = await admin.from("variant_purchases").upsert(
    {
      student_id: studentId,
      variant_id: variantId,
      amount: amount != null ? Number(amount) : variant.price,
      status: "paid",
      provider,
      provider_txn_id: providerTxnId || null,
      paid_at: new Date().toISOString(),
    },
    { onConflict: "student_id,variant_id" }
  );
  if (error) return res.status(500).json({ error: error.message });

  res.status(200).json({ ok: true });
}
