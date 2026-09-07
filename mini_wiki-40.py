# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MiniWiki
import argparse

def main():
    parser = argparse.ArgumentParser(description="MiniWiki CLI")
    parser.add_argument("command", choices=["get", "set", "search", "history", "list"], help="Command to execute")
    parser.add_argument("--key", help="Key for get/set commands")
    parser.add_argument("--value", help="Value for set command")
    parser.add_argument("--tag", help="Tag for set command")
    parser.add_argument("--limit", type=int, default=10, help="Limit for search/history commands")
    args = parser.parse_args()
    
    if args.command == "get":
        if not args.key:
            print("Error: --key is required for get command")
            return
        print(get_note(args.key))
    elif args.command == "set":
        if not args.key or not args.value:
            print("Error: --key and --value are required for set command")
            return
        set_note(args.key, args.value, args.tag)
        print(f"Note '{args.key}' updated successfully")
    elif args.command == "search":
        query = input("Enter search query: ")
        results = search_notes(query)
        print(f"\nSearch results for '{query}':")
        for note in results[:args.limit]:
            print(f"  - {note['key']}: {note['value'][:50]}")
    elif args.command == "history":
        if not args.key:
            print("Error: --key is required for history command")
            return
        history = get_history(args.key)
        print(f"\nHistory for '{args.key}':")
        for entry in history[:args.limit]:
            print(f"  - {entry['timestamp']}: {entry['value'][:50]}")
    elif args.command == "list":
        notes = get_all_notes()
        print("\nAll notes:")
        for note in notes:
            print(f"  - {note['key']}: {note['value'][:50]}")

if __name__ == "__main__":
    main()
