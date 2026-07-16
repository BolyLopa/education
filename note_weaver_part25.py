# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: NoteWeaver
def _parse_date_safe(date_str, default=None):
    if not date_str or not isinstance(date_str, str):
        return default
    try:
        from datetime import datetime
        fmts = ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y')
        for f in fmts:
            try:
                return datetime.strptime(date_str.strip(), f)
            except ValueError:
                continue
    except Exception:
        pass
    return default

def _format_date_error(msg):
    print(f"[NoteWeaver] Ошибка: {msg}")
