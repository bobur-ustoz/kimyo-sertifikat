// Uyga vazifa va imtihon: ustoz (admin) manba, savollar soni va o'quvchilarni tanlaydi, murabbiy o'quvchining
// Telegramiga xabar yuboradi, o'quvchi platformadagi "Vazifalarim" sahifasida ishlaydi, natija darhol chiqadi.
// Ustoz qarori (2026-11-20): yechim ko'rsatilmaydi, javoblar platformada kiritiladi, PDF yuklab olinadi.
//
// Alohida funksiya emas (Vercel Hobby'da funksiya soni chegaralangan):
//   o'quvchi amallari  -> api/purchase-request.js  { action: "vazifa-royxat" | "vazifa-ol" | "vazifa-saqla" | "vazifa-topshir" }
//   admin amallari     -> api/bunny-auth.js        { vazifa: { amal: "malumot" | "yarat" | "natija", ... } }
//   muddat eslatmasi   -> api/keepalive.js?job=nazorat ichida (vazifaEslatma)
//   bot ichida ishlash -> api/organika-webhook.js?bot=sotuv, tugma ma'lumoti "vz:..." (vazifaTugma)
//
// Jadvallar: vazifalar, vazifa_topshiriq (supabase/migrations/20261120000000_vazifalar.sql). Ularga faqat server
// (service role) kiradi: o'quvchi to'g'ri javoblarni shu yo'ldan ololmaydi va natijani o'zi yozolmaydi.
// Savollar ANALOGLARDAN olinadi (ustoz qarori, 2026-11-21): video tushuntirish uchun, vazifa va imtihonda esa o'sha
// misolning analogi (boshqa modda va sonlar) beriladi. Manbalar: analog_questions (variant savollarining tasdiqlangan
// analoglari) va topic_example_analogs (dars misollarining analoglari). Ikkalasida ham savol "shart A) ..; B) ..; C) ..; D) .."
// ko'rinishida, javob "C) spirtlar" ko'rinishida saqlanadi. Faqat to'rt javobli testlar; yozma kataklar keyingi bosqichda.

import { createClient } from "@supabase/supabase-js";
import { yoz } from "./_navbat.js";
import { tg, escapeHtml } from "./_telegram.js";

export const TURLAR = ["uyga", "imtihon"];
export const SONI_MAX = 43, OQUVCHI_MAX = 500, NOM_MAX = 120;
export const ESLATMA_SOAT = 36;      // muddatga shuncha soat qolganda bitta eslatma
const HOUR = 3600e3;
const ms = (t) => (t ? new Date(t).getTime() : 0);
const ism = (p) => String(p?.full_name || "").trim().split(/\s+/)[0] || "";
export const TUR_NOM = { uyga: "Uyga vazifa", imtihon: "Imtihon" };

// "shart ... A) x; B) y; C) z; D) w" -> { stem, opts } (bunday ko'rinmasa null). src/analogPdf.js dagi bilan bir xil qoida.
export function variantlarniAjrat(text) {
  const t = String(text || "").replace(/\s+/g, " ").trim();
  const i = t.search(/(?:Variantlar:\s*)?A\)\s/);
  if (i < 0) return null;
  const stem = t.slice(0, i).replace(/[\s:]+$/, "");
  const parts = t.slice(i).replace(/^Variantlar:\s*/i, "").split(/\s*([ABCD])\)\s*/).slice(1);
  const opts = {};
  for (let k = 0; k + 1 < parts.length; k += 2) opts[parts[k]] = parts[k + 1].replace(/[;\s]+$/, "");
  return stem && ["A", "B", "C", "D"].every((l) => opts[l]) ? { stem, opts } : null;
}
// Analog yozuvini vazifa savoliga aylantiradi. Variantlari yoki javob harfi aniqlanmasa null (bunday analog ishlatilmaydi).
export function analogSavol({ id, savol, formula, javob }) {
  const p = variantlarniAjrat(savol), harf = String(javob ?? "").trim().match(/^([A-D])\s*\)/)?.[1];
  if (!id || !p || !harf) return null;
  return { id, question_text: p.stem, formula: formula || "", option_a: p.opts.A, option_b: p.opts.B, option_c: p.opts.C, option_d: p.opts.D, correct_option: harf, question_type: "mcq" };
}

// Havzadan tasodifiy `soni` ta savol (tartibi ham tasodifiy). rnd sinov uchun almashtiriladi.
export function tanla(pool, soni, rnd = Math.random) {
  const a = [...pool];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a.slice(0, Math.max(0, soni));
}

