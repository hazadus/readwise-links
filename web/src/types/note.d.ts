interface Tag {
  name: string;
  type: string;
  created: number;
}

// В API Readwise Reader всё является документом: пост, highlight,
// заметка к highlight, и имеет одинаковую структуру.
declare interface ReadwiseDocument {
  id: string;
  url: string;
  source_url: string | null;
  title: string | null;
  author: string | null;
  source: string | null;
  category: string;
  location: string | null;
  tags: Record<string, Tag | undefined> | null;
  site_name: string | null;
  word_count: number | null;
  notes: string;
  summary: string | null;
  image_url: string | null;
  parent_id: string | null;
  reading_progress: number;
  content: string | null;
  html_content: string | null;
  published_date: string | null;
  created_at: string;
  updated_at: string;
  saved_at: string;
  first_opened_at: string | null;
  last_opened_at: string | null;
  last_moved_at: string;
  // Эти два поля мы добавляем в своём Python-скрипте:
  highlights?: ReadwiseDocument[];
  notes_attached?: ReadwiseDocument[];
}

// Определяем тип для поста (ссылки на статьи и книги) в Readwise Reader
type Article = ReadwiseDocument;

declare module "@/assets/articles.json" {
  const articles: Article[];
  export default articles;
}
