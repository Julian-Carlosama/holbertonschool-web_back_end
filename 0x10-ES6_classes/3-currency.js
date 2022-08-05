export default class Currency {
  constructor(code, name) {
    // Objects
    this.code = code;
    this.name = name;
  }

  // Method
  displayFullCurrency() {
    return `${this.name}  (${this.code})`;
  }

  // Setters
  set name(name) {
    if (typeof name === 'string') this._name = name;
  }

  set code(code) {
    if (typeof code === 'string') this._code = code;
  }

  // Getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
