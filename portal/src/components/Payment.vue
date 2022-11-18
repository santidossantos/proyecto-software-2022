<template>
    <table class="table table-hover table-dark m-3">
        <thead>
            <tr>
                <td>Mes</td>
                <td>Fecha</td>
            </tr>
        </thead>
        <tbody>
            <tr v-for="pay in payment" :key="pay">
                <td>{{ pay.month }}</td>
                <td>{{ pay.amount }}</td>

            </tr>
        </tbody>
    </table>
</template>
  
<script>
import axios from 'axios';
export default {
    data() {
        return {
            payment: [],
            errores: []
        }
    },
    // Fetches posts when the component is created.
    created() {
        axios.get('http://localhost:5000/api/me/payments/1')
            .then(response => {
                // JSON responses are automatically parsed.
                this.payment = response.data;
            })
            .catch(e => {
                this.errores.push(e)
            })
    }
}
</script>