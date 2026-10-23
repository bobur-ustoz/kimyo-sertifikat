import { useEffect, useState } from "react";
import { Video, Plus, Trash2, Radio } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { C, card, inputStyle, btnPrimary, btnGhost, pill, pageTitle } from "./ui";
import { LiveRoom, joinLesson, fmtWhen } from "../LiveLessons";

// Admin side of live lessons: schedule them, start one as host, end it.
export default function LivePanel() {
  const [rows,setRows]=useState([]);
  const [form,setForm]=useState({title:"",description:"",starts_at:"",duration_min:90,for_all:false});
  const [room,setRoom]=useState(null);
  const [busy,setBusy]=useState("");
  const [error,setError]=useState("");

  const load = () => supabase.from("live_lessons").select("*").order("starts_at",{ascending:false}).then(({data})=>setRows(data||[]));
  useEffect(()=>{ load(); },[]);

  const add = async () => {
    setError("");
    if(!form.title.trim()||!form.starts_at){ setError("Mavzu va vaqtni kiriting"); return; }
    const { error } = await supabase.from("live_lessons").insert({title:form.title.trim(),description:form.description.trim()||null,starts_at:new Date(form.starts_at).toISOString(),duration_min:Number(form.duration_min)||90,for_all:form.for_all});
    if(error){ setError(error.message); return; }
    setForm({title:"",description:"",starts_at:"",duration_min:90,for_all:false}); load();
  };
  const start = async l => {
    setBusy(l.id); setError("");
    try{ const r=await joinLesson(l.id); setRoom({url:r.url,title:l.title}); }catch(e){ setError(e.message); }
    setBusy(""); load();
  };
  const end = async l => { await supabase.from("live_lessons").update({status:"ended"}).eq("id",l.id); load(); };
  const del = async l => { if(!confirm(`"${l.title}" darsini o'chiraymi?`)) return; await supabase.from("live_lessons").delete().eq("id",l.id); load(); };

  if(room) return <LiveRoom url={room.url} title={room.title} onLeave={()=>{setRoom(null);load();}}/>;

  return (
    <div>
      <div style={pageTitle}>Jonli darslar</div>
      <div style={{fontSize:12.5,color:C.textMid,marginBottom:14}}>Dars rejalashtiring, vaqti kelganda "Boshlash" bosing. O'quvchilar faqat siz boshlagandan keyin qo'shila oladi.</div>
      <div style={{...card,marginBottom:16}}>
        <div style={{display:"grid",gridTemplateColumns:"2fr 1fr 110px",gap:10,marginBottom:10}}>
          <input style={inputStyle} placeholder="Dars mavzusi (masalan: Redoks reaksiyalar)" value={form.title} onChange={e=>setForm({...form,title:e.target.value})}/>
          <input style={inputStyle} type="datetime-local" value={form.starts_at} onChange={e=>setForm({...form,starts_at:e.target.value})}/>
          <input style={inputStyle} type="number" min={15} value={form.duration_min} onChange={e=>setForm({...form,duration_min:e.target.value})} title="Davomiyligi (daqiqa)"/>
        </div>
        <input style={{...inputStyle,marginBottom:10}} placeholder="Qisqacha izoh (ixtiyoriy)" value={form.description} onChange={e=>setForm({...form,description:e.target.value})}/>
        <div style={{display:"flex",alignItems:"center",gap:14}}>
          <label style={{fontSize:12.5,color:C.textMid,display:"flex",alignItems:"center",gap:6,cursor:"pointer"}}><input type="checkbox" checked={form.for_all} onChange={e=>setForm({...form,for_all:e.target.checked})}/> Hamma o'quvchi uchun (bepul rejadagilar ham)</label>
          <div style={{flex:1}}/>
          <button style={btnPrimary} onClick={add}><Plus size={14}/> Dars qo'shish</button>
        </div>
        {error&&<div style={{fontSize:12.5,color:C.danger,marginTop:10}}>{error}</div>}
      </div>
      {rows.map(l=>(
        <div key={l.id} style={{...card,marginBottom:10,display:"flex",alignItems:"center",gap:12,flexWrap:"wrap"}}>
          <Video size={18} color={C.primary}/>
          <div style={{flex:1,minWidth:200}}>
            <div style={{fontSize:14,fontWeight:800,color:C.text}}>{l.title}</div>
            <div style={{fontSize:12,color:C.textMid}}>{fmtWhen(l.starts_at)} · {l.duration_min} daqiqa{l.for_all?" · hamma uchun":" · Standart"}</div>
          </div>
          {l.status==="live"&&<span style={pill("#FEE2E2",C.danger,"#FECACA")}>● JONLI</span>}
          {l.status==="ended"&&<span style={pill("#F1F5F9",C.textMid,C.border)}>Tugagan</span>}
          {l.status!=="ended"&&<button style={btnPrimary} disabled={busy===l.id} onClick={()=>start(l)}><Radio size={13}/> {l.status==="live"?"Darsga qaytish":"Boshlash"}</button>}
          {l.status==="live"&&<button style={btnGhost} onClick={()=>end(l)}>Tugatish</button>}
          <button style={btnGhost} onClick={()=>del(l)}><Trash2 size={13}/></button>
        </div>
      ))}
    </div>
  );
}
