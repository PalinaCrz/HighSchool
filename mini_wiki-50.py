# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: MiniWiki
def format_message(text: str) -> str:
    """Очистить и отформатировать сообщение для вывода."""
    if not text:
        return ""
    cleaned = text.strip().replace("  ", " ").replace("\n\n", "\n")
    return cleaned


def format_title(title: str) -> str:
    """Форматировать заголовок: заглавные буквы и дефисы."""
    if not title:
        return ""
    return " ".join(title.split())


def parse_tags(text: str) -> list[str]:
    """Извлечь теги из текста в квадратных скобках."""
    tags = []
    for match in re.finditer(r"\[([^]]+)\]", text):
        tag = match.group(1).strip()
        if tag:
            tags.append(tag)
    return tags
