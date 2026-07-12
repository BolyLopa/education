# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: NoteWeaver
def print_notes_table(notes: list[dict], max_title_len=35, max_body_len=40):
    """Форматированный вывод заметок в виде таблицы в консоль."""
    if not notes:
        print("Ничего не найдено.")
        return

    for n in sorted(notes, key=lambda x: x.get('created', 0), reverse=True):
        title = (n.get('title') or '')[:max_title_len]
        body = (n.get('body') or '')[:max_body_len]
        tags = ', '.join(f'#{t}' for t in n.get('tags', []) if t)
        ts = n.get('created', '—').split('T')[0] if isinstance(n.get('created'), str) else '—'

        print(f"\n{'─'*56}")
        print(f"  📌 {title}")
        print(f"  🕐 {ts} | {body}")
        print(f"  🏷️  {tags}".rstrip())
