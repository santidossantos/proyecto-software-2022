<template>
  <div class="page-content page-container">
    <div class="padding d-flex justify-content-center">
      <div class="row container d-flex justify-content-center">
        <div class="col-xl-6 col-md-12 mt-5">
          <div class="card user-card-full">
            <div class="row m-l-0 m-r-0">
              <div class="col-sm-4 bg-c-lite-green user-profile">
                <div class="card-block text-center text-white">
                  <div class="m-b-25">
                    <div class="m-b-25">
                      <img
                        src=""
                        class="rounded-circle border border-dark border-1"
                        id="img"
                        width="90"
                        height="90"
                      />
                    </div>
                  </div>
                  <h6 class="f-w-600">Asociado</h6>
                  <p>{{ associated.name }} {{ associated.last_name }}</p>
                  <i
                    class="mdi mdi-square-edit-outline feather icon-edit m-t-10 f-16"
                  ></i>
                </div>
              </div>
              <div class="col-sm-8 div-card">
                <div class="card-block">
                  <h6 class="m-b-20 p-b-5 b-b-default f-w-600">Carnet Digital</h6>
                  <div class="row">
                    <div class="col-sm-6">
                      <p class="m-b-10 f-w-600">Email</p>
                      <h6 class="text-muted f-w-400">{{ associated.email }}</h6>
                    </div>
                    <div class="col-sm-6">
                      <p class="m-b-10 f-w-600">Teléfono</p>
                      <h6 class="text-muted f-w-400">{{ associated.mobile_number }}</h6>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-sm-6">
                      <p class="m-b-10 f-w-600">{{ associated.document_type }}</p>
                      <h6 class="text-muted f-w-400">{{ associated.dni }}</h6>
                    </div>
                    <div class="col-sm-6">
                      <p class="m-b-10 f-w-600">N° Socio</p>
                      <h6 class="text-muted f-w-400">{{ associated.member_number }}</h6>
                    </div>
                  </div>
                  <h6 class="m-b-20 m-t-40 p-b-5 b-b-default f-w-600"></h6>
                  <div class="row">
                    <div class="col-sm-6">
                      <p class="m-b-10 f-w-600">Estado</p>
                        <h6 style="color : red" v-if="associated.defaulter">Moroso</h6>
                        <h6 style="color : green" v-else>Al día</h6>
                      <p class="m-b-10 f-w-600">Fecha Alta</p>
                      <h6 class="text-muted f-w-400">{{ associated.create_at }}</h6>
                    </div>

                    <div class="col-sm-6 mt-3">
                      <qrcode-vue
                        :value="QRValue"
                        :size="size"
                        level="H"
                        style="float: right"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/services/api";
import QrcodeVue from "qrcode.vue";
import axios from "axios";

export default {
  components: {
    QrcodeVue,
  },

  data() {
    return {
      associated: [],
      errores: [],
      QRValue: process.env.VUE_APP_RUTA_NON_API + "associates/show/",
      size: 90,
      imagen: null,
    };
  },


  async created() {
    axios
      .get(process.env.VUE_APP_RUTA + "me/license", {
        xsrfCookieName: "csrf_access_token",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.associated = response.data;
        this.imagen = response.data.profile_picture
          .replace("b&#39;", "")
          .replace("&#39;", "");
        document.getElementById("img").src = "data:image/png;base64," + this.imagen;
        this.QRValue += this.associated.id
      })
      .catch((e) => {
        this.errores.push(e);
      });
  },
};
</script>
