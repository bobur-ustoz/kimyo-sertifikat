
import { useState, useEffect } from "react";
import { FlaskConical, Grid3X3, Tag, Wand2, User, Play, Download, ChevronRight, CheckCircle2, Award, TrendingUp, ChevronDown, Eye, Volume2, SkipForward, Settings, Info, BarChart3, Users, BookOpen, AlertTriangle, Trophy, Target, Lightbulb, Zap, Sparkles, Lock, CreditCard, Star, XCircle, RefreshCw, Menu, X } from "lucide-react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from "recharts";
import { supabase } from "./lib/supabaseClient";

const C = { primary:"#0F5132",primaryHov:"#166534",accent:"#0D9488",mint:"#6EE7B7",mintLight:"#D1FAE5",mintBg:"#F0FDF4",bgSoft:"#F8FAFC",text:"#0F172A",textMid:"#475569",textLight:"#94A3B8",border:"#E2E8F0",borderGreen:"#86EFAC",danger:"#DC2626",dangerBg:"#FEF2F2",warning:"#D97706",warningBg:"#FFFBEB" };

const GEN_SRC = [2,1,3,4,2,1,3,4,2,3,1,4,2,3,1,4,2,1,3,4,2,3,4,1,2,3,4,1,2,3,1,4,2,3,1,4,2,1,3,4,2,3,1];
const ANALYTICS = [
  {topic:"Termokimyo",short:"Termo",score:38,attempted:8,correct:3,status:"weak",variants:[3,7,15]},
  {topic:"Elektroliz",short:"Elektroliz",score:42,attempted:12,correct:5,status:"weak",variants:[4,12,18]},
  {topic:"Redoks",short:"Redoks",score:44,attempted:16,correct:7,status:"weak",variants:[2,9,16]},
  {topic:"Muvozanat",short:"Muvozanat",score:57,attempted:14,correct:8,status:"medium",variants:[1,5,8]},
  {topic:"Organik",short:"Organik",score:75,attempted:32,correct:24,status:"good",variants:[]},
  {topic:"Anorganik",short:"Anorganik",score:79,attempted:24,correct:19,status:"good",variants:[]},
  {topic:"Kinetika",short:"Kinetika",score:80,attempted:10,correct:8,status:"good",variants:[]},
  {topic:"Eritmalar",short:"Eritmalar",score:83,attempted:18,correct:15,status:"good",variants:[]},
];
const RADAR=[{subject:"Muvozanat",score:57},{subject:"Eritmalar",score:83},{subject:"Elektroliz",score:42},{subject:"Organik",score:75},{subject:"Anorganik",score:79},{subject:"Redoks",score:44},{subject:"Kinetika",score:80},{subject:"Termokimyo",score:38}];
const PLANS = [
  { id:"free",name:"Bepul",price:"0",period:"har doim",color:"#475569",btnBg:"#F1F5F9",btnColor:"#475569",features:[{t:"3 ta variant ko'rish",ok:true},{t:"Mavzular filtrlash",ok:true},{t:"Asosiy tahlil grafigi",ok:true},{t:"AI Analog Savol Generator",ok:false},{t:"AI Adaptive Test Generator",ok:false},{t:"Barcha o'qituvchilar",ok:false},{t:"PDF yuklab olish",ok:false},{t:"Cheksiz test generatsiya",ok:false}] },
  { id:"standart",name:"Standart",price:"49,900",period:"so'm / oy",color:"#0D9488",btnBg:"#0D9488",btnColor:"#fff",badge:"Mashhur",features:[{t:"Barcha variantlar (20 ta)",ok:true},{t:"Mavzular filtrlash",ok:true},{t:"To'liq tahlil grafigi",ok:true},{t:"AI Analog Savol Generator",ok:true},{t:"AI Adaptive Test Generator",ok:false},{t:"2 ta o'qituvchi kursi",ok:true},{t:"PDF yuklab olish",ok:true},{t:"Cheksiz test generatsiya",ok:false}] },
  { id:"premium",name:"Premium",price:"99,900",period:"so'm / oy",color:"#0F5132",btnBg:"#0F5132",btnColor:"#fff",badge:"🔥 Eng yaxshi",features:[{t:"Barcha variantlar (20 ta)",ok:true},{t:"Mavzular filtrlash",ok:true},{t:"To'liq tahlil grafigi",ok:true},{t:"AI Analog Savol Generator",ok:true},{t:"AI Adaptive Test Generator",ok:true},{t:"Barcha o'qituvchilar",ok:true},{t:"PDF yuklab olish",ok:true},{t:"Cheksiz test generatsiya",ok:true}] },
];

const barCol = s => s>=75?C.primary:s>=60?C.warning:C.danger;
const canUse = (plan,feature) => { if(feature==="analog") return plan!=="free"; if(feature==="adaptive") return plan==="premium"; return true; };

async function fetchTeachers() {
  const { data: tRows } = await supabase.from("teachers").select("*").order("sort_order").order("created_at");
  const { data: vRows } = await supabase.from("variants").select("teacher_id,total_questions");
  const counts = {}, videoCounts = {};
  (vRows||[]).forEach(v=>{ counts[v.teacher_id]=(counts[v.teacher_id]||0)+1; videoCounts[v.teacher_id]=(videoCounts[v.teacher_id]||0)+(v.total_questions||43); });
  return (tRows||[]).map(t=>({ ...t, bgColor:t.bg_color, free:t.is_free, desc:t.description, variants:counts[t.id]||0, videoCount:videoCounts[t.id]||0 }));
}

async function fetchVariants(teacherId) {
  const { data: vRows } = await supabase.from("variants").select("*").eq("teacher_id",teacherId).order("variant_number");
  const ids = (vRows||[]).map(v=>v.id);
  const readyMap = {};
  if (ids.length) {
    const { data: qRows } = await supabase.from("questions").select("variant_id,video_ready").in("variant_id",ids);
    (qRows||[]).forEach(q=>{ if(q.video_ready) readyMap[q.variant_id]=(readyMap[q.variant_id]||0)+1; });
  }
  return (vRows||[]).map(v=>({ id:v.id, number:v.variant_number, total:v.total_questions, ready:readyMap[v.id]||0 }));
}

async function fetchQuestions(variantId) {
  const { data } = await supabase.from("questions").select("*").eq("variant_id",variantId).order("question_number");
  return data||[];
}

async function callClaude(prompt) {
  const res = await fetch("https://api.anthropic.com/v1/messages",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({model:"claude-sonnet-4-6",max_tokens:1000,messages:[{role:"user",content:prompt}]})});
  const data = await res.json();
  const text = data.content[0].text;
  return text.replace(/```json\n?|\n?```/g,"").trim();
}

