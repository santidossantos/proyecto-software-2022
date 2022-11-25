<template>
  <div class="home">
    <Home />
  </div>
</template>

<script>
// @ is an alias to /src
import Home from "@/components/Home.vue";

export default {
  name: "HomeView",
  components: {
    Home,
  },
};
</script>

<style>
.home {
  width: 100%;
  height: 100vh;
  background-color: #e2dfdf;
  font-family: "Share Tech", sans-serif;
  position: relative;
}
</style>
