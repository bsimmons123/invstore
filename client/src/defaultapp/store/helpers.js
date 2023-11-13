export default class Helpers {
  static paths = {
    root: '/api',
    loginPath: '/user/v1/user/login',
    checkLogin() {
      return this.root + this.loginPath;
    },
  };
}
