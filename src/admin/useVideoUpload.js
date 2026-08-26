import { useState } from "react";
import { Upload } from "tus-js-client";
import { supabase } from "../lib/supabaseClient";

// Uploads a file from the browser straight to Bunny Stream, then records the
// resulting video id on the question. The bytes never pass through our server:
// it only signs a short-lived upload authorisation, after checking the caller
// is an admin.
export function useVideoUpload(question, onUploaded) {
  const [pct, setPct] = useState(null);
  const [error, setError] = useState("");

  const upload = async (file) => {
    setPct(0);
    setError("");

    const title = `${question.question_number}-savol`;
    const { data: { session } } = await supabase.auth.getSession();
    const res = await fetch("/api/bunny-auth", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` },
      body: JSON.stringify({ title }),
    });
    const auth = await res.json();
    if (!res.ok) {
      setError(auth.error || "Yuklashda xatolik");
      setPct(null);
      return;
    }

    new Upload(file, {
      endpoint: "https://video.bunnycdn.com/tusupload",
      retryDelays: [0, 3000, 5000, 10000],
      headers: {
        AuthorizationSignature: auth.authorizationSignature,
        AuthorizationExpire: String(auth.authorizationExpire),
        VideoId: auth.videoId,
        LibraryId: String(auth.libraryId),
      },
      metadata: { filetype: file.type, title },
      onError: (err) => { setError(err.message); setPct(null); },
      onProgress: (sent, total) => setPct(Math.round((sent / total) * 100)),
      onSuccess: async () => {
        await supabase.from("questions")
          .update({ bunny_video_id: auth.videoId, video_ready: true })
          .eq("id", question.id);
        setPct(null);
        onUploaded(auth.videoId);
      },
    }).start();
  };

  return { pct, error, upload };
}
