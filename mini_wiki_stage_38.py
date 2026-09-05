# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MiniWiki
def test_miniwiki_edge_cases():
    from miniwiki import MiniWiki
    wiki = MiniWiki()

    # Тест 1: Пустая строка как название
    wiki.add_note("", "Контент пустого заголовка")
    result = wiki.get_note("")
    assert result is not None
    assert result["content"] == "Контент пустого заголовка"
    assert result["title"] == ""

    # Тест 2: Заголовок с пробелами и спецсимволами
    wiki.add_note("Привет! Как дела?", "Привет! Как дела?")
    result = wiki.get_note("Привет! Как дела?")
    assert result is not None
    assert result["content"] == "Привет! Как дела?"

    # Тест 3: Заголовок с кириллицей и спецсимволами
    wiki.add_note("Привет мир! 🌍", "Привет мир! 🌍")
    result = wiki.get_note("Привет мир! 🌍")
    assert result is not None
    assert result["content"] == "Привет мир! 🌍"

    # Тест 4: Заголовок с длинным текстом
    long_text = "Длинный текст" * 100
    wiki.add_note(long_text, "Длинный текст")
    result = wiki.get_note("Длинный текст")
    assert result is not None
    assert result["content"] == long_text

    # Тест 5: Заголовок с кириллицей и спецсимволами
    wiki.add_note("Привет мир! 🌍", "Привет мир! 🌍")
    result = wiki.get_note("Привет мир! 🌍")
    assert result is not None
    assert result["content"] == "Привет мир! 🌍"

    # Тест 6: Тег с кириллицей и спецсимволами
    wiki.add_tag("Привет мир! 🌍", "Привет мир! 🌍")
    result = wiki.get_tag("Привет мир! 🌍")
    assert result is not None
    assert result["name"] == "Привет мир! 🌍"

    # Тест 7: Заголовок с кириллицей и спецсимволами
    wiki.add_note("Привет мир! 🌍", "Привет мир! 🌍")
    result = wiki.get_note("Привет мир! 🌍")
    assert result is not None
    assert result["content"] == "Привет мир! 🌍"

    # Тест 8: Заголовок с кириллицей и спецсимволами
    wiki.add_note("Привет мир! 🌍", "Привет мир! 🌍")
    result = wiki.get_note("Привет мир! 🌍")
    assert result is not None
    assert result["content"] == "Привет мир! 🌍"

    #
