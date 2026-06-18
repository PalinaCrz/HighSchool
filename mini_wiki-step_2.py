# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MiniWiki
class ValidationError(Exception): pass

def validate_input(text: str) -> tuple[str, bool]:
    if not text or len(text.strip()) > 1024:
        raise ValidationError("Текст должен быть непустым и не превышать 1024 символов.")
    return text.strip(), True

def parse_tags(tag_string: str) -> list[str]:
    tags = [t.strip() for t in tag_string.split(',') if t.strip()]
    invalid_chars = set('<>"/\|?*')
    for tag in tags:
        if any(c in tag for c in invalid_chars):
            raise ValidationError(f"В теге '{tag}' недопустимые символы.")
        if len(tag) > 20 or not tag.isalnum() and not all(c.isspace() or (c.isalpha() and c != ' ') for c in tag):
            raise ValidationError(f"Некорректный формат тега: {tag}")
    return tags

def sanitize_link(link_text: str, url: str) -> tuple[str, str]:
    if not link_text.strip():
        raise ValidationError("Текст ссылки не может быть пустым.")
    if len(url) > 2048 or not (url.startswith('http://') or url.startswith('https://')):
        raise ValidationError(f"Некорректный URL или он слишком длинный ({len(url)} символов).")
    return link_text.strip(), url