// O'quvchiga ketadigan savol: to'g'ri javobsiz.
export const oquvchiSavol = (q) => ({ id: q.id, question_text: q.question_text, formula: q.formula || "", option_a: q.option_a, option_b: q.option_b, option_c: q.option_c, option_d: q.option_d, question_type: "mcq" });

// Uyga vazifa yordamchi bot ichida ishlansa, har javobdan keyin to'g'ri javob ko'rsatiladi. Shuning uchun botda berilgan
// javoblar qulflanadi: javoblar ichidagi BOT kaliti qo'yilgach, saytda ham berilgan javobni o'zgartirib bo'lmaydi.
export const BOT = "_bot";
export const berilganSoni = (j) => Object.keys(j || {}).filter((k) => k !== BOT).length;
// Qulflangan bo'lsa eski javoblar ustun: yangi javob faqat hali javob berilmagan savolga qo'shiladi.
export const qoshJavob = (eski = {}, yangi = {}) => (eski[BOT] ? { ...yangi, ...eski } : yangi);

// Faqat A-D va faqat shu vazifaning savollari qoladi.
export function javobTozala(javoblar, idlar) {
  const out = {};
  if (javoblar && typeof javoblar === "object") for (const id of idlar) { const v = String(javoblar[id] ?? "").toUpperCase(); if (["A", "B", "C", "D"].includes(v)) out[id] = v; }
  return out;
}

// Tekshiruv. Javob berilmagan savol xato hisoblanadi.
export function bahola(questions, javoblar) {
  const tafsil = questions.map((q) => ({ id: q.id, tanlangan: javoblar[q.id] || null, togri_javob: q.correct_option, togri: javoblar[q.id] === q.correct_option }));
  return { togri: tafsil.filter((t) => t.togri).length, jami: questions.length, tafsil };
}

// O'quvchi ko'radigan holat.
export function holat(vazifa, top, now = new Date()) {
  if (top.holat === "topshirilgan") return "bajarildi";
  if (vazifa.muddat && ms(vazifa.muddat) < now.getTime()) return "kechikkan";
  return top.holat === "boshlangan" ? "jarayonda" : "yangi";
}

const sana = (t) => new Date(ms(t) + 5 * HOUR).toISOString().slice(0, 10).split("-").reverse().join(".");
const STOP = "\n\nBunday xabarlar kerak bo'lmasa, /stop deb yozing.";
// Murabbiy ohangida (agentlar/murabbiy.md): iliq, majburlamaydi, tekshirib bo'lmaydigan gap yo'q.
export function xabarMatni(v, p) {
  const salom = ism(p) ? `Assalomu alaykum, ${ism(p)}!` : "Assalomu alaykum!";
  const muddat = v.muddat ? ` Muddati: ${sana(v.muddat)} gacha.` : "";
  return v.tur === "imtihon"
    ? `${salom} Sizga imtihon tayinlandi: "${v.nom}", ${v.savollar.length} ta savol.${muddat} Tayyor bo'lganingizda pastdagi tugma orqali boshlang.${STOP}`
    : `${salom} Yangi uyga vazifa: "${v.nom}", ${v.savollar.length} ta savol.${muddat} Pastdagi tugma bilan shu yerning o'zida ishlaysiz, natija darhol chiqadi. Xohlasangiz saytda ochib, PDF qilib yuklab olasiz.${STOP}`;
}
export function eslatmaMatni(v, p, bajarilgan) {
  const salom = ism(p) ? `Assalomu alaykum, ${ism(p)}!` : "Assalomu alaykum!";
  return `${salom} "${v.nom}" ${v.tur === "imtihon" ? "imtihoni" : "vazifasi"}ning muddati ${sana(v.muddat)} da tugaydi.${bajarilgan ? ` ${bajarilgan} ta savolga javob bergansiz, qolganini tugatib topshirsangiz bo'ladi.` : ""} Tushunmagan joy bo'lsa shu yerga yozing.${STOP}`;
}
// Uyga vazifa botning o'zida ishlanadi ("Boshlash"), saytda ham ochsa bo'ladi. Imtihon faqat saytda.
const tugma = (site, v) => ({ inline_keyboard: v?.tur === "uyga" && v.id
  ? [[{ text: "▶️ Shu yerda ishlash", callback_data: `vz:b:${v.id}` }], [{ text: "Saytda ochish", url: `${site}/#vazifa` }]]
  : [[{ text: "Vazifani ochish", url: `${site}/#vazifa` }]] });

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
const optional = ({ data, error }) => (error ? [] : data || []);
const sayt = () => process.env.SITE_URL || "https://kimyo-sertifikat.vercel.app";
const botSend = () => {
  const token = process.env.SOTUV_BOT_TOKEN;
  return token ? (chat_id, text, reply_markup) => tg("sendMessage", { chat_id, text, reply_markup }, { token }) : null;
};

