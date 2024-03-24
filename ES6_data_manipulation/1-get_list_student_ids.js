export default function getListStudentIds(menbres) {
  if (Array.isArray(menbres)) {
    return menbres.map((menbre) => menbre.id);
  } 
  return [];
}
