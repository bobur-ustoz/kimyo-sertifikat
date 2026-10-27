import { useEffect, useState } from "react";
import { CheckCircle2, ClipboardList } from "lucide-react";
import { supabase } from "./lib/supabaseClient";

const C = { primary:"#0F5132", accent:"#0D9488", mintBg:"#F0FDF4", borderGreen:"#86EFAC", text:"#0F172A", textMid:"#475569", textLight:"#94A3B8", border:"#E2E8F0", danger:"#DC2626", dangerBg:"#FEF2F2" };

// The 2019 variant 1 survey: the student taps the questions that were hard for them.
export async function loadSurveyQuestions() {
  const { data: t } = await supabase.from("teachers").select("id").eq("section","dtm").ilike("name","%2019%").limit(1).maybeSingle();
  if(!t) return [];
  const { data: v } = await supabase.from("variants").select("id").eq("teacher_id",t.id).eq("variant_number",1).maybeSingle();
  if(!v) return [];
  const { data } = await supabase.from("questions").select("id,question_number,topic,question_text").eq("variant_id",v.id).order("question_number");
  return data||[];
}

export default function Survey({session,setTab}) {
  const [qs,setQs]=useState(null);
  const [mine,setMine]=useState(new Set());
  const [busy,setBusy]=useState(false);
  const [err,setErr]=useState("");

  useEffect(()=>{ loadSurveyQuestions().then(setQs); },[]);
  useEffect(()=>{
    if(!session) return;
    supabase.from("question_votes").select("question_id").eq("student_id",session.user.id).then(({data})=>setMine(new Set((data||[]).map(r=>r.question_id))));
  },[session?.user?.id]);

  const toggle = async q => {
    if(!session){ setTab("profile"); return; }
    setBusy(true); setErr("");
    const on=mine.has(q.id);
    const next=new Set(mine); on?next.delete(q.id):next.add(q.id); setMine(next);
    const { error } = on
      ? await supabase.from("question_votes").delete().eq("student_id",session.user.id).eq("question_id",q.id)
      : await supabase.from("question_votes").insert({student_id:session.user.id,question_id:q.id});
    if(error){ setErr("Saqlanmadi. Qayta urinib ko'ring."); setMine(mine); }
    setBusy(false);
  };

  return (
    <div style={{padding:"24px 28px 40px",overflowY:"auto"}}>
      <div style={{display:"flex",alignItems:"center",gap:7,marginBottom:6}}><ClipboardList size={14} color={C.accent}/><span style={{fontSize:11,fontWeight:700,color:C.accent,textTransform:"uppercase",letterSpacing:"0.09em"}}>So'rov · 2019 yil, 1-variant</span></div>
      <h1 style={{fontSize:24,fontWeight:900,color:C.text,margin:"0 0 6px"}}>Qaysi misollar sizga qiyin bo'ldi?</h1>
      <p style={{fontSize:13.5,color:C.textMid,margin:"0 0 16px",maxWidth:640}}>Yecholmagan yoki qiynalgan misollarni bosib belgilang. Ko'p kishi belgilagan misollar tahliliga alohida e'tibor beriladi. Javobingiz avtomatik saqlanadi, istalgan vaqtda o'zgartirsangiz bo'ladi.</p>
      {!session&&<div style={{background:C.dangerBg,border:"1px solid #FECACA",borderRadius:12,padding:"12px 14px",marginBottom:14,fontSize:13,color:C.danger}}>Belgilash uchun avval hisobingizga kiring (Profilim).</div>}
      {err&&<div style={{fontSize:12.5,color:C.danger,marginBottom:10}}>{err}</div>}
      {qs===null?<div style={{fontSize:13,color:C.textMid}}>Yuklanmoqda...</div>:!qs.length?<div style={{fontSize:13,color:C.textMid}}>Misollar topilmadi.</div>:(
        <>
          <div style={{fontSize:13,fontWeight:800,color:C.primary,marginBottom:12}}>{mine.size} ta misol belgilandi</div>
          <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(260px,1fr))",gap:10,maxWidth:980}}>
            {qs.map(q=>{ const on=mine.has(q.id); return (
              <button key={q.id} onClick={()=>toggle(q)} disabled={busy} style={{textAlign:"left",display:"flex",gap:11,alignItems:"flex-start",padding:"12px 14px",borderRadius:14,border:`1.5px solid ${on?C.danger:C.border}`,background:on?C.dangerBg:"#fff",cursor:"pointer",fontFamily:"inherit"}}>
                <div style={{width:34,height:34,borderRadius:10,background:on?C.danger:C.mintBg,color:on?"#fff":C.primary,display:"flex",alignItems:"center",justifyContent:"center",fontWeight:900,fontSize:14,flexShrink:0}}>{q.question_number}</div>
                <div style={{flex:1,minWidth:0}}>
                  <div style={{fontSize:13,fontWeight:800,color:C.text}}>{q.topic||`${q.question_number}-misol`}</div>
                  <div style={{fontSize:11.5,color:C.textMid,marginTop:2,lineHeight:1.45,overflow:"hidden",display:"-webkit-box",WebkitLineClamp:2,WebkitBoxOrient:"vertical"}}>{q.question_text||""}</div>
                </div>
                {on&&<CheckCircle2 size={17} color={C.danger} style={{flexShrink:0,marginTop:2}}/>}
              </button>
            ); })}
          </div>
        </>
      )}
    </div>
  );
}
