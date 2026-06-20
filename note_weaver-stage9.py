# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: NoteWeaver
def import_initial_data(json_string: str) -> None:
    """Загружает начальные данные из JSON-строки в глобальное хранилище."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Инициализация структур данных при первом запуске или обновлении
        global notes, topics, links, drafts
        
        # Загрузка заметок (структура: {id: {"title": str, "content": str, "topic_id": int}})
        if "notes" in data:
            for note_data in data["notes"]:
                note = {
                    "id": note_data.get("id"),
                    "title": note_data.get("title", ""),
                    "content": note_data.get("content", ""),
                    "topic_id": note_data.get("topic_id")
                }
                notes.append(note)
        
        # Загрузка тем (структура: {id: {"name": str}})
        if "topics" in data:
            for topic_data in data["topics"]:
                topic = {
                    "id": topic_data.get("id"),
                    "name": topic_data.get("name", "")
                }
                topics.append(topic)
        
        # Загрузка связей (структура: [(from_id, to_id)])
        if "links" in data and isinstance(data["links"], list):
            links.clear()  # Очистка старых связей перед загрузом новых
            for link_data in data["links"]:
                from_id = link_data.get("from")
                to_id = link_data.get("to")
                if from_id is not None and to_id is not None:
                    links.append((from_id, to_id))
        
        # Загрузка черновиков (структура: {date: content})
        if "drafts" in data:
            for date_content in data["drafts"]:
                if isinstance(date_content, dict):
                    date = date_content.get("date")
                    content = date_content.get("content", "")
                    drafts[date] = content
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
