# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: NoteWeaver
def calculate_weekly_stats(notes):
    from collections import defaultdict
    weekly = defaultdict(lambda: {'count': 0, 'total_chars': 0})
    for note in notes:
        if not isinstance(note.get('created_at'), str) or len(note['created_at']) < 10:
            continue
        try:
            date_str = note['created_at'][:10]
            week_start = (int(date_str.split('-')[2]) // 7 - 1) * 7 + 1
            week_key = f"{date_str[:4]}-{date_str[5:7]}-W{week_start}"
        except Exception:
            continue
        weekly[week_key]['count'] += 1
        if 'content' in note:
            weekly[week_key]['total_chars'] += len(note['content'])
    return dict(sorted(weekly.items()))
