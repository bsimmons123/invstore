<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand @click="navigateToRoute(routes.homeList.value)">Catering</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item-dropdown text="Module" right>
            <div v-for="route in routes" :key="route.label">
              <b-dropdown-item @click="navigateToRoute(route.value)">
                {{ route.label }}
              </b-dropdown-item>
            </div>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item @click="logout">Logout</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import RouterList from '@/global-helpers/routerList';
import { mapActions } from 'vuex';
import StoreIndex from '../login/store/_StoreIndex';
import { StoreActions } from '../login/store/actions';

export default {
  name: 'NavBar',
  data() {
    return {
      routes: RouterList.routes,
    };
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      logout: StoreActions.logout,
    }),
    navigateToRoute(routeName) {
      if (this.$router.currentRoute.name !== routeName) {
        this.$router.push({ name: routeName });
      }
    },
  },
};
</script>

<style scoped>

</style>
