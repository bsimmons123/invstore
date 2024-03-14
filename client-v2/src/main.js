import { createApp } from "vue";
import App from "./App.vue";
// import store from "./store";
import stores from "./stores"
import router from "./router";
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import ArgonDashboard from "./argon-dashboard";

const appInstance = createApp(App);
// appInstance.use(store);
appInstance.use(stores);
appInstance.use(router);
appInstance.use(ArgonDashboard);
appInstance.mount("#app");
