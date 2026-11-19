// AI ofis: agentlar ro'yxati va ularning navbatdagi ishlaridan yig'ilgan holat. Sof kod: baza kaliti ham, fayl ham o'qimaydi,
// shuning uchun serverda (api/bunny-auth.js orqali, faqat adminga) ham, kompyuterda (agentlar/ofis.mjs) ham ishlatiladi.
// Yangi agent qo'shilsa yoki holati o'zgarsa shu ro'yxat yangilanadi.

// Agentlar: id navbatdagi "agent" maydoniga teng. "buyum" xonadagi kasbiy buyumlarni belgilaydi.
// holat: ishlaydi | sinovda (o'rgatilgan, saytga chiqmagan yoki haqiqiy ishda sinalmagan) | qurilmagan.
export const AGENTLAR = [
  { id: "marketolog", nom: "Marketolog", guruh: "Kontent", buyum: "doska", joy: "Kompyuter", jadval: "Siz \"boshla\" deganda", holat: "sinovda",
    izoh: "Brend qo'llanmasiga moslangan, qayta sinalmagan", hujjat: "agentlar/marketolog.md",
    qobiliyat: ["Haftalik kontent reja", "Hook va Reels ssenariysi", "Caption va kanal posti", "Marketing raqamlari tahlili"] },
  { id: "montaj", nom: "Reels montajchisi", guruh: "Kontent", buyum: "kamera", joy: "Kompyuter", jadval: "Syomkadan keyin", holat: "sinovda",
    izoh: "Uslub tanlangan (tungi ko'k + sariq), sinov video chiqqan", hujjat: "agentlar/reels_montaj.md",
    qobiliyat: ["Pauzalarni kesish", "Bo'lingan ekran va harakatli grafika (8 sahna turi)", "Subtitr va kalit so'z", "Ovozni tozalash", "9:16 format"] },
  { id: "dars_montaj", nom: "Dars montajchisi", guruh: "Kontent", buyum: "film", joy: "Kompyuter", jadval: "Dars videosi berilganda", holat: "ishlaydi",
    izoh: "Uzun dars videolari uchun", hujjat: ".claude/agents/montaj-agent.md",
    qobiliyat: ["Kesish va ovoz", "Slayd va animatsiya", "Qo'l protokoli", "Ko'rish uchun tayyorlash"] },
  { id: "instagram", nom: "Instagram agenti", guruh: "Kontent", buyum: "telefon", joy: "Kompyuter, Chrome", jadval: "Siz \"joyla\" deganda", holat: "ishlaydi",
    izoh: "4 ta Reels joylagan", hujjat: "agentlar/instagram_agent.md",
    qobiliyat: ["Videoni siqish (sifatni saqlab)", "Muqova yasash", "Caption", "Chrome orqali joylash"] },
  { id: "kanal", nom: "Kanal postchisi", guruh: "Kontent", buyum: "megafon", joy: "Server", jadval: "Har kuni 20:00", holat: "ishlaydi",
    izoh: "Saytda. 4 ta qoralama tasdiqlanmagan, shuning uchun post chiqmaydi", hujjat: "agentlar/kanal_postlar/README.md",
    qobiliyat: ["Tasdiqlangan postni kanalga chiqarish", "Kuniga bitta post", "Imzo va havolalar"] },
  { id: "izoh", nom: "Izoh javobchisi", guruh: "Kontent", buyum: "qurilish", joy: "Server", jadval: "", holat: "qurilmagan",
    izoh: "Meta ilovasini kutadi", hujjat: "", qobiliyat: ["Instagram izohlariga javob (rejada)"] },
  { id: "sotuv", nom: "Sotuv boti", guruh: "O'quvchilar", buyum: "suhbat", joy: "Server", jadval: "Doim (xabar kelganda)", holat: "ishlaydi",
    izoh: "Saytda, sotuv yopiq rejimida", hujjat: "agentlar/sotuv.md",
    qobiliyat: ["Savollarga javob (13 muloqot tamoyili)", "Bepul darslarga yo'naltirish", "Kerak bo'lsa ustozga uzatish", "Mavzular ro'yxatini bilish"] },
  { id: "murabbiy", nom: "O'quvchi murabbiyi", guruh: "O'quvchilar", buyum: "yurak", joy: "Server", jadval: "Har kuni 09:00", holat: "ishlaydi",
    izoh: "Saytda, ustoz ohangida. Birinchi haqiqiy xabarlar hali kuzatilmagan", hujjat: "agentlar/murabbiy.md",
    qobiliyat: ["Qayerda to'xtaganini eslatish", "Qiyin mavzuni aniqlash", "Haftalik natija", "Reja muddati haqida xabar"] },
  { id: "platforma", nom: "Platforma agenti", guruh: "Platforma", buyum: "server", joy: "Kompyuter", jadval: "Siz \"joyla\" deganda", holat: "sinovda",
    izoh: "Haqiqiy yuklash sinalmagan", hujjat: "agentlar/platforma_agent.md",
    qobiliyat: ["Videoni platformaga yuklash", "Mavzu yoki misolga bog'lash", "Dars matnini chiqarish va joylash", "Avval quruq sinov"] },
  { id: "imtihon", nom: "Imtihon tuzuvchi", guruh: "Platforma", buyum: "kolba", joy: "Kompyuter", jadval: "Buyurtma bo'lganda", holat: "ishlaydi",
    izoh: "30 talik va 43 talik variantlar", hujjat: ".claude/agents/imtihon-agent.md",
    qobiliyat: ["DTM (30 talik) variant", "Milliy sertifikat (43 talik) variant", "Hisoblarni tekshirish", "Javoblar kaliti"] },
  { id: "pdf", nom: "PDF dizayneri", guruh: "Platforma", buyum: "qogoz", joy: "Kompyuter", jadval: "Rasm yoki mavzu berilganda", holat: "sinovda",
    izoh: "Uslub tanlangan (ko'k sarlavha), sinov PDF chiqqan", hujjat: "agentlar/pdf_dizayn.md",
    qobiliyat: ["Konspekt va tarqatma", "Rasm papkasidan dars PDF'i", "Formulalarni to'g'ri yozish", "Har sahifani ko'rib tekshirish"] },
  { id: "ovozli", nom: "Ovozli yechim", guruh: "Platforma", buyum: "mikrofon", joy: "Kompyuter", jadval: "Variant berilganda", holat: "sinovda",
    izoh: "Yarim tayyor (ovoz klonini kutadi)", hujjat: "video/namuna/USLUB.md",
    qobiliyat: ["Masala yechimini ovoz bilan tushuntirish", "Ovozga mos kadrlar", "Savol-javob uslubi"] },
  { id: "nazoratchi", nom: "Nazoratchi", guruh: "Nazorat", buyum: "lupa", joy: "Server", jadval: "Har kuni 09:00", holat: "ishlaydi",
    izoh: "Saytda: o'quvchilar hisoboti va platforma tekshiruvi", hujjat: "",
    qobiliyat: ["O'quvchilar bo'yicha kunlik hisobot", "Platformadagi kamchiliklarni topish", "Xatoni kod agentiga uzatish"] },
  { id: "kod", nom: "Kod agenti", guruh: "Nazorat", buyum: "terminal", joy: "Kompyuter (Claude Code)", jadval: "Ish berilganda", holat: "ishlaydi",
    izoh: "Navbatdan o'zi ish olmaydi", hujjat: "",
    qobiliyat: ["Sayt va bot kodini yozish", "Xatolarni tuzatish", "Testlar", "Deploy (faqat \"ha\" dan keyin)"] },
  { id: "hisobchi", nom: "Hisobchi", guruh: "Nazorat", buyum: "tangalar", joy: "Server", jadval: "Har kuni 20:00 (CEO bilan)", holat: "ishlaydi",
    izoh: "Saytda", hujjat: "agentlar/ceo.md",
    qobiliyat: ["Kunlik va oylik tushum", "Faol rejalar soni", "Tugayotgan rejalar", "Tasdiq kutayotgan to'lovlar"] },
  { id: "ceo", nom: "CEO", guruh: "Nazorat", buyum: "toj", joy: "Server", jadval: "Har kuni 20:00, yakshanba: haftalik", holat: "ishlaydi",
    izoh: "Saytda. Qisqa kunlik hisobot", hujjat: "agentlar/ceo.md",
    qobiliyat: ["Kunlik qisqa hisobot", "Haftalik to'liq hisobot", "E'tibor qoidalari (6 ta)", "Sizdan kutilayotgan ishlar ro'yxati"] },
];

