import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const router = createRouter({
  history: createWebHistory("/readwise-links/"),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
  ],
  scrollBehavior() {
    // Всегда прокручивать к верху страницы
    return { top: 0 };
  },
});

export default router;
