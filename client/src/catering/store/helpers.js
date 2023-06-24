export default class Helpers {
  static paths = {
    root: '/api',
    items: '/items',
    getItems() {
      return this.root + this.items;
    },
    getItemUrl(id) {
      return `${this.root}/items/${id}`;
    },
  };

  static messageTypes = {
    warning: 'warning',
    primary: 'primary',
    danger: 'danger',
    success: 'success',
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
