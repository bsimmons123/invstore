import { StoreState } from './state';

export const StoreMutations = {
  SET_ITEMS: 'SET_ITEMS',
  SET_ITEM_TYPES: 'SET_ITEM_TYPES',
  ADD_ITEM: 'ADD_ITEM',
  DELETE_ITEM: 'DELETE_ITEM',
  EDIT_ITEM: 'EDIT_ITEM',
  SET_MESSAGE: 'SET_MESSAGE',
  TOGGLE_SHOW_MESSAGE: 'TOGGLE_SHOW_MESSAGE',
  SET_MESSAGE_TYPE: 'SET_MESSAGE_TYPE',
  SET_ALERT_COUNTDOWN: 'SET_ALERT_COUNTDOWN',
  SET_EDIT_ITEM: 'SET_EDIT_ITEM',
  UPDATE_ADD_CATERING_LIST: 'UPDATE_ADD_CATERING_LIST',
  SET_CATERING_LIST: 'SET_CATERING_LIST',
  UPDATE_ADD_ITEM_FORM: 'UPDATE_ADD_ITEM_FORM',
  ADD_ITEM_TYPE: 'ADD_ITEM_TYPE'
};

export default {
  SET_ITEMS(state, payload) {
    state[StoreState.items] = payload;
  },
  ADD_ITEM(state, payload) {
    state[StoreState.items].push(payload);
  },
  DELETE_ITEM(state, payload) {
    const index = state[StoreState.items].findIndex((item) => item.id === payload);
    if (index !== -1) {
      state[StoreState.items].splice(index, 1);
    }
  },
  EDIT_ITEM(state, payload) {
    const { id, ...updatedItem } = payload;
    const index = state[StoreState.items].findIndex((item) => item.id === id);
    state[StoreState.items][index].name = updatedItem.payload.name;
    state[StoreState.items][index].type = updatedItem.payload.type;
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
  SET_EDIT_ITEM(state, payload) {
    state[StoreState.editItem] = payload;
  },
  UPDATE_ADD_CATERING_LIST(state, payload) {
    state[StoreState.addCateringList].label = payload
  },
  SET_CATERING_LIST(state, payload) {
    state[StoreState.cateringList] = payload
  },
  UPDATE_ADD_ITEM_FORM(state, obj) {
    state[StoreState.addItemForm][obj.key] = obj.value;
  },
  SET_ITEM_TYPES(state, value) {
    state[StoreState.itemTypes] = value;
  },
  ADD_ITEM_TYPE(state, payload) {
    state[StoreState.itemTypes].push(payload);
  }
};
