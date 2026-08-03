# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MiniWiki
def add_profiles():
    profiles = {
        "admin": {"pass": None, "name": "Администратор", "color": "#ff4d4f"},
        "user": {"pass": None, "name": "Пользователь", "color": "#1890ff"},
    }
    for name, p in profiles.items():
        if name not in app_data:
            app_data[name] = {
                "password": hashlib.md5(p["pass"].encode() if p["pass"] else b"empty").hexdigest(),
                "name": p["name"],
                "color": p["color"],
                "history": [],
            }

def get_profile():
    name = input("Введите имя профиля: ")
    if name in app_data:
        return app_data[name]
    print(f"Профиль '{name}' не найден.")
    return None

app_data["admin"]["password"] = hashlib.md5(b"admin").hexdigest()
