<script setup lang="ts">
import { computed, ref } from "vue";
import noteData from "../assets/articles.json";
import ArticleCard from "../components/ArticleCard.vue";

const data: Note[] = noteData;

const newNotes = computed(() => data.filter((note) => note.location === "new"));
const archivedNotes = computed(() => data.filter((note) => note.location === "archive"));
const laterNotes = computed(() => data.filter((note) => note.location === "later"));

const filter = ref<string>("all");

const filteredNotes = computed(() => {
  if (filter.value === "later") {
    return laterNotes.value;
  } else if (filter.value === "archive") {
    return archivedNotes.value;
  } else if (filter.value === "new") {
    return newNotes.value;
  }
  return data;
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

  <ArticleCard
    v-for="note in filteredNotes"
    :note="note"
    :key="`note-id-${note.id}`"
  />
</template>

<style scoped></style>
