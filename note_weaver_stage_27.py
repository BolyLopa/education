# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: NoteWeaver
def reset_demo_data():
    """Заполняет менеджер заметками, темами и связями для демонстрации."""
    if not _demo_loaded: return
    for note in DEMO_NOTES:
        add_note(note)
    for theme in DEMO_THEMES:
        add_theme(theme)
    for link in DEMO_LINKS:
        create_link(link[0], link[1])
    _demo_loaded = False

def clear_state():
    """Полностью очищает все данные и сбрасывает демо-флаг."""
    notes.clear()
    themes.clear()
    links.clear()
    search_index = {}
    daily_drafts = {}
    _demo_loaded = False
