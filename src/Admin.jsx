import { useState, useEffect } from "react";
import { supabase } from "./lib/supabaseClient";
import { LogOut, Plus, Trash2, Save, ChevronLeft, CheckCircle2, Circle, FlaskConical } from "lucide-react";

const C = { primary:"#0F5132", accent:"#0D9488", mint:"#6EE7B7", mintBg:"#F0FDF4", bgSoft:"#F8FAFC", text:"#0F172A", textMid:"#475569", textLight:"#94A3B8", border:"#E2E8F0", danger:"#DC2626" };

const inputStyle = {width:"100%",padding:"9px 11px",borderRadius:8,border:`1px solid ${C.border}`,fontSize:13,fontFamily:"inherit",color:C.text};
const btnPrimary = {padding:"9px 14px",borderRadius:8,background:C.primary,color:"#fff",border:"none",fontSize:12.5,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:6};
const btnGhost = {padding:"8px 12px",borderRadius:8,background:"#fff",color:C.textMid,border:`1px solid ${C.border}`,fontSize:12,fontWeight:600,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:5};
const card = {background:"#fff",border:`1px solid ${C.border}`,borderRadius:12,padding:16};

function LoginScreen(){
  const [email,setEmail]=useState("");
  const [password,setPassword]=useState("");
  const [error,setError]=useState("");
  const [loading,setLoading]=useState(false);
  const submit = async e => {
    e.preventDefault();
    setLoading(true); setError("");
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) setError("Email yoki parol noto'g'ri");
    setLoading(false);
  };
  return (
    <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif"}}>
      <form onSubmit={submit} style={{...card,width:340,padding:28}}>
        <div style={{display:"flex",alignItems:"center",gap:9,marginBottom:20}}>
          <div style={{width:38,height:38,borderRadius:10,background:C.primary,display:"flex",alignItems:"center",justifyContent:"center"}}><FlaskConical size={19} color={C.mint}/></div>
          <div style={{fontSize:16,fontWeight:800,color:C.text}}>Admin panel</div>
        </div>
        <label style={{fontSize:11.5,fontWeight:700,color:C.textMid,marginBottom:5,display:"block"}}>Email</label>
        <input style={{...inputStyle,marginBottom:12}} type="email" value={email} onChange={e=>setEmail(e.target.value)} required/>
        <label style={{fontSize:11.5,fontWeight:700,color:C.textMid,marginBottom:5,display:"block"}}>Parol</label>
        <input style={{...inputStyle,marginBottom:16}} type="password" value={password} onChange={e=>setPassword(e.target.value)} required/>
        {error && <div style={{color:C.danger,fontSize:12,marginBottom:12}}>{error}</div>}
        <button type="submit" disabled={loading} style={{...btnPrimary,width:"100%",justifyContent:"center"}}>{loading?"Kirilmoqda...":"Kirish"}</button>
      </form>
    </div>
  );
}

function TeacherForm({onSaved,editing,onCancel}){
  const [f,setF]=useState(editing || {name:"",subject:"",initials:"",color:"#0F5132",bg_color:"#F0FDF4",rating:5,students:0,badge:"",is_free:true,description:""});
  const set=(k,v)=>setF(p=>({...p,[k]:v}));
  const save = async () => {
    if(!f.name||!f.subject||!f.initials) return;
    if(editing){
      await supabase.from("teachers").update(f).eq("id",editing.id);
    } else {
      await supabase.from("teachers").insert(f);
    }
    onSaved();
  };
  return (
    <div style={{...card,marginBottom:14,background:C.mintBg}}>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
        <div><label style={{fontSize:11,color:C.textMid}}>Ism-familiya</label><input style={inputStyle} value={f.name} onChange={e=>set("name",e.target.value)}/></div>
        <div><label style={{fontSize:11,color:C.textMid}}>Fan</label><input style={inputStyle} value={f.subject} onChange={e=>set("subject",e.target.value)}/></div>
        <div><label style={{fontSize:11,color:C.textMid}}>Inisiallar (2 harf)</label><input style={inputStyle} maxLength={2} value={f.initials} onChange={e=>set("initials",e.target.value.toUpperCase())}/></div>
        <div><label style={{fontSize:11,color:C.textMid}}>Rang (hex)</label><input style={inputStyle} value={f.color} onChange={e=>set("color",e.target.value)}/></div>
        <div><label style={{fontSize:11,color:C.textMid}}>Badge (ixtiyoriy)</label><input style={inputStyle} value={f.badge||""} onChange={e=>set("badge",e.target.value)}/></div>
        <div style={{display:"flex",alignItems:"center",gap:8,marginTop:18}}>
          <input type="checkbox" checked={f.is_free} onChange={e=>set("is_free",e.target.checked)} id="isfree"/>
          <label htmlFor="isfree" style={{fontSize:12,color:C.text}}>Bepul kolleksiya</label>
        </div>
      </div>
      <label style={{fontSize:11,color:C.textMid}}>Tavsif</label>
      <textarea style={{...inputStyle,marginBottom:10,minHeight:60}} value={f.description} onChange={e=>set("description",e.target.value)}/>
      <div style={{display:"flex",gap:8}}>
        <button style={btnPrimary} onClick={save}><Save size={13}/> Saqlash</button>
        <button style={btnGhost} onClick={onCancel}>Bekor qilish</button>
      </div>
    </div>
  );
}

