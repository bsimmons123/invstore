import MessageTypes from "@/store/global-helpers/MessageTypes";
import UserLoginAdapter from "@/store/login/UserLoginAdapter";

export const StoreState = {
  isLoggedIn: 'isLoggedIn',
  message: 'message',
  showMessage: 'showMessage',
  messageType: 'messageType',
  alertDismissCountdown: 'alertDismissCountdown',
  user: 'user',
};

export default {
  isLoggedIn: localStorage.getItem('logged_in'),
  message: '',
  showMessage: false,
  messageType: MessageTypes,
  alertDismissCountdown: 0,
  user: new UserLoginAdapter(),
};
