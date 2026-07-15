# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MiniWiki
def archive_note(note_id):
    """Archive a note by moving it to the archive section."""
    notes = _read_notes()
    if note_id not in notes:
        print(f"Note {note_id} not found.")
        return
    archived = notes.pop(note_id)
    archived["archived"] = True
    archives.append(archived)
    _write_notes()
    print(f"Note {note_id} archived successfully.")

def unarchive_note(note_id):
    """Restore an archived note."""
    if not archives:
        return None
    for i, a in enumerate(archives):
        if a["id"] == note_id:
            notes[a["id"]] = {**a, "archived": False}
            del archives[i]
            _write_notes()
            print(f"Note {note_id} restored.")
            return notes[note_id]
    print("Archived note not found.")
    return None

def list_archives():
    """Display all archived notes."""
    if not archives:
        print("No archived notes.")
        return
    for i, a in enumerate(archives):
        print(f"[{i+1}] {a['title']} (archived on {a.get('date', 'unknown')})")

def search_archives(query=""):
    """Search within archived notes."""
    if not archives:
        print("No archived notes to search.")
        return []
    results = [a for a in archives if query.lower() in (a["title"] + " " + a.get("body", "")).lower()]
    return results

def show_archive_stats():
    """Show count of archived vs active notes."""
    total_archived = len(archives) if archives else 0
    print(f"Active notes: {len(notes)}, Archived: {total_archived}")
