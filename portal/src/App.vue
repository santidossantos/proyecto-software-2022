<template>
  <nav class="navbar navbar-dark bg-dark">
      <router-link class="navbar-brand fs-2" to="/">Home</router-link>
      <router-link class="navbar-brand" to="/disciplinas">Disciplinas</router-link>
      <router-link class="navbar-brand" v-if="$store.state.token === null" to="/login">Inciar Sesion</router-link>
      <router-link class="navbar-brand" v-if="$store.state.token" to="/payment">Realizar Pago</router-link>
      <router-link class="navbar-brand" v-if="$store.state.token" to="/me/disciplinas">Mis Disciplinas</router-link>
      <router-link class="navbar-brand" v-if="$store.state.token" to="/perfil">Mi Perfil</router-link>
      <router-link class="navbar-brand" v-if="$store.state.token" to="/carnet">Carnet</router-link>
      <router-link class="navbar-brand" to="/estadisticas">Estadisticas</router-link>
      <router-link class="navbar-brand" to='/login' v-if="$store.state.token" @click="logout">Cerrar Sesion</router-link>
  </nav>
  <router-view />
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch('logout');
      location.reload();
    },
  },
  mounted() {
    this.$store.commit('initializeStore')
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000203;
}

nav {
  padding: 30px;
}

nav a {
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.chartBox {
   width: 600px;
   height: 600px;
}

</style>
