# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MiniWiki
def sort_notes(notes, key='date'):
    if key == 'date':
        return sorted(notes, key=lambda n: n.get('created_at', 0), reverse=True)
    elif key == 'priority':
        return sorted(notes, key=lambda n: n.get('priority', 5))
    else:
        return sorted(notes, key=lambda n: n.get('title', ''))
