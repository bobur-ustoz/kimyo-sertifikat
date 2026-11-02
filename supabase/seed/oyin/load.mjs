// Kunlik savol faylini (v2) bazaga yuklaydi. SQL editorga nusxalash o'rniga to'g'ridan-to'g'ri yuklaydi:
// maxsus belgilar (pastki indekslar) buzilmaydi.
//
//   node supabase/seed/oyin/load.mjs supabase/seed/oyin/kun_01.json
//
// Avval check.mjs dan o'tkazing. Kerak: .env da VITE_SUPABASE_URL va SUPABASE_SERVICE_ROLE_KEY,
// migratsiya 20261104000000_oyin_game.sql bajarilgan bo'lishi kerak. Qayta yuklash xavfsiz (upsert).
import { readFileSync } from "fs";
import { loadDay } from "../../../api/_oyin/content.js";

const file = process.argv[2];
if (!file) { console.error("Usage: node load.mjs <kun_NN.json>"); process.exit(1); }
const env = Object.fromEntries(readFileSync(new URL("../../../.env", import.meta.url), "utf8").split("\n").filter((l) => l.includes("=")).map((l) => [l.slice(0, l.indexOf("=")), l.slice(l.indexOf("=") + 1).trim()]));
const U = env.VITE_SUPABASE_URL, K = env.SUPABASE_SERVICE_ROLE_KEY;
if (!U || !K) { console.error(".env da VITE_SUPABASE_URL va SUPABASE_SERVICE_ROLE_KEY kerak"); process.exit(1); }
const H = { apikey: K, Authorization: `Bearer ${K}`, "Content-Type": "application/json; charset=utf-8", Prefer: "resolution=merge-duplicates,return=minimal" };

const day = loadDay(JSON.parse(readFileSync(file, "utf8")));
const rows = day.slots.flatMap((s) => s.variants.map((v) => {
  const pub = { p: v.p, ...(v.mol ? { mol: v.mol } : {}), ...(v.chain ? { chain: v.chain } : {}) };
  const sec = v.type === "choice" ? { ok: v.ok, no: v.no } : v.type === "write" ? { re: v.re, pr: v.pr, ans: v.ans } : { build: v.build };
  return { id: v.id, day: day.day, slot: s.slot, variant: Number(v.id.split("-").pop()), grp: s.group, type: s.type, lvl: s.lvl,
    bundle: v.bundle || null, bundle_group: s.bundleGroup, public: pub, secret: sec, explanation: v.w, trap: v.trap || null, uses: v.uses, active: true };
}));

const post = async (path, body) => {
  const r = await fetch(`${U}/rest/v1/${path}`, { method: "POST", headers: H, body: JSON.stringify(body) });
  if (!r.ok) throw new Error(`${path}: ${r.status} ${await r.text()}`);
};
await post("og_days?on_conflict=day", [{ day: day.day, topic: day.topic, substances: day.substances }]);
await post("og_questions?on_conflict=id", rows);
console.log(`${day.day}-kun (${day.topic}): ${rows.length} variant yuklandi`);
