import axios from 'axios';
import Helpers from './helpers';
import MessageTypes from '../../global-helpers/MessageTypes';
import {StoreMutations} from "./mutations";

export const StoreActions = {
  getAllItems: 'getAllItems',
  addItem: 'addItem',
  editItem: 'editItem',
  deleteItem: 'deleteItem',
  addNewCateringList: 'addNewCateringList',
  getCateringLists: 'getCateringLists'
};

export default {
  getAllItems(state, listId) {
    axios.get(`${Helpers.paths.getItems()}`, { params: { listId: listId } })
      .then((res) => {
        state.commit(StoreMutations.SET_ITEMS, res.data.items);
        state.commit(StoreMutations.SET_ITEM_TYPES, res.data.types)
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  addItem(state, payload) {
    axios.post(`${Helpers.paths.getItems()}`, payload)
      .then((res) => {
        state.commit('ADD_ITEM', res.data.obj);
        state.commit('SET_MESSAGE', res.data.message);
        state.commit('SET_MESSAGE_TYPE', MessageTypes.success);
        state.commit('TOGGLE_SHOW_MESSAGE', true);
        state.commit('SET_ALERT_COUNTDOWN', 5);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
  },
  editItem(state, payload) {
    // Destructure the id and rest of the properties into updatedItem
    const { id, ...updatedItem } = payload;
    axios.put(`${Helpers.paths.getItemUrl(id)}`, updatedItem.payload)
      .then((res) => {
        state.commit('EDIT_ITEM', payload);
        state.commit('SET_MESSAGE', res.data.message);
        state.commit('SET_MESSAGE_TYPE', MessageTypes.success);
        state.commit('SET_ALERT_COUNTDOWN', 5);
        state.commit('TOGGLE_SHOW_MESSAGE', true);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  deleteItem(state, payload) {
    axios.delete(Helpers.paths.getItemUrl(payload))
      .then((res) => {
        state.commit('DELETE_ITEM', payload);
        state.commit('SET_MESSAGE', res.data.message);
        state.commit('TOGGLE_SHOW_MESSAGE', true);
        state.commit('SET_ALERT_COUNTDOWN', 5);
        state.commit('SET_MESSAGE_TYPE', MessageTypes.warning);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  addNewCateringList(state, cateringList) {
    axios.post(`${Helpers.paths.getCateringList()}`, cateringList)
      .then((res) => {
        state.commit('ADD_ITEM', res.data.obj);
        state.commit('SET_MESSAGE', res.data.message);
        state.commit('SET_MESSAGE_TYPE', MessageTypes.success);
        state.commit('TOGGLE_SHOW_MESSAGE', true);
        state.commit('SET_ALERT_COUNTDOWN', 5);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
  },
  getCateringLists(state) {
    axios.get(`${Helpers.paths.getCateringList()}`)
      .then((res) => {
        state.commit(StoreMutations.SET_CATERING_LIST, res.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }
};
