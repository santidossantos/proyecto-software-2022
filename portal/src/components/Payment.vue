<template>
    <table class="table table-hover">
        <thead>
            <tr>
                <td>Mes</td>
                <td>Total</td>
                <td>Acción</td>
            </tr>
        </thead>
        <tbody>
            <tr v-for="pay in payment" :key="pay">
                <td>{{ pay.mes }}</td>
                <td>{{ pay.total }}</td>
                <button @click="registerPayment(pay.mes, pay.total)">Pagar </button>
            </tr>
        </tbody>
    </table>
</template>

<script>
import { apiService } from "@/services/api";
export default {
    data() {
        return {
            payment: [],
            errores: [],
        };
    },
    // Fetches posts when the component is created.
    created() {
        apiService
            .get("/me/payments")
            .then((response) => {
                // JSON responses are automatically parsed.
                this.payment = response.data;
            })
            .catch((e) => {
                this.errores.push(e);
            });
    },

    methods: {
        registerPayment(mes, total) {
            const formData = {
                month: mes,
                total: total
            };
            apiService
                .post("/me/payments", formData)
                .then((response) => {
                    // JSON responses are automatically parsed.
                    this.createPayment = response.data;
                })
                .catch((e) => {
                    this.errores.push(e);
                });
        },
    },
};
</script>
