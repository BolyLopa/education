# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: NoteWeaver
class NoteProfile:
    def __init__(self, name, color='#3498db', default_font_size=14):
        self.name = name
        self.color = color
        self.default_font_size = default_font_size

    def to_dict(self):
        return {'name': self.name, 'color': self.color, 'default_font_size': self.default_font_size}

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['color'], d['default_font_size'])


class ProfileManager:
    _profiles = {}
    _current_profile_name = None

    @classmethod
    def get_profiles(cls):
        if not cls._profiles:
            cls._profiles['Default'] = NoteProfile('Default', '#3498db', 14)
        return cls._profiles

    @classmethod
    def set_current_profile(cls, name):
        profiles = cls.get_profiles()
        if name in profiles:
            cls._current_profile_name = name
            return profiles[name]
        raise ValueError(f"Профиль '{name}' не найден")

    @classmethod
    def get_current_profile(cls):
        if not cls._current_profile_name:
            profiles = cls.get_profiles()
            cls._current_profile_name = list(profiles.keys())[0]
        return cls._profiles[cls._current_profile_name]

    @classmethod
    def add_profile(cls, name, color='#e74c3c', font_size=14):
        if not name or name.strip() == '':
            raise ValueError("Имя профиля не может быть пустым")
        profiles = cls.get_profiles()
        if name in profiles:
            raise ValueError(f"Профиль '{name}' уже существует")
        profiles[name] = NoteProfile(name, color, font_size)
        return profiles[name]

    @classmethod
    def delete_profile(cls, name):
        if not name or name.strip() == '':
            raise ValueError("Имя профиля не может быть пустым")
        profiles = cls.get_profiles()
        if name in profiles:
            del profiles[name]
            if cls._current_profile_name == name:
                remaining = list(profiles.keys())
                if remaining:
                    cls._current_profile_name = remaining[0]
            return True
        return False

    @classmethod
    def save_profiles(cls, file_path):
        import json
        profiles = cls.get_profiles()
        data = {name: p.to_dict() for name, p in profiles.items()}
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load_profiles(cls, file_path):
        import json
        if not os.path.exists(file_path):
            return
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for name, info in data.items():
            cls._profiles[name] = NoteProfile.from_dict(info)


import os
