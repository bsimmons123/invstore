<template>
  <div class="content">
    <div class="container">
      <div class="col-md-5 ml-auto mr-auto create-account-container">
        <h2>Create Account</h2>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="username">Username:</label>
            <input
              type="text"
              id="username"
              v-model="registrationParams.username"
              class="form-control"
              placeholder="Enter Username Here"
              required
            />
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input
              type="email"
              id="email"
              v-model="registrationParams.email"
              class="form-control"
              required
              placeholder="Enter Email Here"
            />
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input
              type="password"
              id="password"
              v-model="registrationParams.password"
              class="form-control"
              placeholder="Enter Password Here"
              required
            />
          </div>
          <template v-if="!loggedIn">
            <button type="submit" class="btn btn-primary">Create Account</button>
          </template>
          <template v-else>
            <b-badge variant="danger">You're already logged in!</b-badge>
          </template>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import UserLoginAdapter from "@/login/store/UserLoginAdapter";
import {mapActions, mapMutations, mapState} from "vuex";
import StoreIndex from "@/login/store/_StoreIndex";
import {StoreState} from "@/login/store/state";
import {StoreActions} from "@/login/store/actions";
import {StoreMutations} from "@/login/store/mutations";

export default {
  data() {
    return {
      registrationParams: new UserLoginAdapter()
    };
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      showMessage: StoreState.showMessage,
      getMessage: StoreState.message,
      getMessageType: StoreState.messageType,
      getAlertCountdown: StoreState.alertDismissCountdown,
      loggedIn: StoreState.isLoggedIn
    }),
  },
  methods: {
    ...mapActions(StoreIndex.storeName, {
      register: StoreActions.register,
    }),
    ...mapMutations(StoreIndex.storeName, {
      SET_ALERT_COUNTDOWN: StoreMutations.SET_ALERT_COUNTDOWN,
    }),
    submitForm() {
      this.register(this.registrationParams);
    },
    dismissAlert() {
      this.SET_ALERT_COUNTDOWN(0);
    },
    updateDismissAlert(payload) {
      this.SET_ALERT_COUNTDOWN(payload);
    },
  }
};
</script>

<style scoped>
.create-account-container {
  width: 400px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
