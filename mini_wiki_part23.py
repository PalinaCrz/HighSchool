# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MiniWiki
def render_table(headers, rows):
    if not headers:
        return ""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row or []):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    lines = []
    fmt = " | ".join("{:<" + str(w) + "}" for w in col_widths)
    sep = " | ".join("-" * w for w in col_widths)
    lines.append(fmt.format(*headers))
    lines.append(sep)
    for row in rows:
        lines.append(fmt.format(*row))
    return "\n".join(lines)

def print_wiki_table(title, headers, rows):
    if not rows:
        print(f"[{title}] Нет данных.")
        return
    print(render_table(headers, rows))

# Пример использования (раскомментируйте для демонстрации):
# print_wiki_table("Статистика", ["Заголовок", "Значение"], [
#     ["Пользователей", 1],
#     ["Статей", len(wiki.get_all())],
#     ["Теги", len(set(tag for s in wiki.get_all() for tag in s.tags))],
# ])
