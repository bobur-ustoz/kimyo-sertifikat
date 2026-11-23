// Shaxsiy reja: murabbiy har bir pullik o'quvchini mavzular ketma-ketligida yuritadi (ustoz qarori, 2026-11-23).
//
// Ketma-ketlik bazadagi mavzular tartibi (topics.sort_order); ustoz mavzularni to'ldirib boradi. Har mavzuda uch bosqich:
//   dars     -> o'quvchi mavzu darsini ko'radi (video_views). Ko'rmasa, bir necha kunda bir muloyim eslatma.
//   vazifa   -> dars ko'rilgach murabbiy shu mavzuning analoglaridan uyga vazifa yuboradi (botga PDF bo'lib boradi).
//   imtihon  -> vazifa topshirilgach mavzu imtihoni (qolgan analoglardan, saytda ishlanadi).
// Imtihon topshirilgach keyingi mavzu boshlanadi. Mavzuda analog savol bo'lmasa, dars ko'rilgach keyingisiga o'tiladi
// va ustozga bir marta "bu mavzuda savol yo'q" deb yoziladi.
//
// Kirish testi (ustoz, 2026-11-22: "premium kirgan o'quvchi test ishlaydi, qaysi mavzulardan muammo borligi aniqlanadi,
// shunga qarab mavzular rejasi beriladi"): reja boshlanishidan oldin o'quvchiga savoli bor har mavzudan KIRISH_SAVOL tadan
// savol beriladi (saytda ishlanadi). Mavzudagi savollarning hammasiga to'g'ri javob bergan bo'lsa, o'sha mavzu "biladi" deb
// rejadan chiqariladi; qolganlari va savoli yo'q (tekshirib bo'lmagan) mavzular rejada qoladi. Daraja (oson/qiyin) hozircha yo'q.
// Hech bir mavzuda savol bo'lmasa kirish testi berilmaydi, reja hamma mavzudan tuziladi.
//
// Ishga tushirish: ertalabki kron (api/keepalive.js?job=nazorat) ichida, kuniga bir marta. Bir ishga tushishda har o'quvchi
// ko'pi bilan bitta qadam tashlaydi (kuniga bitta xabar). Jadval: oquvchi_reja (supabase/migrations/20261123010000_oquvchi_reja.sql).

import { yoz } from "./_navbat.js";
import { tg } from "./_telegram.js";
import { tayinla, havza, tanla, muddatHisob } from "./_vazifa.js";

export const VAZIFA_SONI = 10, IMTIHON_SONI = 10;   // ko'pi bilan; mavzuda savol kam bo'lsa borini ikkiga bo'ladi
export const MIN_SAVOL = 3;                         // shundan kam savol bilan vazifa yoki imtihon berilmaydi
export const VAZIFA_KUN = 2, IMTIHON_KUN = 2;       // muddat
export const KIRISH_SAVOL = 3, KIRISH_MAX = 30;      // kirish testi: har mavzudan shuncha savol, jami ko'pi bilan
export const KIRISH_KUN = 3;                        // kirish testining muddati
export const ESLATMA_KUN = 2;                       // dars shuncha kun ko'rilmasa eslatma, keyin yana shuncha kunda
const DAY = 86400e3;
const ms = (t) => (t ? new Date(t).getTime() : 0);
const ism = (p) => String(p?.full_name || "").trim().split(/\s+/)[0] || "";
const STOP = "\n\nBunday xabarlar kerak bo'lmasa, /stop deb yozing.";
const salom = (p) => (ism(p) ? `Assalomu alaykum, ${ism(p)}!` : "Assalomu alaykum!");

