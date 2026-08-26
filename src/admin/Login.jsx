import { useState } from "react";
import { FlaskConical } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { RESET_PATH } from "../ResetPassword";
import { resetErrorText, signInErrorText } from "../lib/authErrors";
import { C, card, inputStyle, btnPrimary, fieldLabel } from "./ui";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [info, setInfo] = useState("");
  const [busy, setBusy] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    setError("");
    setInfo("");
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) setError(signInErrorText(error));
    setBusy(false);
  };

  const sendReset = async () => {
    if (!email) { setError("Avval emailingizni kiriting."); return; }
    setBusy(true);
    setError("");
    setInfo("");
    const { error } = await supabase.auth.resetPasswordForEmail(email, {
      redirectTo: window.location.origin + RESET_PATH,
    });
    setBusy(false);
    // Don't reveal whether the address exists -- same answer either way.
    if (error) setError(resetErrorText(error));
    else setInfo("Agar bu email ro'yxatdan o'tgan bo'lsa, tiklash havolasi yuborildi. Pochtangizni tekshiring.");
  };

  return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif",padding:18}}>
      <form onSubmit={submit} style={{ ...card, width:340, padding:28 }}>
        <div style={{display:"flex",alignItems:"center",gap:9,marginBottom:20}}>
          <div style={{width:38,height:38,borderRadius:10,background:C.primary,display:"flex",alignItems:"center",justifyContent:"center"}}>
            <FlaskConical size={19} color={C.mint}/>
          </div>
          <div style={{fontSize:16,fontWeight:800,color:C.text}}>Admin panel</div>
        </div>

        <label style={fieldLabel} htmlFor="admin-email">Email</label>
        <input id="admin-email" style={{ ...inputStyle, marginBottom:12 }} type="email" autoComplete="username"
          autoFocus required value={email} onChange={e => setEmail(e.target.value)}/>

        <label style={fieldLabel} htmlFor="admin-password">Parol</label>
        <input id="admin-password" style={{ ...inputStyle, marginBottom:16 }} type="password" autoComplete="current-password"
          required value={password} onChange={e => setPassword(e.target.value)}/>

        {error && <div style={{color:C.danger,fontSize:12,marginBottom:12}}>{error}</div>}
        {info && <div style={{color:C.primary,fontSize:12,marginBottom:12,lineHeight:1.55}}>{info}</div>}

        <button type="submit" disabled={busy} style={{ ...btnPrimary, width:"100%", justifyContent:"center" }}>
          {busy ? "Kirilmoqda..." : "Kirish"}
        </button>

        <button type="button" onClick={sendReset} disabled={busy}
          style={{width:"100%",marginTop:12,background:"none",border:"none",color:C.textMid,fontSize:12,fontWeight:600,cursor:"pointer",fontFamily:"inherit",textDecoration:"underline"}}>
          Parolni unutdingizmi?
        </button>
      </form>
    </div>
  );
}
