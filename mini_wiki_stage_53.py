# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: MiniWiki
def import_from_text(path, store):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(" | ")
            if len(parts) < 2:
                continue
            title = parts[0].strip()
            content = " | ".join(parts[1:]).strip()
            tags = []
            if "|" in title:
                title, tag_str = title.split("|", 1)
                title = title.strip()
                tags = [t.strip() for t in tag_str.split(",") if t.strip()]
            store.add_note(title, content, tags)
    print(f"Импортировано из {path}")
