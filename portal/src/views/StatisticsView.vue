<template>
  <div class="est">
    <h1>Estadisticas</h1>
    <Estadisticas />
    <EstadisticasGenero />
  </div>
</template>

<script>
// @ is an alias to /src
import Estadisticas from "@/components/Estadisticas.vue";
import EstadisticasGenero from "@/components/EstadisticasGenero.vue";

export default {
  name: "StatisticsView",
  components: {
    Estadisticas,
    EstadisticasGenero
  },
  
};
</script>
