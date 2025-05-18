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

const formatDate = (date: string) => {
  const d = new Date(date);
  return d.toLocaleDateString("ru-RU", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  });
};
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
    <!-- Заголовок и автор -->
    <div class="flex items-center">
      <a
        v-if="note.source_url"
        :href="note.source_url"
        class="text-xl mr-4 p-2 text-blue-800 hover:underline"
        target="_blank"
        >{{ note.title }}</a
      >
      <a
        v-else
        :href="note.url"
        class="text-xl mr-4 p-2 text-blue-800 hover:underline"
        target="_blank"
        >{{ note.title }}</a
      >
      <span class="text-gray-500">👤 {{ note.author }}</span>
    </div>
    <!-- Тэги -->
    <div class="flex p-2">
      <div
        v-for="tag in note.tags"
        :key="`tag-id-${tag?.name}-${tag?.created}`"
        class="bg-gray-200 text-gray-700 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded"
      >
        {{ tag?.name }}
      </div>
    </div>
    <!-- Заметка к посту -->
    <p
      v-if="note.notes"
      class="p-2"
    >
      📝 {{ note.notes }}
    </p>
    <!-- Highlights с заметками к ним -->
    <div>
      <p
        v-if="note.highlights"
        v-for="hl in note.highlights"
        :key="`hl-id-${hl.id}`"
        class="text-sm text-gray-500 p-2"
      >
        {{ hl.content }}
        <span
          v-if="hl.notes_attached"
          v-for="hlNote in hl.notes_attached"
          :key="`hlNote-id-${hlNote.id}`"
          class="text-xs text-gray-400 italic bg-green-100 rounded"
          >📝 {{ hlNote.content }}</span
        >
      </p>
    </div>
    <!-- Даты -->
    <div class="text-sm text-gray-500 flex p-2">
      <p class="mr-2">📅 Moved: {{ formatDate(note.last_moved_at) }}</p>
      <p class="mr-2">Saved: {{ formatDate(note.saved_at) }}</p>
      <p
        v-if="note.published_date"
        class="mr-2"
      >
        Published: {{ formatDate(note.published_date) }}
      </p>
    </div>
  </div>
</template>

<style scoped></style>
