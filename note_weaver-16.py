# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: NoteWeaver
def calculate_monthly_stats(stats: dict, month: int) -> None:
    """Наполняет статистику за текущий месяц на основе всех заметок."""
    current_year = datetime.now().year
    start_date = date(current_year, month, 1)
    end_date = date(current_year, month + 1, 1)

    for note in all_notes:
        if not note.created_at or not isinstance(note.created_at, datetime):
            continue
        try:
            created_dt = datetime.fromisoformat(note.created_at.replace('Z', '+00:00'))
            if start_date <= created_dt < end_date:
                topic_key = f"{note.topic}" if note.topic else "Без темы"
                stats.setdefault(topic_key, 0)
                stats[topic_key] += 1
        except (ValueError, TypeError):
            continue

    for draft in daily_drafts.values():
        try:
            created_dt = datetime.fromisoformat(draft.created_at.replace('Z', '+00:00'))
            if start_date <= created_dt < end_date:
                stats["Черновики"] += 1
        except (ValueError, TypeError):
            continue
