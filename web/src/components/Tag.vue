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
    class="inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium bg-blue-100 text-blue-700"
    @click="$emit('click')"
  >
    {{ name }}
  </span>
</template>
