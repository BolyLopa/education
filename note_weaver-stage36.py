# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: NoteWeaver
def check_and_repair_data(store, log=None):
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    if log is None:
        log = []
    
    issues = []
    
    # Проверка 1: все ссылки на заметки существуют
    for note in store.notes.values():
        for link_target_id in note.get('links_to', []):
            if link_target_id not in store.notes:
                issues.append(f"Ссылка из заметки {note['id']} указывает на несуществующую заметку {link_target_id}")
    
    # Проверка 2: все теги в заметках корректны (не пустые строки)
    for note in store.notes.values():
        invalid_tags = [t for t in note.get('tags', []) if not isinstance(t, str) or len(t.strip()) == 0]
        if invalid_tags:
            issues.append(f"Заметка {note['id']} содержит невалидные теги: {invalid_tags}")
    
    # Проверка 3: daily_drafts соответствует датам в notes
    for date_str, content in store.daily_drafts.items():
        if not isinstance(content, str):
            issues.append(f"Черновик на {date_str} содержит не строковое значение")
    
    repaired = []
    if issues:
        # Попытка исправить: удалить несуществующие ссылки
        for note in store.notes.values():
            valid_targets = [tid for tid in note.get('links_to', []) if tid in store.notes]
            invalid_links = [lid for lid in note.get('links_to', []) if lid not in store.notes]
            if invalid_links:
                old_links = note['links_to']
                note['links_to'] = valid_targets
                repaired.append(f"Исправлена {len(invalid_links)} ссылок в заметке {note['id']}")
        
        # Удаление невалидных тегов
        for note in store.notes.values():
            old_tags = list(note.get('tags', []))
            valid_tags = [t for t in old_tags if isinstance(t, str) and len(t.strip()) > 0]
            if old_tags != valid_tags:
                note['tags'] = valid_tags
                repaired.append(f"Очищены теги в заметке {note['id']}")
        
        log.extend(repaired)
    else:
        log.append("Все данные целостны, проблем не обнаружено.")
    
    return issues if not repaired else issues + ["Данные частично отремонтированы."]
