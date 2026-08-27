import { useState } from "react";
import { uploadQuestionVideo } from "./uploadVideo";

// Single-row wrapper around the shared upload core, for the button on one
// question. The bulk uploader calls the same core directly.
export function useVideoUpload(question, title, onUploaded) {
  const [pct, setPct] = useState(null);
  const [error, setError] = useState("");

  const upload = async (file) => {
    setPct(0);
    setError("");
    try {
      const videoId = await uploadQuestionVideo({
        question: { ...question, file },
        title,
        onProgress: setPct,
      });
      setPct(null);
      onUploaded(videoId);
    } catch (e) {
      setError(e.message || "Yuklanmadi");
      setPct(null);
    }
  };

  return { pct, error, upload };
}
