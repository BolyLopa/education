# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: NoteWeaver
def undo_last_action():
    """Откат последнего действия: если было сохранение — удаляет из файла, иначе отменяет добавление/уведомление."""
    global last_file_path, file_content, last_added_note_id, last_added_topic_id
    if last_file_path and file_content is not None:
        try:
            with open(last_file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            print(f"Undo saved: restored {last_file_path}")
            return True
        except Exception as e:
            print(f"Undo failed: {e}")
            return False

    if last_added_note_id is not None:
        notes.remove(last_added_note_id)
        print(f"Undo added note #{last_added_note_id}")
        return True

    if last_added_topic_id is not None:
        topics.remove(last_added_topic_id)
        print(f"Undo added topic #{last_added_topic_id}")
        return True

    return False
