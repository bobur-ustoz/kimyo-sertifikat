// Kanal postchisi: tasdiqlangan postlarni Telegram kanalga navbat bilan chiqaradi (kuniga ko'pi bilan bitta).
//
// Ishga tushirish: kechki kron /api/keepalive?job=yangilik (har kuni 20:00, Toshkent) shu ishni ham bajaradi;
// qo'lda: /api/keepalive?job=kanal. Kerakli env: SUPABASE_SERVICE_ROLE_KEY, SOTUV_BOT_TOKEN (yordamchi bot kanalga admin
// bo'lishi kerak: "Post yuborish" huquqi bilan), ixtiyoriy KANAL_CHAT_ID (standart: @KimyogarBobur).
//
// Postlar agentlar/kanal.mjs orqali qo'shiladi va tasdiqlanadi. Tasdiqlanmagan post hech qachon yuborilmaydi.

import { yoz } from "./_navbat.js";

export const KANAL = "@KimyogarBobur";
export const JADVAL = "kanal_postlar";
export const MATN_MAX = 4000, RASM_MATN_MAX = 1000;   // Telegram chegarasi: xabar 4096, rasm osti 1024 (imzo bilan birga)
const RUXSAT_TEGLAR = new Set(["b", "strong", "i", "em", "u", "s", "a", "code", "pre", "blockquote", "tg-spoiler"]);

// Har post oxiridagi blok: havolalar so'z ichiga yashirilgan. Bot havolasi kanaldan kelganlarni sanash uchun belgilangan.
export const IMZO = [
  `🤖 Savolingiz bo'lsa: <a href="https://t.me/Boburkimyoyordamchi_bot?start=kanal_post">Yordamchi bot</a>`,
  `📲 <a href="https://t.me/KimyogarBobur">Telegram</a> | <a href="https://instagram.com/kimyogarbobur">Instagram</a>`,
].join("\n");

export const tashkentKun = (d = new Date()) => new Date(d.getTime() + 5 * 3600e3).toISOString().slice(0, 10);

// So'rovnoma (Telegram quiz): o'quvchi javobni postning o'zida belgilaydi, to'g'ri javob va izoh darhol ko'rinadi.
// Post matni "#sorov" qatori bilan boshlansa so'rovnoma hisoblanadi (alohida ustun kerak emas):
//   #sorov
//   Olmani kesib qo'ysangiz, bir necha daqiqada qorayadi. Nega?
//   A) Olma suvi bug'lanib ketadi
//   B) Olmadagi moddalar kislorod bilan oksidlanadi *        <- yulduzcha: to'g'ri javob
//   C) Olmaga chang qo'nadi
//   izoh: Kesilganda hujayralar buziladi va ...               <- javobdan keyin ko'rinadigan qisqa tushuntirish
// Rasm (rasm_url) bo'lsa, avval rasm chiqadi, ostidan so'rovnoma.
export const SOROV_BELGI = "#sorov";
export const SAVOL_MAX = 300, VARIANT_MAX = 100, IZOH_MAX = 200;      // Telegram chegaralari
export const sorovmi = (matn) => String(matn ?? "").trimStart().toLowerCase().startsWith(SOROV_BELGI);
export function sorovAjrat(matn) {
  if (!sorovmi(matn)) return null;
  const qator = String(matn).trim().split("\n").slice(1).map((l) => l.trim()).filter(Boolean);
  const savol = [], variantlar = []; let togri = -1, izoh = "", yulduz = 0;
  for (const l of qator) {
    const v = l.match(/^[A-Ja-j]\)\s*(.+)$/), z = l.match(/^izoh\s*:\s*(.+)$/i);
    if (z) izoh = z[1].trim();
    else if (v) { let t = v[1].trim(); if (/\*\s*$/.test(t)) { t = t.replace(/\s*\*\s*$/, ""); togri = variantlar.length; yulduz++; } variantlar.push(t); }
    else if (!variantlar.length) savol.push(l);
  }
  return { savol: savol.join("\n"), variantlar, togri, yulduz, izoh };
}

// Yuboriladigan to'liq matn (imzo bilan).
export const toliqMatn = (post) => post.imzo === false ? post.matn.trim() : `${post.matn.trim()}\n\n${IMZO}`;

