# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: NoteWeaver
def migrate_to_v46():
    """Version 46: migrate note structure to include daily drafts and search index."""
    global NOTES, THEMES, LINKS, SEARCH_INDEX, DAILY_DRAFTS
    NOTES = {}
    THEMES = {}
    LINKS = {}
    SEARCH_INDEX = {}
    DAILY_DRAFTS = {}
    for note_id, note_data in NOTES.items():
        if 'drafts' not in note_data:
            note_data['drafts'] = {}
        if 'links' not in note_data:
            note_data['links'] = []
        if 'searchable' not in note_data:
            note_data['searchable'] = True
    return NOTES, THEMES, LINKS, SEARCH_INDEX, DAILY_DRAFTS
