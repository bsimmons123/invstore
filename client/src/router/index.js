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
  routes.push(autoLoadedFiles(fileName).default);
});

routes.push({ path: '*', redirect: '/' });

const router = new VueRouter({
  base: `${process.env.BASE_URL}`,
  routes,
});

export default router;
