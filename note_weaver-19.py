# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: NoteWeaver
def archive_old_notes(days=30):
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=days)
    archived_count = 0
    for note in notes:
        if note.get('created_at') and note['created_at'] < cutoff:
            note['status'] = 'archived'
            note['archived_at'] = datetime.now().isoformat()
            archived_count += 1
    print(f"Archived {archived_count} notes older than {days} days.")
