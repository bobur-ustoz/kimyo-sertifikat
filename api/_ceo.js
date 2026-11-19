// CEO: kun (yoki hafta) yakuni bo'yicha bitta hisobot. Barcha agentlar ishini umumiy navbatdan, o'quvchilar,
// sotuv va pulni bazadan yig'ib, ustozning admin chatiga yuboradi. Hech narsani o'zgartirmaydi.
//
// Ishga tushirish: kechki kron /api/keepalive?job=yangilik (20:00, Toshkent) ichida: har kuni kunlik,
// yakshanba kuni qo'shimcha haftalik. Qo'lda: /api/keepalive?job=ceo (&hafta=1).
// Kerakli env: SUPABASE_SERVICE_ROLE_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_CHAT_ID.

import { escapeHtml } from "./_telegram.js";
import { yoz, xulosa, JADVAL as NAVBAT } from "./_navbat.js";
import { moliya, moliyaQatorlar, som } from "./_hisobchi.js";

const DAY = 86400e3;
const ms = (t) => (t ? new Date(t).getTime() : 0);
export const tashkentKun = (d = new Date()) => new Date(d.getTime() + 5 * 3600e3).toISOString().slice(0, 10);
export const yakshanbami = (d = new Date()) => new Date(d.getTime() + 5 * 3600e3).getUTCDay() === 0;
const AGENT_NOM = { sotuv: "Sotuv boti", nazoratchi: "Nazoratchi", yangilik: "Yangiliklar", kanal: "Kanal postchisi", instagram: "Instagram agenti", platforma: "Platforma agenti", montaj: "Montaj agenti", kod: "Kod agenti", murabbiy: "O'quvchi murabbiyi", marketolog: "Marketolog" };

// Sof hisob: berilgan qatorlardan hisobot raqamlari. kun: davr uzunligi (1 yoki 7).
// Taqqoslash ("oldingi") faqat sanasi o'zgarmaydigan narsalar uchun: yangi hisob, yangi lid, tushum.
// Faol o'quvchilar soni taqqoslanmaydi: video_views.last_at har ko'rishda yangilanadi, o'tgan davr uchun ishonchsiz.
export function hisobla({ profiles = [], leads = [], messages = [], views = [], answers = [], guestViews = [], aiSavollar = [], purchases = [], posts = [], navbat = [], ochiq = [], haftaFaol = null, now = new Date(), kun = 1 }) {
  const t = now.getTime(), boshi = t - kun * DAY, oldingi = boshi - kun * DAY;
  const ichida = (x) => ms(x) > boshi && ms(x) <= t, avval = (x) => ms(x) > oldingi && ms(x) <= boshi;
  const talaba = profiles.filter((p) => !p.is_admin);

  const yangiLid = leads.filter((l) => ichida(l.created_at));
  const manba = {};
  for (const l of yangiLid) { const k = l.source || "to'g'ridan-to'g'ri"; manba[k] = (manba[k] || 0) + 1; }
  const faol = new Set([...views.filter((v) => ichida(v.last_at)).map((v) => v.student_id), ...answers.filter((a) => ichida(a.answered_at)).map((a) => a.student_id)]);
  const pul = moliya({ purchases, profiles, now, boshi: new Date(boshi) });
  const pulOldin = moliya({ purchases, profiles, now: new Date(boshi), boshi: new Date(oldingi) });

  // Pullik rejadagi, lekin 7 kundan beri hech narsa ochmagan o'quvchilar. haftaFaol berilmasa noma'lum (null), qator chiqmaydi.
  const pullik = talaba.filter((p) => p.plan && p.plan !== "free" && (!p.plan_expires_at || ms(p.plan_expires_at) > t));
  const pullik_faolsiz = haftaFaol ? pullik.filter((p) => !haftaFaol.includes(p.id)).length : null;

  const nv = navbat.filter((r) => ichida(r.created_at) && r.holat !== "bekor");      // bekor qilingan (sinov) yozuvlar sanalmaydi
  const x = xulosa(nv);
  return {
    kun, sana: tashkentKun(now), pullik_faolsiz, pullik_soni: pullik.length,
    oquvchilar: {
      yangi: talaba.filter((p) => ichida(p.created_at)).length, yangi_oldin: talaba.filter((p) => avval(p.created_at)).length,
      jami: talaba.length, faol: faol.size,
      mehmon: guestViews.filter((g) => ichida(g.last_at)).length,
      ai_savol: aiSavollar.filter((q) => ichida(q.created_at)).length,
      javoblar: answers.filter((a) => ichida(a.answered_at)).length,
    },
    sotuv: {
      lid: yangiLid.length, lid_oldin: leads.filter((l) => avval(l.created_at)).length, manba,
      xabar: messages.filter((m) => m.role === "user" && ichida(m.created_at)).length,
      uzatish: nv.filter((r) => r.agent === "sotuv" && r.tur === "savol").length,
      ulangan: leads.filter((l) => l.linked_user_id).length, jami: leads.length,
    },
    pul, tushum_oldin: pulOldin.davr.summa,
    kontent: {
      kanal: posts.filter((p) => p.holat === "yuborildi" && ichida(p.sent_at)).length,
      kanal_navbat: posts.filter((p) => p.holat === "tasdiqlangan").length,
      kanal_qoralama: posts.filter((p) => p.holat === "qoralama").length,
      instagram: nv.filter((r) => r.agent === "instagram" && r.tur === "ish" && /^Joylandi/.test(r.sarlavha)).length,
      platforma: nv.filter((r) => r.agent === "platforma" && r.tur === "ish" && /^Platformaga joylandi/.test(r.sarlavha)).length,
    },
    agentlar: x.agentlar,
    ustozga: ochiq.filter((r) => r.kimga === "ustoz"),
    kodga: ochiq.filter((r) => r.kimga === "kod").length,
    platformaga: ochiq.filter((r) => r.kimga === "platforma").length,
  };
}

