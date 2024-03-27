export default function calculateNumber(a, b) {
  if (Number.isNaN(a) || Number.isNaN(b)) {
    throw Error("a and b must be numbers");
  }
  return Math.round(a) + Math.round(b);
}
