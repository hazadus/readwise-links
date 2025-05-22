import { createRouter, createWebHistory } from "vue-router";
import About from "../views/About.vue";
import Home from "../views/Home.vue";

const router = createRouter({
  // Для корректной работы с GitHub Pages
  history: createWebHistory("/readwise-links/"),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/about",
      name: "about",
      component: About,
    },
  ],
  scrollBehavior() {
    // Всегда прокручивать к верху страницы
    return { top: 0 };
  },
});

export default router;
