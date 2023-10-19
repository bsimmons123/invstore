<template>
  <div class="login-container">
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
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex';
import { StoreActions } from '../store/actions';
import StoreIndex from '../store/_StoreIndex';
import UserLoginAdapter from '../store/UserLoginAdapter';
import AlertComponent from '../../global-componets/Alert.vue';
import { StoreState } from '../store/state';
import { StoreMutations } from '../store/mutations';
import routes from "../../router/routes/home/route";
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
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.login-form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

.input-group {
  width: 100%;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn {
  margin-top: 10px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-secondary {
  background-color: #6c757d;
  color: #fff;
}
</style>
