import { StoreState } from './state';

export const StoreMutations = {
  SET_LOGGED_IN: 'SET_LOGGED_IN',
  SET_MESSAGE: 'SET_MESSAGE',
  TOGGLE_SHOW_MESSAGE: 'TOGGLE_SHOW_MESSAGE',
  SET_MESSAGE_TYPE: 'SET_MESSAGE_TYPE',
  SET_ALERT_COUNTDOWN: 'SET_ALERT_COUNTDOWN',
};

export default {
  SET_LOGGED_IN(state, payload) {
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
};
