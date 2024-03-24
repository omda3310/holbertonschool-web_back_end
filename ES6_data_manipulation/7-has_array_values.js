export default function hasValuesFromArray(set, array) {
  return array.every((elt) => set.has(elt));
}
