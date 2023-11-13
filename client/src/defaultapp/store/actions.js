import axios from 'axios';
import Helpers from './helpers';
import { StoreMutations } from './mutations';
import MessageTypes from '../../global-helpers/MessageTypes';

export const StoreActions = {
  check_login: 'check_login'
};

export default {
  check_login(state) {
    return axios.get(Helpers.paths.checkLogin())
      .then((res) => {
        state.commit(StoreMutations.SET_LOGGED_IN, true);
        localStorage.setItem("user", JSON.stringify(res.data.user))
        state.commit(StoreMutations.SET_MESSAGE, res.data.message);
        state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.success);
      })
      .catch((error) => {
        if (error.response && error.response.status === 401) {
          // Unauthorized error
          localStorage.clear();
          state.commit(StoreMutations.SET_LOGGED_IN, false);
        } else if (error.response && error.response.status === 404) {
          state.commit(StoreMutations.SET_MESSAGE, 'User not found');
          state.commit(StoreMutations.SET_MESSAGE_TYPE, MessageTypes.warning);
        } else {
          // Other errors
          console.error(error);
        }
      });
  }
};
