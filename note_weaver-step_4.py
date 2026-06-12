# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: NoteWeaver
def edit_note(note_id: str, new_content: dict) -> Optional[Note]:
    """Редактирует заметку по ID, возвращая обновлённый объект или None при ошибке."""
    try:
        note = _notes_db[note_id]
        if not note:
            print(f"Заметка с ID {note_id} не найдена.")
            return None
        
        # Обновляем поля из словаря new_content, если они предоставлены
        for key in new_content:
            if hasattr(note, key):
                setattr(note, key, new_content[key])
        
        _notes_db[note_id] = note  # Сохраняем изменения в базе (словаре)
        print(f"Заметка {note_id} успешно обновлена.")
        return note
    except Exception as e:
        print(f"Ошибка при редактировании заметки {note_id}: {e}")
        return None
