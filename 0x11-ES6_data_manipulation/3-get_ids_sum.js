export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const reduc = (acc, item) => acc + item.id;

  const sum_id = students.reduce(reduc, 0);

  return sum_id;
}
