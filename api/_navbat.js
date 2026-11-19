// Umumiy navbat: agentlar qilgan ishini, topgan xatosini va ustozga savolini agent_navbat jadvaliga yozadi.
// CEO hisoboti shu yozuvlardan yig'iladi; kod agenti o'ziga atalgan (kimga: "kod") xatolarni shu yerdan oladi.
//
// Alohida funksiya emas (Vercel Hobby'da funksiya soni cheklangan): serverdagi agentlar (sotuv, nazoratchi,
// yangilik) shu faylni import qiladi, kompyuterdagi agentlar (montaj, instagram ...) agentlar/navbat.mjs orqali yozadi.
//
// Muhim: yoz() hech qachon xato otmaydi. Navbatga yozib bo'lmasa ham agent o'z ishini tugatishi kerak.

export const TURLAR = ["ish", "xato", "savol", "hisobot"];
export const HOLATLAR = ["yangi", "jarayonda", "bajarildi", "bekor"];
export const JADVAL = "agent_navbat";
const OCHIQ = ["yangi", "jarayonda"];
const DAY = 86400e3;

const qisqa = (s, n) => String(s ?? "").trim().slice(0, n);

// Yozuvni tekshirib, jadval qatoriga aylantiradi. Noto'g'ri bo'lsa Error otadi.
// Holat ko'rsatilmasa: bajarilgan ish va hisobot "bajarildi", xato va savol "yangi" (kimdir qarashi kerak).
export function tayyorla({ agent, tur, sarlavha, tafsilot, kimga, kalit, holat } = {}) {
  const a = qisqa(agent, 40).toLowerCase(), s = qisqa(sarlavha, 300);
  if (a.length < 2) throw new Error("agent nomi kerak");
  if (!TURLAR.includes(tur)) throw new Error(`tur noto'g'ri: ${tur}`);
  if (!s) throw new Error("sarlavha kerak");
  const h = holat ?? (tur === "ish" || tur === "hisobot" ? "bajarildi" : "yangi");
  if (!HOLATLAR.includes(h)) throw new Error(`holat noto'g'ri: ${h}`);
  const k = kimga ? qisqa(kimga, 40).toLowerCase() : null;
  if (k !== null && k.length < 2) throw new Error("kimga noto'g'ri");
  const t = tafsilot && typeof tafsilot === "object" && !Array.isArray(tafsilot) ? tafsilot : tafsilot == null ? {} : { qiymat: tafsilot };
  return { agent: a, tur, holat: h, sarlavha: s, tafsilot: t, kimga: k, kalit: kalit ? qisqa(kalit, 200) : null };
}

// Navbatga bitta yozuv qo'shadi. `kalit` berilsa, shu kalitli yozuv allaqachon bo'lsa qaytadan yozilmaydi
// (masalan "nazorat:2026-11-18": cron ikki marta ishlasa ham kuniga bitta yozuv).
// -> { ok: true, id } | { ok: true, takror: true } | { ok: false, error }
export async function yoz(db, yozuv) {
  try {
    const row = tayyorla(yozuv);
    const q = row.kalit
      ? db.from(JADVAL).upsert(row, { onConflict: "kalit", ignoreDuplicates: true })
      : db.from(JADVAL).insert(row);
    const { data, error } = await q.select("id");
    if (error) throw new Error(error.message);
    return data?.length ? { ok: true, id: data[0].id } : { ok: true, takror: true };
  } catch (e) {
    console.error("navbat: yozilmadi:", e.message);
    return { ok: false, error: e.message };
  }
}

// Yozuv holatini o'zgartiradi (masalan kod agenti xatoni oldi: "jarayonda", tuzatdi: "bajarildi").
// `izoh` tafsilotga qo'shiladi. -> { ok } | { ok: false, error }
export async function holatQoy(db, id, holat, izoh) {
  try {
    if (!HOLATLAR.includes(holat)) throw new Error(`holat noto'g'ri: ${holat}`);
    const patch = { holat, updated_at: new Date().toISOString() };
    if (izoh) {
      const { data: old, error: e1 } = await db.from(JADVAL).select("tafsilot").eq("id", id).maybeSingle();
      if (e1) throw new Error(e1.message);
      if (!old) throw new Error(`yozuv topilmadi: ${id}`);
      patch.tafsilot = { ...(old.tafsilot || {}), izoh: qisqa(izoh, 500) };
    }
    const { data, error } = await db.from(JADVAL).update(patch).eq("id", id).select("id");
    if (error) throw new Error(error.message);
    if (!data?.length) throw new Error(`yozuv topilmadi: ${id}`);
    return { ok: true };
  } catch (e) {
    console.error("navbat: holat o'zgarmadi:", e.message);
    return { ok: false, error: e.message };
  }
}

// Yozuvlarni o'qiydi (yangisi birinchi). `ochiq: true` bo'lsa faqat hali bajarilmaganlar, sanaga qaramay.
export async function oqi(db, { kun = 1, kimga, agent, tur, ochiq = false, limit = 200, now = new Date() } = {}) {
  let q = db.from(JADVAL).select("*").order("created_at", { ascending: false }).limit(limit);
  if (ochiq) q = q.in("holat", OCHIQ);
  else q = q.gte("created_at", new Date(now.getTime() - kun * DAY).toISOString());
  if (kimga) q = q.eq("kimga", kimga);
  if (agent) q = q.eq("agent", agent);
  if (tur) q = q.eq("tur", tur);
  const { data, error } = await q;
  if (error) throw new Error(error.message);
  return data || [];
}

// Hisobot uchun: yozuvlarni agent va tur bo'yicha sanaydi, hali ochiq xato va savollarni alohida beradi.
export function xulosa(rows) {
  const agentlar = {};
  for (const r of rows) {
    const a = (agentlar[r.agent] ||= { ish: 0, xato: 0, savol: 0, hisobot: 0 });
    if (r.tur in a) a[r.tur]++;
  }
  const ochiq = rows.filter((r) => (r.tur === "xato" || r.tur === "savol") && OCHIQ.includes(r.holat));
  return { jami: rows.length, agentlar, ochiq };
}
