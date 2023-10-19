import List from '@/home/components/List.vue';
import RouterList from '@/global-helpers/routerList';
import CreateAccount from "../../../login/components/CreateAccount.vue";
import Login from "../../../login/components/Login.vue";

const routes = [
  {
    path: '/',
    name: RouterList.routes.homeList.value,
    component: List,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/register',
    name: RouterList.routes.createAccount.value,
    component: CreateAccount,
  },
  {
    path: '/login',
    name: RouterList.routes.login.value,
    component: Login,
  }
];

export default routes;
