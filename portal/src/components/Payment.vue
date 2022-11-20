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
        <button @click="registerPayment(pay.mes, pay.total)">Pagar</button>
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
  async created() {
    apiService
      .get("me/payments")
      .then((response) => {
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
        total: total,
      };
      console.log(formData)
      apiService
        .post("me/payments", formData)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response);
        })
        .catch((e) => {
          this.errores.push(e);
        });
    },
  },
};
</script>
