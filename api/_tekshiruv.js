// Nazoratchi: platformadagi kamchiliklarni qidiradi (kontent bo'shliqlari, kutib qolgan to'lovlar, buzilgan videolar,
// bazada yetishmayotgan jadval va ustunlar) va umumiy navbatga yozadi. Hech narsani o'zi tuzatmaydi.
//
// Ishga tushirish: ertalabki kron /api/keepalive?job=nazorat (09:00, Toshkent) ichida, o'quvchilar hisobotidan keyin.
// Kerakli env: SUPABASE_SERVICE_ROLE_KEY; Bunny tekshiruvi uchun BUNNY_API_KEY va BUNNY_LIBRARY_ID (bo'lmasa o'tkazib yuboriladi).
//
// Har kamchilikning doimiy `kod`i bor ("mavzu_matnsiz:<id>"). Shu kodli ochiq yozuv navbatda bo'lsa qayta yozilmaydi;
// kamchilik yo'qolsa, yozuv "bajarildi" qilib yopiladi. Shunda navbat har kuni bir xil xabar bilan to'lmaydi.

import { escapeHtml } from "./_telegram.js";
import { yoz, holatQoy, JADVAL as NAVBAT } from "./_navbat.js";

export const TOLOV_SOAT = 12;        // to'lov so'rovi shuncha soatdan ko'p kutsa
export const KANAL_QOTDI_DAQIQA = 60; // post "yuborilmoqda" holatida shuncha turib qolsa
export const VIDEO_KODLASH_SOAT = 6;  // Bunny shuncha vaqtda kodlab bo'lmasa
export const ESKI_XATO_KUN = 3;       // ochiq xato shuncha kundan eski bo'lsa hisobotda eslatiladi
const HOUR = 3600e3;
const ms = (t) => (t ? new Date(t).getTime() : 0);

// Bazada bo'lishi shart bo'lgan jadval va ustunlar: FAQAT saytda ishlab turgan (main) kod tayanadiganlari.
// Yo'q bo'lsa tegishli imkoniyat jim buziladi. Hali chiqarilmagan ish uchun ustun bu yerga qo'shilmaydi
// (masalan variants.free_until: kodi chiqarilgach qo'shiladi), aks holda soxta ogohlantirish chiqadi.
export const SXEMA = [
  ["profiles", "phone", "Telegram orqali kirish"],
  ["sotuv_leads", "handoff_at", "sotuv botining ustozga uzatishi"],
  ["tg_logins", "code", "Telegram orqali kirish"],
  ["topic_materials", "id", "mavzu materiallari"],
  ["adaptive_answers", "id", "nazorat hisobotida moslashuvchan mashq javoblari"],
  ["agent_navbat", "id", "umumiy navbat"],
  ["kanal_postlar", "id", "kanal postchisi"],
];

