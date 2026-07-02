# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MiniWiki
import json, os, sys
from pathlib import Path

def load_wiki_data(file_path: str) -> dict | None:
    try:
        with open(Path(file_path), 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Ошибка: JSON должен содержать объект корень.")
            return None
        # Проверка обязательных полей для валидности структуры
        required_keys = {'pages', 'tags'}
        missing = required_keys - set(data.keys())
        if missing:
            print(f"Ошибка: отсутствуют ключи {missing}.")
            return None
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке: {type(e).__name__}: {e}")
        return None

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    data = load_wiki_data("data.json")
    if data:
        print(f"Загружено страниц: {len(data.get('pages', []))}, тегов: {len(data.get('tags', []))}")
