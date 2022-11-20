<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/disciplinas">Disciplinas</router-link> |
    <router-link v-if="$store.state.token === null" to="/login">Login</router-link> |
    <router-link to='/login' v-if="$store.state.token" @click="logout">Cerrar Sesion</router-link> |
    <router-link v-if="$store.state.token" to="/payment">Realizar Pago</router-link> |
    <router-link v-if="$store.state.token" to="/me/disciplinas">Mis Disciplinas</router-link> |
    <router-link v-if="$store.state.token" to="/perfil">Mi Perfil</router-link> |
    <router-link v-if="$store.state.token" to="/carnet">Carnet</router-link> |
    <router-link v-if="$store.state.token" to="/estadisticas">Estadisticas</router-link>
  </nav>
  <router-view />
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch('logout');
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
  font-weight: bold;
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
