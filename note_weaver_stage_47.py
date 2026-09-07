# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: NoteWeaver
def demo():
    """Демонстрация основных сценариев NoteWeaver."""
    print("=" * 60)
    print("NoteWeaver — Демонстрация основных сценариев")
    print("=" * 60)
    
    # 1. Создание заметки
    note = Note()
    note.title = "Мой первый проект"
    note.content = "Это начало моего Python-проекта."
    note.tags = ["python", "coding", "learning"]
    note.add("Идея: создать менеджер заметок с темами и поиском.")
    note.add("Технологии: Python, без внешних библиотек, в одном файле.")
    note.save()
    print(f"✓ Заметка сохранена: {note.title}")
    
    # 2. Поиск по содержимому
    found = NotesManager.search(notes, "Python")
    print(f"✓ Найдено заметок по 'Python': {len(found)}")
    
    # 3. Поиск по тегам
    tagged = NotesManager.search_by_tag(notes, "python")
    print(f"✓ Найдено заметок по тегу 'python': {len(tagged)}")
    
    # 4. Создание ежедневного черновика
    daily = DailyDraft()
    daily.date = datetime.date.today()
    daily.add("Напомнить: проверить работу поиска.")
    daily.add("Задача: добавить поддержку CSV-экспорта.")
    daily.save()
    print(f"✓ Черновик за {daily.date} сохранён")
    
    # 5. Создание темы и добавление заметок
    topic = Topic()
    topic.title = "Изучение Python"
    topic.add_note(note)
    print(f"✓ Создана тема: {topic.title}")
    
    # 6. Установление связи между заметками
    note2 = Note()
    note2.title = "Документация"
    note2.content = "План документации проекта."
    note2.save()
    note.link(note2, "Документация")
    print(f"✓ Заметка связана с {note2.title}")
    
    # 7. Просмотр всех заметок
    print("\n" + "=" * 60)
    print("Все сохранённые заметки:")
    print("=" * 60)
    for n in notes:
        print(f"  [{n.title}]")
    
    print("\n" + "=" * 60)
    print("Demo завершена успешно! 🎉")
    print("=" * 60)
