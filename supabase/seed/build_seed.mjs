// organika_bob_NN.json (to'g'ri javob + 3 ta noto'g'ri) -> SQL seed.
// Variantlar tartibi har savol uchun qat'iy (deterministik) aralashtiriladi, shuning uchun
// skript qayta ishga tushsa ham SQL o'zgarmaydi.
//
//   node supabase/seed/build_seed.mjs supabase/seed/organika_bob_01.json > supabase/seed/organika_bob_01.sql
//
// SQL qayta ishga tushirilsa savollar ko'paymaydi: (chapter, text) bo'yicha yangilanadi.
import { readFileSync } from "fs";

const file = process.argv[2];
if (!file) { console.error("Usage: node build_seed.mjs <questions.json>"); process.exit(1); }
const items = JSON.parse(readFileSync(file, "utf8"));

const rng = (seed) => () => {                 // mulberry32
  seed |= 0; seed = (seed + 0x6d2b79f5) | 0;
  let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
};
const q = (s) => `'${String(s).replace(/'/g, "''")}'`;

const rows = items.map((it, n) => {
  if (!it.ok || it.no?.length !== 3) throw new Error(`#${n + 1}: 1 ta to'g'ri va 3 ta noto'g'ri javob kerak`);
  const rand = rng(n * 7919 + 17);
  const opts = [it.ok, ...it.no];
  for (let i = opts.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [opts[i], opts[j]] = [opts[j], opts[i]];
  }
  if (new Set(opts).size !== 4) throw new Error(`#${n + 1}: variantlar takrorlanmasin`);
  return `(${it.c}, ${q(it.p)}, ${it.d}, ${q(it.q)}, ${q(JSON.stringify(opts))}::jsonb, ${opts.indexOf(it.ok)}, ${q(it.why || "")})`;
});

console.log(`-- Avtomatik yaratilgan (build_seed.mjs). ${file} faylini tahrirlang, SQL ni qayta yarating.
insert into ob_questions (chapter, part, difficulty, text, options, correct, explanation) values
${rows.join(",\n")}
on conflict (chapter, text) do update set
  part = excluded.part, difficulty = excluded.difficulty, options = excluded.options,
  correct = excluded.correct, explanation = excluded.explanation;`);
