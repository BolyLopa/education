# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: NoteWeaver
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "version": 1,
        "timestamp": datetime.utcnow().isoformat(),
        "notes": notes_list,
        "themes": themes_dict,
        "connections": connections_list,
        "drafts": drafts_dict
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
