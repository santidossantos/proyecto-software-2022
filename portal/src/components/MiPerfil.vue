<template>
  <h1>{{ user }}</h1>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      user: [],
      errores: [],
    };
  },
  async created() {
    axios
      .get("http://127.0.0.1:5000/api/me/profile", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("jwt")}`,
        },
      })
      .then((response) => {
        this.user = response.data;
      })
      .catch((e) => {
        this.errores.push(e);
      });
  },
};
</script>
