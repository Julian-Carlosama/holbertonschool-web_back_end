export default class Currency {
  constructor(code, name) {
    // Objects
    this._code = code;
    this._name = name;
  }

  // Method
  displayFullCurrency() {
    return `${this.name}  (${this.code})`;
  }

  // Setters
  set name(new_name) {
    if (typeof new_name === 'string') this._name = new_name;
  }

  set code(new_code) {
    if (typeof new_code === 'string') this._code = new_code;
  }

  // Getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
