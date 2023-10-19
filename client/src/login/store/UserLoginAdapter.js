export default class UserLoginAdapter {
  constructor(adapter = {}) {
    this.email = adapter.email || '';
    this.password = adapter.password || '';
  }
}
