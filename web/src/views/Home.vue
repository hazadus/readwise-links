<script setup lang="ts">
import { computed, ref } from "vue";
import noteData from "../assets/articles.json";
import ArticleCard from "../components/ArticleCard.vue";

const data: Note[] = noteData;

const newNotes = computed(() => data.filter((note) => note.location === "new"));
const archivedNotes = computed(() => data.filter((note) => note.location === "archive"));
const laterNotes = computed(() => data.filter((note) => note.location === "later"));

const filter = ref<string>("later");

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
  <div>
    <a
      @click="filter = 'all'"
      class="hover:underline"
      >Всего постов</a
    >: {{ data.length }} [<a
      @click="filter = 'new'"
      class="hover:underline"
      >New</a
    >: {{ newNotes.length }} |
    <a
      @click="filter = 'later'"
      class="hover:underline"
      >Later</a
    >: {{ laterNotes.length }} |
    <a
      @click="filter = 'archive'"
      class="hover:underline"
      >Archive</a
    >: {{ archivedNotes.length }}]
  </div>

  <ArticleCard
    v-for="note in filteredNotes"
    :note="note"
    :key="`note-id-${note.id}`"
  />
</template>

<style scoped></style>
