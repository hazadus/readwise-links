<script setup lang="ts">
import { ref } from "vue";
import triageData from "../assets/triage.json";
import ArticleCard from "../components/ArticleCard.vue";

const triage = triageData as unknown as TriageJson;

const collections: { key: keyof TriageCollections; title: string; icon: string }[] = [
  { key: "top", title: "Топ подборка", icon: "⭐" },
  { key: "quick_wins", title: "Быстрые победы", icon: "⚡" },
  { key: "deep_reading", title: "Глубокое чтение", icon: "📖" },
  { key: "tutorials", title: "Руководства", icon: "🛠️" },
  { key: "fundamentals", title: "Основы", icon: "🧠" },
  { key: "timely", title: "Читать сейчас", icon: "⏳" },
  { key: "shortest", title: "Короткие статьи", icon: "📄" },
];

const activeTab = ref<keyof TriageCollections>("top");

const formatDate = (iso: string) =>
  new Date(iso).toLocaleDateString("ru-RU", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
</script>

<template>
  <!-- Полоска с табами -->
  <div class="bg-white border-b border-gray-200 sticky top-0 z-10 shadow-sm">
    <div class="container mx-auto px-4">
      <nav class="flex overflow-x-auto gap-1 py-1">
        <button
          v-for="col in collections"
          :key="col.key"
          @click="activeTab = col.key"
          class="flex-shrink-0 px-3 py-2 text-sm rounded-md transition-colors whitespace-nowrap"
          :class="
            activeTab === col.key
              ? 'bg-blue-600 text-white font-medium'
              : 'text-gray-600 hover:bg-gray-100'
          "
        >
          {{ col.icon }} {{ col.title }}
          <span
            class="ml-1 text-xs"
            :class="activeTab === col.key ? 'text-blue-200' : 'text-gray-400'"
          >
            {{ triage.collections[col.key].length }}
          </span>
        </button>
      </nav>
    </div>
  </div>

  <!-- Контент активного таба -->
  <div class="container mx-auto px-4 py-6">
    <div class="mb-4 text-xs text-gray-400">
      Сгенерировано: {{ formatDate(triage.generated_at) }}
    </div>

    <div v-if="triage.collections[activeTab].length === 0" class="text-gray-400 text-sm">
      Нет статей в этой подборке.
    </div>

    <ArticleCard
      v-for="article in triage.collections[activeTab]"
      :key="article.id"
      :article="(article as Article)"
    />
  </div>
</template>
