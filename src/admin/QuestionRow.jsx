import { useRef, useState } from "react";
import { Save, CheckCircle2, Circle, UploadCloud } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useVideoUpload } from "./useVideoUpload";
import { videoTitle } from "./uploadVideo";
import AnalogReview from "./AnalogReview";
import { writeErrorText } from "./writeError";
import { C, card, inputStyle, btnPrimary, btnGhost, toggleBtn, hint, sectionLabel, errorBox } from "./ui";

const TYPE_LABELS = { mcq:"A/B/C/D", open:"Ochiq javob", match:"Moslashtirish" };
const LETTERS = ["A","B","C","D"];

export default function QuestionRow({ q, onChanged, groups, teacher, variant }) {
  const [f, setF] = useState(() => ({ question_type:"mcq", ...q }));
  const [dirty, setDirty] = useState(false);
  const [open, setOpen] = useState(false);
  const fileRef = useRef(null);
  const [saveErr, setSaveErr] = useState("");

  const set = (k, v) => { setF(p => ({ ...p, [k]: v })); setDirty(true); };

  const { pct, error: uploadErr, upload } = useVideoUpload(q, videoTitle(teacher, variant, q), (videoId) => {
    setF(p => ({ ...p, bunny_video_id: videoId, video_ready: true }));
    onChanged();
  });

  const save = async () => {
    setSaveErr("");
    const { error } = await supabase.from("questions").update({
      topic: f.topic, formula: f.formula, question_text: f.question_text,
      video_url: f.video_url, video_ready: f.video_ready,
      question_type: f.question_type,
      option_a: f.option_a, option_b: f.option_b, option_c: f.option_c, option_d: f.option_d,
      correct_option: f.question_type === "open" ? null : f.correct_option,
      correct_answer_text: f.question_type === "open" ? f.correct_answer_text : null,
      option_group_id: f.question_type === "match" ? (f.option_group_id || null) : null,
    }).eq("id", q.id);
    if (error) { setSaveErr(writeErrorText(error)); return; }
    setDirty(false);
    onChanged();
  };

  const selectedGroup = groups.find(g => g.id === f.option_group_id);

  return (
    <div style={{ ...card, marginBottom:8, padding:"12px 14px" }}>
      {/* header: ready mark, number, topic, formula */}
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:8}}>
        <button onClick={() => set("video_ready", !f.video_ready)} title="Video tayyor deb belgilash"
          style={{background:"none",border:"none",cursor:"pointer",padding:0,flexShrink:0}}>
          {f.video_ready ? <CheckCircle2 size={19} color={C.primary}/> : <Circle size={19} color={C.textLight}/>}
        </button>
        <div style={{fontWeight:800,fontSize:13,color:C.text,width:70,flexShrink:0}}>{q.question_number}-savol</div>
        <input style={{ ...inputStyle, flex:1 }} placeholder="Mavzu" value={f.topic || ""} onChange={e => set("topic", e.target.value)}/>
        <input style={{ ...inputStyle, flex:1 }} placeholder="Formula (ixtiyoriy)" value={f.formula || ""} onChange={e => set("formula", e.target.value)}/>
        <button style={btnGhost} onClick={() => setOpen(o => !o)}>{open ? "Yopish" : "Savol va javoblar"}</button>
      </div>

      {/* video row */}
      <div style={{display:"flex",gap:8,marginBottom: open ? 8 : 0, alignItems:"center"}}>
        {f.bunny_video_id ? (
          <div style={{ ...inputStyle, flex:1, display:"flex", alignItems:"center", gap:8, color:C.primary, fontWeight:600 }}>
            <CheckCircle2 size={14}/> Video yuklangan (Bunny)
          </div>
        ) : (
          <input style={{ ...inputStyle, flex:1 }} placeholder="Video havolasi (URL, ixtiyoriy)"
            value={f.video_url || ""} onChange={e => set("video_url", e.target.value)}/>
        )}
        <input ref={fileRef} type="file" accept="video/*" style={{display:"none"}}
          onChange={e => { const file = e.target.files[0]; if (file) upload(file); e.target.value = ""; }}/>
        {pct === null ? (
          <button style={btnGhost} onClick={() => fileRef.current?.click()}>
            <UploadCloud size={13}/> {f.bunny_video_id ? "Almashtirish" : "Video yuklash"}
          </button>
        ) : (
          <div style={{fontSize:11.5,color:C.textMid,fontWeight:700,minWidth:90}}>Yuklanmoqda… {pct}%</div>
        )}
        {dirty && <button style={btnPrimary} onClick={save}><Save size={13}/> Saqlash</button>}
      </div>
      {uploadErr && <p style={{fontSize:11,color:C.danger,marginBottom: open ? 8 : 0}}>Xatolik: {uploadErr}</p>}
      {saveErr && <div style={{ ...errorBox, marginTop:8, marginBottom: open ? 8 : 0 }}>{saveErr}</div>}

      {open && (
        <div style={{borderTop:`1px solid ${C.border}`,paddingTop:10,marginTop:2}}>
          <textarea style={{ ...inputStyle, minHeight:60, resize:"vertical", marginBottom:10, fontFamily:"inherit" }}
            placeholder="Savol matni" value={f.question_text || ""} onChange={e => set("question_text", e.target.value)}/>

          <div style={sectionLabel}>Savol turi</div>
          <div style={{display:"flex",gap:6,marginBottom:12}}>
            {Object.entries(TYPE_LABELS).map(([type, label]) => (
              <button key={type} onClick={() => set("question_type", type)} style={toggleBtn(f.question_type === type)}>
                {label}
              </button>
            ))}
          </div>

          {f.question_type === "mcq" && (<>
            <div style={sectionLabel}>Javob variantlari</div>
            {LETTERS.map(letter => (
              <div key={letter} style={{display:"flex",alignItems:"center",gap:8,marginBottom:6}}>
                <button onClick={() => set("correct_option", letter)} title="To'g'ri javob qilib belgilash"
                  style={toggleBtn(f.correct_option === letter, { width:26, height:26, borderRadius:"50%", flexShrink:0, padding:0, fontSize:11, fontWeight:800 })}>
                  {letter}
                </button>
                <input style={{ ...inputStyle, flex:1 }} placeholder={`${letter} variant matni`}
                  value={f[`option_${letter.toLowerCase()}`] || ""}
                  onChange={e => set(`option_${letter.toLowerCase()}`, e.target.value)}/>
              </div>
            ))}
            <p style={hint}>To'g'ri javobni belgilash uchun harf tugmasini bosing (hozir: {f.correct_option || "tanlanmagan"}).</p>
          </>)}

          {f.question_type === "open" && (
            <div>
              <label style={{fontSize:11,color:C.textMid,display:"block",marginBottom:5}}>To'g'ri javob (namunaviy — AI shu bilan solishtirib tekshiradi)</label>
              <input style={inputStyle} placeholder="masalan: 11/3" value={f.correct_answer_text || ""}
                onChange={e => set("correct_answer_text", e.target.value)}/>
            </div>
          )}

          {f.question_type === "match" && (
            <div>
              <label style={{fontSize:11,color:C.textMid,display:"block",marginBottom:6}}>Qaysi guruhdan foydalanadi</label>
              <select style={inputStyle} value={f.option_group_id || ""} onChange={e => set("option_group_id", e.target.value || null)}>
                <option value="">— tanlang —</option>
                {groups.map(g => <option key={g.id} value={g.id}>{g.label || g.options.map(o => o.letter).join("")}</option>)}
              </select>
              {groups.length === 0 && <p style={{ ...hint, marginTop:6 }}>Avval yuqorida "Guruh qo'shish" orqali A-F javoblarni kiriting.</p>}
              {selectedGroup && (
                <div style={{marginTop:10}}>
                  <div style={{ ...hint, marginBottom:6 }}>To'g'ri javobni tanlang:</div>
                  <div style={{display:"flex",gap:6,flexWrap:"wrap"}}>
                    {selectedGroup.options.map(o => (
                      <button key={o.letter} onClick={() => set("correct_option", o.letter)} title={o.text}
                        style={toggleBtn(f.correct_option === o.letter, { fontSize:12 })}>
                        {o.letter}) {o.text}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          <AnalogReview questionId={q.id} topic={f.topic}/>
        </div>
      )}
    </div>
  );
}
