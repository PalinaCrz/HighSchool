# === Stage 17: Добавь группировку записей по категориям ===
# Project: MiniWiki
def categorize_entries(entries):
    cats = {}
    for e in entries:
        cat = e.get('category', 'Uncategorized')
        if cat not in cats:
            cats[cat] = []
        cats[cat].append(e)
    return dict(sorted(cats.items(), key=lambda x: (x[1][0].get('created_at', 0), x[0])))


def render_categorized(entries, max_per_cat=3):
    out = ['<h2>Categories</h2><ul>']
    grouped = categorize_entries(entries)
    for cat, items in sorted(grouped.items(), key=lambda kv: len(kv[1]), reverse=True)[:10]:
        if not items: continue
        sample = items[:max_per_cat]
        out.append(f'<li><strong>{cat}</strong>: {len(items)}')
        for i, item in enumerate(sample):
            title = item.get('title', 'Untitled')
            out.append(f'<ul class="nested"><li><a href="#{item["id"]}">{title}</a></li>')
        if len(items) > max_per_cat:
            out.append(f'<li>… {len(items)-max_per_cat} more</li>')
        out.append('</ul>')
    out.append('</ul>')
    return '\n'.join(out)
