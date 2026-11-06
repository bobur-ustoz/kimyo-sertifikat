// Nazorat hisobotini HECH NARSA YUBORMASDAN ko'rsatadi (bazadan faqat o'qiydi).
// Ishga tushirish: node agentlar/nazorat_sinov.mjs   (loyihaning .env faylidan kalitlarni oladi)
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { collect, formatReport } from "../api/_nazorat.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const flags = await collect(db);
console.log(formatReport(flags)?.replace(/<\/?b>/g, "") || "Bugun bog'lanish kerak bo'lgan o'quvchi yo'q.");
