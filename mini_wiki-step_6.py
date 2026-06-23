# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MiniWiki
def filter_notes(query=None, status=None, category=None, tags=None):
    if query:
        q = query.lower()
        notes = [n for n in notes if any(q in x.lower() for x in (n.get('title', ''), n.get('body', '')))]
    else:
        notes = list(notes)
    if status is not None:
        notes = [n for n in notes if n.get('status') == status]
    if category:
        notes = [n for n in notes if n.get('category') == category]
    if tags:
        t_list = [t.lower() for t in (tags if isinstance(tags, list) else [tags])]
        notes = [n for n in notes if any(t in n.get('tags', []) for t in t_list)]
    return notes