// Murabbiy ohangida (agentlar/murabbiy.md): iliq, majburlamaydi, va'da bermaydi.
export const XABAR = {
  kirishdan: (p, m, jami, bilgan) => `${salom(p)} Kirish testi tekshirildi. ${bilgan ? `${bilgan} ta mavzuni bilar ekansiz, ularni rejaga qo'shmadim. ` : ""}Rejangizda ${jami} ta mavzu. Birinchisi: "${m.name}". Darsni ko'rib chiqing, keyin shu mavzudan uyga vazifa yuboraman.${STOP}`,
  boshlash: (p, m, jami) => `${salom(p)} Siz uchun o'qish rejasi tayyor: ${jami} ta mavzu, ketma-ket. Birinchisi: "${m.name}". Darsni ko'rib chiqing, keyin shu mavzudan uyga vazifa yuboraman.${STOP}`,
  keyingi: (p, m, tartib, jami) => `${salom(p)} Barakalla, mavzu tugadi. Keyingisi: "${m.name}" (${tartib}/${jami}). Darsni ko'rib chiqing, keyin uyga vazifa yuboraman.${STOP}`,
  eslatma: (p, m) => `${salom(p)} Rejangizda "${m.name}" mavzusining darsi turibdi. Vaqt topsangiz ko'rib chiqing, keyin uyga vazifaga o'tamiz. Tushunmagan joy bo'lsa shu yerga yozing.${STOP}`,
  tugadi: (p) => `${salom(p)} Rejadagi hamma mavzularni tugatdingiz, barakalla! Yangi mavzu qo'shilganda xabar beraman.${STOP}`,
};

// Mavzudagi analoglardan vazifa va imtihonga nechta savol tushishi. -> { vazifa, imtihon }
export function taqsim(n) {
  if (n < MIN_SAVOL) return { vazifa: 0, imtihon: 0 };
  if (n >= VAZIFA_SONI + IMTIHON_SONI) return { vazifa: VAZIFA_SONI, imtihon: IMTIHON_SONI };
  if (n < MIN_SAVOL * 2) return { vazifa: n, imtihon: 0 };               // ikkiga bo'lishga yetmaydi: faqat vazifa
  const vazifa = Math.min(VAZIFA_SONI, Math.ceil(n / 2));
  return { vazifa, imtihon: Math.min(IMTIHON_SONI, n - vazifa) };
}

// Kirish testiga savollar: savoli yetarli har mavzudan KIRISH_SAVOL tadan, tartib bo'yicha, jami KIRISH_MAX gacha.
export function kirishSavollar(mavzular, pool, rnd = Math.random) {
  const out = [];
  for (const m of mavzular) {
    const h = pool.filter((q) => q.topic_id === m.id);
    if (h.length >= KIRISH_SAVOL && out.length + KIRISH_SAVOL <= KIRISH_MAX) out.push(...tanla(h, KIRISH_SAVOL, rnd));
  }
  return out;
}
// Kirish testi natijasi: mavzu bo'yicha [to'g'ri, jami] va bilgan mavzular (hamma savoliga to'g'ri javob).
export function kirishNatija(savollar, javoblar = {}) {
  const natija = {};
  for (const q of savollar) { const n = (natija[q.topic_id] ||= [0, 0]); n[1]++; if (javoblar[q.id] === q.correct_option) n[0]++; }
  return { natija, bilgan: Object.keys(natija).filter((id) => natija[id][0] === natija[id][1]) };
}

// Rejaga kiradigan mavzular: dars videosi borlari, tartib bo'yicha.
export const rejaMavzular = (topics) => topics.filter((t) => t.bunny_video_id).sort((a, b) => (a.sort_order ?? 0) - (b.sort_order ?? 0) || String(a.name).localeCompare(String(b.name)));
// Tugatilmagan birinchi mavzu (yo'q bo'lsa null).
export const keyingiMavzu = (mavzular, tugagan) => mavzular.find((m) => !(tugagan || []).includes(m.id)) || null;

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
const optional = ({ data, error }) => (error ? [] : data || []);
const sayt = () => process.env.SITE_URL || "https://kimyo-sertifikat.vercel.app";
const botSend = () => { const token = process.env.SOTUV_BOT_TOKEN; return token ? (chat_id, text, reply_markup) => tg("sendMessage", { chat_id, text, reply_markup }, { token }) : null; };