const farq = (hozir, oldin) => oldin === hozir ? "" : ` (${hozir > oldin ? "+" : ""}${hozir - oldin} o'tgan haftaga nisbatan)`;

// Kuniga bitta Reels rejasi shu kundan boshlanadi (brend qo'llanmasi: 23-noyabr 2026).
export const REELS_BOSHI = "2026-11-23";

// CEO nimaga e'tibor qaratadi (agentlar/ceo.md dagi qoidalar). Har qator bitta fakt, baho va maslahatsiz.
export function etibor(h) {
  const q = [], m = h.pul;
  if (h.pullik_faolsiz) q.push(`${h.pullik_faolsiz} ta pullik o'quvchi 7 kundan beri kirmayapti (jami pullik: ${h.pullik_soni})`);
  if (m.kutmoqda.soni) q.push(`${m.kutmoqda.soni} ta to'lov tasdig'ingizni kutyapti (${som(m.kutmoqda.summa)})`);
  for (const x of m.tugaydi) q.push(`${x.ism}: ${x.plan} ${x.kun <= 0 ? "bugun tugaydi" : `${x.kun} kunda tugaydi`}`);
  for (const x of m.tugagan) q.push(`${x.ism}: ${x.plan} ${x.kun === 0 ? "bugun tugadi" : `${x.kun} kun oldin tugadi`}, uzaytirmagan`);
  for (const [a, n] of Object.entries(h.agentlar)) if (n.xato) q.push(`${AGENT_NOM[a] || a}: ${n.xato} ta xato`);
  if (h.kun === 1 && h.sana >= REELS_BOSHI && !h.kontent.instagram) q.push("Bugun Reels joylanmadi (reja: kuniga 1 ta)");
  if (h.kodga || h.platformaga) q.push(`Agentlar navbatida ochiq ish: kod agentida ${h.kodga} ta, platforma agentida ${h.platformaga} ta`);
  return q;
}

