// O'quvchi murabbiyi: pullik rejadagi, Telegramni ulagan o'quvchiga shaxsiy yo'l-yo'riq yuboradi:
// qayerda to'xtagani va keyingi qadam, qaysi mavzuda qiynalayotgani, haftalik natija, reja muddati.
// Qoidalari agentlar/murabbiy.md da. Asosiylari:
//   - faqat o'zi Telegramni ulagan va /stop demagan o'quvchiga;
//   - bir o'quvchiga ko'pi bilan KUN_ORALIQ kunda bitta xabar (nazoratchi eslatmasi bilan umumiy hisob: last_nudge_at);
//   - majburlash, uyaltirish va natija va'dasi yo'q; har xabarda /stop eslatiladi.
//
// Ishga tushirish: ertalabki kron /api/keepalive?job=nazorat (09:00, Toshkent) ichida, nazoratchidan OLDIN
// (shunda nazoratchining umumiy eslatmasi ikkinchi xabar bo'lib ketmaydi).

import { yoz } from "./_navbat.js";

export const KUN_ORALIQ = 2;        // bir o'quvchiga xabarlar orasidagi eng kam kun
export const FAOLSIZ_KUN = 3;       // shuncha kun kirmasa "davom" xabari
export const ZAIF_MIN = 6;          // mavzu bo'yicha kamida shuncha javob bo'lsa foiz hisoblanadi
export const ZAIF_FOIZ = 50;        // shundan past bo'lsa mavzu "qiyin" hisoblanadi
export const ZAIF_KUN = 30;         // oxirgi shuncha kun javoblari
export const TUGASH_KUN = 3;        // reja shuncha kun ichida tugasa bir marta eslatiladi
export const ROYXAT_MAX = 500;    // hisobotga yoziladigan o'quvchilar soni chegarasi
const DAY = 86400e3;
const ms = (t) => (t ? new Date(t).getTime() : 0);
const norm = (s) => String(s ?? "").toLowerCase().replace(/[‘’ʻʼ`´']/g, "'").replace(/\s+/g, " ").trim();
const ism = (s) => String(s.full_name || "").trim().split(/\s+/)[0] || "";
export const yakshanbami = (d = new Date()) => new Date(d.getTime() + 5 * 3600e3).getUTCDay() === 0;

// Bitta o'quvchining o'qish holati. views/answers: shu o'quvchiniki. questions: Map(id -> { topic }).
export function holat(student, { views = [], answers = [], topics = [], examples = [], questions = new Map(), now = new Date() }) {
  const t = now.getTime();
  const mavzular = [...topics].sort((a, b) => a.sort_order - b.sort_order);
  const mavzuBy = new Map(mavzular.map((m) => [m.id, m])), misolBy = new Map(examples.map((e) => [e.id, e]));
  const korgan = new Set(views.map((v) => v.ref_id));

  // Oxirgi ko'rilgan dars yoki misol
  const dars = views.filter((v) => (v.kind === "topic" && mavzuBy.has(v.ref_id)) || (v.kind === "example" && misolBy.has(v.ref_id))).sort((a, b) => ms(b.last_at) - ms(a.last_at))[0];
  let oxirgi = null, keyingi = null;
  if (dars) {
    const ex = dars.kind === "example" ? misolBy.get(dars.ref_id) : null;
    const m = mavzuBy.get(ex ? ex.topic_id : dars.ref_id);
    if (m) {
      oxirgi = { mavzu: m.name, misol: ex ? ex.example_number : null };
      // Misollar faqat Premium rejada ochiq.
      const misol = student.plan === "premium" ? examples.filter((e) => e.topic_id === m.id && e.bunny_video_id && !korgan.has(e.id)).sort((a, b) => a.example_number - b.example_number)[0] : null;
      if (misol) keyingi = { mavzu: m.name, misol: misol.example_number };
      else {
        const k = mavzular.find((x) => x.sort_order > m.sort_order && x.bunny_video_id && !korgan.has(x.id));
        if (k) keyingi = { mavzu: k.name, misol: null };
      }
    }
  } else {
    const birinchi = mavzular.find((x) => x.bunny_video_id);
    if (birinchi) keyingi = { mavzu: birinchi.name, misol: null };
  }

  const vaqtlar = [...views.map((v) => ms(v.last_at)), ...answers.map((a) => ms(a.answered_at))].filter(Boolean);
  const faolsiz = vaqtlar.length ? Math.floor((t - Math.max(...vaqtlar)) / DAY) : null;     // null: hali hech narsa qilmagan

  // Qiyin mavzular: savolning mavzusi bo'yicha, oxirgi ZAIF_KUN kun
  const by = new Map();
  for (const a of answers) {
    if (t - ms(a.answered_at) > ZAIF_KUN * DAY) continue;
    const nom = String(questions.get(a.question_id)?.topic || "").trim();
    if (!nom) continue;
    const r = by.get(norm(nom)) || { mavzu: nom, soni: 0, togri: 0 };
    r.soni++; if (a.is_correct) r.togri++;
    by.set(norm(nom), r);
  }
  const darsBor = new Set(mavzular.filter((m) => m.bunny_video_id).map((m) => norm(m.name)));
  const zaif = [...by.values()].filter((r) => r.soni >= ZAIF_MIN).map((r) => ({ mavzu: r.mavzu, soni: r.soni, foiz: Math.round((r.togri / r.soni) * 100), dars: darsBor.has(norm(r.mavzu)) }))
    .filter((r) => r.foiz < ZAIF_FOIZ).sort((a, b) => a.foiz - b.foiz);

  const hv = views.filter((v) => t - ms(v.last_at) <= 7 * DAY), ha = answers.filter((a) => t - ms(a.answered_at) <= 7 * DAY);
  const hafta = { video: hv.length, savol: ha.length, togri: ha.filter((a) => a.is_correct).length };
  const rejaKun = student.plan_expires_at ? Math.ceil((ms(student.plan_expires_at) - t) / DAY) : null;
  return { oxirgi, keyingi, faolsiz, zaif, hafta, rejaKun };
}

const joy = (x) => x.misol ? `"${x.mavzu}" mavzusining ${x.misol}-misoli` : `"${x.mavzu}" mavzusi`;
const STOP = "\n\nBunday xabarlar kerak bo'lmasa, /stop deb yozing.";

// Shu o'quvchiga bugun qaysi xabar ketishini tanlaydi (yoki null). Ustuvorlik: reja muddati, davom ettirish,
// qiyin mavzu, haftalik natija. Bir kunda bitta xabar.
export function xabar(student, h, { yakshanba = false, eslatilgan = false } = {}) {
  // Ohang: ustoz o'zi yozgandek iliq, "Assalomu alaykum" bilan (ustoz 2026-11-19 da namunalardan tanlagan).
  // Tekshirib bo'lmaydigan gap ("oson mavzu", "ko'pchilik qiynaladi") qo'shilmaydi. Javobni yordamchi bot beradi,
  // shuning uchun "menga yozing" emas, "shu yerga yozing" deyiladi.
  const salom = ism(student) ? `Assalomu alaykum, ${ism(student)}!` : "Assalomu alaykum!";
  const rejaNom = student.plan === "premium" ? "Premium" : "Standart";

  if (h.rejaKun != null && h.rejaKun >= 0 && h.rejaKun <= TUGASH_KUN && !eslatilgan) {
    return { tur: "reja", text: `${salom} ${rejaNom} rejangiz ${h.rejaKun === 0 ? "bugun" : `${h.rejaKun} kundan keyin`} tugaydi. Davom ettirish yoki to'xtatish o'zingizning ixtiyoringiz. Savolingiz bo'lsa shu yerga yozing.${STOP}` };
  }
  if (h.faolsiz == null) {
    return { tur: "boshlash", text: `${salom} Platformada hali birorta dars ochmabsiz.${h.keyingi ? ` ${joy(h.keyingi)}dan boshlasangiz bo'ladi.` : ""} Qayerdan boshlashni bilmasangiz, shu yerga yozing, birga tanlaymiz.${STOP}` };
  }
  if (h.faolsiz >= FAOLSIZ_KUN) {
    const qayer = h.oxirgi ? ` Oxirgi marta ${joy(h.oxirgi)}gacha yetib kelgan edingiz.` : "";
    const keyin = h.keyingi ? ` Keyingisi: ${joy(h.keyingi)}. Vaqt topsangiz shundan davom eting.` : "";
    return { tur: "davom", text: `${salom} ${h.faolsiz} kundan beri ko'rinmay qoldingiz. Hammasi joyidami?${qayer}${keyin} Tushunmagan joy bo'lsa shu yerga yozing.${STOP}` };
  }
  if (h.zaif.length) {
    const z = h.zaif[0];
    const dars = z.dars ? " Dars videosini yana bir marta ko'rib, keyin savollarga qayting." : "";
    return { tur: "qiyin", text: `${salom} "${z.mavzu}" mavzusidan ${z.soni} ta savol yechibsiz, ${Math.round((z.soni * z.foiz) / 100)} tasi to'g'ri chiqibdi. Xavotir olmang, bunaqasi bo'lib turadi.${dars} Qaysi joyi chalkash bo'lsa, shu yerga yozing.${STOP}` };
  }
  if (yakshanba && (h.hafta.video || h.hafta.savol)) {
    const foiz = h.hafta.savol ? `, ${h.hafta.savol} ta savol yechibsiz (${Math.round((h.hafta.togri / h.hafta.savol) * 100)}% to'g'ri)` : "";
    const keyin = h.keyingi ? ` Keyingi hafta uchun: ${joy(h.keyingi)}.` : "";
    return { tur: "hafta", text: `${salom} Bu hafta ${h.hafta.video} ta video ko'ribsiz${foiz}. Barakalla, shu tartibda davom eting.${keyin}${STOP}` };
  }
  return null;
}

const must = ({ data, error }) => { if (error) throw new Error(error.message); return data || []; };
const optional = ({ data, error }) => (error ? [] : data || []);

// Har o'quvchi uchun tanlangan xabar. Hech narsa yubormaydi.
export async function collectMurabbiy(db, { now = new Date() } = {}) {
  const t = now.getTime();
  const profiles = must(await db.from("profiles").select("id,full_name,plan,plan_expires_at,is_admin").neq("plan", "free"));
  const students = profiles.filter((p) => !p.is_admin && (!p.plan_expires_at || ms(p.plan_expires_at) > t));
  if (!students.length) return [];
  const ids = students.map((s) => s.id);
  // reja_eslatma ustuni hali qo'shilmagan bo'lishi mumkin (migratsiya 20261119010000): unda ustunsiz o'qiymiz.
  // Aks holda so'rov xato berib, hamma o'quvchi "Telegram ulanmagan" bo'lib ko'rinardi.
  const leadsQ = (cols) => db.from("sotuv_leads").select(cols).in("linked_user_id", ids);
  let lr = await leadsQ("tg_id,linked_user_id,remind,last_nudge_at,reja_eslatma");
  if (lr.error) lr = await leadsQ("tg_id,linked_user_id,remind,last_nudge_at");
  const leads = optional(lr);
  const [views, answers, topics, examples] = await Promise.all([
    db.from("video_views").select("student_id,kind,ref_id,last_at").in("student_id", ids).limit(10000).then(must),
    db.from("answers").select("student_id,question_id,is_correct,answered_at").in("student_id", ids).order("answered_at", { ascending: false }).limit(10000).then(must),
    db.from("topics").select("id,name,sort_order,bunny_video_id").then(must),
    db.from("topic_examples").select("id,topic_id,example_number,bunny_video_id").then(must),
  ]);
  const qIds = [...new Set(answers.map((a) => a.question_id))];
  const questions = new Map(qIds.length ? must(await db.from("questions").select("id,topic").in("id", qIds)).map((q) => [q.id, q]) : []);
  const yak = yakshanbami(now);
  return students.map((s) => {
    const lead = leads.find((l) => l.linked_user_id === s.id) || null;
    const h = holat(s, { views: views.filter((v) => v.student_id === s.id), answers: answers.filter((a) => a.student_id === s.id), topics, examples, questions, now });
    // Reja eslatmasi shu muddat uchun bir marta: reja_eslatma ustuni bo'lmasa (migratsiya ishlamagan) ham bir marta ketadi,
    // chunki oraliq cheklovi (KUN_ORALIQ) va 3 kunlik oyna ko'pi bilan ikki xabarga yo'l qo'yadi.
    const eslatilgan = !!(lead?.reja_eslatma && s.plan_expires_at && ms(lead.reja_eslatma) === ms(s.plan_expires_at));
    const x = xabar(s, h, { yakshanba: yak, eslatilgan });
    let sabab = null;
    if (!x) sabab = "bugun xabar kerak emas";
    else if (!lead) sabab = "Telegram ulanmagan";
    else if (!lead.remind) sabab = "/stop qilgan";
    else if (lead.last_nudge_at && t - ms(lead.last_nudge_at) < KUN_ORALIQ * DAY) sabab = "yaqinda xabar yuborilgan";
    return { student: s, lead, holat: h, xabar: x, sabab };
  });
}

// send(tg_id, text) -> { ok }. Yuborilganlarni belgilaydi va navbatga kunlik bitta hisobot qo'yadi (har o'quvchi bo'yicha qaror bilan).
export async function runMurabbiy(db, send, { now = new Date(), log = (y) => yoz(db, y) } = {}) {
  const hammasi = await collectMurabbiy(db, { now });
  const turlar = {}, royxat = [];
  let yuborildi = 0, xato = 0;
  for (const r of hammasi) {
    // Har o'quvchi bo'yicha qaror hisobotga yoziladi: CEO uni nazoratchi ro'yxati bilan solishtiradi.
    const qator = { id: r.student.id, ism: String(r.student.full_name || "").trim().slice(0, 60) || "Noma'lum", tur: r.xabar?.tur || null, holat: r.sabab };
    royxat.push(qator);
    if (r.sabab) continue;
    const res = await send(r.lead.tg_id, r.xabar.text);
    if (!res?.ok) { xato++; qator.holat = "yetmadi"; continue; }
    qator.holat = "yuborildi";
    yuborildi++; turlar[r.xabar.tur] = (turlar[r.xabar.tur] || 0) + 1;
    const patch = { last_nudge_at: now.toISOString() };
    if (r.xabar.tur === "reja") patch.reja_eslatma = r.student.plan_expires_at;
    const { error } = await db.from("sotuv_leads").update(patch).eq("tg_id", r.lead.tg_id);
    // reja_eslatma ustuni hali yo'q bo'lsa: vaqt belgisi baribir yozilsin (ikkinchi xabar ketmasin).
    if (error && patch.reja_eslatma) await db.from("sotuv_leads").update({ last_nudge_at: patch.last_nudge_at }).eq("tg_id", r.lead.tg_id);
  }
  const kun = new Date(now.getTime() + 5 * 3600e3).toISOString().slice(0, 10);
  // Hisobot HAR KUNI yoziladi, hech kimga xabar ketmagan kuni ham (ustoz 2026-11-19): shunda "yuboradigan odam yo'q edi"
  // bilan "umuman ishlamadi" ajraladi. Kalit kuniga bitta: kron qayta ishlasa birinchi hisobot qoladi.
  const sarlavha = `O'quvchilarga yo'l-yo'riq: ${yuborildi} ta yuborildi${xato ? `, ${xato} tasi yetmadi` : ""} (${hammasi.length} ta o'quvchi ko'rildi)`;
  await log({ agent: "murabbiy", tur: xato && !yuborildi ? "xato" : "hisobot", sarlavha, tafsilot: { yuborildi, xato, turlar, oquvchilar: hammasi.length, royxat: royxat.slice(0, ROYXAT_MAX) }, kalit: `murabbiy:${kun}`, ...(xato && !yuborildi ? { kimga: "kod" } : {}) });
  return { oquvchilar: hammasi.length, yuborildi, xato, turlar };
}
