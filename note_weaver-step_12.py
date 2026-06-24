# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: NoteWeaver
import json, os, sys

def load_notes_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            notes = [Note(note.get('id'), note.get('title', ''), note.get('content', '')) for note in data]
        elif isinstance(data, dict) and 'notes' in data:
            notes = [Note(n['id'], n['title'], n['content']) for n in data['notes']]
        else:
            print("Неверный формат JSON данных.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return []
    except Exception as e:
        print(f"Произошла неизвестная ошибка при загрузке: {e}")
        return []

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "notes_backup.json"
    loaded_notes = load_notes_from_file(file_path)
    print(f"Загружено {len(loaded_notes)} заметок.")
