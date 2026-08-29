# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MiniWiki
TEMPLATE_NAMES = {"note": "Note", "idea": "Idea", "todo": "Todo", "decision": "Decision", "meeting": "Meeting"}

def apply_template(template_name, title, content, tags, link, parent, page, user):
    if template_name not in TEMPLATE_NAMES:
        return None
    title = f"{{template}}: {title}"
    template_body = {
        "note": "## Note\n\n{{content}}",
        "idea": "## Idea\n\n{{content}}\n\n### Tags\n{{tags}}",
        "todo": "## TODO\n\n- [ ] {{content}}\n\n### Tags\n{{tags}}",
        "decision": "## Decision\n\n{{content}}\n\n### Tags\n{{tags}}",
        "meeting": "## Meeting {{title}}\n\n{{content}}\n\n### Tags\n{{tags}}",
    }
    body = template_body[template_name].replace("{{content}}", content).replace("{{tags}}", tags).replace("{{title}}", title)
    new_page = Page(title=title, content=body, tags=tags, links=[link], parent=parent, user=user, timestamp=page.timestamp)
    return new_page