// ── SIDEBAR ──────────────────────────────────────────────────────
function Sidebar({tab,setTab,teacher,setTeacher,setVarId,plan,mobileOpen,onClose,variants}) {
  const TABS=[{id:"collections",label:"Kolleksiyalar",icon:BookOpen},{id:"variants",label:"Variantlar",icon:Grid3X3},{id:"topics",label:"Mavzular",icon:Tag},{id:"analytics",label:"Tahlil & Grafik",icon:BarChart3},{id:"generator",label:"Test Generator",icon:Wand2},{id:"obuna",label:"Obuna & Narxlar",icon:CreditCard},{id:"profile",label:"Profilim",icon:User}];
  const vList=teacher?variants:[];
  const total=vList.length;
  const done=vList.filter(v=>v.total>0&&v.ready===v.total).length;
  const planColors={free:"#475569",standart:"#0D9488",premium:"#0F5132"};
  const planNames={free:"Bepul",standart:"Standart ⭐",premium:"Premium 💎"};
  return (
    <div className={`app-sidebar${mobileOpen?" open":""}`} style={{width:258,maxWidth:"82vw",minHeight:"100vh",background:"#FAFFFE",borderRight:`1px solid ${C.border}`,display:"flex",flexDirection:"column",position:"fixed",top:0,left:0,zIndex:200}}>
      <div style={{background:C.primary,padding:"18px 18px 14px",display:"flex",alignItems:"center",justifyContent:"space-between"}}>
        <div style={{display:"flex",alignItems:"center",gap:10}}>
          <div style={{width:40,height:40,borderRadius:10,background:"rgba(255,255,255,0.14)",display:"flex",alignItems:"center",justifyContent:"center"}}><FlaskConical size={21} color={C.mint}/></div>
          <div>
            <div style={{color:"#fff",fontWeight:800,fontSize:14.5}}>Kimyo Platform</div>
            <div style={{color:C.mint,fontSize:10,fontWeight:600,marginTop:1}}>Milliy Sertifikat · 2026</div>
          </div>
        </div>
        <button onClick={onClose} className="sidebar-close-btn" style={{display:"none",background:"rgba(255,255,255,0.14)",border:"none",borderRadius:8,width:30,height:30,alignItems:"center",justifyContent:"center",cursor:"pointer",flexShrink:0}}>
          <X size={16} color="#fff"/>
        </button>
      </div>
      <div style={{margin:"10px 10px 0",padding:"7px 10px",borderRadius:9,background:planColors[plan]+"18",border:`1px solid ${planColors[plan]}30`,display:"flex",alignItems:"center",gap:7}}>
        <div style={{width:8,height:8,borderRadius:"50%",background:planColors[plan],flexShrink:0}}/>
        <span style={{fontSize:11,fontWeight:700,color:planColors[plan]}}>Joriy reja: {planNames[plan]}</span>
      </div>
      {teacher?(
        <div style={{margin:"8px 10px 0",padding:"9px 12px",borderRadius:11,background:teacher.bgColor,border:`1px solid ${C.borderGreen}`,display:"flex",alignItems:"center",gap:9}}>
          <div style={{width:32,height:32,borderRadius:9,background:teacher.color,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:900,color:"#fff",flexShrink:0}}>{teacher.initials}</div>
          <div style={{flex:1,minWidth:0}}>
            <div style={{fontSize:11.5,fontWeight:800,color:C.text,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{teacher.name}</div>
            <div style={{fontSize:10,color:C.textMid}}>{teacher.variants} variant</div>
          </div>
          <button onClick={()=>{setTeacher(null);setVarId(null);setTab("collections");onClose?.();}} style={{background:"none",border:"none",cursor:"pointer",fontSize:10,fontWeight:700,color:C.accent,fontFamily:"inherit",padding:"3px 6px",borderRadius:5}}>O'zgartir</button>
        </div>
      ):(
        <div onClick={()=>{setTab("collections");onClose?.();}} style={{margin:"8px 10px 0",padding:"9px 12px",borderRadius:11,background:C.mintBg,border:`1px dashed ${C.borderGreen}`,cursor:"pointer",display:"flex",alignItems:"center",gap:8}}>
          <Users size={14} color={C.primary}/><span style={{fontSize:12,color:C.primary,fontWeight:600}}>O'qituvchi tanlang</span>
          <ChevronRight size={13} color={C.primary} style={{marginLeft:"auto"}}/>
        </div>
      )}
      <nav style={{flex:1,padding:"10px 10px 6px"}}>
        <div style={{fontSize:9.5,fontWeight:700,color:C.textLight,letterSpacing:"0.1em",textTransform:"uppercase",padding:"0 8px 8px"}}>Asosiy bo'limlar</div>
        {TABS.map(t=>{
          const Ic=t.icon; const on=tab===t.id;
          return (
            <button key={t.id} onClick={()=>{setTab(t.id);if(t.id!=="variants")setVarId(null);onClose?.();}}
              style={{display:"flex",alignItems:"center",gap:10,width:"100%",padding:"9px 12px",borderRadius:10,marginBottom:2,background:on?C.primary:"transparent",color:on?"#fff":C.textMid,border:"none",cursor:"pointer",textAlign:"left",fontFamily:"inherit",fontSize:12.5,fontWeight:on?700:500,transition:"all 0.14s"}}
              onMouseEnter={e=>{if(!on){e.currentTarget.style.background=C.mintBg;e.currentTarget.style.color=C.primary;}}}
              onMouseLeave={e=>{if(!on){e.currentTarget.style.background="transparent";e.currentTarget.style.color=C.textMid;}}}>
              <div style={{width:28,height:28,borderRadius:8,flexShrink:0,display:"flex",alignItems:"center",justifyContent:"center",background:on?"rgba(255,255,255,0.15)":C.mintBg}}>
                <Ic size={13} color={on?C.mint:C.primary}/>
              </div>
              {t.label}
              {t.id==="analytics"&&<span style={{marginLeft:"auto",fontSize:9,fontWeight:800,background:on?"rgba(255,255,255,0.2)":"#FEF2F2",color:on?"#fff":C.danger,padding:"2px 6px",borderRadius:8}}>Yangi</span>}
              {t.id==="obuna"&&plan==="free"&&<span style={{marginLeft:"auto",fontSize:9,fontWeight:800,background:on?"rgba(255,255,255,0.2)":"#FFFBEB",color:on?"#fff":C.warning,padding:"2px 6px",borderRadius:8}}>⬆️</span>}
            </button>
          );
        })}
      </nav>
      {teacher&&(
        <div style={{margin:"0 10px 12px",padding:"12px 14px",borderRadius:12,background:C.mintBg,border:`1px solid ${C.borderGreen}`}}>
          <div style={{display:"flex",alignItems:"center",gap:5,marginBottom:6}}><TrendingUp size={11} color={C.primary}/><span style={{fontSize:9.5,fontWeight:800,color:C.primary,textTransform:"uppercase",letterSpacing:"0.07em"}}>Sizning natijangiz</span></div>
          <div style={{fontSize:21,fontWeight:900,color:C.primary,lineHeight:1}}>{done}<span style={{fontSize:12,color:C.textMid,fontWeight:500}}>/{total} Variant</span></div>
          <div style={{fontSize:10,color:C.textMid,margin:"2px 0 8px"}}>video tayyor ✓</div>
          <div style={{background:C.mintLight,borderRadius:4,height:5,overflow:"hidden"}}>
            <div style={{width:`${total?(done/total)*100:0}%`,height:"100%",background:C.primary,borderRadius:4}}/>
          </div>
          <div style={{fontSize:9.5,color:C.textLight,marginTop:4}}>{total?Math.round((done/total)*100):0}% tugatildi</div>
        </div>
      )}
    </div>
  );
}

// ── TEACHERS GRID ─────────────────────────────────────────────────
function TeachersGrid({onSelect,plan,teachers}) {
  const totalVariants = teachers.reduce((s,t)=>s+t.variants,0);
  const totalVideos = teachers.reduce((s,t)=>s+t.videoCount,0);
  const totalStudents = teachers.reduce((s,t)=>s+(t.students||0),0);
  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{marginBottom:22}}>
        <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:8}}><BookOpen size={13} color={C.accent}/><span style={{fontSize:11,fontWeight:700,color:C.accent,textTransform:"uppercase",letterSpacing:"0.09em"}}>Barcha kolleksiyalar · 2026</span></div>
        <h1 style={{fontSize:24,fontWeight:900,color:C.text,marginBottom:6}}>O'qituvchi Kolleksiyalarini Tanlang</h1>
        <p style={{color:C.textMid,fontSize:13.5}}>Har bir o'qituvchining milliy sertifikat variant tahlillari bilan ishlang</p>
      </div>
      <div className="stat-row" style={{display:"flex",gap:12,marginBottom:22}}>
        {[{icon:"👨‍🏫",val:String(teachers.length),label:"O'qituvchi"},{icon:"📚",val:String(totalVariants),label:"Jami variant"},{icon:"🎬",val:totalVideos.toLocaleString(),label:"Video dars"},{icon:"👥",val:totalStudents.toLocaleString()+"+",label:"O'quvchi"}].map(s=>(
          <div key={s.label} style={{flex:1,background:"#fff",border:`1px solid ${C.border}`,borderRadius:12,padding:"13px 14px",display:"flex",alignItems:"center",gap:9,boxShadow:"0 1px 4px rgba(0,0,0,0.04)"}}>
            <span style={{fontSize:22}}>{s.icon}</span>
            <div><div style={{fontSize:18,fontWeight:900,color:C.primary}}>{s.val}</div><div style={{fontSize:10,color:C.textMid}}>{s.label}</div></div>
          </div>
        ))}
      </div>
      {teachers.length===0 ? (
        <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:16,padding:40,textAlign:"center",color:C.textMid}}>
          Hali o'qituvchi qo'shilmagan. <a href="/admin" style={{color:C.accent,fontWeight:700}}>Admin panel</a> orqali qo'shing.
        </div>
      ) : (
      <div style={{display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:15}}>
        {teachers.map(t=>{
          const locked = !t.free && plan==="free";
          return (
            <div key={t.id} onClick={()=>onSelect(t)}
              style={{background:"#fff",borderRadius:16,padding:"22px 20px",border:`1px solid ${C.border}`,cursor:"pointer",transition:"all 0.2s",boxShadow:"0 1px 5px rgba(0,0,0,0.05)",position:"relative",overflow:"hidden",opacity:locked?0.7:1}}
              onMouseEnter={e=>{e.currentTarget.style.transform="translateY(-3px)";e.currentTarget.style.boxShadow="0 10px 28px rgba(0,0,0,0.12)";e.currentTarget.style.borderColor=t.color;}}
              onMouseLeave={e=>{e.currentTarget.style.transform="translateY(0)";e.currentTarget.style.boxShadow="0 1px 5px rgba(0,0,0,0.05)";e.currentTarget.style.borderColor=C.border;}}>
              {t.badge&&<div style={{position:"absolute",top:14,right:14,background:t.color,color:"#fff",fontSize:9.5,fontWeight:800,padding:"3px 9px",borderRadius:20}}>{t.badge}</div>}
              {!t.free&&<div style={{position:"absolute",top:t.badge?38:14,right:14,background:"#FFFBEB",color:"#B45309",border:"1px solid #FDE68A",fontSize:9.5,fontWeight:700,padding:"3px 8px",borderRadius:20}}>💳 Premium</div>}
              {locked&&<div style={{position:"absolute",bottom:0,left:0,right:0,background:"rgba(15,81,50,0.06)",padding:"8px",display:"flex",alignItems:"center",justifyContent:"center",gap:5,borderTop:`1px solid ${C.border}`}}><Lock size={11} color={C.primary}/><span style={{fontSize:10.5,color:C.primary,fontWeight:700}}>Obuna talab qiladi</span></div>}
              <div style={{width:56,height:56,borderRadius:14,background:t.color,display:"flex",alignItems:"center",justifyContent:"center",fontSize:18,fontWeight:900,color:"#fff",marginBottom:14}}>{t.initials}</div>
              <div style={{fontSize:16,fontWeight:800,color:C.text,marginBottom:4}}>{t.name}</div>
              <div style={{display:"inline-flex",background:t.bgColor,color:t.color,fontSize:10.5,fontWeight:700,padding:"3px 9px",borderRadius:20,marginBottom:12,border:`1px solid ${t.color}30`}}>{t.subject}</div>
              <p style={{fontSize:12,color:C.textMid,lineHeight:1.6,marginBottom:14}}>{t.desc}</p>
              <div style={{display:"flex",gap:14,marginBottom:16}}>
                {[[t.variants,"Variant"],[`⭐${t.rating}`,"Reyting"],[(t.students||0).toLocaleString(),"O'quvchi"]].map(([v,l])=>(
                  <div key={l}><div style={{fontSize:15,fontWeight:900,color:t.color}}>{v}</div><div style={{fontSize:10,color:C.textLight}}>{l}</div></div>
                ))}
              </div>
              <button style={{width:"100%",padding:"9px",borderRadius:9,background:locked?"#F1F5F9":t.color,color:locked?C.textMid:"#fff",border:"none",fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:5}}>
                {locked?<><Lock size={11}/> Obuna kerak</>:<><Play size={10} fill="currentColor"/> Ko'rish</>}
              </button>
            </div>
          );
        })}
      </div>
      )}
    </div>
  );
}

// ── VARIANTS GRID ─────────────────────────────────────────────────
function VariantsGrid({teacher,onOpen,variants}) {
  const vList=variants; const done=vList.filter(v=>v.total>0&&v.ready===v.total).length; const totalReady=vList.reduce((s,v)=>s+v.ready,0);
  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{marginBottom:20}}>
        <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:8}}>
          <div style={{width:28,height:28,borderRadius:8,background:teacher.color,display:"flex",alignItems:"center",justifyContent:"center",fontSize:10,fontWeight:900,color:"#fff"}}>{teacher.initials}</div>
          <span style={{fontSize:12,fontWeight:700,color:teacher.color,textTransform:"uppercase",letterSpacing:"0.08em"}}>{teacher.name} · {teacher.subject}</span>
        </div>
        <h1 style={{fontSize:23,fontWeight:900,color:C.text,marginBottom:6}}>{teacher.name} — Variantlar Tahlili</h1>
        <p style={{color:C.textMid,fontSize:13.5}}>Har bir variantdagi masalalar to'liq video tahlili — milliy sertifikat qolipida</p>
      </div>
      <div className="stat-row" style={{display:"flex",gap:12,marginBottom:20}}>
        {[{icon:"📚",val:vList.length,label:"Jami variantlar"},{icon:"🎬",val:vList.reduce((s,v)=>s+v.total,0),label:"Jami savol"},{icon:"✅",val:done,label:"To'liq tayyor"},{icon:"👁",val:totalReady,label:"Video tayyor"}].map(s=>(
          <div key={s.label} style={{flex:1,background:"#fff",border:`1px solid ${C.border}`,borderRadius:12,padding:"12px 13px",display:"flex",alignItems:"center",gap:8,boxShadow:"0 1px 4px rgba(0,0,0,0.04)"}}>
            <span style={{fontSize:20}}>{s.icon}</span>
            <div><div style={{fontSize:17,fontWeight:900,color:C.primary}}>{s.val}</div><div style={{fontSize:10,color:C.textMid}}>{s.label}</div></div>
          </div>
        ))}
      </div>
      {vList.length===0 ? (
        <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:16,padding:40,textAlign:"center",color:C.textMid}}>
          Hali variant qo'shilmagan. <a href="/admin" style={{color:C.accent,fontWeight:700}}>Admin panel</a> orqali qo'shing.
        </div>
      ) : (
      <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:14}}>
        {vList.map(v=>{
          const pct=v.total?Math.round((v.ready/v.total)*100):0; const dn=v.total>0&&v.ready===v.total; const bc=pct===100?C.primary:pct>60?C.accent:C.mint;
          return (
            <div key={v.id} onClick={()=>onOpen(v.number)}
              style={{background:"#fff",borderRadius:14,padding:"16px 15px",border:dn?`2px solid ${C.primary}`:`1px solid ${C.border}`,cursor:"pointer",transition:"all 0.2s",boxShadow:dn?"0 4px 16px rgba(15,81,50,0.13)":"0 1px 4px rgba(0,0,0,0.05)",position:"relative"}}
              onMouseEnter={e=>{e.currentTarget.style.transform="translateY(-3px)";e.currentTarget.style.boxShadow="0 10px 26px rgba(15,81,50,0.16)";}}
              onMouseLeave={e=>{e.currentTarget.style.transform="translateY(0)";e.currentTarget.style.boxShadow=dn?"0 4px 16px rgba(15,81,50,0.13)":"0 1px 4px rgba(0,0,0,0.05)";}}>
              {dn&&<div style={{position:"absolute",top:10,right:10}}><CheckCircle2 size={15} color={C.primary}/></div>}
              <div style={{display:"inline-flex",alignItems:"center",gap:4,background:C.mintBg,color:C.primary,border:`1px solid ${C.borderGreen}`,fontSize:9.5,fontWeight:700,padding:"3px 8px",borderRadius:20,marginBottom:9}}><Award size={8}/> Milliy qolip</div>
              <div style={{fontSize:16,fontWeight:900,color:C.text,marginBottom:2}}>{v.number}-Variant</div>
              <div style={{fontSize:10.5,color:C.textMid,marginBottom:10}}>{v.total} ta masala · video tahlil</div>
              <div style={{marginBottom:10}}>
                <div style={{display:"flex",justifyContent:"space-between",marginBottom:4}}><span style={{fontSize:10,color:C.textMid}}>Video tayyor</span><span style={{fontSize:11,fontWeight:800,color:dn?C.primary:C.textMid}}>{v.ready}/{v.total}</span></div>
                <div style={{background:"#F1F5F9",borderRadius:4,height:6,overflow:"hidden"}}><div style={{width:`${pct}%`,height:"100%",borderRadius:4,background:bc}}/></div>
                <div style={{fontSize:9.5,color:C.textLight,marginTop:3}}>{pct}% bajarildi</div>
              </div>
              <button style={{width:"100%",padding:"8px",borderRadius:8,background:dn?C.mintBg:C.primary,color:dn?C.primary:"#fff",border:dn?`1px solid ${C.borderGreen}`:"none",fontSize:11.5,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:5}}>
                <Play size={10} fill="currentColor"/> {dn?"Takror ko'rish":"Tahlilni ko'rish"}
              </button>
            </div>
          );
        })}
      </div>
      )}
    </div>
  );
}