// Kamchiliklar ro'yxati: { kod, kimga, sarlavha, tafsilot }. Sof funksiya: faqat berilgan ma'lumotga qaraydi.
// bunny: Map(videoId -> { status, dateUploaded }) yoki null (tekshirib bo'lmadi).
export function topKamchilik({ topics = [], examples = [], transcripts = [], materials = [], variants = [], questions = [], purchases = [], posts = [], sxemaYoq = [], bunny = null, now = new Date() }) {
  const t = now.getTime(), out = [];
  const add = (kod, kimga, sarlavha, tafsilot = {}) => out.push({ kod, kimga, sarlavha, tafsilot });

  for (const [jadval, ustun, nima] of sxemaYoq) add(`sxema:${jadval}.${ustun}`, "kod", `Bazada ${jadval}.${ustun} yo'q: "${nima}" ishlamaydi`, { jadval, ustun });

  const matnli = new Set(transcripts.map((x) => x.topic_id || x.example_id));
  for (const m of topics) {
    if (!m.bunny_video_id) add(`mavzu_videosiz:${m.id}`, "platforma", `"${m.name}" mavzusida dars videosi yo'q`);
    else if (!matnli.has(m.id)) add(`mavzu_matnsiz:${m.id}`, "platforma", `"${m.name}" darsida matn yo'q: AI yordamchi javob bera olmaydi`);
    const ex = examples.filter((e) => e.topic_id === m.id && e.bunny_video_id && !matnli.has(e.id)).map((e) => e.example_number).sort((a, b) => a - b);
    if (ex.length) add(`misol_matnsiz:${m.id}`, "platforma", `"${m.name}": ${ex.length} ta misol videosida matn yo'q (${ex.join(", ")})`, { misollar: ex });
  }

  for (const v of variants) {
    const qs = questions.filter((q) => q.variant_id === v.id);
    const videosiz = qs.filter((q) => !q.bunny_video_id).map((q) => q.question_number).sort((a, b) => a - b);
    // Hali boshlanmagan variant (birorta videosi yo'q) kamchilik emas: faqat yarim qolgani.
    if (videosiz.length && videosiz.length < qs.length) add(`savol_videosiz:${v.id}`, "ustoz", `${v.variant_number}-variant: ${videosiz.length} ta savolda video tahlil yo'q (${videosiz.join(", ")})`, { savollar: videosiz });
    const javobsiz = qs.filter((q) => !q.correct_option && !String(q.correct_answer_text || "").trim()).map((q) => q.question_number).sort((a, b) => a - b);
    if (javobsiz.length) add(`savol_javobsiz:${v.id}`, "ustoz", `${v.variant_number}-variant: ${javobsiz.length} ta savolda to'g'ri javob kiritilmagan (${javobsiz.join(", ")})`, { savollar: javobsiz });
  }

  const kutgan = purchases.filter((p) => p.status === "pending" && t - ms(p.created_at) > TOLOV_SOAT * HOUR);
  if (kutgan.length) add("tolov_kutmoqda", "ustoz", `${kutgan.length} ta to'lov so'rovi ${TOLOV_SOAT} soatdan beri tasdiqlanmagan`, { soni: kutgan.length, eng_eski: kutgan.map((p) => p.created_at).sort()[0] });

  for (const p of posts) {
    if (p.holat === "xato") add(`kanal_xato:${p.id}`, "kod", `Kanal posti #${p.id} chiqmadi: ${String(p.xato || "sabab yozilmagan").slice(0, 120)}`);
    else if (p.holat === "yuborilmoqda" && t - ms(p.sent_at) > KANAL_QOTDI_DAQIQA * 60e3) add(`kanal_qotdi:${p.id}`, "kod", `Kanal posti #${p.id} "yuborilmoqda" holatida qotib qoldi: kanalda chiqqan-chiqmaganini tekshirish kerak`);
  }

  if (bunny) {
    const joylar = [
      ...topics.filter((x) => x.bunny_video_id).map((x) => [x.bunny_video_id, `"${x.name}" darsi`]),
      ...examples.filter((x) => x.bunny_video_id).map((x) => [x.bunny_video_id, `"${topics.find((m) => m.id === x.topic_id)?.name || "?"}" ${x.example_number}-misol`]),
      ...materials.filter((x) => x.bunny_video_id).map((x) => [x.bunny_video_id, `material "${x.title}"`]),
      ...questions.filter((x) => x.bunny_video_id).map((x) => [x.bunny_video_id, `${variants.find((v) => v.id === x.variant_id)?.variant_number ?? "?"}-variant ${x.question_number}-savol`]),
    ];
    for (const [id, qayer] of joylar) {
      const b = bunny.get(id);
      if (!b) add(`video_yoq:${id}`, "kod", `${qayer}: video Bunny'da topilmadi, o'quvchida ochilmaydi`, { video: id });
      else if (b.status === 5 || b.status === 6) add(`video_buzuq:${id}`, "kod", `${qayer}: video Bunny'da xato bilan to'xtagan, qayta yuklash kerak`, { video: id, status: b.status });
      else if (b.status < 3 && t - ms(b.dateUploaded) > VIDEO_KODLASH_SOAT * HOUR) add(`video_kodlanmadi:${id}`, "kod", `${qayer}: video ${VIDEO_KODLASH_SOAT} soatdan beri kodlanmagan`, { video: id, status: b.status });
    }
  }
  return out;
}

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
// Jadval hali yaratilmagan bo'lishi mumkin: unda bo'sh ro'yxat (yetishmasligi sxema tekshiruvida alohida chiqadi).
const optional = ({ data, error }) => (error ? [] : data || []);

// Bunny'dagi barcha videolar holati. Sozlanmagan yoki javob bermasa null (tekshiruv o'tkazib yuboriladi, soxta xato chiqmaydi).
export async function bunnyRoyxat(fetchFn = fetch, env = process.env) {
  const lib = env.BUNNY_LIBRARY_ID, key = env.BUNNY_API_KEY;
  if (!lib || !key) return null;
  const map = new Map();
  try {
    for (let page = 1; page <= 20; page++) {
      const r = await fetchFn(`https://video.bunnycdn.com/library/${lib}/videos?page=${page}&itemsPerPage=1000`, { headers: { AccessKey: key, accept: "application/json" } });
      if (!r.ok) return null;
      const j = await r.json();
      for (const v of j.items || []) map.set(v.guid, { status: v.status, dateUploaded: v.dateUploaded });
      if (map.size >= (j.totalItems || 0) || !(j.items || []).length) break;
    }
  } catch { return null; }
  return map;
}

