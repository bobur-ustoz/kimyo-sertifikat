import { useState } from "react";
import { FlaskConical } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { C, card, inputStyle, btnPrimary, fieldLabel } from "./ui";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    setError("");
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) setError("Email yoki parol noto'g'ri");
    setBusy(false);
  };

  return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif"}}>
      <form onSubmit={submit} style={{...card, width:340, padding:28}}>
        <div style={{display:"flex",alignItems:"center",gap:9,marginBottom:20}}>
          <div style={{width:38,height:38,borderRadius:10,background:C.primary,display:"flex",alignItems:"center",justifyContent:"center"}}>
            <FlaskConical size={19} color={C.mint}/>
          </div>
          <div style={{fontSize:16,fontWeight:800,color:C.text}}>Admin panel</div>
        </div>

        <label style={fieldLabel} htmlFor="admin-email">Email</label>
        <input id="admin-email" style={{...inputStyle, marginBottom:12}} type="email" autoComplete="username"
          autoFocus value={email} onChange={e=>setEmail(e.target.value)} required/>

        <label style={fieldLabel} htmlFor="admin-password">Parol</label>
        <input id="admin-password" style={{...inputStyle, marginBottom:16}} type="password" autoComplete="current-password"
          value={password} onChange={e=>setPassword(e.target.value)} required/>

        {error && <div style={{color:C.danger,fontSize:12,marginBottom:12}}>{error}</div>}

        <button type="submit" disabled={busy} style={{...btnPrimary, width:"100%", justifyContent:"center"}}>
          {busy ? "Kirilmoqda..." : "Kirish"}
        </button>
      </form>
    </div>
  );
}
