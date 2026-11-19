// Umumiy navbat bilan ishlash (kompyuterdagi agentlar uchun: montaj, instagram, platforma, kod ...).
//
//   node agentlar/navbat.mjs yoz <agent> <tur> "<sarlavha>" ['{"json":"tafsilot"}'] [--kimga kod] [--kalit k] [--holat jarayonda]
//   node agentlar/navbat.mjs oqi [--kun 1] [--kimga kod] [--agent montaj] [--tur xato] [--ochiq]
//   node agentlar/navbat.mjs holat <id> <yangi|jarayonda|bajarildi|bekor> ["izoh"]
//   node agentlar/navbat.mjs xulosa [--kun 1]
//
// tur: ish | xato | savol | hisobot. Kalitlar .env dan olinadi (VITE_SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY).
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { yoz, oqi, holatQoy, xulosa } from "../api/_navbat.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
if (!env.VITE_SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY) { console.error(".env da VITE_SUPABASE_URL va SUPABASE_SERVICE_ROLE_KEY kerak"); process.exit(2); }
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const BOOL = new Set(["ochiq"]);
const args = [], opt = {};
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i];
  if (!a.startsWith("--")) { args.push(a); continue; }
  const k = a.slice(2);
  opt[k] = BOOL.has(k) ? true : process.argv[++i];
}
const [cmd, ...rest] = args;
const vaqt = (t) => new Date(new Date(t).getTime() + 5 * 3600e3).toISOString().slice(5, 16).replace("T", " ");
const qator = (r) => `#${r.id}  ${vaqt(r.created_at)}  ${r.agent.padEnd(12)} ${r.tur.padEnd(8)} ${r.holat.padEnd(10)} ${r.kimga ? `-> ${r.kimga}  ` : ""}${r.sarlavha}`;
const fail = (m) => { console.error(m); process.exit(1); };
const xato = (e) => fail(/agent_navbat/.test(e?.message || "") ? "agent_navbat jadvali topilmadi: avval supabase/migrations/20261118000000_agent_navbat.sql ni Supabase SQL Editor'da ishga tushiring." : `Xato: ${e?.message || e}`);

try {
if (cmd === "yoz") {
  const [agent, tur, sarlavha, json] = rest;
  let tafsilot;
  if (json) { try { tafsilot = JSON.parse(json); } catch { fail("tafsilot JSON emas"); } }
  const r = await yoz(db, { agent, tur, sarlavha, tafsilot, kimga: opt.kimga, kalit: opt.kalit, holat: opt.holat });
  if (!r.ok) fail(`Yozilmadi: ${r.error}`);
  console.log(r.takror ? "Bu kalit bilan yozuv allaqachon bor, qaytadan yozilmadi." : `Yozildi: #${r.id}`);
} else if (cmd === "oqi") {
  const rows = await oqi(db, { kun: Number(opt.kun || 1), kimga: opt.kimga, agent: opt.agent, tur: opt.tur, ochiq: !!opt.ochiq });
  console.log(rows.length ? rows.map(qator).join("\n") : "Yozuv yo'q.");
} else if (cmd === "holat") {
  const [id, holat, izoh] = rest;
  const r = await holatQoy(db, Number(id), holat, izoh);
  if (!r.ok) fail(`O'zgarmadi: ${r.error}`);
  console.log(`#${id} -> ${holat}`);
} else if (cmd === "xulosa") {
  const x = xulosa(await oqi(db, { kun: Number(opt.kun || 1), limit: 1000 }));
  console.log(`Jami yozuv: ${x.jami}`);
  for (const [a, n] of Object.entries(x.agentlar)) console.log(`${a.padEnd(12)} ish ${n.ish}, xato ${n.xato}, savol ${n.savol}, hisobot ${n.hisobot}`);
  console.log(x.ochiq.length ? `\nOchiq (${x.ochiq.length}):\n${x.ochiq.map(qator).join("\n")}` : "\nOchiq xato va savol yo'q.");
} else {
  fail("Buyruq: yoz | oqi | holat | xulosa. To'liq yo'riqnoma shu fayl boshida.");
}
} catch (e) { xato(e); }
