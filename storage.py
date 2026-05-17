import json
from pathlib import Path

from models import Book


DATA_FILE = Path("books.json")


def load_books(filename: Path = DATA_FILE) -> list[Book]:
    if not filename.exists():
        return []

    try:
        with filename.open("r", encoding="utf-8") as file:
            raw_books = json.load(file)
    except json.JSONDecodeError:
        print("Файл books.json повреждён. Будет использован пустой список.")
        return []

    books: list[Book] = []
    for item in raw_books:
        try:
            books.append(Book.from_dict(item))
        except ValueError:
            continue

    return books


def save_books(books: list[Book], filename: Path = DATA_FILE) -> None:
    with filename.open("w", encoding="utf-8") as file:
        json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)


def is_duplicate(new_book: Book, books: list[Book]) -> bool:
    new_author = new_book.author.lower()
    new_title = new_book.title.lower()

    for book in books:
        if book.author.lower() == new_author and book.title.lower() == new_title:
            return True

    return False


def add_book(book: Book, filename: Path = DATA_FILE) -> bool:
    books = load_books(filename)

    if is_duplicate(book, books):
        return False

    books.append(book)
    save_books(books, filename)
    return True


def delete_book(book_number: int, filename: Path = DATA_FILE) -> bool:
    books = load_books(filename)
    index = book_number - 1

    if index < 0 or index >= len(books):
        return False

    books.pop(index)
    save_books(books, filename)
    return True
