<template>
  <div class="hello">
    <h1>Bienvenido</h1>
    <button @click="download()">Download PDF WITH CSS</button>
    <div ref="content" class="hidden">
      <h1>Hola</h1>
      <br>
      <h1>Como va</h1>
      <span>prueba</span>
    </div>
  </div>
</template>

<script>

import jsPDF from "jspdf";
import html2canvas from "html2canvas"
export default {
  name: "Home",
  // props: {
  //   msg: String
  // },
  methods: {

    // generatePdf() {
    //   const doc = new jsPDF();

    //   doc.fromHTML(this.$refs.testHtml);

    //   doc.save('test.pdf');
    // },

    // downloadWithCSS() {
    //   const doc = new jsPDF();
    //   const hola = "una variable cualquiera"
    //   /** WITH CSS */
    //   var canvasElement = document.createElement('canvas');
    //   html2canvas(this.$refs.content, { canvas: canvasElement }).then(function (canvas) {
    //     doc.text(hola, '10', '10');
    //     doc.save("sample.pdf");
    //   });
    // },
    download() {
      const doc = new jsPDF();
      /** WITHOUT CSS */
      const contentHtml = this.$refs.content.textContent;
      doc.text(contentHtml, 15, 15, {
        width: 170
      });
      doc.save("Comprobante.pdf");
    }
  },

}

</script>

<style>
.hidden{
  display:none
}
</style>

