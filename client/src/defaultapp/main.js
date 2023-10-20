import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import router from '@/router/index';
import store from './stores';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';
import NowUiKit from '../plugins/now-ui-kit';

Vue.use(BootstrapVue);
Vue.use(NowUiKit);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
