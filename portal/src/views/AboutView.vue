<template>
  <div class="about">
    <h1>Listado de Disciplinas</h1>
    <Disciplinas />
  </div>
</template>

<script>
// @ is an alias to /src
import Disciplinas from "@/components/Disciplinas.vue";

export default {
  name: "AboutView",
  components: {
    Disciplinas
  },
};
</script>
