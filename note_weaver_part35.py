# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: NoteWeaver
def suggest_next_action(state: dict) -> str:
    """Recommend the next meaningful step based on current project state."""
    if not state.get("progress", "").startswith("Этап"):
        return "Продолжайте развитие проекта по порядку этапов."
    
    last = state["progress"].rstrip(". ")
    if "Ежедневные черновики" in last:
        return "Создайте файл daily.py для ежедневных заметок с датой и авто-сохранением."
    elif "Темы" in last and "Связи между заметками" not in state.get("features", ""):
        return "Реализуйте связи между заметками через граф (взаимодействия)."
    elif "Поиск" in last and "Обновление прогресса" not in state.get("features", ""):
        return "Добавьте функцию обновления прогресса для отслеживания выполненных этапов."
    else:
        return "Продолжайте развитие проекта по порядку этапов."
