import MessageTypes from '../../global-helpers/MessageTypes';
import CateringListAdapter from "./adapters/CateringListAdapter";
import CateringItemAdapter from "./adapters/CateringItemAdapter";
import CateringItemTypeAdapter from "./adapters/CateringItemTypeAdapter";

export const StoreState = {
  items: 'items',
  message: 'message',
  showMessage: 'showMessage',
  messageType: 'messageType',
  alertDismissCountdown: 'alertDismissCountdown',
  editItem: 'editItem',
  addItemForm: 'addItemForm',
  addCateringList: 'addCateringList',
  cateringList: 'cateringList',
  itemTypes: 'itemTypes'
};

export default {
  items: [],
  message: '',
  showMessage: false,
  messageType: MessageTypes,
  alertDismissCountdown: 0,
  editItem: new CateringItemAdapter(),
  addCateringList: new CateringListAdapter(),
  cateringList: [new CateringListAdapter()],
  addItemForm: new CateringItemAdapter(),
  itemTypes: new CateringItemTypeAdapter()
};
