<script setup lang="ts">
/**
 * Компонент для фильтрации по тегам.
 * Отображает доступные теги и выбранные, позволяя перемещать их между списками.
 */
import { computed, ref } from "vue";
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

// Поисковый запрос для фильтрации тегов
const tagSearchQuery = ref<string>("");

// Фильтрованные доступные теги (исключая выбранные и учитывая поиск)
const filteredAvailableTags = computed(() => {
  const availableNotSelected = props.availableTags.filter((t) => !props.modelValue.includes(t));

  if (tagSearchQuery.value.trim() === "") {
    return availableNotSelected;
  }

  const query = tagSearchQuery.value.toLowerCase();
  return availableNotSelected.filter((tag) => tag.toLowerCase().includes(query));
});

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

// Сброс поискового запроса
const clearTagSearch = () => {
  tagSearchQuery.value = "";
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
      <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-gray-600 mr-1">Доступные теги:</span>
        <div class="relative w-48">
          <div class="absolute inset-y-0 left-0 flex items-center pl-2 pointer-events-none">
            <svg
              class="w-3 h-3 text-gray-500"
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
            v-model="tagSearchQuery"
            type="search"
            class="w-full p-1 pl-7 pr-8 text-xs text-gray-900 border border-gray-300 rounded bg-white focus:ring-1 focus:ring-blue-100 focus:border-blue-500 focus:outline-none"
            placeholder="Поиск тегов..."
            @keyup.esc="clearTagSearch"
          />
          <button
            v-if="tagSearchQuery"
            @click="clearTagSearch"
            class="absolute inset-y-0 right-0 flex items-center pr-2 text-gray-400 hover:text-gray-600"
            type="button"
          >
            <svg
              class="w-3 h-3"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>
      </div>
      <div class="flex flex-wrap gap-1 mt-1">
        <Tag
          v-for="tag in filteredAvailableTags"
          :key="`available-tag-${tag}`"
          :name="tag"
          class="cursor-pointer hover:bg-blue-200"
          @click="selectTag(tag)"
        />
        <span
          v-if="
            filteredAvailableTags.length === 0 &&
            props.availableTags.filter((t) => !modelValue.includes(t)).length > 0
          "
          class="text-xs text-gray-500 italic"
        >
          По запросу "{{ tagSearchQuery }}" теги не найдены
        </span>
        <span
          v-else-if="props.availableTags.filter((t) => !modelValue.includes(t)).length === 0"
          class="text-xs text-gray-500 italic"
        >
          Все теги выбраны
        </span>
      </div>
    </div>
  </div>
</template>
