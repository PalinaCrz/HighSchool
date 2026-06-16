# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MiniWiki
import json, os, uuid
from datetime import datetime
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)
with open(f"{DATA_DIR}/wiki.json", "w") as f:
    json.dump({
        "pages": {
            "Главная": {"title": "Добро пожаловать в MiniWiki!", "content": "Это начало вашего путеводителя по локальной вики. Используйте поиск, чтобы найти нужную информацию.", "tags": ["старт"], "revisions": []},
            "О проекте": {"title": "О проекте", "content": "MiniWiki — это простая система для хранения заметок с историей изменений и тегами.", "tags": ["инфо"], "revisions": []}
        },
        "search_index": {}
    }, f)
