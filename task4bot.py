import sys
from typing import Dict, Callable

GREETING_TEXT = "Hello, how can I help you today?"

CommandMap = Dict[str, Callable[..., None]]


def main():
    phone_book: Dict[str, str] = {}

    commands: CommandMap = {
        "hello": lambda: print(GREETING_TEXT),
        "add": lambda *args: upsert_contact(phone_book, *args),
        "change": lambda *args: upsert_contact(phone_book, *args),
        "show": lambda *args: show_phone(phone_book, *args),
        "all": lambda: show_all(phone_book),
        "close": lambda: handle_exit(),
        "exit": lambda: handle_exit(),
    }

    while True:
        parts = input("Enter your command: ").split()
        if not parts:
            print("Invalid command.")
            continue

        command_name = parts[0].lower()
        arguments = parts[1:]

        handler = commands.get(command_name)
        if handler is None:
            print("Invalid command.")
            continue

        try:
            handler(*arguments)
        except TypeError:
            print("Missing arguments for this command.")
        except (IndexError, ValueError) as e:
            print(f"Invalid arguments: {e}")


def upsert_contact(phone_book: Dict[str, str], name: str, phone_number: str) -> None:
    phone_book[name] = phone_number


def show_phone(phone_book: Dict[str, str], name: str) -> None:
    phone_number = phone_book.get(name)
    if phone_number is not None:
        print(f"{phone_number}")
    else:
        print("Such phone number does not exist.")


def show_all(phone_book: Dict[str, str]) -> None:
    if not phone_book:
        print("No contacts saved.")
        return
    for name, number in phone_book.items():
        print(f"Name: {name}; Number: {number}")


def handle_exit() -> None:
    print("Good bye!")
    sys.exit()


if __name__ == "__main__":
    main()
