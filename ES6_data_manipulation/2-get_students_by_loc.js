export default function getStudentsByLocation (students, city) {
  if (Array.isArray(students)) {
	return students.filter((e) => e.location === city);
  }
  return [];
}
