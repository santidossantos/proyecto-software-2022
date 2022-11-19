<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/disciplinas">Disciplinas</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/payment">Pagos</router-link> |
    <router-link to="/">Realizar Pago</router-link> |
    <router-link to="/perfil">Perfil</router-link> |
  </nav>
  <router-view />
</template>

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
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
