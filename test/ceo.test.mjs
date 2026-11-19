import test from "node:test";
import assert from "node:assert/strict";
import { moliya, moliyaQatorlar, som, oyBoshi, TUGASH_KUN } from "../api/_hisobchi.js";
import { solishtir, FARQ_MAX, hisobla, formatHisobot, etibor, runCeo, yakshanbami, tashkentKun } from "../api/_ceo.js";

const NOW = new Date("2026-11-19T15:00:00Z");                 // Toshkentda 20:00, payshanba
const kunOldin = (d) => new Date(NOW.getTime() - d * 86400e3).toISOString();
const kunKeyin = (d) => new Date(NOW.getTime() + d * 86400e3).toISOString();
const paid = (amount, d, extra = {}) => ({ status: "paid", amount, paid_at: kunOldin(d), created_at: kunOldin(d), ...extra });
const prof = (id, extra = {}) => ({ id, full_name: id, email: `${id}@mail.uz`, plan: "free", plan_expires_at: null, is_admin: false, created_at: kunOldin(40), ...extra });

test("som va oyBoshi: minglik bo'shliq bilan; oy Toshkent vaqti bilan boshlanadi", () => {
  assert.equal(som(610000), "610 000 so'm");
  assert.equal(som(0), "0 so'm");
  assert.equal(oyBoshi(new Date("2026-11-30T19:30:00Z")).toISOString(), "2026-11-30T19:00:00.000Z");   // Toshkentda 1-dekabr 00:30
  assert.equal(oyBoshi(NOW).toISOString(), "2026-10-31T19:00:00.000Z");
});

test("moliya: davr, oy va jami tushum; faqat to'langan va sanasi bor to'lovlar sanaladi", () => {
  const m = moliya({
    purchases: [paid(200000, 0.5, { plan_id: "premium" }), paid(5000, 0.2, { variant_id: "v" }), paid(200000, 10, { plan_id: "premium" }), paid(49900, 25, { plan_id: "standart" }),
      { status: "pending", amount: 200000, created_at: kunOldin(1), plan_id: "premium" }, { status: "cancelled", amount: 5000, paid_at: null }, { status: "paid", amount: 999, paid_at: null }],
    now: NOW, boshi: new Date(NOW.getTime() - 86400e3),
  });
  assert.deepEqual(m.davr, { summa: 205000, soni: 2, turlar: { premium: { soni: 1, summa: 200000 }, variant: { soni: 1, summa: 5000 } } });
  assert.equal(m.oy.summa, 405000);                    // 25 kun oldingi (oktabr) kirmaydi
  assert.deepEqual(m.jami, { summa: 454900, soni: 4 });
  assert.deepEqual(m.kutmoqda, { soni: 1, summa: 200000 });
});

test("moliya: faol rejalar, tugayotgan va uzaytirmagan o'quvchilar; admin va bepul sanalmaydi", () => {
  const m = moliya({
    profiles: [prof("ali", { plan: "premium", plan_expires_at: kunKeyin(20) }), prof("vali", { plan: "premium", plan_expires_at: kunKeyin(2.5) }), prof("sami", { plan: "standart", plan_expires_at: kunKeyin(TUGASH_KUN - 0.5) }),
      prof("guli", { plan: "premium", plan_expires_at: kunOldin(3.2) }), prof("eski", { plan: "premium", plan_expires_at: kunOldin(30) }), prof("admin", { plan: "premium", is_admin: true }), prof("bepul"), prof("umrbod", { plan: "premium" })],
    now: NOW,
  });
  assert.deepEqual(m.faol, { premium: 3, standart: 1 });           // ali, vali, umrbod; sami
  assert.deepEqual(m.tugaydi, [{ ism: "vali", plan: "premium", kun: 3 }, { ism: "sami", plan: "standart", kun: 7 }]);
  assert.deepEqual(m.tugagan, [{ ism: "guli", plan: "premium", kun: 3 }]);
});

