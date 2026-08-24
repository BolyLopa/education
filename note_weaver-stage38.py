# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: NoteWeaver
def test_edge_cases():
    """Тесты для пограничных случаев и ошибок."""
    # Тест: пустой текст
    assert NoteWeaver().search("") == []
    assert NoteWeaver().search(None) == []
    # Тест: поиск с пробелами
    assert NoteWeaver().search("   ") == []
    # Тест: добавление и удаление заметки
    note = NoteWeaver().add_note("test", "content")
    assert note.id is not None
    NoteWeaver().remove_note(note.id)
    assert NoteWeaver().search("test") == []
    # Тест: тема без заметок
    theme = NoteWeaver().add_theme("empty_theme")
    assert theme.id is not None
    assert NoteWeaver().get_theme("empty_theme") is None
    # Тест: удаление темы без заметок
    NoteWeaver().remove_theme(theme.id)
    assert NoteWeaver().get_theme(theme.id) is None
    # Тест: ежедневный черновик
    assert NoteWeaver().get_daily_draft() is None
    NoteWeaver().save_daily_draft("test draft")
    assert NoteWeaver().get_daily_draft() == "test draft"
    NoteWeaver().save_daily_draft("new draft")
    assert NoteWeaver().get_daily_draft() == "new draft"
    # Тест: связь с несуществующей заметкой
    note = NoteWeaver().add_note("linked", "content")
    NoteWeaver().link_note(note.id, "nonexistent")
    assert NoteWeaver().search("nonexistent") == []
    NoteWeaver().remove_note(note.id)
    # Тест: валидация email
    assert NoteWeaver().validate_email("") is False
    assert NoteWeaver().validate_email(" ") is False
    assert NoteWeaver().validate_email("user") is False
    assert NoteWeaver().validate_email("user@") is False
    assert NoteWeaver().validate_email("@domain.com") is False
    assert NoteWeaver().validate_email("user@domain.com") is True
    # Тест: валидация URL
    assert NoteWeaver().validate_url("") is False
    assert NoteWeaver().validate_url(" ") is False
    assert NoteWeaver().validate_url("user") is False
    assert NoteWeaver().validate_url("http://example.com") is True
    assert NoteWeaver().validate_url("https://example.com/path?q=1") is True
    # Тест: форматирование даты
    assert NoteWeaver().format_date("2024-01-01") == "2024-01-01"
    assert NoteWeaver().format_date("2024-01-15") == "2024-01-15"
    # Тест: поиск с несколькими словами
    note1 = NoteWeaver().add_note("multi word test", "content1")
    note2 = NoteWeaver().add_note("another test", "content2")
    results = NoteWeaver().search("test")
    assert len(results) == 2
    # Тест: удаление всех заметок
    note = NoteWeaver().add_note("to remove", "content")
    NoteWeaver().remove_note(note.id)
    assert NoteWeaver().search("to remove") == []
