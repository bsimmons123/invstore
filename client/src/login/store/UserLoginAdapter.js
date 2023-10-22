export default class UserLoginAdapter {
  constructor(adapter = {}) {
    this.username = adapter.username || '';
    this.email = adapter.email || '';
    this.password = adapter.password || '';
  }
}
