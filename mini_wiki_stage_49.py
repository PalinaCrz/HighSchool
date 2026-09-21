# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MiniWiki
import sys
from pathlib import Path

def main():
    from miniwiki import Wiki
    wiki = Wiki(Path(__file__).parent / 'data')
    wiki.seed()
    print("=== MiniWiki: Self-Check ===")
    for title, text in wiki.get_all_notes():
        print(f"  Note: {title}\n    {text[:60]}...")
    print(f"  Total notes: {wiki.count_notes()}")
    print(f"  Tags: {', '.join(wiki.get_tags())}")
    print(f"  History: {wiki.get_history()}")
    print("=== Ready! ===")

if __name__ == '__main__':
    main()
