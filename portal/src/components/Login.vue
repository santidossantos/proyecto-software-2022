<template>
    <div class="hello">
        <form action class="form" @submit.prevent="register">
            <label class="form-label" for="#email">Nombre de Usuario:</label>
            <input v-model="username" class="form-input" type="text" id="username" required placeholder="Email">
            <label class="form-label" for="#password">Password:</label>
            <input v-model="password" class="form-input" type="password" id="password" placeholder="Password">
            <input class="form-submit" type="submit" value="Login">
        </form>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            token: "",
            username: "",
            password: "",
            errores: []
        }
    },

    methods: {
        register() {
            const user = {
                "username": this.username,
                "password": this.password

            }
            actions.loginUser(user)
        }
    },
}

const apiService = axios.create({
    baseURL: 'http://localhost:5000/api',
    xsrfCookieName: 'csrf_access_token'
});

const actions = {
    async loginUser(user) {
        const response = await apiService.post('/auth', user)
        localStorage.setItem('jwt', response.data.token);
        console.log(response.data)
    }
};
</script>


