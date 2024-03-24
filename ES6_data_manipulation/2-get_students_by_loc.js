export default function getStudentsByLocation (students, city) {
  return students.filter((e) => e.location === city);
}
