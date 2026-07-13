# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MiniWiki
def add_tag(note_id, tag):
    """Add a tag to a note (create note if missing)."""
    notes = _load_notes()
    note = notes.get(note_id)
    if not note:
        note = {"id": note_id, "title": "", "body": "", "tags": [], "history": []}
        notes[note_id] = note
    tags = set(note["tags"])
    if tag.lower() not in {t.lower() for t in tags}:
        tags.add(tag)
        note["tags"] = sorted(tags)
        _save_notes(notes)

def remove_tag(note_id, tag):
    """Remove a tag from a note (delete note if empty)."""
    notes = _load_notes()
    note = notes.get(note_id)
    if not note:
        return False
    tags = {t.lower(): t for t in note["tags"]}
    removed = tag.lower() in tags
    if removed:
        del tags[removed]
        note["tags"] = sorted(tags.values())
        _save_notes(notes)
        if not note["title"] and not note["body"] and not note["tags"]:
            notes.pop(note_id, None)
    return removed
