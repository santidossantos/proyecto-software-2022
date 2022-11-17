<template>
  <div class="est">
    <h1>Estadisticas</h1>
    <Estadisticas />
  </div>
</template>

<script>
// @ is an alias to /src
import Estadisticas from "@/components/Estadisticas.vue";

export default {
  name: "StatisticsView",
  components: {
    Estadisticas
  },
};
</script>
