# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MiniWiki
def show_record(record):
    if not record:
        return "Запись не найдена."
    title = record.get("title", "(нет заголовка)")
    body = record.get("body", "")
    tags = record.get("tags", [])
    date_str = record.get("date", "")
    edit_count = record.get("edit_count", 0)
    lines = [f"Запись: {title}", f"Тело: {body[:200] if body else '(пусто)'}", f"Теги: {', '.join(tags)}", f"Дата: {date_str}", f"Правок: {edit_count}"]
    return "\n".join(lines)
