<template>
  <div class="container_perfil">
    <h1 class="title_miPerfil">Mi Perfil</h1>
    <div class="mi_permil">
      <h2 class="label_perfil">Nombre:
      <span>{{ user.name }}</span></h2>
      <h2 class="label_perfil">Apellido:
      <span>{{ user.last_name }}</span></h2>
      <hr />
    </div>
  </div>
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

<style>
.container_perfil{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 3rem;
}
.label_perfil {
  color: gray;
}
.title_miPerfil {
  float: left;
}
.mi_permil {
  display: flex;
  flex-direction: column;
  align-items: self-start;
  padding: 2rem;
  border: 1px solid #e9dada;
  margin: 1rem;
  display: grid;
  box-shadow: -7px 10px #6ec1b2;
  border-radius: 5px;
  width: 50%;
}
</style>
