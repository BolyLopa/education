# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: NoteWeaver
class NoteWeaver:
    def __init__(self):
        self.notes = {}  # {id: {'title': str, 'content': str, 'tags': list, 'links': list, 'created_at': int}}
        self.next_id = 1

    def add_note(self, title, content, tags=None, links=None):
        if tags is None:
            tags = []
        if links is None:
            links = []
        note_id = f"note_{self.next_id}"
        self.notes[note_id] = {
            'title': title,
            'content': content,
            'tags': tags,
            'links': links,
            'created_at': int(time.time())
        }
        self.next_id += 1
        return note_id

    def get_note(self, note_id):
        return self.notes.get(note_id)

    def search_notes(self, query):
        results = []
        query_lower = query.lower()
        for note_id, note in self.notes.items():
            if (query_lower in note['title'].lower() or
                query_lower in note['content'].lower() or
                any(query_lower in tag.lower() for tag in note['tags'])):
                results.append(note)
        return results

    def link_notes(self, source_id, target_ids):
        if source_id not in self.notes:
            return False
        if not isinstance(target_ids, list):
            target_ids = [target_ids]
        for tid in target_ids:
            if tid in self.notes:
                self.notes[source_id]['links'].append(tid)
        return True

    def get_daily_draft(self, date_str=None):
        import datetime
        if date_str is None:
            date_str = datetime.date.today().isoformat()
        draft_key = f"draft_{date_str}"
        if draft_key not in self.notes:
            self.notes[draft_key] = {
                'title': f'Черновик на {date_str}',
                'content': '',
                'tags': ['draft'],
                'links': [],
                'created_at': int(datetime.datetime.now().timestamp())
            }
        return self.notes[draft_key]
