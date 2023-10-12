export default class HolbertonCourse {
    constructor(name, length, students) {
      if (typeof name !== 'string') {
        throw new TypeError('name must be a string');
      }
      if (typeof length !== 'number') {
        throw new TypeError('length must be a number');
      }
      if (!Array.isArray(students)) {
        throw new TypeError('students must be an array');
      }
      if (!students.every(std => typeof std === 'string')) {
        throw new TypeError('students must be an array of strings');
      }
      this._name = name;
      this._length = length;
      this._students = students;
    }
    
    /* getter name */
    get name() {
      return this._name;
    }
    
    /* setter name */
    set name(value) {
      if (typeof value !== 'string') {
        throw TypeError('name must be a string');
      }
      this._name = value;
    }
    
    /* getter length */
    get length() {
      return this._length;
    }
    
    /* setter length */
    set length(value) {
      if (typeof value !== 'number') {
        throw new TypeError('length must be a number');
      }
      this._length = value;
    }
    
    /* getter students */
    get students() {
      return this._students;
    }
    
    /* setter students */
    set students(value) {
      if (!Array.isArray(value)) {
        throw new TypeError('students must be an array');
      }
      if (!value.every(std => typeof std === 'string')) {
        throw new TypeError('students must be an array of strings');
      }
      this._students = value;
    }
}