// ---------------------------------------------------------------- o'quvchi

// Vazifadagi savollarni (analog id lari) ikki jadvaldan o'qib, saqlangan tartibda qaytaradi.
async function savollarTartibda(db, idlar) {
  const [a, m] = await Promise.all([
    db.from("analog_questions").select("id,savol,formula,javob").in("id", idlar).then(must),
    db.from("topic_example_analogs").select("example_id,analog_savol,analog_javob").in("example_id", idlar).then(optional),
  ]);
  const by = new Map([...a.map(analogSavol), ...m.map((r) => analogSavol({ id: r.example_id, savol: r.analog_savol, javob: r.analog_javob }))].filter(Boolean).map((q) => [q.id, q]));
  return idlar.map((id) => by.get(id)).filter(Boolean);
}

// Ishlatsa bo'ladigan hamma analoglar, qaysi variant yoki dars mavzusiga tegishli ekani bilan. -> [{ ...savol, variant_id | topic_id }]
async function havza(db) {
  const [a, qs, m, ex] = await Promise.all([
    db.from("analog_questions").select("id,question_id,savol,formula,javob,is_approved").eq("is_approved", true).limit(20000).then(must),
    db.from("questions").select("id,variant_id").limit(20000).then(must),
    db.from("topic_example_analogs").select("example_id,analog_savol,analog_javob").limit(20000).then(optional),
    db.from("topic_examples").select("id,topic_id").limit(20000).then(optional),
  ]);
  const varBy = new Map(qs.map((q) => [q.id, q.variant_id])), topBy = new Map(ex.map((e) => [e.id, e.topic_id]));
  return [
    ...a.map((r) => { const q = analogSavol(r); return q && varBy.has(r.question_id) ? { ...q, variant_id: varBy.get(r.question_id) } : null; }),
    ...m.map((r) => { const q = analogSavol({ id: r.example_id, savol: r.analog_savol, javob: r.analog_javob }); return q && topBy.has(r.example_id) ? { ...q, topic_id: topBy.get(r.example_id) } : null; }),
  ].filter(Boolean);
}

