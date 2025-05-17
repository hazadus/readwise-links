<script setup lang="ts">
import noteData from "../assets/note.json";

const data: Note[] = noteData;
</script>

<template>
  <div>Всего заметок: {{ data.length }}</div>
  <div
    v-for="note in data"
    :key="`note-id-${note.id}`"
    class="p-2 my-2 border"
  >
    <p>{{ note.content }}</p>
  </div>
</template>
<style scoped></style>
