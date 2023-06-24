<template>
  <b-modal ref="editItemModal"
           id="item-update-modal"
           title="Update"
           hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-name-edit-group"
                  label="Name:"
                  label-for="form-name-edit-input">
        <b-form-input id="form-name-edit-input"
                      type="text"
                      :value="item ? item.name : ''" @input="$emit('itemNameChange', $event)"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                    label="Type:"
                    label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        :value="item ? item.type : ''" @input="$emit('itemTypeChange', $event)"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
      <b-button-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
</template>

<script>
import CateringItem from '@/catering/store/model';

export default {
  name: 'EditItem',
  props: {
    item: new CateringItem(),
  },
  methods: {
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      this.$emit('onEdit');
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      this.$emit('onEditReset');
    },
  },
};
</script>

<style scoped>

</style>
