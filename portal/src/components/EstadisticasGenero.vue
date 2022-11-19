<template>
    <div class="chartBox">
      <h1>Cantidad de asociados por genero {{msg}}</h1>
      <canvas id="myChart2"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 
 let cantidad = []

 let url = "http://127.0.0.1:5000/api/club/generosCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')

     const ctx = document.getElementById('myChart2');

     const myChart2 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Hombres', 'Mujeres'],
        datasets: [{
            label: 'cantidad',
            data: cantidad,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
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
                cantidad.push(element.hombres)
                cantidad.push(element.mujeres)
            })        
            //console.log(document.getElementById('line-chart'))//el ID donde se genera el grafico es 'line-chart'                    
        })
    }
  } 
 }
</script>