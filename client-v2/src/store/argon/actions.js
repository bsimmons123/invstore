export const StoreActions = {
  toggleSidebarColor: 'toggleSidebarColor',
};

export default {
  toggleSidebarColor({ commit }, payload) {
      commit("sidebarType", payload);
    },
};
