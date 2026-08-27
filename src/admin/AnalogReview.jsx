import { useState } from "react";
import { Trash2, Sparkles, ThumbsUp } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import { writeErrorText } from "./writeError";
import { C, btnGhost, sectionLabel } from "./ui";

async function callClaude(prompt, maxTokens) {
  const res = await fetch("/api/claude", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt, maxTokens }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || "AI xatosi");
  return (data.text || "").replace(/```json\n?|\n?```/g, "").trim();
}

// AI-written analog questions stay invisible to students until an admin
// approves them: chemistry accuracy can't be auto-guaranteed.
export default function AnalogReview({ questionId, topic }) {
  const [items, reload] = useRows(
    () => supabase.from("analog_questions").select("*").eq("question_id", questionId).order("created_at", { ascending: false }),
    [questionId]
  );
  const [generating, setGenerating] = useState(false);
  const [err, setErr] = useState("");

  const generate = async () => {
    if (!topic) { setErr("Avval mavzuni kiriting."); return; }
    setGenerating(true);
    setErr("");
    try {
      const prompt = `Kimyo fani bo'yicha "${topic}" mavzusida analog savol yarat. O'zbek tilida. FAQAT JSON formatda javob ber, boshqa hech narsa yozma:\n{"savol":"savol matni","formula":"asosiy formula (yoki bo'sh satr)","yechim":["1-qadam","2-qadam","3-qadam"],"javob":"yakuniy javob"}`;
      const parsed = JSON.parse(await callClaude(prompt, 1200));
      const { error } = await supabase.from("analog_questions").insert({
        question_id: questionId,
        savol: parsed.savol,
        formula: parsed.formula || null,
        yechim: parsed.yechim || [],
        javob: parsed.javob,
        is_approved: false,
      });
      if (error) { setErr(writeErrorText(error)); setGenerating(false); return; }
      reload();
    } catch (e) {
      setErr("Generatsiyada xatolik: " + e.message);
    }
    setGenerating(false);
  };

  const setApproved = async (id, is_approved) => {
    setErr("");
    const { error } = await supabase.from("analog_questions").update({ is_approved }).eq("id", id);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  const del = async (id) => {
    if (!confirm("O'chirilsinmi?")) return;
    const { error } = await supabase.from("analog_questions").delete().eq("id", id);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  return (
    <div style={{borderTop:`1px solid ${C.border}`,marginTop:14,paddingTop:12}}>
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:10}}>
        <div style={sectionLabel}>AI Analog savollar (tasdiqlangunicha o'quvchiga ko'rinmaydi)</div>
        <button onClick={generate} disabled={generating} style={{ ...btnGhost, color:C.accent, borderColor:C.accent }}>
          {generating ? "Yaratilmoqda..." : <><Sparkles size={12}/> Yangi analog yaratish</>}
        </button>
      </div>

      {err && <p style={{fontSize:11.5,color:C.danger,marginBottom:8}}>{err}</p>}
      {items.length === 0 && <p style={{fontSize:11.5,color:C.textLight}}>Hali analog yaratilmagan.</p>}

      {items.map(it => (
        <div key={it.id} style={{background: it.is_approved ? C.mintBg : C.warningBg,
          border:`1px solid ${it.is_approved ? "#86EFAC" : "#FDE68A"}`, borderRadius:9, padding:"10px 12px", marginBottom:8}}>
          <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:6}}>
            <span style={{fontSize:10.5,fontWeight:800,color: it.is_approved ? C.primary : C.warning}}>
              {it.is_approved ? "✓ Tasdiqlangan" : "Kutilmoqda"}
            </span>
            <div style={{display:"flex",gap:6}}>
              {it.is_approved
                ? <button style={{ ...btnGhost, padding:"5px 9px" }} onClick={() => setApproved(it.id, false)}>Bekor qilish</button>
                : <button style={{ ...btnGhost, padding:"5px 9px", color:C.primary, borderColor:C.primary }} onClick={() => setApproved(it.id, true)}><ThumbsUp size={11}/> Tasdiqlash</button>}
              <button style={{ ...btnGhost, padding:"5px 9px", color:C.danger }} onClick={() => del(it.id)}><Trash2 size={11}/></button>
            </div>
          </div>
          <p style={{fontSize:12.5,color:C.text,marginBottom:6}}>{it.savol}</p>
          {it.formula && <div style={{fontFamily:"'Courier New',monospace",fontSize:12,color:C.text,background:"#fff",padding:"6px 10px",borderRadius:6,marginBottom:6}}>{it.formula}</div>}
          <ol style={{margin:"0 0 6px 18px",padding:0}}>
            {(it.yechim || []).map((s, i) => <li key={i} style={{fontSize:11.5,color:C.textMid}}>{s}</li>)}
          </ol>
          <div style={{fontSize:12,fontWeight:700,color:C.text}}>Javob: {it.javob}</div>
        </div>
      ))}
    </div>
  );
}
