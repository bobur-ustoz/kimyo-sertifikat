// Uyga vazifa va imtihon: ustoz (admin) mavzu, savollar soni va o'quvchilarni tanlaydi, murabbiy o'quvchining
// Telegramiga xabar yuboradi, o'quvchi platformadagi "Vazifalarim" sahifasida ishlaydi, natija darhol chiqadi.
// Ustoz qarori (2026-11-20): yechim ko'rsatilmaydi, javoblar platformada kiritiladi, PDF yuklab olinadi.
//
// Alohida funksiya emas (Vercel Hobby'da funksiya soni chegaralangan):
//   o'quvchi amallari  -> api/purchase-request.js  { action: "vazifa-royxat" | "vazifa-ol" | "vazifa-saqla" | "vazifa-topshir" }
//   admin amallari     -> api/bunny-auth.js        { vazifa: { amal: "malumot" | "yarat" | "natija", ... } }
//   muddat eslatmasi   -> api/keepalive.js?job=nazorat ichida (vazifaEslatma)
//
// Jadvallar: vazifalar, vazifa_topshiriq (supabase/migrations/20261120000000_vazifalar.sql). Ularga faqat server
// (service role) kiradi: o'quvchi to'g'ri javoblarni shu yo'ldan ololmaydi va natijani o'zi yozolmaydi.
// Birinchi bosqich: faqat to'rt javobli test savollari. Yozma masala kataklari keyingi bosqichda.

import { createClient } from "@supabase/supabase-js";
import { yoz } from "./_navbat.js";
import { tg } from "./_telegram.js";

export const TURLAR = ["uyga", "imtihon"];
export const SONI_MAX = 43, OQUVCHI_MAX = 500, NOM_MAX = 120;
export const ESLATMA_SOAT = 36;      // muddatga shuncha soat qolganda bitta eslatma
const HOUR = 3600e3;
const SAVOL_USTUN = "id,variant_id,topic,formula,question_text,option_a,option_b,option_c,option_d,correct_option,question_type";
const ms = (t) => (t ? new Date(t).getTime() : 0);
const ism = (p) => String(p?.full_name || "").trim().split(/\s+/)[0] || "";
export const TUR_NOM = { uyga: "Uyga vazifa", imtihon: "Imtihon" };

// Vazifaga yaraydigan savol: to'rtta javobi va to'g'ri javobi bor test.
export const yaroqli = (q) => (q.question_type || "mcq") === "mcq" && ["A", "B", "C", "D"].includes(q.correct_option)
  && [q.option_a, q.option_b, q.option_c, q.option_d].every((x) => String(x ?? "").trim()) && String(q.question_text ?? "").trim();

// Havzadan tasodifiy `soni` ta savol (tartibi ham tasodifiy). rnd sinov uchun almashtiriladi.
export function tanla(pool, soni, rnd = Math.random) {
  const a = [...pool];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a.slice(0, Math.max(0, soni));
}