// Kunlik hisobot qisqa (ustoz 2026-11-19 da tanlagan): avval ustozdan kutilayotgan ishlar, keyin o'zgargani va e'tibor talab
// qiladigan narsalar. To'liq raqamlar yakshanba kungi haftalik hisobotda.
function formatKunlik(h, { sana }) {
  const e = escapeHtml, o = h.oquvchilar, k = h.kontent;
  const L = [`📊 <b>Kunlik hisobot</b>, ${e(sana)}`];
  const kut = [...h.ustozga.slice(0, 7).map((r) => `• ${e(r.sarlavha)}`), ...(h.ustozga.length > 7 ? [`... va yana ${h.ustozga.length - 7} ta`] : []),
    ...(k.kanal_qoralama ? [`• Kanalda ${k.kanal_qoralama} ta qoralama tasdig'ingizni kutyapti`] : [])];
  L.push("", ...(kut.length ? ["<b>Sizdan kutilmoqda</b>", ...kut] : ["✅ Sizdan hech narsa kutilmayapti"]));
  const kontent = [k.instagram && `Instagram ${k.instagram} ta reels`, k.kanal && `kanal ${k.kanal} ta post`, k.platforma && `platforma ${k.platforma} ta dars`].filter(Boolean).join(", ");
  L.push("", "<b>O'zgargani</b>",
    `Yangi o'quvchi: ${o.yangi} ta, faol: ${o.faol} ta, yangi lid: ${h.sotuv.lid} ta`,
    e(moliyaQatorlar(h.pul)[0]),
    ...(kontent ? [`Joylandi: ${kontent}`] : []));
  const et = etibor(h);
  if (et.length) L.push("", "<b>E'tibor</b>", ...et.map((x) => `• ${e(x)}`));
  L.push("", "To'liq raqamlar yakshanba kungi haftalik hisobotda.");
  return L.join("\n");
}

export function formatHisobot(h, { sana }) {
  if (h.kun === 1) return formatKunlik(h, { sana });
  const hafta = h.kun > 1, e = escapeHtml;
  const L = [hafta ? `📊 <b>Haftalik hisobot</b> (${e(sana)} gacha 7 kun)` : `📊 <b>Kunlik hisobot</b>, ${e(sana)}`];

  const o = h.oquvchilar;
  L.push("", "<b>O'quvchilar</b>",
    `Yangi hisob: ${o.yangi} ta${hafta ? farq(o.yangi, o.yangi_oldin) : ""} (jami ${o.jami})`,
    `Faol o'quvchi: ${o.faol} ta, yechilgan savol: ${o.javoblar}, AI yordamchiga savol: ${o.ai_savol}`,
    `Ro'yxatdan o'tmagan mehmonlar ko'rgan video: ${o.mehmon} ta`);

  const s = h.sotuv, manba = Object.entries(s.manba).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${e(k)} ${v}`).join(", ");
  L.push("", "<b>Sotuv boti</b>",
    `Yangi lid: ${s.lid} ta${hafta ? farq(s.lid, s.lid_oldin) : ""}${manba ? ` (${manba})` : ""}`,
    `Kelgan xabar: ${s.xabar} ta, sizga uzatilgan: ${s.uzatish} ta`);

  L.push("", "<b>Pul</b>", ...moliyaQatorlar(h.pul, { haftalik: hafta }).map(e));
  if (hafta && h.tushum_oldin !== h.pul.davr.summa) L.push(`O'tgan hafta tushum: ${e(Math.round(h.tushum_oldin).toLocaleString("ru-RU").replace(/ |,/g, " "))} so'm`);

  const k = h.kontent;
  L.push("", "<b>Kontent</b>",
    `Instagram: ${k.instagram} ta reels, kanal: ${k.kanal} ta post, platforma: ${k.platforma} ta dars`,
    ...(k.kanal_navbat || k.kanal_qoralama ? [`Kanal navbati: ${k.kanal_navbat} ta tasdiqlangan, ${k.kanal_qoralama} ta qoralama tasdig'ingizni kutyapti`] : []));

  const ag = Object.entries(h.agentlar).filter(([, n]) => n.ish || n.xato || n.savol);
  if (ag.length) L.push("", "<b>Agentlar ishi</b>", ...ag.map(([a, n]) => `${e(AGENT_NOM[a] || a)}: ${[n.ish && `${n.ish} ish`, n.savol && `${n.savol} savol`, n.xato && `${n.xato} xato`].filter(Boolean).join(", ")}`));

  if (h.ustozga.length || h.kodga || h.platformaga) {
    L.push("", `<b>Sizdan kutilmoqda (${h.ustozga.length} ta)</b>`, ...h.ustozga.slice(0, 7).map((r) => `• ${e(r.sarlavha)}`), ...(h.ustozga.length > 7 ? [`... va yana ${h.ustozga.length - 7} ta`] : []));
    if (h.kodga || h.platformaga) L.push(`Agentlar navbatida: kod agentida ${h.kodga} ta, platforma agentida ${h.platformaga} ta ochiq ish`);
  } else L.push("", "✅ Ochiq ish yo'q");
  const et = etibor(h);
  if (et.length) L.push("", "<b>E'tibor</b>", ...et.map((x) => `• ${e(x)}`));
  return L.join("\n");
}

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
// Hamma bazada bo'lmasligi mumkin bo'lgan jadvallar: ularsiz ham hisobot chiqadi.
const optional = ({ data, error }) => { if (error) console.warn("ceo: jadval o'tkazib yuborildi:", error.message); return error ? [] : data || []; };

