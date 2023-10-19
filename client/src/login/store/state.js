import MessageTypes from '../../global-helpers/MessageTypes';

export const StoreState = {
  isLoggedIn: 'isLoggedIn',
  message: 'message',
  showMessage: 'showMessage',
  messageType: 'messageType',
  alertDismissCountdown: 'alertDismissCountdown',
};

export default {
  isLoggedIn: false,
  message: '',
  showMessage: false,
  messageType: MessageTypes,
  alertDismissCountdown: 0,
};
