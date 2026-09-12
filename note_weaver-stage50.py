# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: NoteWeaver
def polish_note_display(note: Note) -> str:
    """Return a nicely formatted note ready for console output."""
    lines = [
        f"--- {note.title or 'Untitled'} (#{note.id}) ---",
        f"  Created: {note.created_at}",
    ]
    if note.updated_at:
        lines.append(f"  Updated: {note.updated_at}")
    if note.tags:
        lines.append(f"  Tags:   {', '.join(note.tags)}")
    if note.theme:
        lines.append(f"  Theme:  {note.theme}")
    if note.status:
        lines.append(f"  Status: {note.status.value}")
    lines.append(f"  Body:   {note.body}")
    if note.links:
        lines.append(f"  Links:  {', '.join(note.links)}")
    if note.links_to:
        lines.append(f"  Linked to: {', '.join(note.links_to)}")
    return "\n".join(lines)
