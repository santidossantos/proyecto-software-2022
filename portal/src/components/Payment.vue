<template>
  <p>Pagando las cuotas despues del dia 10 se incluye un recargo del {{ this.recargoo }}%</p>
  <table v-if="payment.status == null" class="table table-hover">
    <thead>
      <tr>
        <td>Mes</td>
        <td>Total</td>
        <td>Acción</td>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(pay, index) in payment" :key="index">
        <td>{{ meses[pay.mes] }}</td>
        <td v-if="pay.total == 0">{{ total / this.payment.length + recargo(total / this.payment.length, pay.mes) }}</td>
        <td v-if="pay.total != 0">{{ pay.total }}</td>
        <td>
          <button class="btn btn-success" v-if="pay.total == 0"
            @click="registerPayment(pay.mes, (total / this.payment.length + recargo(total / this.payment.length, pay.mes)))">
            Pagar
          </button>
          <button class="btn btn-info" v-if="pay.total != 0" @click="
            emitirComporbante(
              meses[pay.mes],
              pay.total,
              pay.nroComprobante
            )
          ">
            Emitir comprobante
          </button>
        </td>
      </tr>
      <div ref="content" class="hidden">
        <h1>#Recibo {{ "\n" }}</h1>
        <h1>
          Se registra el pago del asociado {{ $store.state.username }}
          {{ "\n" }}
        </h1>
        El mes de <span id="mes"></span> Un Monto de $<span id="monto"></span>
        {{ "\n" }}
        <li class="list-group-item" v-show="date">
          <strong>Fecha de Emision:</strong> {{ date }} {{ "\n" }}
        </li>
      </div>
    </tbody>
  </table>
  <p v-else>No se ecnontraron resultados</p>
  <div class="section_comprobante">
    <h3>Subir Comprobante</h3>
    <input ref="fileInput" type="file" @change="previewFiles($event)" />
    <button class="btn btn-success" @click="submitFiles">guardar</button>
  </div>
</template>

<script>
import { apiService } from "@/services/api";

import jsPDF from "jspdf";

import axios from "axios";

export default {
  data() {
    return {
      payment: [],
      total: 0,
      errores: [],
      date: "",
      meses: {
        E: "Enero",
        F: "Febrero",
        Mar: "Marzo",
        Abr: "Abril",
        May: "Mayo",
        Jun: "Junio",
        Jul: "Julio",
        Ago: "Agosto",
        S: "Septiembre",
        O: "Octubre",
        N: "Noviembre",
        D: "Diciembre",
        Enero: 1,
        Febrero: 2,
        Marzo: 3,
        Abril: 4,
        Mayo: 5,
        Junio: 6,
        Junio: 7,
        Agosto: 8,
        Septiembre: 9,
        Octubre: 10,
        Noviembre: 11,
        Diciembre: 12,
      },
      comprobante: null,
      recargoo: 0,
    };
  },
  async created() {
    axios
      .get(process.env.VUE_APP_RUTA + "me/paymentsinfo", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.payment = response.data;
      })
      .catch((e) => {
        this.errores.push(e);
      });

    axios
      .get(process.env.VUE_APP_RUTA + "config/porcentaje")
      .then((response) => {
        this.recargoo = response.data.porcentaje;
      })
      .catch((e) => {
        this.errores.push(e);
      });

    axios
      .get(process.env.VUE_APP_RUTA + "me/payments/total", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.total = response.data.total;
      })
      .catch((e) => {
        this.errores.push(e);
      });
    this.date = this.printDate();
  },
  methods: {
    recargo(total, mes) {
      const mesDeHoy = new Date().getMonth() + 1;
      const mesTex = this.meses[mes];
      const mesApagar = this.meses[mesTex];
      const date = new Date().toLocaleDateString();
      const [day, month, year] = date.split("/");
      console.log(day);
      if ((mesDeHoy === mesApagar && day > 10) || (mesApagar < mesDeHoy))
        return total * (this.recargoo / 100);
      else
        return 0;
    },
    previewFiles(event) {
      this.comprobante = event.target.files[0];
      console.log(this.comprobante);
    },
    submitFiles() {
      if (this.comprobante == null) {
        return;
      }
      let InstFormData = new FormData();
      InstFormData.append("file", this.comprobante);
      console.log(InstFormData);
      axios
      apiService
        .post(process.env.VUE_APP_RUTA + "SaveArchivo",
          InstFormData )
        .then((response) => {
          console.log("File upload successful!");
          this.$refs.fileInput.value = "";
          alert("Comprobante guardado con exito");
          location.reload();
        })
        .catch((error) => {
          console.log("File upload failed.");
          console.error(error);
        });
    },
    printDate: function () {
      return new Date().toLocaleDateString();
    },
    registerPayment(mes, total) {
      // if (this.payment.length != 0) {
      //   total = total / this.payment.length;
      // }
      const formData = {
        month: mes,
        total: total,
      };
      console.log(formData);
      apiService
        .post("me/payments", formData)
        .then((response) => {
          console.log(response);
          if (response.status === 200) {
            alert("Se generò el pago");
            location.reload();
          }
        })
        .catch((e) => {
          this.errores.push(e);
        });
    },
    emitirComporbante(mes, total, nroComprobante) {
      var doc = new jsPDF({
        orientation: "landscape",
      });
      const htmlMes = (document.getElementById("mes").innerHTML = mes + "\n");
      const htmlMonto = (document.getElementById("monto").innerHTML = total);
      const contentHtml = this.$refs.content.innerText;
      doc.text(contentHtml, 15, 15, {
        width: 170,
      });
      doc.save(nroComprobante + "-Comprobante.pdf");
    },
  },
};
</script>

<style>
.hidden {
  display: none;
}

.section_comprobante {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  bottom: 1rem;
  border: 0.5px solid #198754;
  box-shadow: -10px 0px 0px 0px #198754;
  width: 40%;
  border-radius: 5px;
  gap: 1rem;
  margin: auto;
}
</style>
