# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: NoteWeaver
TEMPLATE_REGISTRY = {}


def register_template(name, fields):
    """Зарегистрировать шаблон заметки."""
    TEMPLATE_REGISTRY[name] = {
        "name": name,
        "fields": fields,
    }


def new_note_from_template(template_name):
    """Создать записи по шаблону. Возвращает (note_dict, missing)."""
    template = TEMPLATE_REGISTRY.get(template_name)
    if not template:
        raise ValueError(f"Неизвестный шаблон: {template_name}")

    note = {"_template": template_name}
    for field in template["fields"]:
        value = input(f"{field}: ")
        note[field] = value

    return note, []


def list_templates():
    """Вывести список доступных шаблонов."""
    if not TEMPLATE_REGISTRY:
        print("Доступные шаблоны:\n" + "  - Нет зарегистрированных шаблонов")
        return
    for name in sorted(TEMPLATE_REGISTRY):
        fields = TEMPLATE_REGISTRY[name]["fields"]
        print(f"{name} ({', '.join(fields)})")


# --- Зарегистрированные шаблоны ---

register_template("Daily Journal", ["title", "body", "mood"])
register_template("Quick Idea", ["idea", "tags"])
register_template("Meeting Notes", ["attendees", "topics", "action_items"])
register_template("Task List", ["tasks", "priority"])
