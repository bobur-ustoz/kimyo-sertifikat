import { useState } from "react";
import { Plus, ChevronLeft } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import QuestionRow from "./QuestionRow";
import OptionGroups from "./OptionGroups";
import { writeErrorText } from "./writeError";
import { card, btnPrimary, btnGhost, pageTitle, pageSub, C, errorBox } from "./ui";

export default function QuestionsPanel({ variant, teacher, onBack }) {
  const [questions, reloadQuestions] = useRows(
    () => supabase.from("questions").select("*").eq("variant_id", variant.id).order("question_number"),
    [variant.id]
  );
  const [groups, reloadGroups] = useRows(
    () => supabase.from("option_groups").select("*").eq("variant_id", variant.id).order("created_at"),
    [variant.id]
  );

  const [err, setErr] = useState("");

  const generateAll = async () => {
    const rows = Array.from({ length: variant.total_questions }, (_, i) => ({
      variant_id: variant.id,
      question_number: i + 1,
    }));
    setErr("");
    const { error } = await supabase.from("questions").insert(rows);
    if (error) { setErr(writeErrorText(error)); return; }
    reloadQuestions();
  };

  const doneCount = questions.filter(q => q.video_ready).length;

  return (
    <div>
      <button style={{ ...btnGhost, marginBottom:14 }} onClick={onBack}><ChevronLeft size={14}/> Variantlar</button>
      <h2 style={pageTitle}>{teacher.name} · {variant.variant_number}-Variant — Savollar</h2>
      <p style={pageSub}>{doneCount}/{questions.length} video tayyor</p>

      {err && <div style={errorBox}>{err}</div>}

      {questions.length === 0 ? (
        <div style={{ ...card, textAlign:"center", padding:24 }}>
          <p style={{fontSize:13,color:C.textMid,marginBottom:12}}>Bu variant uchun hali savollar yaratilmagan.</p>
          <button style={btnPrimary} onClick={generateAll}>
            <Plus size={14}/> {variant.total_questions} ta savol yaratish
          </button>
        </div>
      ) : (
        <div>
          <OptionGroups variantId={variant.id} groups={groups} onChanged={reloadGroups}/>
          {questions.map(q => <QuestionRow key={q.id} q={q} onChanged={reloadQuestions} groups={groups}/>)}
        </div>
      )}
    </div>
  );
}
