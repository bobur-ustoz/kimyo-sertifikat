import { useRef, useState } from "react";
import { UploadCloud, CheckCircle2, X } from "lucide-react";
import { uploadQuestionVideo, videoTitle } from "./uploadVideo";
import { questionNumberFromFilename } from "./filename";
import { C, card, btnPrimary, btnGhost, hint, errorBox } from "./ui";

// Uploading 43 videos one row at a time is most of the work of filling a
// variant. Here the whole folder goes in at once: each file is matched to a
// question by the number in its name, then they upload one after another so a
// home connection is not split 43 ways.
export default function BulkUpload({ teacher, variant, questions, onDone }) {
  const fileRef = useRef(null);
  const [queue, setQueue] = useState([]);      // [{file, number, question, status, pct, error}]
  const [running, setRunning] = useState(false);
  const [err, setErr] = useState("");

  const pick = (files) => {
    setErr("");
    const items = Array.from(files).map(file => {
      const number = questionNumberFromFilename(file.name);
      const question = number ? questions.find(q => q.question_number === number) : null;
      return {
        file, number, question,
        status: question ? "kutmoqda" : "topilmadi",
        pct: 0, error: "",
      };
    }).sort((a, b) => (a.number ?? 1e9) - (b.number ?? 1e9));
    setQueue(items);
  };

  const start = async () => {
    setRunning(true);
    setErr("");
    for (let i = 0; i < queue.length; i++) {
      const item = queue[i];
      if (!item.question || item.status === "tayyor") continue;

      const patch = (fields) => setQueue(prev => prev.map((x, xi) => xi === i ? { ...x, ...fields } : x));
      patch({ status: "yuklanmoqda", pct: 0, error: "" });
      try {
        await uploadQuestionVideo({
          question: { ...item.question, file: item.file },
          title: videoTitle(teacher, variant, item.question),
          onProgress: (pct) => patch({ pct }),
        });
        patch({ status: "tayyor", pct: 100 });
      } catch (e) {
        patch({ status: "xato", error: e.message || "Yuklanmadi" });
      }
    }
    setRunning(false);
    onDone();
  };

  const matched = queue.filter(q => q.question).length;
  const done = queue.filter(q => q.status === "tayyor").length;
  const failed = queue.filter(q => q.status === "xato").length;

  const badge = (item) => {
    if (item.status === "tayyor") return { bg:C.mintBg, fg:C.primary, text:"✓ tayyor" };
    if (item.status === "xato") return { bg:"#FEF2F2", fg:C.danger, text:"xato" };
    if (item.status === "topilmadi") return { bg:"#FFFBEB", fg:"#B45309", text:"savol topilmadi" };
    if (item.status === "yuklanmoqda") return { bg:"#EFF6FF", fg:"#1E40AF", text:`${item.pct}%` };
    return { bg:"#F1F5F9", fg:C.textMid, text:"navbatda" };
  };

  return (
    <div style={{ ...card, marginBottom:14, background:C.mintBg }}>
      <div style={{display:"flex",alignItems:"center",justifyContent:"space-between",gap:10,flexWrap:"wrap",marginBottom: queue.length ? 12 : 0}}>
        <div>
          <div style={{fontWeight:800,fontSize:13.5,color:C.text}}>Ommaviy video yuklash</div>
          <div style={{ ...hint, marginTop:3 }}>
            Fayl nomidagi raqam savol raqamiga mos keladi — <code>1.mp4</code>, <code>1-savol.mp4</code>, <code>savol_1.mp4</code> hammasi ishlaydi.
          </div>
        </div>
        <input ref={fileRef} type="file" accept="video/*" multiple style={{display:"none"}}
          onChange={e => { if (e.target.files?.length) pick(e.target.files); e.target.value = ""; }}/>
        <button style={btnPrimary} disabled={running} onClick={() => fileRef.current?.click()}>
          <UploadCloud size={14}/> Videolarni tanlash
        </button>
      </div>

      {err && <div style={errorBox}>{err}</div>}

      {queue.length > 0 && (<>
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:10,flexWrap:"wrap"}}>
          <span style={{fontSize:12.5,color:C.textMid}}>
            {queue.length} ta fayl · {matched} tasi savolga mos keldi
            {done ? ` · ${done} yuklandi` : ""}{failed ? ` · ${failed} xato` : ""}
          </span>
          {!running && matched > 0 && (
            <button style={btnPrimary} onClick={start}>
              <UploadCloud size={13}/> {done ? "Qolganini yuklash" : `${matched} ta videoni yuklash`}
            </button>
          )}
          {running && <span style={{fontSize:12.5,fontWeight:700,color:C.primary}}>Yuklanmoqda… sahifani yopmang</span>}
          {!running && (
            <button style={btnGhost} onClick={() => setQueue([])}><X size={12}/> Ro'yxatni tozalash</button>
          )}
        </div>

        <div style={{background:"#fff",border:`1px solid ${C.border}`,borderRadius:9,maxHeight:280,overflowY:"auto"}}>
          {queue.map((item, i) => {
            const b = badge(item);
            return (
              <div key={i} style={{display:"flex",alignItems:"center",gap:10,padding:"7px 11px",borderBottom: i < queue.length-1 ? `1px solid ${C.border}` : "none"}}>
                <div style={{width:58,flexShrink:0,fontSize:11.5,fontWeight:800,color: item.question ? C.text : C.textLight}}>
                  {item.number ? `${item.number}-savol` : "—"}
                </div>
                <div style={{flex:1,minWidth:0,fontSize:11.5,color:C.textMid,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>
                  {item.file.name}
                </div>
                {item.error && <div style={{fontSize:10.5,color:C.danger,maxWidth:200,textAlign:"right"}}>{item.error}</div>}
                <span style={{fontSize:10.5,fontWeight:800,padding:"3px 9px",borderRadius:20,background:b.bg,color:b.fg,flexShrink:0}}>{b.text}</span>
              </div>
            );
          })}
        </div>

        {queue.some(q => q.status === "topilmadi") && (
          <p style={{ ...hint, marginTop:8 }}>
            "savol topilmadi" — fayl nomidagi raqam bu variantdagi savol raqamlariga mos kelmadi. Nomini o'zgartirib qayta tanlang.
          </p>
        )}
        {done > 0 && !running && (
          <p style={{fontSize:12,color:C.primary,fontWeight:700,marginTop:8,display:"flex",alignItems:"center",gap:6}}>
            <CheckCircle2 size={13}/> {done} ta video yuklandi.
          </p>
        )}
      </>)}
    </div>
  );
}
