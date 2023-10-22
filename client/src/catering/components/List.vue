<template>
  <div class="container">
    <alert
      :message=getMessage
      :message-type="getMessageType"
      :dismiss-count-down="getAlertCountdown"
      v-if="showMessage"
      @dismiss="dismissAlert"
      @updateCountdown="updateDismissAlert"
    />
    <button type="button" class="btn btn-success btn-sm" v-b-modal.add-modal>Add Item</button>
    <b-button class="btn btn-secondary btn-sm" v-b-toggle.sidebar-right>Add Type</b-button>
    <br><br>
    <view-item
      :items="getItems"
      @populateEditItem="updateEditItem"
      @populateIdDelete="onDeleteItem"
    />
    <add-item
      :list-id="this.listId"
    />
    <edit-item
      :item="editItem"
      @itemNameChange="updateItemNameEdit"
      @itemTypeChange="itemTypeChangeEdit"
      @onEdit="onSubmitUpdate"
      @onEditReset="onResetUpdate"
    />
    <add-catering-item-type/>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex';
import EditItem from './EditItem.vue';
import AddItem from './AddItem.vue';
import ViewItem from './ViewItem.vue';
import Alert from '../../global-componets/Alert.vue';
import StoreIndex from '../store/_StoreIndex';
import { StoreMutations } from '../store/mutations';
import { StoreState } from '../store/state';
import { StoreActions } from '../store/actions';
import CateringItemAdapter from "../store/adapters/CateringItemAdapter";
import AddCateringItemType from "@/catering/components/AddCateringItemType.vue";

export default {
  name: 'CateringList',
  data() {
    return {
      editItemForm: new CateringItemAdapter(),
      message: '',
    };
  },
  props: ['listId'],
  components: {
    AddCateringItemType,
    ViewItem,
    AddItem,
    EditItem,
    alert: Alert,
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      getItems: `${StoreState.items}`,
      showMessage: `${StoreState.showMessage}`,
      getMessage: `${StoreState.message}`,
      getMessageType: `${StoreState.messageType}`,
      getAlertCountdown: `${StoreState.alertDismissCountdown}`,
      editItem: `${StoreState.editItem}`
    }),
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      getItemsFromList: StoreActions.getAllItems
    }),
    updateEditItem(item) {
      this.$store.commit(`${StoreIndex.storeName}/${StoreMutations.SET_EDIT_ITEM}`, item);
    },
    dismissAlert() {
      this.$store.commit(`${StoreIndex.storeName}/${StoreMutations.SET_ALERT_COUNTDOWN}`, 0);
    },
    updateDismissAlert(payload) {
      this.$store.commit(`${StoreIndex.storeName}/${StoreMutations.SET_ALERT_COUNTDOWN}`, payload);
    },
    onSubmitUpdate() {
      this.updateItem(this.editItem, this.editItem.id);
    },
    removeItem(itemID) {
      this.$store.dispatch(`${StoreIndex.storeName}/${StoreActions.deleteItem}`, itemID);
    },
    updateItemNameEdit(name) {
      this.editItem.name = name;
    },
    itemTypeChangeEdit(type) {
      this.editItem.type = type;
    },
    itemTypeChange(type) {
      this.addItemForm.type = type;
    },
    onDeleteItem(id) {
      this.removeItem(id);
    },
    updateItem(payload, id) {
      this.$store.dispatch(`${StoreIndex.storeName}/${StoreActions.editItem}`, { payload, id });
    },
    onResetUpdate() {
      this.initForm();
    },
    initForm() {
      this.addItemForm.name = '';
      this.addItemForm.type = '';
      this.addItemForm.sweet = false;
      this.editItemForm.id = '';
      this.editItemForm.name = '';
      this.editItemForm.type = '';
      this.editItemForm.sweet = false;
    },
    onSubmit() {
      const payload = {
        name: this.addItemForm.name,
        type: this.addItemForm.type,
      };
      this.addItem(payload);
      this.initForm();
    },
    onReset() {
      this.initForm();
    },
  },
  created() {
    this.getItemsFromList(this.listId)
    document.title = 'Catering';
  }
};
</script>
