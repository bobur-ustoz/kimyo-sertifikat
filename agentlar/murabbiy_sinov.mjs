// O'quvchi murabbiyining quruq sinovi: haqiqiy bazani FAQAT O'QIYDI, hech kimga xabar yubormaydi, hech narsa yozmaydi.
//   node agentlar/murabbiy_sinov.mjs               bugungi holat
//   node agentlar/murabbiy_sinov.mjs --yakshanba   yakshanba kuni nima ketishini ko'rish
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { collectMurabbiy } from "../api/_murabbiy.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
let now = new Date();
if (process.argv.includes("--yakshanba")) while (new Date(now.getTime() + 5 * 3600e3).getUTCDay() !== 0) now = new Date(now.getTime() + 86400e3);
const r = await collectMurabbiy(db, { now });
console.log(`Pullik faol o'quvchi: ${r.length} ta (${now.toISOString().slice(0, 10)})\n`);
for (const x of r) {
  const h = x.holat;
  console.log(`${String(x.student.full_name || "Noma'lum").split(/\s+/)[0]} (${x.student.plan}): faolsiz ${h.faolsiz ?? "hali boshlamagan"} kun, hafta ${h.hafta.video} video / ${h.hafta.savol} savol, reja ${h.rejaKun ?? "muddatsiz"} kun, qiyin mavzu ${h.zaif.length} ta`);
  console.log(x.xabar ? `  ${x.sabab ? `YUBORILMAYDI (${x.sabab})` : "YUBORILADI"} [${x.xabar.tur}]: ${x.xabar.text.replace(/\n+/g, " ")}` : "  xabar kerak emas");
}
