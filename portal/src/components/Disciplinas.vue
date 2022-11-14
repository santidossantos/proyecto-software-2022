<template>
    <div class="hello">
      <h1>{{disciplinas}}</h1>
    </div>
  </template>

<script>
import axios from 'axios';
  export default {
  data() {
    return {
      disciplinas: [],
      errors: []
   }
  },
  // Fetches posts when the component is created.
  created() {
    axios.get('http://127.0.0.1:5000/api/club/disciplines')
    .then(response => {
    // JSON responses are automatically parsed.
    this.disciplinas = response.data;
    })
    .catch(e => {
    this.errors.push(e)
    })
  }
}
</script>