// -> { status, body }. now sinov uchun.
export async function oquvchiAmal(db, userId, body = {}, { now = new Date() } = {}) {
  const amal = body.action;
  if (amal === "vazifa-royxat") {
    const tops = must(await db.from("vazifa_topshiriq").select("vazifa_id,holat,javoblar,togri,jami,topshirilgan_at").eq("student_id", userId));
    if (!tops.length) return { status: 200, body: { vazifalar: [] } };
    const vs = must(await db.from("vazifalar").select("id,tur,nom,mavzu,savollar,muddat,created_at").in("id", tops.map((t) => t.vazifa_id)));
    const vazifalar = vs.map((v) => {
      const t = tops.find((x) => x.vazifa_id === v.id);
      return { id: v.id, tur: v.tur, nom: v.nom, mavzu: v.mavzu, soni: v.savollar.length, muddat: v.muddat, holat: holat(v, t, now),
        javob_berilgan: berilganSoni(t.javoblar), togri: t.togri, jami: t.jami, topshirilgan_at: t.topshirilgan_at, created_at: v.created_at };
    }).sort((a, b) => (a.holat === "bajarildi") - (b.holat === "bajarildi") || ms(b.created_at) - ms(a.created_at));
    return { status: 200, body: { vazifalar } };
  }

  const id = Number(body.id);
  if (!Number.isInteger(id)) return { status: 400, body: { error: "Vazifa ko'rsatilmagan" } };
  const top = must(await db.from("vazifa_topshiriq").select("id,holat,javoblar,togri,jami").eq("vazifa_id", id).eq("student_id", userId))[0];
  if (!top) return { status: 404, body: { error: "Bu vazifa sizga berilmagan" } };
  const v = must(await db.from("vazifalar").select("id,tur,nom,mavzu,savollar,muddat").eq("id", id))[0];
  if (!v) return { status: 404, body: { error: "Vazifa topilmadi" } };
  const qs = await savollarTartibda(db, v.savollar);
  const meta = { id: v.id, tur: v.tur, nom: v.nom, mavzu: v.mavzu, muddat: v.muddat };

  if (amal === "vazifa-ol") {
    if (top.holat === "topshirilgan") return { status: 200, body: { vazifa: meta, savollar: qs.map(oquvchiSavol), javoblar: top.javoblar, natija: bahola(qs, top.javoblar || {}) } };
    const { [BOT]: qulf, ...berilgan } = top.javoblar || {};
    return { status: 200, body: { vazifa: meta, savollar: qs.map(oquvchiSavol), javoblar: berilgan, qulf: !!qulf } };
  }
  if (top.holat === "topshirilgan") return { status: 409, body: { error: "Bu vazifa topshirilgan" } };
  const javoblar = qoshJavob(top.javoblar, javobTozala(body.javoblar, qs.map((q) => q.id)));

  if (amal === "vazifa-saqla") {
    must(await db.from("vazifa_topshiriq").update({ javoblar, holat: "boshlangan", ...(top.holat === "berilgan" ? { boshlangan_at: now.toISOString() } : {}) }).eq("id", top.id).select("id"));
    return { status: 200, body: { ok: true } };
  }
  if (amal === "vazifa-topshir") {
    const natija = bahola(qs, javoblar);
    // Egallash: ikki marta bosilsa ham bir marta topshiriladi.
    const oldim = must(await db.from("vazifa_topshiriq").update({ javoblar, holat: "topshirilgan", togri: natija.togri, jami: natija.jami, topshirilgan_at: now.toISOString() }).eq("id", top.id).neq("holat", "topshirilgan").select("id"));
    if (!oldim.length) return { status: 409, body: { error: "Bu vazifa topshirilgan" } };
    // Javoblar umumiy `answers` jadvaliga yozilmaydi: u variant savollari uchun, bu yerda esa ularning analoglari.
    return { status: 200, body: { ok: true, natija } };
  }
  return { status: 400, body: { error: "Noma'lum amal" } };
}

export async function handleVazifa(req, res) {
  if (!process.env.SUPABASE_SERVICE_ROLE_KEY) return res.status(503).json({ error: "Hali sozlanmagan" });
  const jwt = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  if (!jwt) return res.status(401).json({ error: "Avval hisobingizga kiring" });
  const { data: who, error } = await createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY).auth.getUser(jwt);
  if (error || !who?.user) return res.status(401).json({ error: "Sessiya eskirgan. Qayta kiring." });
  const db = createClient(process.env.VITE_SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
  try {
    const r = await oquvchiAmal(db, who.user.id, req.body || {});
    res.setHeader("Cache-Control", "no-store");
    return res.status(r.status).json(r.body);
  } catch (e) {
    console.error("vazifa failed:", e.message);
    return res.status(500).json({ error: /vazifa/.test(e.message) && /does not exist|schema cache/.test(e.message) ? "Vazifalar bo'limi hali yoqilmagan" : "Xatolik yuz berdi. Qayta urinib ko'ring." });
  }
}

// ---------------------------------------------------------------- admin

// Yangi vazifa so'rovini tekshiradi. -> { xato } | { nom, tur, variantlar, mavzular, soni, muddat, oquvchilar }
export function tekshir(b = {}, now = new Date()) {
  const nom = String(b.nom ?? "").trim().slice(0, NOM_MAX);
  // Manba: variantlar (ularning savollariga yozilgan analoglar) va/yoki dars mavzulari (misollarining analoglari).
  const idlar = (x) => [...new Set((Array.isArray(x) ? x : []).map(String).filter(Boolean))].slice(0, 200);
  const variantlar = idlar(b.variantlar), mavzular = idlar(b.mavzular);
  const tur = TURLAR.includes(b.tur) ? b.tur : "uyga";
  const soni = Number(b.soni), kun = Number(b.kun);
  const oquvchilar = [...new Set(Array.isArray(b.oquvchilar) ? b.oquvchilar.map(String) : [])];
  if (nom.length < 2) return { xato: "Vazifa nomini yozing" };
  if (!mavzular.length && !variantlar.length) return { xato: "Variant yoki mavzuni tanlang" };
  if (!Number.isInteger(soni) || soni < 1 || soni > SONI_MAX) return { xato: `Savollar soni 1 dan ${SONI_MAX} gacha bo'lsin` };
  if (!oquvchilar.length) return { xato: "Kamida bitta o'quvchini tanlang" };
  if (oquvchilar.length > OQUVCHI_MAX) return { xato: `Bir vazifaga ko'pi bilan ${OQUVCHI_MAX} o'quvchi` };
  if (b.kun != null && b.kun !== "" && (!Number.isFinite(kun) || kun < 1 || kun > 60)) return { xato: "Muddat 1 dan 60 kungacha bo'lsin" };
  // Muddat: shuncha kundan keyingi kunning oxiri (Toshkent vaqti bilan 23:59).
  let muddat = null;
  if (Number.isFinite(kun) && kun >= 1) { const d = new Date(now.getTime() + 5 * HOUR + kun * 24 * HOUR).toISOString().slice(0, 10); muddat = new Date(`${d}T23:59:00+05:00`).toISOString(); }
  return { nom, tur, variantlar, mavzular, soni, muddat, oquvchilar };
}

