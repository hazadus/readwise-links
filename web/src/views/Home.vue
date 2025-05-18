<script setup lang="ts">
import { computed, ref } from "vue";
import noteData from "../assets/articles.json";

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
  <div
    v-for="note in filteredNotes"
    :key="`note-id-${note.id}`"
    class="p-2 my-2 border"
  >
    <h2 class="text-xl">{{ note.title }}</h2>
    <p
      v-if="note.notes"
      class="p-2"
    >
      📝 {{ note.notes }}
    </p>
    <p
      v-if="note.highlights"
      v-for="hl in note.highlights"
      :key="`hl-id-${hl.id}`"
      class="text-sm text-gray-500 p-2"
    >
      {{ hl.content }}
    </p>
  </div>
</template>

<style scoped></style>
