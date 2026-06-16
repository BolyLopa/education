# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: NoteWeaver
def filter_notes(status=None, category=None, tags=None):
    filtered = []
    for note in notes:
        if status and note.get('status') != status: continue
        if category and note.get('category') != category: continue
        if tags is not None and set(note.get('tags', [])) & set(tags) == set(): continue
        filtered.append(note)
    return filtered

def search_notes(query):
    query = query.lower()
    results = []
    for note in notes:
        text = f"{note['title']} {note['content']}".lower()
        if query in text or any(q in tag.lower() for q in [query] + (note.get('tags', []) or [])):
            results.append(note)
    return results

def get_daily_drafts():
    today = datetime.date.today().isoformat()
    drafts = [n for n in notes if n.get('is_draft') and n.get('date_created') == today]
    return drafts
