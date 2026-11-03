import { useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C, card, pageTitle } from "./ui";

// Organika: random (qatlamli) jamoa qur'asi. "Ko'rib chiqish" hech narsani saqlamaydi, "Tuzish" bir marta o'tkaziladi.
export default function OyinTeamsPanel() {
  const [res, setRes] = useState(null);
  const [err, setErr] = useState("");
  const [busy, setBusy] = useState(false);
  const run = async (preview) => {
    if (!preview && !window.confirm("Jamoalar bir marta tuziladi va keyin o'zgartirilmaydi. Davom etamizmi?")) return;
    setBusy(true); setErr("");
    try {
      const { data: { session } } = await supabase.auth.getSession();
      const r = await fetch("/api/oyin", { method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${session?.access_token}` }, body: JSON.stringify({ action: "draw", preview }) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.error || "Xatolik");
      setRes(j);
    } catch (e) { setErr(e.message); }
    setBusy(false);
  };
  const btn = (bg) => ({ background: bg, color: "#fff", border: "none", borderRadius: 8, padding: "9px 16px", fontWeight: 800, fontSize: 13, cursor: busy ? "default" : "pointer", opacity: busy ? .6 : 1, marginRight: 10 });
  return (
    <div>
      <div style={pageTitle}>Organika · jamoalar qur'asi</div>
      <div style={{ fontSize: 12.5, color: C.textMid, marginBottom: 14 }}>Kamida 2 kunni bajargan o'quvchilar qatnashadi. Har jamoa ~5 kishi, kuchlari (XP) teng taqsimlanadi. 18-kundan keyin qo'shilganlar jamoaga kirmaydi.</div>
      <div style={{ marginBottom: 14 }}>
        <button style={btn(C.primary)} disabled={busy} onClick={() => run(true)}>Ko'rib chiqish (saqlanmaydi)</button>
        <button style={btn(C.danger)} disabled={busy} onClick={() => run(false)}>Jamoalarni tuzish (bir marta)</button>
      </div>
      {err && <div style={{ ...card, color: C.danger, marginBottom: 14 }}>{err}</div>}
      {res && <div>
        <div style={{ fontSize: 13, fontWeight: 800, marginBottom: 8 }}>{res.preview ? "Ko'rib chiqish: saqlanmadi" : "Jamoalar tuzildi va saqlandi"} · {res.players} o'quvchi, {res.teams.length} jamoa · seed {res.seed}</div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(250px,1fr))", gap: 12 }}>
          {res.teams.map((t) => <div key={t.name} style={card}>
            <div style={{ fontWeight: 900, color: C.primary }}>{t.name} <span style={{ fontWeight: 600, color: C.textMid }}>· {t.size} kishi · o'rtacha {Math.round(t.avgXp / 10)} ♥</span></div>
            <div style={{ fontSize: 12.5, marginTop: 6, color: C.text }}>{t.members.join(", ")}</div>
          </div>)}
        </div>
      </div>}
    </div>
  );
}
