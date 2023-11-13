import MessageTypes from '../../global-helpers/MessageTypes';
import * as LocalStorage from "vue";

export const StoreState = {
  isLoggedIn: 'isLoggedIn',
  message: 'message',
  showMessage: 'showMessage',
  messageType: 'messageType',
  alertDismissCountdown: 'alertDismissCountdown',
};

export default {
  isLoggedIn: JSON.parse(localStorage.getItem('user')) || false,
  message: '',
  showMessage: false,
  messageType: MessageTypes,
  alertDismissCountdown: 0,
};
