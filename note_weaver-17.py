# === Stage 17: Добавь группировку записей по категориям ===
# Project: NoteWeaver
def group_notes_by_category(notes, categories):
    grouped = {cat: [] for cat in categories}
    for note in notes:
        category = note.get('category', 'Uncategorized')
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(note)
    return grouped
