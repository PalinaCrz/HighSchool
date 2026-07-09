# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MiniWiki
def monthly_stats():
    """Рассчитывает количество заметок по месяцам за текущий год."""
    stats = {}
    for note_id, note in notes.items():
        if note.get("date"):
            try:
                month_key = f"{note['date'][:4]}-{note['date'][5:7]}"
            except (IndexError, TypeError):
                continue
            stats[month_key] = stats.get(month_key, 0) + 1
    return dict(sorted(stats.items()))

print("=== Месячная статистика ===")
for month, count in monthly_stats().items():
    print(f"{month}: {count} заметок")
