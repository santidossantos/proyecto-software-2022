<template>
   <div class="est">
      <h1>Cantidad de nuevas inscripciones por mes {{msg}}</h1>
      <canvas id="myChart3" width="100" height="100"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 
 let cantidad = []

 let url = "http://127.0.0.1:5000/api/club/asociadosMesCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')

     const ctx = document.getElementById('myChart3');

     const myChart3 = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [{
            label: 'cantidad',
            data: cantidad,
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },
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
            cantidad = []
            response.data.forEach(element => {
                console.log(element.disciplina) //todoss los console log son testss
                cantidad.push(element.cantidad)
            })        
            //console.log(document.getElementById('line-chart'))//el ID donde se genera el grafico es 'line-chart'                    
        })
    }
  } 
 }
</script>