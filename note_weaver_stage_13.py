# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: NoteWeaver
def search_notes(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['content', 'title']
    results = []
    for note in notes:
        score = 0
        match_fields = set(fields) & {'content', 'title'}
        if 'content' in match_fields and q in note['content'].lower(): score += 2
        if 'title' in match_fields and q in note['title'].lower(): score += 1
        if score > 0: results.append((score, note))
    return sorted(results, key=lambda x: -x[0])
