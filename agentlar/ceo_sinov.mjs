// CEO hisobotining quruq sinovi: haqiqiy bazani FAQAT O'QIYDI, hech kimga yubormaydi, navbatga yozmaydi.
//   node agentlar/ceo_sinov.mjs            kunlik
//   node agentlar/ceo_sinov.mjs --hafta    haftalik
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { collectCeo, formatHisobot, tashkentKun } from "../api/_ceo.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const hafta = process.argv.includes("--hafta");
const h = await collectCeo(db, { kun: hafta ? 7 : 1 });
console.log(formatHisobot(h, { sana: tashkentKun() }).replace(/<[^>]+>/g, "").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&"));
