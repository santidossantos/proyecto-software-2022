<template>
     <div class="chartBoxContent">
      <h1 class="titulo">Cantidad de nuevos asociados por mes{{msg}}</h1>
      <canvas id="myChart3"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 

 let url = process.env.VUE_APP_RUTA + "club/asociadosMesCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')

     const ctx = document.getElementById('myChart3');

     this.data = {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [{
            label: 'cantidad',
            data: [],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },

    this.myChart3 = new Chart(ctx, {
    type: 'line',
    data: this.data,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
    },
      methods:{
    mostrar() {
         axios
        .get(url)
            .then(response => {
            console.log(response.data) //traemos todos los datos desde la API
            //vacio el vector de cantidad
            response.data.forEach(element => {
                this.data.datasets[0].data.push(element.cantidad)
                console.log("contenido de cantidad inscripciones: ", this.data.datasets[0].data)
                this.myChart3.update()
            })        
            //console.log(document.getElementById('line-chart'))//el ID donde se genera el grafico es 'line-chart'                    
        })
    }
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