<template>
  <DisciplinasList :disciplinas="disciplinas" />
</template>

<script>
import DisciplinasList from "./DisciplinasList.vue";
import axios from "axios";

export default {
  data() {
    return {
      disciplinas: [],
      errores: [],
    };
  },
  async created() {
    axios
      .get(process.env.VUE_APP_RUTA + "club/disciplines")
      .then((response) => {
        this.disciplinas = response.data;
      })
      .catch((e) => {
        this.errores.push(e);
      });
  },
  components: { DisciplinasList },
};
</script>
