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
  const [screen, setScreen] = useState("content");   // content | purchases
  const [teacher, setTeacher] = useState(null);      // drilled into a teacher
  const [variant, setVariant] = useState(null);      // ...and one of its variants

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => setSession(data.session));
    const { data: sub } = supabase.auth.onAuthStateChange((_e, s) => setSession(s));
    return () => sub.subscription.unsubscribe();
  }, []);

  if (session === undefined) return null;
  if (!session) return <Login/>;

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
