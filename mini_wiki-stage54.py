# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: MiniWiki
#miniwiki
# Этап 54: Режим избранных записей и быстрый доступ к ним
# 1) Помечаем заметку как избранную (добавляем/обновляем метку)
def favorite_note(title, enabled=True):
    with open("notes.txt", "a") as f:
        f.write(f"#FAV: {title} {str(enabled).lower()}\n")
# 2) Быстрый доступ: вывод списка избранных из начала файла
def list_favorites():
    favorites = []
    with open("notes.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#FAV:"):
                parts = line.split(" #FAV:", 1)[1].split()
                title = parts[0]
                enabled = parts[1].lower() == "true"
                favorites.append((title, enabled))
    if not favorites:
        print("Избранных записей пока нет. Пометьте заметку: favorite_note('Название')")
    else:
        print("Избранные записи:")
        for title, enabled in favorites:
            marker = "*" if enabled else "-"
            print(f"  [{marker}] {title}")
# 3) Переключение избранного: отмечает/снимает метку и перемещает в начало
def toggle_favorite(title):
    lines = []
    with open("notes.txt", "r") as f:
        for line in f:
            if line.startswith("#FAV:"):
                parts = line.split(" #FAV:", 1)[1].split()
                current = parts[1].lower() == "true"
                if parts[0] == title:
                    lines.append(f"#FAV: {title} {str(not current).lower()}\n")
                else:
                    lines.append(line)
    with open("notes.txt", "w") as f:
        f.writelines(lines)
    if title in [p.split(" #FAV:", 1)[0] for p in lines]:
        lines.insert(0, f"#FAV: {title} true\n")
        with open("notes.txt", "w") as f:
            f.writelines(lines)
    print(f"Заметка '{title}' обновлена в списке избранного.")