const DAY = 86400e3;
const qisqa = (r) => ({ id: r.id, tur: r.tur, holat: r.holat, sarlavha: r.sarlavha, kimga: r.kimga || null, vaqt: r.created_at });

// Navbat qatorlaridan har agentning holati. Sof funksiya: testda bazasiz ishlatiladi.
export function yigish(qatorlar, now = new Date()) {
  const t = now.getTime(), jonli = qatorlar.filter((r) => r.holat !== "bekor");
  const agentlar = AGENTLAR.map((a) => {
    const q = jonli.filter((r) => r.agent === a.id).sort((x, y) => new Date(y.created_at) - new Date(x.created_at));
    const ochiq = q.filter((r) => ["yangi", "jarayonda"].includes(r.holat) && ["savol", "xato"].includes(r.tur));
    const jarayonda = q.find((r) => r.holat === "jarayonda" && r.tur === "ish");
    const oxirgi = q[0] || null, soat = oxirgi ? (t - new Date(oxirgi.created_at).getTime()) / 3600e3 : null;
    const xato7 = q.filter((r) => r.tur === "xato" && t - new Date(r.created_at).getTime() < 7 * DAY).length;
    const belgi = a.holat === "qurilmagan" ? "yoq" : ochiq.some((r) => r.tur === "xato") ? "xato" : ochiq.some((r) => r.kimga === "ustoz") ? "savol" : jarayonda ? "ishlayapti" : soat != null && soat < 24 ? "faol" : "kutmoqda";
    return { ...a, belgi, hozir: jarayonda ? jarayonda.sarlavha : null, oxirgi: oxirgi ? qisqa(oxirgi) : null,
      ishlar: q.filter((r) => r.tur === "ish" || r.tur === "hisobot").slice(0, 8).map(qisqa), ochiq: ochiq.map(qisqa),
      soni: { ish: q.filter((r) => r.tur === "ish").length, hisobot: q.filter((r) => r.tur === "hisobot").length, xato7, ochiq: ochiq.length } };
  });
  const ustozga = jonli.filter((r) => r.kimga === "ustoz" && ["yangi", "jarayonda"].includes(r.holat)).sort((x, y) => new Date(x.created_at) - new Date(y.created_at))
    .map((r) => ({ ...qisqa(r), agent: r.agent }));
  const tanilmagan = [...new Set(jonli.map((r) => r.agent))].filter((id) => !AGENTLAR.some((a) => a.id === id));
  return { vaqt: now.toISOString(), agentlar, ustozga, tanilmagan };
}

// Bazadan o'qib yig'adi (oxirgi 30 kun). db: service-role mijoz. Navbat o'qilmasa agentlar baribir ko'rinadi, ogohlantirish bilan.
export async function ofisMalumot(db, now = new Date()) {
  const { data, error } = await db.from("agent_navbat").select("id,agent,tur,holat,sarlavha,kimga,created_at").gte("created_at", new Date(now.getTime() - 30 * DAY).toISOString()).order("created_at", { ascending: false }).limit(2000);
  if (error) return { ...yigish([], now), ogohlantirish: `Navbat o'qilmadi: ${error.message}` };
  return yigish(data || [], now);
}
