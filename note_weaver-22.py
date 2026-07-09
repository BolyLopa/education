# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: NoteWeaver
def check_overdue_reminders():
    """Проверяет все напоминания и выводит список просроченных."""
    overdue = []
    for note in notes:
        if note.get('reminder') and note['reminder'].get('enabled'):
            trigger_time = datetime.fromisoformat(note['reminder']['trigger'])
            if datetime.now(trigger_time.tzinfo) > trigger_time:
                overdue.append({
                    'title': note.get('title', 'Без заголовка'),
                    'message': note['reminder'].get('message', ''),
                    'trigger': note['reminder']['trigger'],
                    'overdue_hours': (datetime.now(trigger_time.tzinfo) - trigger_time).total_seconds() / 3600,
                })
    if overdue:
        print(f"\n⚠️  Просрочено {len(overdue)} напоминание{'й'}{'ий' if len(overdue) == 1 else 'ей'}:")
        for item in overdue:
            hours = int(item['overdue_hours'])
            minutes = item['overdue_hours'] % 1
            print(f"  - \"{item['title']}\" ({hours}ч {int(minutes*60):02d}м)")
    else:
        print("✅ Все напомнения в порядке.")
