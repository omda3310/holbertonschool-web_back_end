export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  const lst = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      lst.push(element.replace(startString, ''));
    }
  });
  return lst.join('-');
}
