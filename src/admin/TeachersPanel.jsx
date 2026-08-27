import { useState } from "react";
import { Plus, Trash2, Save } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import { writeErrorText } from "./writeError";
import { C, card, inputStyle, btnPrimary, btnGhost, pageTitle, errorBox } from "./ui";

const EMPTY = { name:"", subject:"", initials:"", color:"#0F5132", bg_color:"#F0FDF4", rating:5, students:0, badge:"", is_free:true, description:"" };

// Each entry is [key, label, extra props / value transform] so the six near
// identical inputs below stay one loop instead of six copied blocks.
const FIELDS = [
  ["name", "Ism-familiya", {}],
  ["subject", "Fan", {}],
  ["initials", "Inisiallar (2 harf)", { maxLength: 2, transform: v => v.toUpperCase() }],
  ["color", "Rang (hex)", {}],
  ["badge", "Badge (ixtiyoriy)", {}],
];

function TeacherForm({ editing, onSaved, onCancel }) {
  const [f, setF] = useState(editing || EMPTY);
  const [err, setErr] = useState("");
  const set = (k, v) => setF(p => ({ ...p, [k]: v }));

  const save = async () => {
    if (!f.name || !f.subject || !f.initials) {
      setErr("Ism, fan va inisiallar to'ldirilishi shart.");
      return;
    }
    setErr("");
    const { error } = editing
      ? await supabase.from("teachers").update(f).eq("id", editing.id)
      : await supabase.from("teachers").insert(f);
    if (error) { setErr(writeErrorText(error)); return; }
    onSaved();
  };

  return (
    <div style={{ ...card, marginBottom:14, background:C.mintBg }}>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
        {FIELDS.map(([key, label, { transform, ...props }]) => (
          <div key={key}>
            <label style={{fontSize:11,color:C.textMid}}>{label}</label>
            <input {...props} style={inputStyle} value={f[key] || ""}
              onChange={e => set(key, transform ? transform(e.target.value) : e.target.value)}/>
          </div>
        ))}
        <label style={{display:"flex",alignItems:"center",gap:8,marginTop:18,fontSize:12,color:C.text,cursor:"pointer"}}>
          <input type="checkbox" checked={f.is_free} onChange={e => set("is_free", e.target.checked)}/>
          Bepul kolleksiya
        </label>
      </div>

      <label style={{fontSize:11,color:C.textMid}}>Tavsif</label>
      <textarea style={{...inputStyle, marginBottom:10, minHeight:60}} value={f.description || ""}
        onChange={e => set("description", e.target.value)}/>

      {err && <div style={errorBox}>{err}</div>}

      <div style={{display:"flex",gap:8}}>
        <button style={btnPrimary} onClick={save}><Save size={13}/> Saqlash</button>
        <button style={btnGhost} onClick={onCancel}>Bekor qilish</button>
      </div>
    </div>
  );
}

export default function TeachersPanel({ onSelect }) {
  const [teachers, reload] = useRows(() =>
    supabase.from("teachers").select("*").order("sort_order").order("created_at"));
  const [editing, setEditing] = useState(null);   // teacher being edited
  const [showForm, setShowForm] = useState(false);
  const [err, setErr] = useState("");

  const del = async (id) => {
    if (!confirm("O'qituvchini o'chirishni tasdiqlaysizmi? Barcha variant va savollari ham o'chadi.")) return;
    setErr("");
    const { error } = await supabase.from("teachers").delete().eq("id", id);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  return (
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14}}>
        <h2 style={{...pageTitle, marginBottom:0}}>O'qituvchilar</h2>
        <button style={btnPrimary} onClick={() => { setEditing(null); setShowForm(true); }}>
          <Plus size={14}/> Yangi o'qituvchi
        </button>
      </div>

      {showForm && (
        <TeacherForm editing={editing} onCancel={() => setShowForm(false)}
          onSaved={() => { setShowForm(false); reload(); }}/>
      )}

      {err && <div style={errorBox}>{err}</div>}

      <div style={{display:"flex",flexDirection:"column",gap:8}}>
        {teachers.length === 0 && (
          <div style={{color:C.textLight,fontSize:13,padding:20,textAlign:"center"}}>Hali o'qituvchi qo'shilmagan</div>
        )}
        {teachers.map(t => (
          <div key={t.id} style={{...card, display:"flex", alignItems:"center", gap:12}}>
            <div style={{width:38,height:38,borderRadius:10,background:t.color,display:"flex",alignItems:"center",justifyContent:"center",color:"#fff",fontWeight:800,fontSize:13,flexShrink:0}}>
              {t.initials}
            </div>
            <div style={{flex:1,minWidth:0}}>
              <div style={{fontWeight:700,fontSize:13.5,color:C.text}}>{t.name}</div>
              <div style={{fontSize:11.5,color:C.textMid}}>{t.subject}{t.is_free ? " · Bepul" : " · Premium"}</div>
            </div>
            <button style={btnGhost} onClick={() => onSelect(t)}>Variantlar →</button>
            <button style={{...btnGhost, padding:8}} onClick={() => { setEditing(t); setShowForm(true); }}>✏️</button>
            <button style={{...btnGhost, padding:8, color:C.danger}} onClick={() => del(t.id)}><Trash2 size={13}/></button>
          </div>
        ))}
      </div>
    </div>
  );
}
