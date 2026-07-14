# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: NoteWeaver
def print_note(note: dict) -> None:
    """Компактный вывод одной записи."""
    if not note:
        return
    fields = [
        ("id", str(note.get("id"))),
        ("title", note.get("title") or "(нет заголовка)"),
        ("body", note.get("body")[:120] + "..." if len(str(note.get("body",""))) > 120 else note.get("body","")),
    ]
    extra = []
    for key in ("tags", "theme", "linked_to"):
        val = note.get(key)
        if val:
            extra.append((key, str(val)))

    print(f"\n{'─'*50}")
    print(f"[{fields[0][1]}] {fields[1][1]}")
    print(f"  Тело: {fields[2][1]}")
    for k, v in extra:
        print(f"  {k}: {v}")
    if note.get("created_at"):
        print(f"  Создана: {note['created_at']}")
