# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MiniWiki
def undo_last_action(history):
    """Откатывает последнее действие в истории. Возвращает True если откат успешен, иначе False."""
    if not history:
        return False
    last = history[-1]
    if last['type'] == 'edit':
        history.pop()
        history.append({'type': 'edit', 'title': last['title'], 'content': last['before']})
        return True
    elif last['type'] == 'delete':
        history.pop()
        history.append({'type': 'edit', 'title': last['title'], 'content': last['before']})
        return True
    elif last['type'] == 'undo':
        history.pop()
        return True
    return False
