# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MiniWiki
def demo_commands():
    """Демо-команды для ручного тестирования MiniWiki."""
    # Создаём несколько заметок с тегами
    wiki = Wiki()
    
    note1 = Note("Первая заметка", "Привет, это первая запись в вики.", tags=["введение"])
    note2 = Note("Вторая заметка", "Содержимое второй заметки.", tags=["кодинг"])
    note3 = Note("Третья заметка", "Заметка с ссылками: см. [[закон Ома]] для электричества.", tags=["физика", "ссылки"])
    note4 = Note("Четвёртая заметка", "Ещё одна запись.", tags=["введение", "кодинг"])

    wiki.add_note(note1)
    wiki.add_note(note2)
    wiki.add_note(note3)
    wiki.add_note(note4)

    # Тестирование поиска
    print("=== Поиск ===")
    results = wiki.search_notes("заметка")
    for r in results:
        print(f"  {r.title}")

    print("\n=== Теги ===")
    tags = wiki.get_tags()
    for tag_name, count in sorted(tags.items()):
        print(f"  {tag_name}: {count} заметок")

    # Тестирование истории правок
    print("\n=== История ===")
    history = wiki.get_history()
    if history:
        for note_title, changes in history.items():
            print(f"\n  Заметка: {note_title}")
            for change in changes:
                print(f"    Изменено: {change.old_value} -> {change.new_value} (автор: {change.author})")

    # Тестирование получения заметки по ID
    print("\n=== Получить по ID ===")
    note = wiki.get_note_by_id(1)
    if note:
        print(f"  ID={note.id}, Заголовок={note.title}, Содержание={note.content}")

    print("\nДемо-тестирование завершено.")


if __name__ == "__main__":
    demo_commands()
