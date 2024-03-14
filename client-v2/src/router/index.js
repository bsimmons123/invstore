import {createRouter, createWebHashHistory} from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Tables from "../views/Tables.vue";
import Billing from "../views/Billing.vue";
import VirtualReality from "../views/VirtualReality.vue";
import RTL from "../views/Rtl.vue";
import Profile from "../views/Profile.vue";
import Signup from "../views/Signup.vue";
import Signin from "../views/Signin.vue";
import RouterList from "@/store/global-helpers/routerList";

const routes = [
  {
    path: "/",
    name: "/",
    value: "/",  // added line
    redirect: "/dashboard-default",
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/dashboard-default",
    name: "Dashboard",
    value: "Dashboard",  // added line
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/tables",
    name: "Tables",
    value: "Tables",  // added line
    component: Tables,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/billing",
    name: "Billing",
    value: "Billing",  // added line
    component: Billing,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/virtual-reality",
    name: "Virtual Reality",
    value: "Virtual Reality",  // added line
    component: VirtualReality,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/rtl-page",
    name: "RTL",
    value: "RTL",  // added line
    component: RTL,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/profile",
    name: "Profile",
    value: "Profile",  // added line
    component: Profile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/signin",
    name: "Signin",
    value: "Signin",  // added line
    component: Signin,
  },
  {
    path: "/signup",
    name: "Signup",
    value: "Signup",  // added line
    component: Signup,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: Signin
  }
];

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

router.beforeEach((to, from, next) => {
  let isLoggedIn = localStorage.getItem('logged_in');
  if (to.meta.requiresAuth && isLoggedIn === null) {
    if (from.path !== RouterList.routes.signin.path) {
      next(RouterList.routes.signin.path); // Redirect to login page if not authenticated
    }
  } else {
    if (from.name !== to.name) {
      next(); // Proceed to the requested route
    }
  }
});

export default router;
