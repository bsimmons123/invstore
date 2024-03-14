import {createStore} from 'vuex';


// Automatically load all files from ./stores directory and register them
const autoLoadedStores = require.context(
  '../', // Look for files in the current directory
  true, // Include subdirectories
  /_StoreIndex.js$/, // Only include files that end with .js
);

const stores = {};
// Loop over the files in the ./stores directory

autoLoadedStores.keys().forEach((fileName) => {
  // Get the default exported object from the store file
  const store = autoLoadedStores(fileName).default;
  // Extract the store name from the file path (assuming the file is named using PascalCase)
  const storeName = store.storeName || fileName.replace(/^\.\/(.*)\.\w+$/, '$1');
  // Add the store to the stores object using the storeName as the key
  stores[storeName] = {
    namespaced: true,
    ...store, // Include the original module
  };
});

const store = createStore({
  modules: stores,
});

export default store;
