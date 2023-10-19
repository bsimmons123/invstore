export default class CateringItemAdapter {
  constructor(adapter = {}) {
    this.id = adapter.id || 0;
    this.label = adapter.label || '';
    this.type_id = adapter.type_id || 0;
    this.list_id = adapter.list_id || 0;
  }
}
