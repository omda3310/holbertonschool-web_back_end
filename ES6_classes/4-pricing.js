import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  /* getter amount */
  get amount() {
    return this._amount;
  }
  /* setter amount */
  set amount(value) {
    this._amount = this.amount;
  }

  /* getter currency */
  get currency() {
    return this._currency;
  }
  /* stter currency */
  set currency(value) {
    this._currency = this.currency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }
  convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}