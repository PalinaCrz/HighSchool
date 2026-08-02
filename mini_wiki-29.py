# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MiniWiki
class AppSettings:
    def __init__(self):
        self.settings = {
            'app_name': 'MiniWiki',
            'max_history_versions': 10,
            'default_tags': [],
            'search_algorithm': 'linear',
            'case_sensitive_search': False,
            'enable_auto_save': True,
            'auto_save_interval_seconds': 300,
        }

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        if key in self.settings:
            self.settings[key] = value
        else:
            raise KeyError(f"Unknown setting: {key}")
