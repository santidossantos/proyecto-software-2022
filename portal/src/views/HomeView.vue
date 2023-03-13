<template>
  <div class="home">
    <PromptPwa/>
    <Home />
  </div>
</template>

<script>
// @ is an alias to /src
import Home from "@/components/Home.vue";
import PromptPwa from "@/components/PromptPwa.vue";

export default {
  name: "HomeView",
  components: {
    Home,
    PromptPwa
},
};
</script>

<style>



.home {
  width: 100%;
  height: 100vh;
  font-family: "Share Tech", sans-serif;
  position: relative;
}

@media screen and (max-width: 869px) {
  .home {
    height: 100%;
  }
}

</style>
