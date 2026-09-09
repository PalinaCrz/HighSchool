# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MiniWiki
# --- Dry-run mode ---
def dry_run():
    """Return a function that simulates mutating operations without changing state."""
    state = {
        'notes': {},
        'links': [],
        'tags': [],
        'history': [],
    }
    def _add_note(title, body):
        state['notes'][title] = body
    def _add_link(text, url):
        state['links'].append({'text': text, 'url': url})
    def _add_tag(text):
        state['tags'].append(text)
    def _edit_note(title, body):
        state['history'].append({'action': 'edit', 'title': title, 'body': body})
        state['notes'][title] = body
    def _delete_note(title):
        state['history'].append({'action': 'delete', 'title': title})
        del state['notes'][title]
    return _add_note, _add_link, _add_tag, _edit_note, _delete_note
