<template>
  <div v-if="message">
    <b-alert
      :show="dismissCountDown"
      dismissible
      :variant="messageType"
      @dismissed="countDownDismissed"
      @dismiss-count-down="countDownChanged"
    >
      <p>{{ message }}</p>
      <b-progress
        :variant="messageType"
        :max="dismissSecs"
        :value="dismissCountDown"
        height="4px"
      ></b-progress>
    </b-alert>
  </div>
</template>

<script>
export default {
  name: 'AlertComponent',
  data() {
    return {
      dismissSecs: 5,
      showDismissibleAlert: false,
    };
  },
  props: ['message', 'messageType', 'dismissCountDown'],
  methods: {
    countDownDismissed() {
      this.$emit('dismiss');
    },
    countDownChanged(dismissCountDown) {
      this.$emit('updateCountdown', dismissCountDown);
    },
  },
};
</script>

<style scoped>

</style>
