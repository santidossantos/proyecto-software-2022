<template>
  <div class="about">
    <h1 class="title">Listado de Pagos</h1>
    <Payment />
  </div>
</template>

<script>
// @ is an alias to /src
import Payment from "@/components/Payment.vue";

export default {
  name: "PaymentView",
  components: {
    Payment,
  },
};
</script>
