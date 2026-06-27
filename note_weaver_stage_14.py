# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: NoteWeaver
def generate_summary():
    from datetime import date, timedelta
    today = date.today()
    summary_lines = ["=== NoteWeaver Daily Summary ===", f"Date: {today.strftime('%Y-%m-%d')}", ""]
    
    # Count notes by topic (simplified example)
    topics_count = {}
    for note in all_notes:  # Assuming 'all_notes' is your global list of Note objects
        if note.topic:
            topics_count[note.topic] = topics_count.get(note.topic, 0) + 1
    
    summary_lines.append(f"Total notes: {len(all_notes)}")
    summary_lines.append("Top topics:")
    
    # Sort and show top 5 topics
    sorted_topics = sorted(topics_count.items(), key=lambda x: x[1], reverse=True)[:5]
    for topic, count in sorted_topics:
        summary_lines.append(f"  - {topic}: {count} notes")
    
    # Check daily drafts (assuming 'daily_drafts' dict exists)
    draft_date = today.strftime('%Y-%m-%d')
    if draft_date in daily_drafts and daily_drafts[draft_date]:
        summary_lines.append(f"Daily draft for {draft_date}: '{daily_drafts[draft_date]}'")
    else:
        summary_lines.append("No new daily draft created today.")
    
    # Search stats (example)
    search_queries = get_search_history()  # Assume this function exists or is empty list
    if search_queries:
        summary_lines.append(f"Recent searches ({len(search_queries)}): {', '.join(search_queries[-3:])}")
    else:
        summary_lines.append("No recent searches.")
    
    print("\n".join(summary_lines))
