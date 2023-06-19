import { foodTypes } from '@/store/helpers';

export default class CateringItem {
    id = null;

    name = null;

    type = foodTypes;

    constructor(id, name, type) {
      this.id = id;
      this.name = name;
      this.type = type;
    }
}
