# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: NoteWeaver
DEFAULT_CONFIG = {
    "theme": "light",
    "max_notes_per_topic": 50,
    "search_algorithm": "naive",
    "diary_enabled": True,
    "diary_prefix": "[Daily]",
}


class AppConfig:
    """Simple configuration manager for NoteWeaver."""

    def __init__(self):
        self._config = dict(DEFAULT_CONFIG)

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        if key not in DEFAULT_CONFIG:
            raise ValueError(f"Unknown config key: {key}")
        self._config[key] = value

    def to_dict(self):
        return dict(DEFAULT_CONFIG, **self._config)


# Example usage:
cfg = AppConfig()
print("Current theme:", cfg.get("theme"))
cfg.set("diary_prefix", "[Notes]")
print("Updated prefix:", cfg.get("diary_prefix"))
