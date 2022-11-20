<template>
  {{ total }}
  <table class="table table-hover">
    <thead>
      <tr>
        <td>Mes</td>
        <td>Acción</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="pay in payment" :key="pay">
        <td>{{ pay.mes }}</td>
        <button @click="registerPayment(pay.mes, total)">Pagar</button>
        <button @click="emitirComporbante(pay.mes, total)">Emitir comprobante</button>
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
      total: 0,
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

    apiService
      .get("me/payments/total")
      .then((response) => {
        this.total = response.data.total;
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
          if (response.status === 200) {
            alert("Se generò el pago")
            this.$router.push("/perfil")
          }
        })
        .catch((e) => {
          this.errores.push(e);
        });
    },
    emitirComporbante(mes, total) {
      this.$router.push({ path: 'comprobante', props: { mes: mes, total: total } })

    },

  },

}

</script>
