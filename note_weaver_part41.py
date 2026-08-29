# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: NoteWeaver
def dry_run_mode(operations: list[dict]) -> list[dict]:
    """Simulate data mutations without persisting them.

    Args:
        operations: list of dicts with keys 'action', 'target', 'payload'.

    Returns:
        list of dicts describing what would have happened.
    """
    results = []
    for op in operations:
        results.append({
            'action': op.get('action', 'unknown'),
            'target': op.get('target', 'unknown'),
            'payload': op.get('payload', {}),
            'status': 'dry-run',
        })
    return results