// Ertalabki ish. -> { oquvchilar, kirish, boshlandi, vazifa, imtihon, keyingi, eslatma, tugadi }
export async function rejaIsh(db, { now = new Date(), send = botSend(), rnd = Math.random, log = (y) => yoz(db, y), site = sayt(), kirish = true, ...dep } = {}) {
  const t = now.getTime(), hisob = { oquvchilar: 0, kirish: 0, boshlandi: 0, vazifa: 0, imtihon: 0, keyingi: 0, eslatma: 0, tugadi: 0 };
  const profiles = must(await db.from("profiles").select("id,full_name,plan,plan_expires_at,is_admin").neq("plan", "free")).filter((p) => !p.is_admin && (!p.plan_expires_at || ms(p.plan_expires_at) > t));
  if (!profiles.length) return hisob;
  const ids = profiles.map((p) => p.id);
  const [topics, rows, leads, views, pool] = await Promise.all([
    db.from("topics").select("id,name,sort_order,bunny_video_id").then(must),
    db.from("oquvchi_reja").select("*").in("student_id", ids).then(must),
    db.from("sotuv_leads").select("tg_id,linked_user_id,remind").in("linked_user_id", ids).then(optional),
    db.from("video_views").select("student_id,kind,ref_id").eq("kind", "topic").in("student_id", ids).limit(20000).then(must),
    havza(db),
  ]);
  const mavzular = rejaMavzular(topics);
  if (!mavzular.length) return hisob;
  hisob.oquvchilar = profiles.length;
  const analog = (topicId) => pool.filter((q) => q.topic_id === topicId);
  const tugma = { inline_keyboard: [[{ text: "Darsni ochish", url: `${site}/#mavzular` }]] };

  for (const p of profiles) {
    const lead = leads.find((l) => l.linked_user_id === p.id);
    const yoz_ = async (text) => { if (send && lead?.remind) { try { await send(lead.tg_id, text, tugma); } catch { /* xabar ketmasa ham reja yuradi */ } } };
    const row = rows.find((r) => r.student_id === p.id);
    const saqla = (patch) => db.from("oquvchi_reja").update({ ...patch, updated_at: now.toISOString() }).eq("student_id", p.id).select("student_id").then(must);
    const tartib = (m) => mavzular.findIndex((x) => x.id === m.id) + 1;

    // Yangi o'quvchi: avval kirish testi (savol bo'lsa), bo'lmasa birinchi mavzu.
    if (!row) {
      const ks = kirish ? kirishSavollar(mavzular, pool, rnd) : [];
      if (ks.length) {
        const r = await tayinla(db, { tur: "imtihon", nom: "Kirish testi", mavzu: "Reja tuzish uchun", tanlangan: ks, muddat: muddatHisob(KIRISH_KUN, now), profiles: [p], reja: true }, { now, send, log, site, ...dep });
        must(await db.from("oquvchi_reja").insert({ student_id: p.id, topic_id: null, bosqich: "kirish", vazifa_id: r.id, tugagan: [], bilgan: [], boshlangan_at: now.toISOString(), updated_at: now.toISOString() }).select("student_id"));
        hisob.kirish++; continue;
      }
      const m = mavzular[0];
      must(await db.from("oquvchi_reja").insert({ student_id: p.id, topic_id: m.id, bosqich: "dars", tugagan: [], boshlangan_at: now.toISOString(), updated_at: now.toISOString() }).select("student_id"));
      await yoz_(XABAR.boshlash(p, m, mavzular.length)); hisob.boshlandi++; continue;
    }
    // Mavzuni tugatib, keyingisiga o'tish.
    const otish = async () => {
      const tugagan = [...new Set([...(row.tugagan || []), row.topic_id].filter(Boolean))];
      const m = keyingiMavzu(mavzular, tugagan);
      if (!m) { await saqla({ topic_id: null, bosqich: "tugadi", vazifa_id: null, tugagan }); await yoz_(XABAR.tugadi(p)); hisob.tugadi++; return; }
      await saqla({ topic_id: m.id, bosqich: "dars", vazifa_id: null, tugagan, boshlangan_at: now.toISOString(), eslatma_at: null });
      await yoz_(XABAR.keyingi(p, m, tartib(m), mavzular.length)); hisob.keyingi++;
    };
    // Kirish testi topshirilgach: bilgan mavzular rejadan chiqadi, qolganidan birinchisi boshlanadi.
    if (row.bosqich === "kirish") {
      const top = row.vazifa_id ? must(await db.from("vazifa_topshiriq").select("holat,javoblar").eq("vazifa_id", row.vazifa_id).eq("student_id", p.id))[0] : null;
      if (top && top.holat !== "topshirilgan") continue;       // hali ishlanmoqda (muddat eslatmasini vazifaEslatma yuboradi)
      const idlar = top ? must(await db.from("vazifalar").select("savollar").eq("id", row.vazifa_id))[0]?.savollar || [] : [];
      const { natija, bilgan } = kirishNatija(pool.filter((q) => idlar.includes(q.id)), top?.javoblar || {});
      const m = keyingiMavzu(mavzular, bilgan);
      if (!m) { await saqla({ topic_id: null, bosqich: "tugadi", vazifa_id: null, tugagan: bilgan, bilgan, kirish: natija }); await yoz_(XABAR.tugadi(p)); hisob.tugadi++; continue; }
      await saqla({ topic_id: m.id, bosqich: "dars", vazifa_id: null, tugagan: bilgan, bilgan, kirish: natija, boshlangan_at: now.toISOString(), eslatma_at: null });
      await yoz_(XABAR.kirishdan(p, m, mavzular.length - bilgan.length, bilgan.length)); hisob.boshlandi++; continue;
    }
    // Reja tugagan, lekin ustoz yangi mavzu qo'shgan: davom etadi.
    if (row.bosqich === "tugadi") { if (keyingiMavzu(mavzular, row.tugagan)) await otish(); continue; }
    const m = mavzular.find((x) => x.id === row.topic_id);
    if (!m) { await otish(); continue; }                        // mavzu o'chirilgan yoki videosi olib tashlangan
    const hovuz = analog(m.id), bol = taqsim(hovuz.length);
    const top = row.vazifa_id ? must(await db.from("vazifa_topshiriq").select("holat").eq("vazifa_id", row.vazifa_id).eq("student_id", p.id))[0] : null;

    if (row.bosqich === "dars") {
      const korgan = views.some((v) => v.student_id === p.id && v.ref_id === m.id);
      if (!korgan) {
        const oxirgi = Math.max(ms(row.eslatma_at), ms(row.boshlangan_at));
        if (t - oxirgi >= ESLATMA_KUN * DAY) { await saqla({ eslatma_at: now.toISOString() }); await yoz_(XABAR.eslatma(p, m)); hisob.eslatma++; }
        continue;
      }
      if (!bol.vazifa) {                                        // mavzuda savol yo'q: ustozga bir marta aytiladi, o'quvchi kutib qolmaydi
        await log({ agent: "murabbiy", tur: "savol", kimga: "ustoz", kalit: `reja-savolsiz:${m.id}`, sarlavha: `"${m.name}" mavzusida analog savol yo'q: rejadagi o'quvchilar uyga vazifasiz keyingi mavzuga o'tyapti`, tafsilot: { topic_id: m.id, analoglar: hovuz.length } });
        await otish(); continue;
      }
      const r = await tayinla(db, { tur: "uyga", nom: `${m.name}: uyga vazifa`, mavzu: m.name, tanlangan: tanla(hovuz, bol.vazifa, rnd), muddat: muddatHisob(VAZIFA_KUN, now), profiles: [p], reja: true }, { now, send, log, site, ...dep });
      await saqla({ bosqich: "vazifa", vazifa_id: r.id }); hisob.vazifa++; continue;
    }
    if (row.bosqich === "vazifa") {
      if (top && top.holat !== "topshirilgan") continue;       // vazifa hali ishlanmoqda (muddat eslatmasini vazifaEslatma yuboradi)
      const berilgan = row.vazifa_id ? must(await db.from("vazifalar").select("savollar").eq("id", row.vazifa_id))[0]?.savollar || [] : [];
      const qolgan = hovuz.filter((q) => !berilgan.includes(q.id));
      if (!bol.imtihon || qolgan.length < MIN_SAVOL) { await otish(); continue; }
      const r = await tayinla(db, { tur: "imtihon", nom: `${m.name}: imtihon`, mavzu: m.name, tanlangan: tanla(qolgan, bol.imtihon, rnd), muddat: muddatHisob(IMTIHON_KUN, now), profiles: [p], reja: true }, { now, send, log, site, ...dep });
      await saqla({ bosqich: "imtihon", vazifa_id: r.id }); hisob.imtihon++; continue;
    }
    if (row.bosqich === "imtihon") { if (!top || top.holat === "topshirilgan") await otish(); continue; }
  }
  return hisob;
}

