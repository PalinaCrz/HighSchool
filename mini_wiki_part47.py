# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: MiniWiki
def demo():
    print("=== MiniWiki Demo ===")
    w = Wiki()
    w.add_note("Python is great", tags=["language", "programming"])
    w.add_note("Learn Python in 30 days", tags=["tutorial", "language"])
    w.add_note("MiniWiki v1.0", tags=["project", "milestone"])
    print(f"Notes: {len(w.notes)}")
    print(f"Tags: {sorted(set(tag for n in w.notes for tag in n.tags))}")
    print(f"Search 'Python': {w.search('Python')}")
    print(f"Search 'nonexistent': {w.search('nonexistent')}")
    w.edit("Learn Python in 30 days", "Learn Python in 30 days - Beginner Guide")
    print(f"Revisions for 'Learn Python in 30 days - Beginner Guide': {len(w.revisions('Learn Python in 30 days - Beginner Guide'))}")
    print(f"Revisions for 'Learn Python in 30 days': {len(w.revisions('Learn Python in 30 days'))}")
    w.add_note("Project complete!", tags=["project", "done"])
    print(f"Final notes: {len(w.notes)}")
    print("Demo completed successfully.")
    return w
