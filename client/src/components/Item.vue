<template>
  <b-modal ref="addModal"
           id="add-modal"
           title="Add a new item"
           hide-footer
           v-if="add">
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Title:"
                  label-for="form-title-input">
        <b-form-input id="form-title-input"
                      type="text"
                      v-model="addItemForm.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                    label="Author:"
                    label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addItemForm.type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-read-group">
        <b-form-checkbox-group v-model="addItemForm.sweet" id="form-checks">
          <b-form-checkbox value="true">sweet?</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-modal>
  <b-modal ref="editModal"
           id="edit-modal"
           title="Edit item"
           hide-footer
           v-else>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Title:"
                  label-for="form-title-input">
        <b-form-input id="form-title-input"
                      type="text"
                      v-model="editItemForm.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                    label="Author:"
                    label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="editItemForm.type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-read-group">
        <b-form-checkbox-group v-model="editItemForm.sweet" id="form-checks">
          <b-form-checkbox value="true">sweet?</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-modal>
</template>

<script>
export default {
  name: 'ItemComponent',
  props: {
    add: Boolean,
  },
  data() {
    return {
      items: [],
      addItemForm: {
        name: '',
        type: '',
        sweet: [],
      },
      editItemForm: {
        id: '',
        name: '',
        type: '',
        sweet: [],
      },
      message: '',
      showMessage: false,
    };
  },
  methods: {
    onSubmit() {
      this.$emit('onSubmit');
    },
  },
};
</script>

<style scoped>

</style>
