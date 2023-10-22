<template>
  <div class="content">
    <div class="container">
      <div class="col-md-5 ml-auto mr-auto login-container">
        <h2>Login</h2>
        <form @submit.prevent="submitForm" class="login-form">
          <div class="form-group">
            <label for="email">Email:</label>
            <input
              type="email"
              id="email"
              v-model="loginParams.email"
              required
              class="form-control"
              placeholder="Enter Email Here"
            />
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input
              type="password"
              id="password"
              v-model="loginParams.password"
              required
              class="form-control"
              placeholder="Enter Password Here"
            />
          </div>
          <alert-component
            :message="getMessage"
            :message-type="getMessageType"
            :dismiss-count-down="getAlertCountdown"
            v-if="showMessage"
            @dismiss="dismissAlert"
            @updateCountdown="updateDismissAlert"
          />
          <button type="submit" class="btn btn-primary">Login</button>
          <button type="button" class="btn btn-secondary" @click="navigateToRegister" style="margin-left: 10px;">Create Account</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex';
import { StoreActions } from '../store/actions';
import StoreIndex from '../store/_StoreIndex';
import UserLoginAdapter from '../store/UserLoginAdapter';
import AlertComponent from '../../global-componets/Alert.vue';
import { StoreState } from '../store/state';
import { StoreMutations } from '../store/mutations';
import RouterList from "../../global-helpers/routerList";

export default {
  components: { AlertComponent },
  data() {
    return {
      loginParams: new UserLoginAdapter(),
    };
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      showMessage: StoreState.showMessage,
      getMessage: StoreState.message,
      getMessageType: StoreState.messageType,
      getAlertCountdown: StoreState.alertDismissCountdown,
    }),
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      login: StoreActions.login,
    }),
    ...mapMutations(StoreIndex.storeName, {
      SET_ALERT_COUNTDOWN: StoreMutations.SET_ALERT_COUNTDOWN,
    }),
    submitForm() {
      this.login(this.loginParams);
    },
    dismissAlert() {
      this.SET_ALERT_COUNTDOWN(0);
    },
    updateDismissAlert(payload) {
      this.SET_ALERT_COUNTDOWN(payload);
    },
    navigateToRegister() {
      this.$router.push({ name: RouterList.routes.createAccount.value });
    }
  },
};
</script>

<style scoped>
.login-container {
  width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
