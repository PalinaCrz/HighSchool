# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MiniWiki
def migrate_to_v46():
    """Миграция: добавляем историю правок к каждой заметке."""
    global wiki
    if wiki.get("version") != "v45":
        wiki["version"] = "v46"
        for note in wiki.get("notes", []):
            if "history" not in note:
                note["history"] = []
    return wiki
