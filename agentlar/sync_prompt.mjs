// agentlar/sotuv.md ni api/_sotuv_bilim.js ga aylantiradi (Vercel fayl tizimidan .md o'qimaydi).
// Ishga tushirish: node agentlar/sync_prompt.mjs
// "Sinov uchun bo'sh joy" bo'limi ichki eslatma, botga berilmaydi.
import { readFileSync, writeFileSync } from "fs";

const md = readFileSync(new URL("./sotuv.md", import.meta.url), "utf8");
const text = md.split(/^## Sinov uchun bo'sh joy/m)[0].trim();
const out = `// AVTOMATIK YARATILGAN: agentlar/sync_prompt.mjs (manba: agentlar/sotuv.md). Qo'lda tahrir qilmang.
export const SOTUV_BILIM = ${JSON.stringify(text)};
`;
writeFileSync(new URL("../api/_sotuv_bilim.js", import.meta.url), out);
console.log(`api/_sotuv_bilim.js yozildi (${text.length} belgi)`);
