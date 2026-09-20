# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MiniWiki
import re

def extract_tags(text):
    """Extract tags from text wrapped in square brackets and return them as a list of stripped strings."""
    return [tag.strip() for tag in re.findall(r'\[([^\]]+)\]', text)]

def extract_links(text):
    """Extract links from text wrapped in double square brackets and return them as a list of (target, title) tuples."""
    return [(target, title) for target, title in re.findall(r'\[\[([^\]]+)\]\]', text)]

def count_words(text):
    """Count the number of words in a text string."""
    return len(text.split())

def truncate_text(text, max_length=200):
    """Truncate text to a maximum length, adding '...' if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'

def parse_page_content(content):
    """Parse page content to extract title, body, tags, and links. Returns a dictionary."""
    title = ''
    body = ''
    tags = []
    links = []
    title_end = content.find('\n')
    if title_end != -1:
        title = content[:title_end]
        body = content[title_end + 1:]
    tags = extract_tags(body)
    links = extract_links(body)
    return {'title': title, 'body': body, 'tags': tags, 'links': links}
