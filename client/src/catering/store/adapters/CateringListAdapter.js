export default class CateringListAdapter {
  constructor(adapter = {}) {
    this.id = adapter.email || '';
    this.label = adapter.password || '';
    this.user_id = adapter.user_id || 0;
    this.catering_items = adapter.catering_items || [];
  }
}
