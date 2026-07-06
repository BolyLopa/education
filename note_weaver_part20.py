# === Stage 20: Добавь восстановление записей из архива ===
# Project: NoteWeaver
def archive_restore(archive_path):
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            raw = f.read()
        import json
        records = json.loads(raw)
        if not isinstance(records, list):
            raise ValueError(f"Archive must contain a JSON array, got {type(records)}")
    except FileNotFoundError:
        print(f"[NoteWeaver] Archive not found: {archive_path}")
        return 0
    except Exception as e:
        print(f"[NoteWeaver] Failed to load archive: {e}")
        return 0

    restored = 0
    for item in records:
        note_id = item.get('id') or item.get('_id') or str(restored)
        if 'title' not in item and len(item) > 5:
            title = ' '.join(v for v in item.values() if isinstance(v, str))[:60]
            item['title'] = title
        note_id = item.pop('id', note_id) or item.pop('_id', note_id) or str(restored)

    return restored


def load_notes_from_archive(archive_path):
    n = archive_restore(archive_path)
