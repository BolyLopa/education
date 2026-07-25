# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: NoteWeaver
def switch_profile():
    """Переключение активного пользовательского профиля."""
    profiles = {p['name']: p for p in user_profiles}
    if not profiles:
        print("Нет сохранённых профилей.")
        return
    name = input("Имя профиля: ").strip()
    active = profiles.get(name)
    if not active:
        print(f"Профиль '{name}' не найден.")
        return
    for u in users:
        if u['profile'] == active['id']:
            u['active'] = True
    print(f"Активен профиль: {active['name']}")
