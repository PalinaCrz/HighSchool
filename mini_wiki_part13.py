# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MiniWiki
def search_notes(query, fields=None):
    if not query: return []
    q = query.lower()
    results = []
    for note in notes.values():
        match_fields = 0
        total_fields = len(fields) if fields else 4
        for f_name, f_val in [(f"content", note["text"]), (f"title", note["title"])] + \
                              (([(f"tag", t), (f"user", u)] for t, u in zip(note.get("tags", []), [note.get("user", "")])) if fields else []):
            if f_name not in fields: continue
            if q in str(f_val).lower(): match_fields += 1
        if total_fields == 0 or match_fields > 0: results.append((match_fields, note))
    return sorted(results, key=lambda x: -x[0])
