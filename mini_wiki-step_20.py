# === Stage 20: Добавь восстановление записей из архива ===
# Project: MiniWiki
def recover_archived_notes():
    """Восстанавливает записи из архива в основную базу."""
    archive = {}
    for key, value in ARCHIVE.items():
        if isinstance(value, list):
            archive[key] = value[0]
        else:
            archive[key] = value

    main_db["notes"] = archive.get("main_notes", {})
    main_db["links"] = archive.get("main_links", {})
    main_db["tags"] = archive.get("main_tags", [])
    main_db["history"] = archive.get("main_history", [])


recover_archived_notes()
