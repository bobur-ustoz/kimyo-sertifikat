import { useState } from "react";
import { ChevronLeft, CheckCircle2 } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import { writeErrorText } from "./writeError";
import { C, card, btnGhost, pill, toggleBtn, pageTitle, pageSub, errorBox } from "./ui";

const FILTERS = [["pending","Kutilmoqda"],["paid","To'langan"],["cancelled","Bekor qilingan"],["all","Hammasi"]];

const BADGE = {
  paid:      { style: pill(C.mintBg, C.primary, "#86EFAC"), label: "To'langan" },
  pending:   { style: pill(C.warningBg, C.warning, "#FDE68A"), label: "Kutilmoqda" },
  cancelled: { style: pill("#F1F5F9", C.textMid, C.border), label: "Bekor qilingan" },
};

export default function PurchasesPanel({ onBack }) {
  const [filter, setFilter] = useState("pending");
  const [busy, setBusy] = useState(null);
  const [err, setErr] = useState("");

  const [rows, reload] = useRows(() => {
    const q = supabase.from("variant_purchases")
      .select("*, variants(variant_number, price, teachers(name))")
      .order("created_at", { ascending: false })
      .limit(200);
    return filter === "all" ? q : q.eq("status", filter);
  }, [filter]);

  const mark = async (row, status) => {
    setBusy(row.id);
    setErr("");
    const { error } = await supabase.from("variant_purchases")
      .update({ status, paid_at: status === "paid" ? new Date().toISOString() : null })
      .eq("id", row.id);
    setBusy(null);
    if (error) { setErr(writeErrorText(error)); return; }
    reload();
  };

  return (
    <div>
      <button style={{ ...btnGhost, marginBottom:14 }} onClick={onBack}><ChevronLeft size={14}/> Orqaga</button>
      <h2 style={pageTitle}>Variant to'lovlari</h2>
      <p style={pageSub}>O'quvchi so'rov yuboradi → siz to'lovni qabul qilasiz → "To'landi" bosasiz va variant darhol ochiladi.</p>

      <div style={{display:"flex",gap:7,marginBottom:14,flexWrap:"wrap"}}>
        {FILTERS.map(([id, label]) => (
          <button key={id} onClick={() => setFilter(id)} style={toggleBtn(filter === id, { padding:"8px 12px", fontSize:12 })}>
            {label}
          </button>
        ))}
      </div>

      {err && <div style={errorBox}>{err}</div>}

      {rows.length === 0 && <div style={{ ...card, color:C.textLight, fontSize:13 }}>Bu bo'limda hozircha yozuv yo'q.</div>}

      <div style={{display:"flex",flexDirection:"column",gap:9}}>
        {rows.map(r => {
          const badge = BADGE[r.status];
          return (
            <div key={r.id} style={{ ...card, padding:"13px 15px" }}>
              <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",gap:12,flexWrap:"wrap"}}>
                <div style={{minWidth:0}}>
                  <div style={{fontSize:13.5,fontWeight:800,color:C.text}}>
                    {r.variants?.teachers?.name || "—"} · {r.variants?.variant_number}-Variant
                  </div>
                  <div style={{fontSize:11.5,color:C.textMid,marginTop:3}}>
                    {r.amount?.toLocaleString("ru-RU")} so'm · {r.contact || "telefon yo'q"} · {new Date(r.created_at).toLocaleString("uz-UZ")}
                  </div>
                  <div style={{fontSize:10.5,color:C.textLight,marginTop:2,fontFamily:"monospace"}}>{r.student_id}</div>
                </div>
                <div style={{display:"flex",alignItems:"center",gap:7}}>
                  <span style={badge.style}>{badge.label}</span>
                  {r.status !== "paid" && (
                    <button disabled={busy === r.id} style={{ ...btnGhost, color:C.primary, borderColor:C.primary }} onClick={() => mark(r, "paid")}>
                      <CheckCircle2 size={12}/> To'landi
                    </button>
                  )}
                  {r.status === "pending" && (
                    <button disabled={busy === r.id} style={{ ...btnGhost, color:C.danger }} onClick={() => mark(r, "cancelled")}>Bekor</button>
                  )}
                  {r.status === "paid" && (
                    <button disabled={busy === r.id} style={btnGhost} onClick={() => mark(r, "cancelled")}>Yopish</button>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
