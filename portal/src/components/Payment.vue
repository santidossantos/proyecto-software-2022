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
      <div ref="content" class="hidden">
        <h1>Hola</h1>
        <br>
        <h1>Como va</h1>
        <span>prueba</span>
      </div>
    </tbody>
  </table>
</template>

<script>
import { apiService } from "@/services/api";

import jsPDF from "jspdf";
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
      const doc = new jsPDF();
      const mess = mes;
      /** WITHOUT CSS */
      const contentHtml = this.$refs.content.textContent + mes + total;
      //const contentHtml2 = contentHtml.textHTML = mes
      //const contentHtml3 = contentHtml2.textHTML = total
      doc.text(contentHtml, 15, 15, {
        width: 170
      });
      doc.save("Comprobante.pdf");
    },

  },

}

</script>

<style>
.hidden{
  display:none
}
</style>