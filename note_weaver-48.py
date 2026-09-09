# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: NoteWeaver
def _find_linked_notes(self, source_id):
    """Find notes that link to or are linked from the given note."""
    linked_ids = set()
    for note in self._notes.values():
        for link_id in note.get('links', []):
            if link_id == source_id:
                linked_ids.add(note['id'])
    return list(linked_ids)
