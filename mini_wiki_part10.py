# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MiniWiki
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "meta": {"version": 1, "exported_at": datetime.utcnow().isoformat()},
        "pages": {}
    }
    for page_id in pages:
        if page_id not in content or len(content[page_id]) == 0:
            continue
        raw = content[page_id]
        title = raw.get("title", "")
        body = raw.get("body", "")
        tags = set(raw.get("tags", []))
        history = raw.get("history", [])
        links = {k: v for k, v in raw.items() if k.startswith("_link_")}
        data["pages"][page_id] = {
            "title": title,
            "body": body,
            "tags": sorted(tags),
            "links": links,
            "history": history
        }
    return json.dumps(data, ensure_ascii=False)
