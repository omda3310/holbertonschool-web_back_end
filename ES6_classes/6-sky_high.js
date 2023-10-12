import Building from "./5-building";

export default class SkyHighBuilding {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  /* getter floors */
  get floors() {
    return this._floors;
  }

  /* setter floors */
  set floors(value) {
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly ${this.sqft} floors`;
  }
}