export async function collectTekshiruv(db, { bunny = null, now = new Date() } = {}) {
  const sxemaYoq = [];
  for (const [jadval, ustun, nima] of SXEMA) {
    const { error } = await db.from(jadval).select(ustun).limit(1);
    if (error) sxemaYoq.push([jadval, ustun, nima]);
  }
  const [topics, examples, transcripts, variants, questions] = await Promise.all([
    db.from("topics").select("id,name,bunny_video_id").then(must),
    db.from("topic_examples").select("id,topic_id,example_number,bunny_video_id").then(must),
    db.from("video_transcripts").select("topic_id,example_id").then(must),
    db.from("variants").select("id,variant_number").then(must),
    db.from("questions").select("variant_id,question_number,bunny_video_id,correct_option,correct_answer_text").limit(5000).then(must),
  ]);
  const [materials, purchases, posts] = await Promise.all([
    db.from("topic_materials").select("title,bunny_video_id").then(optional),
    db.from("variant_purchases").select("status,created_at").eq("status", "pending").then(optional),
    db.from("kanal_postlar").select("id,holat,xato,sent_at").in("holat", ["xato", "yuborilmoqda"]).then(optional),
  ]);
  return topKamchilik({ topics, examples, transcripts, materials, variants, questions, purchases, posts, sxemaYoq, bunny, now });
}

const KIMGA_NOM = { kod: "kod agenti", platforma: "platforma agenti", ustoz: "siz" };

// Ustozga xabar: faqat bugun yangi topilganlar to'liq, qolgani son bilan. Yangilik yo'q bo'lsa null.
export function formatTekshiruv({ yangi, tuzaldi, ochiq, eski }) {
  if (!yangi.length && !tuzaldi.length && !eski.length) return null;
  const lines = [`🛠 <b>Platforma tekshiruvi</b>`];
  if (yangi.length) lines.push(`\n<b>Yangi kamchiliklar (${yangi.length} ta):</b>`, ...yangi.slice(0, 12).map((k) => `• ${escapeHtml(k.sarlavha)} <i>(${KIMGA_NOM[k.kimga] || k.kimga})</i>`), ...(yangi.length > 12 ? [`... va yana ${yangi.length - 12} ta`] : []));
  if (tuzaldi.length) lines.push(`\n✅ Tuzalgan: ${tuzaldi.length} ta`);
  if (eski.length) lines.push(`\n⏳ ${ESKI_XATO_KUN} kundan beri ochiq: ${eski.length} ta`, ...eski.slice(0, 5).map((r) => `• ${escapeHtml(r.sarlavha)}`));
  lines.push(`\nJami ochiq: ${ochiq} ta`);
  return lines.join("\n");
}

// Kamchiliklarni navbat bilan solishtiradi: yangisini yozadi, yo'qolganini yopadi. notify(text) ustozga xabar.
export async function runTekshiruv(db, notify, { bunny = null, now = new Date() } = {}) {
  const topilgan = await collectTekshiruv(db, { bunny, now });
  const ochiqlar = must(await db.from(NAVBAT).select("id,sarlavha,tafsilot,created_at").eq("agent", "nazoratchi").eq("tur", "xato").in("holat", ["yangi", "jarayonda"]).limit(1000))
    .filter((r) => r.tafsilot?.kod);
  const borKod = new Set(ochiqlar.map((r) => r.tafsilot.kod)), hozirKod = new Set(topilgan.map((k) => k.kod));

  const yangi = topilgan.filter((k) => !borKod.has(k.kod));
  for (const k of yangi) await yoz(db, { agent: "nazoratchi", tur: "xato", sarlavha: k.sarlavha, tafsilot: { ...k.tafsilot, kod: k.kod }, kimga: k.kimga });

  // Bunny tekshirilmagan kuni video kamchiliklarini "tuzaldi" deb yopmaymiz: ular shunchaki ko'rilmagan.
  const korilmagan = (kod) => !bunny && /^video_/.test(kod);
  const tuzaldi = ochiqlar.filter((r) => !hozirKod.has(r.tafsilot.kod) && !korilmagan(r.tafsilot.kod));
  for (const r of tuzaldi) await holatQoy(db, r.id, "bajarildi", "keyingi tekshiruvda topilmadi");

  // Eski kamchilik har kuni emas, har ESKI_XATO_KUN kunda bir marta eslatiladi (ustoz bir xil xabardan charchamasin).
  const yosh = (r) => Math.floor((now.getTime() - ms(r.created_at)) / (24 * HOUR));
  const eski = ochiqlar.filter((r) => hozirKod.has(r.tafsilot.kod) && yosh(r) >= ESKI_XATO_KUN && yosh(r) % ESKI_XATO_KUN === 0);
  const ochiq = ochiqlar.length - tuzaldi.length + yangi.length;
  const text = formatTekshiruv({ yangi, tuzaldi, ochiq, eski });
  if (text) await notify(text);
  return { topildi: topilgan.length, yangi: yangi.length, tuzaldi: tuzaldi.length, ochiq, bunny: !!bunny };
}
