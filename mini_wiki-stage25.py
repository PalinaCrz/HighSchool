# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MiniWiki
def parse_date(text):
    """Парсит строку даты в формат 'YYYY-MM-DD' или без года."""
    text = text.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y"):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    raise ValueError(f"Некорректная дата: '{text}'")

def format_date(dt):
    """Форматирует дату в 'YYYY-MM-DD'. Возвращает None если dt не datetime."""
    if not isinstance(dt, datetime):
        return None
    return dt.strftime("%Y-%m-%d")
