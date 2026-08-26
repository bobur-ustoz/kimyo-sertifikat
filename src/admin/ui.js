// Every visual decision for the admin panel lives here, so the panels
// themselves stay about behaviour rather than pixels.

export const C = {
  primary:"#0F5132", accent:"#0D9488", mint:"#6EE7B7", mintBg:"#F0FDF4",
  bgSoft:"#F8FAFC", text:"#0F172A", textMid:"#475569", textLight:"#94A3B8",
  border:"#E2E8F0", danger:"#DC2626", warning:"#D97706", warningBg:"#FFFBEB",
};

export const card = { background:"#fff", border:`1px solid ${C.border}`, borderRadius:12, padding:16 };

export const inputStyle = {
  width:"100%", padding:"9px 11px", borderRadius:8,
  border:`1px solid ${C.border}`, fontSize:13, fontFamily:"inherit", color:C.text,
};

const btnBase = { borderRadius:8, cursor:"pointer", fontFamily:"inherit", display:"flex", alignItems:"center" };

export const btnPrimary = { ...btnBase, padding:"9px 14px", background:C.primary, color:"#fff", border:"none", fontSize:12.5, fontWeight:700, gap:6 };
export const btnGhost   = { ...btnBase, padding:"8px 12px", background:"#fff", color:C.textMid, border:`1px solid ${C.border}`, fontSize:12, fontWeight:600, gap:5 };

// A button that shows whether it is the current choice: question type, correct
// answer letter, purchase filter. Used often enough that repeating the style
// inline was most of the noise in this panel.
export const toggleBtn = (active, extra = {}) => ({
  padding:"6px 12px", borderRadius:7,
  border:`1px solid ${active ? C.primary : C.border}`,
  background: active ? C.primary : "#fff",
  color: active ? "#fff" : C.textMid,
  fontSize:11.5, fontWeight:700, cursor:"pointer", fontFamily:"inherit",
  ...extra,
});

// Small coloured status pill (BEPUL / PULLIK / To'langan / Kutilmoqda).
export const pill = (bg, fg, bd) => ({
  fontSize:10, fontWeight:800, padding:"3px 9px", borderRadius:20,
  background:bg, color:fg, border:`1px solid ${bd}`,
});

export const pageTitle  = { fontSize:17, fontWeight:800, color:C.text, marginBottom:4 };
export const pageSub    = { fontSize:12.5, color:C.textMid, marginBottom:14 };
export const fieldLabel = { fontSize:11.5, fontWeight:700, color:C.textMid, marginBottom:5, display:"block" };
export const hint       = { fontSize:11, color:C.textLight };
export const sectionLabel = { fontSize:10.5, fontWeight:700, color:C.textLight, textTransform:"uppercase", letterSpacing:"0.06em", marginBottom:6 };
