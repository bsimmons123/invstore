<template>
  <div>
    <NavBar></NavBar>
    <div id="app">
      <water-filling-animation
        v-show="loading"
      />
      <template v-if="!loading">
        <router-view/>
      </template>
    </div>
  </div>
</template>

<script>
import NavBar from '@/global-componets/NavBar.vue';
import {mapActions, mapState} from 'vuex';
import StoreIndex from '../login/store/_StoreIndex';
import { StoreState } from '../login/store/state';
import { StoreActions } from '../login/store/actions';
import LoginPage from '../login/components/Login.vue';
import WaterFillingAnimation from './components/WaterFillingAnimation.vue';

export default {
  data() {
    return {
      loading: true,
      loadingAnimationTime: 500,
    };
  },
  components: {
    NavBar,
    LoginPage,
    WaterFillingAnimation,
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      loggedIn: StoreState.isLoggedIn,
    }),
  },
  created() {
    if (!this.loggedIn) {
      const timeoutPromise = new Promise((resolve) => {
        setTimeout(() => {
          resolve();
        }, this.loadingAnimationTime);
      });
      Promise.all([timeoutPromise])
        .then(() => {
          this.loading = false;
        });
    }
  },
};
</script>

<style>
#app {
  margin-top: 60px
}
</style>
