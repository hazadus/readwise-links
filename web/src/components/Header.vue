<script setup lang="ts">
/**
 * Компонент заголовка страниц приложения.
 */
</script>

<template>
  <header class="px-4 py-3 bg-gray-800 text-white shadow-md">
    <div class="container mx-auto flex flex-col md:flex-row md:items-center md:justify-between">
      <!-- Логотип и название -->
      <div class="flex items-center mb-2 md:mb-0">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6 mr-2 text-blue-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
          />
        </svg>
        <router-link
          to="/"
          class="text-xl font-semibold hover:text-blue-300"
        >
          Архив Readwise
        </router-link>
      </div>

      <!-- Навигация -->
      <nav class="flex items-center">
        <ul class="flex flex-wrap space-x-1 md:space-x-4 items-center">
          <li class="flex items-center">
            <router-link
              to="/"
              class="px-3 py-1 rounded-md hover:bg-gray-700 transition-colors flex items-center"
              active-class="bg-gray-700 font-medium"
              exact
              >Архив ссылок</router-link
            >
          </li>
          <li class="flex items-center">
            <router-link
              to="/about"
              class="px-3 py-1 rounded-md hover:bg-gray-700 transition-colors flex items-center"
              active-class="bg-gray-700 font-medium"
              exact
              >Что это?</router-link
            >
          </li>
          <li>
            <a
              href="https://github.com/hazadus/readwise-links"
              target="_blank"
              class="px-3 py-1 rounded-md hover:bg-gray-700 transition-colors flex items-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 mr-1"
                fill="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                />
              </svg>
              GitHub
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>
