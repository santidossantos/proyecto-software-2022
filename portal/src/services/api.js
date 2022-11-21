import axios from "axios";

export const apiService = axios.create({
  baseURL: process.env.VUE_APP_RUTA,
  xsrfCookieName: "csrf_access_token",
  
  headers: {
    "Access-Control-Allow-Origin": "*,*",
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});
