export default function createInt8TypedArray(lenght, position, value) {
  const buf = new ArrayBuffer(lenght);
  const view = new DataView(buf);
  if (position > lenght - 1) {
	throw Error('Position outside range');
  }
  view.setInt8(position, value);
  return view;
}
