import { StoreState } from './state';

export const StoreMutations = {
  SET_LOGGED_IN: 'SET_LOGGED_IN',
  SET_MESSAGE: 'SET_MESSAGE',
  TOGGLE_SHOW_MESSAGE: 'TOGGLE_SHOW_MESSAGE',
  SET_MESSAGE_TYPE: 'SET_MESSAGE_TYPE',
  SET_ALERT_COUNTDOWN: 'SET_ALERT_COUNTDOWN',
  SET_EMAIL: 'SET_EMAIL',
  SET_PASSWORD: 'SET_PASSWORD',
  SET_NAME: 'SET_NAME'
};

export default {
  SET_LOGGED_IN(state, payload) {
    if (payload === false)
      localStorage.removeItem('logged_in');
    else
      localStorage.setItem('logged_in', true);
    state[StoreState.isLoggedIn] = payload;
  },
  SET_MESSAGE(state, payload) {
    state[StoreState.message] = payload;
  },
  TOGGLE_SHOW_MESSAGE(state, payload) {
    state[StoreState.showMessage] = payload;
  },
  SET_MESSAGE_TYPE(state, payload) {
    state[StoreState.messageType] = payload;
  },
  SET_ALERT_COUNTDOWN(state, payload) {
    state[StoreState.alertDismissCountdown] = payload;
  },
  SET_EMAIL(state, payload) {
    state[StoreState.user].email = payload;
  },
  SET_PASSWORD(state, payload) {
    state[StoreState.user].password = payload
  },
  SET_NAME(state, payload) {
    state[StoreState.user].username = payload
  }
};
