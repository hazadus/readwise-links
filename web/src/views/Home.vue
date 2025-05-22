<script setup lang="ts">
/**
 * Страница для просмотра архива ссылок.
 */
import { useDebounceFn } from "@vueuse/core";
import { computed, ref } from "vue";
import noteData from "../assets/articles.json";
import ArticleCard from "../components/ArticleCard.vue";

const data: Note[] = noteData;

const newNotes = computed(() => data.filter((note) => note.location === "new"));
const archivedNotes = computed(() => data.filter((note) => note.location === "archive"));
const laterNotes = computed(() => data.filter((note) => note.location === "later"));

const filter = ref<string>("all");
const searchQuery = ref<string>("");
const debouncedSearchQuery = ref<string>("");
const hasNotes = ref<boolean>(false);
const hasHighlights = ref<boolean>(false);

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

const filteredNotes = computed(() => {
  let result = data;

  // Применение основных фильтров (new, later, archive)
  if (filter.value === "later") {
    result = laterNotes.value;
  } else if (filter.value === "archive") {
    result = archivedNotes.value;
  } else if (filter.value === "new") {
    result = newNotes.value;
  }

  // Фильтр по наличию заметок
  if (hasNotes.value) {
    result = result.filter((note) => note.notes && note.notes.trim() !== "");
  }

  // Фильтр по наличию highlights
  if (hasHighlights.value) {
    result = result.filter((note) => note.highlights && note.highlights.length > 0);
  }

  // Поиск по тексту (используем debouncedSearchQuery вместо searchQuery)
  if (debouncedSearchQuery.value.trim() !== "") {
    const query = debouncedSearchQuery.value.toLowerCase();
    result = result.filter((note) => {
      // Поиск в заголовке
      const titleMatch = note.title && note.title.toLowerCase().includes(query);
      // Поиск в summary
      const summaryMatch = note.summary && note.summary.toLowerCase().includes(query);
      // Поиск в заметках
      const notesMatch = note.notes && note.notes.toLowerCase().includes(query);
      // Поиск в highlights
      const highlightsMatch =
        note.highlights &&
        note.highlights.some(
          (h) =>
            (h.notes && h.notes.toLowerCase().includes(query)) ||
            (h.content && h.content.toLowerCase().includes(query)),
        );

      return titleMatch || summaryMatch || notesMatch || highlightsMatch;
    });
  }

  return result;
});
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
          newNotes.length
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
          laterNotes.length
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
          archivedNotes.length
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

  <ArticleCard
    v-for="note in filteredNotes"
    :note="note"
    :key="`note-id-${note.id}`"
  />
</template>

<style scoped></style>
