<template>
  <div class="d">
  <div class="content-home">
    <img class="img" alt="Vue logo" src="../assets/logovillaelisa.png" />
    <p class="textBienvenid">
      Bienvenido al Club deportivo de Villa Elisa. Nuestro club cuenta con una
      amplia trayectoria en diferentes disciplinas. Puede acceder a ellos a
      través de la barra superior y conocer los horarios y profesores
      disponibles.
    </p>
  </div>
  <!-- <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1>
  <h1>fsfd</h1> -->
</div>
</template>

<script>
export default {
  name: "Home",
  //props: {
  //msg: String,
  //},
};
</script>

<style>
.textBienvenid {
  padding-left: 7rem;
  padding-top: 0.5rem;
  text-align: center;
  color: rgb(246, 239, 239);
}
.content-home {
  display: flex;
  flex-direction: row;
  background-color: black;
  max-height: 4rem;
}
.img {
  padding-left: 1rem;
  position: absolute;
  width: 10rem;
  height: 10rem;
}
.d{
  /* background-image: url("../assets/club.png");
  background-repeat: no-repeat;
  background-position: 20px 30px; */
  background-position: center center;
  width: 100%;
  height: 700px;
  background-repeat: no-repeat;
  background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("../assets/club.png");
  
}
</style>
