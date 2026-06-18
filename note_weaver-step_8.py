# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: NoteWeaver
def run_cli():
    print("=== NoteWeaver CLI ===")
    while True:
        cmd = input("\nКоманда (create, list, search, journal, exit): ").strip().lower()
        if not cmd: continue
        elif cmd == "exit": break
        elif cmd.startswith("create"): parts = cmd.split(maxsplit=1); title, content = (parts[0], "") if len(parts) < 2 else (parts[0], "\n".join(parts[1:])); print(f"Заметка создана: {title}")
        elif cmd == "list": print("Список заметок:\n(реализация списка)")
        elif cmd.startswith("search"): query = input("Ключевое слово: "); print(f"Поиск по '{query}': (результаты)")
        elif cmd == "journal": today = __import__("datetime").date().isoformat(); print(f"Черновик на {today}:"); content = input("Текст черновика: "); print("Сохранено.")
        else: print("Неизвестная команда")
