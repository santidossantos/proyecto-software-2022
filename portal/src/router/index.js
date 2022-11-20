import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import LoginView from "../views/LoginView.vue";
import PaymentView from "../views/PaymentView.vue";
import MiPerfilView from "../views/MiPerfilView.vue";
import LicenseView from "../views/LicenseView.vue";
import MisDisciplinasView from "../views/MisDisciplinasView.vue";


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
    path: "/perfil",
    name: "Perfil",
    component: MiPerfilView,
  },
  {
<<<<<<< HEAD
    path: "/perfil/carnet",
    name: "Carnet",
    component: LicenseView,
=======
    path: "/disciplinas/me",
    name: "DisciplinasMe",
    component: MisDisciplinasView,
>>>>>>> development
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
