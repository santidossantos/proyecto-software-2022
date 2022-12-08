<template>
  <div class="wrapper">
    <div class="logo">
      <img src="../assets/logovillaelisa.png" alt="" />
    </div>
    <div class="text-center mt-4 name">Iniciar Sesion</div>
    <form class="p-3 mt-3" @submit.prevent="register">
      <div class="form-field d-flex align-items-center">
        <span class="far fa-user"></span>
        <input v-model="username" class="form-input" type="text" id="username" required
          placeholder="Nombre de usuario" />
      </div>
      <div class="form-field d-flex align-items-center">
        <span class="fas fa-key"></span>
        <input v-model="password" class="form-input" type="password" id="password" placeholder="Contraseña" />
      </div>
      <input class="btn mt-3" type="submit" value="Login" @click="displayError">
    </form>
  </div>
</template>

<script>

export default {

  data() {
    return {
      token: "",
      username: "",
      password: "",
      errores: [],
    };
  },

  methods: {

    register() {
      const formData = {
        username: this.username,
        password: this.password,
      };

      this.$store.dispatch("login", formData);
    },

    displayError() {
      setTimeout(() => {
        if (this.$store.state.error_msg != '' && this.$store.state.token === null) {
          this.$toast.error(this.$store.state.error_msg, {
            max: 1,
            position: "bottom",
            duration: 2000,
          });
        }
      }, "200")
    },
  },
};
</script>

<style>
/* Importing fonts from Google */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap");

/* Reseting */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

body {
  background: #ecf0f3;
}

.wrapper {
  max-width: 350px;
  min-height: 500px;
  margin: 80px auto;
  padding: 40px 30px 30px 30px;
  background-color: #ecf0f3;
  border-radius: 15px;
  box-shadow: 13px 13px 20px #cbced1, -13px -13px 20px #fff;
}

.logo {
  width: 80px;
  margin: auto;
}

.logo img {
  width: 100%;
  height: 80px;
  object-fit: cover;
  border-radius: 50%;
  box-shadow: 0px 0px 3px #5f5f5f, 0px 0px 0px 5px #ecf0f3, 8px 8px 15px #a7aaa7,
    -8px -8px 15px #fff;
}

.wrapper .name {
  font-weight: 600;
  font-size: 1.4rem;
  letter-spacing: 1.3px;
  padding-left: 10px;
  color: #555;
}

.wrapper .form-field input {
  width: 100%;
  display: block;
  border: none;
  outline: none;
  background: none;
  font-size: 1.2rem;
  color: #666;
  padding: 10px 15px 10px 10px;
  /* border: 1px solid red; */
}

.wrapper .form-field {
  padding-left: 10px;
  margin-bottom: 20px;
  border-radius: 20px;
  box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;
}

.wrapper .form-field .fas {
  color: #555;
}

.wrapper .btn {
  box-shadow: none;
  width: 100%;
  height: 40px;
  background-color: #07090a;
  color: #fff;
  border-radius: 25px;
  box-shadow: 3px 3px 3px #b1b1b1, -3px -3px 3px #fff;
  letter-spacing: 1.3px;
}

.wrapper .btn:hover {
  background-color: #039be5;
}

.wrapper a {
  text-decoration: none;
  font-size: 0.8rem;
  color: #03a9f4;
}

@media (max-width: 380px) {
  .wrapper {
    margin: 30px 20px;
    padding: 40px 15px 15px 15px;
  }
}
</style>
