export default class Currency {
  constructor(code, name) {
    if (typeof code !== String) throw TypeError('code must be a string');
    this._code = code;
    if (typeof name !== String) throw TypeError('name must be a string');
    this._name = name;
  }

  /* getter code */
  get code() {
    return this._name;
  }
  /* stter code */
  set code(value) {
    if (typeof value !== String) throw TypeError('code must be a string');
    this._code = value;
  }

  /* getter name */
  get name() {
    return this._name;
  }
  /* setter name */
  set name(value) {
    if (typeof value !== String) throw TypeError('name must be a string');
    this._name = value
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}