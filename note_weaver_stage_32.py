# === Stage 32: Добавь журнал действий пользователя ===
# Project: NoteWeaver
def log_action(action_type, details):
    """Append a user action to the in-memory journal."""
    global _action_log
    entry = {
        "timestamp": datetime.now().isoformat(),
        "type": action_type,
        "details": details,
    }
    _action_log.append(entry)


def view_journal():
    """Return and print all logged actions in reverse chronological order."""
    if not _action_log:
        print("Журнал действий пуст.")
        return []
    log = list(reversed(_action_log))
    for i, entry in enumerate(log):
        print(f"[{i+1}] {entry['timestamp'][:19]} | {entry['type']}")
        if isinstance(entry["details"], str) and len(entry["details"]) > 20:
            print(f"     -> {entry['details'][:20]}...")
        else:
            print(f"     -> {entry['details']}")
    return log


# Пример использования:
log_action("create_note", "Создана заметка 'Привет мир'")
log_action("search", "Поиск по ключевому слову 'python'")
view_journal()
