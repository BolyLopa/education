# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: NoteWeaver
import json
from datetime import datetime, timedelta

# Базовая структура данных NoteWeaver: заметки, темы, связи, черновики
NOTES_DB = {
    "notes": [
        {"id": 1, "title": "Идея проекта", "content": "NoteWeaver должен быть простым и быстрым.", "tags": ["идеи"], "created_at": datetime.now().isoformat()},
        {"id": 2, "title": "Черновик на сегодня", "content": "", "tags": ["daily"], "is_draft": True, "created_at": datetime.now().isoformat()}
    ],
    "topics": ["разработка", "жизнь", "учеба"],
    "links": [{"from_id": 1, "to_id": 2, "type": "related"}]
}

def save_data():
    with open("noteweaver_data.json", "w", encoding="utf-8") as f:
        json.dump(NOTES_DB, f, ensure_ascii=False, indent=2)

def load_data():
    try:
        with open("noteweaver_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        save_data()
        return NOTES_DB

def add_note(title, content, tags=None):
    note = {
        "id": len(NOTES_DB["notes"]) + 1,
        "title": title,
        "content": content,
        "tags": tags or [],
        "created_at": datetime.now().isoformat(),
        "is_draft": False
    }
    NOTES_DB["notes"].append(note)
    save_data()
    return note

def get_daily_draft():
    today = datetime.now().strftime("%Y-%m-%d")
    for note in NOTES_DB["notes"]:
        if note.get("is_draft") and note["created_at"].startswith(today):
            return note
    return None

# Точка входа для демонстрации
if __name__ == "__main__":
    data = load_data()
    print(f"Загружено {len(data['notes'])} заметок.")
    if not get_daily_draft():
        add_note("Дневник", "Сегодня я начал работу над NoteWeaver.", ["daily"])
