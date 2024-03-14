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
}
