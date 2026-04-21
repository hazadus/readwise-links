<script setup lang="ts">
/**
 * Страница с информацией о проекте.
 */

// Получаем время сборки приложения
const buildTime = new Date(import.meta.env.BUILD_TIME);

// Форматируем дату и время для отображения
const formattedBuildTime = buildTime.toLocaleString("ru-RU", {
  year: "numeric",
  month: "long",
  day: "numeric",
  hour: "2-digit",
  minute: "2-digit",
});
</script>

<template>
  <div class="max-w-4xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
    <div class="bg-white shadow rounded-lg overflow-hidden">
      <!-- Header with gradient background -->
      <div class="bg-gradient-to-r from-blue-500 to-indigo-600 px-6 py-8 sm:px-10">
        <h1 class="text-3xl font-bold text-white">Архив ссылок Readwise Reader</h1>
        <p class="mt-2 text-lg text-blue-100">
          Утилита сохраняет все мои ссылки с highlights и заметками к ним из Readwise Reader в Markdown-отчёты
          и JSON-файл для архивации и удобного доступа к ним.
        </p>
      </div>

      <!-- Content sections -->
      <div class="px-6 py-6 sm:px-10">
        <section class="mb-8">
          <h3 class="text-xl font-semibold text-gray-800 pb-2 border-b border-gray-200">
            Что за Readwise Reader?
          </h3>
          <div class="mt-4 space-y-4 text-gray-600">
            <p>
              <a
                href="http://read.readwise.io"
                target="_blank"
                class="text-blue-600 hover:text-blue-800 font-medium underline"
                >Readwise Reader</a
              >
              – совершенно прекрасная софтина, позволяющая сохранять ссылки и любые материалы (посты, видео,
              PDF, книги), и потом читать их онлайн или через приложение на телефоне. Платная, но работает
              просто идеально.
            </p>
            <p>
              Reader объединяет в себе приложения нескольких классов: read later, хранилище ссылок, читалка.
              Можно даже кинуть в неё любой текст или письмо по email, и оно сохранится к прочтению во
              входящих. Можно смотреть видео YouTube, не отвлекаясь на предложения других видео, как это
              происходит на сайте.
            </p>
          </div>
        </section>

        <section class="mb-8">
          <h3 class="text-xl font-semibold text-gray-800 pb-2 border-b border-gray-200">
            Зачем нужно архивировать ссылки?
          </h3>
          <p class="mt-4 text-gray-600">
            Всё хорошее когда-то заканчивается, и софт тоже не вечен. Я не хотел бы в один прекрасный день
            потерять ссылки на все накопленные материалы. Я частенько ищу нужные материалы в Readwise, поэтому
            нужно быть уверенным, что они никуда не исчезнут.
          </p>
        </section>

        <section class="mb-8">
          <h3 class="text-xl font-semibold text-gray-800 pb-2 border-b border-gray-200">
            Как формируются подборки?
          </h3>
          <div class="mt-4 text-gray-600">
            <p class="mb-3">
              Каждую ночь LLM (через OpenRouter) анализирует все статьи из раздела «Read Later» и присваивает
              каждой метаданные: балл интереса (1–10), а также признаки <em>tutorial</em>,
              <em>foundational</em> и <em>evergreen</em>. На основе этих данных формируются 7 тематических
              подборок:
            </p>
            <ul class="list-disc pl-6 space-y-2">
              <li>
                <strong>Топ-20</strong> — 20 статей с наивысшим баллом интереса среди всех «Read Later»
                материалов.
              </li>
              <li>
                <strong>Быстрые победы</strong> — короткие статьи с высоким баллом интереса, которые можно
                быстро прочитать и применить.
              </li>
              <li>
                <strong>Короткие статьи</strong> — самые короткие материалы в очереди, отсортированные по
                длине.
              </li>
              <li>
                <strong>Читать сейчас</strong> — актуальные материалы (новости, тренды), которые теряют
                ценность со временем.
              </li>
              <li>
                <strong>Основы</strong> — фундаментальные статьи с признаком <em>foundational</em> или
                <em>evergreen</em>, которые не устаревают.
              </li>
              <li>
                <strong>Руководства</strong> — практические туториалы с признаком <em>tutorial</em>.
              </li>
              <li>
                <strong>Глубокое чтение</strong> — объёмные материалы с высоким баллом интереса для
                вдумчивого изучения.
              </li>
            </ul>
            <p class="mt-3 text-sm text-gray-500">
              Результаты анализа кэшируются; повторный запуск пересчитывает только новые или изменившиеся
              статьи.
            </p>
          </div>
        </section>

        <section class="mb-4">
          <h3 class="text-xl font-semibold text-gray-800 pb-2 border-b border-gray-200">Как это работает?</h3>
          <div class="mt-4 text-gray-600">
            <ol class="list-decimal pl-6 space-y-4">
              <li>
                По расписанию каждую ночь запускается GitHub Action, который выполняет скрипт архивации
                ссылок.
              </li>
              <li>
                Скрипт:
                <ul class="list-disc pl-8 mt-2 space-y-1">
                  <li>запрашивает через API Reader все материалы, сохраненные в моём профиле</li>
                  <li>
                    форматирует полученную инфу в Markdown и сохраняет в файлы с разбивкой по разделам и тэгам
                  </li>
                  <li>
                    сохраняет в файле формата JSON все ссылки с highlights и заметками к ним для использования
                    в фронтовом приложении
                  </li>
                </ul>
              </li>
              <li>Action коммитит созданные файлы в репо.</li>
              <li>
                Запускается Action сборки и деплоя веб-приложения, которое собирается с использованием
                актуального JSON-файла с данными обо всех ссылках и деплоится на GitHub Pages. Это и есть
                страницы, где вы сейчас находитесь 😀.
              </li>
            </ol>
            <p class="mt-4 p-4 bg-gray-50 rounded-lg border border-gray-200 text-gray-700">
              В итоге, мы получаем актуальные списки ссылок и архив в виде истории коммитов. Ссылки доступны
              как в Markdown-файлах, так и в виде простого web-приложения.
            </p>
          </div>
        </section>
      </div>

      <!-- Footer -->
      <div class="bg-gray-50 px-6 py-4 sm:px-10 border-t border-gray-200">
        <p class="text-sm text-gray-500 mb-1">
          Проект с открытым исходным кодом. Более подробная информация доступна в
          <a
            href="https://github.com/hazadus/readwise-links"
            target="_blank"
            class="text-blue-600 hover:text-blue-800"
            >GitHub репозитории</a
          >.
        </p>
        <p class="text-xs text-gray-400">Последнее обновление: {{ formattedBuildTime }}</p>
      </div>
    </div>
  </div>
</template>
