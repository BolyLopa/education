# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: NoteWeaver
DOCS = """
# Use Cases
## 1. Daily Journaling
Write a journal entry for the current date. The system auto-creates the entry if
the date is new, and records the note under the "journal" theme with the date
as its title.

## 2. Topic Management
Create a new topic (e.g., "projects", "travel") and add notes under it.
Topics act as categories; each note belongs to one topic and can be listed
via the topics view.

## 3. Note Linking
While editing a note, type a reference like `[note-title]` to link to another
note. The system resolves the reference and creates a bidirectional link
between the two notes, enabling a knowledge-graph style structure.

## 4. Search
Type a search query in the search bar. The system finds all notes whose
content or title matches the query, and optionally filters by topic.

## 5. Daily Journal Review
At the end of each day, the system prompts the user to write a journal entry
if one hasn't been created yet. This ensures a consistent daily habit.
"""