export async function adminAmal(db, adminId, body = {}, { now = new Date(), send = botSend(), rnd = Math.random, log = (y) => yoz(db, y), site = sayt() } = {}) {
  if (body.amal === "malumot") {
    const [pool, profiles, leads, vs, tops, variants, teachers, topics] = await Promise.all([
      havza(db),
      db.from("profiles").select("id,full_name,email,phone,plan,plan_expires_at,is_admin").limit(5000).then(must),
      db.from("sotuv_leads").select("linked_user_id,remind").not("linked_user_id", "is", null).limit(5000).then(optional),
      db.from("vazifalar").select("id,tur,nom,mavzu,savollar,muddat,created_at").order("created_at", { ascending: false }).limit(50).then(must),
      db.from("vazifa_topshiriq").select("vazifa_id,holat,togri,jami").limit(20000).then(must),
      db.from("variants").select("id,teacher_id,variant_number").limit(2000).then(must),
      db.from("teachers").select("id,name").limit(500).then(must),
      db.from("topics").select("id,name,sort_order").limit(500).then(optional),
    ]);
    const san = (k) => pool.reduce((o, q) => (q[k] ? { ...o, [q[k]]: (o[q[k]] || 0) + 1 } : o), {});
    const varSoni = san("variant_id"), mavSoni = san("topic_id");
    const ulangan = new Map(leads.map((l) => [l.linked_user_id, l.remind]));
    return { status: 200, body: {
      variantlar: variants.filter((v) => varSoni[v.id]).map((v) => ({ id: v.id, nom: `${teachers.find((x) => x.id === v.teacher_id)?.name || "To'plam"}, ${v.variant_number}-variant`, soni: varSoni[v.id] }))
        .sort((a, b) => a.nom.localeCompare(b.nom, "uz", { numeric: true })),
      mavzular: topics.filter((t) => mavSoni[t.id]).sort((a, b) => (a.sort_order ?? 0) - (b.sort_order ?? 0)).map((t) => ({ id: t.id, nom: t.name, soni: mavSoni[t.id] })),
      // Admin o'zini ham tanlay oladi (ro'yxat boshida): vazifa va Telegram xabari qanday ko'rinishini sinab ko'rish uchun.
      oquvchilar: profiles.filter((p) => !p.is_admin || p.id === adminId).map((p) => ({ id: p.id, oz: p.id === adminId, ism: p.full_name || String(p.email || "").split("@")[0] || "Ismsiz",
        plan: p.plan && (!p.plan_expires_at || ms(p.plan_expires_at) > now.getTime()) ? p.plan : "free", telegram: !ulangan.has(p.id) ? "yo'q" : ulangan.get(p.id) ? "ulangan" : "o'chirgan" }))
        .sort((a, b) => b.oz - a.oz || (a.plan === "free") - (b.plan === "free") || a.ism.localeCompare(b.ism, "uz")),
      vazifalar: vs.map((v) => { const t = tops.filter((x) => x.vazifa_id === v.id), b = t.filter((x) => x.holat === "topshirilgan");
        return { id: v.id, tur: v.tur, nom: v.nom, mavzu: v.mavzu, soni: v.savollar.length, muddat: v.muddat, created_at: v.created_at, berilgan: t.length, bajargan: b.length,
          ortacha: b.length ? Math.round(b.reduce((a, x) => a + (x.jami ? x.togri / x.jami : 0), 0) / b.length * 100) : null }; }),
    } };
  }

  if (body.amal === "natija") {
    const id = Number(body.id);
    const v = must(await db.from("vazifalar").select("id,tur,nom,mavzu,savollar,muddat").eq("id", id))[0];
    if (!v) return { status: 404, body: { error: "Vazifa topilmadi" } };
    const tops = must(await db.from("vazifa_topshiriq").select("student_id,holat,javoblar,togri,jami,topshirilgan_at,tg_xabar_at").eq("vazifa_id", id));
    const ps = tops.length ? must(await db.from("profiles").select("id,full_name,email").in("id", tops.map((t) => t.student_id))) : [];
    return { status: 200, body: { vazifa: { id: v.id, nom: v.nom, tur: v.tur, soni: v.savollar.length, muddat: v.muddat },
      oquvchilar: tops.map((t) => { const p = ps.find((x) => x.id === t.student_id); return { ism: p?.full_name || String(p?.email || "").split("@")[0] || "Ismsiz", holat: holat(v, t, now), togri: t.togri ?? null, jami: t.jami ?? null,
        javob_berilgan: berilganSoni(t.javoblar), topshirilgan_at: t.topshirilgan_at, telegram: !!t.tg_xabar_at }; }).sort((a, b) => a.ism.localeCompare(b.ism, "uz")) } };
  }

  if (body.amal === "yarat") {
    const t = tekshir(body, now);
    if (t.xato) return { status: 400, body: { error: t.xato } };
    const pool = (await havza(db)).filter((q) => (q.variant_id && t.variantlar.includes(q.variant_id)) || (q.topic_id && t.mavzular.includes(q.topic_id)));
    if (pool.length < t.soni) return { status: 400, body: { error: `Tanlangan manbada faqat ${pool.length} ta analog savol bor` } };
    const mavzu = String(body.manba_nom || "Analog savollar").slice(0, 300);
    const profiles = must(await db.from("profiles").select("id,full_name,is_admin").in("id", t.oquvchilar)).filter((p) => !p.is_admin || p.id === adminId);
    if (!profiles.length) return { status: 400, body: { error: "Tanlangan o'quvchilar topilmadi" } };
    const savollar = tanla(pool, t.soni, rnd).map((q) => q.id);
    const v = must(await db.from("vazifalar").insert({ tur: t.tur, nom: t.nom, mavzu, savollar, muddat: t.muddat, created_by: adminId }).select("id,tur,nom,mavzu,savollar,muddat"))[0];
    must(await db.from("vazifa_topshiriq").insert(profiles.map((p) => ({ vazifa_id: v.id, student_id: p.id }))).select("id"));

    // Telegram: faqat botni ulagan va /stop demagan o'quvchiga. Qolganlari vazifani platformada ko'radi.
    let yuborildi = 0, yetmadi = 0;
    const leads = send ? optional(await db.from("sotuv_leads").select("tg_id,linked_user_id,remind").in("linked_user_id", profiles.map((p) => p.id))) : [];
    for (const p of profiles) {
      const lead = leads.find((l) => l.linked_user_id === p.id);
      if (!lead || !lead.remind) continue;
      let r; try { r = await send(lead.tg_id, xabarMatni(v, p), tugma(site, v)); } catch { r = null; }
      if (r?.ok) { yuborildi++; await db.from("vazifa_topshiriq").update({ tg_xabar_at: now.toISOString() }).eq("vazifa_id", v.id).eq("student_id", p.id); } else yetmadi++;
    }
    const xabarsiz = profiles.length - yuborildi;
    await log({ agent: "murabbiy", tur: "ish", sarlavha: `${TUR_NOM[v.tur]} tayinlandi: "${v.nom}" (${profiles.length} o'quvchi, ${yuborildi} tasiga Telegram xabar)`,
      tafsilot: { vazifa_id: v.id, tur: v.tur, mavzu: v.mavzu, savollar: savollar.length, oquvchilar: profiles.length, yuborildi, yetmadi, xabarsiz } });
    return { status: 200, body: { ok: true, id: v.id, oquvchilar: profiles.length, yuborildi, yetmadi, xabarsiz } };
  }
  return { status: 400, body: { error: "Noma'lum amal" } };
}

