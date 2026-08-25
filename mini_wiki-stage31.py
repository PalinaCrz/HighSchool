# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MiniWiki
class ProfileManager:
    def __init__(self):
        self.profiles = {
            "user": {"name": "User", "theme": "light"},
            "admin": {"name": "Admin", "theme": "dark"},
        }
        self.active_profile = "user"

    def set_profile(self, name, name_display, theme):
        self.profiles[name] = {"name": name_display, "theme": theme}
        self.active_profile = name

    def show_profile_menu(self):
        print("\n=== Переключение профиля ===")
        for name, info in self.profiles.items():
            marker = " (активен)" if name == self.active_profile else ""
            print(f"[{name}] {info['name']} — тема: {info['theme']}{marker}")
        print("Введите имя профиля для переключения (или 'q' для выхода):")

    def switch_profile(self, input_name):
        if input_name.lower() == "q":
            return False
        if input_name in self.profiles:
            self.active_profile = input_name
            print(f"\nПереключено на профиль: {self.profiles[input_name]['name']}")
            return True
        else:
            print("Профиль не найден.")
            return False
