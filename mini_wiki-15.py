# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MiniWiki
import datetime


def weekly_stats(entries, days=7):
    """Return dict {date_str: list[entry]} for the last `days` weeks."""
    now = datetime.datetime.now(datetime.timezone.utc)
    stats = {}
    cutoff = now - datetime.timedelta(weeks=days)
    for e in entries:
        created = _ts_to_dt(e.get("created", 0), "UTC")
        if created < cutoff:
            continue
        week_key = created.isocalendar()[:2]
        stats.setdefault(f"{week_key[0]}-W{week_key[1]:02d}", []).append(e)
    return stats
