# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MiniWiki
def restore_backup(backup_file, wiki_data):
    """Восстанавливает данные из резервной копии JSON."""
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup = json.load(f)
        wiki_data['notes'] = backup.get('notes', {})
        wiki_data['history'] = backup.get('history', [])
        wiki_data['tags'] = backup.get('tags', {})
        wiki_data['links'] = backup.get('links', {})
        wiki_data['users'] = backup.get('users', {})
        wiki_data['settings'] = backup.get('settings', {})
        print(f"✅ Резервная копия восстановлена: {backup_file}")
        return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Ошибка восстановления: {e}")
        return False
