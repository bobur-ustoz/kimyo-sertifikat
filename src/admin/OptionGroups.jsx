import { useState } from "react";
import { Plus, Trash2, Save } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { writeErrorText } from "./writeError";
import { C, card, inputStyle, btnPrimary, btnGhost, errorBox } from "./ui";

const blankOptions = () => ["A","B","C","D","E","F"].map(letter => ({ letter, text:"" }));

// Shared answer pools for "matching" questions, where 33-35 all pick from the
// same A-F list.
export default function OptionGroups({ variantId, groups, onChanged }) {
  const [adding, setAdding] = useState(false);
  const [label, setLabel] = useState("");
  const [opts, setOpts] = useState(blankOptions);
  const [err, setErr] = useState("");

  const reset = () => { setAdding(false); setLabel(""); setOpts(blankOptions()); };

  const save = async () => {
    const filled = opts.filter(o => o.text.trim());
    if (filled.length < 2) { setErr("Kamida ikkita javob varianti kiriting."); return; }
    setErr("");
    const { error } = await supabase.from("option_groups").insert({ variant_id: variantId, label, options: filled });
    if (error) { setErr(writeErrorText(error)); return; }
    reset();
    onChanged();
  };

  const del = async (id) => {
    if (!confirm("Guruhni o'chirasizmi? Unga bog'langan savollar 'moslashtirish' turida qolib, guruhsiz bo'lib qoladi.")) return;
    const { error } = await supabase.from("option_groups").delete().eq("id", id);
    if (error) { setErr(writeErrorText(error)); return; }
    onChanged();
  };

  return (
    <div style={{ ...card, marginBottom:14, background:C.mintBg }}>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom: groups.length || adding ? 10 : 0}}>
        <div style={{fontWeight:800,fontSize:13.5,color:C.text}}>Moslashtirish guruhlari (umumiy A–F javoblar)</div>
        {!adding && <button style={btnGhost} onClick={() => setAdding(true)}><Plus size={13}/> Guruh qo'shish</button>}
      </div>

      {err && <div style={errorBox}>{err}</div>}

      {groups.map(g => (
        <div key={g.id} style={{background:"#fff",borderRadius:9,padding:"8px 12px",marginBottom:6,display:"flex",alignItems:"center",gap:10,border:`1px solid ${C.border}`}}>
          <div style={{flex:1,fontSize:12,color:C.text}}>
            <strong>{g.label || "(nomsiz guruh)"}</strong> — {g.options.map(o => `${o.letter}) ${o.text}`).join(", ")}
          </div>
          <button style={{ ...btnGhost, padding:6, color:C.danger }} onClick={() => del(g.id)}><Trash2 size={12}/></button>
        </div>
      ))}

      {adding && (
        <div style={{background:"#fff",borderRadius:9,padding:12,border:`1px solid ${C.border}`}}>
          <input style={{ ...inputStyle, marginBottom:8 }} placeholder="Guruh nomi (ixtiyoriy, masalan '33-35 savollar')"
            value={label} onChange={e => setLabel(e.target.value)}/>
          {opts.map((o, i) => (
            <div key={o.letter} style={{display:"flex",gap:8,marginBottom:6,alignItems:"center"}}>
              <div style={{width:22,fontSize:11,fontWeight:800,color:C.textMid}}>{o.letter}</div>
              <input style={{ ...inputStyle, flex:1 }} placeholder={`${o.letter} variant matni`} value={o.text}
                onChange={e => setOpts(prev => prev.map((x, xi) => xi === i ? { ...x, text: e.target.value } : x))}/>
            </div>
          ))}
          <div style={{display:"flex",gap:8,marginTop:8}}>
            <button style={btnPrimary} onClick={save}><Save size={13}/> Saqlash</button>
            <button style={btnGhost} onClick={reset}>Bekor qilish</button>
          </div>
        </div>
      )}

      {!groups.length && !adding && (
        <div style={{fontSize:12,color:C.textLight}}>Hali guruh yo'q. "Moslashtirish" turidagi savollar uchun avval shu yerda guruh yarating.</div>
      )}
    </div>
  );
}
