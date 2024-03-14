<script setup>
import {onBeforeUnmount, onBeforeMount, computed} from "vue";
import { useStore } from "vuex";
import Navbar from "@/examples/PageLayout/Navbar.vue";
import ArgonInput from "@/components/ArgonInput.vue";
import ArgonSwitch from "@/components/ArgonSwitch.vue";
import ArgonButton from "@/components/ArgonButton.vue";
import StoreIndex from "@/store/login/_StoreIndex";
import {StoreActions} from "@/store/login/actions";
import ArgonAlert from "@/components/ArgonAlert.vue";
const body = document.getElementsByTagName("body")[0];

const store = useStore();

const argonState = store.state.argon;
const loginState = store.state.userLogin;

const email = computed(() => loginState.email);
const password = computed(() => loginState.password);

const showErrors = computed(() => loginState.showMessage);
const errors = computed(() => loginState.message);

const emailUpdate = (payload) => store.commit("userLogin/SET_EMAIL", payload);
const passwordUpdate = (payload) => store.commit("userLogin/SET_PASSWORD", payload);
const showError = (payload) => store.commit("userLogin/TOGGLE_SHOW_MESSAGE", payload);

const login = () => store.dispatch(`${StoreIndex.storeName}/${StoreActions.login}`);

onBeforeMount(() => {
  argonState.hideConfigButton = true;
  argonState.showNavbar = false;
  argonState.showSidenav = false;
  argonState.showFooter = false;
  showError(false);
  body.classList.remove("bg-gray-100");
});
onBeforeUnmount(() => {
  argonState.hideConfigButton = false;
  argonState.showNavbar = true;
  argonState.showSidenav = true;
  argonState.showFooter = true;
  // disable errors
  showError(false);
  body.classList.add("bg-gray-100");
});
</script>
<template>
  <div class="container top-0 position-sticky z-index-sticky">
    <div class="row">
      <div class="col-12">
        <navbar
          isBlur="blur  border-radius-lg my-3 py-2 start-0 end-0 mx-4 shadow"
          v-bind:darkMode="true"
          isBtn="bg-gradient-success"
        />
      </div>
    </div>
  </div>
  <main class="mt-0 main-content">
    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div class="row">
            <div
              class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0"
            >
              <div class="card card-plain">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder">Sign In</h4>
                  <p class="mb-0">Enter your email and password to sign in</p>
                </div>
                <argon-alert
                  :dismissible="false"
                  color="danger"
                  v-if="showErrors"
                >
                  <template v-if="showErrors">
                      {{ errors }}
                  </template>
                </argon-alert>
                <div class="card-body">
                  <form role="form"  @submit.prevent="login">
                    <div class="mb-3">
                      <argon-input
                        id="email"
                        type="email"
                        placeholder="Email"
                        name="email"
                        size="lg"
                        :model-value="email"
                        @update:model-value="emailUpdate"
                      />
                    </div>
                    <div class="mb-3">
                      <argon-input
                        id="password"
                        type="password"
                        placeholder="Password"
                        name="password"
                        size="lg"
                        :model-value="password"
                        @update:model-value="passwordUpdate"
                      />
                    </div>
                    <argon-switch id="rememberMe" name="remember-me"
                      >Remember me
                    </argon-switch>

                    <div class="text-center">
                      <argon-button
                        class="mt-4"
                        variant="gradient"
                        color="success"
                        fullWidth
                        size="lg"
                      >
                        Sign in
                      </argon-button>
                    </div>
                  </form>
                </div>
                <div class="px-1 pt-0 text-center card-footer px-lg-2">
                  <p class="mx-auto mb-4 text-sm">
                    Don't have an account?
                    <router-link to="signup" class="text-success text-gradient font-weight-bold">
                      Sign up
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column"
            >
              <div
                class="position-relative bg-gradient-primary h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden"
                style="
                  background-image: url(&quot;https://raw.githubusercontent.com/creativetimofficial/public-assets/master/argon-dashboard-pro/assets/img/signin-ill.jpg&quot;);
                  background-size: cover;
                "
              >
                <span class="mask bg-gradient-success opacity-6"></span>
                <h4
                  class="mt-5 text-white font-weight-bolder position-relative"
                >
                  "Attention is the new currency"
                </h4>
                <p class="text-white position-relative">
                  The more effortless the writing looks, the more effort the
                  writer actually put into the process.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
