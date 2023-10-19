export default class Helpers {
  static paths = {
    root: '/api',
    items: '/catering/v1/catering/items',
    cateringList: '/catering/v1/catering/catering_list',
    getItems() {
      return this.root + this.items;
    },
    getItemUrl(id) {
      return `${this.root}/${this.items}/${id}`;
    },
    getCateringList() {
      return this.root + this.cateringList;
    }
  };

  static foodTypes = {
    sweet: 'Sweet',
    sour: 'Sour',
    american: 'American',
    seafood: 'SeaFood',
    italian: 'Italian',
    french: 'French',
    chinese: 'Chinese',
    dessert: 'Dessert',
    thai: 'Thai',
  };
}
