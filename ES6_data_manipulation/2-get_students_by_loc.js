export default function getStudentsByLocation(students, city) {
  if (Array.isArray(students)) {
    return students.filter((s) => s.location === city)
  }
  return [];
}
