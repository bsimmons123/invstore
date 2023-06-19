<template>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Type</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in items" :key="index">
        <td>{{ item.name }}</td>
        <td>{{ item.type }}</td>
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
</template>

<script>
import CateringItem from '@/store/model';

export default {
  name: 'ViewItem',
  props: {
    items: {
      type: Array,
      default() {
        return [new CateringItem()];
      },
    },
  },
  methods: {
    editItem(item) {
      this.$emit('populateEditItem', item);
    },
    onDeleteItem(item) {
      this.$emit('populateIdDelete', item.id);
    },
  },
};
</script>

<style scoped>

</style>
