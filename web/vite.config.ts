import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "tailwindcss";
import autoprefixer from "autoprefixer";

export default defineConfig({
  plugins: [vue()],
  css: {
    postcss: {
      plugins: [tailwindcss, autoprefixer],
    },
  },
  server: {
    host: "0.0.0.0",
    port: 3000,
  },
  build: {
    rollupOptions: {
      external: ["@/assets/note.json"],
    },
  },
  // Для корректной работы с GitHub Pages
  // Reference: https://vitejs.dev/guide/static-deploy.html#github-pages
  base: "/readwise-links/",
  define: {
    // Добавляем время сборки как глобальную переменную
    "import.meta.env.BUILD_TIME": JSON.stringify(new Date().toISOString()),
  },
});
