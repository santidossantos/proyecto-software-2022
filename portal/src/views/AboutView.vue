<template>
    <h1 class="title">Listado de Disciplinas</h1>
    <Disciplinas />
</template>

<script>
// @ is an alias to /src
import Disciplinas from "@/components/Disciplinas.vue";

export default {
  name: "AboutView",
  components: {
    Disciplinas,
  },
};
</script>
