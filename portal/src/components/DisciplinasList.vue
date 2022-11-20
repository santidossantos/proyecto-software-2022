<template>
  <table v-if="disciplinas.length != 0" class="table table-hover">
    <thead>
      <tr>
        <td>Nombre</td>
        <td>Dias y Horarios</td>
        <td>Instructures</td>
        <td>Costo Mensual</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="disciplina in disciplinas" :key="disciplina">
        <td>{{ disciplina.name }}</td>
        <td>{{ disciplina.daysAndHours }}</td>
        <td>{{ disciplina.nameInstructors }}</td>
        <td>{{ disciplina.monthlyCost }}</td>
      </tr>
    </tbody>
  </table>
  <p v-else>No se ecnontraron resultados</p>
</template>

<script>
export default {
  name: "DisciplinasList",
  props: {
    disciplinas: [],
  }
};
</script>
