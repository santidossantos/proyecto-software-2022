<template>
   <div class="chartBoxContent">
      <h1 class="titulo">Cantidad de insciptos por disciplinas {{msg}}</h1>
      <canvas id="myChart"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';

 let url = process.env.VUE_APP_RUTA + "club/disciplinesCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')
     const ctx = document.getElementById('myChart');
     this.data = {
      labels: [],
      datasets: [{
        label: 'Inscripciones',
        data: [],
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)',
          'rgb(75, 192, 192)',
          'rgb(153, 102, 255)',
          'rgb(255, 159, 64)',
          'rgb(255, 85, 85)',
          'rgb(32, 163, 200',
          'rgb(255, 255, 45)',
          'rgb(20, 255, 115)',
          'rgb(200,150,75)',
          'rgb(150, 50, 200)',
          'rgb(75, 83, 100)',
          'rgb(255, 24, 107)',
          'rgb(255, 98, 255)',
          'rgb(230, 100, 32)',
          'rgb(60, 60, 60)',
          'rgb(46, 178, 100)',
          'rgb(90, 130, 140)',
          'rgb(180, 180, 180)',
          'rgb(220, 50, 89)',
        ],
        hoverOffset: 4
      }]
    };

    this.myChart = new Chart(ctx, {
    type: 'doughnut',
    data: this.data,
    });
    console.log("contenido de labels: ",this.data.labels)
    console.log("contenido de data: ",this.data.datasets[0].data)
    },
    
  methods:{
    mostrar() {
         axios
        .get(url)
            .then(response => {
            console.log(response.data) //traemos todos los datos desde la API
            //vacio el vector disciplinas
            response.data.forEach(element => {
              //guarda element.disciplina en el vector de labels de la linea 32
              this.data.labels.push(element.disciplina)
              //guarda element.inscriptos en el vector data de la linea 31
              this.data.datasets[0].data.push(element.inscriptos)
              this.myChart.update()
            })        
            //console.log(document.getElementById('line-chart'))//el ID donde se genera el grafico es 'line-chart'                    
        })
    },
  } 
}
</script>

<style>
.titulo{
  font-size: 1rem;
}
.chartBoxContent{
  max-width: 100vh;
  max-height: 50vh;
}
</style>