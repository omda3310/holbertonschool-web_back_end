export default function createInt8TypedArray(length, position, value) {
  const buf = new ArrayBuffer(length);
  const view = new DataView(buf, 0);
  if (position >= length) {
    throw Error('Position outside range');
  }
  view.setInt8(value, position);
  return view;
}
