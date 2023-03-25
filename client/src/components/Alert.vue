<template>
  <div>
    <b-alert variant="success" show>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  name: 'AlertComponent',
  props: ['message'],
};
</script>

<style scoped>

</style>
