# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: MiniWiki
from datetime import datetime

class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity, entity_name, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "entity": entity,
            "entity_name": entity_name,
            "details": details,
        }
        self.entries.append(entry)