// ---------------------------------------------------------------- muddat eslatmasi (ertalabki kron)

// Muddatiga ESLATMA_SOAT dan kam qolgan, hali topshirilmagan vazifalar uchun bitta eslatma. send(tg_id, text, reply_markup) -> { ok }.
export async function vazifaEslatma(db, send, { now = new Date(), site = sayt() } = {}) {
  const t = now.getTime();
  const vs = must(await db.from("vazifalar").select("id,tur,nom,savollar,muddat").gt("muddat", now.toISOString()).lt("muddat", new Date(t + ESLATMA_SOAT * HOUR).toISOString()));
  if (!vs.length) return { yuborildi: 0 };
  const tops = must(await db.from("vazifa_topshiriq").select("id,vazifa_id,student_id,holat,javoblar,eslatma_at").in("vazifa_id", vs.map((v) => v.id)).neq("holat", "topshirilgan")).filter((x) => !x.eslatma_at);
  if (!tops.length) return { yuborildi: 0 };
  const ids = [...new Set(tops.map((x) => x.student_id))];
  const [leads, ps] = await Promise.all([db.from("sotuv_leads").select("tg_id,linked_user_id,remind").in("linked_user_id", ids).then(optional), db.from("profiles").select("id,full_name").in("id", ids).then(must)]);
  let yuborildi = 0;
  for (const x of tops) {
    const lead = leads.find((l) => l.linked_user_id === x.student_id);
    if (!lead || !lead.remind) continue;
    const v = vs.find((y) => y.id === x.vazifa_id);
    let r; try { r = await send(lead.tg_id, eslatmaMatni(v, ps.find((p) => p.id === x.student_id), berilganSoni(x.javoblar)), tugma(site, v)); } catch { r = null; }
    if (r?.ok) { yuborildi++; await db.from("vazifa_topshiriq").update({ eslatma_at: now.toISOString() }).eq("id", x.id); }
  }
  return { yuborildi };
}

