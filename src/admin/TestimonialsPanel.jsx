import { useState } from "react";
import { Plus, Trash2, Eye, EyeOff, BadgeCheck, Upload } from "lucide-react";
import { supabase } from "../lib/supabaseClient";
import { useRows } from "./useRows";
import { writeErrorText } from "./writeError";
import { C, card, inputStyle, btnPrimary, btnGhost, pageTitle, pageSub, errorBox } from "./ui";

export const testimonialUrl = (path) => path ? supabase.storage.from("testimonials").getPublicUrl(path).data.publicUrl : null;

const blank = { name: "", result: "", quote: "", video_url: "", verified: false, published: true, featured: false };

// Admin: the teacher's students who got the certificate. A card is shown on the home page only
// when "published" is on. "verified" means the owner has seen the proof (certificate / screenshot).
export default function TestimonialsPanel() {
  const [rows, reload] = useRows(() => supabase.from("testimonials").select("*").order("sort_order").order("created_at", { ascending: false }), []);
  const [f, setF] = useState(blank);
  const [photo, setPhoto] = useState(null);
  const [proof, setProof] = useState(null);
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState("");

  const upload = async (file) => {
    if (!file) return null;
    const ext = (file.name.split(".").pop() || "jpg").toLowerCase();
    const path = `${crypto.randomUUID()}.${ext}`;
    const { error } = await supabase.storage.from("testimonials").upload(path, file, { contentType: file.type });
    if (error) throw error;
    return path;
  };

  const add = async () => {
    if (!f.name.trim()) { setErr("Ism kiriting."); return; }
    if (!f.quote.trim() && !f.video_url.trim()) { setErr("Fikr matni yoki video havolasi kerak."); return; }
    setBusy(true); setErr("");
    try {
      const photo_path = await upload(photo), proof_path = await upload(proof);
      const { error } = await supabase.from("testimonials").insert({ ...f, name: f.name.trim(), photo_path, proof_path, sort_order: rows.length });
      if (error) throw error;
      setF(blank); setPhoto(null); setProof(null); reload();
    } catch (e) { setErr(writeErrorText(e)); }
    setBusy(false);
  };

  const patch = async (r, p) => { const { error } = await supabase.from("testimonials").update(p).eq("id", r.id); if (error) setErr(writeErrorText(error)); else reload(); };
  const del = async (r) => {
    if (!confirm(`"${r.name}" fikrini o'chirishni tasdiqlaysizmi?`)) return;
    const { error } = await supabase.from("testimonials").delete().eq("id", r.id);
    if (error) setErr(writeErrorText(error)); else reload();
  };
  const set = (k, v) => setF((p) => ({ ...p, [k]: v }));

  return (
    <div>
      <div style={pageTitle}>Fikrlar</div>
      <div style={pageSub}>Ustozning o'quvchilari fikri. Bosh sahifada faqat "ko'rsatilsin" yoqilganlari chiqadi. O'quvchining roziligi bilan qo'shing.</div>
      {err && <div style={errorBox}>{err}</div>}

      <div style={{ ...card, marginBottom: 16 }}>
        <div style={{ display: "grid", gap: 8 }}>
          <input style={inputStyle} placeholder="To'liq ism" value={f.name} onChange={(e) => set("name", e.target.value)} />
          <input style={inputStyle} placeholder="Natija (masalan: Milliy sertifikat 2025, kimyodan B2)" value={f.result} onChange={(e) => set("result", e.target.value)} />
          <textarea style={{ ...inputStyle, minHeight: 80, resize: "vertical" }} placeholder="Fikr matni" value={f.quote} onChange={(e) => set("quote", e.target.value)} />
          <input style={inputStyle} placeholder="Video havolasi (YouTube yoki boshqa), ixtiyoriy" value={f.video_url} onChange={(e) => set("video_url", e.target.value)} />
          <div style={{ display: "flex", gap: 10, flexWrap: "wrap", fontSize: 12.5, color: C.textMid }}>
            <label style={{ ...btnGhost, cursor: "pointer" }}><Upload size={13} /> {photo ? photo.name : "O'quvchi rasmi"}<input type="file" accept="image/*" hidden onChange={(e) => setPhoto(e.target.files?.[0] || null)} /></label>
            <label style={{ ...btnGhost, cursor: "pointer" }}><Upload size={13} /> {proof ? proof.name : "Sertifikat / skrinshot rasmi"}<input type="file" accept="image/*" hidden onChange={(e) => setProof(e.target.files?.[0] || null)} /></label>
          </div>
          <div style={{ display: "flex", gap: 16, flexWrap: "wrap", fontSize: 12.5, color: C.textMid }}>
            <label style={{ display: "flex", gap: 6, alignItems: "center", cursor: "pointer" }}><input type="checkbox" checked={f.verified} onChange={(e) => set("verified", e.target.checked)} /> Sertifikat ko'rilgan (tekshirilgan)</label>
            <label style={{ display: "flex", gap: 6, alignItems: "center", cursor: "pointer" }}><input type="checkbox" checked={f.published} onChange={(e) => set("published", e.target.checked)} /> Saytda ko'rsatilsin</label>
            <label style={{ display: "flex", gap: 6, alignItems: "center", cursor: "pointer" }}><input type="checkbox" checked={f.featured} onChange={(e) => set("featured", e.target.checked)} /> Bannerda ko'rsatilsin (eng yaxshi 2 tasi)</label>
          </div>
          <button style={{ ...btnPrimary, justifySelf: "start" }} disabled={busy} onClick={add}><Plus size={14} /> {busy ? "Yuklanmoqda…" : "Fikr qo'shish"}</button>
        </div>
      </div>

      {rows.length === 0 && <div style={{ fontSize: 13, color: C.textMid }}>Hali fikr qo'shilmagan. Fikr bo'lmasa, bosh sahifada bu bo'lim ko'rinmaydi.</div>}
      {rows.map((r) => (
        <div key={r.id} style={{ ...card, marginBottom: 10, display: "flex", gap: 12, alignItems: "center", opacity: r.published ? 1 : 0.6 }}>
          {r.photo_path ? <img src={testimonialUrl(r.photo_path)} alt="" style={{ width: 52, height: 52, borderRadius: "50%", objectFit: "cover" }} /> : <div style={{ width: 52, height: 52, borderRadius: "50%", background: C.bgSoft }} />}
          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ fontWeight: 800, fontSize: 14, color: C.text }}>{r.name} {r.verified && <BadgeCheck size={14} color="#15803D" style={{ verticalAlign: "-2px" }} />}</div>
            <div style={{ fontSize: 12, color: C.textMid }}>{r.result || "—"}{r.video_url ? " · video bor" : ""}{r.featured ? " · bannerda" : ""}{r.proof_path ? " · isbot rasmi bor" : ""}</div>
            <div style={{ fontSize: 12.5, color: C.text, marginTop: 3 }}>{(r.quote || "").slice(0, 140)}</div>
          </div>
          <button style={{ ...btnGhost, fontWeight: 700, color: r.featured ? C.primary : C.textLight }} title="Bosh sahifa bannerida ko'rsatish" onClick={() => patch(r, { featured: !r.featured })}>{r.featured ? "Bannerda" : "Banner"}</button>
          <button style={btnGhost} title="Tekshirilgan belgisi" onClick={() => patch(r, { verified: !r.verified })}><BadgeCheck size={14} color={r.verified ? "#15803D" : C.textLight} /></button>
          <button style={btnGhost} title={r.published ? "Yashirish" : "Ko'rsatish"} onClick={() => patch(r, { published: !r.published })}>{r.published ? <Eye size={14} /> : <EyeOff size={14} />}</button>
          <button style={{ ...btnGhost, color: C.danger }} onClick={() => del(r)}><Trash2 size={14} /></button>
        </div>
      ))}
    </div>
  );
}
