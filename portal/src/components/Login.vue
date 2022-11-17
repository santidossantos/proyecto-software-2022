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

export default {
    data() {
        return {
            token: "",
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

const apiService = axios.create({
    baseURL: 'http://localhost:5000/api',
    xsrfCookieName: 'csrf_access_token'
});

const actions = {
    async loginUser(user) {
        const response = await apiService.post('/auth/token', user)
        console.log(response.data)
    }
};
</script>