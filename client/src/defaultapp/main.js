import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import router from '@/router/index';
import store from '@/stores/index';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
