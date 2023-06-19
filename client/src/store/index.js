import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import CateringItem from '@/store/model';
import { paths, messageTypes } from './helpers';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    items: [],
    message: '',
    showMessage: false,
    messageType: messageTypes,
    alertDismissCountdown: 0,
    editItem: new CateringItem(),
  },
  mutations: {
    setItems(state, payload) {
      state.items = payload;
    },
    addItem(state, payload) {
      state.items.push(payload);
    },
    deleteItem(state, payload) {
      const index = state.items.findIndex((item) => item.id === payload);
      if (index !== -1) {
        state.items.splice(index, 1);
      }
    },
    editItem(state, payload) {
      const { id, ...updatedItem } = payload;
      const index = state.items.findIndex((item) => item.id === id);
      state.items[index].name = updatedItem.payload.name;
      state.items[index].type = updatedItem.payload.type;
    },
    setMessage(state, payload) {
      state.message = payload;
    },
    toggleShowMessage(state, payload) {
      state.showMessage = payload;
    },
    setMessageType(state, payload) {
      state.messageType = payload;
    },
    setAlertDismissCountdown(state, payload) {
      state.alertDismissCountdown = payload;
    },
  },
  actions: {
    getAllItems(state) {
      axios.get(`${paths.items}`)
        .then((res) => {
          state.commit('setItems', res.data.items);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addItem(state, payload) {
      axios.post(`${paths.items}`, payload)
        .then((res) => {
          state.commit('addItem', payload);
          state.commit('setMessage', res.data.message);
          state.commit('setMessageType', messageTypes.success);
          state.commit('toggleShowMessage', true);
          state.commit('setAlertDismissCountdown', 5);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    editItem(state, payload) {
      // Destructure the id and rest of the properties into updatedItem
      const { id, ...updatedItem } = payload;
      axios.put(`${paths.getItemUrl(id)}`, updatedItem)
        .then((res) => {
          state.commit('editItem', payload);
          state.commit('setMessage', res.data.message);
          state.commit('setMessageType', messageTypes.success);
          state.commit('setAlertDismissCountdown', 5);
          state.commit('toggleShowMessage', true);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    deleteItem(state, payload) {
      axios.delete(paths.getItemUrl(payload))
        .then((res) => {
          state.commit('deleteItem', payload);
          state.commit('setMessage', res.data.message);
          state.commit('toggleShowMessage', true);
          state.commit('setAlertDismissCountdown', 5);
          state.commit('setMessageType', messageTypes.warning);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
});
