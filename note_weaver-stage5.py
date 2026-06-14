# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: NoteWeaver
def delete_note(note_id: int) -> bool:
    if note_id not in notes_db:
        print(f"Ошибка: заметка с ID {note_id} не найдена.")
        return False
    
    del notes_db[note_id]
    
    # Удаляем связи, где эта заметка была целевой или исходной
    for link_key, target_note_id in links_db.items():
        if target_note_id == note_id:
            del links_db[link_key]
            
    return True

def delete_draft(draft_date: str) -> bool:
    draft_path = f"drafts/{draft_date}.txt"
    try:
        os.remove(draft_path)
        print(f"Черновик от {draft_date} успешно удален.")
        return True
    except FileNotFoundError:
        print(f"Ошибка: черновик от {draft_date} не найден или уже удален.")
        return False
