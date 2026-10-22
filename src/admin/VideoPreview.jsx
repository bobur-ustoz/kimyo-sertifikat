import { useEffect, useState } from "react";
import { supabase } from "../lib/supabaseClient";
import { C } from "./ui";

// Plays one Bunny video inside the admin so an uploaded file can be checked without
// leaving the page. The embed token comes from the same endpoint students use; the
// signed-in admin is let through even for paid variants.
export default function VideoPreview({ videoId }) {
  const [src, setSrc] = useState(null);
  const [err, setErr] = useState("");

  useEffect(() => {
    let off = false;
    setSrc(null); setErr("");
    (async () => {
      const { data: { session } } = await supabase.auth.getSession();
      const headers = { "Content-Type": "application/json" };
      if (session?.access_token) headers.Authorization = `Bearer ${session.access_token}`;
      try {
        const r = await fetch("/api/bunny-token", { method: "POST", headers, body: JSON.stringify({ videoId }) });
        const d = await r.json().catch(() => ({}));
        if (off) return;
        if (!r.ok) { setErr(d.error || "Video ochilmadi"); return; }
        setSrc(`https://iframe.mediadelivery.net/embed/${d.libraryId}/${videoId}?token=${d.token}&expires=${d.expires}`);
      } catch { if (!off) setErr("Video ochilmadi"); }
    })();
    return () => { off = true; };
  }, [videoId]);

  return (
    <div style={{ position:"relative", paddingTop:"56.25%", background:"#0F172A", borderRadius:10, overflow:"hidden", maxWidth:640 }}>
      {src ? (
        <iframe src={src} title="Video" style={{ position:"absolute", inset:0, width:"100%", height:"100%", border:"none" }}
          allow="accelerometer;gyroscope;autoplay;encrypted-media;picture-in-picture;" allowFullScreen/>
      ) : (
        <div style={{ position:"absolute", inset:0, display:"flex", alignItems:"center", justifyContent:"center", color:"#94A3B8", fontSize:12.5, padding:16, textAlign:"center" }}>
          {err || "Yuklanmoqda…"}
        </div>
      )}
    </div>
  );
}
