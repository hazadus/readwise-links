/**
 * Утилиты для генерации Markdown
 */

// Импортируем типы
/// <reference path="../types/note.d.ts" />

/**
 * Генерирует Markdown представление статьи с highlights и комментариями
 */
export function generateArticleMarkdown(article: Article): string {
  let markdown = "";

  // Заголовок статьи
  markdown += `# ${article.title}\n\n`;

  // Автор
  if (article.author) {
    markdown += `**Автор:** ${article.author}\n`;
  }

  // Ссылка на источник
  const sourceUrl = article.source_url || article.url;
  if (sourceUrl) {
    markdown += `**Ссылка:** ${sourceUrl}\n`;
  }

  // Дата публикации
  if (article.published_date) {
    const publishedDate = new Date(article.published_date).toLocaleDateString("ru-RU", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    markdown += `**Опубликовано:** ${publishedDate}\n`;
  }

  // Дата сохранения
  if (article.saved_at) {
    const savedDate = new Date(article.saved_at).toLocaleDateString("ru-RU", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    markdown += `**Сохранено:** ${savedDate}\n`;
  }

  // Количество слов
  if (article.word_count) {
    markdown += `**Количество слов:** ${article.word_count}\n`;
  }

  // Теги
  if (article.tags) {
    const tagNames = Object.values(article.tags)
      .filter((tag): tag is Tag => tag !== undefined)
      .map((tag) => `#${tag.name}`)
      .join(" ");
    if (tagNames) {
      markdown += `**Теги:** ${tagNames}\n\n`;
    }
  }

  // Заметка пользователя
  if (article.notes) {
    markdown += `## Заметка\n\n${article.notes}\n\n`;
  }

  // Summary
  if (article.summary) {
    markdown += `## Краткое содержание\n\n${article.summary}\n\n`;
  }

  // Highlights
  if (article.highlights && article.highlights.length > 0) {
    markdown += `## Highlights\n\n`;

    // Сортируем highlights по дате создания
    const sortedHighlights = [...article.highlights].sort((a, b) => {
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return dateA.getTime() - dateB.getTime();
    });

    sortedHighlights.forEach((highlight, index) => {
      markdown += `> ${highlight.content}\n\n`;

      // Комментарии к выделению
      if (highlight.notes_attached && highlight.notes_attached.length > 0) {
        markdown += `**Комментарии:**\n\n`;
        highlight.notes_attached.forEach((note, noteIndex) => {
          markdown += `${noteIndex + 1}. ${note.content}\n`;
        });
        markdown += "\n";
      }
    });
  }

  return markdown.trim();
}

/**
 * Копирует текст в буфер обмена
 */
export async function copyToClipboard(text: string): Promise<boolean> {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return true;
    } else {
      // Fallback для старых браузеров
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-999999px";
      textArea.style.top = "-999999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      const result = document.execCommand("copy");
      document.body.removeChild(textArea);
      return result;
    }
  } catch (error) {
    console.error("Ошибка при копировании в буфер обмена:", error);
    return false;
  }
}
