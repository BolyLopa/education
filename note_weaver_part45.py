# === Stage 45: Добавь восстановление из резервной копии ===
# Project: NoteWeaver
def restore_from_backup(backup_path: str) -> bool:
    """Восстанавливает данные из JSON-резервной копии. Возвращает True на успех."""
    import json, os
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    try:
        with open(backup_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict) or "notes" not in data:
            print("Неверный формат резервной копии")
            return False
        _notes = data["notes"]
        _themes = data.get("themes", {})
        _connections = data.get("connections", [])
        _diaries = data.get("diaries", {})
        _settings = data.get("settings", {})
        NotesManager._notes = _notes
        NotesManager._themes = _themes
        NotesManager._connections = _connections
        NotesManager._diaries = _diaries
        NotesManager._settings = _settings
        print(f"✅ Резервная копия восстановлена ({len(_notes)} заметок)")
        return True
    except Exception as e:
        print(f"❌ Ошибка восстановления: {e}")
        return False
