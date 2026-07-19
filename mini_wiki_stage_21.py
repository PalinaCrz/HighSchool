# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MiniWiki
import datetime

class Reminder:
    def __init__(self, title, date_str):
        self.title = title
        self.date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    def is_due(self, now=None):
        if now is None:
            now = datetime.datetime.now()
        return now >= self.date

    def __repr__(self):
        status = "due" if self.is_due() else "pending"
        return f"<Reminder '{self.title}' [{status}]>"


class ReminderManager:
    def __init__(self, storage_path="reminders.txt"):
        self.storage_path = storage_path
        self.reminders = []
        self._load(storage_path)

    def _load(self, path):
        try:
            with open(path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    title, date_str = line.split("||", 1)
                    self.reminders.append(Reminder(title.strip(), date_str.strip()))
        except FileNotFoundError:
            pass

    def add(self, title, date_str):
        reminder = Reminder(title, date_str)
        if not any(r.title == title for r in self.reminders):
            self.reminders.append(reminder)
            with open(self.storage_path, "a") as f:
                f.write(f"{title}||{date_str}\n")

    def check_due(self):
        now = datetime.datetime.now()
        due = [r for r in self.reminders if r.is_due(now)]
        return due
