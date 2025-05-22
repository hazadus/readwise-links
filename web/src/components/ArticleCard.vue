<script setup lang="ts">
/**
 * Компонент для отображения карточки документа Readwise Reader (ссылки на пост, книгу с заметками к ней)
 */
defineProps({
  article: {
    type: Object as () => Article,
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
  <div class="my-4 rounded-md border border-gray-200 bg-white shadow-sm overflow-hidden">
    <!-- Хэдер с названием и автором поста -->
    <div class="border-b border-gray-200 bg-gray-50 px-4 py-3">
      <div class="flex flex-wrap items-start justify-between">
        <div class="flex-1 min-w-0">
          <a
            v-if="article.source_url"
            :href="article.source_url"
            class="text-lg font-semibold text-blue-600 hover:text-blue-800 hover:underline break-words"
            target="_blank"
            >{{ article.title }}</a
          >
          <a
            v-else
            :href="article.url"
            class="text-lg font-semibold text-blue-600 hover:text-blue-800 hover:underline break-words"
            target="_blank"
            >{{ article.title }}</a
          >
          <div class="mt-1 flex items-center text-sm text-gray-600">
            <svg
              class="h-4 w-4 mr-1"
              viewBox="0 0 16 16"
              fill="currentColor"
            >
              <path
                d="M8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16zm.847-8.145a2.502 2.502 0 1 0-1.645 0C5.686 8.15 4.5 9.5 4.5 11c0 .5.5 1 1 1h5c.5 0 1-.5 1-1 0-1.5-1.186-2.85-2.653-3.145zM8 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"
              ></path>
            </svg>
            <span>{{ article.author }}</span>
          </div>
        </div>

        <!-- Превью изображения поста -->
        <div
          v-if="article.image_url"
          class="ml-4 flex-shrink-0 w-24 overflow-hidden border border-gray-200 rounded-md"
          style="aspect-ratio: 3/2"
        >
          <img
            :src="article.image_url"
            alt="Превью"
            class="w-full h-full object-cover"
            loading="lazy"
          />
        </div>
      </div>
    </div>

    <!-- Контент -->
    <div class="px-4 py-3">
      <!-- Тэги -->
      <div
        v-if="article.tags"
        class="flex flex-wrap gap-1 mb-3"
      >
        <span
          v-for="tag in article.tags"
          :key="`tag-id-${tag?.name}-${tag?.created}`"
          class="inline-flex items-center rounded-full bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-700"
        >
          {{ tag?.name }}
        </span>
      </div>

      <!-- Заметка пользователя к посту -->
      <div
        v-if="article.notes"
        class="mb-3 rounded-md bg-yellow-50 border border-yellow-200 px-3 py-2"
      >
        <div class="flex">
          <svg
            class="h-5 w-5 text-yellow-700 mt-0.5 mr-2 flex-shrink-0"
            viewBox="0 0 16 16"
            fill="currentColor"
          >
            <path
              d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25Zm1.75-.25a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM3.5 6.25a.75.75 0 0 1 .75-.75h7a.75.75 0 0 1 0 1.5h-7a.75.75 0 0 1-.75-.75Zm.75 2.25h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1 0-1.5Z"
            ></path>
          </svg>
          <div class="text-sm text-gray-700">{{ article.notes }}</div>
        </div>
      </div>

      <!-- Summary -->
      <div
        v-if="article.summary"
        class="mb-3 rounded-md bg-gray-50 border border-gray-200 px-3 py-2 text-sm text-gray-700"
      >
        {{ article.summary }}
      </div>

      <!-- Highlights -->
      <div
        v-if="article.highlights && article.highlights.length"
        class="space-y-2"
      >
        <div
          v-for="hl in article.highlights"
          :key="`hl-id-${hl.id}`"
          class="border-l-4 border-green-300 bg-green-50 pl-3 py-2 pr-2 text-sm text-gray-700"
        >
          {{ hl.content }}

          <!-- Заметки к highlight -->
          <div
            v-if="hl.notes_attached"
            class="mt-2 pl-3 border-l-2 border-gray-300"
          >
            <div
              v-for="hlNote in hl.notes_attached"
              :key="`hlNote-id-${hlNote.id}`"
              class="text-xs italic text-gray-600"
            >
              <svg
                class="inline-block h-3 w-3 mr-1"
                viewBox="0 0 16 16"
                fill="currentColor"
              >
                <path
                  d="M0 3.75C0 2.784.784 2 1.75 2h12.5c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 14H1.75A1.75 1.75 0 0 1 0 12.25Zm1.75-.25a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM3.5 6.25a.75.75 0 0 1 .75-.75h7a.75.75 0 0 1 0 1.5h-7a.75.75 0 0 1-.75-.75Zm.75 2.25h4a.75.75 0 0 1 0 1.5h-4a.75.75 0 0 1 0-1.5Z"
                ></path>
              </svg>
              {{ hlNote.content }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Футер с датами и количеством слов -->
    <div class="border-t border-gray-200 bg-gray-50 px-4 py-2">
      <div class="flex flex-wrap gap-x-4 gap-y-1 text-xs text-gray-600">
        <div class="flex items-center">
          <svg
            class="h-3.5 w-3.5 mr-1"
            viewBox="0 0 16 16"
            fill="currentColor"
          >
            <path
              d="M4.75 0a.75.75 0 0 1 .75.75V2h5V.75a.75.75 0 0 1 1.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 0 1 4.75 0ZM2.5 7.5v6.75c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V7.5Zm10.75-4H2.75a.25.25 0 0 0-.25.25V6h11V3.75a.25.25 0 0 0-.25-.25Z"
            ></path>
          </svg>
          <span>Moved: {{ formatDate(article.last_moved_at) }}</span>
        </div>
        <div class="flex items-center">
          <svg
            class="h-3.5 w-3.5 mr-1"
            viewBox="0 0 16 16"
            fill="currentColor"
          >
            <path
              d="M2 2h4.5a.5.5 0 0 1 0 1H2a.5.5 0 0 1 0-1Zm0 11h12a.5.5 0 0 1 0 1H2a.5.5 0 0 1 0-1Zm0-2.25h12a.5.5 0 0 1 0 1H2a.5.5 0 0 1 0-1ZM2.5 8c0-.28.22-.5.5-.5h11a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5ZM2 5h4.5a.5.5 0 0 1 0 1H2a.5.5 0 0 1 0-1Z"
            ></path>
          </svg>
          <span>Saved: {{ formatDate(article.saved_at) }}</span>
        </div>
        <div
          v-if="article.published_date"
          class="flex items-center"
        >
          <svg
            class="h-3.5 w-3.5 mr-1"
            viewBox="0 0 16 16"
            fill="currentColor"
          >
            <path
              d="M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"
            ></path>
          </svg>
          <span>Published: {{ formatDate(article.published_date) }}</span>
        </div>
        <div
          v-if="article.word_count"
          class="flex items-center"
        >
          <svg
            class="h-3.5 w-3.5 mr-1"
            viewBox="0 0 16 16"
            fill="currentColor"
          >
            <path
              d="M0 1.75A1.75 1.75 0 0 1 1.75 0h12.5A1.75 1.75 0 0 1 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM1.75 1.5a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25ZM3 5.75A.75.75 0 0 1 3.75 5h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 5.75Zm0 4a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 3 9.75ZM3.75 3h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Z"
            ></path>
          </svg>
          <span>{{ article.word_count }} words</span>
        </div>
      </div>
    </div>
  </div>
</template>