test("moliyaQatorlar: to'lovsiz kun, kutayotgan to'lov va muddat ogohlantirishlari", () => {
  const q = moliyaQatorlar(moliya({ purchases: [{ status: "pending", amount: 200000, created_at: kunOldin(1) }], profiles: [prof("vali", { plan: "premium", plan_expires_at: kunKeyin(2.5) }), prof("guli", { plan: "premium", plan_expires_at: kunOldin(1.5) })], now: NOW }));
  assert.equal(q[0], "Bugun to'lov bo'lmadi");
  assert.ok(q.includes("Tasdiq kutayotgan to'lov: 1 ta (200 000 so'm)"));
  assert.ok(q.includes("⏳ vali: premium 3 kunda tugaydi"));
  assert.ok(q.includes("⚠️ guli: premium 1 kun oldin tugadi, uzaytirmagan"));
  const h = moliyaQatorlar(moliya({ purchases: [paid(200000, 3, { plan_id: "premium" })], now: NOW, boshi: new Date(NOW.getTime() - 7 * 86400e3) }), { haftalik: true });
  assert.equal(h[0], "Hafta tushum: 200 000 so'm (premium 1 ta)");
});

const namuna = () => ({
  profiles: [prof("a", { created_at: kunOldin(0.3) }), prof("b", { created_at: kunOldin(1.5) }), prof("c"), prof("adm", { is_admin: true, created_at: kunOldin(0.1) })],
  leads: [{ created_at: kunOldin(0.2), source: "ig_bio", linked_user_id: "a" }, { created_at: kunOldin(0.4), source: null }, { created_at: kunOldin(0.6), source: "ig_bio" }, { created_at: kunOldin(1.2), source: "kanal" }],
  messages: [{ role: "user", created_at: kunOldin(0.1) }, { role: "assistant", created_at: kunOldin(0.1) }, { role: "user", created_at: kunOldin(3) }],
  views: [{ student_id: "a", last_at: kunOldin(0.5) }, { student_id: "c", last_at: kunOldin(4) }],
  answers: [{ student_id: "a", answered_at: kunOldin(0.2) }, { student_id: "b", answered_at: kunOldin(0.3) }],
  guestViews: [{ last_at: kunOldin(0.9) }, { last_at: kunOldin(2) }],
  aiSavollar: [{ created_at: kunOldin(0.7) }],
  purchases: [paid(200000, 0.5, { plan_id: "premium" }), paid(5000, 1.5, { variant_id: "v" })],
  posts: [{ holat: "yuborildi", sent_at: kunOldin(0.1) }, { holat: "yuborildi", sent_at: kunOldin(5) }, { holat: "tasdiqlangan" }, { holat: "qoralama" }, { holat: "qoralama" }],
  navbat: [
    { agent: "instagram", tur: "ish", holat: "bajarildi", sarlavha: "Joylandi: shisha", created_at: kunOldin(0.2) },
    { agent: "instagram", tur: "ish", holat: "jarayonda", sarlavha: "Qabul qilindi: shisha", created_at: kunOldin(0.3) },
    { agent: "platforma", tur: "ish", holat: "bajarildi", sarlavha: "Platformaga joylandi: Alkenlar", created_at: kunOldin(0.4) },
    { agent: "sotuv", tur: "savol", holat: "yangi", sarlavha: "Ustoz kerak: to'lov", kimga: "ustoz", created_at: kunOldin(0.5) },
    { agent: "kod", tur: "xato", holat: "bekor", sarlavha: "Sinov", created_at: kunOldin(0.5) },
    { agent: "nazoratchi", tur: "xato", holat: "yangi", sarlavha: "Eski", created_at: kunOldin(3) },
  ],
  ochiq: [{ sarlavha: "Ustoz kerak: to'lov", kimga: "ustoz" }, { sarlavha: "Video <buzuq>", kimga: "kod" }, { sarlavha: "Matn yo'q", kimga: "platforma" }, { sarlavha: "Matn yo'q 2", kimga: "platforma" }],
  now: NOW,
});

