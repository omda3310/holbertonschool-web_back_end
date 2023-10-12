export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  /* getter size */
  get size() {
    return this._size;
  }

  /* setter size */
  set size(value) {
    this._size = value;
  }

  /* getter location */
  get location() {
    return this._location;
  }

  /* setter location */
  set location(value) {
    this._location = value;
  }

  valueOf() {
    return this.size;
  }

  toString() {
    return this.location;
  }
}
