export default class HolbertonCourse {
  constructor(name, length, students) {
    // name
    if (Object.getPrototypeOf(name) !== String.prototype) throw TypeError('name must be a string');
    if (Object.getPrototypeOf(length) !== Number.prototype) throw TypeError('length must be a number');
    if (Object.getPrototypeOf(students) !== Array.prototype) throw TypeError('students must be an array of strings');
    students.forEach((student) => {
      if (Object.getPrototypeOf(student) !== String.prototype) throw TypeError('students must be an array of strings');
    });

    // Objects
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Setters
  set name(new_name) {
    if (Object.getPrototypeOf(new_name) !== String.prototype) throw TypeError('Name must be a string');
    this._name = new_name;
  }

  set length(new_length) {
    if (Object.getPrototypeOf(new_length) !== Number.prototype) throw TypeError('Length must be a number');
    this._length = new_length;
  }

  set students(new_students) {
    if (Object.getPrototypeOf(new_students) !== Array.prototype) throw TypeError('Students must be an array');
    new_students.forEach((student) => {
      if (Object.getPrototypeOf(student) !== String.prototype) throw TypeError('Students must be an array of strings');
    });
    this._students = new_students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }
}
