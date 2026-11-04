# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: MiniWiki
def export_report(path):
    notes = list(NOTES.values()) if 'NOTES' in globals() else []
    lines = []
    lines.append("=== MiniWiki Отчёт ===")
    lines.append(f"Заметок: {len(notes)}")
    lines.append(f"Теги: {len(TAGS)}")
    lines.append(f"Ссылок: {len(LINKS)}")
    for name, note in notes:
        lines.append(f"- {name}: {note.get('text', '')[:50]}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path
