import Helpers from './helpers';

export default class CateringItem {
    id = null;

    name = null;

    type = Helpers.foodTypes;

    constructor(id, name, type) {
      this.id = id;
      this.name = name;
      this.type = type;
    }
}
