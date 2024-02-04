import List from '@/home/components/List.vue';
import RouterList from '@/global-helpers/routerList';
import CreateAccount from "../../../login/components/CreateAccount.vue";
import LoginForm from "../../../login/components/LoginForm.vue";

const routes = [
  {
    path: '/',
    name: RouterList.routes.homeList.value,
    component: List,
  },
  {
    path: '/register',
    name: RouterList.routes.createAccount.value,
    component: CreateAccount,
  },
  {
    path: '/login',
    name: RouterList.routes.login.value,
    component: LoginForm,
  }
];

export default routes;
