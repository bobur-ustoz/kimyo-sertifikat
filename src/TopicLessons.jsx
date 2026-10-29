import { useState, useEffect, useRef } from "react";
import { Tag, Play, ChevronLeft, Send, Sparkles } from "lucide-react";
import { supabase } from "./lib/supabaseClient";
import { C } from "./adminStyles";

function VideoBox({Player,videoId,onTime,playerRef}){
  return (
    <div style={{position:"relative",paddingTop:"56.25%",background:"#0F172A",borderRadius:14,overflow:"hidden"}}>
      {videoId
        ? <Player key={videoId} videoId={videoId} onTime={onTime} playerRef={playerRef}/>
        : <div style={{position:"absolute",inset:0,display:"flex",alignItems:"center",justifyContent:"center",color:"#94A3B8",fontSize:13}}>Video tez orada qo'shiladi</div>}
    </div>
  );
}

// Renders \frac{a}{b} as a stacked fraction and _X as a subscript; the rest stays plain text.
function Sub({s}){
  const parts=s.split(/_([A-Za-z0-9]{1,3})/);
  return <>{parts.map((p,i)=>i%2?<sub key={i}>{p}</sub>:p)}</>;
}
export function Rich({text}){
  const out=[]; const re=/\\frac\{([^{}]*)\}\{([^{}]*)\}/g; let last=0,m,k=0;
  while((m=re.exec(text))){
    if(m.index>last) out.push(<Sub key={k++} s={text.slice(last,m.index)}/>);
    out.push(
      <span key={k++} style={{display:"inline-flex",flexDirection:"column",alignItems:"center",verticalAlign:"middle",margin:"0 4px",lineHeight:1.3,fontSize:"0.95em"}}>
        <span style={{padding:"0 5px",borderBottom:"1.5px solid currentColor"}}><Sub s={m[1]}/></span>
        <span style={{padding:"0 5px"}}><Sub s={m[2]}/></span>
      </span>
    );
    last=m.index+m[0].length;
  }
  if(last<text.length) out.push(<Sub key={k++} s={text.slice(last)}/>);
  return <>{out}</>;
}

const fmt=sec=>`${Math.floor(sec/60)}:${String(Math.floor(sec%60)).padStart(2,"0")}`;

export function AskAI({session,target,setTab,time,playerRef}){
  const [q,setQ]=useState("");
  const [busy,setBusy]=useState(false);
  const [thread,setThread]=useState([]);
  const [err,setErr]=useState("");
  const key = target.topicId||target.exampleId||target.questionId;
  const [faq,setFaq]=useState([]);
  const [allOpen,setAllOpen]=useState(false);
  const [locked,setLocked]=useState(false);   // free plan: the assistant is a Premium feature
  useEffect(()=>{
    if(!session){ setLocked(false); return; }
    (async()=>{
      const { data } = await supabase.from("profiles").select("plan,plan_expires_at,is_admin").eq("id",session.user.id).maybeSingle();
      const active=!!data&&!!data.plan&&data.plan!=="free"&&(!data.plan_expires_at||new Date(data.plan_expires_at)>new Date());
      let freeDtm=false;
      if(target.questionId){
        const { data:qv } = await supabase.from("questions").select("variants(is_free,teachers(section))").eq("id",target.questionId).maybeSingle();
        freeDtm=!!qv?.variants?.is_free&&qv.variants.teachers?.section==="dtm";
      }
      setLocked(!!data&&!data.is_admin&&!active&&!freeDtm);
    })();
  },[session?.user?.id,target.questionId]);
  useEffect(()=>{ setThread([]); setErr(""); setQ(""); setAllOpen(false); },[key]);
  useEffect(()=>{
    setFaq([]);
    if(!session) return;
    let live=true;
    supabase.auth.getSession().then(({data:{session:s}})=>{
      if(!s) return;
      return fetch("/api/faq",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${s.access_token}`},body:JSON.stringify(target)})
        .then(r=>r.ok?r.json():{items:[]}).then(d=>{ if(live) setFaq(d.items||[]); });
    }).catch(()=>{});
    return ()=>{live=false;};
  },[key,!!session]);

  // Approved questions answer instantly from the saved text, no AI call.
  const showFaq=(f)=>{
    setThread(t=>[...t,{question:f.question,answer:f.answer,id:f.id,approved:true,flag:null}]);
    if(f.video_seconds!=null) playerRef?.current?.setCurrentTime(f.video_seconds);
  };

  const flag = async (i) => {
    const m=thread[i];
    if(!m?.id) return;
    setThread(t=>t.map((x,j)=>j===i?{...x,flag:"sending"}:x));
    try{
      const { data:{session:s} } = await supabase.auth.getSession();
      if(!s) throw new Error("Sessiya tugagan. Sahifani yangilab, qayta kiring.");
      const r = await fetch("/api/flag-answer",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${s.access_token}`},body:JSON.stringify({questionId:m.id})});
      if(!r.ok) throw new Error();
      setThread(t=>t.map((x,j)=>j===i?{...x,flag:"done"}:x));
    }catch{ setThread(t=>t.map((x,j)=>j===i?{...x,flag:null}:x)); setErr("Xabar yuborilmadi. Keyinroq urinib ko'ring."); }
  };

  if(!session) return (
    <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:12,padding:"14px 16px",fontSize:13,color:C.textMid,display:"flex",alignItems:"center",gap:10,justifyContent:"space-between"}}>
      <span>Video bo'yicha savol berish uchun tizimga kiring.</span>
      <button onClick={()=>setTab("profile")} style={{padding:"8px 14px",borderRadius:9,background:C.primary,color:"#fff",border:"none",fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Kirish</button>
    </div>
  );

  if(locked) return (
    <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:14,padding:"16px 18px",display:"flex",alignItems:"center",gap:12,justifyContent:"space-between",flexWrap:"wrap"}}>
      <div>
        <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:4}}><Sparkles size={15} color={C.accent}/><div style={{fontSize:14,fontWeight:800,color:C.text}}>Savol bering</div></div>
        <div style={{fontSize:13,color:C.textMid}}>AI yordamchi Premium rejada mavjud.</div>
      </div>
      <button onClick={()=>setTab("obuna")} style={{padding:"9px 16px",borderRadius:9,background:C.primary,color:"#fff",border:"none",fontSize:12.5,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Premium'ga o'tish</button>
    </div>
  );

  const ask = async () => {
    const question=q.trim();
    if(!question||busy) return;
    // Show the question at once; the answer fills in when it arrives.
    const tmp=Date.now();
    setBusy(true); setErr(""); setQ("");
    setThread(t=>[...t,{tmp,question,answer:null,id:null,approved:false,flag:null}]);
    try{
      const { data:{session:s} } = await supabase.auth.getSession();
      if(!s) throw new Error("Sessiya tugagan. Sahifani yangilab, qayta kiring.");
      const r = await fetch("/api/ask-video",{method:"POST",headers:{"Content-Type":"application/json",Authorization:`Bearer ${s.access_token}`},body:JSON.stringify({...target,question})});
      const data = await r.json().catch(()=>({}));
      if(!r.ok) throw new Error(data.error||"Server javob bermadi. Keyinroq urinib ko'ring.");
      setThread(t=>t.map(m=>m.tmp===tmp?{...m,answer:data.answer,id:data.id,approved:!!data.approved}:m));
    }catch(e){
      setThread(t=>t.filter(m=>m.tmp!==tmp));
      setQ(question); setErr(e.message);
    }
    setBusy(false);
  };

  return (
    <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:16}}>
      <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:12}}>
        <Sparkles size={15} color={C.accent}/>
        <div style={{fontSize:14,fontWeight:800,color:C.text}}>Savol bering</div>
      </div>
      {faq.length>0&&(()=>{
        const timed=faq.filter(f=>f.video_seconds!=null);
        const WIN=120;
        const near=timed.filter(f=>Math.abs(f.video_seconds-(time||0))<=WIN)
          .sort((a,b)=>Math.abs(a.video_seconds-(time||0))-Math.abs(b.video_seconds-(time||0))).slice(0,4);
        const general=faq.filter(f=>f.video_seconds==null).slice(0,3);
        const chip=f=><button key={f.id} onClick={()=>showFaq(f)} style={{display:"inline-flex",alignItems:"center",gap:6,padding:"6px 11px",borderRadius:20,border:`1px solid ${C.border}`,background:"#fff",fontSize:12.5,color:C.text,cursor:"pointer",fontFamily:"inherit",margin:"0 6px 6px 0",textAlign:"left"}}>
          {f.question}{f.video_seconds!=null&&<span style={{fontSize:11,color:C.textLight}}>{fmt(f.video_seconds)}</span>}</button>;
        const bucket=Array.from(new Set(timed.map(f=>Math.floor(f.video_seconds/300)))).sort((a,b)=>a-b);
        return (
          <div style={{marginBottom:12}}>
            <div style={{fontSize:12,color:C.textMid,marginBottom:6}}>{near.length?`Hozirgi daqiqa (${fmt(time||0)}) atrofidagi savollar:`:"Tez-tez so'raladigan savollar:"}</div>
            <div>{near.map(chip)}{!near.length&&[...timed.slice(0,3),...general].slice(0,4).map(chip)}</div>
            {faq.length>near.length&&<button onClick={()=>setAllOpen(o=>!o)} style={{background:"none",border:"none",padding:0,color:C.accent,fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>{allOpen?"Yopish":`Hammasi (${faq.length})`}</button>}
            {allOpen&&<div style={{marginTop:8}}>
              {bucket.map(b=>(<div key={b} style={{display:"grid",gridTemplateColumns:"84px 1fr",gap:8,padding:"6px 0",borderTop:`1px solid ${C.border}`}}>
                <div style={{fontSize:11.5,color:C.textMid,paddingTop:6}}>{fmt(b*300)} – {fmt(b*300+300)}</div>
                <div>{timed.filter(f=>Math.floor(f.video_seconds/300)===b).map(chip)}</div></div>))}
              {general.length>0&&<div style={{display:"grid",gridTemplateColumns:"84px 1fr",gap:8,padding:"6px 0",borderTop:`1px solid ${C.border}`}}><div style={{fontSize:11.5,color:C.textMid,paddingTop:6}}>Umumiy</div><div>{faq.filter(f=>f.video_seconds==null).map(chip)}</div></div>}
            </div>}
          </div>
        );
      })()}
      {thread.map((m,i)=>(
        <div key={i} style={{marginBottom:12}}>
          <div style={{background:C.mintBg,borderRadius:10,padding:"8px 12px",fontSize:13,color:C.text,marginBottom:6,fontWeight:600}}>{m.question}</div>
          <div style={{padding:"4px 4px 0",fontSize:13,color:C.text,lineHeight:1.65,whiteSpace:"pre-wrap"}}>{m.answer===null?<span style={{color:C.textLight}}>Javob yozilmoqda…</span>:<Rich text={m.answer}/>}</div>
          {m.answer!==null&&<div style={{display:"flex",alignItems:"center",gap:10,padding:"6px 4px 0",fontSize:11.5}}>
            {m.approved&&<span style={{color:C.primary,fontWeight:700}}>✓ O'qituvchi tasdiqlagan</span>}
            {!m.approved&&m.id&&m.flag===null&&<button onClick={()=>flag(i)} style={{background:"none",border:"none",padding:0,color:C.textMid,textDecoration:"underline",cursor:"pointer",fontFamily:"inherit",fontSize:11.5}}>Javob noto'g'rimi?</button>}
            {m.flag==="sending"&&<span style={{color:C.textLight}}>Yuborilmoqda…</span>}
            {m.flag==="done"&&<span style={{color:C.textMid}}>Rahmat! Javob tekshiriladi.</span>}
          </div>}
        </div>
      ))}
      {err&&<p style={{fontSize:12,color:C.danger,marginBottom:8}}>{err}</p>}
      <div style={{display:"flex",gap:8}}>
        <input value={q} maxLength={500} onChange={e=>setQ(e.target.value)} onKeyDown={e=>{if(e.key==="Enter")ask();}} placeholder="Videodagi nimadir tushunarsizmi? Yozing…"
          style={{flex:1,padding:"10px 12px",borderRadius:9,border:`1px solid ${C.border}`,fontSize:13,fontFamily:"inherit",color:C.text}}/>
        <button onClick={ask} disabled={busy||!q.trim()} style={{padding:"10px 14px",borderRadius:9,background:busy||!q.trim()?C.textLight:C.primary,color:"#fff",border:"none",fontSize:12.5,fontWeight:700,cursor:busy?"default":"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:6}}>
          <Send size={13}/> {busy?"Javob yozilmoqda…":"Yuborish"}
        </button>
      </div>
    </div>
  );
}

function Analog({ex}){
  const [show,setShow]=useState(false);
  useEffect(()=>setShow(false),[ex.id]);
  if(!ex.analog_savol) return null;
  return (
    <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:16}}>
      <div style={{fontSize:10.5,fontWeight:800,color:C.accent,textTransform:"uppercase",letterSpacing:"0.08em",marginBottom:6}}>Analog misol</div>
      <p style={{fontSize:13.5,color:C.text,lineHeight:1.65,whiteSpace:"pre-wrap",marginBottom:10}}>{ex.analog_savol}</p>
      {show ? (
        <div style={{background:C.mintBg,borderRadius:10,padding:"10px 12px"}}>
          {ex.analog_yechim&&<p style={{fontSize:12.5,color:C.textMid,lineHeight:1.65,whiteSpace:"pre-wrap",marginBottom:8}}>{ex.analog_yechim}</p>}
          {ex.analog_javob&&<div style={{fontSize:13,fontWeight:800,color:C.text}}>Javob: {ex.analog_javob}</div>}
        </div>
      ) : (
        <button onClick={()=>setShow(true)} style={{padding:"8px 14px",borderRadius:9,background:C.primary,color:"#fff",border:"none",fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Yechimni ko'rsat</button>
      )}
    </div>
  );
}

function TopicPage({topic,Player,session,setTab,onBack,plan}){
  const [examples,setExamples]=useState([]);
  const [active,setActive]=useState(null); // example_number, null = topic video
  const [time,setTime]=useState(0);
  const playerRef=useRef(null);
  useEffect(()=>{ setTime(0); },[active]);
  useEffect(()=>{
    setActive(null);
    supabase.from("topic_examples").select("id,example_number,bunny_video_id,analog_savol,analog_yechim,analog_javob").eq("topic_id",topic.id).order("example_number")
      .then(({data})=>setExamples(data||[]));
  },[topic.id]);
  const ex = examples.find(e=>e.example_number===active);
  return (
    <div style={{padding:"26px 30px",maxWidth:900}}>
      <button onClick={onBack} style={{display:"flex",alignItems:"center",gap:5,padding:"8px 12px",borderRadius:9,background:"#fff",border:`1px solid ${C.border}`,color:C.textMid,fontSize:12,fontWeight:600,cursor:"pointer",fontFamily:"inherit",marginBottom:16}}><ChevronLeft size={14}/> Mavzular</button>
      <h1 style={{fontSize:24,fontWeight:900,color:C.text,marginBottom:4}}>{topic.name}</h1>
      <p style={{fontSize:13,color:C.textMid,marginBottom:16}}>{ex?`${ex.example_number}-misol tahlili`:"Mavzu darsi"}</p>

      <VideoBox Player={Player} videoId={ex?ex.bunny_video_id:topic.bunny_video_id} onTime={sec=>setTime(Math.floor(sec))} playerRef={playerRef}/>
      <div style={{display:"flex",flexDirection:"column",gap:14,marginTop:14}}>
        {ex&&plan!=="free"&&<Analog ex={ex}/>}
        <AskAI session={session} setTab={setTab} time={time} playerRef={playerRef} target={ex?{exampleId:ex.id}:{topicId:topic.id}}/>
      </div>

      <div style={{display:"flex",alignItems:"center",gap:9,margin:"28px 0 12px"}}>
        <div style={{width:4,height:22,background:C.primary,borderRadius:2}}/>
        <h2 style={{fontSize:15.5,fontWeight:800,color:C.text}}>To'plam: {examples.length||20} ta misol tahlili</h2>
      </div>
      {examples.length===0 ? (
        <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:14,padding:28,textAlign:"center",color:C.textMid,fontSize:13}}>Misollar tez orada qo'shiladi.</div>
      ) : (
        <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(110px,1fr))",gap:10}}>
          <button onClick={()=>setActive(null)} style={{padding:"12px 8px",borderRadius:12,border:`2px solid ${active===null?C.primary:C.border}`,background:active===null?C.primary:"#fff",color:active===null?"#fff":C.text,fontSize:12.5,fontWeight:800,cursor:"pointer",fontFamily:"inherit"}}>Mavzu darsi</button>
          {examples.map(e=>{
            const on=active===e.example_number;
            return (
              <button key={e.id} onClick={()=>{setActive(e.example_number);window.scrollTo({top:0,behavior:"smooth"});}} disabled={!e.bunny_video_id}
                style={{padding:"12px 8px",borderRadius:12,border:`2px solid ${on?C.primary:C.border}`,background:on?C.primary:"#fff",color:on?"#fff":e.bunny_video_id?C.text:C.textLight,fontSize:12.5,fontWeight:800,cursor:e.bunny_video_id?"pointer":"default",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:6,opacity:e.bunny_video_id?1:0.55}}>
                <Play size={11} fill="currentColor"/> {e.example_number}-misol
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default function TopicLessons({Player,session,setTab,plan}){
  const [topics,setTopics]=useState(null);
  const [sel,setSel]=useState(null);
  useEffect(()=>{
    supabase.from("topics").select("id,name,bunny_video_id").order("sort_order").order("created_at")
      .then(({data})=>setTopics(data||[]));
  },[]);
  if(sel) return <TopicPage topic={sel} Player={Player} session={session} setTab={setTab} plan={plan} onBack={()=>setSel(null)}/>;
  return (
    <div style={{padding:"26px 30px"}}>
      <h1 style={{fontSize:24,fontWeight:900,color:C.text,marginBottom:6}}>Mavzular</h1>
      <p style={{color:C.textMid,fontSize:13.5,marginBottom:20}}>Mavzuni tanlang: dars videosi, 20 ta misol tahlili va savol-javob.</p>
      {topics===null ? <div style={{color:C.textLight,fontSize:13}}>Yuklanmoqda…</div>
        : topics.length===0 ? <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:16,padding:40,textAlign:"center",color:C.textMid}}>Hali mavzular qo'shilmagan.</div>
        : (
          <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(210px,1fr))",gap:12}}>
            {topics.map(t=>(
              <div key={t.id} onClick={()=>setSel(t)} style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:16,cursor:"pointer",boxShadow:"0 1px 4px rgba(0,0,0,0.04)"}}>
                <Tag size={22} color={C.primary} style={{marginBottom:8}}/>
                <div style={{fontSize:13.5,fontWeight:800,color:C.text,marginBottom:8,lineHeight:1.3}}>{t.name}</div>
                <div style={{display:"inline-flex",background:C.mintBg,color:C.primary,fontSize:10.5,fontWeight:700,padding:"3px 8px",borderRadius:20}}>{t.bunny_video_id?"Video dars bor":"Tez orada"}</div>
              </div>
            ))}
          </div>
        )}
    </div>
  );
}
