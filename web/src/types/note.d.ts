declare interface Note {
  id: string;
  url: string;
  source_url: string | null;
  title: string | null;
  author: string | null;
  source: string;
  category: string;
  location: string | null;
  tags: string[] | null;
  site_name: string | null;
  word_count: number | null;
  notes: string;
  summary: string | null;
  image_url: string | null;
  parent_id: string;
  reading_progress: number;
  content: string;
  html_content: string | null;
  published_date: string | null;
  created_at: string;
  updated_at: string;
  saved_at: string;
  first_opened_at: string | null;
  last_opened_at: string | null;
  last_moved_at: string;
}

declare module "@/assets/note.json" {
  const notes: Note[];
  export default notes;
}
