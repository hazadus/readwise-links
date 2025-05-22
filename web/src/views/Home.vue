<script setup lang="ts">
/**
 * Страница для просмотра архива ссылок.
 */
import { useDebounceFn } from "@vueuse/core";
import { computed, ref } from "vue";
import articlesData from "../assets/articles.json";
import ArticleCard from "../components/ArticleCard.vue";
import TagFilter from "../components/TagFilter.vue";

const data: Article[] = articlesData as Article[];

const newArticles = computed(() => data.filter((article) => article.location === "new"));
const archivedArticles = computed(() => data.filter((article) => article.location === "archive"));
const laterArticles = computed(() => data.filter((article) => article.location === "later"));

const filter = ref<string>("all");
const searchQuery = ref<string>("");
const debouncedSearchQuery = ref<string>("");
const hasNotes = ref<boolean>(false);
const hasHighlights = ref<boolean>(false);
const selectedTags = ref<string[]>([]);

// Применяем debounce к функции обновления debouncedSearchQuery
const updateDebouncedSearch = useDebounceFn((value: string) => {
  debouncedSearchQuery.value = value;
}, 300);

// Следим за изменениями в searchQuery и обновляем debouncedSearchQuery с задержкой
const handleSearchInput = (event: Event) => {
  const value = (event.target as HTMLInputElement).value;
  searchQuery.value = value;
  updateDebouncedSearch(value);
};

const filteredArticles = computed(() => {
  let result = data;

  // Применение основных фильтров (new, later, archive)
  if (filter.value === "later") {
    result = laterArticles.value;
  } else if (filter.value === "archive") {
    result = archivedArticles.value;
  } else if (filter.value === "new") {
    result = newArticles.value;
  }

  // Фильтр по наличию заметок
  if (hasNotes.value) {
    result = result.filter((article) => article.notes && article.notes.trim() !== "");
  }

  // Фильтр по наличию highlights
  if (hasHighlights.value) {
    result = result.filter((article) => article.highlights && article.highlights.length > 0);
  }

  // Фильтр по выбранным тегам
  if (selectedTags.value.length > 0) {
    result = result.filter((article) => {
      if (!article.tags) return false;

      // Получаем все имена тегов статьи
      const articleTagNames = Object.values(article.tags)
        .filter((tag) => tag) // Фильтрация null/undefined значений
        .map((tag) => tag!.name);

      // Проверяем, содержит ли статья все выбранные теги
      return selectedTags.value.every((tag) => articleTagNames.includes(tag));
    });
  }

  // Поиск по тексту
  if (debouncedSearchQuery.value.trim() !== "") {
    const query = debouncedSearchQuery.value.toLowerCase();
    result = result.filter((article) => {
      // Поиск в заголовке
      const titleMatch = article.title && article.title.toLowerCase().includes(query);
      // Поиск в summary
      const summaryMatch = article.summary && article.summary.toLowerCase().includes(query);
      // Поиск в заметках
      const notesMatch = article.notes && article.notes.toLowerCase().includes(query);
      // Поиск в highlights
      const highlightsMatch =
        article.highlights &&
        article.highlights.some(
          (h) =>
            (h.notes && h.notes.toLowerCase().includes(query)) ||
            (h.content && h.content.toLowerCase().includes(query)),
        );

      return titleMatch || summaryMatch || notesMatch || highlightsMatch;
    });
  }

  // Сортировка постов по last_moved_at по убыванию (от новых к старым)
  return result.sort((a, b) => {
    const dateA = new Date(a.last_moved_at);
    const dateB = new Date(b.last_moved_at);
    return dateB.getTime() - dateA.getTime(); // По убыванию (новые в начале)
  });
});

