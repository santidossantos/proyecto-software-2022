import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
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
    component: AboutView,
  },
    {
    path: "/login",
    name: "login",
    component: AboutView,
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

export default router;
