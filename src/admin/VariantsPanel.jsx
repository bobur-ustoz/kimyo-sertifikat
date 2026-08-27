import { useState } from "react";
import { Plus, Trash2, ChevronLeft } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import { writeErrorText } from "./writeError";
import { C, card, inputStyle, btnPrimary, btnGhost, pill, pageTitle, pageSub, errorBox } from "./ui";

export default function VariantsPanel({ teacher, onBack, onSelect }) {
  const [variants, reload] = useRows(
    () => supabase.from("variants").select("*").eq("teacher_id", teacher.id).order("variant_number"),
    [teacher.id]
  );
  const [newNum, setNewNum] = useState("");
  const [err, setErr] = useState("");

  const addVariant = async () => {
    const num = parseInt(newNum, 10);
    if (!num) { setErr("Variant raqamini kiriting."); return; }
    setErr("");
    const { error } = await supabase.from("variants")
      .insert({ teacher_id: teacher.id, variant_number: num, total_questions: 43 });
    if (error) { setErr(writeErrorText(error)); return; }
    setNewNum("");
    reload();
  };

  const delVariant = async (id) => {
    if (!confirm("Variantni o'chirishni tasdiqlaysizmi? Barcha savollari ham o'chadi.")) return;
    setErr("");
    const { error } = await supabase.from("variants").delete().eq("id", id);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  const update = async (v, patch) => {
    setErr("");
    const { error } = await supabase.from("variants").update(patch).eq("id", v.id);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  const freeCount = variants.filter(v => v.is_free).length;

  return (
    <div>
      <button style={{ ...btnGhost, marginBottom:14 }} onClick={onBack}><ChevronLeft size={14}/> O'qituvchilar</button>
      <h2 style={pageTitle}>{teacher.name} — Variantlar</h2>
      <p style={pageSub}>{teacher.subject}</p>

      <div style={{ ...card, marginBottom:14, display:"flex", gap:8, alignItems:"center", background:C.mintBg }}>
        <input style={{ ...inputStyle, width:120 }} type="number" placeholder="Variant raqami"
          value={newNum} onChange={e => setNewNum(e.target.value)}/>
        <button style={btnPrimary} onClick={addVariant}><Plus size={14}/> Variant qo'shish</button>
      </div>

      {err && <div style={errorBox}>{err}</div>}

      <div style={{background: freeCount ? C.mintBg : C.warningBg, border:`1px solid ${freeCount ? "#86EFAC" : "#FDE68A"}`,
        borderRadius:10, padding:"10px 13px", marginBottom:14, fontSize:12, color: freeCount ? C.primary : C.warning, lineHeight:1.6}}>
        {freeCount
          ? `Bu o'qituvchida ${freeCount} ta bepul variant bor — mehmonlar ham ko'ra oladi. Qolganlari pullik.`
          : "Diqqat: bu o'qituvchida bepul variant yo'q. Yangi o'quvchi hech narsa ko'ra olmaydi — bittasini bepul qilib qo'ying."}
      </div>

      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(160px,1fr))",gap:10}}>
        {variants.length === 0 && <div style={{color:C.textLight,fontSize:13,padding:12}}>Hali variant qo'shilmagan</div>}
        {variants.map(v => (
          <div key={v.id} style={{ ...card, padding:14, borderColor: v.is_free ? "#86EFAC" : C.border }}>
            <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:8}}>
              <div style={{fontWeight:800,fontSize:14,color:C.text}}>{v.variant_number}-Variant</div>
              <span style={v.is_free ? pill(C.mintBg, C.primary, "#86EFAC") : pill("#FFFBEB", "#B45309", "#FDE68A")}>
                {v.is_free ? "BEPUL" : "PULLIK"}
              </span>
            </div>

            <label style={{display:"flex",alignItems:"center",gap:6,fontSize:11.5,color:C.textMid,marginBottom:8,cursor:"pointer"}}>
              <input type="checkbox" checked={!!v.is_free} onChange={() => update(v, { is_free: !v.is_free })}/>
              Bepul ko'rsatilsin
            </label>

            {!v.is_free && (
              <div style={{display:"flex",alignItems:"center",gap:6,marginBottom:8}}>
                <input style={{ ...inputStyle, padding:"6px 9px", fontSize:12 }} type="number" min={0} step={1000}
                  defaultValue={v.price ?? 5000}
                  onBlur={e => {
                    const price = parseInt(e.target.value, 10);
                    if (Number.isFinite(price) && price >= 0 && price !== v.price) update(v, { price });
                  }}/>
                <span style={{fontSize:11,color:C.textLight,whiteSpace:"nowrap"}}>so'm</span>
              </div>
            )}

            <div style={{display:"flex",gap:6}}>
              <button style={{ ...btnGhost, flex:1, justifyContent:"center" }} onClick={() => onSelect(v)}>Savollar</button>
              <button style={{ ...btnGhost, padding:8, color:C.danger }} onClick={() => delVariant(v.id)}><Trash2 size={13}/></button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