// ---------------------------------------------------------------- ko'rinishlar

// O'quvchining rejasi: mavzular va holati. -> { mavzular: [{ nom, holat: "tugadi" | "hozir" | "kutmoqda", bosqich? }] } | { yoq: true }
export async function rejaOquvchi(db, userId) {
  const row = optional(await db.from("oquvchi_reja").select("*").eq("student_id", userId))[0];
  if (!row) return { yoq: true };
  if (row.bosqich === "kirish") return { kirish: true };
  const mavzular = rejaMavzular(must(await db.from("topics").select("id,name,sort_order,bunny_video_id")));
  return { mavzular: mavzular.map((m) => ({ nom: m.name, holat: (row.bilgan || []).includes(m.id) ? "biladi" : (row.tugagan || []).includes(m.id) ? "tugadi" : m.id === row.topic_id ? "hozir" : "kutmoqda", ...(m.id === row.topic_id ? { bosqich: row.bosqich } : {}) })) };
}

// Ustoz uchun: mavzular ketma-ketligi (nechta analog bor) va har o'quvchi qayerda. Jadval hali yo'q bo'lsa { yoq: true }.
export async function rejaAdmin(db, { now = new Date() } = {}) {
  const rr = await db.from("oquvchi_reja").select("*");
  if (rr.error) return { yoq: true };
  const [topics, pool] = await Promise.all([db.from("topics").select("id,name,sort_order,bunny_video_id").then(must), havza(db)]);
  const mavzular = rejaMavzular(topics), rows = rr.data || [];
  const ps = rows.length ? must(await db.from("profiles").select("id,full_name,email").in("id", rows.map((r) => r.student_id))) : [];
  return {
    mavzular: mavzular.map((m, i) => { const n = pool.filter((q) => q.topic_id === m.id).length, b = taqsim(n); return { tartib: i + 1, nom: m.name, analoglar: n, vazifa: b.vazifa, imtihon: b.imtihon, oquvchilar: rows.filter((r) => r.topic_id === m.id).length }; }),
    oquvchilar: rows.map((r) => { const p = ps.find((x) => x.id === r.student_id), m = mavzular.find((x) => x.id === r.topic_id);
      return { ism: p?.full_name || String(p?.email || "").split("@")[0] || "Ismsiz", mavzu: m?.name || null, tartib: m ? mavzular.indexOf(m) + 1 : null, bosqich: r.bosqich, tugagan: (r.tugagan || []).length - (r.bilgan || []).length, bilgan: (r.bilgan || []).length, qoldi: mavzular.filter((x) => !(r.tugagan || []).includes(x.id)).length, kun: Math.floor((now.getTime() - ms(r.boshlangan_at)) / DAY) }; })
      .sort((a, b) => a.ism.localeCompare(b.ism, "uz")),
    jami: mavzular.length,
  };
}
