<script setup lang="ts">
/**
 * Компонент для отображения карточки документа Readwise (поста с заметками к нему)
 */
defineProps({
  note: {
    type: Object as () => Note,
    required: true,
  },
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
  <div class="p-2 my-2 border rounded-lg overflow-hidden">
    <!-- Заголовок и автор -->
    <div class="flex items-center flex-wrap">
      <a
        v-if="note.source_url"
        :href="note.source_url"
        class="text-xl mr-4 p-2 text-blue-800 hover:underline break-words overflow-hidden"
        target="_blank"
        >{{ note.title }}</a
      >
      <a
        v-else
        :href="note.url"
        class="text-xl mr-4 p-2 text-blue-800 hover:underline break-words overflow-hidden"
        target="_blank"
        >{{ note.title }}</a
      >
      <span class="text-gray-500 break-words">👤 {{ note.author }}</span>
    </div>
    <!-- Тэги -->
    <div class="flex p-2 flex-wrap">
      <div
        v-for="tag in note.tags"
        :key="`tag-id-${tag?.name}-${tag?.created}`"
        class="bg-gray-200 text-gray-700 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded mb-1"
      >
        {{ tag?.name }}
      </div>
    </div>
    <!-- Заметка к посту -->
    <p
      v-if="note.notes"
      class="p-2 mx-2 mb-1 bg-green-100 text-gray-700 text-sm rounded-lg break-words"
    >
      📝 {{ note.notes }}
    </p>
    <!-- Summary -->
    <div
      v-if="note.summary"
      class="p-2 mx-2 text-gray-500 text-sm rounded-lg bg-gray-100 break-words"
    >
      {{ note.summary }}
    </div>
    <!-- Highlights с заметками к ним -->
    <div>
      <p
        v-if="note.highlights"
        v-for="hl in note.highlights"
        :key="`hl-id-${hl.id}`"
        class="text-sm text-gray-500 p-2 break-words"
      >
        {{ hl.content }}
        <span
          v-if="hl.notes_attached"
          v-for="hlNote in hl.notes_attached"
          :key="`hlNote-id-${hlNote.id}`"
          class="text-xs text-gray-400 italic bg-green-100 rounded break-words"
          >📝 {{ hlNote.content }}</span
        >
      </p>
    </div>
    <!-- Даты -->
    <div class="text-sm text-gray-500 flex p-2 flex-wrap">
      <p class="mr-2 mb-1">📅 Moved: {{ formatDate(note.last_moved_at) }}</p>
      <p class="mr-2 mb-1">Saved: {{ formatDate(note.saved_at) }}</p>
      <p
        v-if="note.published_date"
        class="mr-2 mb-1"
      >
        Published: {{ formatDate(note.published_date) }}
      </p>
    </div>
  </div>
</template>
