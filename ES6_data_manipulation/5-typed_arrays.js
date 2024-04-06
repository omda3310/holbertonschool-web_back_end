export default function createInt8TypedArray(lenght, position, value) {
  const buf = new ArrayBuffer(lenght);
  const view = new Int8Array(buf, 0);
  if (position > lenght - 1) {
    throw Error('Position outside range');
  }
  view.set(position, value);
  return view;
}
