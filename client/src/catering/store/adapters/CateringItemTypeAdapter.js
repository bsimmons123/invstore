export default class CateringItemTypeAdapter {
  constructor(adapter = {}) {
    this.id = adapter.id || 0;
    this.label = adapter.label || '';
  }
}
