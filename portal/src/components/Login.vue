<template>
    <div class="hello">
        <h1>{{ token }}</h1>
        <form action class="form" @submit.prevent="register">
            <label class="form-label" for="#email">Email:</label>
            <input v-model="email" class="form-input" type="email" id="email" required placeholder="Email">
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
            email: "",
            password: "",
            errores: []
        }
    },

    methods: {

        register() {
            console.log(this.email);
            console.log(this.password);
            const user = {
                "email": this.email,
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
        const response = await apiService.post('/auth/token', user)
        localStorage.setItem('jwt', response.data.token);
        console.log(response.data)
    }
};
</script>


