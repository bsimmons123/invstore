export default class Helpers {
  static paths = {
    root: '/api',
    loginPath: '/user/v1/user/login',
    logoutPath: '/user/v1/user/logout',
    checkLogin() {
      return this.root + this.loginPath;
    },
    logout() {
      return this.root + this.logoutPath;
    },
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
