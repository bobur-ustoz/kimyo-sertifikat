import { useState, useEffect } from "react";
import { Check, Pencil, Trash2, Flag, Save } from "lucide-react";
import { supabase } from "./lib/supabaseClient";
import { C, inputStyle, btnPrimary, btnGhost, card } from "./adminStyles";
import { Rich } from "./TopicLessons";

const FILTERS = [
  ["flagged", "Belgilangan"],
  ["auto", "Ko'rilmagan"],
  ["approved", "Tasdiqlangan"],
  ["all", "Hammasi"],
];

function Row({row,onChanged}){
  const [edit,setEdit]=useState(false);
  const [text,setText]=useState(row.answer);
  const [busy,setBusy]=useState(false);
  const [time,setTime]=useState(row.video_seconds!=null?`${Math.floor(row.video_seconds/60)}:${String(row.video_seconds%60).padStart(2,"0")}`:"");
  // "18:37" or "1237" seconds -> seconds; empty = not tied to a moment in the video.
  const secs = () => { const t=time.trim(); if(!t) return null; const m=t.match(/^(\d+):([0-5]?\d)$/); if(m) return +m[1]*60+ +m[2]; return /^\d+$/.test(t)?+t:undefined; };
  const timeBad = secs()===undefined;
  const where = row.topic_examples
    ? `${row.topic_examples.topics?.name||"Mavzu"} · ${row.topic_examples.example_number}-misol`
    : (row.topics?.name||"Mavzu");
  const chip = row.status==="flagged"
    ? {bg:"#FEF2F2",fg:C.danger,t:"Noto'g'ri deb belgilangan"}
    : row.status==="approved"
    ? {bg:C.mintBg,fg:C.primary,t:"Tasdiqlangan"}
    : {bg:C.warningBg,fg:C.warning,t:"Ko'rilmagan"};

  const update = async patch => {
    setBusy(true);
    const { error } = await supabase.from("video_questions").update(patch).eq("id",row.id);
    setBusy(false);
    if(error){ alert("Saqlanmadi: "+error.message); return; }
    onChanged();
  };
  const approve = () => update({status:"approved",reviewed_at:new Date().toISOString(),...(secs()!=null?{video_seconds:secs()}:{})});
  const saveEdit = async () => { await update({answer:text.trim(),status:"approved",reviewed_at:new Date().toISOString(),...(secs()!=null?{video_seconds:secs()}:{})}); setEdit(false); };
  const del = async () => {
    if(!confirm("Bu savol-javobni o'chirishni tasdiqlaysizmi? Boshqa o'quvchilarga ko'rsatilmaydi.")) return;
    setBusy(true);
    const { error } = await supabase.from("video_questions").delete().eq("id",row.id);
    setBusy(false);
    if(error){ alert("O'chirilmadi: "+error.message); return; }
    onChanged();
  };

  return (
    <div style={{...card,marginBottom:10,padding:"14px 16px"}}>
      <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:8,flexWrap:"wrap"}}>
        <span style={{fontSize:11,fontWeight:800,color:C.textMid}}>{where}</span>
        <span style={{fontSize:10.5,fontWeight:800,padding:"2px 9px",borderRadius:20,background:chip.bg,color:chip.fg}}>{chip.t}</span>
        <span style={{fontSize:11,color:C.textLight}}>{row.hits||0} marta qayta ishlatilgan · {new Date(row.created_at).toLocaleString("uz-UZ")}</span>
      </div>
      <div style={{background:C.mintBg,borderRadius:9,padding:"8px 12px",fontSize:13,fontWeight:700,color:C.text,marginBottom:8}}>{row.question}</div>
      {edit
        ? <textarea style={{...inputStyle,minHeight:110,resize:"vertical"}} value={text} onChange={e=>setText(e.target.value)}/>
        : <div style={{fontSize:13,color:C.text,lineHeight:1.65,whiteSpace:"pre-wrap"}}><Rich text={row.answer}/></div>}
      <div style={{display:"flex",alignItems:"center",gap:8,marginTop:10,fontSize:12,color:C.textMid}}>
        Videoda qaysi daqiqada (m:ss)?
        <input style={{...inputStyle,width:90,padding:"6px 10px"}} placeholder="18:37" value={time} onChange={e=>setTime(e.target.value)}
          onBlur={()=>{ if(!timeBad && row.status==="approved") update({video_seconds:secs()??null}); }}/>
        {timeBad&&<span style={{color:C.danger}}>Masalan: 18:37</span>}
      </div>
      <div style={{display:"flex",gap:8,marginTop:12,flexWrap:"wrap"}}>
        {edit ? (<>
          <button style={btnPrimary} disabled={busy||!text.trim()||timeBad} onClick={saveEdit}><Save size={13}/> Saqlash va tasdiqlash</button>
          <button style={btnGhost} onClick={()=>{setEdit(false);setText(row.answer);}}>Bekor qilish</button>
        </>) : (<>
          {row.status!=="approved" && <button style={btnPrimary} disabled={busy||timeBad} onClick={approve}><Check size={13}/> Tasdiqlash</button>}
          <button style={btnGhost} onClick={()=>setEdit(true)}><Pencil size={12}/> Tahrirlash</button>
          <button style={{...btnGhost,color:C.danger}} disabled={busy} onClick={del}><Trash2 size={12}/> O'chirish</button>
        </>)}
      </div>
    </div>
  );
}

