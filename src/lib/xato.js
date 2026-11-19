// O'quvchi brauzerida chiqqan xatolarni serverga yuboradi (api/_xato.js), shunda sayt buzilsa kod agenti biladi.
// O'quvchi kimligi yuborilmaydi: faqat xato matni, sahifa yo'li va tasodifiy qurilma belgisi (nechta qurilmada
// takrorlanganini sanash uchun). Hech qachon xato otmaydi va o'quvchiga hech narsa ko'rsatmaydi.
const MAX_SAHIFADA = 5;        // bitta sahifa ochilishida ko'pi bilan shuncha xato yuboriladi
const yuborilgan = new Set();

function qurilma() {
  try {
    let q = localStorage.getItem("kimyo-qurilma");
    if (!q) { q = Math.random().toString(36).slice(2, 14); localStorage.setItem("kimyo-qurilma", q); }
    return q;
  } catch { return ""; }
}

export function xatoYubor(xabar, stack = "") {
  try {
    const m = String(xabar || "").slice(0, 300);
    if (!m || yuborilgan.has(m) || yuborilgan.size >= MAX_SAHIFADA) return;
    if (/^script error\.?$|resizeobserver loop|failed to fetch|load failed|networkerror|aborterror/i.test(m)) return;      // sayt aybi bo'lmagan shovqin (server ham filtrlaydi)
    if (["localhost", "127.0.0.1"].includes(window.location.hostname) && !window.__xatoSinov) return;      // ishlab chiqish paytida yuborilmaydi
    yuborilgan.add(m);
    fetch("/api/purchase-request", {
      method: "POST", keepalive: true, headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "xato", xabar: m, stack: String(stack || "").slice(0, 800), sahifa: window.location.pathname + window.location.hash, qurilma: qurilma() }),
    }).catch(() => {});
  } catch { /* xato haqidagi xabar yangi xato chiqarmasin */ }
}

export function xatoKuzat() {
  window.addEventListener("error", (e) => { if (e.message) xatoYubor(e.message, e.error?.stack || `${e.filename || ""}:${e.lineno || ""}`); });
  window.addEventListener("unhandledrejection", (e) => { const r = e.reason; xatoYubor(r?.message || String(r || ""), r?.stack || ""); });
}
