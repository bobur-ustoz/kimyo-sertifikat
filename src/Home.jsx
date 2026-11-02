import { useState, useEffect } from "react";
import { ArrowRight, Atom, FileText, Sparkles, Clock, Flame } from "lucide-react";
import { supabase } from "./lib/supabaseClient";

// Home page, laid out like a course catalogue: a rotating banner, then three panels of cards.
// One blue for everything clickable; green / amber / grey only carry a status meaning.
const B = { blue:"#0056D2", blueDark:"#0048B0", navy:"#002457", tint:"#F0F6FF", panel:"#E3EEFF", line:"#DAE1ED", text:"#0D0F12", mid:"#48546E",
  ok:"#15803D", okBg:"#DCFCE7", pro:"#B45309", proBg:"#FFF4E8", soon:"#64748B" };

const btn = (solid) => ({ display:"inline-flex", alignItems:"center", gap:7, padding:"10px 18px", borderRadius:8, fontSize:14, fontWeight:700, cursor:"pointer", fontFamily:"inherit",
  border:solid?"none":`1px solid ${B.blue}`, background:solid?B.blue:"#fff", color:solid?"#fff":B.blue });

function Card({ icon, tile, label, title, note, noteColor, onClick, dim }) {
  return (
    <div onClick={dim ? undefined : onClick} style={{ background:"#fff", borderRadius:10, padding:10, display:"flex", gap:12, alignItems:"center", marginBottom:8,
      cursor:dim?"default":"pointer", opacity:dim?0.7:1, border:`1px solid ${B.line}` }}>
      <div style={{ width:52, height:52, borderRadius:10, background:tile, color:"#fff", display:"flex", alignItems:"center", justifyContent:"center", fontSize:14, fontWeight:800, flexShrink:0 }}>{icon}</div>
      <div style={{ minWidth:0 }}>
        <div style={{ fontSize:12, color:B.mid }}>{label}</div>
        <div style={{ fontSize:14, fontWeight:700, color:B.text, lineHeight:1.3 }}>{title}</div>
        <div style={{ fontSize:12, fontWeight:600, color:noteColor }}>{note}</div>
      </div>
    </div>
  );
}

function Panel({ title, tint = B.panel, color = B.blue, onMore, children }) {
  return (
    <div style={{ background:tint, borderRadius:14, padding:12 }}>
      <div onClick={onMore} style={{ fontSize:15, fontWeight:700, color, padding:"2px 4px 10px", cursor:onMore?"pointer":"default", display:"flex", alignItems:"center", gap:6 }}>{title}{onMore && <ArrowRight size={15}/>}</div>
      {children}
    </div>
  );
}

