import { apiService } from "@/services/api";
import { createStore } from "vuex";
import router from "@/router";
import axios from "axios";

export default createStore({
  state: {
    username: null,
    token: null,
    error_msg: ''
  },
  getters: {
    isAuthenticated(state) {
      return state.token !== null;
    },
  },
  mutations: {
    authUser(state, userData) {
      state.username = userData.username;
      state.token = userData.token;
    },
    clearAuthData(state) {
      state.username = null;
      state.token = null;
      state.error_msg = '';
    },
    initializeStore(state) {
      if (localStorage.getItem("username")) {
        state.username = `${localStorage.getItem("username")}`;
        state.token = `${localStorage.getItem("token")}`;
      }
    },
    setMsg(state, errorData) {
      state.error_msg = errorData.error_msg;
    }

  },
  actions: {
    login: ({ commit }, authData) => {
      apiService
        .post("/auth", authData)
        .then((response) => {
          let success = response.data.token;

          if (success != null) {
            commit("authUser", {
              username: authData.username,
              token: response.data.token,
            });
            localStorage.setItem("token", response.data.token);
            localStorage.setItem("username", authData.username);
            router.replace("perfil");

          }
        })
        .catch((error) => {
          commit("setMsg", {
            error_msg: error.response.data.msg
          });
        });
    },
    logout: ({ commit }) => {

      axios
        .get(process.env.VUE_APP_RUTA + "logout", {
          xsrfCookieName: "csrf_access_token",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            commit("clearAuthData");
            localStorage.removeItem("username");
            localStorage.removeItem("token");
            router.replace("login");
          }
        })
        .catch((e) => {
          console.log("No se pudo cerrar sesionn");
        });

    },
  },
  modules: {},
});
