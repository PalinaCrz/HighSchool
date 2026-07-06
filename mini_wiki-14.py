# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MiniWiki
def generate_summary():
    lines = ["# MiniWiki Summary"]
    lines.append(f"- Pages: {len(pages)}")
    for p in pages[:3]:
        lines.append(f"  - {p['title']}: {' '.join(p.get('tags', []))}")
    total_links = sum(len(p.get("links", [])) for p in pages)
    lines.append(f"- Total internal links: {total_links}")
    return "\n".join(lines)

print(generate_summary())