// O'quvchiga ketadigan savol: to'g'ri javobsiz.
export const oquvchiSavol = (q) => ({ id: q.id, question_text: q.question_text, formula: q.formula || "", option_a: q.option_a, option_b: q.option_b, option_c: q.option_c, option_d: q.option_d, question_type: "mcq" });

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
    : `${salom} Yangi uyga vazifa: "${v.nom}", ${v.savollar.length} ta savol.${muddat} Platformada ishlaysiz, natija darhol chiqadi. Xohlasangiz o'sha yerdan PDF qilib yuklab olasiz.${STOP}`;
}
export function eslatmaMatni(v, p, bajarilgan) {
  const salom = ism(p) ? `Assalomu alaykum, ${ism(p)}!` : "Assalomu alaykum!";
  return `${salom} "${v.nom}" ${v.tur === "imtihon" ? "imtihoni" : "vazifasi"}ning muddati ${sana(v.muddat)} da tugaydi.${bajarilgan ? ` ${bajarilgan} ta savolga javob bergansiz, qolganini tugatib topshirsangiz bo'ladi.` : ""} Tushunmagan joy bo'lsa shu yerga yozing.${STOP}`;
}
const tugma = (site) => ({ inline_keyboard: [[{ text: "Vazifani ochish", url: `${site}/#vazifa` }]] });

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
const optional = ({ data, error }) => (error ? [] : data || []);
const sayt = () => process.env.SITE_URL || "https://kimyo-sertifikat.vercel.app";
const botSend = () => {
  const token = process.env.SOTUV_BOT_TOKEN;
  return token ? (chat_id, text, reply_markup) => tg("sendMessage", { chat_id, text, reply_markup }, { token }) : null;
};

// ---------------------------------------------------------------- o'quvchi

async function savollarTartibda(db, idlar) {
  const rows = must(await db.from("questions").select(SAVOL_USTUN).in("id", idlar));
  const by = new Map(rows.map((q) => [q.id, q]));
  return idlar.map((id) => by.get(id)).filter(Boolean);
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
        javob_berilgan: Object.keys(t.javoblar || {}).length, togri: t.togri, jami: t.jami, topshirilgan_at: t.topshirilgan_at, created_at: v.created_at };
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
    return { status: 200, body: { vazifa: meta, savollar: qs.map(oquvchiSavol), javoblar: top.javoblar || {} } };
  }
  if (top.holat === "topshirilgan") return { status: 409, body: { error: "Bu vazifa topshirilgan" } };
  const javoblar = javobTozala(body.javoblar, qs.map((q) => q.id));

  if (amal === "vazifa-saqla") {
    must(await db.from("vazifa_topshiriq").update({ javoblar, holat: "boshlangan", ...(top.holat === "berilgan" ? { boshlangan_at: now.toISOString() } : {}) }).eq("id", top.id).select("id"));
    return { status: 200, body: { ok: true } };
  }
  if (amal === "vazifa-topshir") {
    const natija = bahola(qs, javoblar);
    // Egallash: ikki marta bosilsa ham bir marta topshiriladi.
    const oldim = must(await db.from("vazifa_topshiriq").update({ javoblar, holat: "topshirilgan", togri: natija.togri, jami: natija.jami, topshirilgan_at: now.toISOString() }).eq("id", top.id).neq("holat", "topshirilgan").select("id"));
    if (!oldim.length) return { status: 409, body: { error: "Bu vazifa topshirilgan" } };
    // Umumiy statistika (Tahlil, murabbiy) ham shu javoblarni ko'rsin. Yozilmasa natija baribir saqlangan.
    const rows = natija.tafsil.filter((t) => t.tanlangan).map((t) => ({ student_id: userId, question_id: t.id, selected_option: t.tanlangan, is_correct: t.togri, answered_at: now.toISOString() }));
    if (rows.length) { const { error } = await db.from("answers").upsert(rows, { onConflict: "student_id,question_id" }); if (error) console.error("vazifa: answers yozilmadi:", error.message); }
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

// Yangi vazifa so'rovini tekshiradi. -> { xato } | { nom, tur, mavzular, variant_id, soni, muddat, oquvchilar }
export function tekshir(b = {}, now = new Date()) {
  const nom = String(b.nom ?? "").trim().slice(0, NOM_MAX);
  // Manba: bir yoki bir necha mavzu, yoki bitta variant (bazada bitta mavzuda savol kam bo'lishi mumkin).
  const mavzular = [...new Set((Array.isArray(b.mavzular) ? b.mavzular : b.mavzu ? [b.mavzu] : []).map((x) => String(x).trim()).filter(Boolean))].slice(0, 100);
  const variant_id = b.variant_id ? String(b.variant_id) : null;
  const tur = TURLAR.includes(b.tur) ? b.tur : "uyga";
  const soni = Number(b.soni), kun = Number(b.kun);
  const oquvchilar = [...new Set(Array.isArray(b.oquvchilar) ? b.oquvchilar.map(String) : [])];
  if (nom.length < 2) return { xato: "Vazifa nomini yozing" };
  if (!mavzular.length && !variant_id) return { xato: "Mavzu yoki variantni tanlang" };
  if (!Number.isInteger(soni) || soni < 1 || soni > SONI_MAX) return { xato: `Savollar soni 1 dan ${SONI_MAX} gacha bo'lsin` };
  if (!oquvchilar.length) return { xato: "Kamida bitta o'quvchini tanlang" };
  if (oquvchilar.length > OQUVCHI_MAX) return { xato: `Bir vazifaga ko'pi bilan ${OQUVCHI_MAX} o'quvchi` };
  if (b.kun != null && b.kun !== "" && (!Number.isFinite(kun) || kun < 1 || kun > 60)) return { xato: "Muddat 1 dan 60 kungacha bo'lsin" };
  // Muddat: shuncha kundan keyingi kunning oxiri (Toshkent vaqti bilan 23:59).
  let muddat = null;
  if (Number.isFinite(kun) && kun >= 1) { const d = new Date(now.getTime() + 5 * HOUR + kun * 24 * HOUR).toISOString().slice(0, 10); muddat = new Date(`${d}T23:59:00+05:00`).toISOString(); }
  return { nom, tur, mavzular, variant_id, soni, muddat, oquvchilar };
}

export async function adminAmal(db, adminId, body = {}, { now = new Date(), send = botSend(), rnd = Math.random, log = (y) => yoz(db, y), site = sayt() } = {}) {
  if (body.amal === "malumot") {
    const [qs, profiles, leads, vs, tops, variants, teachers] = await Promise.all([
      db.from("questions").select(SAVOL_USTUN).limit(20000).then(must),
      db.from("profiles").select("id,full_name,email,phone,plan,plan_expires_at,is_admin").limit(5000).then(must),
      db.from("sotuv_leads").select("linked_user_id,remind").not("linked_user_id", "is", null).limit(5000).then(optional),
      db.from("vazifalar").select("id,tur,nom,mavzu,savollar,muddat,created_at").order("created_at", { ascending: false }).limit(50).then(must),
      db.from("vazifa_topshiriq").select("vazifa_id,holat,togri,jami").limit(20000).then(must),
      db.from("variants").select("id,teacher_id,variant_number").limit(2000).then(must),
      db.from("teachers").select("id,name").limit(500).then(must),
    ]);
    const varSoni = {};
    for (const q of qs) if (yaroqli(q)) varSoni[q.variant_id] = (varSoni[q.variant_id] || 0) + 1;
    const mavzu = {};
    for (const q of qs) if (yaroqli(q) && String(q.topic || "").trim()) mavzu[q.topic.trim()] = (mavzu[q.topic.trim()] || 0) + 1;
    const ulangan = new Map(leads.map((l) => [l.linked_user_id, l.remind]));
    return { status: 200, body: {
      variantlar: variants.filter((v) => varSoni[v.id]).map((v) => ({ id: v.id, nom: `${teachers.find((x) => x.id === v.teacher_id)?.name || "To'plam"}, ${v.variant_number}-variant`, soni: varSoni[v.id] }))
        .sort((a, b) => a.nom.localeCompare(b.nom, "uz", { numeric: true })),
      mavzular: Object.entries(mavzu).map(([nom, soni]) => ({ nom, soni })).sort((a, b) => a.nom.localeCompare(b.nom, "uz")),
      oquvchilar: profiles.filter((p) => !p.is_admin).map((p) => ({ id: p.id, ism: p.full_name || String(p.email || "").split("@")[0] || "Ismsiz",
        plan: p.plan && (!p.plan_expires_at || ms(p.plan_expires_at) > now.getTime()) ? p.plan : "free", telegram: !ulangan.has(p.id) ? "yo'q" : ulangan.get(p.id) ? "ulangan" : "o'chirgan" }))
        .sort((a, b) => (a.plan === "free") - (b.plan === "free") || a.ism.localeCompare(b.ism, "uz")),
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
        javob_berilgan: Object.keys(t.javoblar || {}).length, topshirilgan_at: t.topshirilgan_at, telegram: !!t.tg_xabar_at }; }).sort((a, b) => a.ism.localeCompare(b.ism, "uz")) } };
  }

  if (body.amal === "yarat") {
    const t = tekshir(body, now);
    if (t.xato) return { status: 400, body: { error: t.xato } };
    const pool = must(await (t.variant_id ? db.from("questions").select(SAVOL_USTUN).eq("variant_id", t.variant_id) : db.from("questions").select(SAVOL_USTUN).in("topic", t.mavzular)).limit(5000)).filter(yaroqli);
    if (pool.length < t.soni) return { status: 400, body: { error: `Tanlangan ${t.variant_id ? "variantda" : "mavzularda"} faqat ${pool.length} ta yaroqli savol bor` } };
    const mavzu = (t.variant_id ? String(body.variant_nom || "Variant") : t.mavzular.join(", ")).slice(0, 300);
    const profiles = must(await db.from("profiles").select("id,full_name,is_admin").in("id", t.oquvchilar)).filter((p) => !p.is_admin);
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
      let r; try { r = await send(lead.tg_id, xabarMatni(v, p), tugma(site)); } catch { r = null; }
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
    let r; try { r = await send(lead.tg_id, eslatmaMatni(v, ps.find((p) => p.id === x.student_id), Object.keys(x.javoblar || {}).length), tugma(site)); } catch { r = null; }
    if (r?.ok) { yuborildi++; await db.from("vazifa_topshiriq").update({ eslatma_at: now.toISOString() }).eq("id", x.id); }
  }
  return { yuborildi };
}
