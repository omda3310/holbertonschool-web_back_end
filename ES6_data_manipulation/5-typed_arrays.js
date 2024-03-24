export default function createInt8TypedArray(lenght, position, value) {
  const buf = new ArrayBuffer(lenght);
  const view = new DataView(buf, 0, lenght);
  if (position > lenght - 1) {
	throw Error('Position outside range');
  }
  const array = new Int8Array(buf);
  array[position] = value;
  return view;
}
