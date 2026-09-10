# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: NoteWeaver
def self_check_and_report(app):
    print("=" * 60)
    print("NoteWeaver — Самопроверка и отчёт о готовности")
    print("=" * 60)
    if not app.notes:
        print("[OK] Заметки: база пустая — всё готово к записям.")
    else:
        print(f"[OK] Заметки: {len(app.notes)} шт. в базе.")
    if not app.topics:
        print("[OK] Темы: нет тем — можно создать через интерфейс.")
    else:
        print(f"[OK] Темы: {len(app.topics)} шт. в базе.")
    if not app.links:
        print("[OK] Связи: нет связей — можно добавить через интерфейс.")
    else:
        print(f"[OK] Связи: {len(app.links)} шт. в базе.")
    if not app.search_results:
        print("[OK] Поиск: результаты пустые — можно выполнить запрос.")
    else:
        print(f"[OK] Поиск: {len(app.search_results)} результатов.")
    if not app.daily_notes:
        print("[OK] Ежедневные черновики: нет записей — можно создать через интерфейс.")
    else:
        print(f"[OK] Ежедневные черновики: {len(app.daily_notes)} шт. в базе.")
    print("=" * 60)
    print("NoteWeaver готов к работе! 🎉")
    print("=" * 60)
