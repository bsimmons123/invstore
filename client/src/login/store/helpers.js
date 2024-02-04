export default class Helpers {
  static paths = {
    root: '/api',
    loginPath: '/user/v1/user/login',
    logoutPath: '/user/v1/user/logout',
    registerPath: '/user/v1/user/register',
    checkLogin() {
      return this.root + this.loginPath;
    },
    logout() {
      return this.root + this.logoutPath;
    },
    register() {
      return this.root + this.registerPath;
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
