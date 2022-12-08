import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import LoginView from "../views/LoginView.vue";
import PaymentView from "../views/PaymentView.vue";
import MiPerfilView from "../views/MiPerfilView.vue";
import LicenseView from "../views/LicenseView.vue";
import MisDisciplinasView from "../views/MisDisciplinasView.vue";
import store from "@/store";
import StatisticsView from "../views/StatisticsView.vue";

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
    meta: { requiresAuth: true }
  },
  {
    path: "/perfil",
    name: "Perfil",
    component: MiPerfilView,
    meta: { requiresAuth: true }
  },
  {
    path: "/carnet",
    name: "Carnet",
    component: LicenseView,
  },
  {
   
    path: "/me/disciplinas",
    name: "DisciplinasMe",
    component: MisDisciplinasView,
    meta: { requiresAuth: true }
  },
    {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/Estadisticas",
    name: "Estadisticas",
    component: StatisticsView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(route => route.meta.requiresAuth)) {
    if (!store.state.username) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router;
