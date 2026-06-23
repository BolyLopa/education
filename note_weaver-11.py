# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: NoteWeaver
import json, os

DATA_FILE = "notes_data.json"

def save_notes(notes):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
