export default class Currency {
  constructor(code, name) {

    // Objects
    this._code = code;
    this._name = name;
  }

  // Method
  displayFullCurrency() {
    return (`${this.name}  (${this.code})`);
  }

  // Setters
  set name(new_name) {
    this._name = new_name;
  }

  set code(new_code) {
    this._name = new_code;
  }

  // Getters
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