// ---------------------------------------------------------------- yordamchi bot ichida ishlash

const HARF = ["A", "B", "C", "D"];
const chiziq = (done, total) => "▰".repeat(done) + "▱".repeat(Math.max(total - done, 0));
const kb = (...rows) => ({ inline_keyboard: rows });
// Savol ekrani: sarlavha, progress, shart va to'rt javob; ostida A B C D tugmalari.
export function savolEkrani(v, q, idx, jami) {
  const text = `<b>${escapeHtml(v.nom)}</b>\n${chiziq(idx, jami)}  ${idx + 1}/${jami}\n\n${escapeHtml(q.question_text)}${q.formula ? `\n${escapeHtml(q.formula)}` : ""}\n\n`
    + HARF.map((h) => `<b>${h})</b> ${escapeHtml(q[`option_${h.toLowerCase()}`])}`).join("\n");
  return { text, reply_markup: kb(HARF.map((h) => ({ text: h, callback_data: `vz:a:${v.id}:${idx}:${h}` }))) };
}
// Javobdan keyin: to'g'ri yoki noto'g'ri va to'g'ri javob. Yechim ko'rsatilmaydi (ustoz qarori).
export function hukmEkrani(v, q, tanlangan, oxirgi, natija, site) {
  const ok = tanlangan === q.correct_option, t = q.correct_option;
  let text = `<b>${escapeHtml(v.nom)}</b>\n\n${escapeHtml(q.question_text)}\n\nSizning javobingiz: <b>${tanlangan})</b> ${escapeHtml(q[`option_${tanlangan.toLowerCase()}`])}\n`
    + (ok ? "✅ <b>To'g'ri!</b>" : `❌ <b>Noto'g'ri.</b> To'g'ri javob: <b>${t})</b> ${escapeHtml(q[`option_${t.toLowerCase()}`])}`);
  if (!oxirgi) return { text, reply_markup: kb([{ text: "Keyingi ▶", callback_data: `vz:n:${v.id}` }]) };
  const foiz = Math.round((natija.togri / natija.jami) * 100);
  text += `\n\n🎯 <b>Vazifa topshirildi: ${natija.togri} / ${natija.jami}</b>\n${foiz >= 80 ? "Barakalla, yaxshi natija." : foiz >= 50 ? "Yomon emas. Xato chiqqan savollarni yana bir ko'rib chiqing." : "Xavotir olmang. Mavzuni yana bir ko'rib chiqing, tushunmagan joyingizni shu yerga yozing."}`;
  return { text, reply_markup: kb([{ text: "Natijani saytda ko'rish", url: `${site}/#vazifa` }]) };
}

