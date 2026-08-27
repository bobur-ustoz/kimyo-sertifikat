import { Upload } from "tus-js-client";
import { supabase } from "../lib/supabaseClient";

// 20 MB pieces. tus-js-client defaults to sending the whole file in one
// request, which throws away the only thing tus is for: a dropped connection
// at 90% restarted from zero. With a finite chunk size only the piece in
// flight is lost.
const CHUNK_SIZE = 20 * 1024 * 1024;

// Sends one file straight from the browser to Bunny Stream and records the
// resulting video id on the question. The bytes never pass through our server;
// it only signs a short-lived upload authorisation after checking the caller is
// an admin. Resolves with the new video id.
export async function uploadQuestionVideo({ question, title, onProgress }) {
  const { data: { session } } = await supabase.auth.getSession();
  if (!session) throw new Error("Sessiya topilmadi. Qayta kiring.");

  const res = await fetch("/api/bunny-auth", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` },
    body: JSON.stringify({ title }),
  });
  const auth = await res.json();
  if (!res.ok) throw new Error(auth.error || "Yuklashga ruxsat olinmadi");

  const previousVideoId = question.bunny_video_id || null;

  await new Promise((resolve, reject) => {
    new Upload(question.file, {
      endpoint: "https://video.bunnycdn.com/tusupload",
      chunkSize: CHUNK_SIZE,
      retryDelays: [0, 3000, 5000, 10000, 20000],
      headers: {
        AuthorizationSignature: auth.authorizationSignature,
        AuthorizationExpire: String(auth.authorizationExpire),
        VideoId: auth.videoId,
        LibraryId: String(auth.libraryId),
      },
      metadata: { filetype: question.file.type, title },
      onError: reject,
      onProgress: (sent, total) => onProgress?.(Math.round((sent / total) * 100)),
      onSuccess: resolve,
    }).start();
  });

  const { error } = await supabase.from("questions")
    .update({ bunny_video_id: auth.videoId, video_ready: true })
    .eq("id", question.id);
  if (error) throw new Error(error.message);

  // The old video is now unreachable but still billed for. Replacing used to
  // leave it in the library forever; ask the server to drop it. A failure here
  // costs storage, not correctness, so it must not fail the upload.
  if (previousVideoId && previousVideoId !== auth.videoId) {
    fetch("/api/bunny-delete", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${session.access_token}` },
      body: JSON.stringify({ videoId: previousVideoId }),
    }).catch(() => {});
  }

  return auth.videoId;
}

// Names the video so the Bunny library is readable: without the teacher and
// variant every library entry was just "1-savol", dozens of times over.
export const videoTitle = (teacher, variant, question) =>
  `${teacher?.name || "?"} · ${variant?.variant_number}-variant · ${question.question_number}-savol`;
