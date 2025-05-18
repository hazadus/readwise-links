interface Tag {
  name: string;
  type: string;
  created: number;
}

declare interface Note {
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
  highlights?: Note[];
  notes_attached?: Note[];
}

declare module "@/assets/articles.json" {
  const notes: Note[];
  export default notes;
}
