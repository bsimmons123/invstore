<template>
  <div>
    <NavBar></NavBar>
    <div id="app">
      <router-view/>
    </div>
  </div>
</template>

<style>
#app {
  margin-top: 60px
}
</style>
<script setup>
import NavBar from '@/global-componets/NavBar.vue';
</script>