export default function QuestionsReview(){
  const [rows,setRows]=useState(null);
  const [filter,setFilter]=useState("flagged");
  const [err,setErr]=useState("");

  const load = async () => {
    const { data, error } = await supabase.from("video_questions")
      .select("*, topics(name), topic_examples(example_number, topics(name))")
      .order("created_at",{ascending:false}).limit(300);
    if(error){ setErr(error.message); setRows([]); return; }
    setErr(""); setRows(data||[]);
  };
  useEffect(()=>{load();},[]);

  const shown = (rows||[]).filter(r => filter==="all" || r.status===filter);
  const count = f => (rows||[]).filter(r => f==="all" || r.status===f).length;

  return (
    <div>
      <h2 style={{fontSize:17,fontWeight:800,color:C.text,marginBottom:4}}>Savollar va AI javoblari</h2>
      <p style={{fontSize:12.5,color:C.textMid,marginBottom:14,lineHeight:1.6}}>
        O'quvchilar bergan savollar va AI'ning javoblari. <strong>Tasdiqlang</strong>, <strong>tahrirlang</strong> (shundan keyin hamma o'quvchi sizning javobingizni oladi) yoki noto'g'risini <strong>o'chiring</strong>.
        Qizil belgi: o'quvchi javobni noto'g'ri deb xabar bergan, u boshqalarga ko'rsatilmaydi.
      </p>
      <div style={{display:"flex",gap:8,marginBottom:14,flexWrap:"wrap"}}>
        {FILTERS.map(([id,label])=>(
          <button key={id} onClick={()=>setFilter(id)}
            style={{padding:"7px 13px",borderRadius:20,border:`1px solid ${filter===id?C.primary:C.border}`,background:filter===id?C.primary:"#fff",color:filter===id?"#fff":C.textMid,fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:6}}>
            {id==="flagged"&&<Flag size={11}/>} {label} ({rows?count(id):"…"})
          </button>
        ))}
        <button style={{...btnGhost,marginLeft:"auto"}} onClick={load}>Yangilash</button>
      </div>
      {err && <p style={{color:C.danger,fontSize:12.5,marginBottom:10}}>Xatolik: {err}</p>}
      {rows===null && <div style={{color:C.textLight,fontSize:13}}>Yuklanmoqda…</div>}
      {rows!==null && shown.length===0 && <div style={{...card,textAlign:"center",color:C.textMid,fontSize:13,padding:28}}>Bu bo'limda savol yo'q.</div>}
      {shown.map(r=><Row key={r.id} row={r} onChanged={load}/>)}
    </div>
  );
}
