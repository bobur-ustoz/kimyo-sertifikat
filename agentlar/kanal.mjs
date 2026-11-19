// Kanal postlari navbati (t.me/KimyogarBobur). Post yuborishni server bajaradi (har kuni 20:00, kuniga bitta);
// bu buyruqlar faqat navbatni boshqaradi.
//
//   node agentlar/kanal.mjs qosh <YYYY-MM-DD> <matn-fayl> [--rasm https://...] [--imzosiz]   -> qoralama
//   node agentlar/kanal.mjs royxat [--hammasi]
//   node agentlar/kanal.mjs korsat <id>            kanalga chiqadigan to'liq matn (imzo bilan)
//   node agentlar/kanal.mjs tasdiqla <id>          FAQAT ustoz "tasdiqlayman" degandan keyin
//   node agentlar/kanal.mjs kun <id> <YYYY-MM-DD>  reja kunini o'zgartirish
//   node agentlar/kanal.mjs bekor <id>
//   node agentlar/kanal.mjs qayta <id>             "xato" bo'lgan postni yana qoralamaga qaytarish
//
// Matn Telegram HTML'da: <b>qalin</b>, <i>kursiv</i>, <a href="https://...">havola</a>. "<" va "&" belgilari &lt; va &amp;.
import { readFileSync } from "fs";
import { createClient } from "@supabase/supabase-js";
import { tekshir, toliqMatn, tashkentKun, JADVAL } from "../api/_kanal.js";

const env = Object.fromEntries(readFileSync(new URL("../.env", import.meta.url), "utf8").split("\n")
  .map((l) => l.match(/^([A-Z0-9_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim().replace(/^["']|["']$/g, "")]));
if (!env.VITE_SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY) { console.error(".env da VITE_SUPABASE_URL va SUPABASE_SERVICE_ROLE_KEY kerak"); process.exit(2); }
const db = createClient(env.VITE_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });

const BOOL = new Set(["imzosiz", "hammasi"]);
const args = [], opt = {};
for (let i = 2; i < process.argv.length; i++) {
  const a = process.argv[i];
  if (!a.startsWith("--")) { args.push(a); continue; }
  const k = a.slice(2);
  opt[k] = BOOL.has(k) ? true : process.argv[++i];
}
const [cmd, ...rest] = args;
const fail = (m) => { console.error(m); process.exit(1); };
const must = ({ data, error }) => {
  if (error) fail(/kanal_postlar/.test(error.message) ? "kanal_postlar jadvali topilmadi: avval supabase/migrations/20261119000000_kanal_postlar.sql ni Supabase SQL Editor'da ishga tushiring." : `Xato: ${error.message}`);
  return data;
};
const bitta = async (id) => must(await db.from(JADVAL).select("*").eq("id", Number(id)).maybeSingle()) || fail(`Post topilmadi: ${id}`);
const birQator = (p) => `#${p.id}  ${p.reja_kuni}  ${p.holat.padEnd(13)} ${p.rasm_url ? "[rasm] " : ""}${p.matn.replace(/<[^>]+>/g, "").replace(/\s+/g, " ").slice(0, 70)}`;
// Holatni faqat kutilgan holatdan o'zgartiradi (masalan yuborilgan postni bekor qilib bo'lmaydi).
const otkaz = async (id, dan, patch) => {
  const r = must(await db.from(JADVAL).update(patch).eq("id", Number(id)).in("holat", dan).select("id"));
  if (!r.length) { const p = await bitta(id); fail(`#${id} hozir "${p.holat}" holatida, bu amal faqat ${dan.map((h) => `"${h}"`).join(" yoki ")} uchun.`); }
};

if (cmd === "qosh") {
  const [reja_kuni, fayl] = rest;
  if (!reja_kuni || !fayl) fail("Kerak: qosh <YYYY-MM-DD> <matn-fayl>");
  let matn;
  try { matn = readFileSync(fayl, "utf8").trim(); } catch { fail(`Faylni o'qib bo'lmadi: ${fayl}`); }
  const post = { matn, rasm_url: opt.rasm || null, imzo: !opt.imzosiz, reja_kuni };
  const xatolar = tekshir(post);
  if (xatolar.length) fail(`Post qo'shilmadi:\n- ${xatolar.join("\n- ")}`);
  if (reja_kuni < tashkentKun()) console.error(`Eslatma: ${reja_kuni} o'tib ketgan, tasdiqlansa eng yaqin kechki navbatda chiqadi.`);
  const [r] = must(await db.from(JADVAL).insert(post).select("id"));
  console.log(`Qoralama qo'shildi: #${r.id} (${reja_kuni}). Ustoz tasdiqlagach: node agentlar/kanal.mjs tasdiqla ${r.id}`);
} else if (cmd === "royxat") {
  let q = db.from(JADVAL).select("*").order("reja_kuni").order("id").limit(100);
  if (!opt.hammasi) q = q.in("holat", ["qoralama", "tasdiqlangan", "yuborilmoqda", "xato"]);
  const rows = must(await q);
  console.log(rows.length ? rows.map(birQator).join("\n") : "Navbat bo'sh.");
} else if (cmd === "korsat") {
  const p = await bitta(rest[0]);
  console.log(`#${p.id}  reja: ${p.reja_kuni}  holat: ${p.holat}${p.rasm_url ? `\nrasm: ${p.rasm_url}` : ""}${p.xato ? `\nxato: ${p.xato}` : ""}\n${"-".repeat(40)}\n${toliqMatn(p)}`);
} else if (cmd === "tasdiqla") {
  const p = await bitta(rest[0]);
  const xatolar = tekshir(p);
  if (xatolar.length) fail(`Tasdiqlanmadi, post yaroqsiz:\n- ${xatolar.join("\n- ")}`);
  await otkaz(p.id, ["qoralama"], { holat: "tasdiqlangan" });
  console.log(`#${p.id} tasdiqlandi. ${p.reja_kuni <= tashkentKun() ? "Eng yaqin" : p.reja_kuni + " kungi"} kechki navbatda (20:00) kanalga chiqadi.`);
} else if (cmd === "kun") {
  const [id, reja_kuni] = rest;
  if (!/^\d{4}-\d{2}-\d{2}$/.test(reja_kuni || "") || Number.isNaN(Date.parse(reja_kuni))) fail("Sana YYYY-MM-DD ko'rinishida bo'lsin.");
  await otkaz(id, ["qoralama", "tasdiqlangan"], { reja_kuni });
  console.log(`#${id} reja kuni: ${reja_kuni}`);
} else if (cmd === "bekor") {
  await otkaz(rest[0], ["qoralama", "tasdiqlangan", "xato"], { holat: "bekor" });
  console.log(`#${rest[0]} bekor qilindi.`);
} else if (cmd === "qayta") {
  await otkaz(rest[0], ["xato", "yuborilmoqda"], { holat: "qoralama", xato: null, sent_at: null });
  console.log(`#${rest[0]} qoralamaga qaytdi. Tekshirib, qayta tasdiqlang.`);
} else {
  fail("Buyruq: qosh | royxat | korsat | tasdiqla | kun | bekor | qayta. To'liq yo'riqnoma shu fayl boshida.");
}
