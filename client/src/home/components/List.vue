<template>
  <div>
    <span>This is home</span>
  </div>
</template>

<script>

import {mapMutations} from "vuex";
import StoreIndex from "../../login/store/_StoreIndex";
import {StoreMutations} from "../../login/store/mutations";

export default {
  name: 'HomeList',
  methods: {
    ...mapMutations(StoreIndex.storeName, {
      setLoggedIn: StoreMutations.SET_LOGGED_IN
    })
  },
};
</script>
