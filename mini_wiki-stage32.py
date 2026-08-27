# === Stage 32: Добавь журнал действий пользователя ===
# Project: MiniWiki
class ActionLog:
    def __init__(self):
        self.entries = []
    def log(self, action: str, page: str, user: str):
        self.entries.append({"action": action, "page": page, "user": user, "time": datetime.now().isoformat()})

wiki = ActionLog()
wiki.log("create", "Main", "system")
print(wiki.entries)
