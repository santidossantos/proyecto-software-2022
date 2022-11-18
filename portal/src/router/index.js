import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import LoginView from "../views/LoginView.vue";
import PaymentView from "../views/PaymentView.vue";
import CreatePaymentView from "../views/CreatePaymentView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/disciplinas",
    name: "disciplinas",
    component: AboutView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/payment",
    name: "payment",
    component: PaymentView,
  },
  {
    path: "/createPayment",
    name: "createPayment",
    component: CreatePaymentView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