test("hisobla (kunlik): har bo'lim faqat oxirgi 24 soatni sanaydi; admin, bekor qilingan va eski yozuvlar kirmaydi", () => {
  const h = hisobla(namuna());
  assert.deepEqual(h.oquvchilar, { yangi: 1, yangi_oldin: 1, jami: 3, faol: 2, mehmon: 1, ai_savol: 1, javoblar: 2 });
  assert.deepEqual(h.sotuv, { lid: 3, lid_oldin: 1, manba: { ig_bio: 2, "to'g'ridan-to'g'ri": 1 }, xabar: 1, uzatish: 1, ulangan: 1, jami: 4 });
  assert.equal(h.pul.davr.summa, 200000);
  assert.equal(h.tushum_oldin, 5000);
  assert.deepEqual(h.kontent, { kanal: 1, kanal_navbat: 1, kanal_qoralama: 2, instagram: 1, platforma: 1 });
  assert.deepEqual(Object.keys(h.agentlar).sort(), ["instagram", "platforma", "sotuv"]);
  assert.deepEqual(h.agentlar.instagram, { ish: 2, xato: 0, savol: 0, hisobot: 0 });
  assert.deepEqual([h.ustozga.length, h.kodga, h.platformaga], [1, 1, 2]);
});

test("hisobla (haftalik): davr 7 kun, oldingi 7 kun bilan taqqoslanadi", () => {
  const d = namuna();
  d.profiles.push(prof("d", { created_at: kunOldin(9) }), prof("e", { created_at: kunOldin(10) }), prof("f", { created_at: kunOldin(20) }));
  const h = hisobla({ ...d, kun: 7 });
  assert.deepEqual([h.oquvchilar.yangi, h.oquvchilar.yangi_oldin], [2, 2]);
  assert.deepEqual([h.sotuv.lid, h.sotuv.lid_oldin], [4, 0]);
  assert.equal(h.pul.davr.summa, 205000);
  assert.equal(h.kontent.kanal, 2);
});

