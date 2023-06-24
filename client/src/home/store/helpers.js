export default class Helpers {
  static paths = {
    root: '/api',
    home: '/home',
    getItems() {
      return this.root + this.home;
    },
    getItemUrl(id) {
      return `${this.root}/${this.home}/${id}`;
    },
  };
}
