<template>
   <div class="est">
      <h1>Cantidad de insciptos por disciplinas {{msg}}</h1>
      <canvas id="myChart" width="100" height="100"></canvas>
   </div>
</template>

<script>
 import Chart from 'chart.js/auto';
 import axios from 'axios';
 
 let disciplinas = []
 let inscriptos = []

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
  
    let data = {
      labels: disciplinas,
      datasets: [{
        label: 'Inscripciones',
        data: inscriptos,
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
    mostrar() {
         axios
        .get(url)
            .then(response => {
            console.log(response.data) //traemos todos los datos desde la API
            //vacio el vector disciplinas
            disciplinas = []
            inscriptos = []
            response.data.forEach(element => {
               // console.log(element.disciplina) //todoss los console log son testss
                //console.log(url)
               // console.log(disciplinas)
                disciplinas.push(element.disciplina)
                inscriptos.push(element.inscriptos)
               // console.log(inscriptos)
            })        
            //console.log(document.getElementById('line-chart'))//el ID donde se genera el grafico es 'line-chart'                    
        })
    }
  } 
}
</script>