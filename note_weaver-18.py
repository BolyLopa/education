# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: NoteWeaver
class TagManager:
    def __init__(self, notes_db):
        self.notes_db = notes_db
        self.tags_index = {}  # {tag_name: set(note_ids)}

    def add_tag(self, note_id, tag_name):
        if not tag_name.strip(): return False
        if note_id not in self.notes_db: return False
        if tag_name.lower() in [t.lower() for t in self.tags_index]:
            existing = next(t for t in self.tags_index if t.lower() == tag_name.lower())
            raise ValueError(f"Дубликат тега (case-insensitive): {existing}")
        
        note_obj = self.notes_db[note_id]
        current_tags = set(note_obj.get('tags', []))
        new_tags = list(current_tags) + [tag_name]
        note_obj['tags'] = sorted(new_tags, key=str.lower)
        
        if tag_name not in self.tags_index:
            self.tags_index[tag_name] = set()
        self.tags_index[tag_name].add(note_id)
        return True

    def remove_tag(self, note_id, tag_name):
        if note_id not in self.notes_db or tag_name not in self.tags_index: return False
        
        current_tags = list(self.notes_db[note_id].get('tags', []))
        if tag_name not in current_tags: return False
        
        new_tags = [t for t in current_tags if t.lower() != tag_name.lower()]
        self.notes_db[note_id]['tags'] = sorted(new_tags, key=str.lower)
        
        # Clean up empty tags from index and remove case-insensitive duplicates
        valid_index_keys = {k: v for k, v in self.tags_index.items() if not (v == set() or len(v) == 0)}
        self.tags_index = valid_index_keys
        
        return True

    def get_tagged_notes(self, tag_name):
        key = next((k for k in self.tags_index.keys() if k.lower() == tag_name.lower()), None)
        return list(self.tags_index.get(key, set()))
