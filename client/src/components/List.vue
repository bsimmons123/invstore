<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Catering</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.add-modal>Add Item</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Type</th>
              <th scope="col">Sweet</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in getItems" :key="index">
              <td>{{ item.name }}</td>
              <td>{{ item.type }}</td>
              <td>
                <span v-if="item.sweet">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.item-update-modal
                          @click="editItem(item)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteItem(item)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
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
                      v-model="addItemForm.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                    label="Type:"
                    label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addItemForm.type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-read-group">
        <b-form-checkbox v-model="addItemForm.sweet" id="form-checks" value="true">
          Sweet
        </b-form-checkbox>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </b-modal>
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
                      v-model="editItemForm.name"
                      required
                      placeholder="Enter name">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                    label="Type:"
                    label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="editItemForm.type"
                        required
                        placeholder="Enter type">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-read-edit-group">
        <b-form-checkbox v-model="editItemForm.sweet" id="form-checks" value="true">
          Sweet
        </b-form-checkbox>
      </b-form-group>
      <b-button-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
  </div>
</template>

<script>
import Alert from './Alert.vue';
import store from '../store/index';

export default {
  name: 'CateringList',
  data() {
    return {
      addItemForm: {
        name: '',
        type: '',
        sweet: false,
      },
      editItemForm: {
        id: '',
        name: '',
        type: '',
        sweet: false,
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    editItem(item) {
      this.editItemForm = item;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      let sweet = false;
      if (this.editItemForm.sweet) sweet = true;
      const payload = {
        name: this.editItemForm.name,
        type: this.editItemForm.type,
        sweet,
      };
      this.updateItem(payload, this.editItemForm.id);
    },
    removeItem(itemID) {
      this.$store.dispatch('deleteItem', itemID);
    },
    onDeleteItem(item) {
      this.removeItem(item.id);
    },
    updateItem(payload, id) {
      this.$store.dispatch('editItem', { payload, id });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      this.initForm();
    },
    addItem(payload) {
      this.$store.dispatch('addItem', payload);
    },
    initForm() {
      this.addItemForm.name = '';
      this.addItemForm.type = '';
      this.addItemForm.sweet = [];
      this.editItemForm.id = '';
      this.editItemForm.name = '';
      this.editItemForm.type = '';
      this.editItemForm.sweet = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
      let sweet = false;
      if (this.addItemForm.sweet[0]) sweet = true;
      const payload = {
        name: this.addItemForm.name,
        type: this.addItemForm.type,
        sweet, // property shorthand
      };
      this.addItem(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addModal.hide();
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
  },
};
</script>
