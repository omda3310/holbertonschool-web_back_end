export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  const list = [];
  set.forEach(element => {
    if(element && element.startsWith(startString)) {
      list.push(element.replace(startString, ''));
    }    
  });
  return list.join('-');
}
