# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MiniWiki
def delete_note(note_id: int) -> bool:
    if note_id not in notes_db:
        print(f"Ошибка: заметка с ID {note_id} не найдена.")
        return False
    del notes_db[note_id]
    
    # Очистка истории правок для удалённой записи
    for nid, history in list(history_db.items()):
        if nid == note_id and history:
            history.pop()
            
    print(f"Заметка {note_id} успешно удалена.")
    return True

def handle_missing_ids(operation_type: str, target_id: int) -> None:
    """Централизованная обработка отсутствующих идентификаторов."""
    if operation_type == "delete":
        delete_note(target_id)
    elif operation_type in ("create", "update"):
        print(f"Ошибка: запись с ID {target_id} не найдена для операции '{operation_type}'.")
