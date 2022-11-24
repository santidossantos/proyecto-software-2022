<template>
      <h1 class="title">Disciplinas las que se encuentra inscripto</h1>
      <MisDisciplinas />
  </template>
  
  <script>
  import MisDisciplinas from "@/components/MisDisciplinas.vue";
  
  export default {
    name: "MisDisciplinasView",
    components: {
      MisDisciplinas,
    },
  };
  </script>

<style>
.title{
  padding: 1rem;
}
</style>