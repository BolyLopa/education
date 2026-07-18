# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: NoteWeaver
def demo():
    print("NoteWeaver Demo — быстрый ручной тест")
    n = Note()
    t1, t2, t3 = Theme("Python"), Theme("JS"), Theme("Идеи")
    c1 = Content(t1)
    c2 = Content(t2)
    c3 = Content(t3); c4 = Content(t1)
    c5 = Content(c3, "c4", "связь Python↔Идеи")
    n.add(c1, "Введение в Python"); n.add(c2, "ES6 features"); n.add(c3, "Список идей"); n.add(c4, "Рефакторинг"); n.add(c5)
    print(f"Заметки: {len(n)}")
    print(f"Поиск 'Python': {[n.search('Python')]}")
    print(f"Поиск 'ES6': {[n.search('ES6')]}")
    print(f"Темы: {set(c.theme for c in n)}")
    print(f"Черновик дня: {DailyDraft()}")
