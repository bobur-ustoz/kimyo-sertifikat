import { useState } from "react";
import { C } from "./theme";

// Profildagi "Muammo haqida xabar berish" kartasi: o'quvchi saytdagi nosozlikni bir necha so'z bilan yozadi.
// Server: api/purchase-request.js -> api/_xato.js ({ action: "xato-xabar" }); xabar kod agentiga va ustozga boradi.
export default function XatoXabar({ session }) {
  const [ochiq, setOchiq] = useState(false);
  const [matn, setMatn] = useState("");
  const [holat, setHolat] = useState("");      // "" | "yuborilmoqda" | "yuborildi"
  const [err, setErr] = useState("");
  if (!session) return null;

  const yubor = async () => {
    if (matn.trim().length < 5) { setErr("Nima bo'lganini qisqacha yozing."); return; }
    setHolat("yuborilmoqda"); setErr("");
    try {
      const r = await fetch("/api/purchase-request", {
        method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` },
        body: JSON.stringify({ action: "xato-xabar", matn, sahifa: window.location.pathname + window.location.hash }),
      });
      const d = await r.json().catch(() => ({}));
      if (!r.ok) { setErr(d.error || "Yuborilmadi. Birozdan so'ng urinib ko'ring."); setHolat(""); return; }
      setHolat("yuborildi"); setMatn("");
    } catch { setErr("Internet bilan muammo. Qayta urinib ko'ring."); setHolat(""); }
  };

  const btn = (primary) => ({ padding: "10px 16px", borderRadius: 10, border: primary ? "none" : `1px solid ${C.border}`, background: primary ? C.primary : "#fff", color: primary ? "#fff" : C.primary, fontSize: 13, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" });
  return (
    <div style={{ background: "#fff", border: `1px solid ${C.border}`, borderRadius: 14, padding: "16px 18px", marginBottom: 14 }}>
      <div style={{ fontSize: 13, fontWeight: 800, color: C.text, marginBottom: 4 }}>Saytda muammo bormi?</div>
      {holat === "yuborildi" ? (
        <p style={{ fontSize: 12.5, color: C.ok, lineHeight: 1.65, margin: 0 }}>Rahmat, xabaringiz yetib bordi. Ko'rib chiqamiz.</p>
      ) : !ochiq ? (
        <>
          <p style={{ fontSize: 12.5, color: C.textMid, lineHeight: 1.65, margin: 0 }}>Video ochilmasa, test ishlamasa yoki biror joy noto'g'ri ko'rinsa, bizga yozing.</p>
          <div style={{ marginTop: 12 }}><button onClick={() => setOchiq(true)} style={btn(false)}>Muammo haqida xabar berish</button></div>
        </>
      ) : (
        <>
          <textarea value={matn} onChange={(e) => setMatn(e.target.value)} maxLength={1000} rows={4} placeholder="Masalan: 5-mavzuning videosi ochilmayapti"
            style={{ width: "100%", boxSizing: "border-box", marginTop: 6, padding: "10px 12px", borderRadius: 10, border: `1px solid ${C.border}`, fontSize: 14, fontFamily: "inherit", color: C.text, resize: "vertical" }} />
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>
            <button onClick={yubor} disabled={holat === "yuborilmoqda"} style={btn(true)}>{holat === "yuborilmoqda" ? "Yuborilmoqda…" : "Yuborish"}</button>
            <button onClick={() => { setOchiq(false); setErr(""); }} style={btn(false)}>Bekor qilish</button>
          </div>
        </>
      )}
      {err && <p style={{ fontSize: 12, color: C.danger, margin: "8px 0 0" }}>{err}</p>}
    </div>
  );
}
