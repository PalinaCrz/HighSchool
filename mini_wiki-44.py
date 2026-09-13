# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MiniWiki
def backup_file(path, backup_dir=None):
    """Создаёт резервную копию файла данных в той же папке (backup_YYYYMMDD_HHMMSS.dat) или в указанной директории."""
    if backup_dir is None:
        backup_dir = os.path.dirname(os.path.abspath(path))
    os.makedirs(backup_dir, exist_ok=True)
    now = datetime.now()
    name = f"backup_{now.strftime('%Y%m%d_%H%M%S')}.dat"
    dest = os.path.join(backup_dir, name)
    with open(path, "rb") as src, open(dest, "wb") as dst:
        dst.write(src.read())
    return dest
