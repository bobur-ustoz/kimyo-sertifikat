import { useEffect, useRef, useState } from "react";
import { C } from "./theme";
import { supabase } from "./lib/supabaseClient";

// "Telegram orqali kirish": ro'yxatdan o'tish va kirish bitta tugma. Parol kerak emas.
// Oqim: tugma -> server kod beradi -> botda telefon raqam ulashiladi -> sayt kirish tokenini olib sessiya ochadi.
// Server: api/purchase-request.js -> api/_tgauth.js. Sir (secret) faqat shu brauzerda turadi: havolani olgan begona
// odam uni bilmagani uchun boshqa odamning brauzerini o'z hisobiga kirita olmaydi.
const POLL_MS = 2000;

const post = (body) =>
  fetch("/api/purchase-request", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) })
    .then(async (r) => ({ ok: r.ok, data: await r.json().catch(() => ({})) }));

const makeSecret = () => Array.from(crypto.getRandomValues(new Uint8Array(16)), (b) => b.toString(16).padStart(2, "0")).join("");

export default function TelegramLogin() {
  const [phase, setPhase] = useState("idle");   // idle | starting | waiting
  const [url, setUrl] = useState("");
  const [err, setErr] = useState("");
  const timer = useRef(null);
  const run = useRef(0);                         // bekor qilingan/eskirgan urinishni ajratish uchun

  const stop = () => { run.current++; clearInterval(timer.current); };
  useEffect(() => stop, []);

  const reset = (msg = "") => { stop(); setPhase("idle"); setUrl(""); setErr(msg); };

  const start = async () => {
    stop();
    const me = run.current;
    setPhase("starting"); setErr("");
    const secret = makeSecret();
    let started;
    try { started = await post({ action: "tg-login-start", secret }); } catch { return reset("Internet bilan muammo. Qayta urinib ko'ring."); }
    if (me !== run.current) return;
    if (!started.ok || !started.data.url) return reset(started.data.error || "Havola yaratilmadi. Birozdan so'ng urinib ko'ring.");

    setUrl(started.data.url); setPhase("waiting");
    if (!window.open(started.data.url, "_blank")) window.location.href = started.data.url;

    const deadline = Date.now() + (started.data.minutes || 10) * 60e3;
    timer.current = setInterval(async () => {
      if (me !== run.current) return;
      if (Date.now() > deadline) return reset("Vaqt tugadi. Tugmani qayta bosing.");
      let r;
      try { r = await post({ action: "tg-login-poll", code: started.data.code, secret }); } catch { return; }   // tarmoq uzilsa, keyingi urinishda
      if (me !== run.current) return;
      if (r.data.status === "expired") return reset("Havola eskirgan. Tugmani qayta bosing.");
      if (r.data.status !== "ok") return;
      stop();
      const { error } = await supabase.auth.verifyOtp({ token_hash: r.data.token_hash, type: "magiclink" });
      if (error) reset("Kirishda xatolik. Qayta urinib ko'ring.");
      // Muvaffaqiyatda sessiya ochiladi va ilova o'zi yangilanadi.
    }, POLL_MS);
  };

  const main = { width: "100%", padding: "13px", borderRadius: 10, background: "#229ED9", color: "#fff", border: "none", fontSize: 14, fontWeight: 800, cursor: "pointer", fontFamily: "inherit" };

  return (
    <div>
      {phase !== "waiting" ? (
        <>
          <button type="button" onClick={start} disabled={phase === "starting"} style={main}>
            {phase === "starting" ? "Ochilmoqda…" : "✈️ Telegram orqali kirish"}
          </button>
          <p style={{ fontSize: 12, color: C.textMid, lineHeight: 1.6, margin: "10px 0 0", textAlign: "center" }}>
            Ro'yxatdan o'tish ham shu tugma bilan. Parol va email kerak emas.
          </p>
        </>
      ) : (
        <div style={{ background: "#F0F9FF", border: "1px solid #BAE6FD", borderRadius: 12, padding: "14px 16px" }}>
          <div style={{ fontSize: 13, fontWeight: 800, color: C.text, marginBottom: 6 }}>Telegramda tasdiqlang</div>
          <ol style={{ fontSize: 12.5, color: C.textMid, lineHeight: 1.75, margin: "0 0 10px", paddingLeft: 18 }}>
            <li>Botda <b>Start</b> tugmasini bosing.</li>
            <li><b>"📱 Raqamni ulashish"</b> tugmasini bosing.</li>
            <li>Shu oyna o'zi kiradi.</li>
          </ol>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", alignItems: "center" }}>
            <a href={url} target="_blank" rel="noreferrer" style={{ fontSize: 12.5, fontWeight: 700, color: "#0284C7" }}>Telegram ochilmadimi? Bu yerni bosing</a>
            <button type="button" onClick={() => reset()} style={{ marginLeft: "auto", background: "none", border: "none", color: C.textLight, fontSize: 12, cursor: "pointer", fontFamily: "inherit", textDecoration: "underline" }}>Bekor qilish</button>
          </div>
        </div>
      )}
      {err && <div style={{ color: C.danger, fontSize: 12, marginTop: 10, textAlign: "center" }}>{err}</div>}
    </div>
  );
}

// Telegram hisobining email'i haqiqiy emas (tg123@example.com): foydalanuvchiga ismini ko'rsatamiz.
export const userLabel = (session) => {
  const u = session?.user;
  if (!u) return "";
  return /^tg\d+@example\.com$/.test(u.email || "") ? (u.user_metadata?.full_name || "Telegram hisobi") : u.email;
};
