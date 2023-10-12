export default class HolbertonCourse {
  constructor(name, length, students) {
    if (!(name instanceof String)) {
      TypeError: 'name must be a string';
    }
    if (!(length instanceof Number)) {
      TypeError: 'length must be a number';
    }
    if (!(students instanceof Array)) {
      TypeError: 'students must be an array of strings';
    }
    if (!students.every(std => !(std instanceof String))) {
      TypeError: 'students must be an array of strings';
    }

    this._name = name;
    this._lenght = length;
    this._students = students;
  }
  /* getter name */
  get name() {
    return this._name;
  }
  /* stter name */
  set name(value) {
    if (!(value instanceof String)) TypeError: 'name must be a string';
    this._name = value;
  }

  /* getter lenght */
  get length() {
    return this._lenght;
  }
  /* stter lenght */
  set length(value) {
    if (!(value instanceof Number)) TypeError: 'length must be a number';
    this._lenght = value;
  }

  /* getter students */
  get students() {
    return this._students;
  }
  /* setter students */
  set students(value) {
    if (!(value instanceof Array)) TypeError: 'students must be an array of numbers';
    if (!(value.every(std => std instanceof String))) TypeError: 'students must be an array of numbers';
    this._students = value;
  }
}
