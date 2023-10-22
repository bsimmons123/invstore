<template>
  <b-modal ref="addModal"
           id="add-modal"
           title="Add a new item"
           hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Name:"
                  label-for="form-name-input">
        <b-form-input id="form-name-input"
                      type="text"
                      :value="item.label" @input="updateItem({ key: 'label', value: $event} )"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-select
        v-model="item.type_id"
        :options="itemTypes"
        class="mb-3"
        value-field="id"
        text-field="label"
        disabled-field="notEnabled"
        @change="customChangeHandler"
      />
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-modal>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import {StoreState} from "../store/state";
import StoreIndex from "../store/_StoreIndex"
import {StoreMutations} from "../store/mutations";
import {StoreActions} from "../store/actions";

export default {
  name: 'AddItem',
  props: {
    listId: {
      default: 0,
      required: true
    }
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      item: StoreState.addItemForm,
      itemTypes: StoreState.itemTypes
    })
  },
  methods: {
    ...mapMutations(StoreIndex.storeName, {
      updateItem: StoreMutations.UPDATE_ADD_ITEM_FORM
    }),
    ...mapActions(StoreIndex.storeName, {
      saveItem: StoreActions.addItem
    }),
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.updateItem({ key: 'list_id', value: this.listId })
      this.saveItem(this.item)
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.$emit('onAddReset');
    },
    customChangeHandler(value) {
      this.updateItem({ key: 'type_id', value: value })
    }
  },
};
</script>

<style scoped>

</style>
