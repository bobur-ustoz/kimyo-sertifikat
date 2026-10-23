import { useEffect, useRef, useState } from "react";
import { Video, Calendar, Clock, Lock, X, Radio } from "lucide-react";
import { supabase } from "./lib/supabaseClient";

const C = { primary:"#0F5132", accent:"#0D9488", mint:"#6EE7B7", mintBg:"#F0FDF4", mintLight:"#D1FAE5", borderGreen:"#86EFAC", text:"#0F172A", textMid:"#475569", textLight:"#94A3B8", border:"#E2E8F0", danger:"#DC2626" };

export const fmtWhen = iso => new Date(iso).toLocaleString("uz-UZ",{day:"numeric",month:"long",hour:"2-digit",minute:"2-digit"});

// Asks the server for a room link (it decides who may enter) and returns it.
export async function joinLesson(lessonId) {
  const { data } = await supabase.auth.getSession();
  const jwt = data.session?.access_token;
  const res = await fetch("/api/live-token",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${jwt}`},body:JSON.stringify({lessonId})});
  const body = await res.json().catch(()=>({}));
  if(!res.ok) throw new Error(body.error||"Darsga ulanib bo'lmadi");
  return body;
}

// Full-screen video room, shared by students and the host. Built on Daily's call frame so the
// teacher's shared screen stays the main view for students: no participant strip, no layout switch.
export function LiveRoom({url,token,host,title,onLeave}) {
  const box=useRef(null);
  const [err,setErr]=useState("");
  useEffect(()=>{
    let frame; let dead=false;
    (async()=>{
      try{
        const { default: Daily } = await import("@daily-co/daily-js");
        if(dead||!box.current) return;
        frame = Daily.createFrame(box.current,{
          iframeStyle:{width:"100%",height:"100%",border:"0"},
          showLeaveButton:false, showFullscreenButton:true,
          showParticipantsBar:!!host, showLayoutButton:!!host,
          theme:{colors:{accent:"#0F5132",accentText:"#FFFFFF",background:"#0B1F17",mainAreaBg:"#0B1F17",baseText:"#FFFFFF"}},
        });
        frame.on("left-meeting",()=>onLeave());
        await frame.join({url,token,startVideoOff:!host,startAudioOff:!host});
      }catch(e){ setErr(e?.message||"Darsga ulanib bo'lmadi"); }
    })();
    return ()=>{ dead=true; try{ frame?.destroy(); }catch{} };
  },[url,token]);
  return (
    <div style={{position:"fixed",inset:0,zIndex:1000,background:"#0B1F17",display:"flex",flexDirection:"column"}}>
      <div style={{display:"flex",alignItems:"center",gap:10,padding:"10px 16px",background:C.primary}}>
        <Radio size={16} color={C.mint}/>
        <div style={{flex:1,color:"#fff",fontWeight:800,fontSize:14}}>{title}</div>
        <button onClick={onLeave} style={{display:"flex",alignItems:"center",gap:6,padding:"7px 14px",borderRadius:8,border:"none",background:"#fff",color:C.primary,fontWeight:800,fontSize:12.5,cursor:"pointer",fontFamily:"inherit"}}><X size={14}/> Chiqish</button>
      </div>
      {err&&<div style={{padding:14,color:"#FCA5A5",fontSize:13}}>{err}</div>}
      <div ref={box} style={{flex:1,minHeight:0}}/>
    </div>
  );
}

export default function LiveLessons({session,plan,setTab}) {
  const [lessons,setLessons]=useState([]);
  const [loading,setLoading]=useState(true);
  const [room,setRoom]=useState(null);
  const [busy,setBusy]=useState("");
  const [error,setError]=useState("");
  const [,tick]=useState(0);

  const load = () => supabase.from("live_lessons").select("*").neq("status","ended").order("starts_at").then(({data})=>{ setLessons(data||[]); setLoading(false); });
  useEffect(()=>{ load(); const t=setInterval(()=>{ load(); tick(n=>n+1); },20000); return ()=>clearInterval(t); },[]);

  const join = async l => {
    setBusy(l.id); setError("");
    try{ const r=await joinLesson(l.id); setRoom({url:r.url,token:r.token,host:r.host,title:l.title}); }
    catch(e){ setError(e.message); }
    setBusy("");
  };

  if(room) return <LiveRoom url={room.url} token={room.token} host={room.host} title={room.title} onLeave={()=>{setRoom(null);load();}}/>;

  const live=lessons.filter(l=>l.status==="live");
  const soon=lessons.filter(l=>l.status==="scheduled");
  const card={background:"#fff",border:`1px solid ${C.border}`,borderRadius:16,padding:"16px 18px",boxShadow:"0 2px 12px rgba(15,81,50,0.06)"};
  const locked=l=>!l.for_all&&plan==="free";

  const Row = ({l}) => {
    const isLive=l.status==="live";
    return (
      <div style={{...card,display:"flex",alignItems:"center",gap:14,flexWrap:"wrap",border:`1.5px solid ${isLive?C.danger:C.border}`}}>
        <div style={{width:46,height:46,borderRadius:13,background:isLive?"#FEE2E2":C.mintBg,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>{isLive?<Radio size={21} color={C.danger}/>:<Video size={21} color={C.primary}/>}</div>
        <div style={{flex:1,minWidth:200}}>
          <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:3}}>
            <span style={{fontSize:15,fontWeight:800,color:C.text}}>{l.title}</span>
            {isLive&&<span style={{fontSize:10,fontWeight:900,color:"#fff",background:C.danger,borderRadius:20,padding:"2px 9px"}}>● JONLI</span>}
          </div>
          {l.description&&<div style={{fontSize:12.5,color:C.textMid,marginBottom:5}}>{l.description}</div>}
          <div style={{display:"flex",gap:14,fontSize:11.5,color:C.textMid}}>
            <span style={{display:"flex",alignItems:"center",gap:4}}><Calendar size={12}/> {fmtWhen(l.starts_at)}</span>
            <span style={{display:"flex",alignItems:"center",gap:4}}><Clock size={12}/> {l.duration_min} daqiqa</span>
          </div>
        </div>
        {locked(l)
          ? <button onClick={()=>setTab("obuna")} style={{display:"flex",alignItems:"center",gap:6,padding:"10px 16px",borderRadius:10,border:`1.5px solid ${C.borderGreen}`,background:"#fff",color:C.primary,fontWeight:800,fontSize:12.5,cursor:"pointer",fontFamily:"inherit"}}><Lock size={13}/> Standart kerak</button>
          : <button onClick={()=>join(l)} disabled={!isLive||busy===l.id} style={{padding:"10px 20px",borderRadius:10,border:"none",background:isLive?C.primary:"#E2E8F0",color:isLive?"#fff":C.textLight,fontWeight:800,fontSize:13,cursor:isLive?"pointer":"not-allowed",fontFamily:"inherit"}}>{busy===l.id?"Ulanmoqda...":isLive?"Qo'shilish":"Hali boshlanmagan"}</button>}
      </div>
    );
  };

  return (
    <div style={{padding:"24px 28px 40px",overflowY:"auto"}}>
      <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:6}}><Video size={14} color={C.accent}/><span style={{fontSize:11,fontWeight:700,color:C.accent,textTransform:"uppercase",letterSpacing:"0.09em"}}>Jonli darslar</span></div>
      <h1 style={{fontSize:24,fontWeight:900,color:C.text,margin:"0 0 6px"}}>Ustoz bilan jonli dars</h1>
      <p style={{fontSize:13.5,color:C.textMid,margin:"0 0 18px"}}>Dars boshlanganda "Qo'shilish" tugmasi yonadi. Kamera va mikrofonga ruxsat bering.</p>
      {!session&&<div style={{...card,marginBottom:14,fontSize:13,color:C.danger}}>Darsga qo'shilish uchun avval hisobingizga kiring (Profilim).</div>}
      {error&&<div style={{...card,marginBottom:14,fontSize:13,color:C.danger}}>{error}</div>}
      {loading?<div style={{fontSize:13,color:C.textMid}}>Yuklanmoqda...</div>:!lessons.length?(
        <div style={{...card,textAlign:"center",padding:"40px 20px"}}><div style={{fontSize:42,marginBottom:8}}>🎥</div><div style={{fontSize:16,fontWeight:800,color:C.text}}>Hozircha jonli dars rejalashtirilmagan</div><div style={{fontSize:13,color:C.textMid,marginTop:4}}>Yangi darslar shu yerda paydo bo'ladi.</div></div>
      ):(
        <div style={{display:"flex",flexDirection:"column",gap:12,maxWidth:820}}>
          {live.map(l=><Row key={l.id} l={l}/>)}
          {soon.map(l=><Row key={l.id} l={l}/>)}
        </div>
      )}
    </div>
  );
}