function TeachersPanel({onSelect}){
  const [teachers,setTeachers]=useState([]);
  const [showForm,setShowForm]=useState(false);
  const [editing,setEditing]=useState(null);
  const load = async () => {
    const { data } = await supabase.from("teachers").select("*").order("sort_order").order("created_at");
    setTeachers(data||[]);
  };
  useEffect(()=>{load();},[]);
  const del = async id => { if(confirm("O'qituvchini o'chirishni tasdiqlaysizmi? Barcha variant va savollari ham o'chadi.")){ await supabase.from("teachers").delete().eq("id",id); load(); } };
  return (
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14}}>
        <h2 style={{fontSize:17,fontWeight:800,color:C.text}}>O'qituvchilar</h2>
        <button style={btnPrimary} onClick={()=>{setEditing(null);setShowForm(true);}}><Plus size={14}/> Yangi o'qituvchi</button>
      </div>
      {showForm && <TeacherForm editing={editing} onCancel={()=>setShowForm(false)} onSaved={()=>{setShowForm(false);load();}}/>}
      <div style={{display:"flex",flexDirection:"column",gap:8}}>
        {teachers.length===0 && <div style={{color:C.textLight,fontSize:13,padding:20,textAlign:"center"}}>Hali o'qituvchi qo'shilmagan</div>}
        {teachers.map(t=>(
          <div key={t.id} style={{...card,display:"flex",alignItems:"center",gap:12}}>
            <div style={{width:38,height:38,borderRadius:10,background:t.color,display:"flex",alignItems:"center",justifyContent:"center",color:"#fff",fontWeight:800,fontSize:13,flexShrink:0}}>{t.initials}</div>
            <div style={{flex:1,minWidth:0}}>
              <div style={{fontWeight:700,fontSize:13.5,color:C.text}}>{t.name}</div>
              <div style={{fontSize:11.5,color:C.textMid}}>{t.subject} {t.is_free?"· Bepul":"· Premium"}</div>
            </div>
            <button style={btnGhost} onClick={()=>onSelect(t)}>Variantlar →</button>
            <button style={{...btnGhost,padding:8}} onClick={()=>{setEditing(t);setShowForm(true);}}>✏️</button>
            <button style={{...btnGhost,padding:8,color:C.danger}} onClick={()=>del(t.id)}><Trash2 size={13}/></button>
          </div>
        ))}
      </div>
    </div>
  );
}

