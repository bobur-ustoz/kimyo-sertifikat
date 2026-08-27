import { useEffect, useState } from "react";
import { LogOut, FlaskConical, Wallet } from "lucide-react";
import { supabase } from "./lib/supabaseClient";
import Login from "./admin/Login";
import TeachersPanel from "./admin/TeachersPanel";
import VariantsPanel from "./admin/VariantsPanel";
import QuestionsPanel from "./admin/QuestionsPanel";
import PurchasesPanel from "./admin/PurchasesPanel";
import { C } from "./admin/ui";

const headerBtn = (active) => ({
  background: active ? C.mint : "rgba(255,255,255,0.14)",
  color: active ? C.primary : "#fff",
  border: "none", padding: "7px 12px", borderRadius: 8,
  fontSize: 12, fontWeight: 700, cursor: "pointer", fontFamily: "inherit",
  display: "flex", alignItems: "center", gap: 6,
});

export default function Admin() {
  const [session, setSession] = useState(undefined);
  const [profile, setProfile] = useState(undefined);   // undefined = still loading
  const [screen, setScreen] = useState("content");   // content | purchases
  const [teacher, setTeacher] = useState(null);      // drilled into a teacher
  const [variant, setVariant] = useState(null);      // ...and one of its variants

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => setSession(data.session));
    const { data: sub } = supabase.auth.onAuthStateChange((_e, s) => setSession(s));
    return () => sub.subscription.unsubscribe();
  }, []);

  // Signing in is not the same as being an admin: the database decides that,
  // and it used to only say so by refusing every write in silence.
  useEffect(() => {
    if (!session) { setProfile(null); return; }
    setProfile(undefined);
    supabase.from("profiles").select("is_admin, email").eq("id", session.user.id).maybeSingle()
      .then(({ data }) => setProfile(data || null));
  }, [session]);

  if (session === undefined) return null;
  if (!session) return <Login/>;
  if (profile === undefined) return null;

  if (!profile?.is_admin) return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif",padding:18}}>
      <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:28,maxWidth:400,textAlign:"center"}}>
        <div style={{fontSize:15,fontWeight:800,color:C.text,marginBottom:8}}>Bu hisobda admin huquqi yo'q</div>
        <p style={{fontSize:12.5,color:C.textMid,lineHeight:1.65,marginBottom:8}}>
          Siz <strong>{profile?.email || session.user.email}</strong> bilan kirdingiz. Bu hisob admin panelga yoza olmaydi.
        </p>
        <p style={{fontSize:12,color:C.textLight,lineHeight:1.6,marginBottom:16}}>
          Admin emailingiz bilan qayta kiring — bir-biriga o'xshash ikkita hisobingiz bo'lsa, raqamiga e'tibor bering.
        </p>
        <button onClick={() => supabase.auth.signOut()}
          style={{background:C.primary,color:"#fff",border:"none",padding:"10px 18px",borderRadius:9,fontSize:13,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"inline-flex",alignItems:"center",gap:7}}>
          <LogOut size={13}/> Chiqib, qayta kirish
        </button>
      </div>
    </div>
  );

  // The content side is a three-level drill-down; the deepest set state wins.
  const content =
    variant ? <QuestionsPanel teacher={teacher} variant={variant} onBack={() => setVariant(null)}/> :
    teacher ? <VariantsPanel teacher={teacher} onBack={() => { setTeacher(null); setVariant(null); }} onSelect={setVariant}/> :
              <TeachersPanel onSelect={setTeacher}/>;

  return (
    <div style={{minHeight:"100vh",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif"}}>
      <div style={{background:C.primary,padding:"14px 24px",display:"flex",alignItems:"center",justifyContent:"space-between"}}>
        <div style={{display:"flex",alignItems:"center",gap:10}}>
          <FlaskConical size={19} color={C.mint}/>
          <span style={{color:"#fff",fontWeight:800,fontSize:14.5}}>Kimyo Platform — Admin</span>
        </div>
        <div style={{display:"flex",alignItems:"center",gap:8}}>
          <button style={headerBtn(screen === "purchases")}
            onClick={() => setScreen(screen === "purchases" ? "content" : "purchases")}>
            <Wallet size={13}/> To'lovlar
          </button>
          <button style={headerBtn(false)} onClick={() => supabase.auth.signOut()}>
            <LogOut size={13}/> Chiqish
          </button>
        </div>
      </div>

      <div style={{maxWidth:920,margin:"0 auto",padding:"24px 20px"}}>
        {screen === "purchases"
          ? <PurchasesPanel onBack={() => setScreen("content")}/>
          : content}
      </div>
    </div>
  );
}