// ── VIDEO PLAYER ──────────────────────────────────────────────────
function VideoPlayer({variantId,teacher,onBack,plan,setTab,questions}) {
  const [activeQ,setActiveQ]=useState(questions[0]?.question_number||1);
  const [aiState,setAiState]=useState("idle");
  const [aiResult,setAiResult]=useState(null);
  const total=questions.length; const ready=questions.filter(q=>q.video_ready).length;
  const curQ=questions.find(q=>q.question_number===activeQ);
  const curTopic=curQ?.topic||"";

  const generateAnalog = async () => {
    setAiState("loading"); setAiResult(null);
    try {
      const prompt = `Kimyo fani bo'yicha "${curTopic}" mavzusida analog savol yarat. O'zbek tilida. FAQAT JSON formatda javob ber, boshqa hech narsa yozma:\n{"savol":"savol matni","formula":"asosiy formula","yechim":["1-qadam","2-qadam","3-qadam"],"javob":"yakuniy javob"}`;
      const text = await callClaude(prompt);
      const parsed = JSON.parse(text);
      setAiResult(parsed); setAiState("done");
    } catch(e) { setAiState("error"); }
  };

  const allowed = canUse(plan,"analog");
  return (
    <div className="video-layout" style={{display:"flex",gap:0,height:"100%",overflow:"hidden"}}>
      <div style={{flex:1,minWidth:0,overflowY:"auto",padding:"20px 22px 24px 26px"}}>
        <div style={{display:"flex",alignItems:"center",gap:5,marginBottom:13,fontSize:12.5,color:C.textMid}}>
          <button onClick={onBack} style={{background:"none",border:"none",cursor:"pointer",color:C.accent,fontWeight:600,fontFamily:"inherit",fontSize:12.5,padding:0}}>Variantlar</button>
          <ChevronRight size={13}/><span style={{color:C.primary,fontWeight:700}}>{variantId}-Variant</span>
          <ChevronRight size={13}/><span style={{color:C.text,fontWeight:700}}>{activeQ}-Savol</span>
        </div>
        <div style={{background:"#0A0F1E",borderRadius:14,overflow:"hidden",aspectRatio:"16/9",width:"100%",position:"relative",marginBottom:15,boxShadow:"0 10px 36px rgba(0,0,0,0.22)"}}>
          <a href={curQ?.video_url||undefined} target="_blank" rel="noreferrer" style={{position:"absolute",inset:0,display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",background:"radial-gradient(ellipse at center,#0d2040 0%,#060c17 100%)",cursor:curQ?.video_url?"pointer":"default",textDecoration:"none"}}
            onClick={e=>{if(!curQ?.video_url)e.preventDefault();}}>
            <div style={{position:"absolute",top:18,left:28,opacity:0.1,fontSize:54,userSelect:"none"}}>⬡</div>
            <div style={{width:62,height:62,borderRadius:"50%",background:curQ?.video_ready?C.primary:"#334155",display:"flex",alignItems:"center",justifyContent:"center",boxShadow:curQ?.video_ready?"0 0 0 14px rgba(15,81,50,0.2),0 0 0 28px rgba(15,81,50,0.08)":"none"}}><Play size={24} color="#fff" fill="#fff" style={{marginLeft:3}}/></div>
            <div style={{color:"#e2e8f0",fontSize:13,marginTop:16,fontWeight:600}}>{teacher.name} · {variantId}-Variant · {activeQ}-Savol</div>
            <div style={{color:C.mint,fontSize:11.5,marginTop:4}}>{curTopic||"Mavzu kiritilmagan"}</div>
            {!curQ?.video_ready&&<div style={{color:"#94A3B8",fontSize:11,marginTop:10,background:"rgba(255,255,255,0.06)",padding:"4px 12px",borderRadius:20}}>Video hali tayyor emas</div>}
          </a>
          {curQ?.video_ready&&(
          <div style={{position:"absolute",bottom:0,left:0,right:0,padding:"12px 16px",background:"linear-gradient(transparent,rgba(0,0,0,0.88))",display:"flex",alignItems:"center",gap:10}}>
            <Play size={14} color="#fff" fill="#fff"/>
            <div style={{flex:1,height:3,background:"rgba(255,255,255,0.18)",borderRadius:2}}><div style={{width:"35%",height:"100%",background:C.mint,borderRadius:2}}/></div>
            <Volume2 size={13} color="#fff"/><SkipForward size={13} color="#fff"/>
          </div>
          )}
        </div>
        <div style={{background:C.mintBg,border:`1px solid ${C.borderGreen}`,borderRadius:11,padding:"10px 15px",marginBottom:12,display:"flex",flexWrap:"wrap",gap:7}}>
          {[["Savol",`${activeQ}-savol`],["Yil","2026"],["Mavzu",curTopic],["O'qituvchi",teacher.name]].map(([l,val])=>(
            <div key={l} style={{display:"flex",alignItems:"center",gap:5,background:"#fff",padding:"4px 11px",borderRadius:20,border:`1px solid ${C.border}`}}>
              <span style={{fontSize:10.5,color:C.textMid}}>{l}:</span><span style={{fontSize:11.5,fontWeight:800,color:C.primary}}>{val}</span>
            </div>
          ))}
        </div>
        <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:12,padding:"16px 18px",marginBottom:12}}>
          <div style={{fontSize:10,fontWeight:800,color:C.textLight,textTransform:"uppercase",letterSpacing:"0.09em",marginBottom:8}}>Savol matni — {variantId}-Variant · {activeQ}-Savol</div>
          <p style={{fontSize:14,color:C.text,lineHeight:1.75,marginBottom:11}}>{curQ?.question_text||"Savol matni hali admin panelda kiritilmagan."}</p>
          {curQ?.formula&&<div style={{background:C.mintBg,border:`1px solid ${C.borderGreen}`,borderRadius:9,padding:"10px 15px",fontFamily:"'Courier New',monospace",fontSize:13.5,color:C.primary}}>{curQ.formula}</div>}
        </div>

        {/* Static PDF button */}
        <div style={{background:C.primary,borderRadius:13,padding:"14px 18px",display:"flex",alignItems:"center",gap:13,cursor:"pointer",boxShadow:"0 6px 20px rgba(15,81,50,0.28)",marginBottom:12}}>
          <div style={{width:42,height:42,borderRadius:10,flexShrink:0,background:"rgba(255,255,255,0.14)",display:"flex",alignItems:"center",justifyContent:"center"}}><Download size={18} color={C.mint}/></div>
          <div>
            <div style={{color:"#fff",fontWeight:800,fontSize:13.5}}>Analog misol yuklab olish (PDF)</div>
            <div style={{color:"#A7F3D0",fontSize:11.5,marginTop:3}}>Ushbu savolga mos o'xshash analog misollar yordamida o'zingizni sinang.</div>
          </div>
        </div>

        {/* AI ANALOG SECTION */}
        {!allowed ? (
          <div style={{background:"#F8FAFC",border:`1px dashed ${C.border}`,borderRadius:13,padding:"16px 18px",display:"flex",alignItems:"center",gap:14}}>
            <div style={{width:42,height:42,borderRadius:10,background:"#F1F5F9",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}><Lock size={18} color={C.textLight}/></div>
            <div style={{flex:1}}>
              <div style={{fontWeight:800,fontSize:13.5,color:C.textMid,marginBottom:3}}>🤖 AI Analog Savol Generator</div>
              <div style={{fontSize:12,color:C.textLight}}>Bu funksiya Standart yoki Premium rejada mavjud</div>
            </div>
            <button onClick={()=>setTab("obuna")} style={{padding:"8px 16px",borderRadius:9,background:C.primary,color:"#fff",border:"none",fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit",flexShrink:0}}>Obuna</button>
          </div>
        ) : (
          <div style={{background:"linear-gradient(135deg,#0F172A 0%,#1E3A5F 100%)",borderRadius:13,padding:"16px 18px"}}>
            <div style={{display:"flex",alignItems:"center",gap:12,marginBottom:aiState!=="idle"?14:0}}>
              <div style={{width:42,height:42,borderRadius:10,background:"rgba(110,231,183,0.15)",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}><Sparkles size={18} color={C.mint}/></div>
              <div style={{flex:1}}>
                <div style={{color:"#fff",fontWeight:800,fontSize:13.5}}>Claude AI — Analog Savol Generator</div>
                <div style={{color:"#94A3B8",fontSize:11.5,marginTop:2}}>Mavzu: <span style={{color:C.mint,fontWeight:600}}>{curTopic}</span></div>
              </div>
              {aiState==="idle"&&(
                <button onClick={generateAnalog} style={{padding:"9px 16px",borderRadius:9,background:C.mint,color:C.primary,border:"none",fontSize:12.5,fontWeight:800,cursor:"pointer",fontFamily:"inherit",flexShrink:0,display:"flex",alignItems:"center",gap:6}}>
                  <Sparkles size={12}/> Yaratish
                </button>
              )}
              {aiState==="done"&&(
                <button onClick={()=>{setAiState("idle");setAiResult(null);}} style={{padding:"7px 12px",borderRadius:9,background:"rgba(255,255,255,0.1)",color:"#94A3B8",border:"1px solid rgba(255,255,255,0.1)",fontSize:11,fontWeight:600,cursor:"pointer",fontFamily:"inherit",flexShrink:0,display:"flex",alignItems:"center",gap:5}}>
                  <RefreshCw size={11}/> Yangi
                </button>
              )}
            </div>
            {aiState==="loading"&&(
              <div style={{display:"flex",alignItems:"center",gap:10,padding:"12px",background:"rgba(255,255,255,0.05)",borderRadius:10}}>
                <div style={{width:18,height:18,border:"2.5px solid rgba(110,231,183,0.3)",borderTopColor:C.mint,borderRadius:"50%",animation:"spin 0.75s linear infinite",flexShrink:0}}/>
                <span style={{color:"#94A3B8",fontSize:13}}>Claude AI analog savol yaratmoqda...</span>
              </div>
            )}
            {aiState==="error"&&(
              <div style={{display:"flex",alignItems:"center",gap:10,padding:"12px",background:"rgba(220,38,38,0.1)",borderRadius:10,border:"1px solid rgba(220,38,38,0.2)"}}>
                <XCircle size={16} color={C.danger}/>
                <span style={{color:"#FCA5A5",fontSize:13}}>Xatolik yuz berdi. Qayta urinib ko'ring.</span>
                <button onClick={generateAnalog} style={{marginLeft:"auto",padding:"5px 10px",background:"rgba(220,38,38,0.2)",border:"none",borderRadius:7,color:"#FCA5A5",fontSize:11,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Qayta</button>
              </div>
            )}
            {aiState==="done"&&aiResult&&(
              <div style={{background:"rgba(255,255,255,0.05)",borderRadius:10,padding:"14px",border:"1px solid rgba(110,231,183,0.2)"}}>
                <div style={{display:"flex",alignItems:"center",gap:6,marginBottom:10}}>
                  <Sparkles size={13} color={C.mint}/>
                  <span style={{color:C.mint,fontSize:11,fontWeight:700,textTransform:"uppercase",letterSpacing:"0.08em"}}>AI tomonidan yaratilgan analog savol</span>
                </div>
                <p style={{color:"#E2E8F0",fontSize:13.5,lineHeight:1.7,marginBottom:10}}>{aiResult.savol}</p>
                {aiResult.formula&&<div style={{fontFamily:"'Courier New',monospace",fontSize:13,color:C.mint,background:"rgba(110,231,183,0.08)",padding:"8px 12px",borderRadius:8,marginBottom:10,border:"1px solid rgba(110,231,183,0.15)"}}>{aiResult.formula}</div>}
                <div style={{marginBottom:8}}>
                  <div style={{fontSize:11,fontWeight:700,color:"#94A3B8",textTransform:"uppercase",letterSpacing:"0.07em",marginBottom:7}}>Yechim bosqichlari:</div>
                  {(aiResult.yechim||[]).map((step,i)=>(
                    <div key={i} style={{display:"flex",gap:9,marginBottom:6,alignItems:"flex-start"}}>
                      <div style={{width:20,height:20,borderRadius:"50%",background:"rgba(110,231,183,0.15)",display:"flex",alignItems:"center",justifyContent:"center",fontSize:10,fontWeight:800,color:C.mint,flexShrink:0,marginTop:1}}>{i+1}</div>
                      <span style={{color:"#CBD5E1",fontSize:12.5,lineHeight:1.6}}>{step}</span>
                    </div>
                  ))}
                </div>
                {aiResult.javob&&<div style={{background:"rgba(15,81,50,0.3)",borderRadius:8,padding:"9px 12px",border:"1px solid rgba(110,231,183,0.25)"}}>
                  <span style={{fontSize:11,fontWeight:700,color:C.mint}}>Javob: </span>
                  <span style={{fontSize:13,color:"#E2E8F0",fontWeight:600}}>{aiResult.javob}</span>
                </div>}
              </div>
            )}
          </div>
        )}
      </div>

      <div className="video-sidebar" style={{width:250,borderLeft:`1px solid ${C.border}`,background:"#fff",overflowY:"auto",flexShrink:0,padding:"14px 11px"}}>
        <div style={{fontSize:10,fontWeight:800,color:C.textLight,textTransform:"uppercase",letterSpacing:"0.09em",marginBottom:4,padding:"0 4px"}}>{variantId}-Variant · Savollar</div>
        <div style={{fontSize:11,color:C.textMid,marginBottom:10,padding:"0 4px"}}>{ready}/{total} video tayyor</div>
        {questions.map(q=>{
          const isA=q.question_number===activeQ; const isW=q.video_ready;
          return (
            <button key={q.id} onClick={()=>{setActiveQ(q.question_number);setAiState("idle");setAiResult(null);}}
              style={{width:"100%",padding:"7px 9px",borderRadius:8,marginBottom:3,background:isA?C.primary:"transparent",border:isA?"none":`1px solid ${isW?"#BBF7D0":C.border}`,cursor:"pointer",textAlign:"left",fontFamily:"inherit",display:"flex",alignItems:"center",gap:7}}>
              <div style={{width:22,height:22,borderRadius:"50%",flexShrink:0,background:isA?"rgba(255,255,255,0.18)":isW?C.mintBg:"#F1F5F9",display:"flex",alignItems:"center",justifyContent:"center",fontSize:9,fontWeight:800,color:isA?C.mint:isW?C.primary:C.textMid}}>
                {isW&&!isA?"✓":q.question_number}
              </div>
              <div style={{minWidth:0,flex:1}}>
                <div style={{fontSize:10.5,fontWeight:700,color:isA?"#fff":C.text,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{q.question_number}-Savol</div>
                <div style={{fontSize:9,color:isA?"#A7F3D0":C.textLight,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{q.topic||"—"}</div>
              </div>
              {isA&&<div style={{width:6,height:6,borderRadius:"50%",background:C.mint,flexShrink:0,boxShadow:"0 0 0 3px rgba(110,231,183,0.3)"}}/>}
            </button>
          );
        })}
      </div>
    </div>
  );
}

// ── TOPICS DIRECTORY ─────────────────────────────────────────────
function TopicsDirectory({onGoVariant,teacher,setTab,questions}) {
  const topicMap={};
  questions.forEach(q=>{ if(q.topic){ (topicMap[q.topic]=topicMap[q.topic]||[]).push(q); } });
  const topicsList=Object.entries(topicMap).map(([name,qs])=>({name,qs})).sort((a,b)=>b.qs.length-a.qs.length);
  const [sel,setSel]=useState(null);
  const activeSel = sel && topicMap[sel] ? sel : topicsList[0]?.name;
  const qs = topicMap[activeSel]||[];

  if(!teacher) return (
    <div style={{display:"flex",alignItems:"center",justifyContent:"center",flex:1,flexDirection:"column",gap:16,padding:48,textAlign:"center"}}>
      <div style={{fontSize:52}}>📂</div>
      <div style={{fontSize:20,fontWeight:800,color:C.text}}>O'qituvchi tanlanmagan</div>
      <div style={{fontSize:14,color:C.textMid,maxWidth:340,lineHeight:1.6}}>Mavzular bo'yicha tahlil ko'rish uchun avval o'qituvchi test to'plamini tanlang</div>
      <button onClick={()=>setTab("collections")} style={{padding:"12px 28px",borderRadius:10,background:C.primary,color:"#fff",border:"none",fontSize:14,fontWeight:700,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:8}}>
        <BookOpen size={15}/> Kolleksiyalarni ko'rish
      </button>
    </div>
  );

  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{marginBottom:20}}>
        <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10}}>
          <div style={{width:30,height:30,borderRadius:9,background:teacher.color,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:900,color:"#fff",flexShrink:0}}>{teacher.initials}</div>
          <span style={{fontSize:12,fontWeight:700,color:teacher.color,textTransform:"uppercase",letterSpacing:"0.08em"}}>{teacher.name} · {teacher.subject}</span>
        </div>
        <h1 style={{fontSize:24,fontWeight:900,color:C.text,marginBottom:6}}>Mavzular bo'yicha Tahlil</h1>
        <p style={{color:C.textMid,fontSize:13.5}}><strong>{teacher.name}</strong> test to'plamidagi masalalarni kimyo mavzulari bo'yicha guruhlangan holda ko'ring</p>
      </div>
      {topicsList.length===0 ? (
        <div style={{background:"#fff",border:`1px dashed ${C.border}`,borderRadius:16,padding:40,textAlign:"center",color:C.textMid}}>
          Hali savollarga mavzu kiritilmagan. <a href="/admin" style={{color:C.accent,fontWeight:700}}>Admin panel</a> orqali kiriting.
        </div>
      ) : (<>
      <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:12,marginBottom:24}}>
        {topicsList.map(c=>{const on=activeSel===c.name;return(
          <div key={c.name} onClick={()=>setSel(c.name)} style={{background:on?C.primary:"#fff",border:on?`2px solid ${C.primary}`:`1px solid ${C.border}`,borderRadius:14,padding:"16px",cursor:"pointer",transition:"all 0.18s",boxShadow:on?"0 6px 20px rgba(15,81,50,0.2)":"0 1px 4px rgba(0,0,0,0.04)"}}>
            <div style={{fontSize:26,marginBottom:8}}><Tag size={22} color={on?"#fff":teacher.color}/></div>
            <div style={{fontSize:12,fontWeight:800,color:on?"#fff":C.text,marginBottom:6,lineHeight:1.3}}>{c.name}</div>
            <div style={{display:"inline-flex",background:on?"rgba(255,255,255,0.16)":C.mintBg,color:on?C.mint:C.primary,fontSize:10.5,fontWeight:700,padding:"3px 8px",borderRadius:20}}>{c.qs.length} masala</div>
          </div>
        );})}
      </div>
      <div style={{display:"flex",alignItems:"center",gap:9,marginBottom:14}}>
        <div style={{width:4,height:25,background:teacher.color,borderRadius:2}}/>
        <h2 style={{fontSize:15.5,fontWeight:800,color:C.text}}>
          "{activeSel}" — <span style={{color:teacher.color}}>{teacher.name}</span> to'plamidagi masalalar
        </h2>
        <span style={{background:teacher.bgColor,color:teacher.color,border:`1px solid ${teacher.color}30`,fontSize:10.5,fontWeight:800,padding:"3px 10px",borderRadius:20}}>{qs.length} ta topildi</span>
      </div>
      <div style={{display:"flex",flexDirection:"column",gap:9}}>
        {qs.map(q=>(
            <div key={q.id} style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:13,padding:"14px 17px",display:"flex",alignItems:"center",gap:13,boxShadow:"0 1px 4px rgba(0,0,0,0.04)"}}>
              <div style={{width:46,height:46,borderRadius:11,background:teacher.bgColor,display:"flex",alignItems:"center",justifyContent:"center",fontSize:21,flexShrink:0}}><Tag size={19} color={teacher.color}/></div>
              <div style={{flex:1}}>
                <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:3}}>
                  <div style={{fontSize:13.5,fontWeight:800,color:C.text}}>{q.variant_number}-Variant · {q.question_number}-Savol</div>
                  {q.video_ready&&<div style={{display:"flex",alignItems:"center",gap:5,background:teacher.bgColor,padding:"2px 9px",borderRadius:20,border:`1px solid ${teacher.color}25`}}><CheckCircle2 size={11} color={teacher.color}/><span style={{fontSize:10,fontWeight:700,color:teacher.color}}>Video tayyor</span></div>}
                </div>
                {q.formula&&<div style={{fontFamily:"'Courier New',monospace",fontSize:12.5,color:teacher.color,background:teacher.bgColor,padding:"3px 10px",borderRadius:7,display:"inline-block",border:`1px solid ${teacher.color}25`}}>{q.formula}</div>}
              </div>
              <button onClick={()=>onGoVariant(q.variant_number)} style={{display:"flex",alignItems:"center",gap:5,padding:"8px 13px",background:teacher.color,color:"#fff",border:"none",borderRadius:9,fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit",flexShrink:0}}>
                <Play size={10} fill="currentColor"/> Ko'rish
              </button>
            </div>
        ))}
      </div>
      </>)}
    </div>
  );
}

// ── ANALYTICS SCREEN ──────────────────────────────────────────────
function BTooltip({active,payload,label}){
  if(!active||!payload?.length)return null;
  const d=ANALYTICS.find(b=>b.short===label); const col=barCol(payload[0].value);
  return(<div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:10,padding:"12px 15px",boxShadow:"0 4px 16px rgba(0,0,0,0.1)",minWidth:180}}>
    <div style={{fontWeight:800,color:C.text,marginBottom:6}}>{d?.topic}</div>
    <div style={{display:"flex",alignItems:"center",gap:6,marginBottom:4}}><div style={{width:10,height:10,borderRadius:2,background:col}}/><span style={{fontSize:13,fontWeight:700,color:col}}>{payload[0].value}%</span><span style={{fontSize:11,color:C.textMid}}>ball</span></div>
    <div style={{fontSize:11,color:C.textMid}}>{d?.correct}/{d?.attempted} to'g'ri javob</div>
  </div>);
}
function AnalyticsScreen(){
  const avg=Math.round(ANALYTICS.reduce((s,b)=>s+b.score,0)/ANALYTICS.length);
  const weak=ANALYTICS.filter(b=>b.status==="weak"); const med=ANALYTICS.filter(b=>b.status==="medium"); const good=ANALYTICS.filter(b=>b.status==="good");
  return(
    <div style={{padding:"24px 28px",overflowY:"auto"}}>
      <div style={{marginBottom:18}}>
        <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:8}}><BarChart3 size={14} color={C.accent}/><span style={{fontSize:11,fontWeight:700,color:C.accent,textTransform:"uppercase",letterSpacing:"0.09em"}}>O'quv tahlili · Real vaqt statistikasi</span></div>
        <h1 style={{fontSize:22,fontWeight:900,color:C.text,marginBottom:6}}>Qaysi Mavzular Qiyin? — Grafik Tahlil</h1>
        <p style={{color:C.textMid,fontSize:13.5}}>Har bir kimyo mavzusidan ko'rsatgan natijangiz va tavsiyalar</p>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:12,marginBottom:18}}>
        {[{icon:<Trophy size={17} color="#fff"/>,label:"Umumiy ball",val:`${avg}%`,sub:"O'rtacha",bg:avg>=75?C.primary:avg>=60?C.warning:C.danger},
          {icon:<AlertTriangle size={17} color="#fff"/>,label:"Kuchsiz",val:weak.length,sub:"< 60% natija",bg:C.danger},
          {icon:<Target size={17} color="#fff"/>,label:"O'rta",val:med.length,sub:"60–75%",bg:C.warning},
          {icon:<CheckCircle2 size={17} color="#fff"/>,label:"Kuchli",val:good.length,sub:"> 75% natija",bg:C.primary}].map(s=>(
          <div key={s.label} style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:13,padding:"14px 16px",boxShadow:"0 1px 5px rgba(0,0,0,0.05)",position:"relative",overflow:"hidden"}}>
            <div style={{position:"absolute",top:0,right:0,width:48,height:48,borderRadius:"0 13px 0 36px",background:s.bg,display:"flex",alignItems:"center",justifyContent:"center"}}>{s.icon}</div>
            <div style={{fontSize:26,fontWeight:900,color:s.bg,marginBottom:2,lineHeight:1}}>{s.val}</div>
            <div style={{fontSize:12.5,fontWeight:700,color:C.text,marginBottom:2}}>{s.label}</div>
            <div style={{fontSize:10.5,color:C.textMid}}>{s.sub}</div>
          </div>
        ))}
      </div>
      <div style={{display:"grid",gridTemplateColumns:"58% 42%",gap:14,marginBottom:18}}>
        <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:"18px 18px 14px",boxShadow:"0 1px 5px rgba(0,0,0,0.05)"}}>
          <div style={{fontSize:13.5,fontWeight:800,color:C.text,marginBottom:3}}>Mavzular bo'yicha ball</div>
          <div style={{fontSize:11,color:C.textMid,marginBottom:10}}>Past ball — ko'proq mashq talab qiladi</div>
          <div style={{display:"flex",gap:12,marginBottom:10}}>
            {[["< 60% — Kuchsiz",C.danger],["60–75% — O'rta",C.warning],["> 75% — Kuchli",C.primary]].map(([l,col])=>(
              <div key={l} style={{display:"flex",alignItems:"center",gap:5}}><div style={{width:10,height:10,borderRadius:2,background:col}}/><span style={{fontSize:10.5,color:C.textMid}}>{l}</span></div>
            ))}
          </div>
          <ResponsiveContainer width="100%" height={230}>
            <BarChart data={ANALYTICS} layout="vertical" margin={{top:0,right:16,left:0,bottom:0}}>
              <CartesianGrid strokeDasharray="3 3" horizontal={false} stroke="#F1F5F9"/>
              <XAxis type="number" domain={[0,100]} tickCount={6} tick={{fontSize:10,fill:C.textLight}} tickFormatter={v=>`${v}%`}/>
              <YAxis type="category" dataKey="short" width={70} tick={{fontSize:11,fill:C.text,fontWeight:600}}/>
              <Tooltip content={<BTooltip/>}/>
              <Bar dataKey="score" radius={[0,5,5,0]} maxBarSize={20}>{ANALYTICS.map((e,i)=><Cell key={i} fill={barCol(e.score)}/>)}</Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:"18px",boxShadow:"0 1px 5px rgba(0,0,0,0.05)"}}>
          <div style={{fontSize:13.5,fontWeight:800,color:C.text,marginBottom:3}}>Qamrov Diagrammasi</div>
          <div style={{fontSize:11,color:C.textMid,marginBottom:10}}>8 soha bo'yicha umumiy ko'rinish</div>
          <ResponsiveContainer width="100%" height={230}>
            <RadarChart data={RADAR} margin={{top:10,right:20,left:20,bottom:10}}>
              <PolarGrid stroke={C.border}/>
              <PolarAngleAxis dataKey="subject" tick={{fontSize:9.5,fill:C.textMid,fontWeight:600}}/>
              <PolarRadiusAxis angle={30} domain={[0,100]} tick={{fontSize:9,fill:C.textLight}}/>
              <Radar name="Ball" dataKey="score" stroke={C.primary} fill={C.primary} fillOpacity={0.25} strokeWidth={2}/>
            </RadarChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:14,marginBottom:14}}>
        <div style={{background:C.dangerBg,border:"1px solid #FECACA",borderRadius:14,padding:"16px"}}>
          <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:13}}><AlertTriangle size={15} color={C.danger}/><div style={{fontSize:13,fontWeight:800,color:C.danger}}>Zudlik bilan mustahkamlang!</div></div>
          {weak.map(b=>(
            <div key={b.topic} style={{background:"#fff",borderRadius:10,padding:"11px 13px",marginBottom:7,border:"1px solid #FECACA"}}>
              <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:5}}><span style={{fontSize:12.5,fontWeight:800,color:C.text}}>{b.topic}</span><span style={{fontSize:13.5,fontWeight:900,color:C.danger}}>{b.score}%</span></div>
              <div style={{background:"#F1F5F9",borderRadius:3,height:5,overflow:"hidden",marginBottom:5}}><div style={{width:`${b.score}%`,height:"100%",background:C.danger,borderRadius:3}}/></div>
              <div style={{fontSize:10.5,color:C.textMid}}>{b.correct}/{b.attempted} to'g'ri · Qaytaring: <strong>{b.variants.map(v=>`${v}-V`).join(", ")}</strong></div>
            </div>
          ))}
        </div>
        <div>
          <div style={{background:C.warningBg,border:"1px solid #FDE68A",borderRadius:14,padding:"14px",marginBottom:12}}>
            <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:11}}><Lightbulb size={14} color={C.warning}/><div style={{fontSize:12.5,fontWeight:800,color:C.warning}}>Mashq talab qiladi</div></div>
            {med.map(b=>(
              <div key={b.topic} style={{background:"#fff",borderRadius:10,padding:"10px 12px",border:"1px solid #FDE68A",marginBottom:6}}>
                <div style={{display:"flex",justifyContent:"space-between",marginBottom:4}}><span style={{fontSize:12,fontWeight:700,color:C.text}}>{b.topic}</span><span style={{fontSize:13,fontWeight:900,color:C.warning}}>{b.score}%</span></div>
                <div style={{background:"#F1F5F9",borderRadius:3,height:4,overflow:"hidden",marginBottom:4}}><div style={{width:`${b.score}%`,height:"100%",background:C.warning,borderRadius:3}}/></div>
                <div style={{fontSize:10.5,color:C.textMid}}>{b.correct}/{b.attempted} to'g'ri</div>
              </div>
            ))}
          </div>
          <div style={{background:C.mintBg,border:`1px solid ${C.borderGreen}`,borderRadius:14,padding:"14px"}}>
            <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:11}}><Trophy size={14} color={C.primary}/><div style={{fontSize:12.5,fontWeight:800,color:C.primary}}>Kuchli tomonlaringiz ✓</div></div>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:6}}>
              {good.map(b=>(<div key={b.topic} style={{background:"#fff",borderRadius:9,padding:"9px 11px",border:`1px solid ${C.borderGreen}`}}>
                <div style={{fontSize:11.5,fontWeight:700,color:C.text,marginBottom:3}}>{b.topic}</div>
                <div style={{background:"#F1F5F9",borderRadius:3,height:4,overflow:"hidden",marginBottom:4}}><div style={{width:`${b.score}%`,height:"100%",background:C.primary,borderRadius:3}}/></div>
                <div style={{fontSize:13,fontWeight:900,color:C.primary}}>{b.score}%</div>
              </div>))}
            </div>
          </div>
        </div>
      </div>
      <div style={{background:`linear-gradient(135deg,${C.primary} 0%,${C.accent} 100%)`,borderRadius:14,padding:"18px 22px",display:"flex",alignItems:"center",gap:16}}>
        <div style={{width:46,height:46,borderRadius:11,background:"rgba(255,255,255,0.15)",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}><Zap size={21} color={C.mint}/></div>
        <div>
          <div style={{color:"#fff",fontWeight:800,fontSize:14.5,marginBottom:3}}>Tavsiya etilgan o'quv rejasi</div>
          <div style={{color:"#D1FAE5",fontSize:12.5,lineHeight:1.65}}><strong style={{color:C.mint}}>Bugun:</strong> Termokimyo (3–7–15-Variant) · Elektroliz (4–12-Variant). <strong style={{color:C.mint}}>Ertaga:</strong> Redoks reaksiyalari (2–9-Variant). Har kuni 1–2 soat shu mavzularga e'tibor bering.</div>
        </div>
      </div>
    </div>
  );
}

