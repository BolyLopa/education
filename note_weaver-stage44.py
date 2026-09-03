# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: NoteWeaver
import shutil, datetime, os

def backup_notes_data(data_path, backup_dir=None):
    """Сохраняет копию файла данных в archive с датой."""
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_path), 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'notes_backup_{timestamp}')
    shutil.copy2(data_path, backup_path)
    return backup_path
