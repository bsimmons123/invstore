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
    </b-navbar>
  </div>
</template>

<script>
import RouterList from '@/global-helpers/routerList';

export default {
  name: 'NavBar',
  data() {
    return {
      routes: RouterList.routes,
    };
  },
  methods: {
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
