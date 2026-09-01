# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MiniWiki
def check_integrity_and_repair(data):
    errors = []
    for key in data:
        if not isinstance(data[key], dict):
            errors.append(f"Invalid page structure for '{key}'")
            continue
        page = data[key]
        if 'title' not in page or not page['title']:
            errors.append(f"Empty title for page '{key}'")
            page['title'] = key
        if 'content' not in page or not page['content']:
            errors.append(f"Empty content for page '{key}'")
            page['content'] = ''
        if 'tags' not in page:
            page['tags'] = []
        if 'history' not in page:
            page['history'] = []
        if 'revisions' not in page:
            page['revisions'] = []
        if 'created' not in page:
            page['created'] = None
        if 'last_modified' not in page:
            page['last_modified'] = None
        if 'links' not in page:
            page['links'] = []
        if 'revisions' not in page:
            page['revisions'] = []
        for revision in page['revisions']:
            if 'content' not in revision or not revision['content']:
                errors.append(f"Empty revision content for page '{key}'")
                revision['content'] = ''
            if 'timestamp' not in revision:
                revision['timestamp'] = None
            if 'author' not in revision:
                revision['author'] = None
        for link in page['links']:
            if 'url' not in link or not link['url']:
                errors.append(f"Invalid link for page '{key}'")
                link['url'] = ''
    return errors
