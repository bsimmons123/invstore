import CateringList from '@/catering/components/CateringListView.vue';
import RouterList from '@/global-helpers/routerList';
import List from "../../../catering/components/List.vue";

export default [
  {
    path: '/catering',
    name: RouterList.routes.cateringListView.value,
    component: CateringList,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/catering_list/:listId',
    name: RouterList.routes.cateringList.value,
    component: List,
    meta: {
      requiresAuth: true
    },
    props: true
  }
];
