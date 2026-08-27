// Pulls the question number out of whatever the file happens to be called:
// "1.mp4", "01.mp4", "1-savol.mp4", "savol_1.mp4", "Variant2 - 15.mov".
// The last number in the name wins, since a leading one is usually the variant.
export function questionNumberFromFilename(name) {
  const stem = String(name).replace(/\.[^.]+$/, "");
  const numbers = stem.match(/\d+/g);
  if (!numbers) return null;
  const n = parseInt(numbers[numbers.length - 1], 10);
  return Number.isFinite(n) && n > 0 ? n : null;
}
