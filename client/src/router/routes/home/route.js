import List from '@/home/components/List.vue';
import RouterList from '@/global-helpers/routerList';

const routes = [
  {
    path: '/',
    name: RouterList.routes.homeList.value,
    component: List,
  },
];

export default routes;
