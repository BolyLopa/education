# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: NoteWeaver
def add_reminder(title, description="", due_date=None):
    """Add a reminder with optional due date."""
    reminders = get_state().get("reminders", [])
    new_id = len(reminders) + 1
    reminder = {
        "id": new_id,
        "title": title,
        "description": description,
        "due_date": due_date.isoformat() if due_date else None,
        "done": False,
    }
    reminders.append(reminder)
    state["reminders"] = reminders
    print(f"Reminder added: {title}")
    return reminder


def list_reminders():
    """List all reminders with status."""
    reminders = get_state().get("reminders", [])
    for r in sorted(reminders, key=lambda x: x.get("due_date") or "9999-12-31"):
        due = r["due_date"][:10] if r["due_date"] else "no date"
        status = "✓ done" if r["done"] else f"⏳ due {due}"
        print(f"  [{r['id']}] {status} - {r['title']}")


def complete_reminder(reminder_id):
    """Mark a reminder as done."""
    reminders = get_state().get("reminders", [])
    for r in reminders:
        if r["id"] == reminder_id:
            r["done"] = True
            state["reminders"] = reminders
            print(f"Reminder {reminder_id} completed.")
            return True
    print(f"No reminder found with id {reminder_id}.")
    return False


def check_due_reminders():
    """Print reminders due today."""
    from datetime import date, datetime
    today = date.today().isoformat()
    reminders = get_state().get("reminders", [])
    due_today = [r for r in reminders if r["due_date"] == today and not r["done"]]
    if due_today:
        print(f"⚠ You have {len(due_today)} reminder(s) due today:")
        for r in due_today:
            print(f"  - {r['title']}")
    else:
        print("No reminders due today.")


def remove_reminder(reminder_id):
    """Remove a reminder."""
    reminders = get_state().get("reminders", [])
    new_list = [r for r in reminders if r["id"] != reminder_id]
    state["reminders"] = new_list
    print(f"Reminder {reminder_id} removed.")


def init_reminders():
    """Initialize empty reminders list."""
    get_state()["reminders"] = []
