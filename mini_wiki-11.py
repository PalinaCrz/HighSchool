# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MiniWiki
import json, os

DATA_FILE = "wiki_data.json"

def save_state(state):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"notes": {}, "history": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"notes": {}, "history": []}

def get_state():
    state = load_state()
    save_state(state)
    return state
