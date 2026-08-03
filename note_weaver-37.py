# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: NoteWeaver
import sys, os
sys.path.insert(0, os.path.dirname(__file__) if '__file__' in dir() else '.')
try:
    import note_weaver as nw
except ImportError:
    import note_weaver  # same-dir fallback

# ---- Unit-тесты NoteWeaver (без внешних зависимостей) -------------------

def test_note_crud():
    n = nw.Note("Заголовок", "Текст тела")
    assert n.title == "Заголовок" and n.body == "Текст тела"
    n2 = n.copy()
    n2.body = "Изменённый текст"
    assert n.body == "Текст тела"

def test_note_tags():
    n = nw.Note("Одежда", body="Пиджак")
    n.tag("офис"), n.tag("зима")
    tags = list(n.tags)
    assert "зимой" in tags and len(tags) == 2

def test_note_search():
    notes = [nw.Note(f"План {i}", body=f"Делать номер {i}") for i in range(5)]
    found = nw.search_notes(notes, "номер 3")
    assert any("3" in nb.body for nb in found) and len(found) == 1

def test_note_link():
    a = nw.Note("А", body="ссылка")
    b = nw.Note("Б", body="цель")
    a.link_to(b, "перейти к Б")
    assert any("Б" in nb.body for nb in a.links)

def test_daily_draft():
    d = nw.DailyDraft()
    d.title = "Черновик 1 янв"
    d.add_note(nw.Note("Привет", body="Тест"))
    assert len(d.notes) == 1 and d.notes[0].title == "Привет"

def test_theme():
    t = nw.Theme("Рабочий стол")
    notes = [nw.Note(f"Заметка {i}", body=f"Тема: {t.name}") for i in range(3)]
    t.add_notes(notes)
    assert len(t.notes) == 3 and all("Рабочий стол" in nb.body for nb in t.notes)

def test_search_across_themes():
    themes = [nw.Theme(f"Тема {i}") for i in range(2)]
    notes = [nw.Note(f"Поиск в теме", body=f"Ключ: тема") for _ in range(4)]
    nw.search_notes(notes, "ключ:")
