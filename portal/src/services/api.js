import axios from "axios";

export const apiService = axios.create({
  baseURL: "http://localhost:5000/api",
  xsrfCookieName: "csrf_access_token",
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});
