<template>
    <div  class="chartBoxContent">
      <h1 class="titulo">Cantidad de asociados por genero {{msg}}</h1>
      <canvas id="myChart2"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 
 let cantidad = []

 let url = process.env.VUE_APP_RUTA + "club/generosCant"
 export default { 
    name: "Home",
    props: {
      msg: String,
    },
    mounted(){
     this.mostrar()
     console.log('component mounted.')

     const ctx = document.getElementById('myChart2');
    
    this.data={
        labels: ['Hombres', 'Mujeres', 'Otros'],
        datasets: [{
            label: 'cantidad',
            data: [],
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
    }

    this.myChart2 = new Chart(ctx, {
    type: 'bar',
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
            cantidad = []
            response.data.forEach(element => {
                console.log(element.disciplina) //todoss los console log son testss
                this.data.datasets[0].data.push(element.hombres)
                this.data.datasets[0].data.push(element.mujeres)
                this.data.datasets[0].data.push(element.otros)
                console.log("contenido labels: ", this.data.labels)
                console.log("contenido data: ", this.data.datasets[0].data)
                this.myChart2.update()
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
  max-height: 80vh;
}
</style>