// Получаем уникальные теги из отфильтрованных документов
const availableTags = computed(() =>
  filteredArticles.value.reduce((acc: string[], article) => {
    if (article.tags) {
      // Получаем массив ключей
      const tagKeys = Object.keys(article.tags);

      // Перебираем ключи
      tagKeys.forEach((key) => {
        const tag = article.tags![key];
        if (tag) {
          if (!acc.includes(tag.name)) {
            acc.push(tag.name);
          }
        }
      });
    }
    return acc;
  }, []),
);
</script>

<template>
  <div class="border-b border-gray-200 mb-4">
    <nav
      class="flex -mb-px"
      aria-label="Tabs"
    >
      <button
        @click="filter = 'all'"
        class="px-4 py-2 flex items-center border-b-2 text-sm font-medium"
        :class="
          filter === 'all'
            ? 'border-blue-500 text-blue-600'
            : 'border-transparent hover:border-gray-300 text-gray-500 hover:text-gray-700'
        "
      >
        All
        <span class="ml-2 bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs">{{ data.length }}</span>
      </button>
      <button
        @click="filter = 'new'"
        class="px-4 py-2 flex items-center border-b-2 text-sm font-medium"
        :class="
          filter === 'new'
            ? 'border-blue-500 text-blue-600'
            : 'border-transparent hover:border-gray-300 text-gray-500 hover:text-gray-700'
        "
      >
        New
        <span class="ml-2 bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs">{{
          newArticles.length
        }}</span>
      </button>
      <button
        @click="filter = 'later'"
        class="px-4 py-2 flex items-center border-b-2 text-sm font-medium"
        :class="
          filter === 'later'
            ? 'border-blue-500 text-blue-600'
            : 'border-transparent hover:border-gray-300 text-gray-500 hover:text-gray-700'
        "
      >
        Later
        <span class="ml-2 bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs">{{
          laterArticles.length
        }}</span>
      </button>
      <button
        @click="filter = 'archive'"
        class="px-4 py-2 flex items-center border-b-2 text-sm font-medium"
        :class="
          filter === 'archive'
            ? 'border-blue-500 text-blue-600'
            : 'border-transparent hover:border-gray-300 text-gray-500 hover:text-gray-700'
        "
      >
        Archive
        <span class="ml-2 bg-gray-100 text-gray-700 px-2 py-0.5 rounded-full text-xs">{{
          archivedArticles.length
        }}</span>
      </button>
    </nav>
  </div>

  <!-- Фильтры и поиск -->
  <div class="border border-gray-200 rounded-md mb-4 p-4 bg-gray-50">
    <div class="flex flex-col md:flex-row gap-3">
      <!-- Поиск -->
      <div class="w-full md:w-1/2">
        <div class="relative">
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg
              class="w-4 h-4 text-gray-500"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            v-model="searchQuery"
            type="search"
            class="w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-md bg-white focus:ring-2 focus:ring-blue-100 focus:border-blue-500 focus:outline-none"
            placeholder="Поиск по тексту..."
            @input="handleSearchInput"
            @keyup.esc="
              searchQuery = '';
              debouncedSearchQuery = '';
            "
          />
        </div>
      </div>

      <!-- Фильтры -->
      <div class="flex items-center gap-3">
        <label class="inline-flex items-center cursor-pointer">
          <input
            v-model="hasNotes"
            type="checkbox"
            class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500 cursor-pointer"
          />
          <span class="ml-2 text-sm text-gray-700">Есть заметка</span>
        </label>

        <label class="inline-flex items-center cursor-pointer">
          <input
            v-model="hasHighlights"
            type="checkbox"
            class="w-4 h-4 text-blue-600 rounded focus:ring-blue-500 cursor-pointer"
          />
          <span class="ml-2 text-sm text-gray-700">Есть highlights</span>
        </label>
      </div>
    </div>
  </div>

  <!-- Компонент фильтра по тегам -->
  <TagFilter
    :available-tags="availableTags"
    v-model="selectedTags"
  />

  <ArticleCard
    v-for="article in filteredArticles"
    :article="article"
    :key="`article-id-${article.id}`"
  />
</template>
