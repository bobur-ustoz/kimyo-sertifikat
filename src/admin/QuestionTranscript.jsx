import { useEffect, useRef, useState } from "react";
import { FileText, Save } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { C, inputStyle, btnPrimary, btnGhost } from "./ui";

// The teacher's spoken explanation for one question, as text. Admin-only (RLS):
// students never read it; it is what an AI assistant would answer from.
export default function QuestionTranscript({ questionId }) {
  const [text, setText] = useState("");
  const [loaded, setLoaded] = useState(false);
  const [dirty, setDirty] = useState(false);
  const [msg, setMsg] = useState("");
  const fileRef = useRef(null);

  useEffect(() => {
    let off = false;
    setLoaded(false); setDirty(false); setMsg("");
    supabase.from("question_transcripts").select("content").eq("question_id", questionId).maybeSingle()
      .then(({ data, error }) => {
        if (off) return;
        if (error) setMsg("Matn yuklanmadi: " + error.message);
        setText(data?.content || ""); setLoaded(true);
      });
    return () => { off = true; };
  }, [questionId]);

  const save = async () => {
    setMsg("");
    const content = text.trim();
    const { error } = content
      ? await supabase.from("question_transcripts").upsert({ question_id: questionId, content, updated_at: new Date().toISOString() }, { onConflict: "question_id" })
      : await supabase.from("question_transcripts").delete().eq("question_id", questionId);
    if (error) { setMsg("Saqlanmadi: " + error.message); return; }
    setDirty(false); setMsg(content ? "Saqlandi" : "Matn o'chirildi");
  };

  return (
    <div style={{ marginTop: 14 }}>
      <div style={{ display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:6 }}>
        <div style={{ fontSize:10.5, fontWeight:700, color:C.textLight, textTransform:"uppercase", letterSpacing:"0.06em" }}>
          Video matni (o'quvchiga ko'rinmaydi)
        </div>
        <input ref={fileRef} type="file" accept=".txt,text/plain" style={{ display:"none" }}
          onChange={async e => { const f = e.target.files[0]; if (f) { setText(await f.text()); setDirty(true); } e.target.value = ""; }}/>
        <button style={btnGhost} onClick={() => fileRef.current?.click()}><FileText size={12}/> .txt yuklash</button>
      </div>
      <textarea style={{ ...inputStyle, minHeight:90, resize:"vertical", fontFamily:"inherit" }} disabled={!loaded}
        placeholder={loaded ? "Video matnini shu yerga yozing yoki .txt yuklang" : "Yuklanmoqda…"}
        value={text} onChange={e => { setText(e.target.value); setDirty(true); }}/>
      <div style={{ display:"flex", alignItems:"center", gap:10, marginTop:6 }}>
        {dirty && <button style={btnPrimary} onClick={save}><Save size={13}/> Matnni saqlash</button>}
        {msg && <span style={{ fontSize:11.5, color: msg.startsWith("Saqlanmadi") || msg.startsWith("Matn yuklanmadi") ? C.danger : C.primary }}>{msg}</span>}
        {!dirty && text && !msg && <span style={{ fontSize:11.5, color:C.textLight }}>{text.length} belgi</span>}
      </div>
    </div>
  );
}
