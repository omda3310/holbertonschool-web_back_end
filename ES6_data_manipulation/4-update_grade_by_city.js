export default function updateStudentGradeByCity(students, city, newGrades) {
  const SG = students.filter((student) => student.location === city);

  const SGed = SG.map((student) => {
	const GFilter = newGrades.filter(
	  (newGrade) => newGrade.studentId === student.id);

	  let grade;

	  if (GFilter[0]) {
		grade = GFilter[0].grade;
	  } else {
		grade = 'N/A';
	  }

	  return {
		...student,
		grade,
	  };
	});

  return SGed;
}
