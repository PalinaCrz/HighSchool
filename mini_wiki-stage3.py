# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MiniWiki
class MiniWiki:
    def __init__(self):
        self._notes = {}
        self._history = []

    def add_note(self, title: str, content: str) -> None:
        if not title.strip(): raise ValueError("Title cannot be empty")
        old_content = self._notes.get(title, "")
        new_entry = {"title": title, "content": content, "timestamp": time.time(), "prev_hash": hash(old_content)}
        self._history.append(new_entry)
        if not old_content: self._notes[title] = content
        else:
            current_hash = hash(content)
            for entry in reversed(self._history):
                if entry["title"] == title and entry.get("prev_hash") is None: break
                elif entry["content"] == old_content and entry != new_entry:
                    self._notes[title] = content
                    return
        self._notes[title] = content

    def get_note(self, title: str) -> str | None:
        return self._notes.get(title)

    def list_notes(self) -> list[tuple[str, int]]:
        return [(t, len(c)) for t, c in sorted(self._notes.items())]