// ── TEST GENERATOR (with AI Adaptive) ────────────────────────────
function TestGenerator({teacher,plan,setTab}) {
  const [start,setStart]=useState(1); const [end,setEnd]=useState(4);
  const [shown,setShown]=useState(true); const [loading,setLoading]=useState(false);
  const [adaptState,setAdaptState]=useState("idle");
  const [adaptQs,setAdaptQs]=useState([]);
  const maxV=teacher?.variants||20;
  const vColors=["#0F5132","#0D9488","#7C3AED","#B45309","#0369A1","#DC2626"];
  const sel={padding:"10px 14px",borderRadius:9,border:`1.5px solid ${C.border}`,fontSize:13.5,fontFamily:"inherit",color:C.text,background:"#fff",cursor:"pointer",outline:"none",width:"100%",appearance:"none",WebkitAppearance:"none"};
  const allowed=canUse(plan,"adaptive");
  const weakTopics=ANALYTICS.filter(b=>b.status==="weak").map(b=>b.topic);

  const generateAdaptive = async () => {
    setAdaptState("loading"); setAdaptQs([]);
    try {
      const prompt = `Quyidagi kimyo mavzularidan 9 ta mashq savoli yarat: ${weakTopics.join(", ")}. O'zbek tilida. FAQAT JSON array formatda javob ber:\n[{"id":1,"mavzu":"mavzu","savol":"savol matni","qiyinlik":"oson"},...]`;
      const text = await callClaude(prompt);
      const parsed = JSON.parse(text);
      setAdaptQs(parsed); setAdaptState("done");
    } catch(e) { setAdaptState("error"); }
  };

  const qiyinlikCol={oson:"#16A34A","o'rta":C.warning,qiyin:C.danger};

  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{maxWidth:780}}>
        <div style={{marginBottom:22}}>
          <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:8}}><Wand2 size={14} color={C.accent}/><span style={{fontSize:10.5,fontWeight:700,color:C.accent,textTransform:"uppercase",letterSpacing:"0.09em"}}>Test Generator · Milliy Qolip</span></div>
          <h1 style={{fontSize:22,fontWeight:900,color:C.text,lineHeight:1.25,marginBottom:8}}>43 talik Milliy Sertifikat Qolipidagi Test Generator</h1>
          {teacher&&<div style={{display:"flex",alignItems:"center",gap:7}}><div style={{width:22,height:22,borderRadius:6,background:teacher.color,display:"flex",alignItems:"center",justifyContent:"center",fontSize:9,fontWeight:900,color:"#fff"}}>{teacher.initials}</div><span style={{fontSize:13,color:C.textMid,fontWeight:600}}>{teacher.name} · {teacher.variants} ta variantdan generatsiya</span></div>}
        </div>

        {/* AI ADAPTIVE SECTION */}
        <div style={{background:"linear-gradient(135deg,#0F172A 0%,#1a2744 100%)",borderRadius:14,padding:"20px",marginBottom:16,border:"1px solid rgba(110,231,183,0.15)"}}>
          <div style={{display:"flex",alignItems:"flex-start",gap:14,marginBottom:16}}>
            <div style={{width:44,height:44,borderRadius:11,background:"rgba(110,231,183,0.12)",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}><Sparkles size={20} color={C.mint}/></div>
            <div style={{flex:1}}>
              <div style={{color:"#fff",fontWeight:800,fontSize:14.5,marginBottom:4}}>🤖 AI Adaptive Test Generator</div>
              <div style={{color:"#94A3B8",fontSize:12.5,lineHeight:1.6}}>Sun'iy intellekt sizning <strong style={{color:"#FCA5A5"}}>zaif mavzularingiz</strong>ni aniqlab, maxsus 9 savollik test yaratadi</div>
            </div>
          </div>
          <div style={{display:"flex",gap:8,flexWrap:"wrap",marginBottom:16}}>
            <span style={{fontSize:11,color:"#94A3B8",fontWeight:600}}>Zaif mavzular aniqlandi:</span>
            {weakTopics.map(t=>(<span key={t} style={{fontSize:11,fontWeight:700,background:"rgba(220,38,38,0.15)",color:"#FCA5A5",padding:"3px 10px",borderRadius:20,border:"1px solid rgba(220,38,38,0.2)"}}>{t}</span>))}
          </div>
          {!allowed ? (
            <div style={{display:"flex",alignItems:"center",gap:12,background:"rgba(255,255,255,0.05)",borderRadius:10,padding:"14px",border:"1px solid rgba(255,255,255,0.08)"}}>
              <Lock size={16} color="#94A3B8"/>
              <div style={{flex:1}}><div style={{color:"#CBD5E1",fontSize:13,fontWeight:700}}>Bu funksiya Premium rejada mavjud</div><div style={{color:"#64748B",fontSize:11.5,marginTop:2}}>AI Adaptive Test Generator faqat Premium obunachilarga</div></div>
              <button onClick={()=>setTab("obuna")} style={{padding:"9px 16px",borderRadius:9,background:C.mint,color:C.primary,border:"none",fontSize:12.5,fontWeight:800,cursor:"pointer",fontFamily:"inherit",flexShrink:0}}>Premium olish</button>
            </div>
          ) : (
            <div>
              {adaptState==="idle"&&(
                <button onClick={generateAdaptive} style={{width:"100%",padding:"12px",borderRadius:10,background:C.mint,color:C.primary,border:"none",fontSize:14,fontWeight:800,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:8}}>
                  <Sparkles size={16}/> AI bilan 9 savollik Adaptive Test Yaratish
                </button>
              )}
              {adaptState==="loading"&&(
                <div style={{display:"flex",alignItems:"center",gap:10,padding:"14px",background:"rgba(255,255,255,0.05)",borderRadius:10}}>
                  <div style={{width:18,height:18,border:"2.5px solid rgba(110,231,183,0.3)",borderTopColor:C.mint,borderRadius:"50%",animation:"spin 0.75s linear infinite",flexShrink:0}}/>
                  <span style={{color:"#94A3B8",fontSize:13}}>Claude AI zaif mavzular uchun test yaratmoqda...</span>
                </div>
              )}
              {adaptState==="error"&&(
                <div style={{display:"flex",alignItems:"center",gap:10,padding:"12px",background:"rgba(220,38,38,0.1)",borderRadius:10,border:"1px solid rgba(220,38,38,0.2)"}}>
                  <XCircle size={15} color={C.danger}/><span style={{color:"#FCA5A5",fontSize:13,flex:1}}>Xatolik yuz berdi.</span>
                  <button onClick={generateAdaptive} style={{padding:"5px 10px",background:"rgba(220,38,38,0.2)",border:"none",borderRadius:7,color:"#FCA5A5",fontSize:11,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Qayta</button>
                </div>
              )}
              {adaptState==="done"&&adaptQs.length>0&&(
                <div>
                  <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:10}}>
                    <div style={{display:"flex",alignItems:"center",gap:6}}><Sparkles size={13} color={C.mint}/><span style={{color:C.mint,fontSize:11,fontWeight:700,textTransform:"uppercase",letterSpacing:"0.08em"}}>AI yaratgan {adaptQs.length} ta savol</span></div>
                    <button onClick={()=>{setAdaptState("idle");setAdaptQs([]);}} style={{padding:"5px 10px",background:"rgba(255,255,255,0.08)",border:"1px solid rgba(255,255,255,0.1)",borderRadius:7,color:"#94A3B8",fontSize:11,fontWeight:600,cursor:"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",gap:5}}><RefreshCw size={10}/> Yangi yaratish</button>
                  </div>
                  <div style={{display:"flex",flexDirection:"column",gap:6}}>
                    {adaptQs.map((q,i)=>{
                      const col=qiyinlikCol[q.qiyinlik]||C.primary;
                      return(
                        <div key={i} style={{background:"rgba(255,255,255,0.05)",borderRadius:10,padding:"12px 14px",border:"1px solid rgba(255,255,255,0.08)",display:"flex",gap:11,alignItems:"flex-start"}}>
                          <div style={{width:28,height:28,borderRadius:"50%",background:C.mint,color:C.primary,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:900,flexShrink:0}}>{q.id}</div>
                          <div style={{flex:1,minWidth:0}}>
                            <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:5,flexWrap:"wrap"}}>
                              <span style={{fontSize:11,fontWeight:700,color:col,background:`${col}18`,padding:"2px 9px",borderRadius:20,border:`1px solid ${col}30`}}>{q.qiyinlik}</span>
                              <span style={{fontSize:11,color:"#64748B"}}>{q.mavzu}</span>
                            </div>
                            <p style={{color:"#CBD5E1",fontSize:13,lineHeight:1.6,margin:0}}>{q.savol}</p>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* STANDARD GENERATOR */}
        <div style={{background:"#fff",borderRadius:14,padding:"20px",border:`1px solid ${C.border}`,marginBottom:14,boxShadow:"0 1px 6px rgba(0,0,0,0.05)"}}>
          <div style={{fontSize:13,fontWeight:800,color:C.text,marginBottom:13,display:"flex",alignItems:"center",gap:6}}><Settings size={13} color={C.primary}/> Standart 43 talik Test Generator</div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:14,marginBottom:14}}>
            {[["Variant boshlanishi",start,setStart],["Variant tugashi",end,setEnd]].map(([l,v,fn])=>(
              <div key={l}>
                <label style={{fontSize:11.5,fontWeight:700,color:C.textMid,display:"block",marginBottom:6}}>{l}</label>
                <div style={{position:"relative"}}>
                  <select value={v} onChange={e=>fn(Number(e.target.value))} style={sel}>{Array.from({length:maxV},(_,i)=>i+1).map(n=><option key={n} value={n}>{n}-Variant</option>)}</select>
                  <ChevronDown size={13} style={{position:"absolute",right:12,top:"50%",transform:"translateY(-50%)",pointerEvents:"none",color:C.textMid}}/>
                </div>
              </div>
            ))}
          </div>
          <div style={{background:"#EFF6FF",border:"1px solid #BFDBFE",borderRadius:10,padding:"11px 14px",marginBottom:14,display:"flex",gap:9,alignItems:"flex-start"}}>
            <Info size={13} color="#2563EB" style={{flexShrink:0,marginTop:1}}/>
            <p style={{fontSize:12,color:"#1E40AF",lineHeight:1.65,margin:0}}>Tizim <strong>{start}-variantdan {end}-variantgacha</strong> masalalarni o'zgartirmasdan, <strong>43 talik milliy sertifikat qolipiga</strong> moslab yig'ib beradi.</p>
          </div>
          <button onClick={()=>{setLoading(true);setTimeout(()=>{setLoading(false);setShown(true);},1300);}} disabled={loading}
            style={{width:"100%",padding:"12px",borderRadius:10,background:loading?C.textLight:C.primary,color:"#fff",border:"none",fontSize:14,fontWeight:800,cursor:loading?"not-allowed":"pointer",fontFamily:"inherit",display:"flex",alignItems:"center",justifyContent:"center",gap:8,boxShadow:loading?"none":"0 5px 16px rgba(15,81,50,0.3)",transition:"all 0.2s"}}>
            {loading?(<><div style={{width:16,height:16,border:"2.5px solid rgba(255,255,255,0.35)",borderTopColor:"#fff",borderRadius:"50%",animation:"spin 0.75s linear infinite"}}/> Generatsiya qilinmoqda...</>):(<><Wand2 size={15}/> 43 talik Test Yaratish ({start}–{end})</>)}
          </button>
        </div>
        {shown&&(
          <div style={{background:"#fff",borderRadius:14,padding:"18px 20px",border:`1px solid ${C.border}`}}>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:14}}>
              <div><div style={{fontSize:14,fontWeight:800,color:C.text}}>Generatsiya qilingan test</div><div style={{fontSize:12,color:C.textMid,marginTop:2}}>Variantlar: {start}–{end} · 43 ta savol</div></div>
              <div style={{display:"flex",gap:7}}>
                <button style={{display:"flex",alignItems:"center",gap:5,padding:"7px 12px",background:C.mintBg,color:C.primary,border:`1px solid ${C.borderGreen}`,borderRadius:8,fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}><Download size={11}/> PDF</button>
                <button style={{display:"flex",alignItems:"center",gap:5,padding:"7px 12px",background:C.primary,color:"#fff",border:"none",borderRadius:8,fontSize:12,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}><Play size={10} fill="currentColor"/> Boshlash</button>
              </div>
            </div>
            <div style={{display:"flex",flexDirection:"column",gap:4}}>
              {GEN_SRC.map((fV,i)=>{const col=vColors[(fV-1)%vColors.length];return(
                <div key={i} style={{display:"flex",alignItems:"center",gap:10,padding:"8px 12px",borderRadius:8,background:i%2===0?"#FAFAFA":"#fff",border:`1px solid ${C.border}`}}>
                  <div style={{width:26,height:26,borderRadius:"50%",background:C.primary,color:"#fff",display:"flex",alignItems:"center",justifyContent:"center",fontSize:10,fontWeight:900,flexShrink:0}}>{i+1}</div>
                  <div style={{flex:1,minWidth:0,fontSize:12,fontWeight:500,color:C.text,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{i+1}-savol</div>
                  <div style={{display:"inline-flex",background:`${col}14`,color:col,border:`1px solid ${col}28`,fontSize:10,fontWeight:800,padding:"3px 8px",borderRadius:20,flexShrink:0}}>Variant {fV}</div>
                </div>
              );})}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// ── SUBSCRIPTION SCREEN ───────────────────────────────────────────
function SubscriptionScreen({plan,session,setTab}) {
  const [hover,setHover]=useState(null);
  const [notice,setNotice]=useState("");
  const handleClick = p => {
    if(p.id==="free") return;
    if(!session){ setTab("profile"); return; }
    setNotice(`${p.name} rejasi uchun to'lov tizimi tez orada ulanadi. Hozircha administrator bilan bog'laning.`);
  };
  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{textAlign:"center",marginBottom:30}}>
        <div style={{display:"inline-flex",alignItems:"center",gap:7,background:C.mintBg,border:`1px solid ${C.borderGreen}`,padding:"6px 16px",borderRadius:20,marginBottom:14}}>
          <Star size={13} color={C.primary}/><span style={{fontSize:11.5,fontWeight:700,color:C.primary,textTransform:"uppercase",letterSpacing:"0.09em"}}>Obuna rejalari · 2026</span>
        </div>
        <h1 style={{fontSize:26,fontWeight:900,color:C.text,marginBottom:8}}>O'zingizga mos rejani tanlang</h1>
        <p style={{color:C.textMid,fontSize:14,maxWidth:500,margin:"0 auto"}}>Milliy sertifikat imtihoniga tayyorlanishni yangi bosqichga olib chiqing. AI vositalar va premium kontent bilan.</p>
      </div>
      {notice&&(
        <div style={{background:C.warningBg,border:`1px solid #FDE68A`,borderRadius:12,padding:"12px 16px",marginBottom:20,display:"flex",alignItems:"center",gap:10,maxWidth:640,marginLeft:"auto",marginRight:"auto"}}>
          <Info size={15} color={C.warning}/><span style={{fontSize:12.5,color:"#92400E",flex:1}}>{notice}</span>
          <button onClick={()=>setNotice("")} style={{background:"none",border:"none",cursor:"pointer",color:"#92400E"}}><X size={14}/></button>
        </div>
      )}

      <div style={{display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:18,marginBottom:30}}>
        {PLANS.map(p=>{
          const current=plan===p.id; const isHov=hover===p.id;
          return (
            <div key={p.id}
              onMouseEnter={()=>setHover(p.id)} onMouseLeave={()=>setHover(null)}
              style={{background:"#fff",borderRadius:18,border:current?`2px solid ${p.color}`:`1px solid ${C.border}`,padding:"26px 22px",transition:"all 0.2s",boxShadow:current?`0 8px 32px ${p.color}22`:(isHov?"0 8px 28px rgba(0,0,0,0.1)":"0 1px 5px rgba(0,0,0,0.05)"),transform:current||isHov?"translateY(-4px)":"translateY(0)",position:"relative",overflow:"hidden"}}>
              {p.badge&&<div style={{position:"absolute",top:0,left:0,right:0,padding:"7px",background:p.color,color:"#fff",textAlign:"center",fontSize:11.5,fontWeight:800}}>{p.badge}</div>}
              <div style={{paddingTop:p.badge?24:0}}>
                {current&&<div style={{position:"absolute",top:p.badge?42:14,right:14,display:"flex",alignItems:"center",gap:5,background:p.color,color:"#fff",fontSize:10,fontWeight:800,padding:"3px 9px",borderRadius:20}}><CheckCircle2 size={10}/> Joriy reja</div>}
                <div style={{fontSize:28,fontWeight:900,marginBottom:3,color:p.color}}>{p.name}</div>
                <div style={{display:"flex",alignItems:"baseline",gap:4,marginBottom:4}}>
                  <span style={{fontSize:p.price==="0"?24:26,fontWeight:900,color:C.text}}>{p.price==="0"?"Bepul":p.price}</span>
                  {p.price!=="0"&&<span style={{fontSize:13,color:C.textMid,fontWeight:500}}>{p.period}</span>}
                </div>
                {p.price==="0"&&<div style={{fontSize:12,color:C.textMid,marginBottom:16}}>Hech qanday to'lovsiz</div>}
                {p.price!=="0"&&<div style={{fontSize:12,color:C.textMid,marginBottom:16}}>Har oy avtomatic yangilanadi</div>}
                <div style={{marginBottom:20}}>
                  {p.features.map((f,i)=>(
                    <div key={i} style={{display:"flex",alignItems:"center",gap:9,marginBottom:9}}>
                      <div style={{width:18,height:18,borderRadius:"50%",flexShrink:0,background:f.ok?`${p.color}18`:"#F1F5F9",display:"flex",alignItems:"center",justifyContent:"center"}}>
                        {f.ok?<CheckCircle2 size={11} color={p.color}/>:<XCircle size={11} color="#CBD5E1"/>}
                      </div>
                      <span style={{fontSize:12.5,color:f.ok?C.text:C.textLight,fontWeight:f.ok?500:400}}>{f.t}</span>
                    </div>
                  ))}
                </div>
                <button onClick={()=>handleClick(p)} disabled={current} style={{width:"100%",padding:"12px",borderRadius:11,background:current?"#F1F5F9":p.btnBg,color:current?C.textMid:p.btnColor,border:current?`1px solid ${C.border}`:"none",fontSize:13.5,fontWeight:800,cursor:current?"default":"pointer",fontFamily:"inherit",transition:"all 0.15s",opacity:current?0.7:1}}>
                  {current?"Joriy rejangiz":p.price==="0"?"Bepul boshlash":!session?"Kirish va obuna bo'lish":"Obuna bo'lish"}
                </button>
              </div>
            </div>
          );
        })}
      </div>

      <div style={{background:C.mintBg,border:`1px solid ${C.borderGreen}`,borderRadius:16,padding:"22px 28px"}}>
        <div style={{fontSize:15,fontWeight:800,color:C.primary,marginBottom:16,display:"flex",alignItems:"center",gap:8}}><Award size={16}/> Ko'p so'raladigan savollar</div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:16}}>
          {[
            ["To'lov qanday amalga oshiriladi?","Payme, Uzcard, Humo va boshqa qulay usullar orqali to'lashingiz mumkin. Xavfsiz va tez."],
            ["Obunani bekor qilish mumkinmi?","Ha, istalgan vaqtda bekor qilishingiz mumkin. Hech qanday jarima yo'q."],
            ["AI funksiyalar qanday ishlaydi?","Claude AI texnologiyasi asosida ishlaydi. Har savol uchun noyob analog va adaptive test yaratadi."],
            ["Demo versiya bormi?","Bepul reja orqali platformani sinab ko'rishingiz mumkin. 3 ta variant to'liq ochiq."],
          ].map(([q,a])=>(
            <div key={q} style={{background:"#fff",borderRadius:12,padding:"14px 16px",border:`1px solid ${C.borderGreen}`}}>
              <div style={{fontSize:13,fontWeight:700,color:C.primary,marginBottom:5}}>{q}</div>
              <div style={{fontSize:12,color:C.textMid,lineHeight:1.6}}>{a}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ── PROFILE SCREEN ────────────────────────────────────────────────
function AuthPanel(){
  const [mode,setMode]=useState("login");
  const [email,setEmail]=useState("");
  const [password,setPassword]=useState("");
  const [error,setError]=useState("");
  const [info,setInfo]=useState("");
  const [loading,setLoading]=useState(false);
  const submit = async e => {
    e.preventDefault();
    setLoading(true); setError(""); setInfo("");
    if(mode==="login"){
      const { error } = await supabase.auth.signInWithPassword({ email, password });
      if(error) setError("Email yoki parol noto'g'ri");
    } else {
      const { error } = await supabase.auth.signUp({ email, password });
      if(error) setError(error.message);
      else setInfo("Ro'yxatdan o'tildi! Endi kirishingiz mumkin.");
    }
    setLoading(false);
  };
  return (
    <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:16,padding:28,maxWidth:380,width:"100%"}}>
      <div style={{display:"flex",gap:6,marginBottom:20,background:C.bgSoft,borderRadius:10,padding:4}}>
        {[["login","Kirish"],["signup","Ro'yxatdan o'tish"]].map(([m,l])=>(
          <button key={m} type="button" onClick={()=>{setMode(m);setError("");setInfo("");}} style={{flex:1,padding:"8px",borderRadius:8,border:"none",cursor:"pointer",fontFamily:"inherit",fontSize:12.5,fontWeight:700,background:mode===m?"#fff":"transparent",color:mode===m?C.primary:C.textMid,boxShadow:mode===m?"0 1px 3px rgba(0,0,0,0.08)":"none"}}>{l}</button>
        ))}
      </div>
      <form onSubmit={submit}>
        <label style={{fontSize:11.5,fontWeight:700,color:C.textMid,marginBottom:5,display:"block"}}>Email</label>
        <input type="email" required value={email} onChange={e=>setEmail(e.target.value)} style={{width:"100%",padding:"10px 12px",borderRadius:9,border:`1px solid ${C.border}`,fontSize:13,fontFamily:"inherit",marginBottom:12}}/>
        <label style={{fontSize:11.5,fontWeight:700,color:C.textMid,marginBottom:5,display:"block"}}>Parol</label>
        <input type="password" required minLength={6} value={password} onChange={e=>setPassword(e.target.value)} style={{width:"100%",padding:"10px 12px",borderRadius:9,border:`1px solid ${C.border}`,fontSize:13,fontFamily:"inherit",marginBottom:14}}/>
        {error&&<div style={{color:C.danger,fontSize:12,marginBottom:12}}>{error}</div>}
        {info&&<div style={{color:C.primary,fontSize:12,marginBottom:12}}>{info}</div>}
        <button type="submit" disabled={loading} style={{width:"100%",padding:"11px",borderRadius:9,background:C.primary,color:"#fff",border:"none",fontSize:13,fontWeight:800,cursor:"pointer",fontFamily:"inherit"}}>
          {loading?"Yuklanmoqda...":mode==="login"?"Kirish":"Ro'yxatdan o'tish"}
        </button>
      </form>
    </div>
  );
}

function ProfileScreen({teacher,plan,session,setTab,variants}) {
  const vList=teacher?variants:[];
  const done=vList.filter(v=>v.total>0&&v.ready===v.total).length;
  const total=vList.reduce((s,v)=>s+v.ready,0);
  const allQ=vList.reduce((s,v)=>s+v.total,0);
  const maxV=vList.length||1;
  const planInfo={free:{name:"Bepul",color:"#475569",bg:"#F1F5F9"},standart:{name:"Standart",color:C.accent,bg:"#F0FDFA"},premium:{name:"Premium",color:C.primary,bg:C.mintBg}};
  const pi=planInfo[plan];

  if(!session) return (
    <div style={{padding:"26px 30px",display:"flex",flexDirection:"column",alignItems:"center",gap:20}}>
      <div style={{textAlign:"center",maxWidth:400}}>
        <div style={{fontSize:40,marginBottom:10}}>👤</div>
        <h1 style={{fontSize:20,fontWeight:900,color:C.text,marginBottom:6}}>Hisobingizga kiring</h1>
        <p style={{fontSize:13,color:C.textMid}}>Progressingizni saqlash va obuna bo'lish uchun ro'yxatdan o'ting yoki kiring.</p>
      </div>
      <AuthPanel/>
    </div>
  );

  return (
    <div style={{padding:"26px 30px"}}>
      <div style={{maxWidth:640}}>
        <div style={{background:`linear-gradient(130deg,${C.primary} 0%,${C.accent} 100%)`,borderRadius:16,padding:"24px",marginBottom:20,color:"#fff",display:"flex",gap:18,alignItems:"center"}}>
          <div style={{width:70,height:70,borderRadius:"50%",background:"rgba(255,255,255,0.18)",display:"flex",alignItems:"center",justifyContent:"center",fontSize:30,flexShrink:0}}>👨‍🎓</div>
          <div style={{flex:1,minWidth:0}}>
            <div style={{fontSize:10,color:C.mint,fontWeight:800,marginBottom:4,textTransform:"uppercase",letterSpacing:"0.09em"}}>Kimyo Platform · 2026</div>
            <div style={{fontSize:16,fontWeight:900,marginBottom:3,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis"}}>{session.user.email}</div>
            <div style={{fontSize:12.5,color:"#D1FAE5"}}>{teacher?`${teacher.name} kursi`:"O'qituvchi tanlanmagan"}</div>
            <div style={{display:"inline-flex",alignItems:"center",gap:5,marginTop:6,background:"rgba(255,255,255,0.15)",padding:"4px 12px",borderRadius:20}}>
              <div style={{width:7,height:7,borderRadius:"50%",background:pi.color==="#475569"?"#CBD5E1":C.mint}}/>
              <span style={{fontSize:11,fontWeight:700}}>{pi.name} reja</span>
            </div>
          </div>
          <button onClick={()=>supabase.auth.signOut()} style={{background:"rgba(255,255,255,0.14)",border:"none",color:"#fff",padding:"8px 14px",borderRadius:9,fontSize:11.5,fontWeight:700,cursor:"pointer",fontFamily:"inherit",flexShrink:0}}>Chiqish</button>
        </div>
        <div style={{display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:12,marginBottom:18}}>
          {[{icon:"✅",val:`${done}/${maxV}`,label:"Bajarilgan"},{icon:"🎬",val:total,label:"Video tayyor"},{icon:"🏆",val:`${allQ?Math.round((total/allQ)*100):0}%`,label:"Umumiy Progress"}].map(s=>(
            <div key={s.label} style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:12,padding:"15px",textAlign:"center",boxShadow:"0 1px 4px rgba(0,0,0,0.04)"}}>
              <div style={{fontSize:24,marginBottom:6}}>{s.icon}</div>
              <div style={{fontSize:20,fontWeight:900,color:C.primary,marginBottom:3}}>{s.val}</div>
              <div style={{fontSize:10.5,color:C.textMid}}>{s.label}</div>
            </div>
          ))}
        </div>
        <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:"16px 18px",marginBottom:14}}>
          <div style={{fontSize:13,fontWeight:800,color:C.text,marginBottom:4}}>Obuna holati</div>
          <div style={{display:"flex",alignItems:"center",gap:12}}>
            <div style={{flex:1,background:pi.bg,borderRadius:10,padding:"12px 14px",border:`1px solid ${pi.color}30`}}>
              <div style={{fontSize:15,fontWeight:900,color:pi.color,marginBottom:2}}>{pi.name} reja</div>
              <div style={{fontSize:11.5,color:C.textMid}}>{plan==="free"?"Bepul · Cheklangan imkoniyatlar":plan==="standart"?"49,900 so'm/oy · AI Analog Generator":"99,900 so'm/oy · Barcha imkoniyatlar"}</div>
            </div>
            {plan!=="premium"&&<button onClick={()=>setTab("obuna")} style={{padding:"10px 16px",borderRadius:10,background:C.primary,color:"#fff",border:"none",fontSize:12.5,fontWeight:700,cursor:"pointer",fontFamily:"inherit",flexShrink:0}}>⬆️ Yangilash</button>}
          </div>
        </div>
        {teacher&&(
          <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:14,padding:"16px 18px"}}>
            <div style={{fontSize:13,fontWeight:800,color:C.text,marginBottom:13}}>Variant Progressi</div>
            {vList.map(v=>{const pct=v.total?Math.round((v.ready/v.total)*100):0;return(
              <div key={v.id} style={{display:"flex",alignItems:"center",gap:11,marginBottom:8}}>
                <div style={{width:72,fontSize:11,fontWeight:700,color:C.text,flexShrink:0}}>{v.number}-Variant</div>
                <div style={{flex:1,height:6,background:"#F1F5F9",borderRadius:3,overflow:"hidden"}}><div style={{width:`${pct}%`,height:"100%",borderRadius:3,background:pct===100?C.primary:C.accent}}/></div>
                <div style={{width:34,fontSize:11,fontWeight:800,color:pct===100?C.primary:C.textMid,textAlign:"right",flexShrink:0}}>{pct}%</div>
              </div>
            );})}
          </div>
        )}
      </div>
    </div>
  );
}

// ── APP ───────────────────────────────────────────────────────────
export default function App() {
  const [tab,setTab]=useState("collections");
  const [teacher,setTeacher]=useState(null);
  const [varId,setVarId]=useState(null);
  const [mobileOpen,setMobileOpen]=useState(false);
  const [teachers,setTeachers]=useState([]);
  const [variants,setVariants]=useState([]);
  const [questions,setQuestions]=useState([]);
  const [teacherQuestions,setTeacherQuestions]=useState([]);
  const [session,setSession]=useState(undefined);
  const [profile,setProfile]=useState(null);
  const plan = profile?.plan || "free";

  const reloadTeachers = () => fetchTeachers().then(setTeachers);
  useEffect(()=>{ reloadTeachers(); },[]);

  useEffect(()=>{
    supabase.auth.getSession().then(({data})=>setSession(data.session));
    const { data:sub } = supabase.auth.onAuthStateChange((_e,s)=>setSession(s));
    return ()=>sub.subscription.unsubscribe();
  },[]);

  useEffect(()=>{
    if(!session){ setProfile(null); return; }
    supabase.from("profiles").select("*").eq("id",session.user.id).single().then(({data})=>setProfile(data));
  },[session]);

  useEffect(()=>{
    if(!teacher){ setVariants([]); setTeacherQuestions([]); return; }
    fetchVariants(teacher.id).then(setVariants);
    supabase.from("questions").select("*, variants!inner(variant_number,teacher_id)").eq("variants.teacher_id",teacher.id).order("question_number")
      .then(({data})=>setTeacherQuestions((data||[]).map(q=>({...q,variant_number:q.variants.variant_number}))));
  },[teacher]);

  useEffect(()=>{
    if(!teacher||!varId){ setQuestions([]); return; }
    const v = variants.find(x=>x.number===varId);
    if(!v){ setQuestions([]); return; }
    fetchQuestions(v.id).then(setQuestions);
  },[teacher,varId,variants]);

  const pick=t=>{setTeacher(t);setTab("variants");setVarId(null);setMobileOpen(false);};
  return (
    <div style={{display:"flex",minHeight:"100vh",background:C.bgSoft,fontFamily:"'Inter',system-ui,-apple-system,sans-serif"}}>
      <style>{`@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');*{box-sizing:border-box;margin:0;padding:0;}html,body,#root{overflow-x:hidden;}::-webkit-scrollbar{width:5px;}::-webkit-scrollbar-track{background:#F1F5F9;}::-webkit-scrollbar-thumb{background:#CBD5E1;border-radius:3px;}@keyframes spin{to{transform:rotate(360deg);}}button:focus-visible{outline:2px solid #0F5132;outline-offset:2px;}
        .hamburger-btn{display:none;position:fixed;top:14px;left:14px;z-index:300;width:40px;height:40px;border-radius:10px;background:${C.primary};border:none;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,0.18);}
        .sidebar-overlay{display:none;position:fixed;inset:0;background:rgba(15,23,42,0.45);z-index:150;}
        @media (max-width:900px){
          .app-sidebar{transform:translateX(-100%);transition:transform 0.25s ease;}
          .app-sidebar.open{transform:translateX(0);}
          .app-main{margin-left:0 !important;padding-top:58px;}
          .hamburger-btn{display:flex;}
          .sidebar-close-btn{display:flex !important;}
          .sidebar-overlay{display:block;}
          .video-layout{flex-direction:column !important;height:auto !important;overflow:visible !important;}
          .video-sidebar{width:100% !important;border-left:none !important;border-top:1px solid ${C.border};max-height:none !important;}
          [style*="grid-template-columns"]{grid-template-columns:1fr !important;}
        }
        @media (max-width:640px){
          .stat-row{flex-wrap:wrap;}
          .stat-row>div{min-width:calc(50% - 6px);}
        }`}</style>
      <button className="hamburger-btn" onClick={()=>setMobileOpen(true)} aria-label="Menyu">
        <Menu size={19} color="#fff"/>
      </button>
      {mobileOpen&&<div className="sidebar-overlay" onClick={()=>setMobileOpen(false)}/>}
      <Sidebar tab={tab} setTab={setTab} teacher={teacher} setTeacher={setTeacher} setVarId={setVarId} plan={plan} mobileOpen={mobileOpen} onClose={()=>setMobileOpen(false)} variants={variants}/>
      <main className="app-main" style={{marginLeft:258,flex:1,minHeight:"100vh",overflowY:"auto",display:"flex",flexDirection:"column",minWidth:0}}>
        {tab==="collections"&&<TeachersGrid onSelect={pick} plan={plan} teachers={teachers}/>}
        {tab==="variants"&&!teacher&&(
          <div style={{display:"flex",alignItems:"center",justifyContent:"center",flex:1,flexDirection:"column",gap:14,padding:40}}>
            <div style={{fontSize:48}}>👨‍🏫</div><div style={{fontSize:20,fontWeight:800,color:C.text}}>O'qituvchi tanlanmagan</div>
            <div style={{fontSize:14,color:C.textMid}}>Variantlarni ko'rish uchun avval o'qituvchini tanlang</div>
            <button onClick={()=>setTab("collections")} style={{padding:"12px 28px",borderRadius:10,background:C.primary,color:"#fff",border:"none",fontSize:14,fontWeight:700,cursor:"pointer",fontFamily:"inherit"}}>Kolleksiyalarni ko'rish</button>
          </div>
        )}
        {tab==="variants"&&teacher&&!varId&&<VariantsGrid teacher={teacher} onOpen={id=>setVarId(id)} variants={variants}/>}
        {tab==="variants"&&teacher&&varId&&<VideoPlayer variantId={varId} teacher={teacher} onBack={()=>setVarId(null)} plan={plan} setTab={setTab} questions={questions}/>}
        {tab==="topics"&&<TopicsDirectory onGoVariant={id=>{setVarId(id);setTab("variants");}} teacher={teacher} setTab={setTab} questions={teacherQuestions}/>}
        {tab==="analytics"&&<AnalyticsScreen/>}
        {tab==="generator"&&<TestGenerator teacher={teacher} plan={plan} setTab={setTab}/>}
        {tab==="obuna"&&<SubscriptionScreen plan={plan} session={session} setTab={setTab}/>}
        {tab==="profile"&&<ProfileScreen teacher={teacher} plan={plan} session={session} setTab={setTab} variants={variants}/>}
      </main>
    </div>
  );
}
