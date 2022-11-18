<template>
   <div class="est">
      <h1>Hola {{msg}}</h1>
      <canvas id="myChart" width="400" height="400"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 
 let url = "http://127.0.0.1:5000/api/club/disciplinesCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')

     const ctx = document.getElementById('myChart');

     const data = {
     labels: this.data,
     datasets: [{
        label: this.data,
        data: [300, 50, 100],
        backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
     }]
     };

   const myChart = new Chart(ctx, {
   type: 'doughnut',
   data: data,
   });
   },
   methods:{
      mostrar(){
            axios
               .get(url)
                  .then(response => {
                     response.data.array.forEach(element => {
                        this.data.push(element.disciplina)
                        this.data.push(element.inscriptos)
                     })
                  })
      }
   }
  };
</script>