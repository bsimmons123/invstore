import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

// automatically load all files from ./routes directory and register them
const autoLoadedFiles = require.context(
  './routes', // Look for files in the current directory
  true, // include subdirectories
  /\.js$/, // Only include files that end with .js
);

const routes = [];
// loop over the files in the ./routes directory
autoLoadedFiles.keys().forEach((fileName) => {
  // get the default exported object from the route file and push it to the routes array
  const routeObjects = autoLoadedFiles(fileName).default;
  if (Array.isArray(routeObjects)) {
    routes.push(...routeObjects);
  } else {
    routes.push(routeObjects);
  }
});

routes.push({ path: '*', redirect: '/' });

const router = new VueRouter({
  base: process.env.BASE_URL,
  mode: 'history',
  routes,
});

router.beforeEach((to, from, next) => {
  let isLoggedIn = localStorage.getItem('logged_in');
  if (to.meta.requiresAuth && isLoggedIn === null) {
    if (from.path !== '/login') {
      next('/login'); // Redirect to login page if not authenticated
    }
  } else {
    if (from.name !== to.name) {
      next(); // Proceed to the requested route
    }
  }
});

export default router;
