# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: NoteWeaver
def sort_notes(notes, key='date'):
    reverse = {'date': True, 'priority': False, 'name': False}.get(key, True)
    return sorted(notes, key=lambda n: (n.get('created_at', ''), -n.get('priority', 0), n.get('title', '')), reverse=reverse)
