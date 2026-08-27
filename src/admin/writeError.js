// Every write in this panel used to ignore its error, so a rejected insert
// looked exactly like a working button that did nothing. These are the failures
// an admin can actually act on, in words that say what to do next.
export function writeErrorText(error) {
  if (!error) return "";
  const msg = error.message || "";

  if (error.code === "23505") return "Bu raqam allaqachon mavjud — boshqa raqam kiriting.";
  if (error.code === "23503") return "Bog'langan yozuv topilmadi. Sahifani yangilab qayta urining.";
  if (error.code === "23514") return "Kiritilgan qiymat qoidaga to'g'ri kelmadi.";
  if (error.code === "42501" || /row-level security/i.test(msg)) {
    return "Ruxsat yo'q. Admin hisobingizdan chiqib, qaytadan kiring.";
  }
  if (error.code === "42703" || error.code === "42P01") {
    return "Bazada kerakli ustun yoki jadval yo'q — migratsiya to'liq ishga tushmagan.";
  }
  if (/failed to fetch|load failed|networkerror|fetch failed/i.test(msg)) {
    return "Server javob bermadi. Baza vaqtincha to'xtatilgan bo'lishi mumkin.";
  }
  return msg || "Saqlanmadi. Birozdan keyin qayta urinib ko'ring.";
}
