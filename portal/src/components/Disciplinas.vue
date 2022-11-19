<template>
  <table class="table table-hover table-dark m-3">
    <thead>
      <tr>
        <td>Nombre</td>
        <td>Dias y Horarios</td>
        <td>Instructures</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="disciplina in disciplinas" :key="disciplina">
        <td>{{ disciplina.name }}</td>
        <td>{{ disciplina.daysAndHours }}</td>
        <td>{{ disciplina.nameInstructors }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      disciplinas: [],
      errores: []
    }
  },
  // Fetches posts when the component is created.
  created() {
    axios.get('http://127.0.0.1:5000/api/club/disciplines', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('jwt')}`,
      }

    })
      .then(response => {
        // JSON responses are automatically parsed.
        this.disciplinas = response.data;
      })
      .catch(e => {
        this.errores.push(e)
      })
  }
}
</script>