# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: NoteWeaver
class NoteModel:
    def __init__(self, title: str, content: str, theme: str = "", date: str = ""):
        self.title = title.strip() if title else ""
        self.content = content.strip() if content else ""
        self.theme = theme.strip() if theme else ""
        self.date = date or self._get_today()

    def _get_today(self) -> str:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")

    @property
    def is_valid(self) -> bool:
        return bool(self.title and len(self.title) <= 100 and self.content)

class InputValidator:
    MAX_TITLE_LEN = 100
    MIN_CONTENT_LEN = 1

    @staticmethod
    def validate_title(title: str) -> tuple[bool, str]:
        if not title:
            return False, "Заголовок не может быть пустым."
        if len(title) > InputValidator.MAX_TITLE_LEN:
            return False, f"Заголовок слишком длинный (макс {InputValidator.MAX_TITLE_LEN} символов)."
        return True, ""

    @staticmethod
    def validate_content(content: str) -> tuple[bool, str]:
        if not content or len(content.strip()) < InputValidator.MIN_CONTENT_LEN:
            return False, "Содержание не может быть пустым."
        return True, ""

    @staticmethod
    def validate_theme(theme: str) -> tuple[bool, str]:
        if theme and (len(theme) > 50 or not theme.strip()):
            return False, "Тема должна быть непустой и не длиннее 50 символов."
        return True, ""

    @staticmethod
    def validate_date(date: str) -> tuple[bool, str]:
        if date and len(date) > 10:
            return False, "Дата должна быть в формате YYYY-MM-DD или пустой."
        return True, ""
