import { useEffect, useState } from "react";
import { ChevronLeft, Download, Lock, CheckCircle2 } from "lucide-react";
import { C } from "./theme";

// "Vazifalarim": ustoz tayinlagan uyga vazifa va imtihonlar. O'quvchi bitta ekranda bitta savolga javob beradi,
// topshirgach natija darhol chiqadi. Yechim ko'rsatilmaydi (ustoz qarori): faqat to'g'ri javob harfi.
// Server: api/purchase-request.js -> api/_vazifa.js ({ action: "vazifa-..." }); to'g'ri javoblar topshirguncha kelmaydi.
const call = (session, body) => fetch("/api/purchase-request", {
  method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` }, body: JSON.stringify(body),
}).then(async (r) => { const d = await r.json().catch(() => ({})); if (!r.ok) throw new Error(d.error || "Xatolik yuz berdi"); return d; });

const HARF = ["A", "B", "C", "D"];
const TUR = { uyga: "UYGA VAZIFA", imtihon: "IMTIHON" };
const sana = (t) => new Date(t).toLocaleDateString("ru-RU", { day: "2-digit", month: "2-digit", timeZone: "Asia/Tashkent" });
function muddatMatn(m, now = Date.now()) {
  if (!m) return null;
  const kun = Math.ceil((new Date(m).getTime() - now) / 86400e3);
  return kun < 0 ? "Muddati o'tgan" : kun <= 1 ? "Bugun-erta tugaydi" : `${kun} kun qoldi`;
}

// Savollarni platformaning test PDF'i ko'rinishida yuklab beradi (yechimsiz, javobsiz).
async function pdfYukla(vazifa, savollar) {
  const [{ jsPDF }, { buildTestPdf }] = await Promise.all([import("jspdf"), import("./testPdf")]);
  const doc = new jsPDF();
  const font = async (file, style, family) => {
    const bytes = new Uint8Array(await (await fetch(file)).arrayBuffer());
    let bin = ""; for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
    const name = file.split("/").pop(); doc.addFileToVFS(name, btoa(bin)); doc.addFont(name, family, style);
  };
  await Promise.all([font("/fonts/LMRoman-Regular.ttf", "normal", "LM"), font("/fonts/LMRoman-Bold.ttf", "bold", "LM"), font("/fonts/LMRoman-Slanted.ttf", "normal", "LMSl"), font("/fonts/DejaVuSans.ttf", "normal", "DejaVu")]);
  buildTestPdf(doc, { questions: savollar, label: vazifa.tur === "imtihon" ? "Imtihon" : "Uyga vazifa", subtitle: `${vazifa.nom} · ${savollar.length} ta savol` });
  doc.save(`${vazifa.nom.replace(/[^\p{L}\p{N}-]+/gu, "_")}.pdf`);
}

const btn = (primary, extra = {}) => ({ padding: "12px 16px", borderRadius: 10, border: primary ? "none" : `1px solid ${C.border}`, background: primary ? C.primary : "#fff", color: primary ? "#fff" : C.primary, fontSize: 14, fontWeight: 700, cursor: "pointer", fontFamily: "inherit", ...extra });
const karta = { background: "#fff", border: `1px solid ${C.border}`, borderRadius: 14, padding: "14px 16px", marginBottom: 12 };

export default function Vazifalar({ session, setTab }) {
  const [royxat, setRoyxat] = useState(null);
  const [err, setErr] = useState("");
  const [ochiq, setOchiq] = useState(null);      // { vazifa, savollar, javoblar, natija? }
  const [i, setI] = useState(0);
  const [busy, setBusy] = useState(false);
  const [pdfBusy, setPdfBusy] = useState(false);

  const yukla = () => call(session, { action: "vazifa-royxat" }).then((d) => setRoyxat(d.vazifalar)).catch((e) => { setErr(e.message); setRoyxat([]); });
  useEffect(() => { if (session) yukla(); }, [session?.user?.id]);

  if (!session) return (
    <div style={{ maxWidth: 520, margin: "40px auto", textAlign: "center", padding: "0 20px" }}>
      <div style={{ fontSize: 18, fontWeight: 800, color: C.text, marginBottom: 8 }}>Vazifalarim</div>
      <p style={{ fontSize: 14, color: C.textMid, marginBottom: 16 }}>Vazifalarni ko'rish uchun hisobingizga kiring.</p>
      <button style={btn(true)} onClick={() => setTab("profile")}>Kirish</button>
    </div>
  );

  const och = async (id) => {
    setErr(""); setBusy(true);
    try { const d = await call(session, { action: "vazifa-ol", id }); setOchiq(d); setI(Math.min(Object.keys(d.javoblar || {}).length, d.savollar.length - 1)); }
    catch (e) { setErr(e.message); } finally { setBusy(false); }
  };
  const pdf = async (v, savollar) => { setPdfBusy(true); try { await pdfYukla(v, savollar); } catch { setErr("PDF tayyorlanmadi. Qayta urinib ko'ring."); } finally { setPdfBusy(false); } };

  // ---------- bitta vazifa ----------
  if (ochiq) {
    const { vazifa, savollar, javoblar, natija } = ochiq;
    const yop = () => { setOchiq(null); yukla(); };
    const bosh = (
      <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
        <button onClick={yop} aria-label="Orqaga" style={{ background: "none", border: "none", cursor: "pointer", color: C.primary, display: "flex", padding: 4 }}><ChevronLeft size={24} /></button>
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{ fontSize: 10.5, fontWeight: 800, letterSpacing: 1.2, color: C.primary }}>{TUR[vazifa.tur]}</div>
          <div style={{ fontSize: 16, fontWeight: 800, color: C.text, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{vazifa.nom}</div>
        </div>
        {(vazifa.tur !== "imtihon" || natija) && <button onClick={() => pdf(vazifa, savollar)} disabled={pdfBusy} title="Savollarni PDF qilib yuklab olish" style={btn(false, { padding: "8px 12px", fontSize: 12.5, display: "flex", alignItems: "center", gap: 6 })}><Download size={14} />{pdfBusy ? "Tayyorlanmoqda…" : "PDF"}</button>}
      </div>
    );

    if (natija) {
      const foiz = Math.round((natija.togri / natija.jami) * 100);
      return (
        <div style={{ maxWidth: 620, margin: "0 auto", padding: "18px 16px 30px" }}>
          {bosh}
          <div style={{ ...karta, textAlign: "center", padding: "22px 16px" }}>
            <div style={{ fontSize: 10.5, fontWeight: 800, letterSpacing: 1.4, color: C.primary }}>NATIJA</div>
            <div style={{ fontSize: 44, fontWeight: 800, color: C.navy, lineHeight: 1.15 }}>{natija.togri} <span style={{ fontSize: 22, color: C.textLight }}>/ {natija.jami}</span></div>
            <div style={{ fontSize: 13, color: C.textMid }}>{foiz >= 80 ? "Barakalla, yaxshi natija" : foiz >= 50 ? "Yomon emas, xatolarni ko'rib chiqing" : "Xavotir olmang, mavzuni yana bir ko'rib chiqing"}</div>
          </div>
          {savollar.map((q, k) => {
            const t = natija.tafsil.find((x) => x.id === q.id) || {};
            return (
              <div key={q.id} style={{ ...karta, borderLeft: `4px solid ${t.togri ? C.ok : C.danger}` }}>
                <div style={{ fontSize: 10.5, fontWeight: 800, letterSpacing: 1, color: t.togri ? C.ok : C.danger, marginBottom: 4 }}>{k + 1}-SAVOL · {t.togri ? "TO'G'RI" : "XATO"}</div>
                <div style={{ fontSize: 14, fontWeight: 600, color: C.text, lineHeight: 1.5 }}>{q.question_text}</div>
                {q.formula && <div style={{ fontSize: 13, color: C.textMid, marginTop: 4 }}>{q.formula}</div>}
                <div style={{ display: "flex", gap: 16, flexWrap: "wrap", marginTop: 8, fontSize: 13 }}>
                  <span style={{ color: C.textMid }}>Siz: <b style={{ color: t.togri ? C.ok : C.danger }}>{t.tanlangan ? `${t.tanlangan}) ${q[`option_${t.tanlangan.toLowerCase()}`]}` : "javob berilmagan"}</b></span>
                  {!t.togri && <span style={{ color: C.textMid }}>To'g'ri: <b style={{ color: C.ok }}>{t.togri_javob}) {q[`option_${t.togri_javob.toLowerCase()}`]}</b></span>}
                </div>
              </div>
            );
          })}
          <button style={btn(true, { width: "100%" })} onClick={yop}>Vazifalarimga qaytish</button>
        </div>
      );
    }

    const q = savollar[i], tanlangan = javoblar[q.id];
    const berilgan = Object.keys(javoblar).length;
    const tanla = (h) => {
      const yangi = { ...javoblar, [q.id]: h };
      setOchiq({ ...ochiq, javoblar: yangi });
      call(session, { action: "vazifa-saqla", id: vazifa.id, javoblar: yangi }).catch(() => {});      // saqlanmasa ham topshirishda hammasi ketadi
    };
    const topshir = async () => {
      if (berilgan < savollar.length && !window.confirm(`${savollar.length - berilgan} ta savolga javob bermadingiz. Baribir topshirasizmi?`)) return;
      setBusy(true); setErr("");
      try { const d = await call(session, { action: "vazifa-topshir", id: vazifa.id, javoblar }); setOchiq({ ...ochiq, natija: d.natija }); window.scrollTo(0, 0); }
      catch (e) { setErr(e.message); } finally { setBusy(false); }
    };
    return (
      <div style={{ maxWidth: 620, margin: "0 auto", padding: "18px 16px 30px" }}>
        {bosh}
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, color: C.textMid, marginBottom: 6 }}><span>{i + 1} / {savollar.length}</span><span>{berilgan} ta javob berildi</span></div>
        <div style={{ height: 5, borderRadius: 4, background: C.mintLight, overflow: "hidden", marginBottom: 18 }}><div style={{ height: "100%", width: `${((i + 1) / savollar.length) * 100}%`, background: C.primary }} /></div>
        <div style={{ fontSize: 10.5, fontWeight: 800, letterSpacing: 1.4, color: C.primary }}>{i + 1}-SAVOL</div>
        <div style={{ fontSize: 17, fontWeight: 600, color: C.text, lineHeight: 1.5, margin: "6px 0 4px" }}>{q.question_text}</div>
        {q.formula && <div style={{ fontSize: 14.5, color: C.textMid, marginBottom: 6 }}>{q.formula}</div>}
        <div style={{ display: "grid", gap: 9, margin: "14px 0 18px" }}>
          {HARF.map((h) => {
            const on = tanlangan === h;
            return (
              <button key={h} onClick={() => tanla(h)} aria-pressed={on}
                style={{ display: "flex", alignItems: "center", gap: 12, textAlign: "left", padding: "12px 14px", borderRadius: 12, border: `${on ? 2 : 1.2}px solid ${on ? C.primary : C.border}`, background: on ? C.mintBg : "#fff", fontSize: 15.5, fontWeight: 600, color: C.text, cursor: "pointer", fontFamily: "inherit" }}>
                <span style={{ flex: "none", width: 28, height: 28, borderRadius: "50%", background: on ? C.primary : C.mintBg, color: on ? "#fff" : C.primary, fontSize: 12.5, fontWeight: 800, display: "flex", alignItems: "center", justifyContent: "center" }}>{h}</span>
                {q[`option_${h.toLowerCase()}`]}
              </button>
            );
          })}
        </div>
        {err && <p style={{ fontSize: 12.5, color: C.danger, margin: "0 0 10px" }}>{err}</p>}
        <div style={{ display: "flex", gap: 10 }}>
          <button style={btn(false, { flex: 1, opacity: i === 0 ? 0.45 : 1 })} disabled={i === 0} onClick={() => setI(i - 1)}>Orqaga</button>
          {i < savollar.length - 1
            ? <button style={btn(true, { flex: 1 })} onClick={() => setI(i + 1)}>Keyingi</button>
            : <button style={btn(true, { flex: 1 })} disabled={busy} onClick={topshir}>{busy ? "Tekshirilmoqda…" : "Topshirish"}</button>}
        </div>
      </div>
    );
  }

  // ---------- ro'yxat ----------
  return (
    <div style={{ maxWidth: 620, margin: "0 auto", padding: "18px 16px 30px" }}>
      <div style={{ fontSize: 22, fontWeight: 800, color: C.text }}>Vazifalarim</div>
      <p style={{ fontSize: 13, color: C.textMid, margin: "2px 0 16px" }}>Ustoz tayinlagan uyga vazifa va imtihonlar</p>
      {err && <p style={{ fontSize: 12.5, color: C.danger, margin: "0 0 10px" }}>{err}</p>}
      {royxat === null && <div style={{ ...karta, fontSize: 13, color: C.textMid }}>Yuklanmoqda…</div>}
      {royxat?.length === 0 && !err && <div style={{ ...karta, fontSize: 13.5, color: C.textMid, lineHeight: 1.6 }}>Hozircha sizga vazifa berilmagan. Ustoz tayinlaganda shu yerda ko'rinadi.</div>}
      {royxat?.map((v) => {
        const bajarildi = v.holat === "bajarildi", m = muddatMatn(v.muddat);
        return (
          <div key={v.id} style={{ ...karta, border: bajarildi ? `1px solid ${C.border}` : `1.5px solid ${C.primary}` }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 6, gap: 8 }}>
              <span style={{ fontSize: 9.5, fontWeight: 800, letterSpacing: 1.2, background: bajarildi ? C.mintBg : C.primary, color: bajarildi ? C.primary : "#fff", padding: "3px 9px", borderRadius: 20 }}>{TUR[v.tur]}</span>
              {bajarildi
                ? <span style={{ display: "flex", alignItems: "center", gap: 4, fontSize: 12, fontWeight: 700, color: C.ok }}><CheckCircle2 size={14} />{v.togri} / {v.jami}</span>
                : m && <span style={{ fontSize: 11, fontWeight: 700, color: v.holat === "kechikkan" ? C.danger : C.warning, background: v.holat === "kechikkan" ? C.dangerBg : C.warningBg, padding: "3px 9px", borderRadius: 20 }}>{m}</span>}
            </div>
            <div style={{ fontSize: 15.5, fontWeight: 800, color: C.text }}>{v.nom}</div>
            <div style={{ fontSize: 12.5, color: C.textMid, marginTop: 2 }}>{v.soni} ta savol{!bajarildi && v.javob_berilgan ? ` · ${v.javob_berilgan} tasi bajarildi` : ""}{v.muddat ? ` · ${sana(v.muddat)} gacha` : ""}</div>
            {!bajarildi && v.javob_berilgan > 0 && <div style={{ height: 5, borderRadius: 4, background: C.mintLight, overflow: "hidden", marginTop: 9 }}><div style={{ height: "100%", width: `${(v.javob_berilgan / v.soni) * 100}%`, background: C.primary }} /></div>}
            <button style={btn(!bajarildi, { width: "100%", marginTop: 11 })} disabled={busy} onClick={() => och(v.id)}>{bajarildi ? "Natijani ko'rish" : v.javob_berilgan ? "Davom etish" : "Boshlash"}</button>
            {v.tur === "imtihon" && !bajarildi && <div style={{ display: "flex", alignItems: "center", gap: 5, fontSize: 11.5, color: C.textLight, marginTop: 7 }}><Lock size={12} />PDF imtihon topshirilgach ochiladi</div>}
          </div>
        );
      })}
    </div>
  );
}
