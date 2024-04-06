export default function cleanSet(set, startString) {
  if (typeof set !== Object || startString === '' ||
   typeof startString !== 'string') {
    return '';
  }
  const list_in = [];
  set.forEach(element => {
    if (element && element.startsWith(startString)) {
      list_in.push(element.replace(startString, ''));
    }    
  });
  return list_in.join('-');
}
