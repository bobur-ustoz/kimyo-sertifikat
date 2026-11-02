import { useState, useEffect } from "react";
import { ArrowRight, Atom, FileText, Sparkles, Clock, Flame, ShieldCheck, Send, CalendarCheck, Smartphone, PlayCircle, PencilLine, Repeat, CheckCircle2, BadgeCheck, X } from "lucide-react";
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

const pubUrl = (path) => path ? supabase.storage.from("testimonials").getPublicUrl(path).data.publicUrl : null;
const ytId = (u) => { const m = String(u || "").match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([\w-]{11})/); return m ? m[1] : null; };

// The teacher's students who got the certificate. A card appears only when the admin published it;
// with none published the whole block stays hidden.
function Testimonials({ items }) {
  const [open, setOpen] = useState(null);   // { kind: "video"|"image", src }
  if (!items.length) return null;
  return (
    <div id="natijalar" style={{ marginTop:30, scrollMarginTop:16 }}>
      <div style={{ fontSize:20, fontWeight:800, marginBottom:4 }}>Ustozning o'quvchilari natijalari</div>
      <div style={{ fontSize:14, color:B.mid, marginBottom:14 }}>Milliy sertifikat olgan o'quvchilar o'z so'zlari bilan.</div>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(270px,1fr))", gap:14 }}>
        {items.map(t => {
          const vid = ytId(t.video_url);
          return (
            <div key={t.id} style={{ border:`1px solid ${B.line}`, borderRadius:16, overflow:"hidden", background:"#fff", display:"flex", flexDirection:"column" }}>
              {t.video_url && (
                <div onClick={() => vid ? setOpen({ kind:"video", src:`https://www.youtube.com/embed/${vid}?autoplay=1` }) : window.open(t.video_url, "_blank", "noopener")}
                  style={{ position:"relative", paddingTop:"56.25%", background:B.navy, cursor:"pointer" }}>
                  {vid && <img src={`https://img.youtube.com/vi/${vid}/hqdefault.jpg`} alt="" style={{ position:"absolute", inset:0, width:"100%", height:"100%", objectFit:"cover" }}/>}
                  <div style={{ position:"absolute", inset:0, display:"flex", alignItems:"center", justifyContent:"center" }}>
                    <div style={{ width:56, height:56, borderRadius:"50%", background:"rgba(255,255,255,0.95)", display:"flex", alignItems:"center", justifyContent:"center" }}><PlayCircle size={32} color={B.blue}/></div>
                  </div>
                </div>
              )}
              <div style={{ padding:16, display:"flex", flexDirection:"column", gap:10, flex:1 }}>
                <div style={{ display:"flex", gap:12, alignItems:"center" }}>
                  {t.photo_path ? <img src={pubUrl(t.photo_path)} alt={t.name} style={{ width:48, height:48, borderRadius:"50%", objectFit:"cover", flexShrink:0 }}/>
                    : <div style={{ width:48, height:48, borderRadius:"50%", background:B.panel, color:B.blue, display:"flex", alignItems:"center", justifyContent:"center", fontWeight:800, flexShrink:0 }}>{t.name.slice(0,1)}</div>}
                  <div style={{ minWidth:0 }}>
                    <div style={{ fontSize:15, fontWeight:800 }}>{t.name}</div>
                    {t.result && <div style={{ fontSize:13, color:B.ok, fontWeight:700 }}>{t.result}</div>}
                  </div>
                </div>
                {t.quote && <div style={{ fontSize:14, color:B.text, lineHeight:1.6 }}>«{t.quote}»</div>}
                <div style={{ display:"flex", gap:8, flexWrap:"wrap", marginTop:"auto" }}>
                  {t.proof_path && <button onClick={() => setOpen({ kind:"image", src:pubUrl(t.proof_path) })} style={{ ...btn(false), padding:"6px 12px", fontSize:12.5 }}>Isbotni ko'rish</button>}
                  {t.verified && <span style={{ display:"inline-flex", alignItems:"center", gap:5, background:B.okBg, color:B.ok, fontSize:12.5, fontWeight:700, padding:"6px 10px", borderRadius:999 }}><BadgeCheck size={14}/> Sertifikat ko'rilgan</span>}
                </div>
              </div>
            </div>
          );
        })}
      </div>
      {open && (
        <div onClick={() => setOpen(null)} style={{ position:"fixed", inset:0, background:"rgba(0,20,50,0.78)", zIndex:500, display:"flex", alignItems:"center", justifyContent:"center", padding:16 }}>
          <div onClick={e => e.stopPropagation()} style={{ width:"min(900px,100%)", position:"relative" }}>
            <button onClick={() => setOpen(null)} aria-label="Yopish" style={{ position:"absolute", right:0, top:-42, background:"#fff", border:"none", borderRadius:999, width:34, height:34, cursor:"pointer", display:"flex", alignItems:"center", justifyContent:"center" }}><X size={18}/></button>
            {open.kind === "video"
              ? <div style={{ position:"relative", paddingTop:"56.25%" }}><iframe src={open.src} title="Video fikr" allow="autoplay; encrypted-media; picture-in-picture" allowFullScreen style={{ position:"absolute", inset:0, width:"100%", height:"100%", border:"none", borderRadius:12 }}/></div>
              : <img src={open.src} alt="Isbot" style={{ width:"100%", maxHeight:"85vh", objectFit:"contain", borderRadius:12, background:"#fff" }}/>}
          </div>
        </div>
      )}
    </div>
  );
}

export default function Home({ teachers, setTab, pick, plan, session }) {
  const dtm = teachers.find(t => t.section === "dtm");
  const videos = teachers.reduce((n, t) => n + (t.videoCount || 0), 0);
  const [slide, setSlide] = useState(0);
  const [topics, setTopics] = useState([]);
  const [testimonials, setTestimonials] = useState([]);

  useEffect(() => {
    supabase.from("testimonials").select("*").eq("published", true).order("sort_order").then(({ data }) => setTestimonials(data || []), () => {});
  }, []);
  const featured = testimonials.filter(t => t.featured).slice(0, 2);
  const nSlides = 3 + (featured.length ? 1 : 0);
  useEffect(() => { const t = setInterval(() => setSlide(s => (s + 1) % nSlides), 7000); return () => clearInterval(t); }, [nSlides]);
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
    { kicker:"YANGI", title:"2019 yil · 2\u2011variant qo'shildi",
      text:"30 savoldan 29 tasi ustozning videoli tahlili bilan. Premium bilan to'liq ochiladi.", cta:"Variantlarni ko'rish", go:openDtm },
    { kicker:"MAVZULAR", title:"Mavzu darsi hamma uchun ochiq",
      text:"Kimyoning asosiy tushunchalari: nazariy dars bepul, 20 ta misol tahlili Premiumda.", cta:"Mavzularga o'tish", go:() => setTab("topics") },
    ...(featured.length ? [{ kicker:"NATIJALAR", title:"Ustozning ~100 o'quvchisi Milliy sertifikat olgan",
      text:"O'quvchilarning natijalari va fikrlarini o'zlari aytgan so'zlar bilan ko'ring.", cta:"Natijalarni ko'rish",
      go:() => document.getElementById("natijalar")?.scrollIntoView({ behavior:"smooth", block:"start" }), students:featured }] : []),
  ];
  const s = slides[slide % slides.length];

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
            {s.students
              ? <div style={{ position:"absolute", inset:0, display:"flex", flexDirection:"column", justifyContent:"center", gap:10, padding:"20px 22px 20px 6px" }}>
                  {s.students.map(t => (
                    <div key={t.id} style={{ background:"rgba(255,255,255,0.97)", color:B.text, borderRadius:14, padding:"10px 12px", display:"flex", gap:10, alignItems:"center" }}>
                      {t.photo_path ? <img src={pubUrl(t.photo_path)} alt={t.name} style={{ width:44, height:44, borderRadius:"50%", objectFit:"cover", flexShrink:0 }}/>
                        : <div style={{ width:44, height:44, borderRadius:"50%", background:B.panel, color:B.blue, display:"flex", alignItems:"center", justifyContent:"center", fontWeight:800, flexShrink:0 }}>{t.name.slice(0,1)}</div>}
                      <div style={{ minWidth:0 }}>
                        <div style={{ fontSize:14, fontWeight:800, lineHeight:1.2 }}>{t.name}</div>
                        {t.result && <div style={{ fontSize:12, color:B.ok, fontWeight:700, lineHeight:1.3 }}>{t.result}</div>}
                      </div>
                    </div>
                  ))}
                </div>
            : s.photo
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
          <div style={{ display:"flex", gap:8, flexWrap:"wrap" }}><button onClick={() => setTab("obuna")} style={btn(true)}>{plan === "free" ? "Premium olish" : "Obunani ko'rish"}</button>{!session && <button onClick={() => setTab("profile")} style={btn(false)}>Kirish</button>}</div>
        </div>
      </div>

      <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(150px,1fr))", border:`1px solid ${B.line}`, borderRadius:14, marginTop:18, overflow:"hidden" }}>
        {[[`${videos || 60}+`, "savolning video tahlili"], ["10 yil", "ustozning o'qitish tajribasi"], ["~100", "ustozning o'quvchisi Milliy sertifikat olgan"], ["10", "savol butunlay bepul"]].map(([n, l], i) => (
          <div key={l} style={{ padding:"14px 18px", borderLeft:i ? `1px solid ${B.line}` : "none" }}>
            <div style={{ fontSize:24, fontWeight:800, color:B.blue }}>{n}</div>
            <div style={{ fontSize:12.5, color:B.mid }}>{l}</div>
          </div>
        ))}
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

      <div style={{ background:B.tint, border:`1px solid ${B.line}`, borderRadius:16, padding:"22px clamp(16px,3vw,26px)", marginTop:26 }}>
        <div style={{ display:"flex", gap:20, alignItems:"center", flexWrap:"wrap" }}>
          <img src="/ustoz.jpg" alt="Bobur Jumanazarov" style={{ width:112, height:112, borderRadius:"50%", objectFit:"cover", objectPosition:"56% 20%", border:"3px solid #fff", boxShadow:"0 0 0 1px "+B.line, flexShrink:0 }}/>
          <div style={{ flex:1, minWidth:240 }}>
            <div style={{ fontSize:12, color:B.blue, fontWeight:700, letterSpacing:"0.05em" }}>SIZNING USTOZINGIZ</div>
            <div style={{ fontSize:24, fontWeight:800, margin:"2px 0 4px" }}>Bobur Jumanazarov</div>
            <div style={{ fontSize:15, color:B.mid, lineHeight:1.55 }}>Kimyo fani o'qituvchisi. 10 yildan beri o'quvchilarni imtihonga tayyorlaydi.</div>
          </div>
        </div>
        <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(130px,1fr))", gap:10, marginTop:18 }}>
          {[["10 yil", "o'qitish tajribasi"], ["~100", "ustozning o'quvchisi Milliy sertifikat olgan"]].map(([n, l]) => (
            <div key={l} style={{ background:"#fff", border:`1px solid ${B.line}`, borderRadius:12, padding:"12px 14px" }}>
              <div style={{ fontSize:26, fontWeight:800, color:B.blue, lineHeight:1.1 }}>{n}</div>
              <div style={{ fontSize:13, color:B.mid, marginTop:3, lineHeight:1.4 }}>{l}</div>
            </div>
          ))}
        </div>
        <div style={{ display:"grid", gap:9, marginTop:16 }}>
          {["Har bir masalani o'zi yechib, qadamma-qadam tushuntiradi.", "Eng qiyin misollar o'quvchilar so'rovi asosida qayta tahlil qilinadi.", "Tushunmagan joyingizni AI yordamchidan so'rashingiz mumkin."].map(t => (
            <div key={t} style={{ display:"flex", gap:10, alignItems:"flex-start", fontSize:14.5, color:B.text, lineHeight:1.5 }}>
              <CheckCircle2 size={19} color={B.ok} style={{ flexShrink:0, marginTop:1 }}/>{t}
            </div>
          ))}
        </div>
      </div>

      <Testimonials items={testimonials}/>

      <div style={{ fontSize:20, fontWeight:800, margin:"30px 0 12px" }}>Qanday ishlaydi</div>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(220px,1fr))", gap:12 }}>
        {[[<PencilLine size={22}/>, "1-qadam", "Savolni ishlang", "Variantdan savol tanlab, javobni belgilang. To'g'ri yoki noto'g'riligini darrov ko'rasiz."],
          [<PlayCircle size={22}/>, "2-qadam", "Videoni ko'ring", "Ustoz masalani qanday yechishini bosqichma-bosqich ko'rsatadi. Tushunmasangiz, AI'dan so'rang."],
          [<Repeat size={22}/>, "3-qadam", "Mustahkamlang", "Analog savol va Test Generator bilan takrorlang, natijangizni tahlil bo'limida kuzating."]].map(([ic, k, t, d]) => (
          <div key={k} style={{ border:`1px solid ${B.line}`, borderRadius:14, padding:16 }}>
            <div style={{ width:42, height:42, borderRadius:10, background:B.panel, color:B.blue, display:"flex", alignItems:"center", justifyContent:"center" }}>{ic}</div>
            <div style={{ fontSize:12, color:B.blue, fontWeight:700, margin:"10px 0 2px" }}>{k}</div>
            <div style={{ fontSize:16, fontWeight:800, marginBottom:4 }}>{t}</div>
            <div style={{ fontSize:13.5, color:B.mid, lineHeight:1.55 }}>{d}</div>
          </div>
        ))}
      </div>

      <div style={{ fontSize:20, fontWeight:800, margin:"30px 0 12px" }}>Ishonchli va qulay</div>
      <div style={{ display:"grid", gridTemplateColumns:"repeat(auto-fit,minmax(220px,1fr))", gap:12 }}>
        {[[<ShieldCheck size={22}/>, "Xavfsiz to'lov", "Karta o'tkazmasi qilib, chekni yuborasiz, ustoz tasdiqlaydi. Sizdan parol yoki karta raqami so'ralmaydi."],
          [<CalendarCheck size={22}/>, "Majburiy emas", "Premium 30 kunga olinadi va o'zi uzaytirilmaydi. Davom etish yoki to'xtatish o'zingizning ixtiyoringizda."],
          [<Send size={22}/>, "Telegram orqali tasdiq", "To'lovingiz ustoz tomonidan tasdiqlanadi va kontent ochiladi. Holatni sayt ichida ko'rasiz."],
          [<Smartphone size={22}/>, "Telefonda ham", "Sayt telefon, planshet va kompyuterda bir xil qulay ishlaydi."]].map(([ic, t, d]) => (
          <div key={t} style={{ display:"flex", gap:12, border:`1px solid ${B.line}`, borderRadius:14, padding:14 }}>
            <div style={{ color:B.blue, flexShrink:0, marginTop:2 }}>{ic}</div>
            <div><div style={{ fontSize:15, fontWeight:800, marginBottom:3 }}>{t}</div><div style={{ fontSize:13.5, color:B.mid, lineHeight:1.55 }}>{d}</div></div>
          </div>
        ))}
      </div>

      <div style={{ fontSize:20, fontWeight:800, margin:"30px 0 12px" }}>Ko'p so'raladigan savollar</div>
      <div style={{ display:"grid", gap:8 }}>
        {[["Nimalar bepul?", "Har yilning 1-variantidan dastlabki 10 savol, mavzu darslari, hamda AI yordamchi shu savollarda. Qolgan variantlar va misollar Premiumda."],
          ["To'lov qanday amalga oshiriladi?", "Premium narxini ko'rsatilgan kartaga o'tkazasiz, chek rasmini saytga yuklaysiz. Ustoz tasdiqlagach hammasi ochiladi."],
          ["Variantni alohida sotib olsam bo'ladimi?", "Ha, variantni alohida sotib olish mumkin, narxi variantning o'zida ko'rsatilgan. Premium esa hamma variantni ochadi."]].map(([q, a]) => (
          <details key={q} style={{ border:`1px solid ${B.line}`, borderRadius:12, padding:"12px 16px" }}>
            <summary style={{ fontSize:15, fontWeight:700, cursor:"pointer" }}>{q}</summary>
            <div style={{ fontSize:14, color:B.mid, lineHeight:1.6, marginTop:8 }}>{a}</div>
          </details>
        ))}
      </div>

      <div style={{ background:B.navy, color:"#fff", borderRadius:16, padding:"24px 22px", marginTop:30, textAlign:"center" }}>
        <div style={{ fontSize:20, fontWeight:800 }}>Birinchi savolni hozir ishlab ko'ring</div>
        <div style={{ fontSize:14, color:"#C7D8F5", margin:"6px 0 16px" }}>Karta shart emas. Ro'yxatdan o'tish bir daqiqa.</div>
        <button onClick={openDtm} style={{ ...btn(false), background:"#fff", color:B.blue, border:"none" }}>Bepul boshlash <ArrowRight size={15}/></button>
      </div>
    </div>
  );
}
