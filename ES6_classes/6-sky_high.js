import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqrt, floors) {
    super(sqrt);
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
    return `Evacuate slowly ${this.floors} floors`;
  }
}