// Matndagi xatolar ro'yxati (bo'sh bo'lsa post yaroqli). Telegram noma'lum yoki yopilmagan tegli xabarni rad etadi,
// shuning uchun buni yuborishdan oldin, post qo'shilayotganda ushlaymiz.
export function tekshir({ matn, rasm_url, reja_kuni, imzo = true } = {}) {
  const x = [];
  const m = String(matn ?? "").trim();
  if (sorovmi(m)) {
    const s = sorovAjrat(m);
    if (!s.savol) x.push("so'rovnoma savoli yo'q");
    if (s.savol.length > SAVOL_MAX) x.push(`savol uzun: ${s.savol.length} belgi, chegara ${SAVOL_MAX}`);
    if (s.variantlar.length < 2 || s.variantlar.length > 10) x.push("so'rovnomada 2 tadan 10 tagacha javob bo'lsin");
    for (const v of s.variantlar) if (v.length > VARIANT_MAX) x.push(`javob uzun (${v.length} belgi, chegara ${VARIANT_MAX}): ${v.slice(0, 30)}...`);
    if (s.yulduz !== 1) x.push("to'g'ri javob bitta bo'lsin: uning oxiriga * qo'ying");
    if (s.izoh.length > IZOH_MAX) x.push(`izoh uzun: ${s.izoh.length} belgi, chegara ${IZOH_MAX}`);
    if (rasm_url && !/^https:\/\/\S+$/.test(rasm_url)) x.push("rasm_url https:// bilan boshlanishi kerak");
    if (!/^\d{4}-\d{2}-\d{2}$/.test(String(reja_kuni ?? "")) || Number.isNaN(Date.parse(reja_kuni))) x.push("reja_kuni YYYY-MM-DD ko'rinishida bo'lishi kerak");
    return x;
  }
  if (!m) x.push("matn bo'sh");
  const toliq = imzo === false ? m : `${m}\n\n${IMZO}`;
  const korinadigan = toliq.replace(/<[^>]+>/g, "");
  const chegara = rasm_url ? RASM_MATN_MAX : MATN_MAX;
  if (korinadigan.length > chegara) x.push(`matn uzun: ${korinadigan.length} belgi, chegara ${chegara}${rasm_url ? " (rasmli post)" : ""}`);
  const ochiq = [];
  for (const t of m.matchAll(/<\s*(\/?)\s*([a-zA-Z-]*)([^>]*)>/g)) {
    const [, yop, nom] = t, n = nom.toLowerCase();
    if (!RUXSAT_TEGLAR.has(n)) { x.push(`ruxsat etilmagan teg: ${t[0].slice(0, 30)} ("<" belgisi kerak bo'lsa &lt; deb yozing)`); continue; }
    if (!yop) ochiq.push(n);
    else if (ochiq.pop() !== n) x.push(`teg noto'g'ri yopilgan: </${n}>`);
  }
  if (ochiq.length) x.push(`yopilmagan teg: <${ochiq.join(">, <")}>`);
  if (/<a\b(?![^>]*\bhref="https?:\/\/[^"]+")[^>]*>/i.test(m)) x.push(`havola <a href="https://..."> ko'rinishida bo'lishi kerak`);
  if (/&(?!(amp|lt|gt|quot);)/.test(m)) x.push(`"&" belgisi &amp; deb yozilishi kerak`);
  if (rasm_url && !/^https:\/\/\S+$/.test(rasm_url)) x.push("rasm_url https:// bilan boshlanishi kerak");
  if (!/^\d{4}-\d{2}-\d{2}$/.test(String(reja_kuni ?? "")) || Number.isNaN(Date.parse(reja_kuni))) x.push("reja_kuni YYYY-MM-DD ko'rinishida bo'lishi kerak");
  return x;
}

// Telegram so'rovi: rasm bo'lsa sendPhoto, bo'lmasa sendMessage.
export function yigish(post, chat = KANAL) {
  const text = toliqMatn(post);
  return post.rasm_url
    ? { method: "sendPhoto", payload: { chat_id: chat, photo: post.rasm_url, caption: text, parse_mode: "HTML" } }
    : { method: "sendMessage", payload: { chat_id: chat, text, parse_mode: "HTML", disable_web_page_preview: true } };
}

// Kanalga CHIQQAN postni tuzatish yoki o'chirish so'rovi (kompyuterdagi agentlar/kanal.mjs ishlatadi, faqat ustoz aytganda).
// Rasmli postda matn rasm ostidagi yozuv, shuning uchun editMessageCaption.
export function tuzatishSorov(post, chat = KANAL) {
  if (post.holat !== "yuborildi" || !post.message_id) throw new Error("faqat kanalga chiqqan postni tuzatib bo'ladi");
  if (sorovmi(post.matn)) throw new Error("so'rovnomani tuzatib bo'lmaydi (Telegram cheklovi): o'chirib, yangisini chiqaring");
  const text = toliqMatn(post), asos = { chat_id: chat, message_id: post.message_id, parse_mode: "HTML" };
  return post.rasm_url ? { method: "editMessageCaption", payload: { ...asos, caption: text } } : { method: "editMessageText", payload: { ...asos, text, disable_web_page_preview: true } };
}
export function ochirishSorov(post, chat = KANAL) {
  if (post.holat !== "yuborildi" || !post.message_id) throw new Error("faqat kanalga chiqqan postni o'chirib bo'ladi");
  return { method: "deleteMessage", payload: { chat_id: chat, message_id: post.message_id } };
}

// Postni chiqarish uchun so'rovlar ketma-ketligi. Oddiy post: bitta so'rov. So'rovnoma: (rasm bo'lsa) rasm, keyin quiz.
export function yigishlar(post, chat = KANAL) {
  const s = sorovAjrat(post.matn);
  if (!s) return [yigish(post, chat)];
  const out = [];
  if (post.rasm_url) out.push({ method: "sendPhoto", payload: { chat_id: chat, photo: post.rasm_url, ...(post.imzo === false ? {} : { caption: IMZO, parse_mode: "HTML" }) } });
  out.push({ method: "sendPoll", payload: { chat_id: chat, question: s.savol, options: s.variantlar.map((text) => ({ text })), type: "quiz", correct_option_id: s.togri, is_anonymous: true, ...(s.izoh ? { explanation: s.izoh } : {}) } });
  return out;
}

// Kuniga bitta: bugun post chiqqan bo'lsa to'xtaydi. Aks holda reja kuni kelgan eng eski tasdiqlangan postni yuboradi.
// send(method, payload) -> Telegram javobi ({ ok, result: { message_id }, description }).
// -> { sent: 0|1, id?, sabab? }
// majbur: ustoz "bugun yana chiqar" deganda kunlik bitta post cheklovini chetlab o'tadi (tasdiq baribir shart).
export async function runKanal(db, send, { now = new Date(), chat = KANAL, log = (y) => yoz(db, y), majbur = false } = {}) {
  const kun = tashkentKun(now);
  const kunBoshi = new Date(`${kun}T00:00:00+05:00`).toISOString();
  const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };

  const bugun = must(await db.from(JADVAL).select("id").in("holat", ["yuborildi", "yuborilmoqda"]).gte("sent_at", kunBoshi).limit(1));
  if (bugun.length && !majbur) return { sent: 0, sabab: "bugun post chiqqan" };

  const navbat = must(await db.from(JADVAL).select("*").eq("holat", "tasdiqlangan").lte("reja_kuni", kun).order("reja_kuni").order("id").limit(1));
  if (!navbat.length) return { sent: 0, sabab: "tasdiqlangan post yo'q" };
  const post = navbat[0];

  // Egallash: kron ikki marta ishlasa ham post bir marta ketadi (faqat "tasdiqlangan" holatdan o'ta oladi).
  const oldim = must(await db.from(JADVAL).update({ holat: "yuborilmoqda", sent_at: now.toISOString() }).eq("id", post.id).eq("holat", "tasdiqlangan").select("id"));
  if (!oldim.length) return { sent: 0, sabab: "postni boshqa ishga tushish oldi" };

  // So'rovnomada ikki xabar bo'lishi mumkin (rasm, keyin quiz): birortasi o'tmasa post "xato" bo'ladi.
  let r = null;
  for (const { method, payload } of yigishlar(post, chat)) { r = await send(method, payload); if (!r?.ok) break; }
  if (r?.ok) {
    must(await db.from(JADVAL).update({ holat: "yuborildi", message_id: r.result?.message_id ?? null, xato: null }).eq("id", post.id).select("id"));
    await log({ agent: "kanal", tur: "ish", sarlavha: `Kanalga post chiqdi: #${post.id}`, tafsilot: { post_id: post.id, message_id: r.result?.message_id ?? null }, kalit: `kanal:${post.id}:yuborildi` });
    return { sent: 1, id: post.id };
  }
  const sabab = String(r?.description || "noma'lum xato").slice(0, 300);
  must(await db.from(JADVAL).update({ holat: "xato", xato: sabab, sent_at: null }).eq("id", post.id).select("id"));
  await log({ agent: "kanal", tur: "xato", sarlavha: `Kanalga post chiqmadi: #${post.id}`, tafsilot: { post_id: post.id, xato: sabab }, kimga: "kod" });
  return { sent: 0, id: post.id, sabab };
}
