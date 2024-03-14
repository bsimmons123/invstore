import { StoreState } from './state';

export const StoreMutations = {
  toggleConfigurator: 'toggleConfigurator',
  sidebarMinimize: 'sidebarMinimize',
  sidebarType: 'sidebarType',
  navbarFixed: 'navbarFixed',
};

export default {
    toggleConfigurator(state) {
      state[StoreState.showConfig] = !state.showConfig;
    },
    sidebarMinimize(state) {
      let sidenav_show = document.querySelector("#app");
      if (state.isPinned) {
        sidenav_show.classList.add("g-sidenav-hidden");
        sidenav_show.classList.remove("g-sidenav-pinned");
        state[StoreState.isPinned] = false;
      } else {
        sidenav_show.classList.add("g-sidenav-pinned");
        sidenav_show.classList.remove("g-sidenav-hidden");
        state[StoreState.isPinned] = true;
      }
    },
    sidebarType(state, payload) {
      state[StoreState.sidebarType] = payload;
    },
    navbarFixed(state) {
      if (state.isNavFixed === false) {
        state[StoreState.isNavFixed] = true;
      } else {
        state[StoreState.isNavFixed] = false;
      }
    },
};
