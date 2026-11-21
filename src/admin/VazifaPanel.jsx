import { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C, card, inputStyle, btnPrimary, btnGhost, toggleBtn } from "./ui";

// Uyga vazifa va imtihon tayinlash: mavzu, savollar soni, muddat va o'quvchilar tanlanadi.
// Server: api/bunny-auth.js -> api/_vazifa.js ({ vazifa: { amal } }). Savollarni server mavzudan tasodifiy tanlaydi,
// Telegramni ulagan o'quvchilarga murabbiy xabar yuboradi, qolganlari vazifani platformada ko'radi.
async function ask(vazifa) {
  const { data: { session } } = await supabase.auth.getSession();
  const r = await fetch("/api/bunny-auth", { method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` }, body: JSON.stringify({ vazifa }) });
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(d.error || "Xatolik yuz berdi");
  return d;
}
const sana = (t) => t ? new Date(t).toLocaleDateString("ru-RU", { day: "2-digit", month: "2-digit", timeZone: "Asia/Tashkent" }) : "muddatsiz";
const TG = { ulangan: ["Telegram ulangan", C.accent], "o'chirgan": ["xabarlarni o'chirgan", C.warning], "yo'q": ["Telegram ulanmagan", C.textLight] };
const HOLAT = { bajarildi: ["Bajarildi", C.primary], jarayonda: ["Ishlayapti", C.accent], yangi: ["Boshlamagan", C.textLight], kechikkan: ["Kechikkan", C.danger] };
const label = { fontSize: 11.5, fontWeight: 700, color: C.textMid, marginBottom: 5, display: "block" };

export default function VazifaPanel() {
  const [d, setD] = useState(null);
  const [err, setErr] = useState("");
  const [f, setF] = useState({ tur: "uyga", nom: "", manba: "variant", mavzular: [], variant_id: "", soni: 10, kun: 2 });
  const [tanlangan, setTanlangan] = useState([]);
  const [faqatPullik, setFaqatPullik] = useState(true);
  const [busy, setBusy] = useState(false);
  const [xabar, setXabar] = useState("");
  const [natija, setNatija] = useState(null);

  const yukla = () => ask({ amal: "malumot" }).then(setD).catch((e) => setErr(e.message));
  useEffect(() => { yukla(); }, []);

  if (err && !d) return <div style={{ ...card, color: C.danger, fontSize: 13 }}>{err}</div>;
  if (!d) return <div style={{ ...card, fontSize: 13, color: C.textMid }}>Yuklanmoqda…</div>;

  // Savollar manbai: bitta variant yoki bir necha mavzu (bitta mavzuda savol kam bo'lishi mumkin).
  const variant = d.variantlar.find((v) => v.id === f.variant_id);
  const bor = f.manba === "variant" ? (variant?.soni || 0) : d.mavzular.filter((m) => f.mavzular.includes(m.nom)).reduce((a, m) => a + m.soni, 0);
  const manbaNom = f.manba === "variant" ? (variant?.nom || "") : f.mavzular.length === 1 ? f.mavzular[0] : f.mavzular.length ? `${f.mavzular.length} ta mavzu` : "";
  const mavzuBos = (nom) => setF((x) => ({ ...x, mavzular: x.mavzular.includes(nom) ? x.mavzular.filter((m) => m !== nom) : [...x.mavzular, nom] }));
  const royxat = d.oquvchilar.filter((o) => !faqatPullik || o.plan !== "free");
  const hammasi = royxat.length > 0 && royxat.every((o) => tanlangan.includes(o.id));
  const bos = (id) => setTanlangan((t) => t.includes(id) ? t.filter((x) => x !== id) : [...t, id]);

  const yubor = async () => {
    setBusy(true); setErr(""); setXabar("");
    try {
      const r = await ask({ amal: "yarat", tur: f.tur, soni: f.soni, kun: f.kun, nom: f.nom || standartNom, oquvchilar: tanlangan,
        ...(f.manba === "variant" ? { variant_id: f.variant_id, variant_nom: variant?.nom } : { mavzular: f.mavzular }) });
      setXabar(`Tayinlandi: ${r.oquvchilar} ta o'quvchi. Telegramga xabar ${r.yuborildi} tasiga ketdi${r.xabarsiz ? `, ${r.xabarsiz} tasi vazifani faqat platformada ko'radi` : ""}.`);
      setTanlangan([]); setF((x) => ({ ...x, nom: "" })); yukla();
    } catch (e) { setErr(e.message); }
    finally { setBusy(false); }
  };
  const standartNom = manbaNom ? `${manbaNom}: ${f.tur === "imtihon" ? "imtihon" : "uyga vazifa"}` : "";
  const tayyor = bor > 0 && tanlangan.length > 0 && f.soni >= 1 && f.soni <= bor;

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <div style={card}>
        <div style={{ fontSize: 15, fontWeight: 800, color: C.text, marginBottom: 4 }}>Vazifa tayinlash</div>
        <p style={{ fontSize: 12.5, color: C.textMid, margin: "0 0 14px", lineHeight: 1.6 }}>Savollar tanlangan variant yoki mavzulardan tasodifiy olinadi. O'quvchi platformada ishlaydi, natija darhol chiqadi. Yechim ko'rsatilmaydi.</p>

        <div style={{ display: "flex", gap: 6, marginBottom: 14 }}>
          {[["uyga", "Uyga vazifa"], ["imtihon", "Imtihon"]].map(([k, n]) => <button key={k} style={toggleBtn(f.tur === k)} onClick={() => setF({ ...f, tur: k })}>{n}</button>)}
        </div>

        <span style={label}>Savollar qayerdan olinadi</span>
        <div style={{ display: "flex", gap: 6, marginBottom: 8 }}>
          {[["variant", "Bitta variantdan"], ["mavzu", "Mavzulardan"]].map(([k, n]) => <button key={k} style={toggleBtn(f.manba === k)} onClick={() => setF({ ...f, manba: k })}>{n}</button>)}
        </div>
        {f.manba === "variant" ? (
          <select value={f.variant_id} onChange={(e) => setF({ ...f, variant_id: e.target.value })} style={{ ...inputStyle, marginBottom: 14 }}>
            <option value="">Variantni tanlang…</option>
            {d.variantlar.map((v) => <option key={v.id} value={v.id}>{v.nom} ({v.soni} ta savol)</option>)}
          </select>
        ) : (
          <div style={{ maxHeight: 190, overflowY: "auto", border: `1px solid ${C.border}`, borderRadius: 10, marginBottom: 14, padding: "4px 0" }}>
            {d.mavzular.map((m) => (
              <label key={m.nom} style={{ display: "flex", alignItems: "center", gap: 9, padding: "5px 12px", cursor: "pointer", fontSize: 12.5 }}>
                <input type="checkbox" checked={f.mavzular.includes(m.nom)} onChange={() => mavzuBos(m.nom)} />
                <span style={{ flex: 1, color: C.text }}>{m.nom}</span><span style={{ color: C.textLight }}>{m.soni} ta</span>
              </label>
            ))}
          </div>
        )}
        {bor > 0 && <p style={{ fontSize: 12, color: C.textMid, margin: "-6px 0 12px" }}>Tanlangan manbada {bor} ta yaroqli savol bor.</p>}

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(170px,1fr))", gap: 12 }}>
          <label><span style={label}>Savollar soni</span>
            <input type="number" min={1} max={43} value={f.soni} onChange={(e) => setF({ ...f, soni: Number(e.target.value) })} style={inputStyle} /></label>
          <label><span style={label}>Muddat (kun)</span>
            <input type="number" min={1} max={60} value={f.kun} onChange={(e) => setF({ ...f, kun: Number(e.target.value) })} style={inputStyle} /></label>
          <label><span style={label}>Nomi (ixtiyoriy)</span>
            <input value={f.nom} maxLength={120} placeholder={standartNom || "Masalan: pH va pOH hisoblash"} onChange={(e) => setF({ ...f, nom: e.target.value })} style={inputStyle} /></label>
        </div>
        {bor > 0 && f.soni > bor && <p style={{ fontSize: 12, color: C.danger, margin: "8px 0 0" }}>Tanlangan manbada faqat {bor} ta yaroqli savol bor.</p>}
        {!d.mavzular.length && <p style={{ fontSize: 12, color: C.warning, margin: "8px 0 0" }}>Bazada mavzusi belgilangan, to'rt javobli va to'g'ri javobi kiritilgan savol topilmadi.</p>}

        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", margin: "18px 0 8px", gap: 8, flexWrap: "wrap" }}>
          <span style={{ ...label, margin: 0 }}>O'quvchilar ({tanlangan.length} ta tanlandi)</span>
          <div style={{ display: "flex", gap: 6 }}>
            <button style={toggleBtn(faqatPullik)} onClick={() => setFaqatPullik(!faqatPullik)}>Faqat pullik</button>
            <button style={btnGhost} onClick={() => setTanlangan(hammasi ? tanlangan.filter((id) => !royxat.some((o) => o.id === id)) : [...new Set([...tanlangan, ...royxat.map((o) => o.id)])])}>{hammasi ? "Belgini olish" : "Hammasini belgilash"}</button>
          </div>
        </div>
        <div style={{ maxHeight: 260, overflowY: "auto", border: `1px solid ${C.border}`, borderRadius: 10 }}>
          {royxat.length === 0 && <div style={{ padding: 14, fontSize: 12.5, color: C.textMid }}>O'quvchi yo'q.</div>}
          {royxat.map((o) => (
            <label key={o.id} style={{ display: "flex", alignItems: "center", gap: 10, padding: "9px 12px", borderBottom: `1px solid ${C.border}`, cursor: "pointer", fontSize: 13 }}>
              <input type="checkbox" checked={tanlangan.includes(o.id)} onChange={() => bos(o.id)} />
              <span style={{ flex: 1, fontWeight: 600, color: C.text }}>{o.ism}</span>
              <span style={{ fontSize: 11, color: C.textMid }}>{o.plan === "free" ? "bepul" : o.plan}</span>
              <span style={{ fontSize: 11, fontWeight: 700, color: TG[o.telegram][1] }}>{TG[o.telegram][0]}</span>
            </label>
          ))}
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: 12, marginTop: 14, flexWrap: "wrap" }}>
          <button style={{ ...btnPrimary, opacity: tayyor && !busy ? 1 : 0.5 }} disabled={!tayyor || busy} onClick={yubor}>{busy ? "Tayinlanmoqda…" : f.tur === "imtihon" ? "Imtihonni tayinlash" : "Vazifani tayinlash"}</button>
          {xabar && <span style={{ fontSize: 12.5, color: C.primary, fontWeight: 600 }}>{xabar}</span>}
          {err && <span style={{ fontSize: 12.5, color: C.danger }}>{err}</span>}
        </div>
      </div>

      <div style={card}>
        <div style={{ fontSize: 15, fontWeight: 800, color: C.text, marginBottom: 10 }}>Tayinlangan vazifalar</div>
        {d.vazifalar.length === 0 && <p style={{ fontSize: 12.5, color: C.textMid, margin: 0 }}>Hali vazifa tayinlanmagan.</p>}
        {d.vazifalar.map((v) => (
          <div key={v.id} style={{ borderTop: `1px solid ${C.border}`, padding: "10px 0" }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
              <span style={{ fontSize: 10.5, fontWeight: 800, letterSpacing: 0.6, color: v.tur === "imtihon" ? C.warning : C.accent }}>{v.tur === "imtihon" ? "IMTIHON" : "UYGA VAZIFA"}</span>
              <span style={{ flex: 1, minWidth: 160, fontSize: 13.5, fontWeight: 700, color: C.text }}>{v.nom}</span>
              <span style={{ fontSize: 12, color: C.textMid }}>{v.soni} savol · {sana(v.muddat)}</span>
              <span style={{ fontSize: 12, fontWeight: 700, color: C.primary }}>{v.bajargan} / {v.berilgan} bajardi{v.ortacha != null ? ` · o'rtacha ${v.ortacha}%` : ""}</span>
              <button style={btnGhost} onClick={() => natija?.vazifa.id === v.id ? setNatija(null) : ask({ amal: "natija", id: v.id }).then(setNatija).catch((e) => setErr(e.message))}>{natija?.vazifa.id === v.id ? "Yopish" : "Natijalar"}</button>
            </div>
            {natija?.vazifa.id === v.id && (
              <div style={{ marginTop: 8, background: C.bgSoft, borderRadius: 8, padding: "6px 12px" }}>
                {natija.oquvchilar.map((o, i) => (
                  <div key={i} style={{ display: "flex", gap: 10, padding: "6px 0", fontSize: 12.5, borderBottom: i < natija.oquvchilar.length - 1 ? `1px solid ${C.border}` : "none" }}>
                    <span style={{ flex: 1, fontWeight: 600, color: C.text }}>{o.ism}</span>
                    <span style={{ color: C.textMid }}>{o.holat === "bajarildi" ? `${o.togri} / ${o.jami}` : o.javob_berilgan ? `${o.javob_berilgan} ta javob` : ""}</span>
                    <span style={{ fontWeight: 700, color: HOLAT[o.holat][1], minWidth: 86, textAlign: "right" }}>{HOLAT[o.holat][0]}</span>
                    <span style={{ color: C.textLight, minWidth: 66, textAlign: "right" }}>{o.telegram ? "xabar ketgan" : "xabarsiz"}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
