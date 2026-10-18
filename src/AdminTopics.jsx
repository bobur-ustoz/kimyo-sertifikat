import { useState, useEffect, useRef } from "react";
import { Upload } from "tus-js-client";
import { Plus, Trash2, Save, ChevronLeft, CheckCircle2, UploadCloud, FileText } from "lucide-react";
import { supabase } from "./lib/supabaseClient";
import { C, inputStyle, btnPrimary, btnGhost, card } from "./adminStyles";

async function uploadToBunny(file, title, onProgress) {
  const { data:{session} } = await supabase.auth.getSession();
  const authRes = await fetch("/api/bunny-auth",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${session.access_token}`},body:JSON.stringify({title})});
  const auth = await authRes.json();
  if(!authRes.ok) throw new Error(auth.error||"Yuklashda xatolik");
  await new Promise((resolve,reject)=>{
    new Upload(file,{
      endpoint:"https://video.bunnycdn.com/tusupload",
      retryDelays:[0,3000,5000,10000],
      headers:{
        AuthorizationSignature: auth.authorizationSignature,
        AuthorizationExpire: String(auth.authorizationExpire),
        VideoId: auth.videoId,
        LibraryId: String(auth.libraryId),
      },
      metadata:{ filetype:file.type, title },
      onError:reject,
      onProgress:(sent,total)=>onProgress(Math.round(sent/total*100)),
      onSuccess:resolve,
    }).start();
  });
  return auth.videoId;
}

function VideoField({videoId,title,onUploaded}){
  const [pct,setPct]=useState(null);
  const [err,setErr]=useState("");
  const ref=useRef(null);
  const pick = async file => {
    setErr(""); setPct(0);
    try{ onUploaded(await uploadToBunny(file,title,setPct)); }
    catch(e){ setErr(e.message); }
    setPct(null);
  };
  return (
    <div>
      <div style={{display:"flex",gap:8,alignItems:"center"}}>
        <div style={{...inputStyle,flex:1,color:videoId?C.primary:C.textLight,fontWeight:videoId?600:400,display:"flex",alignItems:"center",gap:8}}>
          {videoId?<><CheckCircle2 size={14}/> Video yuklangan (Bunny)</>:"Video hali yuklanmagan"}
        </div>
        <input ref={ref} type="file" accept="video/*" style={{display:"none"}} onChange={e=>{const f=e.target.files[0];if(f)pick(f);e.target.value="";}}/>
        {pct===null
          ? <button style={btnGhost} onClick={()=>ref.current?.click()}><UploadCloud size={13}/> {videoId?"Almashtirish":"Video yuklash"}</button>
          : <div style={{fontSize:11.5,color:C.textMid,fontWeight:700,minWidth:90}}>Yuklanmoqda… {pct}%</div>}
      </div>
      {err&&<p style={{fontSize:11,color:C.danger,marginTop:4}}>Xatolik: {err}</p>}
    </div>
  );
}

// target = {topic_id} or {example_id}
function TranscriptField({target}){
  const key = target.topic_id ? "topic_id" : "example_id";
  const id = target[key];
  const [text,setText]=useState("");
  const [loaded,setLoaded]=useState(false);
  const [dirty,setDirty]=useState(false);
  const [msg,setMsg]=useState("");
  const ref=useRef(null);
  useEffect(()=>{
    let off=false;
    setLoaded(false); setDirty(false); setMsg("");
    supabase.from("video_transcripts").select("content").eq(key,id).maybeSingle()
      .then(({data})=>{ if(!off){ setText(data?.content||""); setLoaded(true); } });
    return ()=>{off=true;};
  },[key,id]);
  const save = async () => {
    setMsg("");
    const content = text.trim();
    let error;
    if(!content){
      ({error} = await supabase.from("video_transcripts").delete().eq(key,id));
    } else {
      const { data:existing } = await supabase.from("video_transcripts").select("id").eq(key,id).maybeSingle();
      ({error} = existing
        ? await supabase.from("video_transcripts").update({content,updated_at:new Date().toISOString()}).eq("id",existing.id)
        : await supabase.from("video_transcripts").insert({[key]:id,content}));
    }
    if(error){ setMsg("Saqlanmadi: "+error.message); return; }
    setDirty(false); setMsg(content?"Saqlandi":"Matn o'chirildi");
  };
  const readFile = async file => { setText(await file.text()); setDirty(true); };
  return (
    <div>
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:6}}>
        <div style={{fontSize:10.5,fontWeight:700,color:C.textLight,textTransform:"uppercase",letterSpacing:"0.06em"}}>Video matni (AI shu matndan javob beradi, o'quvchiga ko'rinmaydi)</div>
        <input ref={ref} type="file" accept=".txt,text/plain" style={{display:"none"}} onChange={e=>{const f=e.target.files[0];if(f)readFile(f);e.target.value="";}}/>
        <button style={btnGhost} onClick={()=>ref.current?.click()}><FileText size={12}/> .txt yuklash</button>
      </div>
      <textarea style={{...inputStyle,minHeight:90,resize:"vertical"}} disabled={!loaded} placeholder={loaded?"Video matnini shu yerga yozing yoki .txt yuklang":"Yuklanmoqda…"} value={text} onChange={e=>{setText(e.target.value);setDirty(true);}}/>
      <div style={{display:"flex",alignItems:"center",gap:10,marginTop:6}}>
        {dirty&&<button style={btnPrimary} onClick={save}><Save size={13}/> Matnni saqlash</button>}
        {msg&&<span style={{fontSize:11.5,color:msg.startsWith("Saqlanmadi")?C.danger:C.primary}}>{msg}</span>}
        {!dirty&&text&&!msg&&<span style={{fontSize:11.5,color:C.textLight}}>{text.length} belgi</span>}
      </div>
    </div>
  );
}

function ExampleRow({ex,topicName,onChanged}){
  const [f,setF]=useState(ex);
  const [dirty,setDirty]=useState(false);
  const [open,setOpen]=useState(false);
  const set=(k,v)=>{setF(p=>({...p,[k]:v}));setDirty(true);};
  const saveVideo = async videoId => {
    await supabase.from("topic_examples").update({bunny_video_id:videoId}).eq("id",ex.id);
    setF(p=>({...p,bunny_video_id:videoId})); onChanged();
  };
  const saveAnalog = async () => {
    await supabase.from("topic_examples").update({analog_savol:f.analog_savol||null,analog_yechim:f.analog_yechim||null,analog_javob:f.analog_javob||null}).eq("id",ex.id);
    setDirty(false); onChanged();
  };
  return (
    <div style={{...card,marginBottom:8,padding:"12px 14px"}}>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:8}}>
        {f.bunny_video_id?<CheckCircle2 size={19} color={C.primary}/>:<div style={{width:19,height:19,borderRadius:"50%",border:`2px solid ${C.border}`}}/>}
        <div style={{fontWeight:800,fontSize:13,color:C.text,flex:1}}>{ex.example_number}-misol</div>
        <button style={btnGhost} onClick={()=>setOpen(o=>!o)}>{open?"Yopish":"Tahrirlash"}</button>
      </div>
      {open&&(
        <div style={{borderTop:`1px solid ${C.border}`,paddingTop:10,display:"flex",flexDirection:"column",gap:12}}>
          <VideoField videoId={f.bunny_video_id} title={`${topicName} — ${ex.example_number}-misol`} onUploaded={saveVideo}/>
          <TranscriptField target={{example_id:ex.id}}/>
          <div>
            <div style={{fontSize:10.5,fontWeight:700,color:C.textLight,textTransform:"uppercase",letterSpacing:"0.06em",marginBottom:6}}>Analog misol (matn)</div>
            <textarea style={{...inputStyle,minHeight:60,resize:"vertical",marginBottom:8}} placeholder="Analog savol" value={f.analog_savol||""} onChange={e=>set("analog_savol",e.target.value)}/>
            <textarea style={{...inputStyle,minHeight:70,resize:"vertical",marginBottom:8}} placeholder="Yechim (qadamma-qadam)" value={f.analog_yechim||""} onChange={e=>set("analog_yechim",e.target.value)}/>
            <input style={inputStyle} placeholder="Javob" value={f.analog_javob||""} onChange={e=>set("analog_javob",e.target.value)}/>
            {dirty&&<button style={{...btnPrimary,marginTop:8}} onClick={saveAnalog}><Save size={13}/> Analogni saqlash</button>}
          </div>
        </div>
      )}
    </div>
  );
}

function TopicEditor({topic,onBack,onChanged}){
  const [t,setT]=useState(topic);
  const [name,setName]=useState(topic.name);
  const [examples,setExamples]=useState([]);
  const load = async () => {
    const { data } = await supabase.from("topic_examples").select("*").eq("topic_id",topic.id).order("example_number");
    setExamples(data||[]);
  };
  useEffect(()=>{load();},[topic.id]);
  const saveName = async () => {
    if(!name.trim()) return;
    await supabase.from("topics").update({name:name.trim()}).eq("id",topic.id);
    setT(p=>({...p,name:name.trim()})); onChanged();
  };
  const saveVideo = async videoId => {
    await supabase.from("topics").update({bunny_video_id:videoId}).eq("id",topic.id);
    setT(p=>({...p,bunny_video_id:videoId})); onChanged();
  };
  const createExamples = async () => {
    const have = new Set(examples.map(e=>e.example_number));
    const rows = Array.from({length:20},(_,i)=>i+1).filter(n=>!have.has(n)).map(n=>({topic_id:topic.id,example_number:n}));
    if(rows.length) await supabase.from("topic_examples").insert(rows);
    load();
  };
  const ready = examples.filter(e=>e.bunny_video_id).length;
  return (
    <div>
      <button style={{...btnGhost,marginBottom:14}} onClick={onBack}><ChevronLeft size={14}/> Mavzular</button>
      <div style={{...card,marginBottom:14,background:C.mintBg,display:"flex",flexDirection:"column",gap:12}}>
        <div style={{display:"flex",gap:8}}>
          <input style={{...inputStyle,flex:1,fontWeight:700}} value={name} onChange={e=>setName(e.target.value)}/>
          {name.trim()!==t.name&&<button style={btnPrimary} onClick={saveName}><Save size={13}/> Nomini saqlash</button>}
        </div>
        <div>
          <div style={{fontSize:10.5,fontWeight:700,color:C.textLight,textTransform:"uppercase",letterSpacing:"0.06em",marginBottom:6}}>Mavzu videosi</div>
          <VideoField videoId={t.bunny_video_id} title={t.name} onUploaded={saveVideo}/>
        </div>
        <TranscriptField target={{topic_id:topic.id}}/>
      </div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:10}}>
        <h3 style={{fontSize:15,fontWeight:800,color:C.text}}>To'plam: misollar tahlili <span style={{fontWeight:600,color:C.textMid,fontSize:12.5}}>({ready}/{examples.length||20} video tayyor)</span></h3>
        {examples.length<20&&<button style={btnPrimary} onClick={createExamples}><Plus size={14}/> {examples.length?"Qolgan misollarni yaratish":"20 ta misol yaratish"}</button>}
      </div>
      {examples.map(ex=><ExampleRow key={ex.id} ex={ex} topicName={t.name} onChanged={load}/>)}
    </div>
  );
}

export default function TopicsAdmin(){
  const [topics,setTopics]=useState([]);
  const [newName,setNewName]=useState("");
  const [sel,setSel]=useState(null);
  const load = async () => {
    const { data } = await supabase.from("topics").select("*").order("sort_order").order("created_at");
    setTopics(data||[]);
  };
  useEffect(()=>{load();},[]);
  const add = async () => {
    const name=newName.trim();
    if(!name) return;
    await supabase.from("topics").insert({name,sort_order:topics.length+1});
    setNewName(""); load();
  };
  const del = async id => { if(confirm("Mavzuni o'chirishni tasdiqlaysizmi? Uning misollari va matnlari ham o'chadi.")){ await supabase.from("topics").delete().eq("id",id); load(); } };
  if(sel) return <TopicEditor topic={sel} onBack={()=>{setSel(null);load();}} onChanged={load}/>;
  return (
    <div>
      <h2 style={{fontSize:17,fontWeight:800,color:C.text,marginBottom:14}}>Mavzular</h2>
      <div style={{...card,marginBottom:14,display:"flex",gap:8,background:C.mintBg}}>
        <input style={{...inputStyle,flex:1}} placeholder="Yangi mavzu nomi (masalan: Proporsiya)" value={newName} onChange={e=>setNewName(e.target.value)} onKeyDown={e=>{if(e.key==="Enter")add();}}/>
        <button style={btnPrimary} onClick={add}><Plus size={14}/> Mavzu qo'shish</button>
      </div>
      <div style={{display:"flex",flexDirection:"column",gap:8}}>
        {topics.length===0&&<div style={{color:C.textLight,fontSize:13,padding:20,textAlign:"center"}}>Hali mavzu yo'q</div>}
        {topics.map(t=>(
          <div key={t.id} style={{...card,display:"flex",alignItems:"center",gap:12}}>
            <div style={{flex:1,fontWeight:700,fontSize:13.5,color:C.text}}>{t.name}</div>
            {t.bunny_video_id&&<span style={{fontSize:11,color:C.primary,fontWeight:700,display:"flex",alignItems:"center",gap:4}}><CheckCircle2 size={12}/> video</span>}
            <button style={btnGhost} onClick={()=>setSel(t)}>Ochish →</button>
            <button style={{...btnGhost,padding:8,color:C.danger}} onClick={()=>del(t.id)}><Trash2 size={13}/></button>
          </div>
        ))}
      </div>
    </div>
  );
}