export default function Home({ teachers, setTab, pick, plan }) {
  const dtm = teachers.find(t => t.section === "dtm");
  const videos = teachers.reduce((n, t) => n + (t.videoCount || 0), 0);
  const [slide, setSlide] = useState(0);
  const [topics, setTopics] = useState([]);

  useEffect(() => { const t = setInterval(() => setSlide(s => (s + 1) % 3), 7000); return () => clearInterval(t); }, []);
  useEffect(() => {
    (async () => {
      const [{ data: tp }, { data: ex }] = await Promise.all([
        supabase.from("topics").select("id,name,bunny_video_id").order("sort_order").order("created_at").limit(6),
        supabase.from("topic_examples").select("topic_id").not("bunny_video_id", "is", null).limit(2000),
      ]);
      const has = new Set((ex || []).map(r => r.topic_id));
      setTopics((tp || []).map(t => ({ ...t, soon: !t.bunny_video_id && !has.has(t.id) })));
    })();
  }, []);

  const openDtm = () => (dtm ? pick(dtm) : setTab("dtm"));
  const slides = [
    { kicker:"DTM · KIMYO", title:"Masalalarning videoli yechimini ustozdan o'rganing",
      text:`${videos || 60} dan ortiq savol tahlili va AI yordamchi. Har yilning birinchi variantidan 10 savol bepul.`, cta:"Bepul boshlash", go:openDtm, photo:true },
    { kicker:"YANGI", title:"2019 yil · 2-variant qo'shildi",
      text:"30 savoldan 29 tasi ustozning videoli tahlili bilan. Premium bilan to'liq ochiladi.", cta:"Variantlarni ko'rish", go:openDtm },
    { kicker:"MAVZULAR", title:"Mavzu darsi hamma uchun ochiq",
      text:"Kimyoning asosiy tushunchalari: nazariy dars bepul, 20 ta misol tahlili Premiumda.", cta:"Mavzularga o'tish", go:() => setTab("topics") },
  ];
  const s = slides[slide];

  return (
    <div style={{ padding:"22px clamp(14px,3vw,32px) 40px", background:"#fff", minHeight:"100%", color:B.text }}>
      <div style={{ display:"flex", flexWrap:"wrap", gap:14 }}>
        <div style={{ flex:"2 1 440px", minWidth:0, background:B.navy, borderRadius:16, color:"#fff", position:"relative", overflow:"hidden", minHeight:250, display:"flex" }}>
          <div style={{ padding:"30px 28px", flex:"1 1 55%", zIndex:2, minWidth:0 }}>
            <div style={{ fontSize:12, color:"#8FB4FF", letterSpacing:"0.06em", fontWeight:700 }}>{s.kicker}</div>
            <div style={{ fontSize:"clamp(22px,3.2vw,32px)", lineHeight:1.2, fontWeight:800, margin:"8px 0 10px" }}>{s.title}</div>
            <div style={{ fontSize:14, color:"#C7D8F5", lineHeight:1.55, maxWidth:420 }}>{s.text}</div>
            <button onClick={s.go} style={{ ...btn(false), background:"#fff", color:B.blue, border:"none", marginTop:18 }}>{s.cta} <ArrowRight size={15}/></button>
          </div>
          <div style={{ flex:"1 1 45%", position:"relative", minWidth:0 }}>
            {s.photo
              ? <img src="/ustoz.jpg" alt="Kimyo o'qituvchisi" style={{ position:"absolute", inset:0, width:"100%", height:"100%", objectFit:"cover", objectPosition:"56% 22%", maskImage:"linear-gradient(to right,transparent 0,#000 38%)", WebkitMaskImage:"linear-gradient(to right,transparent 0,#000 38%)" }}/>
              : <>
                  <div style={{ position:"absolute", right:-40, top:-40, width:240, height:240, borderRadius:"50%", background:"#7C5CFF" }}/>
                  <div style={{ position:"absolute", right:60, bottom:-50, width:150, height:150, borderRadius:"50%", background:"#FFB020" }}/>
                  <div style={{ position:"absolute", right:18, bottom:50, width:70, height:70, borderRadius:"50%", background:"#22C55E" }}/>
                </>}
          </div>
          <div style={{ position:"absolute", left:28, bottom:14, display:"flex", gap:6, zIndex:3 }}>
            {slides.map((_, i) => <span key={i} onClick={() => setSlide(i)} style={{ width:i===slide?24:7, height:7, borderRadius:5, background:i===slide?"#fff":"rgba(255,255,255,0.4)", cursor:"pointer", transition:"width .2s" }}/>)}
          </div>
        </div>
        <div style={{ flex:"1 1 260px", background:B.proBg, borderRadius:16, padding:22, minWidth:0 }}>
          <div style={{ fontSize:12, color:"#C2410C", fontWeight:700, letterSpacing:"0.05em" }}>PREMIUM</div>
          <div style={{ fontSize:20, lineHeight:1.25, fontWeight:800, margin:"6px 0 8px" }}>Hamma variant, AI va tahlil bitta obunada</div>
          <div style={{ fontSize:13, color:"#7A4A2A", marginBottom:14 }}><span style={{ textDecoration:"line-through" }}>250 000</span> <b style={{ fontSize:18, color:B.text }}>200 000</b> so'm / 30 kun</div>
          <button onClick={() => setTab("obuna")} style={btn(true)}>{plan === "free" ? "Premium olish" : "Obunani ko'rish"}</button>
        </div>
      </div>

      <div style={{ fontSize:20, fontWeight:800, margin:"26px 0 12px" }}>Yangi va mashhur</div>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(260px,1fr))", gap:14 }}>
        <Panel title="Eng ko'p ko'rilgan" onMore={openDtm}>
          <Card tile="#16A34A" icon="2019" label="DTM · Variant" title="1-variant tahlili" note="10 savol bepul" noteColor={B.ok} onClick={openDtm}/>
          <Card tile="#0891B2" icon={<Atom size={24}/>} label="Mavzu darsi" title="Kimyoning asosiy tushunchalari" note="Bepul" noteColor={B.ok} onClick={() => setTab("topics")}/>
          <Card tile="#7C5CFF" icon={<Sparkles size={24}/>} label="AI yordamchi" title="Videodan savol bering" note="Savolga javob oling" noteColor={B.ok} onClick={openDtm}/>
        </Panel>
        <Panel title="Yangi qo'shilganlar" tint="#F1EBFF" color="#5B3FD6" onMore={openDtm}>
          <Card tile="#16A34A" icon="V2" label="2019 yil" title="2-variant, 29 video" note="Premium" noteColor={B.pro} onClick={openDtm}/>
          <Card tile="#0891B2" icon="20" label="Mavzu misollari" title="20 ta misol tahlili" note="Premium" noteColor={B.pro} onClick={() => setTab("topics")}/>
          <Card tile="#F59E0B" icon={<FileText size={24}/>} label="Test Generator" title="Kitob ko'rinishida PDF test" note="Bepul sinab ko'ring" noteColor={B.ok} onClick={() => setTab("generator")}/>
        </Panel>
        <Panel title="Mavzular" tint="#E6F7F1" color="#0F766E" onMore={() => setTab("topics")}>
          {topics.length === 0 && <div style={{ fontSize:13, color:B.mid, padding:8 }}>Yuklanmoqda…</div>}
          {topics.slice(0, 3).map(t => (
            <Card key={t.id} dim={t.soon} tile={t.soon ? "#94A3B8" : "#0891B2"} icon={t.soon ? <Clock size={24}/> : <Atom size={24}/>} label="Mavzu" title={t.name}
              note={t.soon ? "Tez orada" : t.bunny_video_id ? "Dars ochiq" : "Misollar tayyor"} noteColor={t.soon ? B.pro : B.ok} onClick={() => setTab("topics")}/>
          ))}
        </Panel>
      </div>

      <div style={{ display:"flex", gap:12, alignItems:"center", background:B.tint, border:`1px solid ${B.line}`, borderRadius:14, padding:"14px 18px", marginTop:22, flexWrap:"wrap" }}>
        <Flame size={22} color={B.blue}/>
        <div style={{ flex:1, minWidth:220 }}>
          <div style={{ fontSize:15, fontWeight:800 }}>Pul to'lamasdan sinab ko'ring</div>
          <div style={{ fontSize:13, color:B.mid }}>Har yilning 1-variantidan dastlabki 10 savol va mavzu darslari bepul. Yoqsa, Premiumga o'tasiz.</div>
        </div>
        <button onClick={openDtm} style={btn(true)}>Boshlash</button>
      </div>
    </div>
  );
}
