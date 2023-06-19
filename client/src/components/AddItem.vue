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
                      :value="item.name" @input="$emit('itemNameChange', $event)"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                    label="Type:"
                    label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        :value="item.type" @input="$emit('itemTypeChange', $event)"
                        required
                        placeholder="Enter type">
          </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    </b-modal>
</template>

<script>
import CateringItem from '@/store/model';

export default {
  name: 'AddItem',
  props: {
    item: new CateringItem(),
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.$emit('onAdd');
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      this.$emit('onAddReset');
    },
  },
};
</script>

<style scoped>

</style>
