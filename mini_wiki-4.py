# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MiniWiki
def edit_note(note_id: int, new_content: dict) -> bool:
    if note_id not in notes:
        print(f"Ошибка: заметка с ID {note_id} не найдена.")
        return False
    
    existing = notes[note_id]
    
    # Сохраняем историю правок перед изменением
    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "author": current_user,
        "content_snapshot": existing["content"],
        "tags_snapshot": list(existing.get("tags", []))
    }
    
    if not history:
        history = []
    history.append(history_entry)
    
    # Обновляем контент и теги
    existing["content"] = new_content.get("text", existing["content"])
    existing["tags"] = list(new_content.get("tags", existing.get("tags", [])))
    
    print(f"Заметка {note_id} успешно обновлена.")
    return True
