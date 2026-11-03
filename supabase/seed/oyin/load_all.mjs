// Barcha tayyor kunlarni (tayyor/kun_01..24.json) bazaga yuklaydi, eski 1-kunning ortiqcha variantlarini o'chirib qo'ymasdan faolsizlantiradi
// va yangi mavsum ochadi (1-kun bugun). Qayta yuklash xavfsiz (upsert).
//   node supabase/seed/oyin/load_all.mjs [--season] 
import { readFileSync } from "fs";
import { loadDay } from "../../../api/_oyin/content.js";

const env = Object.fromEntries(readFileSync(new URL("../../../.env", import.meta.url), "utf8").split("\n").filter((l) => l.includes("=")).map((l) => [l.slice(0, l.indexOf("=")), l.slice(l.indexOf("=") + 1).trim()]));
const U = env.VITE_SUPABASE_URL, K = env.SUPABASE_SERVICE_ROLE_KEY;
const H = { apikey: K, Authorization: `Bearer ${K}`, "Content-Type": "application/json; charset=utf-8", Prefer: "resolution=merge-duplicates,return=minimal" };
const call = async (method, path, body) => {
  const r = await fetch(`${U}/rest/v1/${path}`, { method, headers: H, body: body ? JSON.stringify(body) : undefined });
  if (!r.ok) throw new Error(`${method} ${path}: ${r.status} ${await r.text()}`);
};

let total = 0;
for (let n = 1; n <= 24; n++) {
  const file = new URL(`./tayyor/kun_${String(n).padStart(2, "0")}.json`, import.meta.url);
  const day = loadDay(JSON.parse(readFileSync(file, "utf8")));
  const rows = day.slots.flatMap((s) => s.variants.map((v) => {
    const pub = { p: v.p, ...(v.mol ? { mol: v.mol } : {}), ...(v.chain ? { chain: v.chain } : {}) };
    const sec = v.type === "choice" ? { ok: v.ok, no: v.no } : v.type === "write" ? { re: v.re, pr: v.pr, ans: v.ans } : { build: v.build };
    return { id: v.id, day: day.day, slot: s.slot, variant: Number(v.id.split("-").pop()), grp: s.group, type: s.type, lvl: s.lvl,
      bundle: v.bundle || null, bundle_group: s.bundleGroup, public: pub, secret: sec, explanation: v.w, trap: v.trap || null, uses: v.uses, active: true };
  }));
  await call("POST", "og_days?on_conflict=day", [{ day: day.day, topic: day.topic, substances: day.substances }]);
  await call("POST", "og_questions?on_conflict=id", rows);
  // shu kunning yangi faylda yo'q eski variantlari tanlanmasin (qator o'chirilmaydi: eski javoblar unga bog'langan)
  const keep = rows.map((r) => r.id).join(",");
  await call("PATCH", `og_questions?day=eq.${day.day}&id=not.in.(${keep})`, { active: false });
  total += rows.length;
  console.log(`${day.day}-kun (${day.topic}): ${rows.length} variant`);
}
console.log("Jami", total);
