<template>
  <DisciplinasList :disciplinas="disciplinas" />
</template>

<script>
import { apiService } from "@/services/api";
import DisciplinasList from "./DisciplinasList.vue";

export default {
  data() {
    return {
      disciplinas: [],
      errores: [],
    };
  },
  async created() {
    apiService
      .get("club/disciplines")
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
