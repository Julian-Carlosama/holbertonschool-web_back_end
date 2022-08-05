import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {

    // Objects
    this._amount = amount;
    this._currency = currency;
  }

  // Methods
  displayFullPrice() {
    return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  // Setters
  set amount(new_amount) {
    this._amount = new_amount;
  }

  set currency(new_current) {
    if (!(new_current instanceof Currency)) throw TypeError('Currency must be an instance of currency');
    this._currency = new_current;
  }

  // Getters
  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }
}
