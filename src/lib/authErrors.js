// Supabase answers in English, and every failure used to be reported as
// "Email yoki parol noto'g'ri" -- including the case that matters most, a
// paused or unreachable project, where the password was never even checked.

const unreachable = (err) =>
  err?.status === 0 ||
  err?.name === "AuthRetryableFetchError" ||
  /failed to fetch|networkerror|load failed|fetch failed/i.test(err?.message || "");

export function signInErrorText(err) {
  if (unreachable(err)) {
    return "Server javob bermadi. Baza vaqtincha to'xtatilgan bo'lishi mumkin — Supabase'da loyihani qayta ishga tushiring.";
  }
  const msg = err?.message || "";
  if (/invalid login credentials/i.test(msg)) return "Email yoki parol noto'g'ri.";
  if (/email not confirmed/i.test(msg)) return "Email hali tasdiqlanmagan. Pochtangizdagi tasdiqlash xatini oching.";
  if (/after (\d+) seconds?/i.test(msg)) {
    return `Juda ko'p urinish bo'ldi. ${msg.match(/after (\d+) seconds?/i)[1]} soniyadan keyin qayta urinib ko'ring.`;
  }
  return msg || "Kirib bo'lmadi. Birozdan keyin urinib ko'ring.";
}

export function resetErrorText(err) {
  if (unreachable(err)) {
    return "Server javob bermadi. Baza vaqtincha to'xtatilgan bo'lishi mumkin — Supabase'da loyihani qayta ishga tushiring.";
  }
  const msg = err?.message || "";
  if (/after (\d+) seconds?/i.test(msg)) {
    return `Juda tez-tez so'radingiz. ${msg.match(/after (\d+) seconds?/i)[1]} soniyadan keyin qayta urinib ko'ring.`;
  }
  if (/rate limit/i.test(msg)) return "Bugun juda ko'p xat yuborildi. Bir soatdan keyin urinib ko'ring.";
  if (/invalid/i.test(msg) && /email/i.test(msg)) return "Email manzil noto'g'ri yozilgan.";
  return msg || "Xat yuborilmadi. Birozdan keyin urinib ko'ring.";
}
