<script setup lang="ts">
/**
 * Компонент для фильтрации по тегам.
 * Отображает доступные теги и выбранные, позволяя перемещать их между списками.
 */
import Tag from "./Tag.vue";

const props = defineProps({
  availableTags: {
    type: Array as () => string[],
    required: true,
  },
  modelValue: {
    type: Array as () => string[],
    default: () => [],
  },
});

const emit = defineEmits(["update:modelValue"]);

const selectTag = (tag: string) => {
  if (!props.modelValue.includes(tag)) {
    const updatedSelection = [...props.modelValue, tag];
    emit("update:modelValue", updatedSelection);
  }
};

const removeTag = (tag: string) => {
  const updatedSelection = props.modelValue.filter((t) => t !== tag);
  emit("update:modelValue", updatedSelection);
};
</script>

<template>
  <div class="border border-gray-200 rounded-md mb-4 p-4 bg-gray-50">
    <!-- Выбранные теги -->
    <div
      v-if="modelValue.length > 0"
      class="mb-2"
    >
      <span class="text-sm text-gray-600 mr-1">Выбранные теги:</span>
      <div class="flex flex-wrap gap-1 mt-1">
        <Tag
          v-for="tag in modelValue"
          :key="`selected-tag-${tag}`"
          :name="tag"
          class="cursor-pointer bg-blue-500 text-white hover:bg-blue-600"
          @click="removeTag(tag)"
        />
      </div>
    </div>

    <!-- Доступные теги -->
    <div>
      <span class="text-sm text-gray-600 mr-1">Доступные теги:</span>
      <div class="flex flex-wrap gap-1 mt-1">
        <Tag
          v-for="tag in availableTags.filter((t) => !modelValue.includes(t))"
          :key="`available-tag-${tag}`"
          :name="tag"
          class="cursor-pointer hover:bg-blue-200"
          @click="selectTag(tag)"
        />
        <span
          v-if="availableTags.filter((t) => !modelValue.includes(t)).length === 0"
          class="text-xs text-gray-500 italic"
        >
          Все теги выбраны
        </span>
      </div>
    </div>
  </div>
</template>
