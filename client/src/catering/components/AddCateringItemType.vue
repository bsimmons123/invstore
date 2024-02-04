<template>
  <div>
    <b-sidebar id="sidebar-right" title="Add new Item Type" right shadow>
      <div class="px-3 py-2">
        <form @submit.prevent="submitForm" class="login-form">
          <div class="form-group">
            <label for="email">Type:</label>
            <input
              type="text"
              id="type"
              v-model="type.label"
              required
              class="form-control"
              placeholder="Enter Type Here"
            />
          </div>
          <button type="submit" class="btn btn-primary">Add</button>
        </form>
      </div>
      <b-list-group>
        <b-list-group-item v-for="type in types" :key="type.id">{{ type.label }}</b-list-group-item>
      </b-list-group>
    </b-sidebar>
  </div>
</template>

<script>
import AlertComponent from "@/global-componets/Alert.vue";
import {mapActions, mapState} from "vuex";
import StoreIndex from "@/catering/store/_StoreIndex";
import {StoreActions} from "@/catering/store/actions";
import CateringItemTypeAdapter from "@/catering/store/adapters/CateringItemTypeAdapter";
import {StoreState} from "@/catering/store/state";

export default {
  components: {AlertComponent},
  data() {
    return {
      type: new CateringItemTypeAdapter(),
    };
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      types: StoreState.itemTypes
    })
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      createItemType: StoreActions.addNewItemType,
    }),
    submitForm() {
      this.createItemType(this.type);
    },
  }
};
</script>

<style scoped>

</style>
