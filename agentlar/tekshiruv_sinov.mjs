// Platforma tekshiruvining quruq sinovi: haqiqiy bazani FAQAT O'QIYDI, navbatga yozmaydi, hech kimga xabar yubormaydi.
//   node agentlar/tekshiruv_sinov.mjs
// Bunny tekshiruvi uchun .env da BUNNY_LIBRARY_ID kerak (bo'lmasa o'tkazib yuboriladi).
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { collectTekshiruv, bunnyRoyxat, formatTekshiruv } from "../api/_tekshiruv.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const bunny = await bunnyRoyxat(fetch, env);
const k = await collectTekshiruv(db, { bunny });
console.log(`Bunny: ${bunny ? `${bunny.size} ta video tekshirildi` : "tekshirilmadi (BUNNY_LIBRARY_ID yoki kalit yo'q)"}\nTopildi: ${k.length} ta\n`);
for (const x of k) console.log(`[${x.kimga.padEnd(9)}] ${x.sarlavha}\n            kod: ${x.kod}`);
console.log("\n--- Ustozga boradigan xabar (hammasi yangi deb hisoblansa) ---\n" + (formatTekshiruv({ yangi: k, tuzaldi: [], ochiq: k.length, eski: [] }) || "(xabar yuborilmaydi)").replace(/<[^>]+>/g, ""));
