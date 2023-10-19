<template>
  <b-modal ref="addModal"
           id="add-list-modal"
           title="Add a new List"
           hide-footer>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Label:"
                  label-for="form-name-input">
        <b-form-input id="form-name-input"
                      type="text"
                      :value="cateringList.name" @input="updateCateringList($event)"
                      required
                      placeholder="Enter label">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-modal>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";
import StoreIndex from "../store/_StoreIndex";
import {StoreState} from "../store/state";
import {StoreMutations} from "../store/mutations";
import {StoreActions} from "../store/actions";

export default {
  name: 'AddCateringList',
  computed: {
    ...mapState(StoreIndex.storeName, {
      cateringList: StoreState.addCateringList
    }),
  },
  methods: {
    ...mapMutations(StoreIndex.storeName, {
      updateCateringList: StoreMutations.UPDATE_ADD_CATERING_LIST
    }),
    ...mapActions(StoreIndex.storeName, {
      addCateringList: StoreActions.addNewCateringList
    }),
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.addCateringList(this.cateringList)
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.$emit('onAddReset');
    },
  }
}
</script>

<style scoped>

</style>
