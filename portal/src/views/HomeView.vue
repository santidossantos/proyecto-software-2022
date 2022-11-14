<template>
  <div class="home">
    <Home />
    <img alt="Vue logo" src="../assets/logovillaelisa.png" />
  </div>
</template>

<script>
// @ is an alias to /src
import Home from "@/components/Home.vue";

export default {
  name: "HomeView",
  components: {
    Home
  },
};
</script>
