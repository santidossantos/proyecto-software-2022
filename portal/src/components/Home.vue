<template>
  <div class="hello">
    <h1>Bienvenido</h1>
    <button @click="download()">Download PDF WITH CSS</button>
    <div ref="content">>
      <h1>Hola</h1>
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

    downloadWithCSS() {
      const doc = new jsPDF();
      /** WITH CSS */
      var canvasElement = document.createElement('canvas');
      html2canvas(this.$refs.content, { canvas: canvasElement }).then(function (canvas) {
        doc.html(canvas.content);
        doc.save("sample.pdf");
      });
    },
    // download() {
    //   const doc = new jsPDF();
    //   /** WITHOUT CSS */
    //   const contentHtml = this.$refs.content.innerHTML;
    //   doc.html(contentHtml, 15, 15, {
    //     width: 170
    //   });
    //   doc.save("sample.pdf");
    // }
  },

}

</script>


