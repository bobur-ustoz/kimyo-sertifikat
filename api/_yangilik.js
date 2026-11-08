// Kunlik yangilik xabari: kun davomida yuklangan mavzu, misol va variantlar bitta xabarga jamlanib,
// Telegramni ulagan Premium o'quvchilarga yuboriladi. Yangilik bo'lmasa hech narsa yuborilmaydi.
//
// Ishga tushirish: vercel.json cron -> /api/keepalive?job=yangilik (funksiya soni cheklangani uchun
// keepalive.js ichidan chaqiriladi). Kerakli env: SUPABASE_SERVICE_ROLE_KEY, SOTUV_BOT_TOKEN.

import { escapeHtml } from "./_telegram.js";

const DAY = 86400e3;
const uniq = (a) => [...new Set(a)];

// topics: yangi mavzular { id, name }; examples: yangi misollar { topic_id }; topicNames: id -> nom;
// variants: yangi variantlar { variant_number }. Qaytaradi: [{ text }] (bo'sh bo'lsa yangilik yo'q).
export function buildItems({ topics, examples, topicNames, variants }) {
  const items = [];
  const newIds = new Set(topics.map((t) => t.id));
  const count = {};
  for (const e of examples) count[e.topic_id] = (count[e.topic_id] || 0) + 1;
  for (const t of topics) {
    const n = count[t.id];
    items.push({ text: `${t.name} — yangi mavzu${n ? `, ${n} ta misol videosi` : ""}` });
  }
  for (const [id, n] of Object.entries(count)) {
    if (newIds.has(id)) continue;
    items.push({ text: `${topicNames[id] || "Mavzu"}: ${n} ta yangi misol videosi` });
  }
  for (const n of uniq(variants.map((v) => v.variant_number)).sort((a, b) => a - b)) items.push({ text: `Variant ${n} — yangi` });
  return items;
}

export function buildMessage(items) {
  return `📚 <b>Bugungi yangiliklar</b>\n\n${items.map((i) => `• ${escapeHtml(i.text)}`).join("\n")}\n\nKo'rish uchun pastdagi tugmani bosing.`;
}

// Premium: plan "premium" va muddati tugamagan.
export const isActivePremium = (p, now = new Date()) => p.plan === "premium" && (!p.plan_expires_at || new Date(p.plan_expires_at) > now);

// send(chat_id, text, button) -> { ok, error_code }. dryRun: hech narsa yuborilmaydi va yozilmaydi.
export async function runYangilik(db, send, site, { now = new Date(), dryRun = false } = {}) {
  const { data: last } = await db.from("digest_runs").select("run_at").order("run_at", { ascending: false }).limit(1);
  const since = last?.[0]?.run_at || new Date(now.getTime() - DAY).toISOString();

  const [t, e, v] = await Promise.all([
    db.from("topics").select("id, name").gt("created_at", since),
    db.from("topic_examples").select("topic_id").gt("created_at", since),
    db.from("variants").select("variant_number").gt("created_at", since),
  ]);
  const err = t.error || e.error || v.error;
  if (err) throw new Error(err.message);
  const ids = uniq(e.data.map((x) => x.topic_id));
  const names = {};
  if (ids.length) {
    const { data } = await db.from("topics").select("id, name").in("id", ids);
    for (const r of data || []) names[r.id] = r.name;
  }
  const items = buildItems({ topics: t.data, examples: e.data, topicNames: names, variants: v.data });
  if (!items.length) return { sent: 0, failed: 0, items: 0, since };
  const text = buildMessage(items);
  if (dryRun) return { sent: 0, failed: 0, items: items.length, since, text };

  // Telegramni ulagan, to'xtatmagan, hozir Premium bo'lgan o'quvchilar.
  const { data: leads } = await db.from("sotuv_leads").select("tg_id, linked_user_id").not("linked_user_id", "is", null).eq("remind", true).neq("stage", "stopped");
  const uids = (leads || []).map((l) => l.linked_user_id);
  const { data: profs } = uids.length ? await db.from("profiles").select("id, plan, plan_expires_at").in("id", uids) : { data: [] };
  const ok = new Set((profs || []).filter((p) => isActivePremium(p, now)).map((p) => p.id));
  let sent = 0, failed = 0;
  for (const l of (leads || []).filter((l) => ok.has(l.linked_user_id))) {
    const r = await send(l.tg_id, text, { text: "📖 Saytni ochish", url: site });
    if (r?.ok) sent++;
    else {
      failed++;
      // Bot bloklangan bo'lsa qayta urinmaymiz.
      if (r?.error_code === 403) await db.from("sotuv_leads").update({ remind: false }).eq("tg_id", l.tg_id);
    }
    await new Promise((res) => setTimeout(res, 50));
  }
  await db.from("digest_runs").insert({ items, sent, failed });
  return { sent, failed, items: items.length, since };
}
