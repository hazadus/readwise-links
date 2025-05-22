<script setup lang="ts">
/**
 * Компонент для отображения тега (метки) в карточке документа Readwise Reader.
 */
defineProps({
  name: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <span
    class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-700"
  >
    {{ name }}
  </span>
</template>