test("formatHisobot: kunlik matn qisqa: avval sizdan kutilayotgani, keyin o'zgargani va e'tibor", () => {
  const t = formatHisobot(hisobla(namuna()), { sana: "2026-11-19" });
  assert.match(t, /^📊 <b>Kunlik hisobot<\/b>, 2026-11-19\n\n<b>Sizdan kutilmoqda<\/b>\n• Ustoz kerak: to'lov/);
  assert.match(t, /• Kanalda 2 ta qoralama tasdig'ingizni kutyapti/);
  assert.match(t, /<b>O'zgargani<\/b>\nYangi o'quvchi: 1 ta, faol: \d+ ta, yangi lid: 3 ta\nBugun tushum: 200 000 so'm \(premium 1 ta\)/);
  assert.match(t, /Joylandi: Instagram 1 ta reels, kanal 1 ta post, platforma 1 ta dars/);
  assert.match(t, /<b>E'tibor<\/b>[\s\S]*Agentlar navbatida ochiq ish: kod agentida 1 ta, platforma agentida 2 ta/);
  assert.match(t, /To'liq raqamlar yakshanba kungi haftalik hisobotda\.$/);
  assert.doesNotMatch(t, /Shu oy|Faol rejalar|Agentlar ishi|o'tgan haftaga nisbatan/);       // to'liq raqamlar faqat haftalikda
  assert.ok(t.length < 4000);
});

test("etibor: pullik faolsiz o'quvchilar, xatolar, Reels rejasi", () => {
  const p = (id, plan, extra = {}) => ({ id, plan, created_at: "2026-10-01T00:00:00Z", ...extra });
  const profiles = [p("a", "premium"), p("b", "premium"), p("c", "free"), p("d", "premium", { plan_expires_at: "2026-11-01T00:00:00Z" }), p("x", "premium", { is_admin: true })];
  const h = hisobla({ profiles, haftaFaol: ["a"], now: NOW });
  assert.deepEqual([h.pullik_soni, h.pullik_faolsiz], [2, 1]);                             // muddati o'tgan, bepul va admin sanalmaydi
  assert.match(etibor(h).join("\n"), /1 ta pullik o'quvchi 7 kundan beri kirmayapti \(jami pullik: 2\)/);
  assert.equal(hisobla({ profiles, now: NOW }).pullik_faolsiz, null);                      // ma'lumot yo'q: qator chiqmaydi
  assert.doesNotMatch(etibor(hisobla({ profiles, now: NOW })).join("\n"), /kirmayapti/);
  assert.doesNotMatch(etibor(h).join("\n"), /Reels/);                                      // 23-noyabrgacha eslatilmaydi
  const keyin = new Date("2026-11-24T15:00:00Z");
  assert.match(etibor(hisobla({ now: keyin })).join("\n"), /Bugun Reels joylanmadi/);
  assert.doesNotMatch(etibor(hisobla({ now: keyin, kun: 7 })).join("\n"), /Reels/);         // haftalikda emas
  assert.match(etibor(hisobla({ now: NOW, navbat: [{ agent: "kod", tur: "xato", holat: "yangi", sarlavha: "x", created_at: new Date(NOW.getTime() - 3600e3).toISOString() }] })).join("\n"), /Kod agenti: 1 ta xato/);
});

test("formatHisobot: haftalik matn to'liq va taqqoslash bilan; jim kunda ham hisobot chiqadi", () => {
  const h = formatHisobot(hisobla({ ...namuna(), kun: 7 }), { sana: "2026-11-19" });
  assert.match(h, /Haftalik hisobot<\/b> \(2026-11-19 gacha 7 kun\)/);
  assert.match(h, /Yangi lid: 4 ta \(\+4 o'tgan haftaga nisbatan\)/);
  assert.match(h, /Shu oy: /);
  assert.match(h, /Instagram agenti: \d+ ish/);
  const jim = formatHisobot(hisobla({ now: NOW }), { sana: "2026-11-19" });
  assert.match(jim, /✅ Sizdan hech narsa kutilmayapti/);
  assert.match(jim, /Yangi o'quvchi: 0 ta, faol: 0 ta, yangi lid: 0 ta\nBugun to'lov bo'lmadi/);
  assert.doesNotMatch(jim, /E'tibor|Joylandi/);
});

test("yakshanbami va tashkentKun: hafta kuni Toshkent vaqti bilan", () => {
  assert.equal(yakshanbami(new Date("2026-11-22T15:00:00Z")), true);       // yakshanba 20:00
  assert.equal(yakshanbami(new Date("2026-11-21T18:59:00Z")), false);      // shanba 23:59
  assert.equal(yakshanbami(new Date("2026-11-21T19:00:00Z")), true);       // yakshanba 00:00
  assert.equal(tashkentKun(NOW), "2026-11-19");
});

// runCeo uchun bazaning xotiradagi nusxasi.
function fakeDb(tables, yoq = []) {
  let seq = 0;
  const from = (name) => {
    const q = { op: "select", filters: [] };
    const run = () => {
      if (yoq.includes(name)) return { data: null, error: { message: `relation ${name} does not exist` } };
      const rows = (tables[name] ||= []);
      if (q.op === "upsert") { if (rows.some((r) => r.kalit === q.row.kalit)) return { data: [], error: null }; const r = { id: ++seq, created_at: NOW.toISOString(), ...q.row }; rows.push(r); return { data: [{ id: r.id }], error: null }; }
      if (q.op === "insert") { const r = { id: ++seq, created_at: NOW.toISOString(), ...q.row }; rows.push(r); return { data: [{ id: r.id }], error: null }; }
      return { data: rows.filter((r) => q.filters.every((f) => f(r))), error: null };
    };
    const api = {
      select() { return api; }, order() { return api; }, limit() { return api; },
      insert(row) { q.op = "insert"; q.row = row; return api; },
      upsert(row) { q.op = "upsert"; q.row = row; return api; },
      eq(k, v) { q.filters.push((r) => r[k] === v); return api; },
      in(k, vs) { q.filters.push((r) => vs.includes(r[k])); return api; },
      gte(k, v) { q.filters.push((r) => r[k] >= v); return api; },
      then(res, rej) { return Promise.resolve(run()).then(res, rej); },
    };
    return api;
  };
  return { from, tables };
}

test("runCeo: hisobot bir marta yuboriladi, navbatga yoziladi; kron ikki marta ishlasa ikkinchisi yubormaydi", async () => {
  const db = fakeDb({ profiles: [prof("a", { created_at: kunOldin(0.3) })], variant_purchases: [paid(200000, 0.5, { plan_id: "premium" })], agent_navbat: [] }), notes = [];
  const notify = async (t) => { notes.push(t); };
  assert.deepEqual(await runCeo(db, notify, { now: NOW }), { sent: true, hafta: false });
  assert.deepEqual(await runCeo(db, notify, { now: NOW }), { sent: false, sabab: "bugungi hisobot yuborilgan" });
  assert.equal(notes.length, 1);
  assert.match(notes[0], /Kunlik hisobot/);
  const yozuv = db.tables.agent_navbat[0];
  assert.deepEqual({ agent: yozuv.agent, tur: yozuv.tur, kalit: yozuv.kalit, tushum: yozuv.tafsilot.tushum }, { agent: "ceo", tur: "hisobot", kalit: "ceo:kun:2026-11-19", tushum: 200000 });
  assert.deepEqual(await runCeo(db, notify, { now: NOW, hafta: true }), { sent: true, hafta: true });      // haftalik alohida kalit
  assert.match(notes[1], /Haftalik hisobot/);
});

test("runCeo: ixtiyoriy jadvallar yo'q bo'lsa ham hisobot chiqadi; asosiy jadval o'qilmasa xato yashirilmaydi va hech narsa yuborilmaydi", async () => {
  const notes = [], warn = console.warn; console.warn = () => {};
  try {
    const db = fakeDb({ profiles: [], variant_purchases: [], agent_navbat: [] }, ["sotuv_leads", "sotuv_messages", "guest_views", "kanal_postlar", "video_questions"]);
    assert.equal((await runCeo(db, async (t) => { notes.push(t); }, { now: NOW })).sent, true);
    await assert.rejects(() => runCeo(fakeDb({ agent_navbat: [] }, ["profiles"]), async (t) => { notes.push(t); }, { now: NOW }), /profiles does not exist/);
  } finally { console.warn = warn; }
  assert.equal(notes.length, 1);
});

// ---- Nazoratchi va Murabbiy hisobotini solishtirish ----
const nz = (royxat, extra = {}) => ({ flagged: royxat.length, jami: 4, royxat, ...extra });
const mr = (royxat, extra = {}) => ({ oquvchilar: royxat.length, royxat, ...extra });
const N = (id, extra = {}) => ({ id, ism: id, faolsiz: true, past: false, status: null, ...extra });
const M = (id, tur, holat) => ({ id, ism: id, tur, holat });

test("solishtir: hisobot yo'q bo'lsa aytadi; eski ko'rinishdagi yozuvda jim", () => {
  assert.match(solishtir(null, null)[0], /ham bugun hisobot bermadi/);
  assert.deepEqual(solishtir(null, mr([])), ["Nazoratchi bugun hisobot bermadi"]);
  assert.deepEqual(solishtir(nz([]), null), ["Murabbiy bugun hisobot bermadi"]);
  assert.deepEqual(solishtir({ flagged: 2, sent: true, nudged: 0 }, mr([])), []);
});

test("solishtir: ikkalasi mos bo'lsa farq yo'q", () => {
  const n = nz([N("ali"), N("vali", { status: "not_linked" }), N("guli", { faolsiz: false, past: true })]);
  const m = mr([M("ali", "davom", "yuborildi"), M("vali", "boshlash", "Telegram ulanmagan"), M("guli", "qiyin", "yuborildi"), M("sami", null, "bugun xabar kerak emas")]);
  assert.deepEqual(solishtir(n, m), []);
});

test("solishtir: faollik bo'yicha kelishmovchilik, ikki xabar, yetmagan xabar va son farqi topiladi", () => {
  const n = nz([N("ali"), N("vali", { status: "sent" }), N("yoq")], { jami: 5 });
  const m = mr([M("ali", null, "bugun xabar kerak emas"), M("vali", "davom", "yuborildi"), M("guli", "davom", "yetmadi"), M("sami", "boshlash", "yuborildi")]);
  assert.deepEqual(solishtir(n, m), [
    "Pullik o'quvchilar soni: Nazoratchi 5 ta, Murabbiy 4 ta ko'rgan",
    "ali: Nazoratchi faolsiz deydi, Murabbiy faol deb hisoblagan",
    "vali: bugun ikkalasidan ham xabar oldi",
    "yoq: Nazoratchi faolsiz deydi, Murabbiy ro'yxatida yo'q",
    "guli: Murabbiy faolsiz deb hisoblagan, Nazoratchi faol deydi",
    "Murabbiy xabari yetmadi: guli",
  ]);
});

test("solishtir: farq ko'p bo'lsa qisqartiriladi; hisobotda alohida bo'lim, farq bo'lmasa bo'lim yo'q", () => {
  const ids = Array.from({ length: 10 }, (_, i) => `o${i}`);
  const q = solishtir(nz(ids.map((id) => N(id)), { jami: 10 }), mr(ids.map((id) => M(id, null, "bugun xabar kerak emas"))));
  assert.equal(q.length, FARQ_MAX + 1);
  assert.match(q.at(-1), /va yana 4 ta farq/);
  const bor = formatHisobot(hisobla({ now: NOW, ertalab: { nazorat: nz([N("ali")], { jami: 1 }), murabbiy: null } }), { sana: "2026-11-19" });
  assert.match(bor, /Nazoratchi va Murabbiy hisobotida farq<\/b>\n• Murabbiy bugun hisobot bermadi/);
  assert.doesNotMatch(formatHisobot(hisobla({ now: NOW }), { sana: "2026-11-19" }), /hisobotida farq/);
  assert.deepEqual(hisobla({ now: NOW, kun: 7, ertalab: { nazorat: null, murabbiy: null } }).farqlar, []);      // haftalikda solishtirilmaydi
});

// ---- Kutilgan ish jadvali va eskirgan ishlar ----
test("etibor: reja kuni kelgan post chiqmasa, post xato bo'lsa va ssenariylar tugayotgan bo'lsa aytadi", () => {
  const posts = [{ holat: "tasdiqlangan", reja_kuni: "2026-11-18" }, { holat: "tasdiqlangan", reja_kuni: "2026-12-01" }, { holat: "xato", reja_kuni: "2026-11-10" }];
  const e1 = etibor(hisobla({ now: NOW, posts, rejaOxiri: "2026-11-21" })).join("\n");
  assert.match(e1, /reja kuni kelgan 1 ta tasdiqlangan post bor, lekin bugun post chiqmadi/);
  assert.match(e1, /1 ta post xato bilan to'xtagan/);
  assert.match(e1, /Tayyor ssenariylar 2026-11-21 gacha yetadi \(2 kun qoldi\)/);
  const chiqdi = [...posts, { holat: "yuborildi", sent_at: new Date(NOW.getTime() - 3600e3).toISOString() }];
  assert.doesNotMatch(etibor(hisobla({ now: NOW, posts: chiqdi })).join("\n"), /bugun post chiqmadi/);      // kuniga bitta: bugun chiqqan, qolgani navbatda
  assert.doesNotMatch(etibor(hisobla({ now: NOW, rejaOxiri: "2026-11-29" })).join("\n"), /ssenariylar/);    // hali uzoq
  assert.match(etibor(hisobla({ now: NOW, rejaOxiri: "2026-11-17" })).join("\n"), /2026-11-17 da tugagan/);
});

test("etibor: 3 kundan eski ochiq ish nomi bilan ko'rsatiladi, yangisi faqat sonda", () => {
  const eski = new Date(NOW.getTime() - 5 * 86400e3).toISOString(), yangi = new Date(NOW.getTime() - 86400e3).toISOString();
  const ochiq = [{ sarlavha: "Bazada ustun yo'q", kimga: "kod", tur: "xato", created_at: eski }, { sarlavha: "Yangi xato", kimga: "kod", tur: "xato", created_at: yangi }, { sarlavha: "To'lov kutyapti", kimga: "ustoz", tur: "savol", created_at: eski }];
  const e1 = etibor(hisobla({ now: NOW, ochiq })).join("\n");
  assert.match(e1, /5 kundan beri ochiq \(kod agenti\): Bazada ustun yo'q/);
  assert.doesNotMatch(e1, /beri ochiq.*Yangi xato|beri ochiq.*To'lov/);
});
