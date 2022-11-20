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
      .get(process.env.VUE_APP_RUTA + "me/profile", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
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
