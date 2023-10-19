<template>
  <div>
    <div class="flex">
      <div class="min-h-screen flex-1">
        <div class="flex h-full items-center py-8 px-5">
          <LoginForm />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from './LoginForm.vue';

export default {
  name: 'LoginPage',
  components: { LoginForm },
  layout: 'login',
};
</script>
