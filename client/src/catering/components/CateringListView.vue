<template>
  <div class="modern-list">
    <b-button variant="primary" class="mb-2" v-b-modal.add-list-modal>Create List</b-button>
    <h2 class="list-title">Modernized List</h2>
    <div class="list-container">
      <div v-for="item in cateringLists" :key="item.id" class="list-item">
        <div class="item-info">
          <h3 class="item-title">{{ item.label }}</h3>
          <p class="item-description">TODO add description here</p>
        </div>
        <button class="item-action-button" @click="toList(item.id)">Open</button>
      </div>
    </div>
    <b-pagination
      v-if="totalPages > 1"
      v-model="currentPage"
      :total-rows="cateringLists.length"
      :per-page="perPage"
      aria-controls="modern-list"
      class="mt-3"
      align="center"
    />
    <add-catering-list

    />
  </div>
</template>

<script>
import AddCateringList from "./AddCateringList.vue";
import {mapActions, mapState} from "vuex";
import StoreIndex from "../store/_StoreIndex"
import {StoreState} from "../store/state";
import {StoreActions} from "../store/actions";
import RouterList from "../../global-helpers/routerList";

export default {
  components: { AddCateringList },
  data() {
    return {
      perPage: 2,
      currentPage: 1
    };
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      cateringLists: StoreState.cateringList
    }),
    totalPages() {
      return Math.ceil(this.cateringLists.length / this.perPage);
    },
    displayedItems() {
      const start = (this.currentPage - 1) * this.perPage;
      const end = start + this.perPage;
      return this.cateringLists.slice(start, end);
    }
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      getCateringLists: StoreActions.getCateringLists
    }),
    toList(id) {
      this.$router.push({ name: RouterList.routes.cateringList.value, params: { listId: id } })
    }
  },
  created() {
    this.getCateringLists()
  }
};
</script>

<style scoped>
.modern-list {
  text-align: center;
}

.list-title {
  font-size: 2em;
  margin-bottom: 20px;
}

.list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  width: 400px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.item-info {
  flex-grow: 1;
}

.item-title {
  font-size: 1.2em;
  margin-bottom: 5px;
}

.item-description {
  color: #666;
}

.item-action-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 12px;
  cursor: pointer;
  font-size: 0.9em;
}
</style>