// Tugma bosilishi: "vz:b:<vazifa>" boshlash yoki davom etish (savol yangi xabar bo'lib keladi, tayinlash xabari joyida qoladi),
// "vz:n:<vazifa>" keyingi savol (shu xabar o'rnida), "vz:a:<vazifa>:<idx>:<harf>" javob.
// send(method, payload) -> Bot API. Tugma bosilgan xabar tahrirlanadi (chat xabarga to'lib ketmaydi).
export async function vazifaTugma(db, send, cq, { now = new Date(), site = sayt() } = {}) {
  const [, amal, vid, idxS, harf] = String(cq.data || "").split(":");
  const chat_id = cq.message?.chat?.id ?? cq.from?.id, message_id = cq.message?.message_id;
  const ack = (text) => send("answerCallbackQuery", { callback_query_id: cq.id, ...(text ? { text, show_alert: true } : {}) });
  const korsat = (ekran, yangi = false) => message_id && !yangi
    ? send("editMessageText", { chat_id, message_id, parse_mode: "HTML", ...ekran })
    : send("sendMessage", { chat_id, parse_mode: "HTML", ...ekran });

  const lead = optional(await db.from("sotuv_leads").select("linked_user_id").eq("tg_id", cq.from?.id))[0];
  if (!lead?.linked_user_id) return ack("Avval saytdagi Profilim sahifasida Telegramni hisobingizga ulang.");
  const id = Number(vid);
  const top = Number.isInteger(id) ? must(await db.from("vazifa_topshiriq").select("id,holat,javoblar,togri,jami").eq("vazifa_id", id).eq("student_id", lead.linked_user_id))[0] : null;
  const v = top ? must(await db.from("vazifalar").select("id,tur,nom,savollar,muddat").eq("id", id))[0] : null;
  if (!top || !v) return ack("Bu vazifa topilmadi.");
  if (v.tur !== "uyga") return ack("Imtihon saytda ishlanadi.");
  if (top.holat === "topshirilgan") return ack(`Bu vazifa topshirilgan: ${top.togri} / ${top.jami}.`);
  const qs = await savollarTartibda(db, v.savollar);
  if (!qs.length) return ack("Savollar topilmadi. Ustozga yozing.");
  const javoblar = top.javoblar || {};
  const keyingi = () => qs.findIndex((q) => !javoblar[q.id]);

  if (amal === "b" || amal === "n") {
    await ack();
    const idx = keyingi();
    if (idx < 0) return topshir();                       // hammasiga javob berilgan, lekin topshirilmagan (saytda boshlangan)
    return korsat(savolEkrani(v, qs[idx], idx, qs.length), amal === "b");
  }
  if (amal === "a") {
    const idx = Number(idxS), q = qs[idx];
    if (!q || !HARF.includes(harf)) return ack();
    if (javoblar[q.id]) return ack("Bu savolga allaqachon javob berilgan.");
    javoblar[q.id] = harf; javoblar[BOT] = true;
    const oxirgi = keyingi() < 0;
    const natija = oxirgi ? bahola(qs, javoblar) : null;
    // Topshirilgan vazifaga yozilmaydi: ikki marta bosilsa yoki saytda topshirilgan bo'lsa ikkinchisi o'tmaydi.
    const yozildi = must(await db.from("vazifa_topshiriq").update({ javoblar, ...(oxirgi
      ? { holat: "topshirilgan", togri: natija.togri, jami: natija.jami, topshirilgan_at: now.toISOString() }
      : { holat: "boshlangan", ...(top.holat === "berilgan" ? { boshlangan_at: now.toISOString() } : {}) }) }).eq("id", top.id).neq("holat", "topshirilgan").select("id"));
    if (!yozildi.length) return ack("Bu vazifa topshirilgan.");
    await ack();
    return korsat(hukmEkrani(v, q, harf, oxirgi, natija, site));
  }
  return ack();

  async function topshir() {
    const natija = bahola(qs, javoblar);
    const yozildi = must(await db.from("vazifa_topshiriq").update({ holat: "topshirilgan", togri: natija.togri, jami: natija.jami, topshirilgan_at: now.toISOString() }).eq("id", top.id).neq("holat", "topshirilgan").select("id"));
    if (!yozildi.length) return;
    return korsat({ text: `<b>${escapeHtml(v.nom)}</b>\n\n🎯 <b>Vazifa topshirildi: ${natija.togri} / ${natija.jami}</b>`, reply_markup: kb([{ text: "Natijani saytda ko'rish", url: `${site}/#vazifa` }]) }, true);
  }
}
