import { useEffect, useState } from "react";
import { C } from "./theme";

// Profildagi "Telegramni ulash" kartasi: ulangan o'quvchiga bot bir necha kun kirmasa muloyim eslatma yuboradi.
// Server: api/purchase-request.js -> api/_tglink.js ({ action: "tg-link" | "tg-status" }).
const call = (session, action) =>
  fetch("/api/purchase-request", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` },
    body: JSON.stringify({ action }),
  }).then(async (r) => ({ ok: r.ok, data: await r.json().catch(() => ({})) }));

export default function TelegramLink({ session }) {
  const [st, setSt] = useState(null);       // { linked, remind } | null (yuklanmoqda)
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");
  const [opened, setOpened] = useState(false);

  const load = () => call(session, "tg-status").then(({ ok, data }) => { if (ok) setSt(data); }).catch(() => {});
  useEffect(() => { if (session) load(); }, [session?.user?.id]);

  const connect = async () => {
    setBusy(true); setErr("");
    try {
      const { ok, data } = await call(session, "tg-link");
      if (!ok || !data.url) { setErr(data.error || "Havola yaratilmadi. Birozdan so'ng urinib ko'ring."); return; }
      setOpened(true);
      if (!window.open(data.url, "_blank")) window.location.href = data.url;
    } catch { setErr("Internet bilan muammo. Qayta urinib ko'ring."); }
    finally { setBusy(false); }
  };

  const btn = (primary) => ({ padding: "10px 16px", borderRadius: 10, border: primary ? "none" : `1px solid ${C.border}`, background: primary ? C.primary : "#fff", color: primary ? "#fff" : C.primary, fontSize: 12.5, fontWeight: 700, cursor: "pointer", fontFamily: "inherit" });

  return (
    <div style={{ background: "#fff", border: `1px solid ${C.border}`, borderRadius: 14, padding: "16px 18px", marginBottom: 14 }}>
      <div style={{ fontSize: 13, fontWeight: 800, color: C.text, marginBottom: 4 }}>Telegram eslatmalari</div>
      {st?.linked ? (
        <p style={{ fontSize: 12.5, color: C.textMid, lineHeight: 1.65, margin: 0 }}>
          ✅ Telegram ulangan. {st.remind ? "Bir necha kun kirmasangiz, bot sizga muloyim eslatma yuboradi. To'xtatish uchun botga /stop deb yozing." : "Eslatmalar o'chirilgan. Qayta yoqish uchun pastdagi tugma bilan qayta ulang."}
        </p>
      ) : (
        <p style={{ fontSize: 12.5, color: C.textMid, lineHeight: 1.65, margin: 0 }}>
          Telegramni ulasangiz, bir necha kun kirmasangiz bot sizga muloyim eslatma yuboradi va savollaringizga javob beradi. Istalgan payt /stop bilan to'xtatasiz.
        </p>
      )}
      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 12 }}>
        {(!st?.linked || !st?.remind) && <button onClick={connect} disabled={busy} style={btn(true)}>{busy ? "Ochilmoqda…" : st?.linked ? "Qayta ulash" : "Telegramni ulash"}</button>}
        {opened && <button onClick={load} style={btn(false)}>Ulanganini tekshirish</button>}
      </div>
      {opened && !st?.linked && <p style={{ fontSize: 11.5, color: C.textLight, margin: "8px 0 0" }}>Telegram ochilgach botda "Start" tugmasini bosing, so'ng shu yerga qaytib "Ulanganini tekshirish"ni bosing.</p>}
      {err && <p style={{ fontSize: 12, color: C.danger, margin: "8px 0 0" }}>{err}</p>}
    </div>
  );
}
