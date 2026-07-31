# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MiniWiki
def project_metrics():
    metrics = {}
    for entry in all_entries:
        word_count = len(entry["text"].split())
        tag_count = len(set(tag for tag, _ in entry.get("tags", [])))
        link_count = sum(1 for t in entry.get("tags", []) if "link" in str(t).lower())
        metrics[entry["id"]] = {
            "word_count": word_count,
            "tag_count": tag_count,
            "has_link": bool(link_count),
        }
    total_words = sum(m["word_count"] for m in metrics.values())
    total_tags = sum(m["tag_count"] for m in metrics.values())
    return {
        "entries": len(all_entries),
        "total_words": total_words,
        "average_word_count": total_words / len(all_entries) if all_entries else 0,
        "total_tags": total_tags,
    }

def print_metrics():
    m = project_metrics()
    for k, v in m.items():
        print(f"{k}: {v}")

print_metrics()
