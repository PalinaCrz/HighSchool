# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MiniWiki
def paginate(items, page_size=10):
    pages = []
    for start in range(0, len(items), page_size):
        pages.append(items[start:start + page_size])
    return pages
