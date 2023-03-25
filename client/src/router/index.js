import Vue from 'vue';
import Router from 'vue-router';
import Books from '@/components/Books.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'BookList',
      component: Books,
    },
    {
      path: '/ping',
      name: 'PingCounter',
      component: Ping,
    },
    {
      path: '*',
      name: 'BookList',
      component: Books,
    },
  ],
});
