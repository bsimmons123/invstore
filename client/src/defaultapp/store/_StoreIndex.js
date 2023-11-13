import state from './state';
import mutations from './mutations';
import actions from './actions';
import getters from './getters';

const storeName = 'default/store';

export default {
  state,
  actions,
  getters,
  mutations,
  storeName,
};
