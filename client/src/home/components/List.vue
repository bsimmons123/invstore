<template>
  <div>
    <div style="margin-left: 10%; margin-right:5%; margin-top: 4%;" v-html="markdownToHtml"></div>
  </div>
</template>

<script>
import Parallax from "../../components/Parallax.vue";
import {FormGroupInput, Button} from "../../components";
import NButton from "../../components/Button.vue";
import FgInput from "../../components/Inputs/formGroupInput.vue";
import {mapActions, mapState} from "vuex";
import {StoreState} from "../../login/store/state";
import StoreIndex from "../../login/store/_StoreIndex";
import {StoreActions} from "../../login/store/actions";
import { marked } from 'marked'

export default {
  name: 'landing',
  bodyClass: 'landing-page',
  components: {
    FgInput,
    NButton,
    Parallax,
    [Button.name]: Button,
    [FormGroupInput.name]: FormGroupInput
  },
  computed: {
    ...mapState(StoreIndex.storeName, {
      isLoggedIn: StoreState.isLoggedIn
    }),
    markdownToHtml() {
     return marked(this.markdown);
    }
  },
  data() {
    return {
      form: {
        firstName: '',
        email: '',
        message: ''
      },
      markdown: "![Alt text](./android-chrome-192x192.png)\n" +
        "# InvStore - Event Planner App\n" +
        "\n" +
        "Welcome to InvStore! 🎉 This application helps you organize events by allowing participants to sign up and contribute items for the occasion. Whether it's a potluck dinner, picnic, or any gathering, InvStore makes coordination a breeze.\n" +
        "\n" +
        "## Features\n" +
        "\n" +
        "- **User Registration and Authentication:** Users can create accounts, log in, and manage their profile.\n" +
        "\n" +
        "- **Event Creation:** Easily create events, specifying the date, location, and any other relevant details.\n" +
        "\n" +
        "- **Item Contributions:** Participants can view upcoming events and indicate what items they plan to bring. This ensures a diverse and well-coordinated spread.\n" +
        "\n" +
        "- **Event Details:** Get comprehensive details about each event, including who's bringing what.\n" +
        "\n" +
        "- **User-Friendly Interface:** InvStore features an intuitive and user-friendly interface, making it easy for everyone to participate and contribute.\n" +
        "\n" +
        "## Getting Started\n" +
        "\n" +
        "1. **Sign Up:** Create an account to start using InvStore.\n" +
        "\n" +
        "2. **Create an Event:** Plan your next gathering and invite friends or colleagues.\n" +
        "\n" +
        "3. **Contribute Items:** Let everyone know what you're bringing to the event.\n" +
        "\n" +
        "4. **Explore and Enjoy:** Check out what others are bringing and get excited about the upcoming occasion!\n" +
        "\n" +
        "## Technologies Used\n" +
        "\n" +
        "- **Frontend:** Vue.js, Bootstrap, etc.\n" +
        "\n" +
        "- **Backend:** Node.js, Express, MongoDB, etc.\n" +
        "\n" +
        "## Feedback and Contributions\n" +
        "\n" +
        "We welcome your feedback! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/yourusername/invstore/issues).\n" +
        "\n" +
        "Feel free to contribute to the project by submitting pull requests.\n" +
        "\n" +
        "Happy event planning with InvStore! 🥳\n"
    };
  },  
  methods: {
    ...mapActions(StoreIndex.storeName, {
      checkLogin: StoreActions.check_login
    })
  },
  created() {
    this.checkLogin();
  }
};
</script>

<style>
.parallax-style {
  background-image: url('@/assets/img/bg6.jpg');
}
.login-style {
  background-image: url('@/assets/img/login.jpg');
}
.right-image {
  background-image: url('@/assets/img/bg3.jpg');
}
.another-image {
  background-image: url('@/assets/img/bg1.jpg');
}
</style>
