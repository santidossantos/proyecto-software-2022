<!-- PWAPrompt.vue -->
<template>
  <br />
  <div v-if="shown" class="alert">
    ¿Desea instalar la aplicación?

      <button class="btn btn-success btn-sm me-1" @click="installPWA">
        Instalar
      </button>
      
      <button class="btn btn-secondary btn-sm" @click="dismissPrompt">
        No, gracias
      </button>
   

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

.alert {
  display: revert;
  font-size: 1rem;
  background-color: bisque;
  padding: 0;
}

.button-container {
  justify-content: space-between;
  margin: 2px;
}

</style>