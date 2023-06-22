<template>
  <div>
    <alert
      :message=getMessage
      :message-type="getMessageType"
      :dismiss-count-down="getAlertCountdown"
      v-if="showMessage"
      @dismiss="dismissAlert"
      @updateCountdown="updateDismissAlert"
    />
    <button type="button" class="btn btn-success btn-sm" v-b-modal.add-modal>Add Item</button>
    <br><br>
    <view-item
      :items="getItems"
      @populateEditItem="editItem"
      @populateIdDelete="onDeleteItem"
    />
    <add-item
      :item="addItemForm"
      @itemNameChange="updateItemName"
      @itemTypeChange="itemTypeChange"
      @onAdd="onSubmit"
      @onAddReset="onResetUpdate"
    />
    <edit-item
      :item="$store.state.editItem"
      @itemNameChange="updateItemNameEdit"
      @itemTypeChange="itemTypeChangeEdit"
      @onEdit="onSubmitUpdate"
      @onEditReset="onResetUpdate"
    />
  </div>
</template>

<script>
import EditItem from '@/components/EditItem.vue';
import AddItem from '@/components/AddItem.vue';
import ViewItem from '@/components/ViewItem.vue';
import CateringItem from '@/store/model';
import Alert from './Alert.vue';
import store from '../store/index';

export default {
  name: 'CateringList',
  data() {
    return {
      addItemForm: new CateringItem(),
      editItemForm: new CateringItem(),
      message: '',
    };
  },
  components: {
    ViewItem,
    AddItem,
    EditItem,
    alert: Alert,
  },
  methods: {
    editItem(item) {
      this.$store.state.editItem = item;
    },
    dismissAlert() {
      this.$store.commit('SET_ALERT_COUNTDOWN', 0);
    },
    updateDismissAlert(payload) {
      this.$store.commit('SET_ALERT_COUNTDOWN', payload);
    },
    onSubmitUpdate() {
      this.updateItem(this.$store.state.editItem, this.$store.state.editItem.id);
    },
    removeItem(itemID) {
      this.$store.dispatch('deleteItem', itemID);
    },
    updateItemNameEdit(name) {
      this.$store.state.editItem.name = name;
    },
    itemTypeChangeEdit(type) {
      this.$store.state.editItem.type = type;
    },
    updateItemName(name) {
      this.addItemForm.name = name;
    },
    itemTypeChange(type) {
      this.addItemForm.type = type;
    },
    onDeleteItem(id) {
      this.removeItem(id);
    },
    updateItem(payload, id) {
      this.$store.dispatch('editItem', { payload, id });
    },
    onResetUpdate() {
      this.initForm();
    },
    addItem(payload) {
      this.$store.dispatch('addItem', payload);
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
    this.$store.dispatch('getAllItems');
    document.title = 'Catering';
  },
  computed: {
    getItems() {
      return store.state.items;
    },
    showMessage() {
      return store.state.showMessage;
    },
    getMessage() {
      return store.state.message;
    },
    getMessageType() {
      return store.state.messageType;
    },
    getAlertCountdown() {
      return store.state.alertDismissCountdown;
    },
  },
};
</script>