export async function collectCeo(db, { now = new Date(), kun = 1 } = {}) {
  const dan = new Date(now.getTime() - 2 * kun * DAY).toISOString();     // joriy va oldingi davr
  const hafta7 = new Date(now.getTime() - 7 * DAY).toISOString();
  const [profiles, purchases, leads, messages, views, answers, guestViews, aiSavollar, posts, navbat, ochiq, v7, a7] = await Promise.all([
    db.from("profiles").select("id,full_name,email,plan,plan_expires_at,is_admin,created_at").limit(10000).then(must),
    db.from("variant_purchases").select("status,amount,paid_at,created_at,plan_id,live_lesson_id").limit(10000).then(must),
    db.from("sotuv_leads").select("created_at,source,linked_user_id").limit(10000).then(optional),
    db.from("sotuv_messages").select("role,created_at").gte("created_at", dan).limit(10000).then(optional),
    db.from("video_views").select("student_id,last_at").gte("last_at", dan).limit(10000).then(optional),
    db.from("answers").select("student_id,answered_at").gte("answered_at", dan).limit(10000).then(optional),
    db.from("guest_views").select("last_at").gte("last_at", dan).limit(10000).then(optional),
    db.from("video_questions").select("created_at").gte("created_at", dan).limit(10000).then(optional),
    db.from("kanal_postlar").select("holat,sent_at").limit(1000).then(optional),
    db.from(NAVBAT).select("agent,tur,holat,sarlavha,kimga,created_at").gte("created_at", dan).limit(5000).then(optional),
    db.from(NAVBAT).select("sarlavha,kimga,tur,created_at").in("holat", ["yangi", "jarayonda"]).in("tur", ["xato", "savol"]).order("created_at").limit(1000).then(optional),
    db.from("video_views").select("student_id").gte("last_at", hafta7).limit(10000).then(optional),
    db.from("answers").select("student_id").gte("answered_at", hafta7).limit(10000).then(optional),
  ]);
  const haftaFaol = [...new Set([...v7, ...a7].map((r) => r.student_id))];
  return hisobla({ profiles, purchases, leads, messages, views, answers, guestViews, aiSavollar, posts, navbat, ochiq, haftaFaol, now, kun });
}

// Hisobotni yuboradi. Navbatdagi kalit orqali kuniga (haftasiga) bir marta: kron ikki marta ishlasa ikkinchisi yubormaydi.
export async function runCeo(db, notify, { now = new Date(), hafta = false } = {}) {
  const sana = tashkentKun(now), kun = hafta ? 7 : 1;
  const h = await collectCeo(db, { now, kun });
  const band = await yoz(db, { agent: "ceo", tur: "hisobot", sarlavha: `${hafta ? "Haftalik" : "Kunlik"} hisobot: ${sana}`,
    tafsilot: { yangi_hisob: h.oquvchilar.yangi, faol: h.oquvchilar.faol, lid: h.sotuv.lid, tushum: h.pul.davr.summa, ustozga: h.ustozga.length }, kalit: `ceo:${hafta ? "hafta" : "kun"}:${sana}` });
  if (band.takror) return { sent: false, sabab: "bugungi hisobot yuborilgan" };
  await notify(formatHisobot(h, { sana }));
  return { sent: true, hafta };
}
