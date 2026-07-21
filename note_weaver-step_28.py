# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: NoteWeaver
def project_metrics():
    """Compact metrics block for NoteWeaver."""
    import os, re, datetime

    base = os.path.dirname(os.path.abspath(__file__))
    notes_dir = os.path.join(base, "notes")
    drafts_dir = os.path.join(notes_dir, "drafts")
    tags_dir = os.path.join(notes_dir, "tags")

    total_notes = 0
    today = datetime.date.today().isoformat()
    draft_count = 0
    tag_count = 0
    daily_count = 0
    note_sizes = []
    link_count = 0
    unique_links = set()

    for fname in os.listdir(notes_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(notes_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        total_notes += 1
        note_sizes.append(len(content))
        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        link_count += len(links)
        unique_links.update(links)

    for fname in os.listdir(drafts_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(drafts_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        draft_count += 1

    for fname in os.listdir(tags_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(tags_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        tag_count += 1

    for fname in os.listdir(notes_dir):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(notes_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if today in content:
            daily_count += 1

    avg_size = sum(note_sizes) / len(note_sizes) if note_sizes else 0

    print(f"NoteWeaver Metrics Report:")
    print(f"  Total notes:       {total_notes}")
    print(f"  Drafts (today):    {draft_count}")
    print(f"  Tags defined:      {tag_count}")
    print(f"  Daily entries:     {daily_count}")
    print(f"  Internal links:    {link_count} ({len(unique_links)} unique)")
    print(f"  Avg note size:     {avg_size:.0f} chars")

if __name__ == "__main__":
    project_metrics()
