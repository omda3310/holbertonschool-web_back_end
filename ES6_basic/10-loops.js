export default function appendToEachArrayValue(array, appendString) {
  const arrays = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    arrays[idx] = appendString + value;
  }

  return array;
}
