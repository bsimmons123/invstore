<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="primary" style="margin-bottom: 0">
      <b-navbar-brand @click="navigateToRoute(routes.homeList.value)">Catering</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
<!--          <b-nav-item-dropdown text="Module" right>-->
<!--            <div v-for="route in routes" :key="route.label">-->
<!--              <b-dropdown-item @click="navigateToRoute(route.value)">-->
<!--                {{ route.label }}-->
<!--              </b-dropdown-item>-->
<!--            </div>-->
<!--          </b-nav-item-dropdown>-->
          <b-nav-item @click="navigateToRoute(routes.homeList.value)">Home</b-nav-item>
          <b-nav-item @click="navigateToRoute(routes.cateringListView.value)">Lists</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item @click="performLogout" v-if="loggedIn">Logout</b-nav-item>
        <b-nav-item @click="toLogin" v-else>Login</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import RouterList from '@/global-helpers/routerList';
import {mapActions, mapMutations, mapState} from 'vuex';
import StoreIndex from '@/login/store/_StoreIndex';
import { StoreActions } from '@/login/store/actions';
import {StoreState} from "@/login/store/state";
import {StoreMutations} from "@/login/store/mutations";

export default {
  name: 'NavBar',
  data() {
    return {
      routes: RouterList.routes,
    };
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      loggedIn: StoreState.isLoggedIn
    })
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      logout: StoreActions.logout,
    }),
    ...mapMutations(StoreIndex.storeName, {
      setLoggedIn: StoreMutations.SET_LOGGED_IN
    }),
    performLogout() {
      this.logout()
    },
    navigateToRoute(routeName) {
      if (this.$router.currentRoute.name !== routeName) {
        this.$router.push({ name: routeName });
      }
    },
    toLogin() {
      if (this.$router.currentRoute.name !== RouterList.routes.login.value) {
        this.$router.push({ name: RouterList.routes.login.value })
      }
    }
  },
  created() {
    let isLoggedIn = localStorage.getItem('logged_in');
    if (isLoggedIn === null) {
      this.setLoggedIn(false)
    } else {
      if (isLoggedIn) {
        this.setLoggedIn(true)
      } else
        this.setLoggedIn(false)
    }
  }
};
</script>

<style scoped>

</style>
