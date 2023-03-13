<!-- PWAPrompt.vue -->
<template>
  <br />
  <div v-if="shown" class="btn btn-warning btn-sm">
    ¿Desea instalar la aplicación?

    <div class="promt">
      <button class="btn btn-success btn-sm" @click="installPWA">
        Instalar
      </button>
      
      <button class="btn btn-danger btn-sm" @click="dismissPrompt">
        No, gracias
      </button>
    </div>

  </div>
</template>

<script>
export default {
  data: () => ({
    shown: false,
  }),

  beforeMount() {
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault()
      this.installEvent = e
      this.shown = true
    })
  },

  methods: {
    dismissPrompt() {
      this.shown = false
    },

    installPWA() {
      this.installEvent.prompt()
      this.installEvent.userChoice.then((choice) => {
        this.dismissPrompt() // Hide the prompt once the user's clicked
        if (choice.outcome === 'accepted') {
          // Do something additional if the user chose to install
        } else {
          // Do something additional if the user declined
        }
      })
    },
  }
}
</script>

<style>

.btn btn-info btn-sm {
    margin-right: 3px;
    margin-left: 3px;
}

</style>