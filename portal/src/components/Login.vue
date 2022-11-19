<template>
  <div class="hello">
    <form action class="form" @submit.prevent="register">
      <label class="form-label" for="#email">Nombre de Usuario:</label>
      <input
        v-model="username"
        class="form-input"
        type="text"
        id="username"
        required
        placeholder="Email"
      />
      <label class="form-label" for="#password">Password:</label>
      <input
        v-model="password"
        class="form-input"
        type="password"
        id="password"
        placeholder="Password"
      />
      <input class="form-submit" type="submit" value="Login" />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      token: "",
      username: "",
      password: "",
      errores: [],
    };
  },

  methods: {
    register() {
      const formData = {
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch("login", formData)
    },
  },
};
</script>
