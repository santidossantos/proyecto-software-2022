<template>
    <div class="hello">
        <h1>{{ token }}</h1>

        <form action="">
            <label for="nombre">
                <span>¿Cuál es tu nombre?</span>
                <input type="text" id="email" placeholder="email">
            </label>
            <label for="inicio-platzi">
                <span>¿Contraseña?</span>
                <input type="text" id="password" placeholder="password">
            </label>
        </form>


    </div>
</template>
  
<script>
import axios from 'axios';

const apiService = axios.create({
    baseURL: 'http://localhost:5000/api',
    withCredentials: true,
    xsrfCookieName: 'csrf_access_token'
});



const actions = {
    async loginUser(user) {
        await apiService.post('/auth/token', user)
        await fetchUser()
    },
    async fetchUser() {
        await apiService.get('/auth/user_jwt')
            .then(({ data }) => console.log(data))
    },

    //  async logoutUser({ commit }) {
    //  await apiService.get('/auth/logout_jwt');
    //  commit('logoutUserState');
    //  }
};


export default {
    data() {
        return {
            token: {},
            errores: []
        }
    },
    // Fetches posts when the component is created.

    created() {
        const user = {
            "email": "admin@gmail.com",
            "password": "1234"
        }
        actions.loginUser(user)
    }


}



</script>