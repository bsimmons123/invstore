<template>
  <div class="login-image">
    <NavBar></NavBar>
    <water-filling-animation
      v-show="loading"
    />
    <template v-if="!loading">
      <router-view/>
    </template>
    <alert
      :type="messageType"
      dismissible
      v-if="message"
      class="position-absolute bottom-0 end-0 bottom-right-alert"
    >
      <!-- Content inside the alert -->
      {{ message }}
    </alert>
  </div>
</template>

<script>
import NavBar from '@/global-componets/NavBar.vue';
import { mapState } from 'vuex';
import StoreIndex from './store/_StoreIndex';
import { StoreState } from './store/state';
import WaterFillingAnimation from './components/WaterFillingAnimation.vue';
import Alert from "../components/Alert.vue";

export default {
  data() {
    return {
      loading: true,
      loadingAnimationTime: 500,
    };
  },
  components: {
    Alert,
    NavBar,
    WaterFillingAnimation,
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      loggedIn: StoreState.isLoggedIn,
      message: StoreState.message,
      messageType: StoreState.messageType
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
    } else {
      this.loading = false;
    }
  },
};
</script>

<style>
.bottom-right-alert {
  position: fixed;
  bottom: 10px; /* Adjust the top position as needed */
  right: 10px; /* Adjust the right position as needed */
}
</style>