function VariantsPanel({teacher,onBack,onSelect}){
  const [variants,setVariants]=useState([]);
  const [newNum,setNewNum]=useState("");
  const load = async () => {
    const { data } = await supabase.from("variants").select("*").eq("teacher_id",teacher.id).order("variant_number");
    setVariants(data||[]);
  };
  useEffect(()=>{load();},[teacher.id]);
  const addVariant = async () => {
    const num = parseInt(newNum,10);
    if(!num) return;
    await supabase.from("variants").insert({teacher_id:teacher.id,variant_number:num,total_questions:43});
    setNewNum(""); load();
  };
  const delVariant = async id => { if(confirm("Variantni o'chirishni tasdiqlaysizmi? Barcha savollari ham o'chadi.")){ await supabase.from("variants").delete().eq("id",id); load(); } };
  return (
    <div>
      <button style={{...btnGhost,marginBottom:14}} onClick={onBack}><ChevronLeft size={14}/> O'qituvchilar</button>
      <h2 style={{fontSize:17,fontWeight:800,color:C.text,marginBottom:4}}>{teacher.name} — Variantlar</h2>
      <p style={{fontSize:12.5,color:C.textMid,marginBottom:14}}>{teacher.subject}</p>
      <div style={{...card,marginBottom:14,display:"flex",gap:8,alignItems:"center",background:C.mintBg}}>
        <input style={{...inputStyle,width:120}} type="number" placeholder="Variant raqami" value={newNum} onChange={e=>setNewNum(e.target.value)}/>
        <button style={btnPrimary} onClick={addVariant}><Plus size={14}/> Variant qo'shish</button>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(160px,1fr))",gap:10}}>
        {variants.length===0 && <div style={{color:C.textLight,fontSize:13,padding:12}}>Hali variant qo'shilmagan</div>}
        {variants.map(v=>(
          <div key={v.id} style={{...card,padding:14}}>
            <div style={{fontWeight:800,fontSize:14,color:C.text,marginBottom:8}}>{v.variant_number}-Variant</div>
            <div style={{display:"flex",gap:6}}>
              <button style={{...btnGhost,flex:1,justifyContent:"center"}} onClick={()=>onSelect(v)}>Savollar</button>
              <button style={{...btnGhost,padding:8,color:C.danger}} onClick={()=>delVariant(v.id)}><Trash2 size={13}/></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function QuestionRow({q,onChanged}){
  const [f,setF]=useState(q);
  const [dirty,setDirty]=useState(false);
  const set=(k,v)=>{setF(p=>({...p,[k]:v}));setDirty(true);};
  const save = async () => {
    await supabase.from("questions").update({topic:f.topic,formula:f.formula,question_text:f.question_text,video_url:f.video_url,video_ready:f.video_ready}).eq("id",q.id);
    setDirty(false); onChanged();
  };
  return (
    <div style={{...card,marginBottom:8,padding:"12px 14px"}}>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:8}}>
        <button onClick={()=>set("video_ready",!f.video_ready)} style={{background:"none",border:"none",cursor:"pointer",padding:0,flexShrink:0}}>
          {f.video_ready?<CheckCircle2 size={19} color={C.primary}/>:<Circle size={19} color={C.textLight}/>}
        </button>
        <div style={{fontWeight:800,fontSize:13,color:C.text,width:70,flexShrink:0}}>{q.question_number}-savol</div>
        <input style={{...inputStyle,flex:1}} placeholder="Mavzu" value={f.topic||""} onChange={e=>set("topic",e.target.value)}/>
        <input style={{...inputStyle,flex:1}} placeholder="Formula (ixtiyoriy)" value={f.formula||""} onChange={e=>set("formula",e.target.value)}/>
      </div>
      <div style={{display:"flex",gap:8}}>
        <input style={{...inputStyle,flex:1}} placeholder="Video havolasi (URL)" value={f.video_url||""} onChange={e=>set("video_url",e.target.value)}/>
        {dirty && <button style={btnPrimary} onClick={save}><Save size={13}/> Saqlash</button>}
      </div>
    </div>
  );
}

function QuestionsPanel({variant,teacher,onBack}){
  const [questions,setQuestions]=useState([]);
  const load = async () => {
    const { data } = await supabase.from("questions").select("*").eq("variant_id",variant.id).order("question_number");
    setQuestions(data||[]);
  };
  useEffect(()=>{load();},[variant.id]);
  const generateAll = async () => {
    const rows = Array.from({length:variant.total_questions},(_,i)=>({variant_id:variant.id,question_number:i+1}));
    await supabase.from("questions").insert(rows);
    load();
  };
  const doneCount = questions.filter(q=>q.video_ready).length;
  return (
    <div>
      <button style={{...btnGhost,marginBottom:14}} onClick={onBack}><ChevronLeft size={14}/> Variantlar</button>
      <h2 style={{fontSize:17,fontWeight:800,color:C.text,marginBottom:4}}>{teacher.name} · {variant.variant_number}-Variant — Savollar</h2>
      <p style={{fontSize:12.5,color:C.textMid,marginBottom:14}}>{doneCount}/{questions.length} video tayyor</p>
      {questions.length===0 ? (
        <div style={{...card,textAlign:"center",padding:24}}>
          <p style={{fontSize:13,color:C.textMid,marginBottom:12}}>Bu variant uchun hali savollar yaratilmagan.</p>
          <button style={btnPrimary} onClick={generateAll}><Plus size={14}/> {variant.total_questions} ta savol yaratish</button>
        </div>
      ) : (
        <div>{questions.map(q=><QuestionRow key={q.id} q={q} onChanged={load}/>)}</div>
      )}
    </div>
  );
}

export default function Admin(){
  const [session,setSession]=useState(undefined);
  const [teacher,setTeacher]=useState(null);
  const [variant,setVariant]=useState(null);

  useEffect(()=>{
    supabase.auth.getSession().then(({data})=>setSession(data.session));
    const { data:sub } = supabase.auth.onAuthStateChange((_e,s)=>setSession(s));
    return ()=>sub.subscription.unsubscribe();
  },[]);

  if (session===undefined) return null;
  if (!session) return <LoginScreen/>;

  return (
    <div style={{minHeight:"100vh",background:C.bgSoft,fontFamily:"'Inter',system-ui,sans-serif"}}>
      <div style={{background:C.primary,padding:"14px 24px",display:"flex",alignItems:"center",justifyContent:"space-between"}}>
        <div style={{display:"flex",alignItems:"center",gap:10}}>
          <FlaskConical size={19} color={C.mint}/>
          <span style={{color:"#fff",fontWeight:800,fontSize:14.5}}>Kimyo Platform — Admin</span>
        </div>
        <button onClick={()=>supabase.auth.signOut()} style={{background:"rgba(255,255,255,0.14)",border:"none",color:"#fff",padding:"7px 12px",borderRadius:8,fontSize:12,fontWeight:600,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:6}}><LogOut size={13}/> Chiqish</button>
      </div>
      <div style={{maxWidth:920,margin:"0 auto",padding:"24px 20px"}}>
        {!teacher && <TeachersPanel onSelect={t=>setTeacher(t)}/>}
        {teacher && !variant && <VariantsPanel teacher={teacher} onBack={()=>setTeacher(null)} onSelect={v=>setVariant(v)}/>}
        {teacher && variant && <QuestionsPanel teacher={teacher} variant={variant} onBack={()=>setVariant(null)}/>}
      </div>
    </div>
  );
}
