import { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C, card, pageTitle } from "./ui";
import { loadSurveyQuestions } from "../Survey";

// Admin view of the 2019 / variant 1 survey: how many students marked each question as hard.
export default function SurveyResults() {
  const [rows,setRows]=useState(null);
  const [voters,setVoters]=useState(0);
  useEffect(()=>{
    (async()=>{
      const qs=await loadSurveyQuestions();
      const { data } = await supabase.from("question_votes").select("student_id,question_id").in("question_id",qs.map(q=>q.id)).limit(20000);
      const cnt={}; (data||[]).forEach(v=>{ cnt[v.question_id]=(cnt[v.question_id]||0)+1; });
      setVoters(new Set((data||[]).map(v=>v.student_id)).size);
      setRows(qs.map(q=>({...q,votes:cnt[q.id]||0})).sort((a,b)=>b.votes-a.votes||a.question_number-b.question_number));
    })();
  },[]);
  const max=Math.max(1,...(rows||[]).map(r=>r.votes));
  return (
    <div>
      <div style={pageTitle}>So'rov natijalari · 2019 yil, 1-variant</div>
      <div style={{fontSize:12.5,color:C.textMid,marginBottom:14}}>{rows?`${voters} ta o'quvchi qatnashdi. Eng ko'p "qiyin" deyilgan misollar tepada.`:"Yuklanmoqda..."}</div>
      {rows&&<div style={card}>
        {rows.map(r=>(
          <div key={r.id} style={{display:"flex",alignItems:"center",gap:12,padding:"8px 0",borderBottom:`1px solid ${C.border}`}}>
            <div style={{width:34,fontWeight:900,color:C.primary}}>{r.question_number}</div>
            <div style={{width:190,fontSize:12.5,fontWeight:700,color:C.text,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>{r.topic||"—"}</div>
            <div style={{flex:1,background:"#F1F5F9",borderRadius:6,height:12,overflow:"hidden"}}><div style={{width:`${(r.votes/max)*100}%`,height:"100%",background:r.votes===max&&r.votes>0?C.danger:C.accent,borderRadius:6}}/></div>
            <div style={{width:60,textAlign:"right",fontSize:13,fontWeight:900,color:C.text}}>{r.votes} ta</div>
          </div>
        ))}
      </div>}
    </div>
  );
}
