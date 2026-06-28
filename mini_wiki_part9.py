# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MiniWiki
import json, base64, hashlib, uuid, time, os, sys, re, datetime as dt

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict): raise ValueError("JSON root must be an object")
        
        # Normalize and store notes
        for note_id, content in data.get('notes', {}).items():
            if not isinstance(content, dict): continue
            note = {
                'id': note_id,
                'title': content.get('title', ''),
                'content': content.get('content', ''),
                'tags': set(content.get('tags', [])),
                'links': [l.strip() for l in content.get('links', []) if l],
                'created_at': float(content.get('created_at', time.time())),
                'updated_at': float(time.time())
            }
            # Sanitize links (basic check)
            note['links'] = [link for link in note['links'] if len(link) > 0 and not link.startswith('#')]
            
        return data.get('notes', {}), data.get('history', []), data.get('settings', {})
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

# Example usage within the main script logic to initialize state
INITIAL_JSON = '{"notes": {"intro": {"title": "Welcome", "content": "# Hello World\n## Tags: [start]", "tags": ["start"], "links": [], "created_at": 1700000000.0, "updated_at": 1700000000.0}}, "history": [{"note_id": "intro", "action": "create", "timestamp": 1700000000.0}], "settings": {"theme": "light"}}'
notes_db, history_log, settings = load_initial_data(INITIAL_JSON)
