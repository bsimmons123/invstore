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
    SET_ITEMS(state, payload) {
      state.items = payload;
    },
    ADD_ITEM(state, payload) {
      state.items.push(payload);
    },
    DELETE_ITEM(state, payload) {
      const index = state.items.findIndex((item) => item.id === payload);
      if (index !== -1) {
        state.items.splice(index, 1);
      }
    },
    EDIT_ITEM(state, payload) {
      const { id, ...updatedItem } = payload;
      const index = state.items.findIndex((item) => item.id === id);
      state.items[index].name = updatedItem.payload.name;
      state.items[index].type = updatedItem.payload.type;
    },
    SET_MESSAGE(state, payload) {
      state.message = payload;
    },
    TOGGLE_SHOW_MESSAGE(state, payload) {
      state.showMessage = payload;
    },
    SET_MESSAGE_TYPE(state, payload) {
      state.messageType = payload;
    },
    SET_ALERT_COUNTDOWN(state, payload) {
      state.alertDismissCountdown = payload;
    },
  },
  actions: {
    getAllItems(state) {
      axios.get(`${paths.items}`)
        .then((res) => {
          state.commit('SET_ITEMS', res.data.items);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addItem(state, payload) {
      axios.post(`${paths.items}`, payload)
        .then((res) => {
          state.commit('ADD_ITEM', res.data.obj);
          state.commit('SET_MESSAGE', res.data.message);
          state.commit('SET_MESSAGE_TYPE', messageTypes.success);
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
      axios.put(`${paths.getItemUrl(id)}`, updatedItem)
        .then((res) => {
          state.commit('EDIT_ITEM', payload);
          state.commit('SET_MESSAGE', res.data.message);
          state.commit('SET_MESSAGE_TYPE', messageTypes.success);
          state.commit('SET_ALERT_COUNTDOWN', 5);
          state.commit('TOGGLE_SHOW_MESSAGE', true);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    deleteItem(state, payload) {
      axios.delete(paths.getItemUrl(payload))
        .then((res) => {
          state.commit('DELETE_ITEM', payload);
          state.commit('SET_MESSAGE', res.data.message);
          state.commit('TOGGLE_SHOW_MESSAGE', true);
          state.commit('SET_ALERT_COUNTDOWN', 5);
          state.commit('SET_MESSAGE_TYPE', messageTypes.warning);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
});
