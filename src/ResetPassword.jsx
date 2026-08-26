import { useEffect, useState } from "react";
import { FlaskConical, CheckCircle2 } from "lucide-react";
import { supabase } from "./lib/supabaseClient";
import { C, card, inputStyle, btnPrimary, fieldLabel } from "./admin/ui";

// Where the recovery email lands. Supabase puts a one-time token in the URL
// fragment; supabase-js picks it up on load and signs the user in just long
// enough for them to set a new password.
export const RESET_PATH = "/parol-yangilash";

// Supabase answers in English, and its most common refusal here is a rate
// limit that reads like a failure rather than "wait a moment".
export function resetErrorText(err) {
  const msg = err?.message || "";
  if (/after (\d+) seconds?/i.test(msg)) {
    const secs = msg.match(/after (\d+) seconds?/i)[1];
    return `Juda tez-tez so'radingiz. ${secs} soniyadan keyin qayta urinib ko'ring.`;
  }
  if (/rate limit/i.test(msg)) return "Bugun juda ko'p xat yuborildi. Bir soatdan keyin urinib ko'ring.";
  if (/invalid/i.test(msg) && /email/i.test(msg)) return "Email manzil noto'g'ri yozilgan.";
  return msg || "Xat yuborilmadi. Birozdan keyin urinib ko'ring.";
}

export default function ResetPassword() {
  const [ready, setReady] = useState(false);   // did the recovery link check out?
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState("");
  const [done, setDone] = useState(false);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    // The token may already be consumed by the time we mount, so check for an
    // existing session too rather than waiting only for the event.
    const { data: sub } = supabase.auth.onAuthStateChange((event) => {
      if (event === "PASSWORD_RECOVERY" || event === "SIGNED_IN") setReady(true);
    });
    supabase.auth.getSession().then(({ data }) => { if (data.session) setReady(true); });
    return () => sub.subscription.unsubscribe();
  }, []);

  const submit = async (e) => {
    e.preventDefault();
    if (password !== confirm) { setError("Parollar mos kelmadi."); return; }
    if (password.length < 6) { setError("Parol kamida 6 ta belgidan iborat bo'lsin."); return; }
    setBusy(true);
    setError("");
    const { error } = await supabase.auth.updateUser({ password });
    setBusy(false);
    if (error) { setError(error.message); return; }
    setDone(true);
  };

  const shell = (children) => (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif",padding:18}}>
      <div style={{ ...card, width:360, padding:28 }}>
        <div style={{display:"flex",alignItems:"center",gap:9,marginBottom:20}}>
          <div style={{width:38,height:38,borderRadius:10,background:C.primary,display:"flex",alignItems:"center",justifyContent:"center"}}>
            <FlaskConical size={19} color={C.mint}/>
          </div>
          <div style={{fontSize:16,fontWeight:800,color:C.text}}>Yangi parol</div>
        </div>
        {children}
      </div>
    </div>
  );

  if (done) return shell(
    <>
      <div style={{display:"flex",alignItems:"center",gap:8,color:C.primary,fontSize:13.5,fontWeight:700,marginBottom:14}}>
        <CheckCircle2 size={17}/> Parol yangilandi
      </div>
      <p style={{fontSize:12.5,color:C.textMid,lineHeight:1.65,marginBottom:16}}>Endi yangi parolingiz bilan kirishingiz mumkin.</p>
      <a href="/" style={{ ...btnPrimary, width:"100%", justifyContent:"center", textDecoration:"none" }}>Saytga qaytish</a>
    </>
  );

  if (!ready) return shell(
    <p style={{fontSize:12.5,color:C.textMid,lineHeight:1.65}}>
      Havola tekshirilmoqda… Agar bu yozuv qolib ketsa, havolaning muddati tugagan bo'lishi mumkin —
      kirish sahifasidan "Parolni unutdingizmi?" ni qaytadan bosing.
    </p>
  );

  return shell(
    <form onSubmit={submit}>
      <label style={fieldLabel} htmlFor="new-password">Yangi parol</label>
      <input id="new-password" style={{ ...inputStyle, marginBottom:12 }} type="password" autoComplete="new-password"
        autoFocus required minLength={6} value={password} onChange={e => setPassword(e.target.value)}/>

      <label style={fieldLabel} htmlFor="confirm-password">Parolni takrorlang</label>
      <input id="confirm-password" style={{ ...inputStyle, marginBottom:16 }} type="password" autoComplete="new-password"
        required minLength={6} value={confirm} onChange={e => setConfirm(e.target.value)}/>

      {error && <div style={{color:C.danger,fontSize:12,marginBottom:12}}>{error}</div>}

      <button type="submit" disabled={busy} style={{ ...btnPrimary, width:"100%", justifyContent:"center" }}>
        {busy ? "Saqlanmoqda..." : "Parolni saqlash"}
      </button>
    </form>
  );
}
