import Vue from 'vue';
import Router from 'vue-router';
import List from '@/components/List.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'CateringList',
      component: List,
    },
  ],
});
