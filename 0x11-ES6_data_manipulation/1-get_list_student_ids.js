export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  
  const id_list = students.map((item) => item.id);
  
  return id_list;
}
