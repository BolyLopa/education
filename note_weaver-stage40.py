# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: NoteWeaver
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="NoteWeaver CLI")
    sub = parser.add_subparsers(dest="command")

    p_create = sub.add_parser("create", help="Создать заметку")
    p_create.add_argument("--topic", "-t", help="Тема заметки")
    p_create.add_argument("body", help="Текст заметки")

    p_read = sub.add_parser("read", help="Прочитать заметку")
    p_read.add_argument("id", help="ID заметки")

    p_search = sub.add_parser("search", help="Поиск заметок")
    p_search.add_argument("query", help="Текст запроса")

    p_list = sub.add_parser("list", help="Список заметок")

    p_diary = sub.add_parser("diary", help="Дневник за день")
    p_diary.add_argument("date", help="Дата (YYYY-MM-DD)")

    return parser.parse_args()

def main():
    args = parse_args()
    print(f"NoteWeaver: command={args.command}")
    if args.command == "create":
        print(f"  topic={args.topic}, body={args.body[:50]}...")
    elif args.command == "read":
        print(f"  reading note {args.id}")
    elif args.command == "search":
        print(f"  searching for: {args.query}")
    elif args.command == "list":
        print(f"  listing all notes")
    elif args.command == "diary":
        print(f"  diary for {args.date}")
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
