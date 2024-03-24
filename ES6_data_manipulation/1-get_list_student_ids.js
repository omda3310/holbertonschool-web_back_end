export default function getListStudentIds(menbres) {
  if (!Array.isArray(menbres)) {
    return [];
  }
  return menbres.map((menbre) => menbre.id); 
}
