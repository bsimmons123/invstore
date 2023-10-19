import axios from 'axios';
import Helpers from './helpers';
import { StoreMutations } from './mutations';
import MessageTypes from '../../global-helpers/MessageTypes';

export const StoreActions = {
  login: 'login',
  check_login: 'check_login',
  logout: 'logout',
};

export default {
  login(state, loginParams) {
    axios.post(Helpers.paths.checkLogin(), loginParams)
      .then((res) => {
        localStorage.setItem('logged_in', true);
        state.commit(StoreMutations.SET_LOGGED_IN, true);
        state.commit(StoreMutations.SET_MESSAGE, res.data.message);
        state.commit(StoreMutations.TOGGLE_SHOW_MESSAGE, true);
        state.commit(StoreMutations.SET_ALERT_COUNTDOWN, 5);
        state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.success);
      })
      .catch((error) => {
        if (error.response && error.response.status === 401) {
          // Unauthorized error
          state.commit(StoreMutations.SET_MESSAGE, 'Invalid credentials. Please try again.');
          state.commit(StoreMutations.TOGGLE_SHOW_MESSAGE, true);
          state.commit(StoreMutations.SET_ALERT_COUNTDOWN, 5);
          state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.warning);
        } else {
          // Other errors
          console.error(error);
        }
      });
  },
  check_login(state) {
    return axios.get(Helpers.paths.checkLogin())
      .then((res) => {
        state.commit(StoreMutations.SET_LOGGED_IN, true);
        state.commit(StoreMutations.SET_MESSAGE, res.data.message);
        state.commit(StoreMutations.TOGGLE_SHOW_MESSAGE, true);
        state.commit(StoreMutations.SET_ALERT_COUNTDOWN, 5);
        state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.success);
      })
      .catch((error) => {
        if (error.response && error.response.status === 401) {
          // Unauthorized error
          state.commit(StoreMutations.SET_LOGGED_IN, false);
        } else if (error.response && error.response.status === 404) {
          state.commit(StoreMutations.SET_MESSAGE, 'User not found');
          state.commit(StoreMutations.TOGGLE_SHOW_MESSAGE, true);
          state.commit(StoreMutations.SET_ALERT_COUNTDOWN, 5);
          state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.warning);
        } else {
          // Other errors
          console.error(error);
        }
      });
  },
  logout(state) {
    return axios.get(Helpers.paths.logout())
      .then((res) => {
        localStorage.removeItem('logged_in');
        state.commit(StoreMutations.SET_LOGGED_IN, false);
        state.commit(StoreMutations.SET_MESSAGE, res.data.message);
        state.commit(StoreMutations.TOGGLE_SHOW_MESSAGE, true);
        state.commit(StoreMutations.SET_ALERT_COUNTDOWN, 5);
        state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.primary);
      })
      .catch((error) => {
        // Other errors
        state.commit(StoreMutations.SET_LOGGED_IN, false);
        console.error(error);
      });
  },
};
